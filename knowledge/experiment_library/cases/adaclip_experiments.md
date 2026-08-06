# AdaCLIP Experiments

Source: [AdaCLIP card](../../cards/yao-2024-adaclip.md), text `../../text/yao-2024-adaclip.txt`

## Experiment Claim

Hybrid static and dynamic prompts adapt CLIP to ZSAD by combining shared anomaly knowledge with instance-specific adaptation.

## Main Experiment Package

- Main comparison in industrial and medical domains.
- Industrial datasets include MVTec AD, VisA, MPDD, BTAD, KSDD, DAGM, and DTD-Synthetic.
- Medical datasets include image-level and pixel-level tasks.
- Metrics include AUROC and max-F1 at image and pixel levels.
- Baselines include SAA, WinCLIP, DINOV2, SAM, APRIL-GAN, and AnomalyCLIP-style methods.
- Reports average rank across datasets.

## Tables And Figures

- Tables 1-2: industrial and medical comparison with average rank.
- Figure 3: anomaly map visualization across industrial and medical domains.
- Table 3: static prompt and dynamic prompt ablation.
- Figure 4: patch embeddings and anomaly maps under different prompt variants.
- Table 4: HSF ablation.
- Figure 5: prompt depth and length sensitivity.
- Table 5: training data source ablation for medical transfer.
- Figure 6: anomaly maps under different training sets.
- Table 6: backbone comparison and parameter overhead.
- Figure 7: t-SNE visualization of normal/abnormal patch embeddings.
- Appendix tables: detailed dataset-level comparisons and qualitative maps.

## What Is Required To Borrow

If a new paper claims hybrid prompts:

- Include static-only, dynamic-only, neither, and both variants.
- Add visualization showing how prompt variants affect patch embeddings or anomaly maps.
- Include prompt length/depth sensitivity.
- Report auxiliary training data choice if the method uses source data.
- Report parameter overhead or backbone comparison if claiming lightweight adaptation.

## What Is Optional

- Medical evaluation is strong for cross-domain claims but optional for an industrial-only method.
- Average ranking is useful when many datasets are included, but it should not replace raw metrics.
- Long per-category qualitative galleries belong in appendix.

## Do Not Copy Blindly

Do not call a method "hybrid" without showing that each branch has a distinct role. Static-only and dynamic-only ablations are mandatory for this story.

## Transfer Checklist

- Main table: industrial MVTec/VisA plus broader datasets if claiming generality.
- Ablation: static prompts, dynamic prompts, HSF, training data source, backbone.
- Figure: prompt variant embeddings/maps and qualitative maps.
