# PromptAD: Prompt Learning -> One-Class Contrast Construction

Source: [PromptAD card](../../cards/li-2024-promptad.md)

## Raw Technical Move

Learn prompts using only normal samples by creating anomaly prompts through semantic concatenation and enforcing an explicit anomaly margin.

## Naive Story

```text
We adapt prompt learning to few-shot anomaly detection.
```

## Paper Packaging

PromptAD packages the idea as `one-class prompt learning`: the core issue is not prompt learning itself, but how to create contrastive supervision when anomaly images are absent.

## Constructed Problem

The paper constructs a missing-negative problem:

- Prompt learning relies on contrastive learning.
- One-class anomaly detection has only normal samples during training.
- Without anomaly samples, there is no explicit margin between normal and abnormal prompt features.
- Therefore, anomaly semantics must be constructed in prompt space.

## Narrative Bridge

```text
Conventional prompt learning assumes multiple classes.
Few-shot anomaly detection is one-class.
The missing negative class can be synthesized semantically by transforming normal prompts into anomaly prompts.
An explicit margin then makes normal visual features closer to normal prompts than anomaly prompts.
```

## Naming Strategy

`semantic concatenation` turns appending anomaly suffixes into a conceptual operation: semantic transposition. `explicit anomaly margin` turns a loss term into the missing supervision signal.

## Reviewer-Facing Contribution

The reviewer sees a task-specific adaptation of prompt learning to the one-class constraint.

## Transfer Pattern

Use this when your method creates a missing supervision signal in representation space.

Reusable packaging:

```text
[Standard method] requires [missing supervision]. In [target setting], only [available signal] exists. We construct [surrogate contrast/reference] in [representation space] and regularize it with [explicit constraint].
```

## Risk Boundary

The surrogate negative must be validated. Otherwise it may look like arbitrary synthetic labels.

