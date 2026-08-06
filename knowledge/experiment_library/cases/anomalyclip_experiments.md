# AnomalyCLIP Experiments

Source: [AnomalyCLIP card](../../cards/zhou-2024-anomalyclip.md), text `../../text/zhou-2024-anomalyclip.txt`

## Experiment Claim

Object-agnostic prompt learning can transfer generic normality/abnormality to unseen object categories and even non-industrial domains.

## Main Experiment Package

- Industrial ZSAD comparison on MVTec AD, VisA, MPDD, BTAD, SDD, DAGM, and DTD-style datasets.
- Medical-domain comparison on multiple image and segmentation datasets.
- Image-level metrics: AUROC and AP.
- Pixel-level metrics: AUROC and PRO/AUPRO.
- Baselines include CLIP, CLIP-AC, WinCLIP, VAND, CoOp, and AnomalyCLIP.
- A supplementary comparison against full-shot industrial methods such as PatchCore and RD4AD is used as upper-bound context.

## Tables And Figures

- Table 1: industrial-domain ZSAD main comparison, split into image-level and pixel-level blocks.
- Table 2: medical-domain ZSAD comparison.
- Table 3: additional medical transfer setting.
- Table 4: module ablation.
- Table 5: local/global context optimization ablation.
- Figure 1: motivation and qualitative comparison of CLIP, WinCLIP, CoOp, and AnomalyCLIP.
- Figure 2: method overview.
- Figure 3: DPAM visualization.
- Figure 4: segmentation visualization.
- Figure 5: object-agnostic versus object-aware prompt gain.
- Figure 6: DPAM component ablation.
- Figure 7: hyperparameter analysis.
- Figure 8 and related tables: object/token robustness and prompt-word robustness.

## What Is Required To Borrow

If a new paper claims object/category-agnostic transfer:

- Do industrial cross-dataset evaluation with source-target category separation.
- Include both image-level and pixel-level metrics.
- Include an object-aware versus object-agnostic prompt ablation.
- Show qualitative maps on categories not seen during tuning.
- Add prompt/state-word robustness only if text prompts are central.

## What Is Optional

- Medical-domain evaluation is useful only if the paper claims cross-domain abnormality transfer.
- Full-shot PatchCore/RD comparison should be framed as an upper-bound context, not a fair zero-shot comparison.
- Extensive prompt-token synonym tables can be appendix material.

## Do Not Copy Blindly

Do not fine-tune on target test data without explicitly matching the original protocol. For a new paper, source and target datasets must be stated in the setup table.

## Transfer Checklist

- Main table: MVTec AD + VisA at minimum.
- Generalization table: add MPDD/BTAD/KSDD/DAGM/DTD if claiming broad transfer.
- Ablation: object-aware vs object-agnostic, local/global losses, visual refinement module.
- Figure: qualitative anomaly maps plus representation/attention visualization if claiming mechanism.
