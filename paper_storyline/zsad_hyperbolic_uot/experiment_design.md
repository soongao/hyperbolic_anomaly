# Experiment Design: Hyperbolic UOT for CLIP-based ZSAD

## 1. Experimental Goal

The experiments should prove a narrow mechanism claim:

> CLIP-based zero-shot anomaly localization benefits from rejectable semantic transport: anomalous patches should appear as high-cost or unmatched mass when transported to normality anchors, and hyperbolic normality cost should make this transport more semantically meaningful than flat cosine or Euclidean cost.

This claim has two separable components:

1. **UOT necessity**: mass relaxation is needed because balanced transport forces anomalous patches to match normal anchors.
2. **Hyperbolic cost necessity**: the transport cost should reflect normality structure better than flat similarity.

The final paper should not rely only on aggregate AUROC. It must show that UOT changes the failure mode: anomalous pixels receive higher unmatched mass, while complex normal structures are not over-scored.

## 2. Testable Claims

| ID | Claim | Supporting evidence | Refuting evidence |
|---|---|---|---|
| C1 | Balanced OT over-matches anomalous regions to normal anchors. | Balanced OT has high matched mass on GT anomaly pixels and higher false positives or weaker pixel PRO. | Balanced OT performs the same as UOT and shows no over-matching failure. |
| C2 | UOT produces a meaningful anomaly signal through unmatched mass. | Unmatched mass separates normal and anomalous pixels; inside-mask unmatched mass is higher than outside-mask mass. | Unmatched mass is noisy, uncorrelated with masks, or only helps image-level metrics. |
| C3 | Hyperbolic cost is better than flat cost for semantic transport. | UOT with hyperbolic distance or cone cost beats UOT with cosine/Euclidean cost, especially on fine-grained classes. | UOT with cosine cost matches or exceeds hyperbolic UOT. |
| C4 | The final method improves both metrics and failure modes. | Better pixel AUROC/AUPRO and lower normal-image FPR at fixed anomaly-pixel TPR. | Metric gain exists but visualizations show the same false positives. |

## 3. Method Variants

### 3.1 Existing Non-OT Baselines

These are already close to the current codebase.

| Variant | Meaning | Purpose |
|---|---|---|
| `cosine` | Flat CLIP/AnomalyCLIP prompt scoring | Original CLIP-style ZSAD baseline |
| `euclidean_contrastive` | Euclidean normal/anomaly energy | Controls for energy scoring |
| `hyperbolic_distance_contrastive` | Hyperbolic distance to normal/anomaly text anchors | Controls for geometry without cones or OT |
| `cone_normal_only` | Normality cone violation only | Tests normality rejection without anomaly calibration |
| `cone_anomaly_only` | Anomaly cone explanation only | Tests whether anomaly prompt alone is enough |
| `cone_contrastive` | Existing hyperbolic contrastive cone scoring | Strong non-OT hyperbolic baseline |

### 3.2 New OT and UOT Variants

The new variants should isolate transport mode and cost type.

| Variant | Transport | Cost | Anomaly signal | Purpose |
|---|---|---|---|---|
| `bot_cosine` | Balanced OT | `1 - cosine` | matched cost | Tests whether global matching alone helps |
| `bot_hyperbolic_distance` | Balanced OT | hyperbolic distance | matched cost | Tests strict transport with hyperbolic geometry |
| `bot_hyperbolic_cone` | Balanced OT | cone violation | matched cost | Tests strict normality entailment transport |
| `pot_hyperbolic_cone` | Partial OT | cone violation | unmatched mass + matched cost | Tests fixed-ratio rejection |
| `uot_cosine` | UOT | `1 - cosine` | unmatched mass + matched cost | Tests mass relaxation without hyperbolic cost |
| `uot_euclidean` | UOT | Euclidean distance or energy | unmatched mass + matched cost | Controls for non-hyperbolic metric cost |
| `uot_hyperbolic_distance` | UOT | hyperbolic distance | unmatched mass + matched cost | Tests geometry plus mass relaxation |
| `uot_hyperbolic_cone` | UOT | cone violation | unmatched mass + matched cost | Final mechanism variant |

Recommended final method name:

```text
H-UOT-Cone
```

where `H` means hyperbolic cost and `UOT` means unbalanced semantic transport.

## 4. Datasets and Evaluation Scope

### Phase 1: Fast Mechanism Validation

Use MVTec weak or failure-prone classes already used in the project:

```text
capsule
pill
transistor
screw
toothbrush
```

Reason: these classes expose complex normal local structures, which is where forced matching and flat prompt scoring are most likely to fail.

