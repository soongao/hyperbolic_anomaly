# Wavelet / Scattering: Frequency Module -> Multiscale Stable Evidence

Sources: [Group Invariant Scattering card](../../cards/mallat-2012-groupinvariantscattering.md), [Multi-Level Wavelet-CNN card](../../cards/liu-2018-multilevelwaveletcnn.md), [Synchrosqueezed Wavelet Transforms card](../../cards/daubechies-2011-synchrosqueezedwavelettransforms.md), [FcaNet card](../../cards/qin-2021-fcanet.md)

## Raw Technical Move

Apply wavelet, scattering, DCT, or frequency decomposition to image/features, then feed the decomposed coefficients into attention, reconstruction, matching, or anomaly scoring.

## Naive Story

```text
We add a wavelet/frequency branch to capture high-frequency defects.
```

This sounds like a feature-engineering add-on, and it is weak if the story is only "frequency is useful".

## Paper Packaging

The stronger packaging is `multiscale stable evidence`: wavelet-style transforms are not added because frequency sounds novel, but because they decompose local image evidence across scale and frequency while preserving spatially meaningful structure.

## Constructed Problem

The paper story can construct a representation-mismatch problem:

- Patch features in CLIP/CNN space often compress subtle texture, boundary, periodic, or scale-dependent changes.
- Pixel-space high-frequency heuristics are brittle because not every anomaly is simply high frequency.
- Wavelet and scattering transforms provide a structured multiresolution view instead of a single spatial or spectral cue.
- Therefore, anomaly evidence should be represented as scale-localized deviations rather than only semantic similarity.

## Narrative Bridge

```text
ZSAD methods usually score semantic or patch-level visual similarity.
However, many industrial defects are not new objects; they are small deviations in texture, edge continuity, periodicity, or local scale.
Pure spatial features may smooth these deviations, while pure spectral statistics lose locality.
We therefore introduce multiscale wavelet evidence that preserves local structure while exposing frequency-sensitive deviations.
```

## Naming Strategy

Avoid names like `wavelet module` or `frequency branch`. Better names bind the transform to the anomaly problem:

- `multiscale deviation evidence`
- `wavelet-localized anomaly cues`
- `scale-frequency anomaly anchors`
- `stable scattering evidence`
- `spectral-local defect representation`

## Reviewer-Facing Contribution

The reviewer is expected to see:

- a diagnosis: semantic CLIP features can miss non-semantic local defects;
- a mechanism: multiscale decomposition separates local deviation evidence by scale/frequency;
- a controlled role: the wavelet branch complements semantic matching rather than replacing it.

## Transfer Pattern

Use this when your raw idea adds wavelet, Fourier, DCT, scattering, local statistics, edge, texture, or multi-resolution features.

Reusable packaging:

```text
Prior methods rely on [single representation], which underrepresents [subtle/local/scale-dependent evidence]. We introduce [structured multiscale evidence] to expose [deviation type] while preserving [locality/stability/semantic compatibility].
```

## Risk Boundary

Do not claim "anomalies are high-frequency" unless experiments support it. Safer: anomalies may induce scale-frequency deviations, and wavelet features provide a structured way to expose them.

Also avoid presenting a fixed transform as universal novelty. The claim should be about the mismatch it solves in ZSAD and the evidence that the transform improves robustness, localization, or cross-category transfer.
