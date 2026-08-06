# Agent Guide

Use this folder as a local literature memory, not as a black-box summary.

## Retrieval Order

1. Start from `metadata/papers.jsonl` for title, area, tags, priority, and file paths.
2. Use `rg` over `text/` for exact claims, method details, datasets, ablations, and limitations.
3. Open the matching `cards/*.md` for human notes and page-anchored evidence.
4. Use the original PDF only when layout, equations, figures, or tables matter.

## Grounding Rules

- Do not cite a card note as evidence unless it has an Evidence Log entry.
- Prefer exact quotes from `text/` plus PDF page checks for important claims.
- Keep new notes scoped to a paper card unless they synthesize multiple papers.
- When adding a cross-paper synthesis, link to every supporting card and name the evidence status.

## Common Queries

```bash
rg -n "MVTec|VisA|MPDD|BTAD" knowledge/text
rg -n "zero-shot|few-shot|training-free|prompt" knowledge/text
rg -n "ablation|limitation|failure|sensitivity" knowledge/text
rg -n "hyperbolic|Poincare|entailment|cone" knowledge/text
rg -n "optimal transport|unbalanced|Sinkhorn|partial" knowledge/text
rg -n "frequency|wavelet|scattering|Fourier" knowledge/text
```

## Status Convention

Use these values in card frontmatter when updating reading progress:

- `unread`
- `skimmed`
- `read`
- `summarized`
- `excluded`

Use `priority` for triage, not quality:

- `core`: closest to the ZSAD research direction.
- `method`: transferable method backbone.
- `supporting`: useful context or adjacent work.
- `background`: baseline or general reference.