### Phase 2: Main Industrial Benchmark

Use full MVTec AD and VisA under the same train-once/test-other protocol as AnomalyCLIP where possible.

Minimum reporting:

- MVTec AD all classes
- VisA all classes

Optional but useful:

- MPDD
- BTAD
- SDD
- DAGM

### Phase 3: Cross-domain Stress Test

If time allows, include medical datasets used by AnomalyCLIP:

- BrainMRI
- HeadCT
- COVID-19
- ISIC
- CVC-ColonDB / ClinicDB / Kvasir

Purpose: test whether UOT is robust when normality anchors are less industrial-texture-specific.

## 5. Metrics

### Standard ZSAD Metrics

| Metric | Level | Purpose |
|---|---|---|
| Pixel AUROC | pixel | Measures mask-level ranking quality |
| Pixel AUPRO | pixel-region | Measures region-level localization quality |
| Image AUROC | image | Measures image-level anomaly detection |
| Image AP | image | Handles class imbalance |

### Mechanism Metrics

| Metric | Definition | Purpose |
|---|---|---|
| `normal_fpr_at_target_tpr` | Normal-image false positive rate at fixed anomaly-pixel TPR, e.g. 80% | Tests false positives on normal structures |
| `unmatched_mass_gap` | mean unmatched mass inside GT mask minus outside GT mask | Tests whether UOT rejection aligns with anomalies |
| `unmatched_mass_auc` | AUROC of unmatched mass for anomaly pixels vs normal pixels | Tests whether unmatched mass alone is meaningful |
| `matched_cost_gap` | mean matched cost inside GT mask minus outside GT mask | Tests whether high transport cost aligns with defects |
| `overmatch_rate` | matched mass assigned to GT anomaly pixels under balanced OT | Tests whether strict OT forces anomalous regions into normality |
| `transport_entropy` | entropy of transport plan per image | Detects degenerate transport |
| Runtime / memory | wall time and peak memory | Tests practical overhead |

## 6. Core Experiments

### Experiment 1: Main Benchmark

**Question:** Does H-UOT-Cone improve CLIP-based ZSAD performance?

Compare:

- AnomalyCLIP original / cosine prompt scoring
- current hyperbolic non-OT variants
- `uot_cosine`
- `uot_hyperbolic_distance`
- `uot_hyperbolic_cone`

Report:

- full dataset mean
- per-class result
- industrial and medical groups separately if medical datasets are included

Success condition:

- `uot_hyperbolic_cone` improves pixel AUPRO or normal FPR over `cone_contrastive` and `uot_cosine`.
- Image-level metrics should not collapse.

Failure interpretation:

- If `cone_contrastive` equals final UOT, then OT is not necessary.
- If `uot_cosine` equals final UOT, then hyperbolic cost is not necessary.

### Experiment 2: UOT Necessity

**Question:** Is mass relaxation necessary, or is any OT enough?

Hold cost fixed as hyperbolic cone violation:

```text
no OT cone scoring
balanced OT
partial OT
unbalanced OT
```

For partial OT, sweep matched ratio:

```text
0.70, 0.80, 0.90, 0.95
```

For UOT, sweep relaxation strength:

```text
tau_patch = 0.05, 0.1, 0.5, 1.0, 5.0
tau_anchor = 0.05, 0.1, 0.5, 1.0, 5.0
```

Expected result:

- Balanced OT should assign mass to anomalous pixels because it must preserve patch mass.
- Partial OT should be sensitive to the manually chosen matched ratio.
- UOT should be more stable and produce meaningful unmatched mass.

Primary figures:

- anomaly map
- unmatched mass map
- matched cost map
- transport mass map

### Experiment 3: Hyperbolic Cost Necessity

**Question:** Does hyperbolic normality cost matter once UOT is used?

Hold transport fixed as UOT:

```text
cosine cost
Euclidean cost
hyperbolic distance cost
hyperbolic cone violation cost
```

Expected result:

- cosine UOT may improve over cosine prompt scoring, because mass relaxation is useful.
- hyperbolic cone UOT should better separate normal complex structures from actual defects.

Critical control:

- Use the same anchors and same UOT hyperparameters across costs.

### Experiment 4: Anomaly Signal Decomposition

**Question:** Which part of UOT actually detects anomalies?

For `uot_hyperbolic_cone`, compare:

```text
score = unmatched_mass
score = matched_cost
score = unmatched_mass + matched_cost
score = alpha * unmatched_mass + beta * matched_cost
```

Sweep:

```text
alpha / beta = 0, 0.25, 0.5, 1, 2, 4
```

Expected result:

