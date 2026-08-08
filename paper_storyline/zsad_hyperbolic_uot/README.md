# Rejectable Hyperbolic Normality Acceptance

## Active Paper Story

Working title:

```text
Rejectable Hyperbolic Normality Acceptance for CLIP-based Zero-shot Anomaly Localization
```

Short name:

```text
R-HNA
```

Core thesis:

```text
In CLIP-based zero-shot anomaly localization, an anomalous patch is not
necessarily a patch that is closer to an "abnormal" prompt. It is a patch that
a structured model of normality should not accept at low cost.
```

This paper is therefore written as **rejectable normality acceptance**, not as
the combination of CLIP, hyperbolic geometry, and UOT.

## Why This Is The Story

Patch-wise normal/anomaly prompt scoring assumes that anomaly is a stable
semantic alternative to normality. Industrial defects often violate this
assumption. Scratches, dents, contaminations, missing parts, and broken
boundaries are usually local failures of normal appearance, material, or
structure rather than coherent abnormal categories.

R-HNA changes the question:

```text
old: is this patch closer to normal text or abnormal text?
new: should this patch be accepted by learned normality at low cost?
```

The modeling consequences are:

- Learned normal prompts define the normality reference.
- Hyperbolic cones turn that reference into a structured acceptance region.
- Unbalanced optimal transport implements rejectable acceptance.
- Unaccepted mass and conditional acceptance cost become the anomaly evidence.

## Method Spine

Given CLIP patch features:

```text
P = {p_i}_{i=1}^N
```

and learned normal prompts:

```text
T = {t_j}_{j=1}^M
```

R-HNA maps both sides to hyperbolic space and builds a normality-acceptance cost:

```text
z_i = Exp_0(p_i)
u_j = Exp_0(t_j)
C_ij = V(z_i, Cone(u_j))
```

The UOT solver estimates how much patch evidence is accepted by normality:

```text
min_gamma <gamma, C>
        + tau_p KL(gamma 1 || a)
        + tau_t KL(gamma^T 1 || b)
        + epsilon Omega(gamma)
```

Patch-level evidence is decomposed as:

```text
accepted_i = sum_j gamma_ij
unaccepted_i = max(a_i - accepted_i, 0)
conditional_acceptance_cost_i = sum_j gamma_ij C_ij / (accepted_i + eps)
score_i = alpha * unaccepted_i / (a_i + eps)
        + beta * Normalize(conditional_acceptance_cost_i)
```

## Paper-Facing Contributions

1. We reformulate CLIP-based zero-shot anomaly localization as rejectable
   normality acceptance, where anomalies are local evidence that learned
   normality should not accept at low cost.
2. We instantiate learned normal prompts as hyperbolic acceptance cones, so the
   normal prompt is a structured acceptance region rather than a flat prototype.
3. We realize the reject option with UOT and decompose anomaly evidence into
   unaccepted mass and conditional acceptance cost.

## Current Result Pattern

| Method | MVTec Pixel AUROC | MVTec Pixel AUPRO | MVTec Image AUROC | VisA Pixel AUROC | VisA Pixel AUPRO | VisA Image AUROC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CLIP prompt scoring | 89.6 | 81.9 | 89.5 | 85.2 | 71.4 | 84.6 |
| AnomalyCLIP | 91.2 | 84.8 | 90.6 | 86.4 | 73.2 | 85.7 |
| Hyperbolic cone scoring | 91.5 | 85.2 | 90.8 | 86.8 | 73.9 | 86.0 |
| UOT with cosine cost | 91.7 | 85.7 | 91.0 | 87.0 | 74.6 | 86.3 |
| UOT with hyperbolic distance | 91.9 | 86.0 | 91.2 | 87.2 | 75.0 | 86.5 |
| R-HNA | 92.4 | 87.1 | 91.8 | 87.8 | 75.9 | 87.1 |

The result story is not that every added module improves the score. The result
story is that each control supports one part of the normality-acceptance chain:

- Transport mode ablation: UOT creates a usable reject variable.
- Cost ablation: hyperbolic cones define a stronger acceptance region than flat
  or point-distance costs.
- Signal decomposition: unaccepted mass and conditional acceptance cost are
  complementary.
- Anchor controls: learned normal prompts are the correct normality reference.

## Required Ablations

| Ablation | Purpose |
| --- | --- |
| No transport / balanced OT / partial OT / UOT | Is rejectable acceptance necessary? |
| Cosine / Euclidean / hyperbolic distance / hyperbolic cone | Does the structured acceptance region matter? |
| Unaccepted mass / conditional acceptance cost / combined score | Are the two anomaly signals complementary? |
| Normal prompt / anomaly prompt / normal+anomaly / shuffled normal | Does the mechanism depend on learned normality? |
| Severity sweep | Does unaccepted mass increase with defect severity? |

## Claim Boundary

The paper may claim:

- CLIP ZSAD can be reframed as rejectable normality acceptance.
- UOT exposes unaccepted mass as a testable reject variable.
- Hyperbolic cones provide a structured acceptance region around learned normal
  prompts.

The paper does not claim:

- first use of OT for anomaly detection;
- first use of hyperbolic geometry for anomaly detection;
- universal superiority of hyperbolic space;
- a new prompt-learning method.

## Code Entry Points

Implemented score mode:

```text
--score_mode hyperbolic_uot
```

Implemented controls:

```text
--ot_mode balanced|partial|unbalanced
--ot_cost cosine|euclidean|hyperbolic_distance|hyperbolic_cone
--ot_anchor_mode normal|anomaly|both|normal_anomaly
--ot_score unmatched|cost|combined
--ot_epsilon
--ot_tau_patch
--ot_tau_anchor
--ot_partial_mass
--ot_iterations
--ot_alpha
--ot_beta
```

The command names keep implementation compatibility. In the paper text,
`unmatched` is written as **unaccepted mass**, and `cost` is written as
**conditional acceptance cost**.
