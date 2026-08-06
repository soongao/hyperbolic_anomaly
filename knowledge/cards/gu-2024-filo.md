---
id: gu-2024-filo
title: "FiLo: Zero-Shot Anomaly Detection by Fine-Grained Description and High-Quality Localization"
year: "2024"
area: "CLIP / ZSAD"
priority: "core"
tags: ["anomaly-detection", "clip", "clip-zsad", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Gu_2024_FiLo.pdf"
text: "text/gu-2024-filo.txt"
source: "https://arxiv.org/pdf/2404.13671"
pages: 21
bytes: 5029089
sha256: 4febc607368ff37f481a455d707bfabfdb0cd0c9846f8f4fb6cb36c386fe44ac
---

# FiLo: Zero-Shot Anomaly Detection by Fine-Grained Description and High-Quality Localization

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

abnormal 0.4 STATE 0.45 abnormal cos normal cos Zero-shot anomaly detection (ZSAD) methods detect sim 0.55 normal STATE sim 0.5 cut ANOMALY anomalies without prior access to known normal or ab0.7 color pollution CLASS Text template: normal samples within target categories. Existing methText template: [w1][w2]…[wn] [STATE] wood A photo of [STATE] wood. ods typically rely on pretrained multimodal models, comwith [ANOMALY CLASS]. Previous ZSAD methods FG-Des puting similarities between manually crafted textual feaAnomaly Localization tures representing ”normal” or ”abnormal” semantics and image patch features to detect anomalies. However, the Patch Grounding MMCI generic descriptions of ”abnormal” often fail to precisely Matching match diverse types of anomalies across different object categories. Additionally, computing feature similarities for Previous ZSAD methods HQ-Loc single patches struggles to pinpoint specific locations of anomalies with various sizes and scales. To address these issues, we propose a novel ZSAD method called FiLo, comtween FiLo and previous ZSAD methods. Previous ZSAD methprising two components: adaptively learned Fine-Grained ods utilize fixed templates and generic anomaly descriptions, poDescription (FG-Des) and position-enhanced High-Quality tentially resulting in errors. Our FG-Des enhances detection accuracy with adaptively learned text templates and fine-grained Localization (HQ-Loc). FG-Des introduces fine-grained anomaly descriptions. For localization, ZSAD methods often proanomaly descriptions for each category using Large Landuce false positives in background areas by directly comparing guage Models (LLMs) and employs adaptively learned teximage patches with text features. Our HQ-Loc approach, using tual templates to enhance the accuracy and interpretabilGrounding DINO, location enhancement, and MMCI, effectively ity of anomaly detection. HQ-Loc, utilizing Grounding removes background regions and improves localization accuracy. DINO for preliminary localization, position-enhanced text prompts, and Multi-scale Multi-shape Cross-modal Interaction (MMCI) module, facilitates more accurate localizaa pixel-level AUC of 95.9% on the VisA dataset. Code is tion of anomalies of different sizes and shapes. Experimenavailable at https://github.com/CASIA-IVA-Lab/FiLo. tal results on datasets like MVTec and VisA demonstrate that FiLo significantly improves the performance of ZSAD in both detection and localization, achieving state-of-the

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

- PDF: [`Gu_2024_FiLo.pdf`](../PDFs/Gu_2024_FiLo.pdf)
- Extracted text: [`gu-2024-filo.txt`](../text/gu-2024-filo.txt)
- Suggested grep queries:
  - `FiLo`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
