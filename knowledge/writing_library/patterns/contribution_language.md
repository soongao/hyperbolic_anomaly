# Contribution Language

Use this file for contribution bullets, Abstract endings, and Introduction summary paragraphs.

## Core Move

Each contribution should combine action, mechanism, scope, and evidence.

Reusable pattern:

```text
We [reveal/propose/design/introduce/validate] [object], which [mechanism/effect] under [setting], as supported by [evidence].
```

## Contribution Types

### Insight Contribution

Sources: [AnomalyCLIP](../../cards/zhou-2024-anomalyclip.md), [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md), [AA-CLIP](../../cards/ma-2025-aa-clip.md)

Reusable patterns:

```text
We identify [failure mode] as a key bottleneck for [task], showing that [prior representation] is misaligned with [required evidence].
```

```text
We provide an empirical analysis showing that [phenomenon] is [multi-band/object-agnostic/generalizable], motivating [method family].
```

Use for:

- `object semantics vs abnormality/normality`
- `CLIP anomaly-unawareness`
- `frequency-dependent deviation across low/mid/high bands`

### Method Contribution

Sources: [VCP-CLIP](../../cards/qu-2024-vcp-clip.md), [AdaCLIP](../../cards/yao-2024-adaclip.md), [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md)

Reusable patterns:

```text
We propose [method], a [setting-aware] framework that integrates [module A], [module B], and [module C] for [target decision].
```

```text
We design [module] to [local function], enabling [global method-level benefit].
```

Good verbs:

- `introduce` for a new framework or module.
- `design` for a component with a clear function.
- `construct` for anchors, prompts, references, or coordinate systems.
- `regularize` for losses and training constraints.
- `organize` for representation spaces and channel/frequency coordinates.

### Evidence Contribution

Sources: [AnomalyCLIP](../../cards/zhou-2024-anomalyclip.md), [AdaCLIP](../../cards/yao-2024-adaclip.md), [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md), [AA-CLIP](../../cards/ma-2025-aa-clip.md)

Reusable patterns:

```text
Extensive experiments on [number] [industrial/medical/cross-domain] benchmarks demonstrate [claim], with ablations confirming the role of [module].
```

```text
We validate [method] under [protocol], showing [metric-level effect] and [qualitative behavior].
```

Claim boundary:

```text
Only write "state-of-the-art" if the tables support it under the same protocol. Otherwise use "competitive", "consistent gains", or "improves over selected baselines".
```

### Efficiency Or Resource Contribution

Sources: [AA-CLIP](../../cards/ma-2025-aa-clip.md), [Tent](../../cards/wang-2021-tent.md), [TPT](../../cards/shu-2022-tpt.md)

Reusable patterns:

```text
The proposed adaptation uses [limited parameter group/data level/update step], preserving [pretrained knowledge/generalization] while adding [task-specific capability].
```

```text
The method adapts at [training/test] time using only [available signal], avoiding [source data/annotations/full-model fine-tuning].
```

## Contribution Bullet Template

```text
Our contributions are summarized as follows:

1. We identify [specific bottleneck] in [prior family] for [setting], and show that [evidence/analysis] motivates [new viewpoint].
2. We propose [method name], which [core mechanism] by combining [module A] and [module B] under [constraint].
3. We design [objective/module] to [local technical role], improving [specific capability] without [cost/assumption].
4. Experiments on [benchmarks] demonstrate [supported result], and ablations verify [module/effect].
```

## Strong But Safer Alternatives

- Instead of `solves ZSAD`, write `improves ZSAD under [protocol]`.
- Instead of `generalizes to all domains`, write `generalizes across the evaluated industrial and medical benchmarks`.
- Instead of `requires no data`, write `requires no target-domain training data`.
- Instead of `simple yet effective`, write the actual reason: `uses only two class-level prompts`, `updates only prompt parameters`, or `freezes the vision encoder`.

