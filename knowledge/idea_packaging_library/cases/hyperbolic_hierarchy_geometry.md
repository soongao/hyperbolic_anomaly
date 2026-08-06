# Hyperbolic: Geometry Replacement -> Hierarchy-Aware Capacity

Sources: [Poincare Embeddings card](../../cards/nickel-2017-poincareembeddings.md), [Hyperbolic Entailment Cones card](../../cards/ganea-2018-hyperbolicentailmentcones.md)

## Raw Technical Move

Embed representations in hyperbolic space instead of Euclidean space; optionally use entailment cones or curvature-based geometry.

## Naive Story

```text
We replace Euclidean features with hyperbolic features.
```

## Paper Packaging

The strong packaging is `geometry matches latent structure`: hyperbolic space is not a random metric choice; it is justified when the data has hierarchy, tree-like structure, scale-free organization, or asymmetric entailment.

## Constructed Problem

- Euclidean embeddings encode similarity but struggle with tree-like expansion in low dimensions.
- Hierarchical data grows exponentially with depth.
- Hyperbolic space has exponential volume growth under negative curvature.
- Therefore, it can compactly encode hierarchy and similarity.

## Narrative Bridge

```text
The problem is not only feature quality; it is geometry mismatch.
If anomalies or categories have hierarchical/scale-varying relations, Euclidean distance may be the wrong inductive bias.
Hyperbolic geometry provides capacity for tree-like organization.
```

## Naming Strategy

Good names should bind geometry to the anomaly structure:

- `hierarchy-aware anomaly embedding`
- `curvature-guided defect representation`
- `hyperbolic normality manifold`
- `entailment-aware abnormality scoring`

## Reviewer-Facing Contribution

The reviewer should see that geometry is solving a representational bottleneck, not merely adding mathematical flavor.

## Transfer Pattern

Use this only when you can argue that the anomaly space has hierarchy, scale, entailment, part-whole structure, or tree-like expansion.

Reusable packaging:

```text
Prior methods represent [objects/anomalies/features] in Euclidean space, implicitly assuming flat similarity. However, [task evidence] exhibits [hierarchy/scale/asymmetry]. We therefore use [geometry] to encode [relation] with a better inductive bias.
```

## Risk Boundary

Hyperbolic space is easy to overpackage. Without an experiment that tests hierarchy, scale, or curvature sensitivity, reviewers may treat it as decorative complexity.

