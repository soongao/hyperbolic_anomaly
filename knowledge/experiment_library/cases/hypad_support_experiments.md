# HypAD Support Experiments

Source: [HypAD card](../../cards/li-2024-hypad.md), text `../../text/li-2024-hypad.txt`

## Experiment Claim

Hyperbolic space can better represent hierarchical local-to-global structures in industrial anomaly detection than Euclidean feature space.

## Scope Warning

HypAD is not a core CLIP-ZSAD paper. Use it as a support case only when a new ZSAD idea borrows hyperbolic geometry or hierarchy-aware representation claims.

## Main Experiment Package

- Industrial anomaly localization on MVTec AD and VisA.
- Primary metric: pixel-level AUPRO.
- Additional metrics: image-level AUROC/AUPR and pixel-level AUROC/AUPR.
- Baselines are industrial AD methods rather than CLIP-ZSAD methods.
- Includes curvature sensitivity and qualitative maps.

## Tables And Figures

- Table 1: mean AUPRO comparison on MVTec AD and VisA.
- Tables 2-3: subset-wise pixel-level AUPRO for MVTec AD and VisA.
- Table 4: curvature parameter sensitivity.
- Table 5: image-level anomaly detection AUROC/AUPR.
- Table 7: pixel-level AUROC/AUPR comparison.
- Figures 1-2: motivation for hyperbolic representation.
- Figure 3: method architecture.
- Figure 4: hierarchical image relationship illustration.
- Figures 5-6: qualitative category visualizations.

## What Is Required To Borrow

If a new paper claims hyperbolic geometry helps ZSAD:

- Include Euclidean versus hyperbolic ablation.
- Sweep curvature or show sensitivity to curvature.
- Show a representation/hierarchy visualization, not only final performance.
- Use ZSAD baselines separately if the paper is CLIP-based.

## What Is Optional

- Industrial full-shot baselines are optional for a ZSAD paper and should be upper-bound context only.
- AUPRO-only reporting is insufficient for a CLIP-ZSAD paper; add AUROC/AP/F1.

## Do Not Copy Blindly

Do not use HypAD's metric package as the full experiment set for ZSAD. It lacks the zero-shot CLIP protocol and prompt/adapter baselines expected in ZSAD papers.

## Transfer Checklist

- Ablation: Euclidean vs hyperbolic, curvature, mapping module.
- Figure: hierarchy or embedding visualization.
- Main comparison: keep CLIP-ZSAD baselines if the new method is ZSAD.
