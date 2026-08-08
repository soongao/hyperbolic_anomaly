# R-HNA Paper Outline

## Title

Rejectable Hyperbolic Normality Acceptance for CLIP-based Zero-shot Anomaly Localization

## One-Sentence Thesis

CLIP zero-shot anomaly localization should ask whether a patch can be accepted
by learned normality at low cost; R-HNA implements this view with hyperbolic
normality acceptance cones and UOT-based rejectable acceptance.

## Exemplar-Level Packaging

| Paper pattern | Raw mechanism | Concept-level story |
| --- | --- | --- |
| AnomalyCLIP | prompt learning | object-agnostic abnormality |
| VCP-CLIP | visual conditioning | visual context prompting |
| AA-CLIP | adapters | anomaly-aware concept alignment |
| R-HNA | hyperbolic cones + UOT | rejectable hyperbolic normality acceptance |

R-HNA should be introduced as a task reformulation, not as a module stack.

## Abstract Spine

1. CLIP ZSAD usually scores patches through normal/anomaly prompt similarity.
2. Industrial anomalies are often local failures of normality rather than
   stable abnormal categories.
3. The paper reformulates localization as rejectable normality acceptance.
4. Learned normal prompts define the normality reference.
5. Hyperbolic cones turn that reference into a structured acceptance region.
6. UOT exposes unaccepted mass and conditional acceptance cost.
7. Main and mechanism results validate the formulation on MVTec AD and VisA.

## Introduction Structure

### Paragraph 1: Task And CLIP Interface

Zero-shot anomaly localization matters because defects are sparse and diverse.
CLIP gives a natural open-vocabulary interface, so recent methods compare
patches with normal and anomaly prompts.

### Paragraph 2: Failed Assumption

The hidden assumption is that anomaly is a semantic option parallel to normal.
This is weak for industrial defects: scratches, dents, stains, missing parts,
and broken boundaries are local violations of normal structure or material.

### Paragraph 3: New Question

The right question is not only whether a patch is closer to normal or abnormal
text. The right question is whether learned normality should accept that patch
at low cost.

### Paragraph 4: Structured Acceptance Region

A normal prompt cannot remain a flat point prototype. Normality has hierarchy
and directionality: object, part, surface, texture, material state. Hyperbolic
cones instantiate learned normal prompts as structured acceptance regions.

### Paragraph 5: Reject Option

Balanced matching over-explains defects by forcing every patch into normality.
UOT relaxes mass conservation and provides a soft reject option. The reject
variable is unaccepted mass; the accepted side is measured by conditional
acceptance cost.

### Paragraph 6: Contributions

State three contributions:

1. Reformulate CLIP ZSAD as rejectable normality acceptance.
2. Instantiate learned normal prompts as hyperbolic acceptance cones.
3. Use UOT to decompose anomaly evidence into unaccepted mass and conditional
   acceptance cost, validated by mechanism ablations.

## Method Structure

### 3.1 Problem Setup

Define patch features, learned normal prompt anchors, and the zero-shot setting.
Emphasize that the main method uses learned normal prompts rather than a
hand-crafted text bank.

### 3.2 Normality Acceptance Region

Map patch and prompt features to the Poincare ball. Define hyperbolic distance
as a control and hyperbolic cone violation as the main cost.

### 3.3 Rejectable Acceptance

Introduce balanced OT as the non-rejectable baseline, then UOT as the
acceptance solver with mass relaxation.

### 3.4 Evidence Decomposition

Define:

```text
accepted mass
unaccepted mass
unaccepted ratio
conditional acceptance cost
combined anomaly score
```

Explain the two evidence types:

- unaccepted mass: the patch should not be accepted by learned normality;
- conditional acceptance cost: the patch can be accepted only at high cost.

## Results Structure

### Table 1: Main Results

Purpose: show that R-HNA improves pixel-level localization on MVTec AD and VisA.

Key reading: the strongest gains are on Pixel AUPRO, which matches the
localization-focused mechanism claim.

### Table 2: Transport Mode

Compare no transport, balanced OT, partial OT, and UOT.

Key reading: UOT has the largest unaccepted-ratio gap, lowest over-match rate,
and lowest normal-image FPR.

### Table 3: Cost Type

Compare cosine, Euclidean, hyperbolic distance, and hyperbolic cone under the
same UOT setting.

Key reading: hyperbolic cone beats hyperbolic distance, so the story is
acceptance-region violation rather than generic curved distance.

### Table 4: Evidence Decomposition

Compare unaccepted mass only, conditional acceptance cost only, combined score,
and weighted combined score.

Key reading: the two signals are complementary and together support the
normality-acceptance interpretation.

### Table 5: Anchor Controls

Compare learned normal prompts, learned anomaly prompts, normal+anomaly prompts,
and shuffled normal features.

Key reading: the mechanism depends on the learned normal reference, not just on
transport regularization or anchor count.

### Figure 1: Motivation

Panels:

1. flat prompt scoring;
2. balanced normality acceptance;
3. rejectable normality acceptance.

### Figure 2: Method

Panels:

1. CLIP patch features and learned normal prompts;
2. hyperbolic acceptance cone;
3. UOT rejectable acceptance;
4. unaccepted mass plus conditional acceptance cost.

### Figure 3: Mechanism Visualization

Show original image, GT mask, accepted mass, unaccepted mass, conditional
acceptance cost, and final score.

## Discussion Spine

The discussion should reinforce the conceptual move:

```text
R-HNA does not make anomaly a better text class. It makes normality capable of
accepting, costly accepting, or rejecting local evidence.
```

The strongest claim is not universal superiority of hyperbolic geometry or OT.
The strongest claim is that rejectable normality acceptance gives CLIP ZSAD a
mechanism variable that can be decomposed, visualized, and ablated.

## Claim Boundaries

Do not claim first use of OT, UOT, hyperbolic geometry, or CLIP for anomaly
detection.

Do claim:

- normality acceptance is a stronger framing than normal/anomaly prompt
  comparison for this method;
- hyperbolic cones provide the structured acceptance region;
- UOT provides the rejectable acceptance mechanism;
- unaccepted mass and conditional acceptance cost are complementary anomaly
  evidence.
