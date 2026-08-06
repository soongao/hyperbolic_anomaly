# DevPrompt Experiments

Source: [DevPrompt card](../../cards/poudineh-2026-devprompt.md), text `../../text/poudineh-2026-devprompt.txt`

## Experiment Claim

Deviation-guided prompt learning improves one-normal/few-shot localization by using statistically significant patch deviations.

## Main Experiment Package

- MVTec AD and VisA class-wise pixel-level AUROC.
- Baselines include PromptAD, WinCLIP, PatchCore, and the proposed method.
- Sensitivity analysis for deviation coefficient, top-K patch percentage, and confidence parameter.
- Qualitative patch-wise anomaly score visualization.

## Tables And Figures

- Table 1: MVTec AD class-wise AUROC.
- Table 2: VisA class-wise AUROC.
- Figure 1: patch-wise anomaly score visualization.
- Figure 2: average AUROC comparison across MVTec AD and VisA.
- Table 3: deviation coefficient lambda sensitivity.
- Table 4: top-K percentage sensitivity.
- Table 5: confidence parameter sensitivity.

## What Is Required To Borrow

If a new paper claims deviation-guided one-normal prompt learning:

- Compare to PromptAD directly.
- Report class-wise AUROC on MVTec AD and VisA.
- Include sensitivity for deviation threshold/top-K/confidence.
- Add qualitative score maps showing what the deviation term changes.

## What Is Optional

- If the method is not one-normal/few-shot, DevPrompt's sensitivity package is not necessary.
- Average AUROC bar charts are optional; use tables for primary evidence.

## Do Not Copy Blindly

This paper's experiment package is narrower than the strongest ZSAD papers. For a top-tier ZSAD submission, add AP/F1/PRO, stronger baselines, and seed variance.

## Transfer Checklist

- Main table: MVTec/VisA class-wise plus average metrics.
- Ablation: deviation coefficient, top-K patches, confidence filtering.
- Figure: patch score maps and average comparison.
