from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter
from sklearn.metrics import roc_auc_score

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import AnomalyCLIP_lib
from dataset import Dataset
from prompt_ensemble import AnomalyCLIP_PromptLearner
from utils import get_transform


VARIANT_CONFIGS: dict[str, dict[str, Any]] = {
    "cosine": {
        "score_mode": "cosine",
        "entailment_mode": "contrastive",
    },
    "euclidean_contrastive": {
        "score_mode": "euclidean_energy",
        "entailment_mode": "contrastive",
        "patch_score_space": "prob",
    },
    "hyperbolic_distance_contrastive": {
        "score_mode": "hyperbolic_distance",
        "entailment_mode": "contrastive",
        "patch_score_space": "prob",
    },
    "cone_normal_only": {
        "score_mode": "normality_entailment",
        "entailment_mode": "normal_only",
        "context_weight": 0.0,
        "order_weight": 0.0,
        "patch_score_space": "prob",
    },
    "cone_anomaly_only": {
        "score_mode": "normality_entailment",
        "entailment_mode": "anomaly_only",
        "context_weight": 0.0,
        "order_weight": 0.0,
        "patch_score_space": "prob",
    },
    "cone_contrastive": {
        "score_mode": "normality_entailment",
        "entailment_mode": "contrastive",
        "context_weight": 0.0,
        "order_weight": 0.0,
        "patch_score_space": "prob",
    },
    "bot_cosine": {
        "score_mode": "hyperbolic_uot",
        "ot_mode": "balanced",
        "ot_cost": "cosine",
        "ot_score": "cost",
        "patch_score_space": "prob",
    },
    "bot_hyperbolic_cone": {
        "score_mode": "hyperbolic_uot",
        "ot_mode": "balanced",
        "ot_cost": "hyperbolic_cone",
        "ot_score": "cost",
        "patch_score_space": "prob",
    },
    "pot_hyperbolic_cone": {
        "score_mode": "hyperbolic_uot",
        "ot_mode": "partial",
        "ot_cost": "hyperbolic_cone",
        "ot_score": "combined",
        "patch_score_space": "prob",
    },
    "uot_cosine": {
        "score_mode": "hyperbolic_uot",
        "ot_mode": "unbalanced",
        "ot_cost": "cosine",
        "ot_score": "combined",
        "patch_score_space": "prob",
    },
    "uot_euclidean": {
        "score_mode": "hyperbolic_uot",
        "ot_mode": "unbalanced",
        "ot_cost": "euclidean",
        "ot_score": "combined",
        "patch_score_space": "prob",
    },
    "uot_hyperbolic_distance": {
        "score_mode": "hyperbolic_uot",
        "ot_mode": "unbalanced",
        "ot_cost": "hyperbolic_distance",
        "ot_score": "combined",
        "patch_score_space": "prob",
    },
    "uot_hyperbolic_cone": {
        "score_mode": "hyperbolic_uot",
        "ot_mode": "unbalanced",
        "ot_cost": "hyperbolic_cone",
        "ot_score": "combined",
        "patch_score_space": "prob",
    },
}


