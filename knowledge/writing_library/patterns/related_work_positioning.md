# Related Work Positioning

Use this file when comparing a new idea against existing ZSAD and adjacent methods.

## Core Move

Compare methods by assumption, representation, supervision, and decision mechanism. Performance-only comparison belongs in Experiments, not Related Work.

Reusable pattern:

```text
Unlike [prior family], which [assumption or mechanism], our method [different mechanism] to address [target setting].
```

## Positioning Axes

### Prompt Source

Sources: [WinCLIP](../../cards/jeong-2023-winclip.md), [AnomalyCLIP](../../cards/zhou-2024-anomalyclip.md), [VCP-CLIP](../../cards/qu-2024-vcp-clip.md), [AdaCLIP](../../cards/yao-2024-adaclip.md)

Use this axis when the difference is how normal/anomaly text representations are built.

Reusable comparisons:

```text
WinCLIP constructs compositional prompt ensembles from state words and templates, while AnomalyCLIP learns object-agnostic prompts for generic normality and abnormality.
```

```text
VCP-CLIP conditions text prompts on visual context, shifting the prompt source from fixed category wording to image-dependent context.
```

```text
AdaCLIP combines static and dynamic learnable prompts, separating dataset-level adaptation from image-specific adaptation.
```

### Reference Source

Sources: [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md), [VCP-CLIP](../../cards/qu-2024-vcp-clip.md)

Use this axis when the method changes what evidence is compared: text prompts, visual anchors, normal references, frequency anchors, or patch distributions.

Reusable comparison:

```text
Reference-based ZSAD methods compare test samples with normal or abnormal references; the key distinction is whether those references are textual, visual, frequency-domain, or geometry-induced.
```

### Adaptation Time

Sources: [Tent](../../cards/wang-2021-tent.md), [MEMO](../../cards/zhang-2022-memo.md), [TPT](../../cards/shu-2022-tpt.md)

Use this axis when borrowing TTA into ZSAD.

Reusable comparison:

```text
Test-time adaptation methods update the model or prompts using unlabeled test inputs, whereas standard ZSAD methods usually keep the trained detector fixed during evaluation.
```

Boundary:

```text
If your method uses TTA, report the extra inference cost and specify whether adaptation is episodic, online, or batch-based.
```

### Representation Space

Sources: [Poincare Embeddings](../../cards/nickel-2017-poincareembeddings.md), [Hyperbolic Entailment Cones](../../cards/ganea-2018-hyperbolicentailmentcones.md), [HADNet](../../cards/hadnet-2025-scientificreports.md)

Use this axis when the method changes geometry.

Reusable comparison:

```text
Euclidean feature spaces primarily encode similarity through symmetric distances, while hyperbolic spaces can compactly represent hierarchical or tree-like structure through negative curvature.
```

Boundary:

```text
Do not introduce hyperbolic space as decoration. Tie it to hierarchy, scale, entailment, or feature organization.
```

### Matching Constraint

Sources: [Sinkhorn Distances](../../cards/cuturi-2013-sinkhorndistances.md), [Unbalanced OT](../../cards/chizat-2018-unbalancedoptimaltransport.md)

Use this axis when comparing patch distributions, normal/anomaly token sets, or source-target feature sets.

Reusable comparison:

```text
Balanced OT enforces exact marginal matching, while unbalanced OT relaxes this constraint to handle mass variation, partial correspondence, or unmatched evidence.
```

## Related Work Paragraph Template

```text
[Family] has improved [task] by [main mechanism]. Representative methods include [method A] and [method B], which [specific mechanisms]. However, these methods generally assume [shared assumption], making it difficult to [gap]. In contrast, our method [mechanism], targeting [setting] without [unavailable data/assumption].
```

## Avoid

- Do not write `different from previous methods` without naming the axis of difference.
- Do not use `more robust` or `better generalization` in Related Work unless you explain why mechanistically.
- Do not collapse zero-shot, few-shot, one-class, source-free, and test-time adaptation into one setting.

