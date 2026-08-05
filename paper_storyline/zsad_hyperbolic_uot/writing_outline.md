# Writing Outline: Hyperbolic UOT for CLIP-based ZSAD

## 1. Recommended Positioning

### Preferred Title

```text
Hyperbolic Unbalanced Semantic Transport for CLIP-based Zero-shot Anomaly Localization
```

### Short Title

```text
Hyperbolic Unbalanced Transport for ZSAD
```

### Core One-sentence Claim

```text
We formulate CLIP-based zero-shot anomaly localization as unbalanced semantic transport, where normal regions are transported to normality anchors under a hyperbolic semantic cost, while anomalous regions emerge as high-cost or unmatched mass.
```

### What Not to Claim

Do not center the paper on:

- first use of hyperbolic space for anomaly detection;
- first use of OT for anomaly detection;
- first use of CLIP and OT together;
- universal superiority of hyperbolic geometry.

The contribution should be centered on:

```text
rejectable patch-to-normality matching for CLIP-based ZSAD
```

## 2. Abstract Skeleton

1. **Background:** CLIP-based zero-shot anomaly detection commonly compares patch features with normal and abnormal prompts.
2. **Problem:** This flat scoring formulation forces every patch into prompt classes and does not model whether a patch should be rejected from normal semantic matching.
3. **Method:** Introduce hyperbolic unbalanced semantic transport. Patch features are transported to normality anchors with a hyperbolic cost; anomalous regions are detected by unmatched mass and high transport cost.
4. **Evidence:** Experiments compare no-OT scoring, balanced OT, partial OT, UOT, cosine cost, Euclidean cost, and hyperbolic cost.
5. **Conclusion:** UOT-based rejectable matching improves localization and reduces false positives on complex normal structures.

## 3. Introduction Outline

### Paragraph 1: CLIP ZSAD Context

Start from CLIP-based ZSAD:

- CLIP provides image-text alignment and strong zero-shot transfer.
- Recent methods adapt prompts to describe normality and abnormality.
- Most scoring rules still compare each patch independently against normal/abnormal prompts.

Key sentence:

```text
Despite their effectiveness, most CLIP-based ZSAD methods still reduce anomaly localization to independent patch-wise prompt scoring.
```

### Paragraph 2: Failure of Forced Prompt Assignment

Introduce the limitation:

- Industrial anomalies are local deviations from normality, not necessarily semantic categories.
- A defect patch should not always be assigned to the closest normal or abnormal text prototype.
- Balanced or flat assignment can over-explain anomalous pixels as normal.

Key sentence:

```text
The central issue is not only whether a patch is closer to "normal" or "anomaly", but whether it can be reasonably explained by the distribution of normality at all.
```

### Paragraph 3: UOT as the Classical Tool

Introduce UOT carefully:

- Optimal transport models distribution matching.
- Balanced OT is too strict because it preserves all mass.
- UOT relaxes mass conservation and naturally supports rejection.

Key sentence:

```text
Unbalanced optimal transport offers a principled way to model this reject option: patches that cannot be transported to normality at low cost can remain as unmatched mass.
```

### Paragraph 4: Why Hyperbolic Cost

Explain why cost matters:

- UOT itself needs a cost matrix.
- Cosine and Euclidean costs treat normality anchors as flat prototypes.
- Hyperbolic distance or cone violation can encode hierarchical normality relations.

Key sentence:

```text
We instantiate the transport cost in hyperbolic space so that patch-to-anchor matching reflects normality structure rather than flat prototype similarity.
```

### Paragraph 5: Contributions

Use bounded contribution bullets:

1. We reformulate CLIP-based ZSAD as rejectable patch-to-normality semantic transport.
2. We instantiate this formulation with hyperbolic normality costs and unbalanced OT, producing anomaly maps from unmatched mass and matched cost.
3. We design mechanism ablations separating transport mode, cost type, and anomaly signal, showing when mass relaxation and hyperbolic cost are necessary.

Avoid saying:

```text
We propose a novel combination of hyperbolic space and OT.
```

Prefer:

```text
We show that anomaly localization can be treated as a mass-relaxed normality matching problem.
```

## 4. Related Work Outline

### 4.1 CLIP-based Zero-shot Anomaly Detection

Cover:

- AnomalyCLIP
- WinCLIP
- PromptAD
- APRIL-GAN / VAND-style CLIP anomaly methods if relevant

Positioning:

```text
These methods improve prompt design, visual-language alignment, or patch scoring, but generally retain flat patch-wise normal/abnormal comparison.
```

