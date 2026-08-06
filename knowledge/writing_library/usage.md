# Writing Library Usage

## Fast Workflows

### Draft An Abstract

1. Open `templates/abstract_template.md`.
2. Choose one task-definition pattern from `patterns/problem_framing.md`.
3. Choose one gap pattern from `patterns/gap_and_motivation.md`.
4. Fill the method and evidence slots with your actual method and numbers.
5. Check every strong claim against `patterns/claim_boundaries.md`.

### Draft An Introduction

1. Open `templates/introduction_template.md`.
2. Use `patterns/problem_framing.md` for paragraph 1.
3. Use `patterns/gap_and_motivation.md` for paragraphs 2-3.
4. Use `patterns/method_narrative.md` for the bridge paragraph.
5. Use `patterns/contribution_language.md` for contribution bullets.

### Position A New Method Against Prior Work

1. Open `patterns/related_work_positioning.md`.
2. Pick the comparison axis: supervision, prompt source, reference source, representation space, adaptation time, or evidence type.
3. Use the "Unlike..., which..., our method..." pattern only when the contrast is factually true.
4. Add a claim boundary from `patterns/claim_boundaries.md`.

### Write Experiments And Ablations

1. Open `templates/experiment_section_template.md`.
2. Map each experiment to one claim before drafting.
3. Use `patterns/experiment_and_ablation_language.md` for result and ablation wording.
4. Add limitations from `patterns/limitations_and_future_work.md` when results expose failure modes.

## Query Recipes

Search curated patterns:

```bash
rg -n "Reusable pattern|Claim boundary|Use when" knowledge/writing_library/patterns
```

Search source-linked candidates:

```bash
rg -n "\"category\": \"problem_gap\"|\"category\": \"method_narrative\"" knowledge/writing_library/generated/excerpts.jsonl
```

Search for a specific rhetorical move:

```bash
rg -n "Although|However|Unlike|Motivated by|Specifically|Extensive experiments|may fail" knowledge/writing_library
```

Search original paper text before finalizing:

```bash
rg -n "object-agnostic|anomaly-aware|visual context prompting|frequency-deviation|test-time prompt tuning|unbalanced optimal transport|Poincare" knowledge/text
```

## Agent Prompt Recipes

Use this when asking an agent to draft prose:

```text
Use knowledge/writing_library as the writing source. Draft [section] for [method idea].
First choose the relevant pattern file, then use the matching template.
Do not copy source-paper sentences. Preserve claim boundaries and mark missing evidence.
```

Use this when asking for writing review:

```text
Review this section against knowledge/writing_library/patterns:
1. task definition,
2. gap clarity,
3. method bridge,
4. contribution specificity,
5. claim-evidence alignment,
6. limitation wording.
Return concrete rewrite suggestions.
```

## Rewrite Rule

Convert source phrasing into a reusable pattern:

```text
Source phrase: "CLIP falls short on anomaly classification and segmentation tasks."
Writing move: strength-to-gap.
Reusable pattern: "Although [foundation model] provides [broad capability], it remains limited for [target task] because [task-specific mismatch]."
New sentence: "Although CLIP provides broad visual-language alignment, it remains limited for zero-shot defect localization because anomaly evidence often appears as fine-grained local deviations rather than object-level semantics."
```

