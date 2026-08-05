import AnomalyCLIP_lib
import torch
import argparse
import torch.nn.functional as F
from prompt_ensemble import AnomalyCLIP_PromptLearner
from loss import FocalLoss, BinaryDiceLoss
from utils import normalize
from dataset import Dataset
from logger import get_logger
from tqdm import tqdm

import os
import random
import numpy as np
from tabulate import tabulate
from utils import get_transform

def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def normality_kwargs(args):
    return {
        "curvature": args.hyperbolic_curvature,
        "temperature": args.hyperbolic_temperature,
        "radius_scale": args.hyperbolic_radius_scale,
        "cone_aperture": args.cone_aperture,
        "context_weight": args.context_weight,
        "radial_weight": args.radial_weight,
        "order_weight": args.order_weight,
        "margin": args.entailment_margin,
        "entailment_mode": args.entailment_mode,
    }


def apply_class_filter(dataset, class_filter):
    if not class_filter:
        return dataset.obj_list

    selected = set(class_filter)
    dataset.data_all = [item for item in dataset.data_all if item["cls_name"] in selected]
    dataset.length = len(dataset.data_all)
    dataset.cls_names = [name for name in dataset.cls_names if name in selected]
    dataset.obj_list = [name for name in dataset.obj_list if name in selected]
    if dataset.length == 0:
        raise ValueError(f"class_filter has no matching samples: {sorted(selected)}")
    return dataset.obj_list

from visualization import visualizer

