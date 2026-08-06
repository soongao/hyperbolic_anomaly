# WinCLIP: Prompt Ensemble + Windowing -> State Definition And Local Evidence

Source: [WinCLIP card](../../cards/jeong-2023-winclip.md)

## Raw Technical Move

Use prompt templates/state words for normal and anomalous states, extract CLIP features over windows/patches/images, and aggregate local anomaly scores.

## Naive Story

```text
We ensemble prompts and run CLIP on image windows.
```

## Paper Packaging

WinCLIP packages prompt engineering as `compositional prompt ensemble`: language is used to define the abstract states of normality and anomaly, while window-level features provide localized evidence.

## Constructed Problem

The paper constructs two gaps:

- CLIP's zero-shot object recognition does not directly solve anomaly classification/segmentation.
- "Normal" and "anomalous" are contextual states, not fixed object classes.
- Local defects require local image-text alignment, not only image-level CLIP features.

## Narrative Bridge

```text
Anomaly detection is a state decision, not only an object decision.
Language can define the state words.
Window-level features can localize where the state evidence appears.
Therefore, combine compositional state prompts with multi-scale window features.
```

## Naming Strategy

`compositional` makes prompt lists look systematic rather than hand-crafted. `window-based CLIP` ties the localization mechanism directly to the model name.

## Reviewer-Facing Contribution

The reviewer sees a bridge from CLIP's broad alignment to anomaly-specific state discrimination and segmentation.

## Transfer Pattern

Use this when your raw idea contains a set of manually or automatically composed descriptions.

Reusable packaging:

```text
The target decision is not a category decision but a [state/relation/condition] decision. We define this decision through compositional language and ground it with [local evidence extraction].
```

## Risk Boundary

If the prompt list is arbitrary, call it engineering. To package it as compositional, define the axes and show ablation for each axis.