### 4.2 Hyperbolic Representation and Hyperbolic VLMs

Cover:

- hyperbolic anomaly detection;
- hyperbolic prompt learning for CLIP ZSAD;
- hyperbolic VLM entailment or safety hierarchy.

Positioning:

```text
Existing hyperbolic methods mainly use geometry for representation, alignment, or entailment. Our use is narrower: hyperbolic geometry defines the semantic cost in a rejectable transport problem.
```

### 4.3 Optimal Transport and Unbalanced OT

Cover:

- optimal transport as distribution matching;
- entropic Sinkhorn solvers;
- partial OT and unbalanced OT;
- OT in vision-language matching if applicable;
- OT in anomaly detection if literature search confirms it.

Positioning:

```text
Unlike balanced matching, UOT allows mass variation, which matches the anomaly localization setting where abnormal regions should not be forcibly explained by normal semantics.
```

### 4.4 One-class and Open-set Anomaly Detection

Optional section if space allows.

Purpose:

- connect unmatched mass to reject option / one-class modeling;
- avoid making UOT look like an arbitrary matching trick.

## 5. Method Section Outline

### 5.1 Problem Setup

Define:

```text
image x
patch features P = {p_i}_{i=1}^N
normality anchors T = {t_j}_{j=1}^M
anomaly map S = {s_i}_{i=1}^N
```

State zero-shot setting:

- no target anomaly training;
- use CLIP/AnomalyCLIP features;
- normality anchors come from learned prompts or text prompt bank.

### 5.2 Hyperbolic Normality Cost

Explain mapping:

```text
z_i = Exp_0(p_i)
u_j = Exp_0(t_j)
```

Cost options:

```text
C_ij = d_H(z_i, u_j)
C_ij = V(z_i, Cone(u_j))
```

State that cone cost is the final version if experiments support it.

### 5.3 Unbalanced Semantic Transport

Write the UOT objective:

```text
min_gamma <gamma, C>
        + tau_p D(gamma 1 || a)
        + tau_t D(gamma^T 1 || b)
        + epsilon H(gamma)
```

Explain each term in plain language:

- `<gamma, C>`: transport cost;
- `D(gamma 1 || a)`: patch-side mass relaxation;
- `D(gamma^T 1 || b)`: anchor-side mass relaxation;
- entropy: stable optimization.

### 5.4 Anomaly Scoring

Define:

```text
m_i = sum_j gamma_ij
unmatched_i = a_i - m_i
cost_i = sum_j gamma_ij C_ij / (m_i + eps)
s_i = alpha * unmatched_i + beta * cost_i
```

Explain:

- `unmatched_i` captures rejection from normality;
- `cost_i` captures difficult or poor matches;
- combined score handles both clear and subtle defects.

### 5.5 Inference and Complexity

Include:

- entropic Sinkhorn iterations;
- number of anchors;
- patch resolution;
- runtime overhead compared with direct scoring.

This section is important because reviewers may see OT as expensive post-processing.

## 6. Experiments Section Outline

### 6.1 Experimental Setup

Report:

- datasets;
- train/test protocol;
- CLIP backbone;
- checkpoint;
- feature layers;
- prompt settings;
- UOT hyperparameters;
- metrics.

### 6.2 Main Results

Use Table 1:

- MVTec AD
- VisA
- optional medical datasets

Compare:

- AnomalyCLIP / cosine
- hyperbolic non-OT baselines
- final UOT method

Write this section conservatively:

```text
The goal is not only to obtain the best mean score, but to test whether rejectable transport improves localization under zero-shot transfer.
```

### 6.3 Does UOT Matter?

Use Table 2:

```text
no OT
balanced OT
partial OT
UOT
```

Primary claim:

```text
Mass relaxation is necessary because strict transport over-explains anomalous regions.
```

Show:

- `overmatch_rate`;
- unmatched mass visualization;
- normal FPR at target TPR.

### 6.4 Does Hyperbolic Cost Matter?

Use Table 3:

```text
UOT + cosine cost
UOT + Euclidean cost
UOT + hyperbolic distance
UOT + hyperbolic cone violation
```

Primary claim:

```text
UOT requires a normality-aware cost; otherwise it becomes generic matching.
```

### 6.5 What Detects the Anomaly?

Use Table 4:

```text
unmatched mass only
matched cost only
combined score
```

Primary claim:

```text
Unmatched mass captures rejection, while matched cost complements it for subtle defects.
```

