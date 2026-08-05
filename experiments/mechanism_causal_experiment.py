from __future__ import annotations

import argparse
import math
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.stats import spearmanr
from tqdm import tqdm

from normality_experiment_utils import (
    add_common_args,
    build_inference_context,
    ensure_dir,
    finite_mean,
    load_meta_samples,
    mask_from_pil,
    open_sample_image,
    open_sample_mask,
    run_variants_on_tensor,
    safe_roc_auc,
    save_comparison_grid,
    setup_seed,
    tensor_from_pil,
    validate_variants,
    write_csv,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        "Mechanism-causal experiment for contrastive normality entailment",
        add_help=True,
    )
    add_common_args(parser)
    parser.add_argument(
        "--defect_types",
        type=str,
        nargs="+",
        default=["noise_patch", "color_shift", "cutout", "scratch"],
    )
    parser.add_argument("--severity_levels", type=float, nargs="+", default=[0.25, 0.5, 0.75, 1.0])
    parser.add_argument("--include_clean_baseline", action="store_true", default=True)
    parser.add_argument("--no_clean_baseline", action="store_false", dest="include_clean_baseline")
    parser.add_argument("--trials_per_image", type=int, default=2)
    parser.add_argument("--defect_size_ratio", type=float, default=0.16)
    parser.add_argument("--max_normal_per_class", type=int, default=8)
    parser.add_argument("--max_anomaly_per_class", type=int, default=8)
    parser.add_argument("--include_real_repairs", action="store_true")
    parser.add_argument("--max_visuals_per_class", type=int, default=3)
    return parser.parse_args()


def choose_box(width: int, height: int, size_ratio: float, rng: random.Random) -> tuple[int, int, int, int]:
    side = max(8, int(min(width, height) * size_ratio))
    side = min(side, width, height)
    margin_x = max(0, int(width * 0.05))
    margin_y = max(0, int(height * 0.05))
    max_x = max(margin_x, width - side - margin_x)
    max_y = max(margin_y, height - side - margin_y)
    x0 = rng.randint(margin_x, max_x) if max_x > margin_x else max(0, (width - side) // 2)
    y0 = rng.randint(margin_y, max_y) if max_y > margin_y else max(0, (height - side) // 2)
    return x0, y0, x0 + side, y0 + side


def defect_mask_from_box(size: tuple[int, int], box: tuple[int, int, int, int]) -> Image.Image:
    mask = Image.new("L", size, color=0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle(box, fill=255)
    return mask


def apply_box_defect(
    image: Image.Image,
    defect_type: str,
    severity: float,
    box: tuple[int, int, int, int],
    artifact_seed: int,
) -> tuple[Image.Image, Image.Image]:
    image = image.convert("RGB")
    width, height = image.size
    x0, y0, x1, y1 = box
    rng = np.random.default_rng(artifact_seed)
    arr = np.asarray(image).astype(np.float32)
    out = arr.copy()
    region = arr[y0:y1, x0:x1]
    severity = float(np.clip(severity, 0.0, 1.0))

    if defect_type == "noise_patch":
        noise = rng.uniform(0, 255, size=region.shape).astype(np.float32)
        out[y0:y1, x0:x1] = (1.0 - severity) * region + severity * noise
        mask = defect_mask_from_box((width, height), box)
    elif defect_type == "color_shift":
        signs = rng.choice(np.array([-1.0, 1.0]), size=(3,))
        shift = signs * np.array([80.0, 55.0, 95.0], dtype=np.float32) * severity
        out[y0:y1, x0:x1] = np.clip(region + shift.reshape(1, 1, 3), 0, 255)
        mask = defect_mask_from_box((width, height), box)
    elif defect_type == "cutout":
        fill = rng.choice(np.array([0.0, 255.0], dtype=np.float32), size=(1, 1, 3))
        out[y0:y1, x0:x1] = (1.0 - severity) * region + severity * fill
        mask = defect_mask_from_box((width, height), box)
    elif defect_type == "scratch":
        mask = Image.new("L", (width, height), color=0)
        mask_draw = ImageDraw.Draw(mask)
        line_rng = random.Random(artifact_seed)
        p0 = (line_rng.randint(x0, max(x0, x1 - 1)), line_rng.randint(y0, max(y0, y1 - 1)))
        p1 = (line_rng.randint(x0, max(x0, x1 - 1)), line_rng.randint(y0, max(y0, y1 - 1)))
        line_width = max(1, int((y1 - y0) * 0.08))
        color = rng.choice(np.array([20.0, 235.0], dtype=np.float32), size=(3,))
        mask_draw.line([p0, p1], fill=255, width=line_width)
        mask_np = np.asarray(mask).astype(bool)
        out[mask_np] = (1.0 - severity) * out[mask_np] + severity * color.reshape(1, 3)
        return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), mode="RGB"), mask
    else:
        raise ValueError(f"Unknown defect_type: {defect_type}")

    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), mode="RGB"), mask


