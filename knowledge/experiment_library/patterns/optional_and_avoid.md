# Optional And Avoided Experiments

Use this file to keep the experiment section focused.

## Usually Optional

### Medical Domain Evaluation

Do it when:

- the paper claims cross-domain generalization;
- the method is object/category agnostic;
- the method is language-free and should not depend on industrial object names;
- the paper wants to show transfer from industrial to medical anomaly patterns.

Skip or appendix it when:

- the method is explicitly industrial-only;
- there is no clean protocol for target-domain training;
- the results would distract from the main ZSAD claim.

### Full-Shot Industrial AD Comparison

Use as:

- an upper-bound context;
- a sanity check against mature full-shot AD methods.

Do not use as:

- the main fair comparison table for zero-shot claims.

### Exhaustive Per-Class Tables

Use in appendix when:

- the benchmark has many categories;
- the main result is averaged;
- reviewers may ask whether gains come from a few categories.

Keep out of main paper unless:

- the method specifically targets category-level variation.

### Many Hyperparameter Sweeps

Use in appendix for:

- prompt length/depth;
- loss weights;
- number of clusters;
- top-K patches;
- spectral layout;
- curvature.

Only keep in main paper if:

- the hyperparameter is central to the method story.

## Experiments To Avoid

### 1. AUROC-Only Segmentation Evidence

Avoid reporting only pixel-AUROC for localization. Pixel-AUROC can look high under severe class imbalance. Add AP/F1-max and PRO/AUPRO when possible.

### 2. Unfair Full-Shot Baseline Framing

Do not claim to beat full-shot methods unless the training protocol is comparable. It is acceptable to say the result is competitive under a stricter zero-shot or auxiliary-data protocol.

### 3. Prompt Robustness Without A Prompt Claim

If the method is not text-prompt sensitive, do not spend main-paper space on many word/template variants.

### 4. Medical Dataset Sweep Without A Story

Medical evaluation is useful for object-agnostic or modality-transfer claims. It is weak if added only to inflate dataset count.

### 5. Component Ablation That Does Not Match Contributions

Do not ablate random implementation details while ignoring named modules in the method section.

### 6. Qualitative Figures With Only Easy Cases

Avoid showing only obvious defects. Include tiny, low-contrast, logical, or over-detection-prone cases.

### 7. Source-Target Leakage

Avoid any experiment where target test images, labels, masks, or category-specific target statistics are used without an explicit protocol. If test-time adaptation is used, state exactly what signal is allowed.

## Reviewer Attack Questions

- Are the baselines current and protocol-matched?
- Does every paper claim have a corresponding table or figure?
- Does the ablation isolate the named contribution?
- Are the metrics sufficient for anomaly imbalance?
- Is there hidden target data usage?
- Does the qualitative figure show failure modes or only cherry-picked cases?
