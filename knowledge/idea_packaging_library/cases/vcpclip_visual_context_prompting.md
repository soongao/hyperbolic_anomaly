# VCP-CLIP: CoCoOp-Like Conditioning -> Visual Context Prompting

Source: [VCP-CLIP card](../../cards/qu-2024-vcp-clip.md)

## Raw Technical Move

Condition text prompts on image features and refine text embeddings with dense visual features. The core idea is close to visual-conditioned prompt learning, adapted to ZSAS with Pre-VCP and Post-VCP.

## Naive Story

```text
We use a CoCoOp-like prompt conditioned on the image, then add a cross-modal refinement module.
```

This sounds like applying a known prompt-learning trick.

## Paper Packaging

VCP-CLIP packages the method as `visual context prompting`: the model cannot rely on fixed product-specific prompts because the unseen product category may be unknown or hard to name, so the category/context should be inferred from the image itself.

## Constructed Problem

The paper constructs a missing-information problem:

- Existing CLIP-based ZSAS methods need text prompts.
- Product-specific prompts are hard to design for unseen products.
- The product category and context are available visually even when not available as reliable text.
- Therefore, visual context should be injected into the textual space.

## Narrative Bridge

```text
ZSAS needs product-aware prompts.
But unseen products do not provide reliable product-specific text.
The image already contains global and local context.
Therefore, use global visual context to form image-specific prompts and local visual context to refine text embeddings for segmentation.
```

## Naming Strategy

`visual context` makes the method sound like solving a semantic availability problem rather than simply conditioning a prompt. `Pre-VCP` and `Post-VCP` give the pipeline a before/after structure.

## Reviewer-Facing Contribution

The reviewer is expected to see:

- a practical ZSAS bottleneck: category-specific prompt design is unavailable or brittle;
- a conceptual fix: use the image as context for the prompt;
- a segmentation-specific extension: dense visual features refine text embeddings.

## Transfer Pattern

Use this when a prior method assumes a variable is provided explicitly, but the variable can be inferred from the input.

Reusable packaging:

```text
Prior methods require [explicit variable]. In [target setting], [explicit variable] is unavailable or unreliable. We therefore derive [surrogate representation] from [input signal] and use it to condition [model component].
```

## Risk Boundary

Do not claim the method "knows the category" unless you measure category recovery. Safer: it uses visual context as a surrogate for category-specific prompting.

