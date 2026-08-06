# Naming Strategies

Good names encode the problem and the mechanism. They should not merely rename a module.

## Name Formula

```text
[missing/incorrect assumption] + [mechanism] + [target evidence]
```

Examples:

- `object-agnostic prompt learning`: removes object semantics, uses prompt learning.
- `visual context prompting`: uses visual context to solve prompt uncertainty.
- `anomaly-aware CLIP`: adds missing anomaly concept.
- `frequency-deviation anchoring`: models deviation in frequency space using anchors.
- `multiscale stable evidence`: turns a wavelet/frequency branch into a representation-mismatch fix.
- `one-class prompt learning`: adapts prompt learning to one-class constraints.

## Naming Moves

### A. Agnostic Names

Use when removing a nuisance variable.

Pattern:

```text
[variable]-agnostic [representation/mechanism]
```

Examples:

- object-agnostic prompts
- category-agnostic abnormality modeling
- domain-agnostic normality anchors

Risk: if the method still depends on the variable, this name will backfire.

### B. Aware Names

Use when adding a missing concept.

Pattern:

```text
[concept]-aware [model/space/feature]
```

Examples:

- anomaly-aware CLIP
- boundary-aware localization
- normality-aware alignment

Risk: needs evidence that the concept is better represented, not only performance improved.

### C. Context Names

Use when deriving information from the input.

Pattern:

```text
[source] context [prompting/adaptation/alignment]
```

Examples:

- visual context prompting
- test-instance context adaptation
- reference-context calibration

Risk: avoid implying semantic understanding if only low-level conditioning is shown.

### D. Hybrid Names

Use when combining complementary mechanisms.

Pattern:

```text
hybrid [mechanism]
```

Must define the axis:

- static + dynamic
- global + local
- semantic + visual
- spatial + frequency

Risk: "hybrid" is weak unless the components have distinct roles.

### E. Deviation Names

Use when modeling difference from normality.

Pattern:

```text
[space]-deviation [scoring/anchoring/modeling]
```

Examples:

- frequency-deviation anchoring
- normality-deviation scoring
- channel-deviation projection
- multiscale deviation evidence
- wavelet-localized anomaly cues

Risk: must define the reference and deviation space.

### F. Relaxed/Unbalanced Names

Use when relaxing a constraint.

Pattern:

```text
[constraint]-relaxed [matching/alignment]
```

Examples:

- mass-relaxed patch matching
- unbalanced normality transport
- partial evidence alignment

Risk: must explain what the relaxed constraint means in the task.