from metrics import image_level_metrics, pixel_level_metrics
from tqdm import tqdm
from scipy.ndimage import gaussian_filter
def test(args):
    img_size = args.image_size
    features_list = args.features_list
    dataset_dir = args.data_path
    save_path = args.save_path
    dataset_name = args.dataset

    logger = get_logger(args.save_path)
    device = "cuda" if torch.cuda.is_available() else "cpu"

    AnomalyCLIP_parameters = {"Prompt_length": args.n_ctx, "learnabel_text_embedding_depth": args.depth, "learnabel_text_embedding_length": args.t_n_ctx}
    
    model, _ = AnomalyCLIP_lib.load("ViT-L/14@336px", device=device, design_details = AnomalyCLIP_parameters)
    model.eval()

    preprocess, target_transform = get_transform(args)
    test_data = Dataset(root=args.data_path, transform=preprocess, target_transform=target_transform, dataset_name = args.dataset)
    obj_list = apply_class_filter(test_data, args.class_filter)
    test_dataloader = torch.utils.data.DataLoader(test_data, batch_size=1, shuffle=False)


    results = {}
    metrics = {}
    for obj in obj_list:
        results[obj] = {}
        results[obj]['gt_sp'] = []
        results[obj]['pr_sp'] = []
        results[obj]['imgs_masks'] = []
        results[obj]['anomaly_maps'] = []
        metrics[obj] = {}
        metrics[obj]['pixel-auroc'] = 0
        metrics[obj]['pixel-aupro'] = 0
        metrics[obj]['image-auroc'] = 0
        metrics[obj]['image-ap'] = 0

    prompt_learner = AnomalyCLIP_PromptLearner(model.to("cpu"), AnomalyCLIP_parameters)
    checkpoint = torch.load(args.checkpoint_path, map_location=device)
    prompt_learner.load_state_dict(checkpoint["prompt_learner"])
    prompt_learner.to(device)
    model.to(device)
    model.visual.DAPM_replace(DPAM_layer = 20)

    prompts, tokenized_prompts, compound_prompts_text = prompt_learner(cls_id = None)
    text_features_raw = model.encode_text_learn(prompts, tokenized_prompts, compound_prompts_text).float()
    text_features_raw = torch.stack(torch.chunk(text_features_raw, dim = 0, chunks = 2), dim = 1)
    text_features = text_features_raw
    text_features = text_features/text_features.norm(dim=-1, keepdim=True)


    model.to(device)
    for idx, items in enumerate(tqdm(test_dataloader)):
        image = items['img'].to(device)
        cls_name = items['cls_name']
        cls_id = items['cls_id']
        gt_mask = items['img_mask']
        gt_mask[gt_mask > 0.5], gt_mask[gt_mask <= 0.5] = 1, 0
        results[cls_name[0]]['imgs_masks'].append(gt_mask)  # px
        results[cls_name[0]]['gt_sp'].extend(items['anomaly'].detach().cpu())

        with torch.no_grad():
            image_features_raw, patch_features = model.encode_image(image, features_list, DPAM_layer = 20)
            image_features = image_features_raw / image_features_raw.norm(dim=-1, keepdim=True)

            if args.score_mode == "normality_entailment":
                image_logits, _ = AnomalyCLIP_lib.compute_normality_image_logits(
                    image_features_raw.float(),
                    text_features_raw[0],
                    **normality_kwargs(args),
                )
                text_probs = image_logits.softmax(dim=-1)[:, 1]
            elif args.score_mode == "euclidean_energy":
                image_logits, _ = AnomalyCLIP_lib.compute_euclidean_image_logits(
                    image_features_raw.float(),
                    text_features_raw[0],
                    temperature=args.hyperbolic_temperature,
                    margin=args.entailment_margin,
                    entailment_mode=args.entailment_mode,
                )
                text_probs = image_logits.softmax(dim=-1)[:, 1]
            elif args.score_mode == "hyperbolic_distance":
                image_logits, _ = AnomalyCLIP_lib.compute_hyperbolic_distance_image_logits(
                    image_features_raw.float(),
                    text_features_raw[0],
                    curvature=args.hyperbolic_curvature,
                    temperature=args.hyperbolic_temperature,
                    radius_scale=args.hyperbolic_radius_scale,
                    margin=args.entailment_margin,
                    entailment_mode=args.entailment_mode,
                )
                text_probs = image_logits.softmax(dim=-1)[:, 1]
            else:
                text_probs = image_features @ text_features.permute(0, 2, 1)
                text_probs = (text_probs/0.07).softmax(-1)
                text_probs = text_probs[:, 0, 1]
            anomaly_map_list = []
            parent_patch_feature = None
            for idx, patch_feature in enumerate(patch_features):
                if idx >= args.feature_map_layer[0]:
                    patch_feature_raw = patch_feature.float()
                    if args.score_mode == "normality_entailment":
                        similarity, energy, _ = AnomalyCLIP_lib.compute_normality_entailment(
                            patch_feature_raw,
                            text_features_raw[0],
                            image_features=image_features_raw.float(),
                            parent_patch_features=parent_patch_feature,
                            **normality_kwargs(args),
                        )
                    elif args.score_mode == "euclidean_energy":
                        similarity, energy = AnomalyCLIP_lib.compute_euclidean_energy(
                            patch_feature_raw,
                            text_features_raw[0],
                            temperature=args.hyperbolic_temperature,
                            margin=args.entailment_margin,
                            entailment_mode=args.entailment_mode,
                        )
                    elif args.score_mode == "hyperbolic_distance":
                        similarity, energy = AnomalyCLIP_lib.compute_hyperbolic_distance(
                            patch_feature_raw,
                            text_features_raw[0],
                            curvature=args.hyperbolic_curvature,
                            temperature=args.hyperbolic_temperature,
                            radius_scale=args.hyperbolic_radius_scale,
                            margin=args.entailment_margin,
                            entailment_mode=args.entailment_mode,
                        )
                    if args.score_mode != "cosine":
                        if args.patch_score_space == "energy":
                            anomaly_map = AnomalyCLIP_lib.get_similarity_map(
                                energy[:, 1:].unsqueeze(-1),
                                args.image_size,
                            )[..., 0]
                            anomaly_map_list.append(anomaly_map)
                            parent_patch_feature = patch_feature_raw
                            continue
                    if args.score_mode == "cosine":
                        patch_feature = patch_feature/ patch_feature.norm(dim = -1, keepdim = True)
                        similarity, _ = AnomalyCLIP_lib.compute_similarity(patch_feature, text_features[0])
                    similarity_map = AnomalyCLIP_lib.get_similarity_map(similarity[:, 1:, :], args.image_size)
                    anomaly_map = (similarity_map[...,1] + 1 - similarity_map[...,0])/2.0
                    # The following code is equivalent. 
                    # anomaly_map = similarity_map[...,1] 
                    anomaly_map_list.append(anomaly_map)
                    parent_patch_feature = patch_feature_raw

            anomaly_map = torch.stack(anomaly_map_list)
            
            anomaly_map = anomaly_map.sum(dim = 0)
            results[cls_name[0]]['pr_sp'].extend(text_probs.detach().cpu())
            anomaly_map = torch.stack([torch.from_numpy(gaussian_filter(i, sigma = args.sigma)) for i in anomaly_map.detach().cpu()], dim = 0 )
            results[cls_name[0]]['anomaly_maps'].append(anomaly_map)
            # visualizer(items['img_path'], anomaly_map.detach().cpu().numpy(), args.image_size, args.save_path, cls_name)

    table_ls = []
    image_auroc_list = []
    image_ap_list = []
    pixel_auroc_list = []
    pixel_aupro_list = []
    for obj in obj_list:
        table = []
        table.append(obj)
        results[obj]['imgs_masks'] = torch.cat(results[obj]['imgs_masks'])
        results[obj]['anomaly_maps'] = torch.cat(results[obj]['anomaly_maps']).detach().cpu().numpy()
        if args.metrics == 'image-level':
            image_auroc = image_level_metrics(results, obj, "image-auroc")
            image_ap = image_level_metrics(results, obj, "image-ap")
            table.append(str(np.round(image_auroc * 100, decimals=1)))
            table.append(str(np.round(image_ap * 100, decimals=1)))
            image_auroc_list.append(image_auroc)
            image_ap_list.append(image_ap) 
        elif args.metrics == 'pixel-level':
            pixel_auroc = pixel_level_metrics(results, obj, "pixel-auroc")
            pixel_aupro = pixel_level_metrics(results, obj, "pixel-aupro")
            table.append(str(np.round(pixel_auroc * 100, decimals=1)))
            table.append(str(np.round(pixel_aupro * 100, decimals=1)))
            pixel_auroc_list.append(pixel_auroc)
            pixel_aupro_list.append(pixel_aupro)
        elif args.metrics == 'image-pixel-level':
            image_auroc = image_level_metrics(results, obj, "image-auroc")
            image_ap = image_level_metrics(results, obj, "image-ap")
            pixel_auroc = pixel_level_metrics(results, obj, "pixel-auroc")
            pixel_aupro = pixel_level_metrics(results, obj, "pixel-aupro")
            table.append(str(np.round(pixel_auroc * 100, decimals=1)))
            table.append(str(np.round(pixel_aupro * 100, decimals=1)))
            table.append(str(np.round(image_auroc * 100, decimals=1)))
            table.append(str(np.round(image_ap * 100, decimals=1)))
            image_auroc_list.append(image_auroc)
            image_ap_list.append(image_ap) 
            pixel_auroc_list.append(pixel_auroc)
            pixel_aupro_list.append(pixel_aupro)
        table_ls.append(table)

    if args.metrics == 'image-level':
        # logger
        table_ls.append(['mean', 
                        str(np.round(np.mean(image_auroc_list) * 100, decimals=1)),
                        str(np.round(np.mean(image_ap_list) * 100, decimals=1))])
        results = tabulate(table_ls, headers=['objects', 'image_auroc', 'image_ap'], tablefmt="pipe")
    elif args.metrics == 'pixel-level':
        # logger
        table_ls.append(['mean', str(np.round(np.mean(pixel_auroc_list) * 100, decimals=1)),
                        str(np.round(np.mean(pixel_aupro_list) * 100, decimals=1))
                       ])
        results = tabulate(table_ls, headers=['objects', 'pixel_auroc', 'pixel_aupro'], tablefmt="pipe")
    elif args.metrics == 'image-pixel-level':
        # logger
        table_ls.append(['mean', str(np.round(np.mean(pixel_auroc_list) * 100, decimals=1)),
                        str(np.round(np.mean(pixel_aupro_list) * 100, decimals=1)), 
                        str(np.round(np.mean(image_auroc_list) * 100, decimals=1)),
                        str(np.round(np.mean(image_ap_list) * 100, decimals=1))])
        results = tabulate(table_ls, headers=['objects', 'pixel_auroc', 'pixel_aupro', 'image_auroc', 'image_ap'], tablefmt="pipe")
    logger.info("\n%s", results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("AnomalyCLIP", add_help=True)
    # paths
    parser.add_argument("--data_path", type=str, default="./data/visa", help="path to test dataset")
    parser.add_argument("--save_path", type=str, default='./results/', help='path to save results')
    parser.add_argument("--checkpoint_path", type=str, default='./checkpoint/', help='path to checkpoint')
    # model
    parser.add_argument("--dataset", type=str, default='mvtec')
    parser.add_argument("--features_list", type=int, nargs="+", default=[6, 12, 18, 24], help="features used")
    parser.add_argument("--image_size", type=int, default=518, help="image size")
    parser.add_argument("--depth", type=int, default=9, help="image size")
    parser.add_argument("--n_ctx", type=int, default=12, help="zero shot")
    parser.add_argument("--t_n_ctx", type=int, default=4, help="zero shot")
    parser.add_argument("--feature_map_layer", type=int,  nargs="+", default=[0, 1, 2, 3], help="zero shot")
    parser.add_argument("--class_filter", type=str, nargs="+", default=None, help="optional class names to evaluate")
    parser.add_argument("--metrics", type=str, default='image-pixel-level')
    parser.add_argument("--score_mode", type=str, default="normality_entailment", choices=["normality_entailment", "euclidean_energy", "hyperbolic_distance", "cosine"], help="anomaly scoring mechanism")
    parser.add_argument("--patch_score_space", type=str, default="prob", choices=["prob", "energy"], help="normality patch map scoring space")
    parser.add_argument("--hyperbolic_curvature", type=float, default=1.0, help="Poincare ball curvature")
    parser.add_argument("--hyperbolic_temperature", type=float, default=1.0, help="normality entailment logit temperature")
    parser.add_argument("--hyperbolic_radius_scale", type=float, default=0.1, help="scale used to preserve raw feature norm before the exponential map")
    parser.add_argument("--cone_aperture", type=float, default=0.1, help="minimum aperture constant for normality cones")
    parser.add_argument("--entailment_margin", type=float, default=0.2, help="energy margin separating normal and anomaly logits")
    parser.add_argument("--entailment_mode", type=str, default="normal_only", choices=["normal_only", "anomaly_only", "contrastive"], help="normal-only, anomaly-only, or normal-vs-anomaly scoring")
    parser.add_argument("--context_weight", type=float, default=0.5, help="weight for global-context cone violation")
    parser.add_argument("--radial_weight", type=float, default=0.25, help="weight for radial severity excess")
    parser.add_argument("--order_weight", type=float, default=0.5, help="weight for multi-scale parent-child order rupture")
    parser.add_argument("--seed", type=int, default=111, help="random seed")
    parser.add_argument("--sigma", type=int, default=4, help="zero shot")
    
    args = parser.parse_args()
    print(args)
    setup_seed(args.seed)
    test(args)
