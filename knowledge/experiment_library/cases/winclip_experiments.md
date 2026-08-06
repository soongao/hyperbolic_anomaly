# WinCLIP Experiments

Source: [WinCLIP card](../../cards/jeong-2023-winclip.md), text `../../text/jeong-2023-winclip.txt`

## Experiment Claim

CLIP can perform zero-/few-shot anomaly classification and segmentation when prompts define anomaly states and windowed features provide local evidence.

## Main Experiment Package

- Zero-shot anomaly classification and segmentation on MVTec AD and VisA.
- Few-normal-shot variants, usually 1/2/4-shot, with mean and standard deviation over random seeds.
- Image-level metrics: AUROC, AUPR, F1-max.
- Pixel-level metrics: pAUROC, PRO, F1-max.
- Baselines include SPADE, PaDiM, PatchCore, and other zero-/few-shot methods.

## Tables And Figures

- Table 1: anomaly classification comparison on MVTec AD and VisA.
- Table 2: comparison with existing many-shot methods on MVTec AD.
- Table 3: ablation of WinCLIP components for classification.
- Table 4: anomaly segmentation comparison on MVTec AD and VisA.
- Tables 5-6: k-shot classification and segmentation ablations.
- Table 7: specific state-word ablation.
- Table 8: segmentation performance and runtime-style analysis.
- Figure 5: qualitative 1-shot segmentation comparison.
- Supplement Figure 6: prompt list.
- Supplement Figures 7-10: additional qualitative maps.
- Supplement Figure 11: curated failure cases.
- Supplement Tables 10-21: class-wise AUROC/AUPR/F1/PRO details.

## What Is Required To Borrow

If a new paper claims zero-/few-shot performance:

- Separate zero-shot and few-shot protocols.
- Report mean and standard deviation for few-shot settings.
- Use both MVTec AD and VisA.
- Report classification and segmentation metrics separately.
- Include qualitative maps and at least one failure-case discussion.

## What Is Optional

- Class-wise tables for every metric are useful in appendix, not main paper.
- Detailed prompt lists are useful when prompt design is a contribution.
- Many-shot comparison should be used as context, not as the central fairness claim.

## Do Not Copy Blindly

Do not use WinCLIP's object-name prompt setup if your method claims object-agnostic prompting. That would contradict the story.

## Transfer Checklist

- Main table: zero-shot classification and segmentation.
- Few-shot table: 1/2/4-shot with mean/std.
- Ablation: state words, templates, window/multiscale local features.
- Figure: anomaly maps plus failure cases for logical and tiny defects.