@dataclass
class InferenceContext:
    model: Any
    text_features_raw: torch.Tensor
    text_features: torch.Tensor
    preprocess: Any
    target_transform: Any
    device: str


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--dataset", type=str, default="mvtec")
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument("--checkpoint_path", type=str, required=True)
    parser.add_argument("--save_path", type=str, required=True)
    parser.add_argument("--features_list", type=int, nargs="+", default=[24])
    parser.add_argument("--feature_map_layer", type=int, nargs="+", default=[0])
    parser.add_argument("--image_size", type=int, default=518)
    parser.add_argument("--depth", type=int, default=9)
    parser.add_argument("--n_ctx", type=int, default=12)
    parser.add_argument("--t_n_ctx", type=int, default=4)
    parser.add_argument("--hyperbolic_curvature", type=float, default=1.0)
    parser.add_argument("--hyperbolic_temperature", type=float, default=1.0)
    parser.add_argument("--hyperbolic_radius_scale", type=float, default=0.1)
    parser.add_argument("--cone_aperture", type=float, default=0.1)
    parser.add_argument("--entailment_margin", type=float, default=0.2)
    parser.add_argument("--context_weight", type=float, default=0.0)
    parser.add_argument("--radial_weight", type=float, default=0.25)
    parser.add_argument("--order_weight", type=float, default=0.0)
    parser.add_argument("--patch_score_space", type=str, default="prob", choices=["prob", "energy"])
    parser.add_argument("--ot_mode", type=str, default="unbalanced", choices=["balanced", "partial", "unbalanced"])
    parser.add_argument("--ot_cost", type=str, default="hyperbolic_cone", choices=["cosine", "euclidean", "hyperbolic_distance", "hyperbolic_cone"])
    parser.add_argument("--ot_anchor_mode", type=str, default="normal", choices=["normal", "anomaly", "both", "normal_anomaly"])
    parser.add_argument("--ot_epsilon", type=float, default=0.05)
    parser.add_argument("--ot_tau_patch", type=float, default=0.5)
    parser.add_argument("--ot_tau_anchor", type=float, default=0.5)
    parser.add_argument("--ot_partial_mass", type=float, default=0.9)
    parser.add_argument("--ot_iterations", type=int, default=50)
    parser.add_argument("--ot_score", type=str, default="combined", choices=["unmatched", "cost", "combined"])
    parser.add_argument("--ot_alpha", type=float, default=1.0)
    parser.add_argument("--ot_beta", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=111)
    parser.add_argument("--sigma", type=float, default=4.0)
    parser.add_argument("--class_filter", type=str, nargs="+", default=None)
    parser.add_argument("--variants", type=str, nargs="+", default=["cosine", "cone_normal_only", "cone_contrastive"])


