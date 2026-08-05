#!/usr/bin/env bash
set -euo pipefail

DEFAULT_DATA_PATH="${ANOMALYCLIP_MVTEC_DATA_PATH:-/Users/bytedance/Downloads/mvtec_anomaly_detection}"
DEFAULT_CHECKPOINT_PATH="${ANOMALYCLIP_CHECKPOINT_PATH:-checkpoints/9_12_4_multiscale/epoch_15.pth}"

if [ "$#" -ge 1 ]; then
  DATA_PATH="$1"
  shift
else
  DATA_PATH="${DEFAULT_DATA_PATH}"
fi
if [ "$#" -ge 1 ]; then
  CHECKPOINT_PATH="$1"
  shift
else
  CHECKPOINT_PATH="${DEFAULT_CHECKPOINT_PATH}"
fi
if [ "$#" -ge 1 ]; then
  SAVE_ROOT="$1"
  shift
else
  SAVE_ROOT="./results/topconf_failure_mode_mvtec"
fi
DEVICE="${CUDA_VISIBLE_DEVICES:-0}"
PYTHON_BIN="${PYTHON_BIN:-python}"
export CLIP_CACHE_DIR="${CLIP_CACHE_DIR:-/Users/bytedance/code/env/.cache/clip}"

if [ ! -f "${DATA_PATH}/meta.json" ]; then
  echo "MVTec meta.json not found under DATA_PATH=${DATA_PATH}" >&2
  exit 1
fi
if [ ! -f "${CHECKPOINT_PATH}" ]; then
  echo "Checkpoint not found: ${CHECKPOINT_PATH}" >&2
  exit 1
fi
if [ ! -f "${CLIP_CACHE_DIR}/ViT-L-14-336px.pt" ]; then
  echo "CLIP ViT-L/14@336px weights not found under CLIP_CACHE_DIR=${CLIP_CACHE_DIR}" >&2
  exit 1
fi

CUDA_VISIBLE_DEVICES="${DEVICE}" "${PYTHON_BIN}" experiments/failure_mode_benchmark.py \
  --dataset mvtec \
  --data_path "${DATA_PATH}" \
  --checkpoint_path "${CHECKPOINT_PATH}" \
  --save_path "${SAVE_ROOT}" \
  --features_list 24 \
  --feature_map_layer 0 \
  --image_size 518 \
  --depth 9 \
  --n_ctx 12 \
  --t_n_ctx 4 \
  --class_filter capsule pill transistor screw toothbrush \
  --variants cosine cone_normal_only cone_contrastive \
  --target_anomaly_tpr 0.80 \
  "$@"
