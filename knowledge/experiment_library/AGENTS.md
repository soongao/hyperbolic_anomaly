# Experiment Library Agent Instructions

This folder is a knowledge base for designing and auditing experiments in ZSAD and CLIP-based anomaly detection papers.

## Retrieval Order

1. Read `README.md` and `usage.md`.
2. For a new method, open `patterns/required_experiments.md` and `patterns/metrics_and_protocols.md`.
3. Open the nearest paper cases under `cases/`.
4. Use `templates/new_zsad_experiment_plan.md` to map method claims to experiments.
5. Check `patterns/optional_and_avoid.md` before recommending expensive experiments.

## Required Distinctions

Always separate:

- `experiment type`: main comparison, ablation, sensitivity, qualitative, efficiency, failure case.
- `claim supported`: what paper claim the experiment validates.
- `required level`: must-have, recommended, optional, or avoid.
- `table/figure role`: what the table or figure is supposed to communicate.
- `protocol risk`: leakage, unfair baseline, metric mismatch, or overclaiming.

## Do Not

- Do not treat full-shot industrial AD baselines as fair direct competitors for zero-shot claims. Use them as an upper-bound context unless the protocol matches.
- Do not recommend medical benchmarks unless the paper claims cross-domain or clinical generalization.
- Do not recommend prompt-word robustness if the method does not depend on text prompts.
- Do not recommend many hyperparameter plots in the main paper; keep most sensitivity details in appendix.
- Do not accept AUROC-only segmentation evidence when AP/F1/PRO would reveal imbalance or region quality.

## Good Entry Standard

A good experiment entry should let a future user answer:

```text
My method claims [X]. Which experiment table or figure do I need to make that claim credible, and which experiments can I skip?
```
