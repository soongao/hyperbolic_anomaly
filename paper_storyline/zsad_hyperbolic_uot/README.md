# ZSAD + Hyperbolic Space + Unbalanced Optimal Transport Storyline

## 1. Core Claim

CLIP-based zero-shot anomaly detection should not force every image patch into an independent normal-versus-anomaly prompt classification. A more faithful formulation is **unbalanced semantic transport**: normal patches should be transportable to normality anchors at low cost, while anomalous patches emerge as high-cost or unmatched mass.

In this formulation:

- CLIP provides patch and text features.
- Hyperbolic geometry defines hierarchical normality costs.
- Unbalanced Optimal Transport decides which patches can be explained by normal semantics and which patches should be rejected.

Working title:

**Hyperbolic Unbalanced Semantic Transport for CLIP-based Zero-shot Anomaly Detection**

Shorter title:

**Hyperbolic Unbalanced Transport for Zero-shot Anomaly Localization**

## 2. Problem

Existing CLIP-based ZSAD methods usually score each patch independently:

```text
score_i = f(sim(p_i, normal_text), sim(p_i, anomaly_text))
```

This has two limitations.

First, patch-wise prompt scoring treats anomaly detection as a flat binary classification problem. It does not model whether all normal-looking regions in an image can be jointly explained by a normality distribution.

Second, forcing every patch to match normal or anomaly prompts is mismatched with anomaly localization. An anomalous patch should not always be assigned to a normal semantic anchor. It may be better interpreted as **mass that cannot be transported to normality under reasonable cost**.

## 3. Method

Given an image, extract CLIP patch features:

```text
P = {p_i}_{i=1}^N
```

Construct normality anchors from CLIP text features or learned AnomalyCLIP normal prompts:

```text
T = {t_j}_{j=1}^M
```

Examples of normality anchors:

```text
normal object
normal surface
normal texture
normal structure
normal boundary
intact state
regular pattern
```

Map patch and text features into hyperbolic space:

```text
z_i = Exp_0(p_i)
u_j = Exp_0(t_j)
```

Define the transport cost between patch `i` and normality anchor `j`:

```text
C_ij = d_H(z_i, u_j)
```

or, if using cone entailment:

```text
C_ij = V(z_i, Cone(u_j))
```

Then solve an unbalanced OT problem:

```text
min_gamma <gamma, C>
        + tau_p D(gamma 1 || a)
        + tau_t D(gamma^T 1 || b)
        + epsilon H(gamma)
```

where:

- `gamma` is the transport plan.
- `C` is the hyperbolic semantic cost.
- `a` is the patch mass distribution.
- `b` is the normality-anchor mass distribution.
- `D` is usually a KL divergence.
- `tau_p` and `tau_t` control how strictly mass is preserved.
- `H` is entropy regularization for stable Sinkhorn-style optimization.

The patch anomaly score can combine unmatched mass and matched cost:

```text
unmatched_i = a_i - sum_j gamma_ij
cost_i = sum_j gamma_ij C_ij / (sum_j gamma_ij + eps)
score_i = alpha * unmatched_i + beta * cost_i
```

## 4. Why UOT Fits ZSAD

Balanced OT requires all patch mass to be transported to normality anchors:

```text
gamma 1 = a
gamma^T 1 = b
```

This is too strict for anomaly detection because abnormal regions are forced to match some normal anchor.

Partial OT allows only a fixed amount of mass to be matched, but the matching ratio must be manually chosen.

Unbalanced OT is more suitable because it lets the model softly decide how much patch mass should be matched. In anomaly localization, this gives a natural interpretation:

```text
normal region: low-cost transported mass
abnormal region: high-cost or unmatched mass
```

## 5. Why Hyperbolic Cost Matters

UOT alone only provides a distribution matching mechanism. Its behavior depends heavily on the cost matrix.

Using Euclidean or cosine cost treats normality anchors as flat prototypes. Hyperbolic cost can encode asymmetric or hierarchical normality relations:

```text
normal object
  -> normal part
    -> normal texture / structure / material state
```

The expected contribution is not simply "OT improves CLIP". The claim should be:

> Hyperbolic geometry provides a normality-aware semantic cost, while unbalanced OT turns patch anomaly scoring into rejectable semantic transport.

## 6. Problem-Method-Insight

