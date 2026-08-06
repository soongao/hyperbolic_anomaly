# Writing Library Agent Instructions

This folder is a writing-oriented library built from the local ZSAD paper knowledge base.

## Required Retrieval Order

1. Read `README.md` and `usage.md` to understand the writing task.
2. Open the relevant file in `patterns/`.
3. Use `templates/` only after the rhetorical role is clear.
4. Search `generated/excerpts.jsonl` or `generated/excerpts_by_category.md` for additional source candidates.
5. Verify important factual claims in `../text/`, `../cards/`, and PDFs when necessary.

## How To Use The Library

- Use `patterns/` to decide the writing move: task definition, gap, motivation bridge, contribution, method narrative, evidence, boundary, or limitation.
- Use `templates/` to draft new prose with slots. Fill slots with the user's method, evidence, and setting.
- Keep paper-specific language separate from reusable language. Do not present a source paper's claim as the user's claim.
- Prefer mechanism-level comparison over vague superiority claims.

## Evidence Rules

- Extracted text can contain column interleaving, figure captions, broken words, and null bytes.
- Generated excerpts are candidates only. Curated files are safer but still require verification for high-stakes claims.
- Do not invent "first", "SOTA", "significant", "generalizable", or "resource-efficient" claims unless the user has evidence.
- If a claim depends on protocol, name the protocol: zero-shot, few-shot, source categories, target categories, auxiliary data, target-domain training data, language-free, test-time adaptation, or cross-domain evaluation.

## Update Rules

When adding a new writing example:

1. Add it to the most specific `patterns/*.md` file.
2. Include a source link to `../cards/*.md` when writing from this directory, or `../../cards/*.md` from inside `patterns/` and `templates/`.
3. Add a reusable pattern, not only a quote.
4. Mark uncertainty if the extracted text is noisy.
5. Do not overwrite human notes in `../cards/`.

## Good Output Standard

A useful writing-library entry should answer:

- What rhetorical problem does this solve?
- Which source paper demonstrates the move?
- What is the reusable sentence pattern?
- What claim boundary prevents overstatement?

