# UOT/Sinkhorn: Relaxed OT Loss -> Partial Evidence Matching

Sources: [Unbalanced OT card](../../cards/chizat-2018-unbalancedoptimaltransport.md), [Sinkhorn card](../../cards/cuturi-2013-sinkhorndistances.md)

## Raw Technical Move

Use entropic optimal transport or unbalanced optimal transport to compare distributions/features with relaxed marginal constraints.

## Naive Story

```text
We add an OT/UOT matching loss.
```

## Paper Packaging

The useful packaging is not "OT is powerful". It is that classical matching assumes balanced mass, while anomaly evidence is sparse, partial, or unmatched.

## Constructed Problem

- Classical OT requires normalized distributions or exact mass conservation.
- Anomaly evidence may appear only in a few patches.
- Forcing every normal and abnormal feature to match can create false correspondences.
- Relaxing marginal constraints makes the comparison compatible with partial evidence.

## Narrative Bridge

```text
Anomaly matching is not full correspondence.
Some evidence should be transported, some should be ignored or down-weighted.
Unbalanced transport relaxes the conservation assumption.
Entropic scaling makes the optimization practical.
```

## Naming Strategy

Avoid generic names like `OT loss`. Use names that include the mismatch:

- `partial anomaly transport`
- `unbalanced patch correspondence`
- `mass-relaxed normality matching`
- `partial evidence alignment`

## Reviewer-Facing Contribution

The reviewer sees a principled matching objective aligned with the sparse and partial nature of anomalies.

## Transfer Pattern

Use this when your method compares sets, patches, distributions, prototypes, or token banks under partial mismatch.

Reusable packaging:

```text
Prior alignment assumes [balanced/full correspondence]. In anomaly detection, [evidence] is partial and sparse. We relax [constraint] to allow [unmatched/mass-varying evidence], yielding [method name].
```

## Risk Boundary

Do not use OT terminology as decoration. Define what mass means, what can be unmatched, and why relaxed matching improves the anomaly decision.

