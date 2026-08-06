# FreqAnchorAD: Frequency Modules -> Frequency-Deviation Anchoring

Source: [FreqAnchorAD card](../../cards/qiu-2026-freqanchorad.md)

## Raw Technical Move

Enhance patch tokens with local frequency cues, reorder channels using source statistics, apply spectral projection, and compare representations to normal/anomaly anchors with asymmetric supervision.

## Naive Story

```text
We add frequency-domain features and anchors to ZSAD.
```

## Paper Packaging

FreqAnchorAD packages the method as `frequency-deviation anchoring`: the point is not simply adding frequency, but modeling anomaly evidence as deviations across multiple frequency bands relative to normal/anomaly anchors.

## Constructed Problem

The paper constructs a signal-evidence problem:

- Existing reference-based ZSAD mainly uses spatial features or textual references.
- Subtle texture, boundary, and micro-structural defects can be hard to distinguish in spatial space.
- Local anomalies are not universally high-frequency; low, mid, and high bands can each dominate.
- Therefore, frequency evidence needs structured multi-band modeling.

## Narrative Bridge

```text
Spatial features underuse signal-level deviations.
Anomaly frequency responses are multi-band, not only high-frequency.
A stable source-derived channel coordinate makes spectral comparison meaningful.
Therefore, project frequency-enhanced tokens into a channel-spectral anchor space and score relative to normal/anomaly anchors.
```

## Naming Strategy

`frequency-deviation` avoids the weak name "frequency feature". `anchor` connects the representation to a decision rule. `source-derived channel-spectral space` makes a technical preprocessing step sound necessary rather than incidental.

## Reviewer-Facing Contribution

The reviewer sees:

- an empirical observation;
- a representational correction;
- a structured anchor-based discrimination mechanism.

## Transfer Pattern

Use this when your idea adds another evidence domain.

Reusable packaging:

```text
Prior methods assume [dominant evidence space]. We show that [target signal] is distributed across [multiple evidence modes]. We therefore organize [representation] into [structured coordinate/anchor space] for [relative discrimination].
```

## Risk Boundary

You need evidence that the new domain captures information not already captured by the baseline.

