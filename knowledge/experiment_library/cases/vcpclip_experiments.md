# VCP-CLIP Experiments

Source: [VCP-CLIP card](../../cards/qu-2024-vcp-clip.md), text `../../text/qu-2024-vcp-clip.txt`

## Experiment Claim

Visual context prompting improves zero-shot anomaly segmentation by deriving prompt context from the image when product categories or category-specific prompts are unreliable.

## Main Experiment Package

- Main segmentation comparison on MVTec AD and VisA.
- Extended evaluation on ten industrial anomaly segmentation datasets in the appendix.
- Metrics: pixel-level AUROC, PRO, and AP.
- Source-target protocol: train on VisA for non-VisA datasets, train on MVTec AD for VisA.
- Baselines include WinCLIP, AnVoL, CoCoOp, AnomalyGPT, APRIL-GAN, and a VCP-CLIP baseline.

## Tables And Figures

- Table 1: main comparison with pixel-level AUROC/PRO/AP on MVTec AD and VisA.
- Figure 5: qualitative segmentation results on MVTec AD and VisA.
- Figure 6: AP improvement over baseline per product.
- Figure 7: prompt robustness under train/test prompt changes.
- Table 2: ablation of different VCP components.
- Table 3: ablation of ensemble image layers.
- Table 4: text template and state-word ablation.
- Tables 5-6: input resolution and pretrained backbone ablations.
- Figure 8: deep text prompting ablation.
- Figure 9: hyperparameter ablations for prompt vector length/depth, fusion weight, and attention heads.
- Table 8: inference time and GPU memory.
- Figure 10: t-SNE visualization of output text embeddings.
- Table 10: image-level classification comparison.
- Tables 11-16 and Figures 11-33: per-product and extra-dataset details.

## What Is Required To Borrow

If a new paper claims visual context prompting or category-unavailable prompting:

- Include a strong segmentation table with AUROC/PRO/AP, not AUROC alone.
- Compare against a baseline that uses fixed or manually designed prompts.
- Add prompt transfer/robustness experiments where train and test templates differ.
- Add product-level AP analysis if the claim is about product/context variability.
- Include efficiency if the context module changes inference cost.

## What Is Optional

- Extra industrial datasets can be appendix unless broad industrial scalability is a main claim.
- Product-level tables are useful for diagnosis but too dense for the main paper.
- Image-level classification is optional if the paper is purely segmentation-focused.

## Do Not Copy Blindly

Do not claim category recognition unless the experiment measures category recovery. VCP-CLIP's evidence supports visual context as a prompt surrogate, not explicit category naming.

## Transfer Checklist

- Main table: MVTec AD and VisA with P-AUROC/P-PRO/P-AP.
- Ablation: Pre-VCP/Post-VCP, DTP, image-layer ensemble, prompt template/state words.
- Figure: product-level qualitative maps and AP improvement plot.
- Resource table: time and GPU memory if the module is dense.
