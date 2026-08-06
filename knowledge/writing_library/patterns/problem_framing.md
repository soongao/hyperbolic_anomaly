# Problem Framing

Use this file when opening an Abstract, Introduction, or Problem Setting section.

## Core Move

Define the task through its operational constraint, then name the source of difficulty.

Reusable pattern:

```text
[Task] aims to [decision/output] in [target setting] without [unavailable supervision/data], where the main difficulty is [variation or mismatch].
```

For ZSAD, the constraint is usually not "no training" in general; it is no target-domain training samples, often with auxiliary source data.

## Source-Backed Patterns

### ZSAD As Target-Data Absence

Source: [AnomalyCLIP](../../cards/zhou-2024-anomalyclip.md)

Writing move: define the task by unavailable target samples and cross-domain variation.

Reusable pattern:

```text
Zero-shot anomaly detection requires a model trained with [auxiliary/source data] to detect and localize anomalies in [target domains] without target-domain training samples.
```

Claim boundary:

```text
Use "without target-domain training samples"; do not write "without training" if the method uses auxiliary training data.
```

### ZSAS As Novel-Product Segmentation

Source: [VCP-CLIP](../../cards/qu-2024-vcp-clip.md)

Writing move: define segmentation by novel products and lack of pre-customized data.

Reusable pattern:

```text
Zero-shot anomaly segmentation aims to localize anomalous regions in novel products without pre-customized training data for those products.
```

Good follow-up:

```text
This setting requires generalization across product appearance, defect type, and background structure.
```

### Frequency-Aware ZSAD As Deviation Modeling

Source: [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md)

Writing move: define anomalies as deviations from normal patterns, then broaden the evidence space.

Reusable pattern:

```text
Anomaly detection can be framed as identifying deviations from normal patterns; in ZSAD, the challenge is to make this deviation signal transferable to unseen target domains.
```

Use when:

```text
The proposed method relies on signal-level, frequency-domain, or reference-relative evidence rather than language prompts.
```

### Few-Shot AD As One-Class Prompt Learning

Source: [PromptAD](../../cards/li-2024-promptad.md)

Writing move: introduce few-shot AD through the one-class constraint.

Reusable pattern:

```text
Few-shot anomaly detection in industrial inspection is often a one-class problem: only a small number of normal samples are available during training, while the model must identify anomalous samples at test time.
```

Claim boundary:

```text
Use "few-shot" only when target normal references are available; use "zero-shot" when no target training/reference samples are used.
```

### UOT As Relaxing A Classical Assumption

Source: [Scaling Algorithms for Unbalanced Optimal Transport Problems](../../cards/chizat-2018-unbalancedoptimaltransport.md)

Writing move: define a mathematical tool by the assumption it relaxes.

Reusable pattern:

```text
Classical [method] assumes [balanced/normalized condition], which becomes restrictive when [real data violates condition]. A relaxed formulation is needed to handle [missing, extra, or partial structure].
```

Use for ZSAD:

```text
Use this pattern when motivating unbalanced matching between normal and anomalous evidence, patch distributions, or source-target feature sets.
```

## Opening Sentence Bank

- `Zero-shot anomaly detection targets anomaly recognition and localization in unseen categories without target-domain training samples.`
- `Industrial anomaly detection becomes operationally difficult when each new product line lacks sufficient normal or defective training examples.`
- `A practical ZSAD model must transfer abnormality cues across object categories, visual domains, and defect scales.`
- `In this setting, the central challenge is not only recognizing object semantics, but separating generic normality from abnormality.`

## Avoid

- `Anomaly detection is very important in many fields.` Too generic.
- `ZSAD detects anomalies without any data.` Usually false if auxiliary data or pretrained models are used.
- `The model generalizes to all domains.` Use evaluated domains and protocols.

