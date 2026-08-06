# Related Work Template

Use this to write concise related-work sections that position by mechanism.

## Section Opening

```text
We organize related work around [axis 1], [axis 2], and [axis 3], because these axes determine how methods obtain normal-abnormal evidence under limited target data.
```

## CLIP-Based ZSAD Paragraph

```text
CLIP-based ZSAD methods adapt image-text alignment to anomaly recognition and localization. WinCLIP uses compositional prompt ensembles and window-level features to define normal and anomalous states. AnomalyCLIP learns object-agnostic prompts for generic normality and abnormality. VCP-CLIP conditions prompts on visual context, while AdaCLIP introduces hybrid static and dynamic prompts. These methods show that prompt design is central to ZSAD, but they differ in whether anomaly references are manually designed, learned from auxiliary data, or conditioned on the test image.
```

## Frequency Or Signal Evidence Paragraph

```text
Frequency-aware methods complement spatial representations by modeling signal-level deviations. Instead of assuming that anomalies are always high-frequency responses, recent ZSAD work suggests that low-, mid-, and high-frequency components can provide complementary localization evidence. This motivates methods that organize spectral or channel-spectral responses relative to normal and anomaly anchors.
```

## TTA Paragraph

```text
Test-time adaptation updates model parameters, prompts, or normalization statistics using unlabeled test inputs. Tent adapts by entropy minimization on target data, MEMO uses augmentations to minimize marginal entropy for a single test point, and TPT tunes prompts with confidence-selected augmented views. These methods are relevant to ZSAD because they provide adaptation signals without target labels, but they introduce inference-time computation and must be distinguished from fixed zero-shot evaluation.
```

## OT/UOT Paragraph

```text
Optimal transport provides a principled way to compare distributions or sets of features. Entropic regularization makes OT scalable through Sinkhorn-style matrix scaling, while unbalanced OT relaxes exact marginal matching to handle mass variation and partial correspondence. This is relevant when anomaly evidence is sparse, unmatched, or only partially aligned between normal and abnormal feature sets.
```

## Hyperbolic Paragraph

```text
Hyperbolic representation learning replaces Euclidean geometry with negative-curvature spaces that compactly encode hierarchical or tree-like structure. Poincare embeddings and hyperbolic entailment cones show that hierarchy and asymmetric relations can be represented more naturally outside Euclidean space. For anomaly detection, this perspective is useful only when the method explicitly models scale, hierarchy, entailment, or category structure.
```

## Closing Positioning Paragraph

```text
In contrast to methods that [prior assumption], our work [main distinction]. This design targets [setting] where [constraint], and is evaluated through [evidence].
```

