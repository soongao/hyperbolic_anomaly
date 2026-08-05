#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <mvtec_data_path> <checkpoint_path> [save_root]" >&2
  exit 1
fi

DATA_PATH="$1"
CHECKPOINT_PATH="$2"
SAVE_ROOT="${3:-./results/gap_ablation_mvtec}"
DEVICE="${CUDA_VISIBLE_DEVICES:-0}"

COMMON_ARGS=(
  --dataset mvtec
  --data_path "${DATA_PATH}"
  --checkpoint_path "${CHECKPOINT_PATH}"
  --features_list 24
  --feature_map_layer 0
  --image_size 518
  --depth 9
  --n_ctx 12
  --t_n_ctx 4
  --metrics image-pixel-level
  --class_filter capsule pill transistor screw toothbrush
)

run_variant() {
  local name="$1"
  shift
  echo "Running ${name}"
  CUDA_VISIBLE_DEVICES="${DEVICE}" python test.py \
    "${COMMON_ARGS[@]}" \
    --save_path "${SAVE_ROOT}/${name}" \
    "$@"
}

# Baseline: flat CLIP/AnomalyCLIP prompt similarity.
run_variant cosine \
  --score_mode cosine

# Controls that isolate whether gains come from generic energy scoring or distance geometry.
run_variant euclidean_contrastive \
  --score_mode euclidean_energy \
  --entailment_mode contrastive \
  --patch_score_space prob

run_variant hyperbolic_distance_contrastive \
  --score_mode hyperbolic_distance \
  --entailment_mode contrastive \
  --patch_score_space prob

# Cone controls that isolate the need for contrastive normality entailment.
run_variant cone_normal_only \
  --score_mode normality_entailment \
  --entailment_mode normal_only \
  --context_weight 0.0 \
  --order_weight 0.0 \
  --patch_score_space prob

run_variant cone_anomaly_only \
  --score_mode normality_entailment \
  --entailment_mode anomaly_only \
  --context_weight 0.0 \
  --order_weight 0.0 \
  --patch_score_space prob

run_variant cone_contrastive \
  --score_mode normality_entailment \
  --entailment_mode contrastive \
  --context_weight 0.0 \
  --order_weight 0.0 \
  --patch_score_space prob
