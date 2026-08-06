# FiLo Experiments

Source: [FiLo card](../../cards/gu-2024-filo.md), text `../../text/gu-2024-filo.txt`

## Experiment Claim

Fine-grained anomaly descriptions and high-quality localization improve zero-shot anomaly detection by making text prompts more defect-specific and localization more precise.

## Main Experiment Package

- Main ZSAD comparison on MVTec AD and VisA.
- Metrics include image-level AUC and pixel-level AUC.
- Baselines include CLIP, CLIP-AC, WinCLIP, APRIL-GAN, AnomalyCLIP, and FiLo.
- Ablations target anomaly descriptions, text templates, and HQ-Loc modules.
- Additional appendix tables provide subset-wise detection/localization results.

## Tables And Figures

- Table 1: main comparison on VisA and MVTec AD.
- Table 2: anomaly description ablation.
- Table 3: text template ablation.
- Table 4: HQ-Loc module ablation.
- Figure 1: comparison/motivation for detection and localization.
- Figure 2: overall architecture.
- Figure 3: qualitative visualization on MVTec and VisA.
- Figure 4: similarity between images and fine-grained anomaly descriptions.
- Tables 5-8: class-wise localization and detection performance.
- Additional appendix tables: backbone, resolution, and other implementation choices.

## What Is Required To Borrow

If a new paper uses LLM-generated descriptions or fine-grained text:

- Compare generic state words against fine-grained anomaly descriptions.
- Ablate text template design.
- Show image-region similarity to fine-grained descriptions.
- Include qualitative maps where fine-grained descriptions fix a baseline failure.
- Keep localization and classification metrics separate.

## What Is Optional

- Detailed per-class tables are appendix material.
- Extensive LLM prompt variants are optional unless LLM prompting is a core contribution.
- Backbone/resolution tables are optional unless the method depends on high-resolution localization.

## Do Not Copy Blindly

Do not add LLM descriptions unless you can show they affect localization or anomaly type discrimination. Otherwise the experiment reads as prompt decoration.

## Transfer Checklist

- Main table: MVTec AD and VisA comparison.
- Ablation: descriptions, templates, HQ-Loc modules.
- Figure: qualitative maps and description-region similarity.
