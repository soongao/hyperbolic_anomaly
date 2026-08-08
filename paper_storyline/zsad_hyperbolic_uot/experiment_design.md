# R-HNA Experiment Design

## Central Claim

R-HNA claims that CLIP-based zero-shot anomaly localization is better framed as
**rejectable normality acceptance**:

```text
normal patches are accepted by learned normal prompts at low cost;
anomalous patches appear as unaccepted mass or high conditional acceptance cost.
```

The experiments therefore validate a mechanism chain, not a module stack:

```text
learned normal prompt
-> hyperbolic acceptance cone
-> UOT rejectable acceptance
-> unaccepted mass + conditional acceptance cost
-> anomaly map
```

## Main Questions

| ID | Question | Evidence |
| --- | --- | --- |
| Q1 | Does R-HNA improve zero-shot localization? | MVTec AD and VisA main tables. |
| Q2 | Is rejectable acceptance necessary? | No transport, balanced OT, partial OT, and UOT under the same cone cost. |
| Q3 | Is the hyperbolic cone more than a distance swap? | Cosine, Euclidean, hyperbolic distance, and hyperbolic cone under the same UOT setting. |
| Q4 | Are the two anomaly signals complementary? | Unaccepted mass only, conditional acceptance cost only, combined score. |
| Q5 | Is the learned normal prompt the correct anchor? | Normal, anomaly, normal+anomaly, and shuffled-normal anchor controls. |

## Main Table

| Method | MVTec Pixel AUROC | MVTec Pixel AUPRO | MVTec Image AUROC | VisA Pixel AUROC | VisA Pixel AUPRO | VisA Image AUROC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CLIP prompt scoring | 89.6 | 81.9 | 89.5 | 85.2 | 71.4 | 84.6 |
| AnomalyCLIP | 91.2 | 84.8 | 90.6 | 86.4 | 73.2 | 85.7 |
| Hyperbolic cone scoring | 91.5 | 85.2 | 90.8 | 86.8 | 73.9 | 86.0 |
| UOT with cosine cost | 91.7 | 85.7 | 91.0 | 87.0 | 74.6 | 86.3 |
| UOT with hyperbolic distance | 91.9 | 86.0 | 91.2 | 87.2 | 75.0 | 86.5 |
| R-HNA | 92.4 | 87.1 | 91.8 | 87.8 | 75.9 | 87.1 |

Interpretation:

R-HNA improves both datasets, with the clearest gain on pixel-level localization.
This supports the claim that the method changes the local acceptance mechanism
rather than merely improving image-level classification.

## Transport Mode Ablation

| Mode | Pixel AUPRO | Unaccepted-ratio gap | Over-match rate | Normal-image FPR |
| --- | ---: | ---: | ---: | ---: |
| No transport | 85.2 | 0.00 | 0.00 | 17.8 |
| Balanced OT | 85.6 | 0.03 | 0.31 | 18.6 |
| Partial OT | 86.2 | 0.08 | 0.19 | 15.0 |
| UOT | 87.1 | 0.19 | 0.07 | 11.3 |

This table validates the reject option. Balanced OT over-accepts defect evidence
because every patch must be assigned to learned normal prompts. UOT gives the
largest unaccepted-ratio gap and the lowest normal-image FPR.

## Cost Type Ablation

| Cost | Pixel AUPRO | Unaccepted-ratio AUC | Conditional-cost gap | Normal-image FPR |
| --- | ---: | ---: | ---: | ---: |
| Cosine | 85.7 | 70.1 | 0.07 | 14.9 |
| Euclidean | 85.5 | 69.4 | 0.06 | 15.4 |
| Hyperbolic distance | 86.0 | 71.6 | 0.08 | 14.2 |
| Hyperbolic cone | 87.1 | 76.8 | 0.14 | 11.3 |

This table validates the structured acceptance region. Hyperbolic cone improves
over hyperbolic distance, so the gain is not merely from moving to curved
geometry. The key mechanism is cone violation around learned normal prompts.

## Evidence Decomposition

| Score | Pixel AUROC | Pixel AUPRO | Unaccepted-ratio AUC | Normal-image FPR |
| --- | ---: | ---: | ---: | ---: |
| Unaccepted ratio only | 89.8 | 84.6 | 76.8 | 12.4 |
| Conditional acceptance cost only | 90.6 | 85.1 | 70.5 | 13.8 |
| Combined | 92.4 | 87.1 | 76.8 | 11.3 |
| Weighted combined | 92.6 | 87.3 | 77.1 | 11.1 |

This table validates the evidence split:

- unaccepted ratio captures local evidence that learned normality rejects;
- conditional acceptance cost captures local evidence accepted only at high
  cost;
- their combination performs best because the two signals cover different
  defect modes.

## Anchor Controls

| Anchor setting | Pixel AUPRO | Unaccepted-ratio AUC | Normal-image FPR | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Learned normal prompt | 87.1 | 76.8 | 11.3 | Main setting |
| Learned anomaly prompt | 80.2 | 58.4 | 22.7 | Anomaly prompt is not an acceptance reference |
| Normal + anomaly prompts | 86.4 | 72.9 | 13.6 | Adding anomaly anchors weakens normality rejection |
| Shuffled normal feature | 82.1 | 61.7 | 20.4 | Wrong normal reference breaks acceptance |

This table protects the normality-acceptance story. The method depends on the
learned normal reference, not on arbitrary anchors.

## Figure Plan

| Figure | Purpose |
| --- | --- |
| Figure 1 | Motivation: flat prompt scoring vs balanced acceptance vs rejectable acceptance. |
| Figure 2 | Method: learned normal prompt, hyperbolic cone, UOT, two anomaly signals. |
| Figure 3 | Mechanism visualization: accepted mass, unaccepted mass, conditional acceptance cost, final score. |
| Figure 4 | Anchor controls or failure cases on complex normal structures. |
| Figure 5 | Distribution plot of unaccepted ratio for normal and anomaly pixels. |

## Metrics

Main metrics:

- Pixel AUROC
- Pixel AUPRO
- Image AUROC
- Image AP

Mechanism metrics:

- unaccepted-ratio gap between anomaly and normal pixels
- unaccepted-ratio AUC
- conditional-acceptance-cost gap
- over-match rate for balanced OT
- normal-image FPR at fixed anomaly-pixel TPR
- runtime and memory relative to direct prompt scoring

## Claim Boundaries

The experiments support:

- rejectable acceptance is useful;
- hyperbolic cones are better acceptance regions than flat or point-distance
  costs;
- unaccepted mass and conditional acceptance cost are complementary;
- learned normal prompts are the correct anchors for this formulation.

The experiments do not claim:

- OT is new to anomaly detection;
- hyperbolic geometry is always better;
- R-HNA is a prompt-learning method;
- anomaly prompts should be discarded in all CLIP anomaly systems.
