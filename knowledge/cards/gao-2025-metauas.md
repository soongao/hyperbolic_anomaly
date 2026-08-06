---
id: gao-2025-metauas
title: "MetaUAS: Universal Anomaly Segmentation with One-Prompt Meta-Learning"
year: "2025"
area: "LVLM / SAM anomaly"
priority: "background"
tags: ["anomaly-detection", "lvlm-sam-anomaly", "prompt-learning"]
status: unread
pdf: "PDFs/Gao_2025_MetaUAS.pdf"
text: "text/gao-2025-metauas.txt"
source: "https://arxiv.org/pdf/2505.09265"
pages: 18
bytes: 25882945
sha256: 6b0f70a7e94fca0fac7fe856175a7bd4df01b5b21e7bff84c1fd7f5a3c65e8e1
---

# MetaUAS: Universal Anomaly Segmentation with One-Prompt Meta-Learning

## Why This Paper Is Here

- Area: `LVLM / SAM anomaly`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Zero- and few-shot visual anomaly segmentation relies on powerful vision-language models that detect unseen anomalies using manually designed textual prompts. However, visual representations are inherently independent of language. In this paper, we explore the potential of a pure visual foundation model as an alternative to widely used vision-language models for universal visual anomaly segmenta- tion. We present a novel paradigm that unifies anomaly segmentation into change segmentation. This paradigm enables us to leverage large-scale synthetic image pairs, featuring object-level and local region changes, derived from existing image datasets, which are independent of target anomaly datasets. We propose a one- prompt Meta-learning framework for Universal Anomaly Segmentation (MetaUAS) that is trained on this synthetic dataset and then generalizes well to segment any novel or unseen visual anomalies in the real world. To handle geometrical vari- ations between prompt and query images, we propose a soft feature alignment module that bridges paired-image change perception and single-image semantic segmentation. This is the first work to achieve universal anomaly segmentation using a pure vision model without relying on special anomaly detection datasets and pre-trained visual-language models. Our method effectively and efficiently segments any anomalies with only one normal image prompt and enjoys training- free without guidance from language. Our MetaUAS significantly outperforms previous zero-shot, few-shot, and even full-shot anomaly segmentation methods.

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

- PDF: [`Gao_2025_MetaUAS.pdf`](../PDFs/Gao_2025_MetaUAS.pdf)
- Extracted text: [`gao-2025-metauas.txt`](../text/gao-2025-metauas.txt)
- Suggested grep queries:
  - `MetaUAS`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