def setup_seed(seed: int) -> None:
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def ensure_dir(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def validate_variants(variants: list[str]) -> None:
    unknown = sorted(set(variants) - set(VARIANT_CONFIGS))
    if unknown:
        raise ValueError(f"Unknown variants: {unknown}. Available: {sorted(VARIANT_CONFIGS)}")


def variant_config(args: argparse.Namespace, variant: str) -> dict[str, Any]:
    cfg = {
        "score_mode": "normality_entailment",
        "entailment_mode": "contrastive",
        "patch_score_space": args.patch_score_space,
        "context_weight": args.context_weight,
        "order_weight": args.order_weight,
    }
    cfg.update(VARIANT_CONFIGS[variant])
    return cfg


def normality_kwargs(args: argparse.Namespace, cfg: dict[str, Any]) -> dict[str, Any]:
    return {
        "curvature": args.hyperbolic_curvature,
        "temperature": args.hyperbolic_temperature,
        "radius_scale": args.hyperbolic_radius_scale,
        "cone_aperture": args.cone_aperture,
        "context_weight": cfg.get("context_weight", args.context_weight),
        "radial_weight": args.radial_weight,
        "order_weight": cfg.get("order_weight", args.order_weight),
        "margin": args.entailment_margin,
        "entailment_mode": cfg["entailment_mode"],
    }


def transport_kwargs(args: argparse.Namespace, cfg: dict[str, Any]) -> dict[str, Any]:
    return {
        "ot_mode": cfg.get("ot_mode", args.ot_mode),
        "ot_cost": cfg.get("ot_cost", args.ot_cost),
        "ot_anchor_mode": cfg.get("ot_anchor_mode", args.ot_anchor_mode),
        "ot_epsilon": cfg.get("ot_epsilon", args.ot_epsilon),
        "ot_tau_patch": cfg.get("ot_tau_patch", args.ot_tau_patch),
        "ot_tau_anchor": cfg.get("ot_tau_anchor", args.ot_tau_anchor),
        "ot_partial_mass": cfg.get("ot_partial_mass", args.ot_partial_mass),
        "ot_iterations": cfg.get("ot_iterations", args.ot_iterations),
        "ot_score": cfg.get("ot_score", args.ot_score),
        "ot_alpha": cfg.get("ot_alpha", args.ot_alpha),
        "ot_beta": cfg.get("ot_beta", args.ot_beta),
        "curvature": args.hyperbolic_curvature,
        "temperature": args.hyperbolic_temperature,
        "radius_scale": args.hyperbolic_radius_scale,
        "cone_aperture": args.cone_aperture,
        "margin": args.entailment_margin,
    }


def apply_class_filter(dataset: Dataset, class_filter: list[str] | None) -> list[str]:
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


def build_dataset(args: argparse.Namespace) -> tuple[Dataset, list[str]]:
    preprocess, target_transform = get_transform(args)
    dataset = Dataset(
        root=args.data_path,
        transform=preprocess,
        target_transform=target_transform,
        dataset_name=args.dataset,
    )
    obj_list = apply_class_filter(dataset, args.class_filter)
    return dataset, obj_list


def build_inference_context(args: argparse.Namespace) -> InferenceContext:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    params = {
        "Prompt_length": args.n_ctx,
        "learnabel_text_embedding_depth": args.depth,
        "learnabel_text_embedding_length": args.t_n_ctx,
    }
    model, _ = AnomalyCLIP_lib.load("ViT-L/14@336px", device=device, design_details=params)
    model.eval()

    preprocess, target_transform = get_transform(args)
    prompt_learner = AnomalyCLIP_PromptLearner(model.to("cpu"), params)
    checkpoint = torch.load(args.checkpoint_path, map_location=device)
    prompt_learner.load_state_dict(checkpoint["prompt_learner"])
    prompt_learner.to(device)
    model.to(device)
    model.visual.DAPM_replace(DPAM_layer=20)

    prompts, tokenized_prompts, compound_prompts_text = prompt_learner(cls_id=None)
    text_features_raw = model.encode_text_learn(prompts, tokenized_prompts, compound_prompts_text).float()
    text_features_raw = torch.stack(torch.chunk(text_features_raw, dim=0, chunks=2), dim=1)
    text_features = text_features_raw / text_features_raw.norm(dim=-1, keepdim=True)

    return InferenceContext(
        model=model,
        text_features_raw=text_features_raw,
        text_features=text_features,
        preprocess=preprocess,
        target_transform=target_transform,
        device=device,
    )


def tensor_from_pil(ctx: InferenceContext, image: Image.Image, args: argparse.Namespace) -> torch.Tensor:
    rgb = image.convert("RGB")
    tensor = ctx.preprocess(rgb).reshape(1, 3, args.image_size, args.image_size)
    return tensor.to(ctx.device)


def mask_from_pil(ctx: InferenceContext, mask: Image.Image | None, args: argparse.Namespace) -> np.ndarray:
    if mask is None:
        return np.zeros((args.image_size, args.image_size), dtype=np.uint8)
    mask_tensor = ctx.target_transform(mask.convert("L"))
    mask_np = mask_tensor.squeeze(0).detach().cpu().numpy()
    return (mask_np > 0.5).astype(np.uint8)


def extract_features(
    ctx: InferenceContext,
    image_tensor: torch.Tensor,
    args: argparse.Namespace,
) -> tuple[torch.Tensor, torch.Tensor, list[torch.Tensor]]:
    with torch.no_grad():
        image_features_raw, patch_features = ctx.model.encode_image(
            image_tensor,
            args.features_list,
            DPAM_layer=20,
        )
    image_features = image_features_raw / image_features_raw.norm(dim=-1, keepdim=True)
    return image_features_raw.float(), image_features.float(), patch_features


def _map_from_patch_values(values: torch.Tensor, image_size: int) -> torch.Tensor:
    return AnomalyCLIP_lib.get_similarity_map(values[:, 1:].unsqueeze(-1), image_size)[..., 0]


def score_extracted_features(
    ctx: InferenceContext,
    args: argparse.Namespace,
    image_features_raw: torch.Tensor,
    image_features: torch.Tensor,
    patch_features: list[torch.Tensor],
    variant: str,
    return_components: bool = False,
) -> dict[str, Any]:
    cfg = variant_config(args, variant)
    score_mode = cfg["score_mode"]
    text_features_raw = ctx.text_features_raw[0]
    text_features = ctx.text_features[0]

    with torch.no_grad():
        if score_mode == "normality_entailment":
            image_logits, _ = AnomalyCLIP_lib.compute_normality_image_logits(
                image_features_raw,
                text_features_raw,
                **normality_kwargs(args, cfg),
            )
            image_score = image_logits.softmax(dim=-1)[:, 1]
        elif score_mode == "euclidean_energy":
            image_logits, _ = AnomalyCLIP_lib.compute_euclidean_image_logits(
                image_features_raw,
                text_features_raw,
                temperature=args.hyperbolic_temperature,
                margin=args.entailment_margin,
                entailment_mode=cfg["entailment_mode"],
            )
            image_score = image_logits.softmax(dim=-1)[:, 1]
        elif score_mode == "hyperbolic_distance":
            image_logits, _ = AnomalyCLIP_lib.compute_hyperbolic_distance_image_logits(
                image_features_raw,
                text_features_raw,
                curvature=args.hyperbolic_curvature,
                temperature=args.hyperbolic_temperature,
                radius_scale=args.hyperbolic_radius_scale,
                margin=args.entailment_margin,
                entailment_mode=cfg["entailment_mode"],
            )
            image_score = image_logits.softmax(dim=-1)[:, 1]
        elif score_mode == "hyperbolic_uot":
            image_score = None
        elif score_mode == "cosine":
            text_probs = image_features @ ctx.text_features.permute(0, 2, 1)
            text_probs = (text_probs / 0.07).softmax(-1)
            image_score = text_probs[:, 0, 1]
        else:
            raise ValueError(f"Unknown score_mode: {score_mode}")

        anomaly_map_list: list[torch.Tensor] = []
        component_map_lists: dict[str, list[torch.Tensor]] = {}
        parent_patch_feature = None
        min_layer = args.feature_map_layer[0] if args.feature_map_layer else 0

        for layer_idx, patch_feature in enumerate(patch_features):
            if layer_idx < min_layer:
                parent_patch_feature = patch_feature.float()
                continue

            patch_feature_raw = patch_feature.float()
            components: dict[str, torch.Tensor] = {}
            if score_mode == "normality_entailment":
                similarity, score_energy, components = AnomalyCLIP_lib.compute_normality_entailment(
                    patch_feature_raw,
                    text_features_raw,
                    image_features=image_features_raw,
                    parent_patch_features=parent_patch_feature,
                    **normality_kwargs(args, cfg),
                )
            elif score_mode == "euclidean_energy":
                similarity, score_energy = AnomalyCLIP_lib.compute_euclidean_energy(
                    patch_feature_raw,
                    text_features_raw,
                    temperature=args.hyperbolic_temperature,
                    margin=args.entailment_margin,
                    entailment_mode=cfg["entailment_mode"],
                )
            elif score_mode == "hyperbolic_distance":
                similarity, score_energy = AnomalyCLIP_lib.compute_hyperbolic_distance(
                    patch_feature_raw,
                    text_features_raw,
                    curvature=args.hyperbolic_curvature,
                    temperature=args.hyperbolic_temperature,
                    radius_scale=args.hyperbolic_radius_scale,
                    margin=args.entailment_margin,
                    entailment_mode=cfg["entailment_mode"],
                )
            elif score_mode == "hyperbolic_uot":
                similarity, score_energy, components = AnomalyCLIP_lib.compute_transport_anomaly(
                    patch_feature_raw,
                    text_features_raw,
                    **transport_kwargs(args, cfg),
                )
            else:
                patch_feature_norm = patch_feature / patch_feature.norm(dim=-1, keepdim=True)
                similarity, _ = AnomalyCLIP_lib.compute_similarity(patch_feature_norm, text_features)
                score_energy = None

            if score_mode != "cosine" and cfg.get("patch_score_space", args.patch_score_space) == "energy":
                anomaly_map = _map_from_patch_values(score_energy, args.image_size)
            else:
                similarity_map = AnomalyCLIP_lib.get_similarity_map(similarity[:, 1:, :], args.image_size)
                anomaly_map = (similarity_map[..., 1] + 1 - similarity_map[..., 0]) / 2.0
            anomaly_map_list.append(anomaly_map)

            if return_components and components:
                for name, value in components.items():
                    component_map_lists.setdefault(name, []).append(_map_from_patch_values(value, args.image_size))
                if score_energy is not None:
                    component_map_lists.setdefault("score_energy", []).append(
                        _map_from_patch_values(score_energy, args.image_size)
                    )

            parent_patch_feature = patch_feature_raw

        if not anomaly_map_list:
            raise ValueError("No patch feature layers were selected for scoring.")

        anomaly_map = torch.stack(anomaly_map_list).sum(dim=0)[0].detach().cpu().numpy()
        if args.sigma and args.sigma > 0:
            anomaly_map = gaussian_filter(anomaly_map, sigma=args.sigma)
        if image_score is None:
            image_score_value = float(np.max(anomaly_map))
        else:
            image_score_value = float(image_score.detach().cpu().item())

        component_maps: dict[str, np.ndarray] = {}
        for name, maps in component_map_lists.items():
            component_map = torch.stack(maps).sum(dim=0)[0].detach().cpu().numpy()
            if args.sigma and args.sigma > 0:
                component_map = gaussian_filter(component_map, sigma=args.sigma)
            component_maps[name] = component_map

    return {
        "variant": variant,
        "image_score": image_score_value,
        "anomaly_map": anomaly_map.astype(np.float32),
        "component_maps": component_maps,
    }


def run_variants_on_tensor(
    ctx: InferenceContext,
    args: argparse.Namespace,
    image_tensor: torch.Tensor,
    variants: list[str],
    return_components: bool = False,
) -> dict[str, dict[str, Any]]:
    image_features_raw, image_features, patch_features = extract_features(ctx, image_tensor, args)
    return {
        variant: score_extracted_features(
            ctx,
            args,
            image_features_raw,
            image_features,
            patch_features,
            variant,
            return_components=return_components,
        )
        for variant in variants
    }


def load_meta_samples(
    data_path: str | Path,
    mode: str = "test",
    class_filter: list[str] | None = None,
    normal_only: bool | None = None,
    max_per_class: int | None = None,
    seed: int = 111,
) -> list[dict[str, Any]]:
    data_path = Path(data_path)
    with (data_path / "meta.json").open("r") as f:
        meta = json.load(f)[mode]

    selected = set(class_filter or [])
    samples: list[dict[str, Any]] = []
    rng = random.Random(seed)
    for cls_name, records in meta.items():
        if selected and cls_name not in selected:
            continue
        filtered = []
        for record in records:
            if normal_only is True and record["anomaly"] != 0:
                continue
            if normal_only is False and record["anomaly"] == 0:
                continue
            filtered.append(record)
        if max_per_class is not None and len(filtered) > max_per_class:
            filtered = rng.sample(filtered, max_per_class)
        samples.extend(filtered)
    return samples


def open_sample_image(data_path: str | Path, sample: dict[str, Any]) -> Image.Image:
    return Image.open(Path(data_path) / sample["img_path"]).convert("RGB")


def open_sample_mask(data_path: str | Path, sample: dict[str, Any]) -> Image.Image | None:
    if sample["anomaly"] == 0:
        return None
    mask_path = Path(data_path) / sample["mask_path"]
    if not mask_path.is_file():
        return None
    return Image.open(mask_path).convert("L")


def safe_roc_auc(labels: np.ndarray, scores: np.ndarray) -> float:
    labels = labels.astype(np.uint8).ravel()
    scores = scores.astype(np.float64).ravel()
    if len(np.unique(labels)) < 2:
        return float("nan")
    return float(roc_auc_score(labels, scores))


def finite_mean(values: np.ndarray) -> float:
    values = values[np.isfinite(values)]
    if values.size == 0:
        return float("nan")
    return float(values.mean())


def threshold_for_tpr(anomaly_scores: np.ndarray, target_tpr: float) -> float:
    anomaly_scores = anomaly_scores[np.isfinite(anomaly_scores)]
    if anomaly_scores.size == 0:
        return float("nan")
    return float(np.percentile(anomaly_scores, (1.0 - target_tpr) * 100.0))


def rate_at_threshold(scores: np.ndarray, threshold: float) -> float:
    scores = scores[np.isfinite(scores)]
    if scores.size == 0 or not np.isfinite(threshold):
        return float("nan")
    return float((scores >= threshold).mean())


def topk_mean(values: np.ndarray, fraction: float = 0.01) -> float:
    values = values[np.isfinite(values)].ravel()
    if values.size == 0:
        return float("nan")
    k = max(1, int(values.size * fraction))
    return float(np.partition(values, -k)[-k:].mean())


def write_csv(path: str | Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    if fieldnames is None:
        fieldnames = sorted({key for row in rows for key in row})
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_json(path: str | Path, payload: Any) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    with path.open("w") as f:
        json.dump(payload, f, indent=2)


def normalize_map(score_map: np.ndarray) -> np.ndarray:
    score_map = score_map.astype(np.float32)
    finite = np.isfinite(score_map)
    if not finite.any():
        return np.zeros_like(score_map, dtype=np.float32)
    min_v = float(score_map[finite].min())
    max_v = float(score_map[finite].max())
    if max_v <= min_v:
        return np.zeros_like(score_map, dtype=np.float32)
    return np.clip((score_map - min_v) / (max_v - min_v), 0.0, 1.0)


def colorize_scoremap(score_map: np.ndarray) -> Image.Image:
    x = normalize_map(score_map)
    r = np.clip(1.5 - np.abs(4.0 * x - 3.0), 0.0, 1.0)
    g = np.clip(1.5 - np.abs(4.0 * x - 2.0), 0.0, 1.0)
    b = np.clip(1.5 - np.abs(4.0 * x - 1.0), 0.0, 1.0)
    rgb = np.stack([r, g, b], axis=-1)
    return Image.fromarray((rgb * 255).astype(np.uint8), mode="RGB")


def overlay_scoremap(image: Image.Image, score_map: np.ndarray, alpha: float = 0.45) -> Image.Image:
    base = image.convert("RGB").resize((score_map.shape[1], score_map.shape[0]))
    heat = colorize_scoremap(score_map)
    return Image.blend(base, heat, alpha=alpha)


def mask_panel(mask: np.ndarray) -> Image.Image:
    panel = (mask.astype(np.uint8) * 255)
    return Image.fromarray(panel, mode="L").convert("RGB")


def _labeled_panel(image: Image.Image, label: str, width: int, height: int) -> Image.Image:
    image = image.convert("RGB").resize((width, height))
    label_h = 24
    canvas = Image.new("RGB", (width, height + label_h), color=(255, 255, 255))
    canvas.paste(image, (0, label_h))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, width, label_h), fill=(245, 245, 245))
    draw.text((6, 5), label[:32], fill=(20, 20, 20))
    return canvas


def save_comparison_grid(
    image: Image.Image,
    mask: np.ndarray | None,
    maps: dict[str, np.ndarray],
    path: str | Path,
    labels: dict[str, str] | None = None,
) -> None:
    labels = labels or {}
    path = Path(path)
    ensure_dir(path.parent)

    first_map = next(iter(maps.values()))
    height, width = first_map.shape
    panels = [_labeled_panel(image, "image", width, height)]
    if mask is not None:
        panels.append(_labeled_panel(mask_panel(mask), "mask", width, height))
    for name, score_map in maps.items():
        label = labels.get(name, name)
        panels.append(_labeled_panel(overlay_scoremap(image, score_map), label, width, height))

    grid = Image.new("RGB", (width * len(panels), height + 24), color=(255, 255, 255))
    for idx, panel in enumerate(panels):
        grid.paste(panel, (idx * width, 0))
    grid.save(path)