- unmatched mass should be strong on clear defects;
- matched cost should help subtle defects that are still partially transported;
- combined score should be most stable.

### Experiment 5: Normality Anchor Study

**Question:** Are results caused by meaningful normality anchors or arbitrary prompt choices?

Compare anchor sets:

| Anchor set | Description | Expected role |
|---|---|---|
| `learned_normal_prompts` | AnomalyCLIP learned normal text features | Main zero-shot-compatible setting |
| `generic_normality_bank` | prompts like normal surface, intact structure, regular texture | Tests interpretable anchors |
| `object_conditioned_bank` | class name plus normality attributes if class names are available | Tests class-aware upper bound |
| `random_text_anchors` | unrelated text prompts | Negative control |
| `shuffled_anchor_assignment` | anchors from unrelated classes | Negative control |

Success condition:

- learned or generic normality anchors should outperform random or shuffled anchors.
- object-conditioned anchors may improve results but should not be the only working setting if the claim is object-agnostic ZSAD.

### Experiment 6: Failure-mode Benchmark

**Question:** Does UOT reduce false positives on complex normal local structures?

Reuse the existing failure-mode framework and add UOT variants.

Classes:

```text
capsule
pill
transistor
screw
toothbrush
```

Primary metric:

```text
normal_fpr_at_target_tpr
```

Required visuals:

- worst normal images for cosine, cone contrastive, balanced OT, and UOT;
- defect images showing that UOT does not remove true anomaly localization;
- side-by-side maps: final score, unmatched mass, matched cost.

### Experiment 7: Sensitivity and Efficiency

**Question:** Is the method stable and practical?

Sweep:

- `ot_epsilon`
- `tau_patch`
- `tau_anchor`
- number of anchors
- curvature
- radius scale
- feature layer
- patch resolution

Report:

- pixel AUPRO vs runtime;
- memory usage;
- number of Sinkhorn iterations;
- convergence failures if any.

## 7. Tables and Figures

| Item | Content |
|---|---|
| Table 1 | Main comparison on MVTec AD and VisA |
| Table 2 | Transport-mode ablation: no OT, balanced OT, partial OT, UOT |
| Table 3 | Cost ablation: cosine, Euclidean, hyperbolic distance, hyperbolic cone |
| Table 4 | Signal decomposition: unmatched, matched cost, combined |
| Table 5 | Anchor-set ablation |
| Figure 1 | Motivation: flat scoring forces every patch into prompt classes, UOT allows rejection |
| Figure 2 | Method diagram: CLIP features, hyperbolic cost matrix, UOT plan, anomaly map |
| Figure 3 | Transport visualization: mass, unmatched mass, matched cost |
| Figure 4 | Failure-mode visualization on normal complex structures |
| Figure 5 | Distribution plot of unmatched mass for normal vs anomaly pixels |
| Figure 6 | Sensitivity curves for `tau` and `epsilon` |

## 8. Minimal Implementation Targets

Add new score mode:

```text
--score_mode hyperbolic_uot
```

Add OT controls:

```text
--ot_mode balanced|partial|unbalanced
--ot_cost cosine|euclidean|hyperbolic_distance|hyperbolic_cone
--ot_epsilon
--ot_tau_patch
--ot_tau_anchor
--ot_partial_mass
--ot_score unmatched|cost|combined
--ot_alpha
--ot_beta
--ot_anchor_mode normal|anomaly|both|normal_anomaly
```

Add outputs:

```text
transport_mass_map.npy
unmatched_mass_map.npy
matched_cost_map.npy
uot_score_map.npy
transport_summary.csv
```

Add scripts:

```text
scripts/run_uot_ablation_mvtec.sh
scripts/run_uot_failure_mode_mvtec.sh
scripts/run_uot_mechanism_causal_mvtec.sh
scripts/run_uot_anchor_ablation_mvtec.sh
```

## 9. Decision Rules

Use these rules to keep the paper honest.

| Result | Interpretation |
|---|---|
| UOT beats balanced OT and partial OT | Mass relaxation is a valid contribution. |
| Balanced OT matches UOT | Remove or weaken the mass-relaxation claim. |
| UOT cosine matches UOT hyperbolic cone | Make UOT the main contribution and demote hyperbolic geometry. |
| Hyperbolic cone without OT matches UOT | Make cone entailment the main contribution and demote OT. |
| Unmatched mass separates masks but metrics do not improve | Reframe as mechanism/interpretability, not SOTA. |
| UOT improves only image-level metrics | Do not claim localization mechanism. |
| UOT improves weak classes but not all classes | Claim failure-mode repair, not universal superiority. |
