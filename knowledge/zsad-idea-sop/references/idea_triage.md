# Idea Triage

Use this reference after normalizing the user's rough idea.

## Raw-Idea Decomposition

Write four lines before judging:

```text
Raw move:
Naive story:
Target protocol:
Claim the user probably wants:
```

Examples:

- `add two adapters` -> adapter/fine-tuning family.
- `use CoCoOp with image features` -> visual-context prompt family.
- `add wavelet branch` -> frequency/multiscale evidence family.
- `use UOT for patch matching` -> relaxed/partial matching family.
- `map features to hyperbolic space` -> geometry/hierarchy family.
- `update prompt at inference` -> TTA/test-time prompt family.

## Feasibility Checks

Reject or heavily qualify the idea if:

- it needs target anomaly labels under a zero-shot protocol;
- it trains on target test images without explicitly being TTA and label-free;
- it depends on category names while claiming object-agnostic transfer;
- it adds a heavy model while claiming efficient deployment without measuring cost;
- it changes CLIP features aggressively while claiming to preserve zero-shot generalization;
- it only stacks modules without explaining what assumption of prior work fails.

## Prior-Overlap Grades

Use these grades in the answer:

- `Already covered`: the raw move and paper story are both close to an existing paper.
- `Mechanism covered, story open`: the module exists, but a different ZSAD mismatch might be defensible.
- `Story covered, mechanism open`: the problem framing exists, but the implementation differs.
- `Adjacent support only`: related method exists outside ZSAD; ZSAD transfer needs evidence.
- `Likely novel but risky`: little direct overlap, but feasibility or protocol risk remains.

## Novelty Grades

Use a 4-level novelty assessment:

- `N0: not novel`: same raw move and same story as prior work.
- `N1: incremental`: small module replacement with weak task reason.
- `N2: viable`: existing components, but a clear new mismatch, protocol, or causal design.
- `N3: strong`: new mechanism plus clear ZSAD-specific assumption failure and testable evidence.

## Reasonableness Questions

Ask internally:

1. What exact prior assumption is wrong?
2. Why does the proposed module naturally address that assumption?
3. What does the module change: prompt, text space, visual space, matching, scoring, protocol, or geometry?
4. What baseline would make the idea look trivial?
5. What ablation would falsify the claimed mechanism?

If these cannot be answered, the idea is not ready for packaging.
