# Claim Boundaries

Use this file before finalizing Abstract, Introduction, Conclusion, and contribution bullets.

## Core Rule

Every strong claim needs a setting, data condition, and evidence boundary.

Reusable pattern:

```text
Under [protocol] on [benchmarks], [method] achieves [claim]. This does not imply [stronger unevaluated claim].
```

## Common Boundaries For ZSAD

### Data Boundary

Use:

```text
without target-domain training samples
```

Not:

```text
without training data
```

Reason: Many ZSAD methods use auxiliary anomaly data, pretrained CLIP, source categories, or generated prompts.

### Supervision Boundary

Use:

```text
trained on auxiliary annotated anomaly detection data
```

when the method uses image- or pixel-level anomaly labels outside the target domain.

Use:

```text
training-free at the target domain
```

only if no target-domain optimization is used.

### Inference Boundary

Use:

```text
without test-time adaptation
```

only when the model is fixed during evaluation.

Use:

```text
with one-step test-time prompt tuning
```

when using TPT-like adaptation.

### Generalization Boundary

Use:

```text
across the evaluated industrial and medical benchmarks
```

Not:

```text
across arbitrary real-world domains
```

unless that broader claim is directly tested.

### Language-Free Boundary

Source: [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md)

Use:

```text
language-free
```

only when the method does not use text encoders, text prompts, or cross-modal alignment at inference/training for the anomaly decision.

### "First" Claim Checklist

Before writing `first`, verify:

1. Same task setting.
2. Same supervision protocol.
3. Same data availability.
4. Same method category.
5. Same publication timeline.

Safer alternatives:

- `to our knowledge`
- `we revisit`
- `we provide evidence that`
- `we identify`
- `we take a step toward`

## Reviewer-Safe Phrase Bank

- `within the evaluated protocol`
- `under the zero-shot setting`
- `when no target-domain training images are available`
- `on the evaluated benchmarks`
- `relative to the selected baselines`
- `suggesting that`
- `indicating that`
- `consistent with`
- `we observe`
- `this does not require`
- `this does not assume`

## Boundary Examples

```text
Strong: The method achieves state-of-the-art ZSAD performance.
Safer: The method achieves the best mean performance among the compared ZSAD baselines on the evaluated industrial benchmarks.
```

```text
Strong: The model detects arbitrary logical anomalies.
Safer: The model improves localization for the evaluated defect types, while logical anomalies without structural deviations remain challenging.
```

```text
Strong: Hyperbolic space solves anomaly hierarchy.
Safer: Hyperbolic space provides a compact geometry for representing hierarchical or scale-varying defect structure, which we evaluate through [experiment].
```

