# PromptAD Experiments

Source: [PromptAD card](../../cards/li-2024-promptad.md), text `../../text/li-2024-promptad.txt`

## Experiment Claim

Prompt learning can work in few-shot anomaly detection with only normal samples if the method constructs anomaly-side prompt contrast through semantic concatenation and explicit anomaly margin.

## Main Experiment Package

- Few-shot normal-only evaluation on MVTec AD and VisA.
- Shot settings: 1-shot, 2-shot, and 4-shot.
- Metrics: image-level AUROC and pixel-level AUROC, with appendix AUPR/PRO.
- Baselines include SPADE, PaDiM, PatchCore, WinCLIP+, and prompt-learning baselines such as CoOp/CoCoOp/MaPLe variants.
- Additional MPDD and LOCO-style few-shot results appear in appendix.

## Tables And Figures

- Table 1: image-level AUROC comparison on MVTec and VisA across few-shot settings.
- Table 2: comparison with many-shot/full-shot methods on MVTec.
- Table 3: core ablation of PAD/VAD/SC/EAM components.
- Table 4: pixel-level AUROC comparison on MVTec and VisA.
- Table 5: different CLIP transformations.
- Figure 1: one-class prompt learning motivation.
- Figure 2: method overview.
- Figure 3: qualitative 1-shot pixel-level anomaly detection.
- Figure 4: effect of number of prompts/suffixes.
- Figure 5: lambda sensitivity.
- Figure 6: t-SNE visualization of prompt and visual features.
- Figure 7: manual anomaly suffix examples.
- Figures 8-10: additional qualitative results, logical anomaly, and tiny anomaly cases.
- Tables 11-18: subset-wise AUROC/AUPR/PRO details.

## What Is Required To Borrow

If a new paper claims few-shot normal-only prompt learning:

- Report 1/2/4-shot results with mean and standard deviation.
- Compare against strong normal-memory baselines and WinCLIP+.
- Include a prompt-learning baseline that fails under one-class constraints.
- Ablate constructed anomaly prompts and margin loss.
- Show t-SNE or prompt-feature visualization if claiming semantic separation.

## What Is Optional

- MPDD/LOCO transfer is optional unless the method claims broad few-shot robustness.
- Manual suffix lists should be appendix unless text construction is the central novelty.
- Many-shot comparison should be contextual, not the main fairness claim.

## Do Not Copy Blindly

Do not evaluate few-shot prompt learning without multiple seeds. The sampled normal images can strongly change results.

## Transfer Checklist

- Main table: MVTec/VisA 1/2/4-shot image and pixel AUROC.
- Ablation: semantic concatenation, manual/learnable anomaly prompts, explicit margin, visual memory.
- Figure: qualitative maps and t-SNE of prompt/visual features.