def repair_with_blurred_mask(image: Image.Image, mask: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    mask_np = np.asarray(mask.convert("L").resize(image.size)) > 0
    if not mask_np.any():
        return image
    radius = max(5, int(min(image.size) * 0.04))
    blurred = image.filter(ImageFilter.GaussianBlur(radius=radius))
    arr = np.asarray(image).copy()
    blur_arr = np.asarray(blurred)
    arr[mask_np] = blur_arr[mask_np]
    return Image.fromarray(arr, mode="RGB")


def region_stats(mask: np.ndarray, score_map: np.ndarray) -> dict[str, float]:
    mask_bool = mask.astype(bool)
    positive = score_map[mask_bool]
    negative = score_map[~mask_bool]
    return {
        "mask_mean": finite_mean(positive),
        "background_mean": finite_mean(negative),
        "region_gap": finite_mean(positive) - finite_mean(negative),
        "pixel_auc": safe_roc_auc(mask, score_map),
    }


def component_region_stats(mask: np.ndarray, component_maps: dict[str, np.ndarray]) -> dict[str, float]:
    stats: dict[str, float] = {}
    mask_bool = mask.astype(bool)
    for name in ["normal_energy", "anomaly_energy", "energy_gap", "score_energy"]:
        score_map = component_maps.get(name)
        if score_map is None:
            stats[f"{name}_mask_mean"] = float("nan")
            stats[f"{name}_background_mean"] = float("nan")
            stats[f"{name}_region_gap"] = float("nan")
            continue
        positive = score_map[mask_bool]
        negative = score_map[~mask_bool]
        stats[f"{name}_mask_mean"] = finite_mean(positive)
        stats[f"{name}_background_mean"] = finite_mean(negative)
        stats[f"{name}_region_gap"] = finite_mean(positive) - finite_mean(negative)
    return stats


def push_candidate(bucket: list[dict[str, Any]], candidate: dict[str, Any], max_count: int) -> None:
    if max_count <= 0:
        return
    bucket.append(candidate)
    bucket.sort(key=lambda item: item["rank_score"], reverse=True)
    del bucket[max_count:]


def aggregate_by_keys(rows: list[dict[str, Any]], keys: list[str], metrics: list[str]) -> list[dict[str, Any]]:
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)

    output: list[dict[str, Any]] = []
    for group_key, group_rows in grouped.items():
        summary = {key: value for key, value in zip(keys, group_key)}
        summary["n"] = len(group_rows)
        for metric in metrics:
            values = np.array([row.get(metric, float("nan")) for row in group_rows], dtype=np.float64)
            values = values[np.isfinite(values)]
            summary[f"{metric}_mean"] = float(values.mean()) if values.size else float("nan")
            summary[f"{metric}_std"] = float(values.std()) if values.size else float("nan")
        output.append(summary)
    return output


def monotonicity_rows(rows: list[dict[str, Any]], metrics: list[str]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(row["class"], row["defect_type"], row["variant"])].append(row)

    output: list[dict[str, Any]] = []
    for (cls_name, defect_type, variant), group_rows in grouped.items():
        severities = np.array([row["severity"] for row in group_rows], dtype=np.float64)
        for metric in metrics:
            values = np.array([row.get(metric, float("nan")) for row in group_rows], dtype=np.float64)
            keep = np.isfinite(severities) & np.isfinite(values)
            if keep.sum() < 3 or np.unique(severities[keep]).size < 2:
                rho, p_value = float("nan"), float("nan")
            else:
                rho_raw, p_raw = spearmanr(severities[keep], values[keep])
                rho = float(rho_raw) if np.isfinite(rho_raw) else float("nan")
                p_value = float(p_raw) if np.isfinite(p_raw) else float("nan")
            output.append(
                {
                    "class": cls_name,
                    "defect_type": defect_type,
                    "variant": variant,
                    "metric": metric,
                    "spearman_rho_vs_severity": rho,
                    "p_value": p_value,
                    "n": int(keep.sum()),
                }
            )
    return output


