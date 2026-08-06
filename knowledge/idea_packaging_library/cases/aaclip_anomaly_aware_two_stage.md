# AA-CLIP: Adapter Tuning -> Concept-First Anomaly Awareness

Source: [AA-CLIP card](../../cards/ma-2025-aa-clip.md)

## Raw Technical Move

Add lightweight residual adapters to CLIP's text and image encoders, train text first, then train visual patch features to align with adapted text anchors.

## Naive Story

```text
We fine-tune CLIP with adapters for anomaly detection.
```

This sounds like ordinary parameter-efficient fine-tuning.

## Paper Packaging

AA-CLIP packages the same kind of adaptation as solving `anomaly-unawareness`: CLIP first needs to learn abnormality as a concept in text space, and only then should patch-level visual features align to that anomaly-aware concept space.

## Constructed Problem

The paper constructs a semantic-entanglement problem:

- Original CLIP aligns category-level image and text semantics.
- Normal and abnormal text/texture features can overlap.
- Direct adaptation risks damaging CLIP's generalization.
- Therefore, adaptation should be controlled and staged.

## Narrative Bridge

```text
CLIP is not merely under-tuned; it is anomaly-unaware.
Anomaly awareness should first be established as separated normal/abnormal text anchors.
Once the semantic anchors are clear, patch-level visual features can be aligned to them.
Residual adapters make this controlled rather than destructive.
```

## Naming Strategy

`Anomaly-Aware CLIP` upgrades "adapter tuning" into "encoding missing awareness". `Disentangling text anchors` and `aligning patch features` create a cognitive sequence: learn the concept first, then ground it visually.

## Reviewer-Facing Contribution

The reviewer is expected to see:

- a diagnosis: CLIP is intrinsically anomaly-unaware;
- a mechanism: disentangle text anchors;
- a controlled adaptation story: residual adapters preserve class knowledge while adding anomaly discrimination.

## Transfer Pattern

Use this when your method uses adapters, LoRA, prompt tuning, projection layers, or other light fine-tuning.

Reusable packaging:

```text
Instead of treating adaptation as direct fine-tuning, we first establish [task concept] in [semantic/reference space], then align [visual/patch/source] representations to that task-aware space.
```

## Risk Boundary

This framing needs evidence that staged adaptation is better than one-stage adaptation or direct fine-tuning.

