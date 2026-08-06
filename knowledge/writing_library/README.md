# ZSAD Writing Library

Generated: 2026-08-06

This library is for writing papers, not for summarizing papers. It distills reusable academic writing assets from the local ZSAD paper collection: phrasing, vocabulary, narrative moves, contribution patterns, related-work positioning, experiment language, claim boundaries, and limitation writing.

## What To Use First

1. Start with `patterns/` when deciding how to frame an idea.
2. Use `templates/` when drafting a section.
3. Search `generated/` only when you need more source-linked candidate excerpts.
4. Verify important claims in `../text/`, `../cards/`, or the original PDF before using them in a manuscript.

## Directory Map

- `patterns/`: curated writing patterns distilled from the papers. This is the primary human/agent-facing layer.
- `templates/`: reusable section skeletons for Abstract, Introduction, Related Work, Method, and Experiments.
- `generated/`: automatically mined source-linked excerpts. Useful for retrieval, but not clean enough for direct reuse.
- `scripts/build_writing_library.py`: rebuilds the generated excerpt bank from `../metadata/papers.jsonl` and `../text/`.
- `usage.md`: practical workflows and query recipes.
- `AGENTS.md`: rules for future agents maintaining or using this writing library.

## Current Curated Pattern Files

- `patterns/problem_framing.md`: how to define ZSAD, ZSAS, few-shot AD, and adjacent method constraints.
- `patterns/gap_and_motivation.md`: how to move from prior capability to a concrete unsolved gap.
- `patterns/contribution_language.md`: contribution bullets and action-evidence wording.
- `patterns/related_work_positioning.md`: how to compare against CLIP-ZSAD, prompt learning, TTA, frequency, UOT, and hyperbolic methods.
- `patterns/method_narrative.md`: method-overview and module-level narration.
- `patterns/experiment_and_ablation_language.md`: result, benchmark, ablation, and qualitative-analysis wording.
- `patterns/claim_boundaries.md`: phrases that keep claims reviewer-safe.
- `patterns/limitations_and_future_work.md`: limitation and future-work patterns.
- `patterns/zsad_vocabulary.md`: reusable vocabulary grouped by writing function.

## Quick Retrieval

```bash
rg -n "object-agnostic|anomaly-aware|frequency-aware|visual context|test-time|unbalanced|hyperbolic" knowledge/writing_library
rg -n "Claim boundary|Reusable pattern|Template" knowledge/writing_library/patterns
rg -n "Abstract|Introduction|Related Work|Experiments" knowledge/writing_library/templates
```

## Source Discipline

The generated excerpt bank contains noisy two-column PDF text. Treat `generated/excerpts_by_category.md` as a candidate pool, not a polished writing source. The curated files quote only short phrases and mostly convert source wording into reusable patterns.

When using this library for a manuscript, do not copy long source sentences. Extract the writing move, rewrite it around the new method, and cite the original paper only when making a literature claim.

