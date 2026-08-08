# Notes: R-HNA Experiment And Writing Design

## Active Storyline

R-HNA frames CLIP-based zero-shot anomaly localization as rejectable normality
acceptance.

Mechanism:

- CLIP extracts patch features.
- AnomalyCLIP learned normal prompts define the normality reference.
- Hyperbolic cones define structured acceptance regions.
- UOT estimates rejectable acceptance.
- The anomaly score combines unaccepted mass and conditional acceptance cost.

## Current Code Context

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
```

The CLI names remain implementation-compatible. Paper-facing text maps them to:

- `unmatched` -> unaccepted mass
- `cost` -> conditional acceptance cost
- `hyperbolic_cone` -> hyperbolic normality acceptance cone

## Evidence Needed In The Paper

- Main table on MVTec AD and VisA.
- Rejectable acceptance ablation: no transport, balanced OT, partial OT, UOT.
- Acceptance-region cost ablation: cosine, Euclidean, hyperbolic distance,
  hyperbolic cone.
- Evidence decomposition: unaccepted mass, conditional acceptance cost, combined
  score.
- Anchor controls: learned normal prompt, learned anomaly prompt,
  normal+anomaly prompts, shuffled normal feature.
- Mechanism visualization: accepted mass, unaccepted mass, conditional
  acceptance cost, final score.

## Claim Boundary

Do not claim first use of OT, UOT, hyperbolic geometry, or CLIP for anomaly
detection.

Do claim that R-HNA turns CLIP ZSAD into a normality-acceptance problem with a
testable reject variable.