def run_synthetic_causal(args: argparse.Namespace, ctx: Any, save_path: Path) -> list[dict[str, Any]]:
    normal_samples = load_meta_samples(
        args.data_path,
        class_filter=args.class_filter,
        normal_only=True,
        max_per_class=args.max_normal_per_class,
        seed=args.seed,
    )
    rng = random.Random(args.seed)
    rows: list[dict[str, Any]] = []
    visual_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    severity_levels = sorted(set(args.severity_levels))
    if args.include_clean_baseline and 0.0 not in severity_levels:
        severity_levels = [0.0] + severity_levels

    max_severity = max(severity_levels)
    for sample in tqdm(normal_samples, desc="synthetic-causal"):
        image = open_sample_image(args.data_path, sample)
        cls_name = sample["cls_name"]
        for trial_idx in range(args.trials_per_image):
            box = choose_box(image.width, image.height, args.defect_size_ratio, rng)
            for defect_type in args.defect_types:
                artifact_seed = rng.randint(0, 2**31 - 1)
                for severity in severity_levels:
                    synthetic_image, defect_mask = apply_box_defect(
                        image,
                        defect_type,
                        severity,
                        box,
                        artifact_seed,
                    )
                    image_tensor = tensor_from_pil(ctx, synthetic_image, args)
                    mask_np = mask_from_pil(ctx, defect_mask, args)
                    outputs = run_variants_on_tensor(
                        ctx,
                        args,
                        image_tensor,
                        args.variants,
                        return_components=True,
                    )
                    maps = {variant: outputs[variant]["anomaly_map"] for variant in args.variants}

                    contrastive_gap = -math.inf
                    for variant, output in outputs.items():
                        stats = region_stats(mask_np, output["anomaly_map"])
                        component_stats = component_region_stats(mask_np, output["component_maps"])
                        row = {
                            "class": cls_name,
                            "image_path": str(Path(args.data_path) / sample["img_path"]),
                            "variant": variant,
                            "defect_type": defect_type,
                            "trial": trial_idx,
                            "severity": severity,
                            "box_x0": box[0],
                            "box_y0": box[1],
                            "box_x1": box[2],
                            "box_y1": box[3],
                            **stats,
                            **component_stats,
                        }
                        rows.append(row)
                        if variant == "cone_contrastive":
                            contrastive_gap = max(contrastive_gap, stats["region_gap"])

                    if severity == max_severity and np.isfinite(contrastive_gap):
                        energy_maps = outputs.get("cone_contrastive", {}).get("component_maps", {})
                        push_candidate(
                            visual_candidates[cls_name],
                            {
                                "rank_score": contrastive_gap,
                                "image": synthetic_image.copy(),
                                "mask": mask_np.copy(),
                                "maps": {name: score_map.copy() for name, score_map in maps.items()},
                                "energy_maps": {
                                    name: energy_maps[name].copy()
                                    for name in ["normal_energy", "anomaly_energy", "energy_gap"]
                                    if name in energy_maps
                                },
                                "defect_type": defect_type,
                                "severity": severity,
                            },
                            args.max_visuals_per_class,
                        )

    for cls_name, candidates in visual_candidates.items():
        for rank, candidate in enumerate(candidates, start=1):
            stem = f"rank_{rank:02d}_{candidate['defect_type']}_sev_{candidate['severity']:.2f}"
            out_dir = save_path / "visuals" / "synthetic" / cls_name
            save_comparison_grid(
                candidate["image"],
                candidate["mask"],
                candidate["maps"],
                out_dir / f"{stem}_variants.png",
            )
            if candidate["energy_maps"]:
                save_comparison_grid(
                    candidate["image"],
                    candidate["mask"],
                    candidate["energy_maps"],
                    out_dir / f"{stem}_energies.png",
                )

    return rows


