# Risk Boundaries

Use this before turning a raw idea into a strong story.

## Boundary 1: Packaging Must Explain Necessity

Bad:

```text
We add wavelet features and call it frequency-aware.
```

Better:

```text
Spatial features under-represent subtle texture and boundary deviations, and anomalies are not always high-frequency. We therefore model multi-band deviation relative to normal anchors.
```

## Boundary 2: The Name Needs A Measured Claim

If the name says:

- `agnostic`: show transfer across the removed variable.
- `aware`: show representation separation or concept sensitivity.
- `context`: show conditioning changes behavior.
- `hybrid`: show each component has a distinct role.
- `unbalanced`: show partial/unmatched evidence matters.
- `hyperbolic`: show hierarchy, scale, or curvature matters.
- `wavelet` / `frequency`: show scale-frequency evidence matters; do not assume every anomaly is high-frequency.

## Boundary 3: Do Not Hide The Raw Move

Always keep the raw move in internal notes. It prevents overpackaging.

```text
Raw move: add two adapters.
Acceptable packaging: staged anomaly-aware text anchors and patch alignment.
Unacceptable packaging: a fundamentally new foundation model.
```

## Boundary 4: Do Not Borrow A Story Without The Condition

AnomalyCLIP's story works because object semantics can be a nuisance in ZSAD. It does not transfer to a method that heavily depends on category names.

VCP-CLIP's story works because the unavailable variable can be inferred from visual context. It does not transfer if the variable cannot be observed in the image.

AA-CLIP's story works because there is staged evidence for text-anchor disentanglement and patch alignment. It does not transfer to arbitrary one-stage adapter tuning.

## Boundary 5: Reviewer Attack Questions

- Is this just prompt learning/fine-tuning/feature fusion under a new name?
- What exact assumption of prior work is wrong?
- Why does this method follow naturally from the assumption failure?
- What experiment isolates the packaging claim?
- What would make the name false?
