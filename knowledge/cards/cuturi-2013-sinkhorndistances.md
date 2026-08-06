---
id: cuturi-2013-sinkhorndistances
title: "Sinkhorn Distances: Lightspeed Computation of Optimal Transport"
year: "2013"
area: "OT / UOT"
priority: "method"
tags: ["optimal-transport", "ot-uot"]
status: unread
pdf: "PDFs/Cuturi_2013_SinkhornDistances.pdf"
text: "text/cuturi-2013-sinkhorndistances.txt"
source: "https://proceedings.neurips.cc/paper_files/paper/2013/file/af21d0c97db2e27e13572cbf59eb343d-Paper.pdf"
pages: 9
bytes: 369066
sha256: ec3bb83fc9cc12be1c703d0b1bf99c170eb19c08a585ad910a696f25f596c78b
---

# Sinkhorn Distances: Lightspeed Computation of Optimal Transport

## Why This Paper Is Here

- Area: `OT / UOT`
- Priority: `method`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Optimal transport distances are a fundamental family of distances for probability measures and histograms of features. Despite their appealing theoretical proper- ties, excellent performance in retrieval tasks and intuitive formulation, their com- putation involves the resolution of a linear program whose cost can quickly be- come prohibitive whenever the size of the support of these measures or the his- tograms’ dimension exceeds a few hundred. We propose in this work a new family of optimal transport distances that look at transport problems from a maximum- entropy perspective. We smooth the classic optimal transport problem with an entropic regularization term, and show that the resulting optimum is also a dis- tance which can be computed through Sinkhorn’s matrix scaling algorithm at a speed that is several orders of magnitude faster than that of transport solvers. We also show that this regularized distance improves upon classic optimal transport distances on the MNIST classification problem.

## Reading Notes

- Main problem:
- Core idea:
- Key method components:
- Datasets / protocol:
- Important results:
- Limitations:
- Relevance to ZSAD improvement:
- Possible experiments to borrow:

## Agent Use

- PDF: [`Cuturi_2013_SinkhornDistances.pdf`](../PDFs/Cuturi_2013_SinkhornDistances.pdf)
- Extracted text: [`cuturi-2013-sinkhorndistances.txt`](../text/cuturi-2013-sinkhorndistances.txt)
- Suggested grep queries:
  - `Sinkhorn Distances`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
