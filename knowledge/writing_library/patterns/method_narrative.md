# Method Narrative

Use this file when writing Method overview paragraphs, module introductions, and figure captions.

## Core Move

Narrate modules in the same order as the problem decomposition.

Reusable overview:

```text
Given [input] and [available supervision/reference], our framework first [representation preparation], then [alignment/scoring/optimization], and finally [decision output]. Each component addresses a distinct difficulty: [difficulty A], [difficulty B], and [difficulty C].
```

## Overview Patterns From Source Papers

### Object-Agnostic Prompt Learning

Source: [AnomalyCLIP](../../cards/zhou-2024-anomalyclip.md)

Writing move:

```text
Define generic normality/abnormality prompts first, then explain global-local optimization.
```

Reusable narration:

```text
The method first constructs task-level prompts for normality and abnormality, independent of object categories. It then optimizes these prompts with both image-level and pixel-level objectives so that global semantics and local abnormal regions contribute to the same normal-abnormal decision.
```

### Visual Context Prompting

Source: [VCP-CLIP](../../cards/qu-2024-vcp-clip.md)

Writing move:

```text
Use visual context before and after text encoding.
```

Reusable narration:

```text
A global visual context module injects image-level information into the text prompt, while a dense context module refines the output text embeddings with patch-level visual features.
```

### Hybrid Prompt Adaptation

Source: [AdaCLIP](../../cards/yao-2024-adaclip.md)

Writing move:

```text
Separate shared adaptation from instance-specific adaptation.
```

Reusable narration:

```text
Static prompts provide a shared adaptation learned from auxiliary anomaly data, whereas dynamic prompts are generated for each test image to capture instance-specific variation. Their combination balances stable task knowledge with flexible test-time context.
```

### Two-Stage Anomaly Awareness

Source: [AA-CLIP](../../cards/ma-2025-aa-clip.md)

Writing move:

```text
First adapt text anchors, then align visual patch features to those anchors.
```

Reusable narration:

```text
The first stage separates normal and abnormal semantics in the text space to form anomaly-aware anchors. The second stage aligns patch-level visual features to these anchors, transferring anomaly awareness from text representations to local visual evidence.
```

### Frequency-Deviation Anchoring

Source: [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md)

Writing move:

```text
Enhance local frequency cues, organize them into a stable coordinate, then compare against anchors.
```

Reusable narration:

```text
The framework enhances patch tokens with local spatial-frequency cues, projects the responses into a source-derived channel-spectral space, and measures anomaly evidence by relative similarity to normal and anomaly anchors.
```

## Module Paragraph Template

```text
Motivation: [Failure mode] makes [subproblem] unreliable.
Design: To address this, we introduce [module], which [operation].
Technical role: This module [aligns/filters/regularizes/organizes] [representation].
Benefit: As a result, [method] can [specific capability] under [setting].
Boundary: This component assumes [available data/model property] and does not require [unavailable resource].
```

## Figure Caption Template

```text
Overview of [method]. A frozen/pretrained [backbone] extracts [features]. [Module A] [technical function], [Module B] [technical function], and [Module C/objective] [training or inference role]. The final anomaly score/map is obtained by [aggregation/scoring].
```

## Mathematical Writing Rules

- Define inputs and available data before objectives.
- Name the supervision setting before losses.
- Explain why each loss term exists before presenting all hyperparameters.
- Put notation-heavy derivations after the conceptual pipeline.
- Use `relative to normal/anomaly anchors`, `under the source-derived coordinate`, or `conditioned on the test image` to keep formulas tied to the story.

## Avoid

- Do not list modules without explaining what failure mode each module fixes.
- Do not introduce a loss by formula alone.
- Do not say "we simply add" if the component is central to the method.

