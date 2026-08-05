from __future__ import annotations

import argparse
import math
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import torch
from PIL import Image
from tqdm import tqdm

from normality_experiment_utils import (
    add_common_args,
    build_dataset,
    build_inference_context,
    ensure_dir,
    rate_at_threshold,
    run_variants_on_tensor,
    safe_roc_auc,
    save_comparison_grid,
    setup_seed,
    threshold_for_tpr,
    topk_mean,
    validate_variants,
    write_csv,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        "Failure-mode benchmark for flat scoring vs contrastive normality entailment",
        add_help=True,
    )
    add_common_args(parser)
    parser.add_argument("--target_anomaly_tpr", type=float, default=0.80)
    parser.add_argument("--max_pixels_per_image", type=int, default=4096)
    parser.add_argument("--max_visuals_per_class", type=int, default=3)
    parser.add_argument("--num_workers", type=int, default=0)
    return parser.parse_args()


def sample_pixels(values: np.ndarray, max_pixels: int, rng: random.Random) -> np.ndarray:
    values = values[np.isfinite(values)].ravel()
    if values.size <= max_pixels:
        return values.astype(np.float32)
    indices = rng.sample(range(values.size), max_pixels)
    return values[np.array(indices, dtype=np.int64)].astype(np.float32)


def push_candidate(bucket: list[dict[str, Any]], candidate: dict[str, Any], max_count: int) -> None:
    if max_count <= 0:
        return
    bucket.append(candidate)
    bucket.sort(key=lambda item: item["rank_score"], reverse=True)
    del bucket[max_count:]


def tensor_to_mask(mask_tensor: torch.Tensor) -> np.ndarray:
    mask_np = mask_tensor.detach().cpu().squeeze().numpy()
    return (mask_np > 0.5).astype(np.uint8)


def finite_mean(values: np.ndarray) -> float:
    values = values[np.isfinite(values)]
    if values.size == 0:
        return float("nan")
    return float(values.mean())


def finite_percentile(values: np.ndarray, percentile: float) -> float:
    values = values[np.isfinite(values)]
    if values.size == 0:
        return float("nan")
    return float(np.percentile(values, percentile))


