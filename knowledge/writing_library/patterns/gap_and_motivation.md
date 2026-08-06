# Gap And Motivation

Use this file when moving from prior work to the need for a new method.

## Core Move

Start from a real prior strength, identify the exact mismatch, then connect it to a design choice.

Reusable pattern:

```text
Although [prior family] provides [capability], it remains limited for [target setting] because [mechanism] does not capture [required evidence]. Motivated by this mismatch, we [design choice].
```

## High-Value Gap Patterns

### Foundation Model Strength To Anomaly-Specific Mismatch

Sources: [AnomalyCLIP](../../cards/zhou-2024-anomalyclip.md), [WinCLIP](../../cards/jeong-2023-winclip.md)

Writing move:

```text
CLIP is strong at broad visual recognition, but anomaly detection requires normal/abnormal state discrimination and local evidence.
```

Reusable sentence:

```text
Although CLIP provides transferable image-text alignment, its object-level semantics are not sufficient for fine-grained anomaly recognition, where the decisive evidence is often a local deviation from normality.
```

Design bridge:

```text
This motivates learning or constructing anomaly-oriented prompts, anchors, or reference features that explicitly represent normality and abnormality.
```

### Prompt Engineering To Adaptive Prompting

Sources: [WinCLIP](../../cards/jeong-2023-winclip.md), [VCP-CLIP](../../cards/qu-2024-vcp-clip.md), [AdaCLIP](../../cards/yao-2024-adaclip.md)

Writing move:

```text
Manual prompts are useful but brittle; adaptive prompts reduce dependence on product-specific wording.
```

Reusable sentence:

```text
Manually designed text prompts can encode useful anomaly states, but their effectiveness depends on category-specific wording and may degrade when product appearance or defect semantics shift.
```

Design bridge:

```text
We therefore condition the prompt representation on [visual context/test image/auxiliary anomaly data] to make the normal-abnormal decision less dependent on fixed prompt templates.
```

### Text Prompts To Visual Or Frequency References

Sources: [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md), [VCP-CLIP](../../cards/qu-2024-vcp-clip.md)

Writing move:

```text
Spatial or language references miss subtle signal-level evidence.
```

Reusable sentence:

```text
Existing reference-based ZSAD methods mainly discriminate anomalies in spatial feature spaces, making subtle texture, boundary, and micro-structural changes hard to separate from normal appearance variation.
```

Design bridge:

```text
This motivates a frequency-aware representation that models anomaly evidence as band-dependent deviations rather than assuming all defects are dominated by high-frequency responses.
```

### Balanced Matching To Unbalanced Matching

Source: [Unbalanced OT](../../cards/chizat-2018-unbalancedoptimaltransport.md)

Writing move:

```text
Classical matching assumes equal mass; anomaly evidence is often partial, sparse, or unmatched.
```

Reusable sentence:

```text
A balanced matching objective can force every patch or token to be transported, even when anomaly evidence is partial and should be allowed to remain unmatched or receive different mass.
```

Design bridge:

```text
Relaxing the marginal constraints provides a natural way to compare normal and anomalous evidence under partial correspondence.
```

### Euclidean Geometry To Hyperbolic Geometry

Sources: [Poincare Embeddings](../../cards/nickel-2017-poincareembeddings.md), [Hyperbolic Entailment Cones](../../cards/ganea-2018-hyperbolicentailmentcones.md)

Writing move:

```text
Euclidean space under-represents hierarchy; hyperbolic space gives capacity for tree-like or scale-free structure.
```

Reusable sentence:

```text
When normal and anomalous patterns form hierarchical or scale-varying structures, Euclidean embeddings may require high dimensionality to preserve their relations, whereas hyperbolic geometry provides a compact space for tree-like organization.
```

Claim boundary:

```text
Use this only if the method actually models hierarchy, scale, entailment, or norm/radius structure.
```

## Motivation Bridge Bank

- `Motivated by this mismatch, we reformulate [task] as [new comparison/alignment/deviation problem].`
- `This observation suggests that [evidence type] should be modeled explicitly rather than treated as a by-product of [prior representation].`
- `The key idea is to replace [brittle assumption] with [adaptive/reference-relative/geometry-aware mechanism].`
- `Instead of asking CLIP to recognize object categories, we ask it to separate normality from abnormality under [constraint].`

## Avoid

- Do not say prior work "ignores" something unless the paper truly does.
- Do not motivate a module only by "improving performance"; state the failure mode it addresses.
- Do not call a gap "challenging" without naming the concrete source of difficulty.

