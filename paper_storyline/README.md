# Current Paper Storyline

## Active Storyline

The current and only active storyline is:

```text
zsad_hyperbolic_uot/
```

Working title:

```text
Hyperbolic Unbalanced Semantic Transport for CLIP-based Zero-shot Anomaly Localization
```

Core claim:

```text
CLIP-based zero-shot anomaly localization should be formulated as rejectable
patch-to-normality semantic transport: normal regions are transported to
normality anchors under a hyperbolic semantic cost, while anomalous regions
appear as high-cost or unmatched mass.
```

## Current Narrative

The paper should be written around **rejectable patch-to-normality matching**.
The method is not positioned as a loose combination of CLIP, hyperbolic
geometry, and optimal transport.

The intended mechanism is:

1. CLIP extracts image patch features and normality-anchor text features.
2. Hyperbolic geometry defines the patch-to-normality transport cost.
3. Unbalanced optimal transport relaxes mass conservation, so abnormal patches
   do not have to be forcibly matched to normal anchors.
4. The anomaly map is produced from unmatched mass and conditional matched cost.

## Main Files

Use these files as the current source of truth:

| File | Purpose |
|---|---|
| `zsad_hyperbolic_uot/README.md` | Main idea and implementation entry points |
| `zsad_hyperbolic_uot/experiment_design.md` | Required experiments and decision rules |
| `zsad_hyperbolic_uot/writing_outline.md` | Paper positioning and section outline |
| `zsad_hyperbolic_uot/zh_draft/draft_zh.md` | Chinese manuscript draft |
| `zsad_hyperbolic_uot/latex_draft/main.tex` | English LaTeX draft |
| `zsad_hyperbolic_uot/latex_draft/main_zh.tex` | Chinese LaTeX draft |

## Claim Boundaries

The paper may claim:

- CLIP ZSAD can be reframed as rejectable patch-to-normality transport.
- UOT provides a testable rejection variable through unmatched mass.
- Hyperbolic cone or distance costs should be justified only if they beat flat
  costs under the same transport setup.
- The final strength of the method depends on transport-mode, cost-type,
  anchor, and signal-decomposition ablations.

The paper should not claim:

- first use of hyperbolic space for anomaly detection;
- first use of optimal transport for anomaly detection;
- universal superiority of hyperbolic geometry;
- SOTA or mechanism conclusions before real experiments support them.

## Legacy Scope

Older alternate drafts have been removed from this directory to avoid
conflicting paper narratives.

The remaining `normality_entailment` and `cone_contrastive` code paths are
baseline and ablation machinery for experiments, not the active paper story.
