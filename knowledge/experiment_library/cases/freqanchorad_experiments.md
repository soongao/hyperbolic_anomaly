# FreqAnchorAD Experiments

Source: [FreqAnchorAD card](../../cards/qiu-2026-freqanchorad.md), text `../../text/qiu-2026-freqanchorad.txt`

## Experiment Claim

Language-free frequency-deviation anchoring improves ZSAD by representing anomaly evidence in a source-derived channel-spectral anchor space.

## Main Experiment Package

- Industrial benchmark sweep on MVTec AD, VisA, BTAD, KSDD2, DAGM, and DTD.
- Medical benchmark sweep with both classification and segmentation datasets.
- Metrics:
  - image-level: AUROC, F1-max, AP;
  - pixel-level: AUROC, F1-max, AP, AUPRO.
- Baselines include language-based and language-free methods, marked explicitly.
- Source-target protocol: VisA as source for non-VisA targets, MVTec AD as source for VisA.

## Tables And Figures

- Table 1: industrial benchmark comparison with language-free/language-based tags.
- Table 2: medical benchmark comparison.
- Table 3: core ablation of LFCM, FDAP, and AAS.
- Table 4: training-time soft canonicalization ablation.
- Table 5: bidirectional representation-space ablation, raw token -> LFCM -> plain MLP -> FDAP.
- Table 6: spectral organization ablation.
- Table 7: transform-basis ablation.
- Figure 1: motivation for frequency-aware anomaly deviation modeling.
- Figure 2: method overview.
- Figure 3: patch-score distributions across representation spaces.
- Figure 4: individual band removal analysis.

## What Is Required To Borrow

If a new paper claims frequency/wavelet/spectral anomaly evidence:

- Use multi-metric industrial main tables; AUROC alone is not enough.
- Include a strong spatial-only or plain-MLP replacement.
- Ablate the frequency transform basis, spectral layout, or band groups.
- Show whether low/mid/high bands contribute differently.
- Include a representation-space or score-distribution visualization.

## What Is Optional

- Medical-domain sweep is optional unless the paper claims language-free cross-domain generality.
- Every transform-basis variant can be appendix if frequency is not the main contribution.

## Do Not Copy Blindly

Do not claim "high-frequency anomaly" as a universal rule. FreqAnchorAD's stronger experimental story is multi-band deviation and anchor-relative scoring.

## Transfer Checklist

- Main table: industrial datasets with image and pixel metric blocks.
- Ablation: LFCM/frequency module, anchor projector, scoring rule, transform basis, band removal.
- Figure: score distributions and band contribution.
