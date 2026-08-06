# Limitations And Future Work

Use this file for Discussion, Limitations, Conclusion, and reviewer response writing.

## Core Move

Name the failure condition, explain why it matters, and point to a concrete next step.

Reusable pattern:

```text
Although [method] improves [supported setting], it may fail when [condition] because [technical reason]. Addressing this case will require [future evidence/component/protocol].
```

## Source-Backed Limitation Patterns

### Logical Or Non-Structural Anomalies

Source: [AdaCLIP](../../cards/yao-2024-adaclip.md)

Reusable pattern:

```text
The method may fail on anomalies that lack clear structural deviations, where abnormality is defined by semantic or logical departure from the normal configuration rather than visible local defects.
```

Future direction:

```text
Future work can incorporate normal-reference reasoning, relational constraints, or object-layout priors to handle logical anomalies.
```

### Background Overlap And Noise

Source: [HADNet](../../cards/hadnet-2025-scientificreports.md)

Reusable pattern:

```text
Defects that overlap strongly with background texture or are obscured by noise can lead to inaccurate boundary detection.
```

Future direction:

```text
Future work can combine hierarchy-aware representations with more robust boundary modeling or noise-aware feature selection.
```

### Test-Time Adaptation Cost

Source: [TPT](../../cards/shu-2022-tpt.md)

Reusable pattern:

```text
Test-time prompt tuning avoids additional training data, but it introduces backpropagation and multiple augmented views during inference, increasing latency and memory cost.
```

Future direction:

```text
Future work can reduce the number of augmented views, cache prompt updates, or design representation-level losses with lower computational overhead.
```

### Entropy Objective Scope

Source: [Tent](../../cards/wang-2021-tent.md)

Reusable pattern:

```text
Entropy minimization is broadly applicable but limited in scope: it can require batches or carefully chosen parameters and may not handle all shifts.
```

Future direction:

```text
Future work can study losses that remain reliable for single-image, local, or representation-level adaptation.
```

### Frequency Evidence Is Complementary, Not Universal

Source: [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md)

Reusable pattern:

```text
No single frequency band consistently dominates anomaly localization; frequency cues should be treated as complementary evidence rather than a universal replacement for spatial semantics.
```

Future direction:

```text
Future work can learn data-dependent band weighting or combine spectral deviations with semantic and structural reasoning.
```

## Limitation Paragraph Template

```text
Limitations. The proposed method is designed for [setting] and is evaluated on [benchmarks]. Its main limitation appears when [failure condition]. In this case, [technical reason] weakens [module/assumption]. A natural next step is to [concrete extension] and evaluate it on [needed protocol or dataset].
```

## Good Verbs

- `may fail`
- `can degrade`
- `remains challenging`
- `requires further investigation`
- `suggests the need for`
- `points to`
- `leaves room for`

## Avoid

- Do not write limitations as vague humility: `there is still room for improvement`.
- Do not list limitations unrelated to the method.
- Do not promise a future method without naming the missing mechanism or evidence.

