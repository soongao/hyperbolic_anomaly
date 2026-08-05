# Top-Conference Experiment Protocols: Failure Mode and Causal Mechanism

This file defines the first two large experiments for the contrastive normality entailment story.

## Experiment 1: Failure-Mode Benchmark

Claim tested:

> Flat prompt scoring and normal-only entailment systematically over-score complex but normal local structures; contrastive normality entailment should reduce these false positives while preserving defect localization.

Run:

```bash
PYTHON_BIN=.venv/bin/python bash scripts/run_failure_mode_mvtec.sh \
  <mvtec_data_path> \
  checkpoints/9_12_4_multiscale/epoch_15.pth
```

Main outputs:

- `failure_summary.csv`: per-class and per-variant false-positive rates.
- `failure_per_image.csv`: per-image top-score and region statistics.
- `visuals/normal_worst/`: worst normal images by high anomaly-map activation.
- `visuals/defect_examples/`: defect localization examples.

Primary paper metric:

`normal_image_fpr_at_target_tpr`, measured at a fixed anomaly-pixel TPR, e.g. 80%.

Interpretation:

- Supports the story if `cone_normal_only` and/or `cosine` show higher normal-image FPR on complex normal classes than `cone_contrastive`.
- Weakens the story if contrastive scoring does not reduce normal-region false positives or only improves aggregate AUROC without visible failure-mode repair.

## Experiment 2: Mechanism-Causal Experiment

Claim tested:

> If anomaly scoring captures local normality violation, controlled defect severity should monotonically increase anomaly scores and the normal/anomaly energy gap.

Run:

```bash
PYTHON_BIN=.venv/bin/python bash scripts/run_mechanism_causal_mvtec.sh \
  <mvtec_data_path> \
  checkpoints/9_12_4_multiscale/epoch_15.pth
```

Optional real-anomaly repair negative control:

```bash
PYTHON_BIN=.venv/bin/python bash scripts/run_mechanism_causal_mvtec.sh \
  <mvtec_data_path> \
  checkpoints/9_12_4_multiscale/epoch_15.pth \
  ./results/topconf_mechanism_causal_mvtec_repair \
  --include_real_repairs
```

Main outputs:

- `causal_synthetic_per_sample.csv`: every synthetic intervention result.
- `causal_synthetic_summary.csv`: grouped means by class, defect type, variant, and severity.
- `causal_synthetic_monotonicity.csv`: Spearman correlation between severity and mechanism metrics.
- `causal_real_repair.csv`: optional before/after score drops on real masked anomalies.
- `visuals/synthetic/`: variant maps and energy maps for representative synthetic defects.
- `visuals/real_repair/`: optional before/after repair maps.

Primary paper metrics:

- `spearman_rho_vs_severity` for `region_gap`, `normal_energy_region_gap`, and `energy_gap_region_gap`.
- `mask_mean_drop` and `region_gap_drop` for optional real-anomaly repair.

Interpretation:

- Supports the mechanism if severity has a positive monotonic relation with the contrastive region gap and energy gap.
- Weakens the mechanism if score changes are not monotonic, or if the same trend appears equally in flat cosine scoring without energy-level evidence.

