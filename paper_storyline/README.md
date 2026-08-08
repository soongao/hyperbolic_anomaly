# Current Paper Storyline

## Active Storyline

The current and only active storyline is:

```text
zsad_hyperbolic_uot/
```

Working title:

```text
Rejectable Hyperbolic Normality Acceptance for CLIP-based Zero-shot Anomaly Localization
```

Core claim:

```text
CLIP-based zero-shot anomaly localization should be formulated as rejectable
normality acceptance: normal patches are accepted by learned normal prompts at
low cost, while anomalous patches appear as unaccepted mass or high conditional
acceptance cost.
```

## Current Narrative

The paper should be written around **rejectable hyperbolic normality acceptance**.
The method is not positioned as a loose combination of CLIP, hyperbolic
geometry, and optimal transport.

The intended mechanism is:

1. CLIP extracts image patch features and normality-anchor text features.
2. Hyperbolic cones turn learned normal prompts into structured acceptance
   regions.
3. Unbalanced optimal transport implements rejectable acceptance, so abnormal
   patches do not have to be fully accepted by normal anchors.
4. The anomaly map is produced from unaccepted mass and conditional acceptance
   cost.

## Main Files

Use these files as the current source of truth:

| File | Purpose |
|---|---|
| `zsad_hyperbolic_uot/README.md` | Main idea and implementation entry points |
| `zsad_hyperbolic_uot/results_story_reference_zh.md` | Current result pattern and result-facing story |
| `zsad_hyperbolic_uot/experiment_design.md` | Required experiments and decision rules |
| `zsad_hyperbolic_uot/writing_outline.md` | Paper positioning and section outline |
| `zsad_hyperbolic_uot/zh_draft/draft_zh.md` | Chinese manuscript draft |
| `zsad_hyperbolic_uot/latex_draft/main.tex` | English LaTeX draft |
| `zsad_hyperbolic_uot/latex_draft/main_zh.tex` | Chinese LaTeX draft |

## Claim Boundaries

The paper may claim:

- CLIP ZSAD can be reframed as rejectable normality acceptance.
- UOT provides a testable rejection variable through unaccepted mass.
- Hyperbolic cones provide a structured acceptance region around learned normal
  prompts.
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