### 6.6 Anchor Analysis

Use Table 5:

```text
learned normal prompts
generic normality anchors
object-conditioned anchors
random anchors
shuffled anchors
```

Primary claim:

```text
The method depends on meaningful normality anchors, not arbitrary prompt count.
```

### 6.7 Failure-mode Visualization

Use Figure 4:

- worst normal examples;
- defect examples;
- map comparison:
  - cosine score;
  - cone score;
  - balanced OT;
  - UOT unmatched mass;
  - UOT final score.

Primary claim:

```text
UOT reduces false positives on complex normal structures while preserving defect localization.
```

### 6.8 Sensitivity and Runtime

Use Figure 6:

- `tau_patch`;
- `tau_anchor`;
- `epsilon`;
- anchor count;
- runtime.

Primary claim:

```text
The method is stable across a reasonable hyperparameter range and has manageable overhead.
```

## 7. Discussion Section

Cover:

- why UOT is a better conceptual fit than balanced OT;
- when hyperbolic cost helps most;
- failure cases where unmatched mass is unreliable;
- relation to one-class/reject-option detection;
- practical cost of Sinkhorn inference.

Important honest boundary:

```text
If UOT with cosine cost performs similarly to hyperbolic UOT, the paper should shift its main claim from hyperbolic normality geometry to unbalanced semantic transport.
```

## 8. Limitations

Include:

- anchor quality affects transport quality;
- UOT introduces hyperparameters;
- Sinkhorn computation adds overhead;
- if anomalies are globally semantic rather than local structural defects, unmatched mass may be less informative;
- literature verification is required for OT-related novelty.

## 9. Figure Flow

### Figure 1: Motivation

Three panels:

1. flat patch-wise prompt scoring;
2. balanced transport forcing every patch to normal anchors;
3. UOT leaving anomalous patches as unmatched mass.

### Figure 2: Method

Pipeline:

```text
image -> CLIP patch features -> hyperbolic cost matrix -> UOT -> unmatched/cost maps -> anomaly map
```

### Figure 3: Transport Mechanism

Show one defect image with:

- original image;
- GT mask;
- transport mass;
- unmatched mass;
- matched cost;
- final score.

### Figure 4: Failure Mode

Show normal images where:

- cosine over-activates normal structures;
- balanced OT over-matches;
- UOT suppresses false positives.

### Figure 5: Distribution Evidence

Histograms or density curves:

- unmatched mass for normal pixels vs anomaly pixels;
- matched cost for normal pixels vs anomaly pixels.

### Figure 6: Sensitivity

Curves:

- AUPRO vs `tau`;
- AUPRO vs `epsilon`;
- runtime vs number of anchors.

## 10. Table Flow

| Table | Purpose |
|---|---|
| Table 1 | Main benchmark against CLIP ZSAD baselines |
| Table 2 | Transport-mode ablation |
| Table 3 | Cost-type ablation |
| Table 4 | Anomaly-score decomposition |
| Table 5 | Anchor-set ablation |
| Table 6 | Runtime and memory |

## 11. Contribution Wording

Use:

```text
We reformulate CLIP-based zero-shot anomaly localization as rejectable semantic transport, where anomalous regions are identified by high-cost or unmatched transport to normality anchors.
```

Use:

```text
We instantiate the transport cost with hyperbolic normality geometry, enabling patch-to-anchor matching beyond flat prompt similarity.
```

Use:

```text
We provide mechanism ablations showing the separate roles of mass relaxation, hyperbolic cost, and unmatched-mass scoring.
```

Avoid:

```text
We are the first to combine hyperbolic space and optimal transport for anomaly detection.
```

Avoid:

```text
Our method proves hyperbolic space is inherently superior for anomaly detection.
```

## 12. Conditional Writing Based on Results

| Experimental outcome | How to write the paper |
|---|---|
| UOT and hyperbolic cone both clearly help | Keep current title and claim. |
| UOT helps, hyperbolic cost does not | Retitle around unbalanced semantic transport; present hyperbolic cost as optional. |
| Hyperbolic cone helps, UOT does not | Retitle around hyperbolic normality entailment; drop OT as main contribution. |
| Only weak classes improve | Write as failure-mode repair for fine-grained normal structures, not universal SOTA. |
| Metrics improve but mechanism metrics fail | Avoid mechanism claim; present as empirical transport regularization. |
| Mechanism metrics work but aggregate metrics are mixed | Target workshop or method-analysis framing unless additional improvements are found. |

