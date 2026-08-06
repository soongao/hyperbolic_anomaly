# APRIL-GAN Experiments

Source: [APRIL-GAN card](../../cards/chen-2023-april-gan.md), text `../../text/chen-2023-april-gan.txt`

## Experiment Claim

APRIL-GAN is a challenge-style zero-/few-shot anomaly classification and segmentation solution that aligns dense visual features with text features and combines zero-shot maps with few-shot reference features.

## Main Experiment Package

- VAND challenge zero-shot and few-shot tracks.
- Standard MVTec AD and VisA evaluations.
- Metrics include F1-max for challenge leaderboard, plus AUROC, AP, and PRO for standard datasets.
- Shot settings include 0-shot, 1-shot, 2-shot, and 4-shot.
- Reports mean and standard deviation over random seeds for standard comparisons.

## Tables And Figures

- Tables 1-2: top-five VAND challenge leaderboard results for zero-shot and few-shot tracks.
- Figure 1: overall solution diagram.
- Figure 2: zero-/few-shot visualization on challenge examples.
- Tables 3-4: quantitative comparisons on MVTec AD and VisA with AUROC-segm, F1-max-segm, AP-segm, PRO-segm, AUROC-cls, F1-max-cls, AP-cls.
- Figures 3-4: qualitative results on MVTec AD and VisA.
- Tables 5-12: per-object results for zero-shot, 1-shot, 2-shot, and 4-shot settings.

## What Is Required To Borrow

If a new paper uses APRIL-GAN as a baseline:

- Match the metric set: AUROC, AP, PRO, F1-max for segmentation; AUROC/AP/F1 for classification.
- State the source-target training setup clearly.
- Use APRIL-GAN mainly as a strong early CLIP-ZSAD baseline.

If borrowing the experiment style:

- Include challenge metrics only when targeting challenge-like evaluation.
- Use shot-wise tables when few-shot references are part of the method.

## What Is Optional

- Leaderboard-style top-five comparisons are not needed for a normal conference paper unless there is a challenge protocol.
- Per-object tables belong in appendix.

## Do Not Copy Blindly

APRIL-GAN's challenge protocol is not the same as a clean no-training zero-shot protocol. Do not mix challenge scores with standard ZSAD scores without explaining the setting.

## Transfer Checklist

- Use APRIL-GAN as a baseline in main comparison.
- For few-shot claims, include 0/1/2/4-shot tables and qualitative examples.
- Use F1-max only with clear threshold interpretation.
