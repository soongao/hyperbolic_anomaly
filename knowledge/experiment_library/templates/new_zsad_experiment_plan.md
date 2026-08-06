# New ZSAD Experiment Plan

Use this canvas before running experiments.

## 1. Method Claim

```text
Our method claims to improve [task] by [mechanism] under [protocol].
```

## 2. Protocol

- Setting: zero-shot / auxiliary-data ZSAD / few-shot normal-only / test-time adaptation / language-free / SAM-LVLM.
- Source data allowed:
- Target data allowed:
- Target labels/masks allowed:
- Backbones:
- Input resolution:

## 3. Must-Have Main Tables

| Table | Claim Supported | Datasets | Metrics | Baselines | Required? |
|---|---|---|---|---|---|
| Main industrial comparison | | MVTec AD, VisA | I-AUROC/I-AP, P-AUROC/P-AP/P-AUPRO | | P0 |
| Cross-dataset generalization | | MPDD/BTAD/etc. | | | P1/P0 if claimed |
| Medical/cross-domain | | | | | optional unless claimed |
| Few-shot shot curve | | 1/2/4-shot | mean/std | | P0 if few-shot |

## 4. Required Ablations

| Ablation | Full Method Component | Variant | Claim Tested | Dataset | Metric |
|---|---|---|---|---|---|
| w/o module A | | remove | | MVTec/VisA | |
| replace module A | | simple baseline | | MVTec/VisA | |
| sensitivity | | sweep | | | |

## 5. Figures

| Figure | Role | Contents | Required? |
|---|---|---|---|
| Motivation | show prior failure | | P0 |
| Pipeline | explain method | | P0 |
| Qualitative maps | show localization | input/GT/baselines/ours | P0 |
| Mechanism visualization | support core story | t-SNE/attention/distribution | P1 |
| Failure cases | expose boundary | | P2 |

## 6. Experiments To Skip

- Skip:
- Reason:

## 7. Risk Checks

- Does any table use target test data for training?
- Are full-shot baselines framed as upper bounds, not fair zero-shot competitors?
- Are segmentation metrics more than AUROC?
- Does every paper claim have an experiment?
- Are qualitative cases representative, not only easy?
