# Idea Packaging Library Agent Instructions

This folder is a knowledge base for turning raw research ideas into honest paper narratives.

## Retrieval Order

1. Read `README.md` and `usage.md`.
2. If analyzing a known paper, open its file under `cases/`.
3. If packaging a new idea, open `templates/new_idea_packaging_canvas.md`.
4. Use `patterns/packaging_primitives.md` and `patterns/naming_strategies.md` to propose framings.
5. Verify paper facts in `../cards/` and `../text/` before adding or modifying a case.

## Required Distinctions

Always separate:

- `raw technical move`: what was actually implemented.
- `paper packaging`: how the paper frames it.
- `constructed problem`: the gap that makes the move necessary.
- `reviewer-facing contribution`: what a reviewer is expected to value.
- `risk boundary`: what would make the packaging overclaim.

## Do Not

- Do not describe ordinary code changes as conceptual contributions unless there is a real task mismatch.
- Do not invent novelty.
- Do not use "first", "general", "universal", or "fundamental" without evidence.
- Do not collapse zero-shot, few-shot, test-time adaptation, and source-free adaptation.
- Do not remove the "naive story"; it is the control that makes the packaging analysis useful.

## Good Entry Standard

A good case file should let a future user say:

```text
My idea is basically [raw move]. Which paper packaged a similar move well, and what problem construction can I borrow without copying the paper?
```

