import AnomalyCLIP_lib
import torch
import argparse
import torch.nn.functional as F
from prompt_ensemble import AnomalyCLIP_PromptLearner
from PIL import Image

import os
import random
import numpy as np
from utils import get_transform, normalize

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

# from visualization import visualizer
import cv2


def apply_ad_scoremap(image, scoremap, alpha=0.5):
    np_image = np.asarray(image, dtype=float)
    scoremap = (scoremap * 255).astype(np.uint8)
    scoremap = cv2.applyColorMap(scoremap, cv2.COLORMAP_JET)
    scoremap = cv2.cvtColor(scoremap, cv2.COLOR_BGR2RGB)
    return (alpha * np_image + (1 - alpha) * scoremap).astype(np.uint8)

def visualizer(path, anomaly_map, img_size):
    filename = os.path.basename(path)
    dirname = os.path.dirname(path)
    vis = cv2.cvtColor(cv2.resize(cv2.imread(path), (img_size, img_size)), cv2.COLOR_BGR2RGB)  # RGB
    mask = normalize(anomaly_map[0])
    vis = apply_ad_scoremap(vis, mask)
    vis = cv2.cvtColor(vis, cv2.COLOR_RGB2BGR)  # BGR
    save_vis = os.path.join(dirname, f'anomaly_map_{filename}')
    print(save_vis)
    cv2.imwrite(save_vis, vis)

from scipy.ndimage import gaussian_filter
def test(args):
    img_size = args.image_size
    features_list = args.features_list
    image_path = args.image_path

    device = "cuda" if torch.cuda.is_available() else "cpu"

    AnomalyCLIP_parameters = {"Prompt_length": args.n_ctx, "learnabel_text_embedding_depth": args.depth, "learnabel_text_embedding_length": args.t_n_ctx}
    
    model, _ = AnomalyCLIP_lib.load("ViT-L/14@336px", device=device, design_details = AnomalyCLIP_parameters)
    model.eval()

    preprocess, target_transform = get_transform(args)


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

    img = Image.open(image_path)
    img = preprocess(img)
    
    print("img", img.shape)
    image = img.reshape(1, 3, img_size, img_size).to(device)
   
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
                    if args.patch_score_space == "energy":
                        anomaly_map = AnomalyCLIP_lib.get_similarity_map(
                            energy[:, 1:].unsqueeze(-1),
                            args.image_size,
                        )[..., 0]
                        anomaly_map_list.append(anomaly_map)
                        parent_patch_feature = patch_feature_raw
                        continue
                else:
                    patch_feature = patch_feature/ patch_feature.norm(dim = -1, keepdim = True)
                    similarity, _ = AnomalyCLIP_lib.compute_similarity(patch_feature, text_features[0])
                similarity_map = AnomalyCLIP_lib.get_similarity_map(similarity[:, 1:, :], args.image_size)
                anomaly_map = (similarity_map[...,1] + 1 - similarity_map[...,0])/2.0
                anomaly_map_list.append(anomaly_map)
                parent_patch_feature = patch_feature_raw

        anomaly_map = torch.stack(anomaly_map_list)
        
        anomaly_map = anomaly_map.sum(dim = 0)
      
        anomaly_map = torch.stack([torch.from_numpy(gaussian_filter(i, sigma = args.sigma)) for i in anomaly_map.detach().cpu()], dim = 0 )

        visualizer(image_path, anomaly_map.detach().cpu().numpy(), args.image_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("AnomalyCLIP", add_help=True)
    # paths
    parser.add_argument("--image_path", type=str, default="./data/visa", help="path to test dataset")
    parser.add_argument("--checkpoint_path", type=str, default='./checkpoint/', help='path to checkpoint')
    # model
    parser.add_argument("--features_list", type=int, nargs="+", default=[6, 12, 18, 24], help="features used")
    parser.add_argument("--image_size", type=int, default=518, help="image size")
    parser.add_argument("--depth", type=int, default=9, help="image size")
    parser.add_argument("--n_ctx", type=int, default=12, help="zero shot")
    parser.add_argument("--t_n_ctx", type=int, default=4, help="zero shot")
    parser.add_argument("--feature_map_layer", type=int,  nargs="+", default=[0, 1, 2, 3], help="zero shot")
    parser.add_argument("--score_mode", type=str, default="normality_entailment", choices=["normality_entailment", "cosine"], help="anomaly scoring mechanism")
    parser.add_argument("--patch_score_space", type=str, default="prob", choices=["prob", "energy"], help="normality patch map scoring space")
    parser.add_argument("--hyperbolic_curvature", type=float, default=1.0, help="Poincare ball curvature")
    parser.add_argument("--hyperbolic_temperature", type=float, default=1.0, help="normality entailment logit temperature")
    parser.add_argument("--hyperbolic_radius_scale", type=float, default=0.1, help="scale used to preserve raw feature norm before the exponential map")
    parser.add_argument("--cone_aperture", type=float, default=0.1, help="minimum aperture constant for normality cones")
    parser.add_argument("--entailment_margin", type=float, default=0.2, help="energy margin separating normal and anomaly logits")
    parser.add_argument("--entailment_mode", type=str, default="normal_only", choices=["normal_only", "contrastive"], help="normal-only or normal-vs-anomaly hyperbolic entailment")
    parser.add_argument("--context_weight", type=float, default=0.5, help="weight for global-context cone violation")
    parser.add_argument("--radial_weight", type=float, default=0.25, help="weight for radial severity excess")
    parser.add_argument("--order_weight", type=float, default=0.5, help="weight for multi-scale parent-child order rupture")
    parser.add_argument("--seed", type=int, default=111, help="random seed")
    parser.add_argument("--sigma", type=int, default=4, help="zero shot")
    
    args = parser.parse_args()
    print(args)
    setup_seed(args.seed)
    test(args)