def run_real_repairs(args: argparse.Namespace, ctx: Any, save_path: Path) -> list[dict[str, Any]]:
    anomaly_samples = load_meta_samples(
        args.data_path,
        class_filter=args.class_filter,
        normal_only=False,
        max_per_class=args.max_anomaly_per_class,
        seed=args.seed,
    )
    rows: list[dict[str, Any]] = []
    visual_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for sample in tqdm(anomaly_samples, desc="real-repair"):
        image = open_sample_image(args.data_path, sample)
        mask_pil = open_sample_mask(args.data_path, sample)
        if mask_pil is None:
            continue
        repaired = repair_with_blurred_mask(image, mask_pil)
        mask_np = mask_from_pil(ctx, mask_pil, args)
        if not mask_np.any():
            continue

        original_outputs = run_variants_on_tensor(
            ctx,
            args,
            tensor_from_pil(ctx, image, args),
            args.variants,
            return_components=True,
        )
        repaired_outputs = run_variants_on_tensor(
            ctx,
            args,
            tensor_from_pil(ctx, repaired, args),
            args.variants,
            return_components=True,
        )

        rank_score = -math.inf
        before_maps = {}
        after_maps = {}
        for variant in args.variants:
            before = region_stats(mask_np, original_outputs[variant]["anomaly_map"])
            after = region_stats(mask_np, repaired_outputs[variant]["anomaly_map"])
            score_drop = before["mask_mean"] - after["mask_mean"]
            rows.append(
                {
                    "class": sample["cls_name"],
                    "image_path": str(Path(args.data_path) / sample["img_path"]),
                    "variant": variant,
                    "mask_mean_before": before["mask_mean"],
                    "mask_mean_after": after["mask_mean"],
                    "mask_mean_drop": score_drop,
                    "background_mean_before": before["background_mean"],
                    "background_mean_after": after["background_mean"],
                    "region_gap_before": before["region_gap"],
                    "region_gap_after": after["region_gap"],
                    "region_gap_drop": before["region_gap"] - after["region_gap"],
                }
            )
            before_maps[f"{variant}_before"] = original_outputs[variant]["anomaly_map"]
            after_maps[f"{variant}_after"] = repaired_outputs[variant]["anomaly_map"]
            if variant == "cone_contrastive":
                rank_score = max(rank_score, score_drop)

        if np.isfinite(rank_score):
            push_candidate(
                visual_candidates[sample["cls_name"]],
                {
                    "rank_score": rank_score,
                    "image": image.copy(),
                    "repaired": repaired.copy(),
                    "mask": mask_np.copy(),
                    "before_maps": {name: score_map.copy() for name, score_map in before_maps.items()},
                    "after_maps": {name: score_map.copy() for name, score_map in after_maps.items()},
                },
                args.max_visuals_per_class,
            )

    for cls_name, candidates in visual_candidates.items():
        for rank, candidate in enumerate(candidates, start=1):
            out_dir = save_path / "visuals" / "real_repair" / cls_name
            save_comparison_grid(
                candidate["image"],
                candidate["mask"],
                candidate["before_maps"],
                out_dir / f"rank_{rank:02d}_before.png",
            )
            save_comparison_grid(
                candidate["repaired"],
                candidate["mask"],
                candidate["after_maps"],
                out_dir / f"rank_{rank:02d}_after.png",
            )

    return rows


def main() -> None:
    args = parse_args()
    setup_seed(args.seed)
    validate_variants(args.variants)
    save_path = ensure_dir(args.save_path)
    ctx = build_inference_context(args)

    synthetic_rows = run_synthetic_causal(args, ctx, save_path)
    metric_names = [
        "mask_mean",
        "background_mean",
        "region_gap",
        "pixel_auc",
        "normal_energy_region_gap",
        "anomaly_energy_region_gap",
        "energy_gap_region_gap",
        "score_energy_region_gap",
    ]
    write_csv(save_path / "causal_synthetic_per_sample.csv", synthetic_rows)
    write_csv(
        save_path / "causal_synthetic_summary.csv",
        aggregate_by_keys(
            synthetic_rows,
            keys=["class", "defect_type", "variant", "severity"],
            metrics=metric_names,
        ),
    )
    write_csv(
        save_path / "causal_synthetic_monotonicity.csv",
        monotonicity_rows(
            synthetic_rows,
            metrics=[
                "mask_mean",
                "region_gap",
                "pixel_auc",
                "normal_energy_region_gap",
                "energy_gap_region_gap",
                "score_energy_region_gap",
            ],
        ),
    )

    repair_rows: list[dict[str, Any]] = []
    if args.include_real_repairs:
        repair_rows = run_real_repairs(args, ctx, save_path)
        write_csv(save_path / "causal_real_repair.csv", repair_rows)

    write_json(
        save_path / "experiment_manifest.json",
        {
            "experiment": "mechanism_causal_experiment",
            "claim_tested": (
                "If anomaly scoring captures local normality violation, controlled defect severity "
                "should monotonically increase anomaly scores and normal/anomaly energy gaps."
            ),
            "dataset": args.dataset,
            "data_path": args.data_path,
            "checkpoint_path": args.checkpoint_path,
            "classes": args.class_filter,
            "variants": args.variants,
            "defect_types": args.defect_types,
            "severity_levels": args.severity_levels,
            "include_clean_baseline": args.include_clean_baseline,
            "include_real_repairs": args.include_real_repairs,
            "synthetic_rows": len(synthetic_rows),
            "repair_rows": len(repair_rows),
        },
    )


if __name__ == "__main__":
    main()
