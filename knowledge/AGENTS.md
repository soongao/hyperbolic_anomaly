# Knowledge Base Agent Instructions

This folder is a paper knowledge base for ZSAD and adjacent methods.

## Required Retrieval Order

1. Read `metadata/papers.jsonl` or `README.md` to locate candidate papers.
2. Search `text/` with `rg` for exact evidence.
3. Open the relevant `cards/*.md` for curated notes and reading status.
4. Open PDFs only for figures, equations, tables, or page validation.

## Evidence Discipline

- Do not treat extracted text as perfectly structured; PDF two-column extraction can interleave captions.
- For important claims, verify against the PDF page and add the quote to the card's `Evidence Log`.
- Keep machine-readable paths relative to this folder.
- Do not overwrite human notes in cards unless explicitly asked; if rebuilding, preserve manual notes first.

## Update Rules

- Add new PDFs to `PDFs/`.
- Add or update the row in `manifests/download_manifest.md`.
- Run `python3 scripts/build_kb.py`.
- If the script overwrites a card that already has human notes, merge the notes back manually.
