# AA-CLIP Experiments

Source: [AA-CLIP card](../../cards/ma-2025-aa-clip.md), text `../../text/ma-2025-aa-clip.txt`

## Experiment Claim

CLIP is anomaly-unaware, and a two-stage adapter strategy can first build anomaly-aware text anchors and then align visual patch features to them.

## Main Experiment Package

- Zero-shot AD comparison across industrial and medical domains.
- Industrial datasets include MVTec AD, VisA, BTAD, and MPDD.
- Medical datasets include image-level and pixel-level datasets.
- Metrics are mainly AUROC at pixel and image levels.
- Baselines include CLIP variants, WinCLIP, APRIL-GAN/AnomalyCLIP-style methods, and adapter-related comparisons.
- Shot/data efficiency analysis shows performance under limited auxiliary samples.

## Tables And Figures

- Table 1: pixel-level AUROC across industrial and medical domains.
- Table 2: image-level AUROC across industrial and medical domains.
- Table 3: ablation of training strategy using VisA/MVTec transfer.
- Figure 1: conceptual visualization of anomaly unawareness.
- Figure 2: examples of CLIP anomaly-unawareness.
- Figure 3: t-SNE visualization of text features before/after anomaly awareness.
- Figure 4: two-stage training pipeline.
- Figure 5: average results and data-efficiency/shot analysis.
- Figure 6: anomaly localization visualization.
- Figure 7: one-stage training text-space visualization.

## What Is Required To Borrow

If a new paper claims "anomaly awareness", "concept-first learning", or staged adapter training:

- Include a one-stage versus two-stage ablation.
- Include adapter/no-adapter or residual-adapter removal.
- Visualize text anchors or representation separation.
- Show localization maps before and after the alignment stage.
- Report training data efficiency if the method claims efficient adaptation.

## What Is Optional

- Large medical benchmark sweeps are optional unless cross-domain anomaly awareness is a central claim.
- If the method does not alter text space, t-SNE of text anchors is not necessary.

## Do Not Copy Blindly

Do not use "anomaly-aware" as a name unless the experiments directly show concept separation or staged alignment advantage. Pure performance improvement is not enough.

## Transfer Checklist

- Main table: image and pixel AUROC on industrial datasets.
- Ablation: one-stage vs two-stage, text adapter, image adapter, residual design.
- Figure: text-space t-SNE and anomaly maps.
- Optional: data-efficiency curve with limited auxiliary samples.
