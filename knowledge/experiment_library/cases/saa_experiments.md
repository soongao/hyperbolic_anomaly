# SAA+ Experiments

Source: [SAA card](../../cards/cao-2023-segmentanyanomaly.md), text `../../text/cao-2023-segmentanyanomaly.txt`

## Experiment Claim

SAM and CLIP can be assembled for zero-shot anomaly segmentation if hybrid prompt regularization filters irrelevant anomaly candidates.

## Main Experiment Package

- Zero-shot anomaly segmentation on VisA, MVTec AD, KSDD2, and MTD.
- Metrics focus on max-F1-pixel and max-F1-region.
- Baselines include ClipSeg, UTAD, vanilla SAA, WinCLIP where available, and SAA+.
- Experiments are segmentation-only.

## Tables And Figures

- Table 1: quantitative comparison by dataset and defect type.
- Figure 1: vanilla baseline and motivation.
- Figure 2: SAA+ framework.
- Figure 3: qualitative comparison on four datasets.
- Table 2: hybrid prompt regularization ablation.
- Figure 4: qualitative effect of disabling/enabling prompt components.
- Figure 5: hyperparameter sensitivity.

## What Is Required To Borrow

If a new paper uses SAM/LVLM or candidate mask filtering:

- Include region-level and pixel-level segmentation metrics.
- Compare against a vanilla foundation-model assembly baseline.
- Ablate language, saliency, and property prompts or equivalent filters.
- Show qualitative over-detection reduction.

## What Is Optional

- Image-level classification is unnecessary if the method is segmentation-only.
- AUROC/AP can be added for compatibility with ZSAD papers, but max-F1 is closer to SAA's mask-selection story.

## Do Not Copy Blindly

Do not use SAA-style metrics alone if your paper targets CLIP-ZSAD benchmarks. Reviewers will expect AUROC/AP/PRO alongside F1.

## Transfer Checklist

- Main table: segmentation metrics by dataset.
- Ablation: prompt/filter components.
- Figure: candidate mask over-detection before/after filtering.
