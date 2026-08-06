# ZSAD Vocabulary

Use this file as a phrase bank. Prefer precise terms over inflated claims.

## Task And Setting

- `zero-shot anomaly detection`
- `zero-shot anomaly segmentation`
- `few-shot anomaly detection`
- `one-class anomaly detection`
- `source categories`
- `target categories`
- `unseen target domains`
- `auxiliary anomaly detection data`
- `target-domain training samples`
- `normal reference images`
- `image-level anomaly recognition`
- `pixel-level defect localization`
- `cross-dataset zero-shot testing`
- `industrial and medical benchmarks`

## Anomaly Evidence

- `normality and abnormality`
- `normal-abnormal discrimination`
- `anomaly-relevant regions`
- `fine-grained local deviations`
- `texture irregularities`
- `boundary discontinuities`
- `micro-structural defects`
- `logical anomalies`
- `structural deviations`
- `normal appearance variation`
- `reference-relative anomaly evidence`

## CLIP And Prompting

- `image-text alignment`
- `object-level semantics`
- `state words`
- `prompt templates`
- `compositional prompt ensemble`
- `object-agnostic prompts`
- `visual context prompting`
- `static prompts`
- `dynamic prompts`
- `hybrid prompts`
- `prompt tuning`
- `anomaly-aware text anchors`
- `textual anomaly references`
- `cross-modal alignment`

## Visual And Frequency Representation

- `patch-level features`
- `dense image embeddings`
- `multi-scale features`
- `intermediate patch tokens`
- `local spatial-frequency cues`
- `low-, mid-, and high-frequency deviations`
- `frequency-dependent anomaly evidence`
- `channel-spectral space`
- `source-derived channel coordinate`
- `anchor-relative discrimination`
- `band-dependent responses`

## TTA And Adaptation

- `test-time adaptation`
- `test-time prompt tuning`
- `entropy minimization`
- `marginal entropy`
- `confidence selection`
- `augmented views`
- `single test sample`
- `source-free adaptation`
- `online adaptation`
- `episodic adaptation`
- `feature modulation`

## Geometry And Transport

- `hyperbolic space`
- `negative curvature`
- `Poincare ball`
- `hierarchical representation`
- `tree-like structure`
- `entailment relation`
- `geodesically convex cones`
- `optimal transport`
- `entropic regularization`
- `Sinkhorn scaling`
- `unbalanced optimal transport`
- `relaxed marginal constraints`
- `partial correspondence`
- `mass variation`

## Useful Verbs

- `identify`
- `reveal`
- `formulate`
- `revisit`
- `construct`
- `align`
- `disentangle`
- `regularize`
- `calibrate`
- `condition`
- `aggregate`
- `localize`
- `stabilize`
- `preserve`
- `relax`
- `generalize`

## Transition Phrases

- `Motivated by this observation`
- `To address this mismatch`
- `In contrast to`
- `Rather than`
- `This suggests that`
- `Specifically`
- `As a result`
- `Under this setting`
- `The gains are most visible on`
- `This indicates that`
- `A natural next step is`

## Risky Phrases To Replace

| Risky phrase | Prefer |
|---|---|
| `without any data` | `without target-domain training samples` |
| `solves anomaly detection` | `improves anomaly detection under [protocol]` |
| `generalizes to arbitrary domains` | `generalizes across the evaluated domains` |
| `significantly better` | `improves [metric] by [number]` |
| `novel module` | `[module name], which [technical role]` |
| `robust` | `consistent across [splits/domains/perturbations]` |
| `simple yet effective` | `uses [specific small parameter/data/update budget] while improving [metric]` |