def main() -> None:
    args = parse_args()
    setup_seed(args.seed)
    validate_variants(args.variants)
    save_path = ensure_dir(args.save_path)
    ensure_dir(save_path / "visuals" / "normal_worst")
    ensure_dir(save_path / "visuals" / "defect_examples")

    dataset, obj_list = build_dataset(args)
    dataloader = torch.utils.data.DataLoader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=args.num_workers,
    )
    ctx = build_inference_context(args)
    rng = random.Random(args.seed)

    pixel_banks: dict[str, dict[str, dict[str, list[np.ndarray]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )
    per_image_rows: list[dict[str, Any]] = []
    normal_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    defect_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for items in tqdm(dataloader, desc="failure-mode"):
        image_tensor = items["img"].to(ctx.device)
        cls_name = items["cls_name"][0]
        image_path = items["img_path"][0]
        anomaly_label = int(items["anomaly"].detach().cpu().item())
        mask_np = tensor_to_mask(items["img_mask"])

        outputs = run_variants_on_tensor(
            ctx,
            args,
            image_tensor,
            args.variants,
            return_components=False,
        )
        maps = {variant: outputs[variant]["anomaly_map"] for variant in args.variants}

        normal_rank_score = -math.inf
        defect_rank_score = -math.inf
        for variant, output in outputs.items():
            anomaly_map = output["anomaly_map"]
            mask_bool = mask_np.astype(bool)
            top1 = topk_mean(anomaly_map, fraction=0.01)
            top5 = topk_mean(anomaly_map, fraction=0.05)
            row = {
                "class": cls_name,
                "variant": variant,
                "image_path": image_path,
                "anomaly_label": anomaly_label,
                "image_score": output["image_score"],
                "map_mean": finite_mean(anomaly_map),
                "map_p95": finite_percentile(anomaly_map, 95.0),
                "map_top1pct_mean": top1,
                "map_top5pct_mean": top5,
            }

            if anomaly_label == 0:
                normal_pixels = sample_pixels(anomaly_map, args.max_pixels_per_image, rng)
                pixel_banks[cls_name][variant]["normal"].append(normal_pixels)
                normal_rank_score = max(normal_rank_score, top1)
                row.update(
                    {
                        "anomaly_region_mean": float("nan"),
                        "background_region_mean": finite_mean(anomaly_map),
                        "region_gap": float("nan"),
                        "pixel_auc_within_image": float("nan"),
                    }
                )
            else:
                anomaly_pixels = anomaly_map[mask_bool]
                background_pixels = anomaly_map[~mask_bool]
                pixel_banks[cls_name][variant]["anomaly"].append(
                    sample_pixels(anomaly_pixels, args.max_pixels_per_image, rng)
                )
                pixel_banks[cls_name][variant]["defect_background"].append(
                    sample_pixels(background_pixels, args.max_pixels_per_image, rng)
                )
                auc = safe_roc_auc(mask_np, anomaly_map)
                region_gap = finite_mean(anomaly_pixels) - finite_mean(background_pixels)
                defect_rank_score = max(defect_rank_score, auc if np.isfinite(auc) else -math.inf)
                row.update(
                    {
                        "anomaly_region_mean": finite_mean(anomaly_pixels),
                        "background_region_mean": finite_mean(background_pixels),
                        "region_gap": region_gap,
                        "pixel_auc_within_image": auc,
                    }
                )
            per_image_rows.append(row)

        if anomaly_label == 0 and np.isfinite(normal_rank_score):
            push_candidate(
                normal_candidates[cls_name],
                {
                    "rank_score": normal_rank_score,
                    "image_path": image_path,
                    "mask": mask_np.copy(),
                    "maps": {name: score_map.copy() for name, score_map in maps.items()},
                },
                args.max_visuals_per_class,
            )
        elif anomaly_label == 1 and np.isfinite(defect_rank_score):
            push_candidate(
                defect_candidates[cls_name],
                {
                    "rank_score": defect_rank_score,
                    "image_path": image_path,
                    "mask": mask_np.copy(),
                    "maps": {name: score_map.copy() for name, score_map in maps.items()},
                },
                args.max_visuals_per_class,
            )

    summary_rows: list[dict[str, Any]] = []
    for cls_name in obj_list:
        for variant in args.variants:
            banks = pixel_banks[cls_name][variant]
            normal_scores = np.concatenate(banks["normal"]) if banks["normal"] else np.array([])
            anomaly_scores = np.concatenate(banks["anomaly"]) if banks["anomaly"] else np.array([])
            background_scores = (
                np.concatenate(banks["defect_background"]) if banks["defect_background"] else np.array([])
            )
            threshold = threshold_for_tpr(anomaly_scores, args.target_anomaly_tpr)

            defect_labels = np.concatenate(
                [
                    np.ones_like(anomaly_scores, dtype=np.uint8),
                    np.zeros_like(background_scores, dtype=np.uint8),
                ]
            )
            defect_scores = np.concatenate([anomaly_scores, background_scores])
            all_background_scores = np.concatenate([normal_scores, background_scores])

            summary_rows.append(
                {
                    "class": cls_name,
                    "variant": variant,
                    "target_anomaly_tpr": args.target_anomaly_tpr,
                    "threshold_at_target_tpr": threshold,
                    "actual_anomaly_tpr": rate_at_threshold(anomaly_scores, threshold),
                    "normal_image_fpr_at_target_tpr": rate_at_threshold(normal_scores, threshold),
                    "defect_background_fpr_at_target_tpr": rate_at_threshold(background_scores, threshold),
                    "all_background_fpr_at_target_tpr": rate_at_threshold(all_background_scores, threshold),
                    "defect_pixel_auc_sampled": safe_roc_auc(defect_labels, defect_scores),
                    "normal_score_mean": finite_mean(normal_scores),
                    "normal_score_p95": finite_percentile(normal_scores, 95.0),
                    "anomaly_score_mean": finite_mean(anomaly_scores),
                    "defect_background_score_mean": finite_mean(background_scores),
                    "sampled_normal_pixels": int(normal_scores.size),
                    "sampled_anomaly_pixels": int(anomaly_scores.size),
                    "sampled_defect_background_pixels": int(background_scores.size),
                }
            )

    write_csv(save_path / "failure_summary.csv", summary_rows)
    write_csv(save_path / "failure_per_image.csv", per_image_rows)
    write_json(
        save_path / "experiment_manifest.json",
        {
            "experiment": "failure_mode_benchmark",
            "claim_tested": (
                "Flat prompt scoring and normal-only entailment should show higher false positives "
                "on complex normal structures than contrastive normality entailment."
            ),
            "dataset": args.dataset,
            "data_path": args.data_path,
            "checkpoint_path": args.checkpoint_path,
            "classes": obj_list,
            "variants": args.variants,
            "target_anomaly_tpr": args.target_anomaly_tpr,
        },
    )

    for cls_name, candidates in normal_candidates.items():
        for rank, candidate in enumerate(candidates, start=1):
            image = Image.open(candidate["image_path"]).convert("RGB")
            out_path = save_path / "visuals" / "normal_worst" / cls_name / f"rank_{rank:02d}.png"
            save_comparison_grid(image, candidate["mask"], candidate["maps"], out_path)

    for cls_name, candidates in defect_candidates.items():
        for rank, candidate in enumerate(candidates, start=1):
            image = Image.open(candidate["image_path"]).convert("RGB")
            out_path = save_path / "visuals" / "defect_examples" / cls_name / f"rank_{rank:02d}.png"
            save_comparison_grid(image, candidate["mask"], candidate["maps"], out_path)


if __name__ == "__main__":
    main()
