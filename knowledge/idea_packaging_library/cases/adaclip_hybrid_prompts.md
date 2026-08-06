# AdaCLIP: Static + Dynamic Prompts -> Hybrid Adaptation

Source: [AdaCLIP card](../../cards/yao-2024-adaclip.md)

## Raw Technical Move

Add static prompts and image-generated dynamic prompts to CLIP, including prompting layers for image and text encoders.

## Naive Story

```text
We combine CoOp-style static prompts and CoCoOp-style dynamic prompts for anomaly detection.
```

## Paper Packaging

AdaCLIP packages this as `hybrid learnable prompts`: static prompts capture shared anomaly knowledge from auxiliary data, while dynamic prompts adapt to each test image.

## Constructed Problem

The paper constructs an adaptation tradeoff:

- Auxiliary anomaly data contains reusable abnormal patterns.
- A single static prompt may be too rigid for diverse target distributions.
- A purely dynamic prompt may lack stable task knowledge.
- Therefore, static and dynamic prompts are complementary.

## Narrative Bridge

```text
ZSAD needs both stable task adaptation and flexible instance adaptation.
Static prompts provide the former.
Dynamic prompts provide the latter.
Their sum becomes a hybrid prompt that adapts CLIP without abandoning shared anomaly knowledge.
```

## Naming Strategy

`hybrid` is a useful packaging word when two simple components solve opposite sides of a tradeoff. It should be paired with a clear axis: shared vs instance-specific, stable vs flexible, global vs local.

## Reviewer-Facing Contribution

The reviewer sees a principled decomposition of adaptation rather than "we added more prompts".

## Transfer Pattern

Use this when your method has two variants of the same mechanism.

Reusable packaging:

```text
[Mechanism A] captures stable cross-sample structure, while [Mechanism B] responds to instance-specific variation. Their combination addresses the stability-adaptivity tradeoff in [task].
```

## Risk Boundary

You need ablations showing both components help and that the combination is better or meaningfully different.

