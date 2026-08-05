# LaTeX Narrative Draft

This folder contains English and Chinese LaTeX first drafts for the paper idea:

`CLIP-based zero-shot anomaly localization + hyperbolic normality cost + unbalanced optimal transport`.

## Files

- `main.tex`: complete English narrative-first LaTeX manuscript draft.
- `main_zh.tex`: complete Chinese narrative-first LaTeX manuscript draft.
- `main.pdf`: compiled English draft if LaTeX has been run.
- `main_zh.pdf`: compiled Chinese draft if XeLaTeX has been run.
- `references.bib`: empty verified-reference placeholder.
- `TODO_CHECKLIST.md`: checklist for filling results, figures, citations, and final claims.
- `figures/`: placeholder directory for future figures.

## Draft Boundary

The draft intentionally leaves all experimental results, proof details, and verified citations blank. It uses explicit markers:

- `\needcite{...}` for citations that must be verified.
- `\resulttodo{...}` for result-dependent claims.
- `\prooftodo{...}` for proof or derivation details if needed.
- `\figtodo{...}` for figure placeholders.

Do not turn any result placeholder into a claim until the corresponding table, figure, or mechanism analysis is inserted.

## Compile

English draft:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Chinese draft:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main_zh.tex
```
