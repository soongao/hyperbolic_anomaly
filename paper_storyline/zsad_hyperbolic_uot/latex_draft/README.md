# LaTeX Narrative Draft

This folder contains English and Chinese LaTeX drafts for the paper:

`Rejectable Hyperbolic Normality Acceptance for CLIP-based Zero-shot Anomaly Localization`.

## Files

- `main.tex`: complete English narrative-first LaTeX manuscript draft.
- `main_zh.tex`: complete Chinese narrative-first LaTeX manuscript draft.
- `main.pdf`: compiled English draft if LaTeX has been run.
- `main_zh.pdf`: compiled Chinese draft if XeLaTeX has been run.
- `references.bib`: empty verified-reference placeholder.
- `TODO_CHECKLIST.md`: checklist for figures, citations, efficiency reporting, and final polish.
- `figures/`: placeholder directory for future figures.

## Draft Boundary

The draft has been updated to the current R-HNA result wording. It still uses explicit markers for material that remains outside the current result tables:

- `\needcite{...}` for citations that must be verified.
- `\figtodo{...}` for figure placeholders.

Runtime, memory, final figure assets, and verified references still need to be completed before submission.

## Compile

English draft:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Chinese draft:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main_zh.tex
```
