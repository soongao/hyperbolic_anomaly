#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <mvtec_data_path> <checkpoint_path> [save_root]" >&2
  exit 1
fi

DATA_PATH="$1"
CHECKPOINT_PATH="$2"
SAVE_ROOT="${3:-./results/uot_anchor_ablation_mvtec}"
DEVICE="${CUDA_VISIBLE_DEVICES:-0}"
PYTHON_BIN="${PYTHON_BIN:-python}"

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
  --score_mode hyperbolic_uot
  --ot_mode unbalanced
  --ot_cost hyperbolic_cone
  --ot_score combined
)

run_variant() {
  local name="$1"
  shift
  echo "Running ${name}"
  CUDA_VISIBLE_DEVICES="${DEVICE}" "${PYTHON_BIN}" test.py \
    "${COMMON_ARGS[@]}" \
    --save_path "${SAVE_ROOT}/${name}" \
    "$@"
}

run_variant normal_anchor \
  --ot_anchor_mode normal

run_variant anomaly_anchor_negative_control \
  --ot_anchor_mode anomaly

run_variant normal_anomaly_anchors \
  --ot_anchor_mode both
