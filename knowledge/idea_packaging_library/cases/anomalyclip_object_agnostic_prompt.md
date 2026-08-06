# AnomalyCLIP: Prompt Learning -> Object-Agnostic Abnormality

Source: [AnomalyCLIP card](../../cards/zhou-2024-anomalyclip.md)

## Raw Technical Move

Learn two normal/abnormal text prompts using auxiliary anomaly data, with global and local losses.

## Naive Story

```text
We do prompt learning for the normal and abnormal classes.
```

This sounds incremental because prompt learning already exists, and normal/abnormal labels are the obvious two classes in anomaly detection.

## Paper Packaging

AnomalyCLIP reframes the move as `object-agnostic prompt learning`: the key is not merely learning prompts, but removing the object category from the prompt and learning generic normality/abnormality.

## Constructed Problem

The paper constructs the problem as a mismatch between CLIP's object semantics and ZSAD's abnormality semantics:

- CLIP is strong at object-level image-text alignment.
- ZSAD needs transfer across unseen foreground objects.
- Object names in prompts may become noisy because anomaly patterns can transfer while object semantics change.
- Therefore, the prompt should block object semantics and focus on generic abnormality/normality.

## Narrative Bridge

```text
Prior prompts bind anomaly detection to object categories.
But ZSAD target categories are unseen and object semantics vary.
The transferable part is not "bottle" or "cable", but "normality" and "abnormality".
Therefore, replace the category token with a generic object token and learn object-agnostic prompts.
```

## Naming Strategy

`object-agnostic` is doing most of the packaging work. It turns "we removed class names" into a principle: the method deliberately excludes a harmful nuisance variable.

## Reviewer-Facing Contribution

The reviewer is expected to see:

- a diagnosis: object semantics can be harmful for ZSAD;
- a clean design: learn generic normality/abnormality prompts;
- a broad implication: anomaly cues transfer across object categories.

## Transfer Pattern

Use this when your raw idea removes, masks, marginalizes, or replaces an input variable that prior work assumes is necessary.

Reusable packaging:

```text
Prior methods condition on [variable], but [task] requires transfer across changes in [variable]. We therefore learn [task-level representation] that is agnostic to [variable] and focuses on [transferable evidence].
```

## Risk Boundary

Do not use this framing if the removed variable is actually needed by your method or if experiments do not show robustness across categories/domains.

