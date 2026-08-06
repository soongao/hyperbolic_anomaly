# FiLo: LLM Descriptions + Detector Cues -> Fine-Grained Description And High-Quality Localization

Source: [FiLo card](../../cards/gu-2024-filo.md)

## Raw Technical Move

Use LLM-generated category-specific anomaly descriptions, learnable text templates, GroundingDINO for coarse localization, position prompts, and multi-scale multi-shape cross-modal interaction.

## Naive Story

```text
We ask an LLM for defect descriptions and use GroundingDINO boxes to improve CLIP localization.
```

## Paper Packaging

FiLo packages external tool usage as two named deficiencies in prior ZSAD:

- generic descriptions are not fine-grained enough;
- direct patch-text matching is not high-quality localization.

The method becomes `Fine-Grained Description` plus `High-Quality Localization`.

## Constructed Problem

The paper constructs a granularity-and-localization problem:

- Generic words like damaged/defective do not describe category-specific defects.
- Standard CLIP prompt templates are designed for foreground object classification, not abnormal parts.
- Patch-level similarity can create background false positives.
- Coarse localization and position information can guide the model toward the relevant region.

## Narrative Bridge

```text
Anomaly semantics are category-specific and visually fine-grained.
LLMs can provide candidate defect vocabulary.
Localization requires suppressing background evidence before fine scoring.
Therefore, use fine-grained descriptions for detection and coarse-to-fine localization for segmentation.
```

## Naming Strategy

The names are direct and operational: `FG-Des` names the semantic granularity; `HQ-Loc` names the quality of spatial evidence. This works because each name maps to a clear weakness.

## Reviewer-Facing Contribution

The reviewer sees a system that improves both semantic specificity and spatial precision.

## Transfer Pattern

Use this when your idea combines an external knowledge source with a localization or filtering step.

Reusable packaging:

```text
Prior methods use generic [semantic/evidence] descriptions and direct [matching/scoring], which causes [semantic ambiguity/spatial false positives]. We introduce [fine-grained knowledge source] and [quality-control localization/filtering] to refine both what to look for and where to look.
```

## Risk Boundary

External tools can look like engineering unless the paper isolates what knowledge they contribute and why the task needs it.

