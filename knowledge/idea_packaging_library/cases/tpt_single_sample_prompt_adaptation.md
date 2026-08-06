# TPT: Test-Time Prompt Update -> Single-Sample Adaptive Context

Source: [TPT card](../../cards/shu-2022-tpt.md)

## Raw Technical Move

At inference, generate augmented views of one test image and update prompt parameters by minimizing marginal entropy with confidence selection.

## Naive Story

```text
We optimize the prompt at test time.
```

## Paper Packaging

TPT packages this as `test-time prompt tuning` for zero-shot generalization: the prompt becomes an adaptive handle for retrieving pretrained CLIP knowledge from a single unlabeled test sample.

## Constructed Problem

The paper constructs a data-availability problem:

- Hand prompts are brittle.
- Prompt tuning usually needs downstream training data.
- Zero-shot evaluation has no downstream training data.
- At inference, the only available information is the test sample itself.

## Narrative Bridge

```text
Prompt tuning is useful but violates zero-shot assumptions when it uses downstream data.
The single test sample is still available at inference.
Augmented views provide a self-consistency signal.
Therefore, tune only the prompt to adapt context without changing pretrained features.
```

## Naming Strategy

`test-time` shifts the contribution from "prompt optimization" to "optimization under a strict data constraint". `confidence selection` turns filtering augmentations into a named reliability mechanism.

## Reviewer-Facing Contribution

The reviewer sees a way to adapt without training data or labels, with a bounded parameter group.

## Transfer Pattern

Use this when your idea uses inference-time self-supervision.

Reusable packaging:

```text
Although [adaptation] usually requires [training data], [test-time signal] is available under the deployment protocol. We use [self-consistency/objective] to adapt [small parameter group] while preserving [pretrained model/generalization].
```

## Risk Boundary

Always disclose inference-time cost, extra views, and backpropagation.

