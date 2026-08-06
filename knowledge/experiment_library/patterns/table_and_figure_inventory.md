# Table And Figure Inventory

## Common Main Tables

### Table A: Main Industrial Comparison

Purpose: prove baseline competitiveness.

Rows:

- CLIP / CLIP-AC.
- WinCLIP.
- APRIL-GAN.
- AnomalyCLIP / AdaCLIP / FiLo / VCP-CLIP depending on task.
- Proposed method.

Columns:

- Dataset groups: MVTec AD, VisA, MPDD, BTAD, etc.
- Image-level block: AUROC, AP/F1.
- Pixel-level block: AUROC, AP/F1, AUPRO.

### Table B: Cross-Domain Or Medical Comparison

Purpose: support object-agnostic, anomaly-aware, or language-free generalization.

Rows:

- Same ZSAD baselines as Table A.

Columns:

- Medical image-level datasets.
- Medical pixel-level datasets.
- Average rank if many datasets are used.

### Table C: Core Component Ablation

Purpose: prove each contribution is causal.

Rows:

- Full method.
- w/o module A.
- w/o module B.
- w/o module C.
- simple replacement for module A or B.

Columns:

- At least MVTec AD and VisA.
- At least one image metric and one pixel metric if both tasks are claimed.
- Delta relative to full method is useful.

### Table D: Prompt / Text Design Ablation

Purpose: validate prompt-related paper stories.

Rows:

- manual prompts;
- learnable prompts;
- object-aware vs object-agnostic;
- different state words;
- different templates;
- prompt length/depth.

### Table E: Efficiency / Resource Table

Purpose: make heavy models defensible.

Columns:

- Backbone.
- Input resolution.
- Trainable parameters.
- Inference time.
- GPU memory.
- Main metric.

## Common Figures

### Figure 1: Motivation / Failure Of Prior Methods

Purpose: show the problem before the method.

Common contents:

- CLIP or baseline anomaly maps fail.
- Object-specific prompts fail on unseen categories.
- Prompt choices produce unstable outputs.
- Spatial features miss subtle local defects.

### Figure 2: Method Pipeline

Purpose: make the technical contribution readable.

Common contents:

- frozen CLIP/VLM encoder;
- learnable prompts/adapters/context module;
- visual-text matching;
- anomaly map generation;
- losses or training stages.

### Figure 3: Qualitative Anomaly Maps

Purpose: show localization quality and failure boundaries.

Rows:

- input image;
- ground truth;
- strong baseline maps;
- proposed method map.

Columns:

- multiple categories and defect types across MVTec AD and VisA.

### Figure 4: Representation Or Attention Visualization

Purpose: support the mechanism.

Examples:

- t-SNE/PCA of text anchors or patch embeddings.
- attention maps before/after DPAM/V-V attention.
- patch-score distribution across representation spaces.
- similarity between fine-grained anomaly descriptions and image regions.

### Figure 5: Sensitivity / Hyperparameter Plot

Purpose: show stable design choices.

Examples:

- prompt length/depth;
- lambda/loss weight;
- top-K patches;
- number of clusters;
- input resolution;
- spectral band removal;
- hyperbolic curvature.

### Figure 6: Failure Cases

Purpose: define limits honestly.

Good failure types:

- logical anomalies;
- tiny defects;
- low-contrast texture shifts;
- irrelevant normal variation;
- over-detection around object edges;
- defects requiring normal reference comparison.
