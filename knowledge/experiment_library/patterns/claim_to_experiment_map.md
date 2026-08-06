# Claim To Experiment Map

Use this file to translate a paper claim into required experiments.

## Claim: Better Zero-Shot Anomaly Detection

Must do:

- Main comparison on MVTec AD and VisA.
- Image-level and pixel-level metrics if both tasks are claimed.
- Compare with current CLIP-ZSAD baselines.
- Qualitative anomaly maps.

Usually skip:

- Medical benchmarks unless claiming cross-domain generalization.
- Full-shot baselines in the main fair comparison table.

## Claim: Object-Agnostic Or Category-Agnostic Transfer

Must do:

- Object-aware versus object-agnostic ablation.
- Cross-dataset transfer with disjoint categories.
- Per-dataset results beyond MVTec/VisA if claiming broad generality.

Good figures:

- performance gain plot by dataset/category;
- qualitative maps on unseen object categories.

Nearest case: AnomalyCLIP.

## Claim: Visual Context Solves Unknown Category/Prompt

Must do:

- Fixed prompt baseline versus visual-context prompt.
- Prompt template/state-word robustness.
- Product-level AP or category-level analysis.
- Segmentation metrics including AP and PRO.

Good figures:

- qualitative maps;
- output text embedding visualization;
- per-product improvement plot.

Nearest case: VCP-CLIP.

## Claim: Adapter/Fine-Tuning Adds Anomaly Awareness

Must do:

- Frozen CLIP baseline.
- Adapter/no-adapter ablation.
- One-stage versus staged training.
- Representation visualization of text/patch separation.

Good figures:

- t-SNE/PCA of text anchors or patch embeddings;
- anomaly maps before/after alignment.

Nearest case: AA-CLIP.

## Claim: Hybrid Prompts Are Necessary

Must do:

- no prompt / static-only / dynamic-only / hybrid.
- Prompt length/depth sensitivity.
- Prompt effect visualization.

Good figures:

- patch embedding visualization under each prompt variant;
- anomaly maps under each prompt variant.

Nearest case: AdaCLIP.

## Claim: Fine-Grained Text Descriptions Help

Must do:

- generic state words versus fine-grained anomaly descriptions.
- text template ablation.
- description-region similarity visualization.

Good figures:

- similarity between image regions and anomaly descriptions;
- qualitative maps where generic prompts fail.

Nearest case: FiLo.

## Claim: Few-Shot Normal-Only Prompt Learning

Must do:

- 1/2/4-shot tables.
- mean/std over random seeds.
- compare with normal-memory methods and WinCLIP+.
- ablate anomaly prompt construction and margin.

Good figures:

- t-SNE of normal/anomaly prompt features;
- qualitative maps for logical/tiny defects.

Nearest case: PromptAD.

## Claim: Frequency/Wavelet/Spectral Evidence

Must do:

- spatial-only or plain-MLP replacement.
- transform basis or spectral layout ablation.
- low/mid/high band contribution if using bands.
- score distribution or representation-space visualization.

Good figures:

- band removal plot;
- score distributions before/after spectral module.

Nearest case: FreqAnchorAD.

## Claim: SAM/LVLM Candidate Filtering

Must do:

- vanilla foundation-model assembly baseline.
- prompt/filter component ablation.
- region-level and pixel-level segmentation metrics.
- qualitative over-detection examples.

Good figures:

- candidate masks before/after filtering.

Nearest cases: SAA+, AnomalyGPT, MetaUAS.

## Claim: Test-Time Adaptation Helps ZSAD

Must do:

- no-adaptation baseline;
- test-time augmentation without parameter updates;
- adapted parameter-group ablation;
- confidence selection/filtering ablation if used;
- runtime, augmented-view count, and update-step reporting;
- strict statement of what data is visible at test time.

Good figures:

- test-time adaptation pipeline;
- efficiency-performance tradeoff curve;
- anomaly maps before/after adaptation.

Nearest case: TPT / TTA support case.

## Claim: Hyperbolic Geometry Helps

Must do:

- Euclidean versus hyperbolic ablation.
- curvature sensitivity.
- representation or hierarchy visualization.
- CLIP-ZSAD baselines if the method is CLIP-based.

Good figures:

- hierarchy/embedding visualization;
- curvature sensitivity table or plot.

Nearest case: HypAD support case.

## Claim: Partial Matching Or UOT Helps

Must do:

- compare balanced matching versus relaxed/unbalanced matching;
- ablate the mass/relaxation coefficient;
- show unmatched or down-weighted evidence qualitatively;
- report stability under missing, noisy, or partial correspondences.

Good figures:

- transport/matching plan visualization;
- patch-to-prototype correspondence before/after relaxation.

Nearest source papers: UOT/Sinkhorn/OT cards; no dedicated ZSAD case yet.
