# Method Overview Template

Use this to draft the beginning of a Method section.

## Problem Setting

```text
Let [source data] contain [available labels/references] from source categories [Cs], and let [target data] contain images from unseen categories [Ct], with [Cs intersection Ct = empty] when applicable. During evaluation, no [target-domain training images/annotations] are used. Given a test image [x], the goal is to produce an image-level anomaly score [s] and a pixel-level anomaly map [M].
```

## Overview Paragraph

```text
Figure [x] gives an overview of [METHOD]. The framework contains three components: [A], [B], and [C]. First, [A] transforms [input representation] into [intermediate representation] to address [difficulty]. Second, [B] [aligns/organizes/conditions] the representation with [anchors/prompts/references]. Third, [C] [regularizes/aggregates/scores] the result to produce [output]. During inference, [state frozen/adapted components and available data].
```

## Module Subsection Pattern

```text
### [Module Name]

[Failure mode] motivates [module]. Given [input], [module] computes [operation] to obtain [output]. This design [technical advantage], because [reason]. The output is used by [next module/scoring function].
```

## Objective Subsection Pattern

```text
### Training Objective

The objective combines [loss A], [loss B], and [loss C]. [Loss A] encourages [effect]. [Loss B] regularizes [effect]. [Loss C] preserves [effect]. The total loss is:

[formula]

where [only explain variables needed for understanding].
```

## Inference Paragraph

```text
At inference time, [METHOD] receives only [test image / normal references / augmented views]. It computes [features], applies [learned modules/fixed anchors], and aggregates [layer-wise/patch-wise/view-wise] scores into [image score and anomaly map]. No [target training labels/source data/text prompts/test-time updates] are required, if true.
```

## Boundary Reminder

End the overview with one exact resource statement:

```text
The method uses [actual resources] and does not use [unavailable resources].
```