| Layer | Statement |
|---|---|
| Problem | CLIP-based ZSAD often forces each patch into flat normal/anomaly prompt scoring, which cannot express that anomalous patches should be rejected from normal semantic matching. |
| Method | We build a hyperbolic semantic cost between image patches and normality anchors, then solve an unbalanced OT problem to obtain patch-level matched cost and unmatched mass. |
| Insight | Anomaly localization can be viewed as a mass relaxation problem: normal regions are transportable to normality, while anomalies appear as semantic mass that cannot be transported at reasonable cost. |

## 7. Main Ablations

The key experiments should prove that the method is not just a complicated scoring trick.

| Variant | Purpose |
|---|---|
| Cosine prompt scoring | Original flat CLIP/AnomalyCLIP-style baseline. |
| Hyperbolic distance scoring | Tests whether geometry alone is enough. |
| Balanced OT with cosine cost | Tests whether global matching alone is enough. |
| Balanced OT with hyperbolic cost | Tests whether strict transport hurts anomaly rejection. |
| Partial OT with hyperbolic cost | Tests fixed-ratio rejection. |
| UOT with cosine cost | Tests whether mass relaxation alone is enough. |
| UOT with hyperbolic cost | Final formulation. |
| UOT with hyperbolic cone violation cost | Strongest entailment version. |

Expected evidence:

- Balanced OT should over-match anomalous regions to normality anchors.
- UOT should produce higher unmatched mass on anomalous pixels than normal pixels.
- Hyperbolic cost should improve separation over cosine or Euclidean cost when normality anchors have hierarchical semantics.

## 8. Paper-Facing Contributions

1. We reformulate CLIP-based zero-shot anomaly localization as an unbalanced semantic transport problem, where anomalous regions are identified by high-cost or unmatched transport to normality anchors.
2. We introduce a hyperbolic normality cost for patch-to-text transport, allowing normal semantics to be represented beyond flat prompt similarity.
3. We show through balanced OT, partial OT, UOT, cosine-cost, and hyperbolic-cost ablations that both mass relaxation and normality-aware cost are necessary for robust anomaly localization.

## 9. Reviewer Pressure Points

| Risk | Likely reviewer question | Repair |
|---|---|---|
| OT looks like post-processing | Why is this more than smoothing or matching after CLIP scoring? | Show balanced OT, partial OT, UOT, and no-OT baselines; emphasize unmatched mass as the anomaly signal. |
| Hyperbolic space looks unnecessary | Does UOT with cosine cost already work? | Include cosine-cost UOT and Euclidean-cost UOT. The claim only holds if hyperbolic cost improves separation or failure modes. |
| Too many normality anchors | Are prompt anchors hand-engineered? | Compare learned AnomalyCLIP normal prompts, generic anchors, and class-agnostic anchor banks. |
| Computation overhead | Is OT too expensive for patch maps? | Use entropic Sinkhorn, reduced anchor count, and report runtime/FLOPs. |
| Novelty overlap | Has OT already been used in anomaly detection or CLIP matching? | Literature verification is required; narrow claim to unbalanced patch-to-normality semantic transport for CLIP-based ZSAD with hyperbolic cost. |

## 10. Minimal Implementation Plan

1. Build a cost matrix from current CLIP patch features to normality text anchors.
2. Implement entropic UOT in PyTorch or use a small dependency if available.
3. Produce anomaly maps from unmatched mass and transport cost.
4. Add CLI switches:

```text
--score_mode hyperbolic_uot
--ot_mode balanced|partial|unbalanced
--ot_cost cosine|euclidean|hyperbolic_distance|hyperbolic_cone
--ot_epsilon
--ot_tau_patch
--ot_tau_anchor
```

5. Run first on MVTec weak classes:

```text
capsule
pill
screw
toothbrush
transistor
```

6. Compare pixel AUROC, AUPRO, image AUROC, and unmatched-mass visualization.

## 11. Claim Boundary

Do not claim:

- "First to use OT for anomaly detection."
- "First to combine CLIP and OT."
- "Hyperbolic space is universally better."

Safer claim:

> We use unbalanced optimal transport as a rejectable semantic matching rule for CLIP-based ZSAD, and instantiate its cost with hyperbolic normality geometry so that anomalous patches can emerge as unmatched or high-cost mass rather than being forced into flat prompt classes.

