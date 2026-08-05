# Notes: ZSAD Hyperbolic UOT Experiment and Writing Design

## Source: Current UOT Storyline

- File: `paper_storyline/zsad_hyperbolic_uot/README.md`
- Core claim: CLIP-based ZSAD should be formulated as rejectable semantic transport rather than independent normal/anomaly prompt classification.
- Mechanism:
  - CLIP extracts patch and text features.
  - Hyperbolic geometry defines the patch-to-normality cost.
  - UOT produces matched cost and unmatched mass.
- Main claim boundary:
  - Do not claim first use of OT, CLIP+OT, or hyperbolic anomaly detection.
  - Claim unbalanced patch-to-normality semantic transport for CLIP-based ZSAD with hyperbolic cost.

## Source: Existing Code and Experiment Infrastructure

- `test.py` supports:
  - `--score_mode cosine`
  - `--score_mode euclidean_energy`
  - `--score_mode hyperbolic_distance`
  - `--score_mode normality_entailment`
  - `--entailment_mode normal_only|anomaly_only|contrastive`
- `experiments/normality_experiment_utils.py` already defines variants for:
  - cosine
  - euclidean_contrastive
  - hyperbolic_distance_contrastive
  - cone_normal_only
  - cone_anomaly_only
  - cone_contrastive
- `scripts/run_gap_ablation_mvtec.sh` runs weak-class ablations on:
  - capsule
  - pill
  - transistor
  - screw
  - toothbrush
- `scripts/run_failure_mode_mvtec.sh` and `scripts/run_mechanism_causal_mvtec.sh` already provide top-conference-style failure-mode and synthetic-causal protocols for current cone scoring variants.

## Design Implications

- The UOT experiment design should not replace the existing hyperbolic/cone ablations. It should extend them.
- The minimal new variants should isolate three factors:
  - transport: no OT vs balanced OT vs partial OT vs UOT
  - cost: cosine vs Euclidean vs hyperbolic distance vs hyperbolic cone violation
  - anomaly signal: matched cost vs unmatched mass vs combined score
- The key mechanism evidence should show:
  - balanced OT over-matches anomalous pixels;
  - UOT gives anomalous pixels higher unmatched mass;
  - hyperbolic/cone cost improves transport quality over cosine cost;
  - unmatched mass is not just a noisy saliency map.

## Required Paper Evidence

- Main table: MVTec, VisA, and if possible medical datasets from AnomalyCLIP.
- Mechanism table: balanced/partial/UOT with cost variants.
- Failure-mode figure: normal images where balanced or cosine scoring over-activates normal structures, while UOT reduces false positives.
- Transport visualization:
  - transport mass map;
  - unmatched mass map;
  - matched cost map;
  - final anomaly map.
- Distribution figure:
  - normal pixels vs anomaly pixels for unmatched mass and matched cost.

