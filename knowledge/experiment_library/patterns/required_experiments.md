# Required Experiments For ZSAD Papers

This file summarizes what reviewers usually expect from ZSAD and CLIP-based anomaly detection papers.

## P0: Must-Have Experiments

### 1. Main Comparison On Standard Benchmarks

Required when claiming ZSAD, ZSAS, or zero-shot anomaly detection.

Minimum package:

- Industrial benchmarks: at least MVTec AD and VisA.
- Metrics for image-level detection: AUROC plus AP/AUPR or F1-max.
- Metrics for pixel-level localization/segmentation: pixel-AUROC plus AP/F1-max and PRO/AUPRO when available.
- Baselines: CLIP-style baseline, WinCLIP, APRIL-GAN, AnomalyCLIP/AdaCLIP/FiLo/VCP-CLIP depending on publication time and task.

Why: this table proves the method is competitive under the standard protocol.

### 2. Protocol Fairness / Source-Target Separation

Required when the method uses auxiliary anomaly data, prompt learning, adapters, or trainable modules.

Minimum package:

- State clearly which dataset is used for training or auxiliary tuning.
- Use disjoint target evaluation, e.g. train on VisA for non-VisA targets and train on MVTec AD when evaluating VisA.
- Report zero-shot/few-shot/full-shot settings separately.
- Avoid silently using target test images as training data unless the protocol explicitly permits it.

Why: ZSAD claims collapse if target leakage is suspected.

### 3. Image-Level And Pixel-Level Results

Required when the paper claims both detection and localization.

Minimum package:

- Separate image-level and pixel-level blocks.
- Use consistent metric names with direction: `I-AUROC ↑`, `I-AP ↑`, `P-AUROC ↑`, `P-AP ↑`, `P-AUPRO ↑`.
- Do not mix classification-only and segmentation-only datasets in the same metric block without explaining missing metrics.

Why: good image-level classification can hide poor localization, and high pixel-AUROC can hide poor precision.

### 4. Core Module Ablation

Required for every named contribution.

Minimum package:

- Remove each proposed module.
- Replace important modules with simple alternatives.
- Report deltas relative to the full method.
- If two modules are coupled, include an interaction ablation.

Why: the ablation is what turns performance gains into causal evidence.

### 5. Qualitative Anomaly Maps

Required when the method outputs pixel-level maps.

Minimum package:

- Image, ground truth, key baselines, full method.
- Include both easy large defects and subtle/tiny defects.
- Show MVTec AD and VisA at minimum.
- Use same color scale if comparing anomaly maps.

Why: localization quality is visual; tables alone do not show over-detection, boundary errors, or missed tiny defects.

## P1: Strongly Recommended Experiments

### 6. Prompt / Text Robustness

Required if the method claims prompt robustness or prompt learning.

Typical variants:

- State words: `good/damaged`, `normal/abnormal`, `perfect/flawed`, etc.
- Template variants.
- Object-aware versus object-agnostic prompts.
- Prompt length and depth.
- Manual versus learnable prompts.

### 7. Cross-Dataset Generalization

Required if the story says "general", "category-agnostic", "language-free", "domain-transferable", or "source-free".

Typical package:

- Train/tune on one dataset, test on unseen datasets.
- Include MPDD, BTAD, KSDD/SDD/DAGM/DTD if claiming broad industrial transfer.
- Add medical datasets only if the paper claims cross-domain or clinical generalization.

### 8. Shot Curve

Required if the method uses normal references or few-shot adaptation.

Typical package:

- 0-shot, 1-shot, 2-shot, 4-shot.
- Report mean and standard deviation over multiple seeds.
- Compare with PatchCore, PaDiM, SPADE, WinCLIP+ or PromptAD depending on setting.

### 9. Representation Visualization

Recommended when the method claims semantic disentanglement, anomaly awareness, visual context, or frequency separation.

Typical figures:

- t-SNE/PCA of normal and abnormal embeddings.
- Text anchor visualization.
- Patch-score distribution.
- Attention map before/after module.

### 10. Efficiency / Resource Table

Required when the method adds heavy modules, high input resolution, SAM/LVLM, test-time optimization, or dense context modules.

Typical columns:

- Inference time.
- GPU memory.
- Trainable parameters.
- Backbone/resolution.

## P2: Optional / Appendix Experiments

- Full class-wise tables for every dataset and metric.
- Additional qualitative maps for every category.
- Failure case gallery.
- More hyperparameter sweeps.
- Alternative backbone sweeps.
- Full-shot method comparison as upper-bound context.

## Minimal Main-Paper Package

For a standard ZSAD paper, the main paper should usually contain:

1. Table 1: main industrial results on MVTec AD and VisA.
2. Table 2: broader generalization or medical/extra industrial results if claimed.
3. Table 3: core component ablation.
4. Figure 1: motivation or teaser.
5. Figure 2: method pipeline.
6. Figure 3: qualitative anomaly maps.
7. One small sensitivity or representation figure only if it supports the central claim.
