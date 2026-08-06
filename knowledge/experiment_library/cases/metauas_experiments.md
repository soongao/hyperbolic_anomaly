# MetaUAS Experiments

Source: [MetaUAS card](../../cards/gao-2025-metauas.md), text `../../text/gao-2025-metauas.txt`

## Experiment Claim

One-prompt meta-learning can produce a universal anomaly segmentation model that competes with zero-shot, few-shot, and full-shot methods.

## Main Experiment Package

- Benchmarks: MVTec, VisA, and Goods.
- Compares zero-shot CLIP/VLM methods, few-shot methods, and full-shot segmentation methods.
- Metrics:
  - image-level: ROC, PR, F1max;
  - pixel-level: ROC, PR, F1max, PRO.
- Includes complexity and efficiency comparison.
- Uses a broad ablation table for alignment, fusion, backbone learning, change type, decoder, and sample count.

## Tables And Figures

- Table 1: quantitative comparison on MVTec, VisA, and Goods.
- Figure 1: MetaUAS framework.
- Figure 2: synthetic image pairs for meta-learning.
- Figures 3-4: qualitative comparisons and normal-prompt examples.
- Table 2: complexity and efficiency.
- Table 3: ablation study on MVTec.
- Appendix Tables A1-A3: per-dataset detailed results.

## What Is Required To Borrow

If a new paper claims universal anomaly segmentation or one-prompt meta-learning:

- Compare across zero-shot, few-shot, and full-shot families, but mark the setting clearly.
- Report complexity and efficiency.
- Use PR/F1max in addition to ROC because anomaly segmentation is imbalanced.
- Ablate meta-learning data construction, feature alignment, decoder, and sample count.

## What Is Optional

- Goods-like extra benchmark is optional unless the paper claims universal multi-category deployment.
- Full-shot comparisons should be marked by setting, not mixed as equal competitors.

## Do Not Copy Blindly

Do not compare zero-shot and full-shot methods in one undifferentiated table. MetaUAS explicitly uses `Shot` and `Auxiliary` columns to avoid protocol confusion.

## Transfer Checklist

- Main table: method family and shot setting columns.
- Ablation: alignment, fusion, synthetic change type, decoder, sample count.
- Figure: qualitative maps with varied normal prompts.
