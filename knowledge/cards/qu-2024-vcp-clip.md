---
id: qu-2024-vcp-clip
title: "VCP-CLIP: A Visual Context Prompting Model for Zero-Shot Anomaly Segmentation"
year: "2024"
area: "CLIP / ZSAD"
priority: "core"
tags: ["anomaly-detection", "clip", "clip-zsad", "prompt-learning", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Qu_2024_VCP-CLIP.pdf"
text: "text/qu-2024-vcp-clip.txt"
source: "https://arxiv.org/pdf/2407.12276"
pages: 36
bytes: 23241534
sha256: f1f241bc9e57119ef07bc443366854aa808d416b97eb38b7258e196e8c55bc98
---

# VCP-CLIP: A Visual Context Prompting Model for Zero-Shot Anomaly Segmentation

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Recently, large-scale vision-language models such as CLIP have demonstrated immense potential in zero-shot anomaly segmenta- tion (ZSAS) task, utilizing a unified model to directly detect anomalies on any unseen product with painstakingly crafted text prompts. How- ever, existing methods often assume that the product category to be inspected is known, thus setting product-specific text prompts, which is difficult to achieve in the data privacy scenarios. Moreover, even the same type of product exhibits significant differences due to specific components and variations in the production process, posing significant challenges to the design of text prompts. In this end, we propose a visual context prompting model (VCP-CLIP) for ZSAS task based on CLIP. The in- sight behind VCP-CLIP is to employ visual context prompting to acti- vate CLIP’s anomalous semantic perception ability. In specific, we first design a Pre-VCP module to embed global visual information into the text prompt, thus eliminating the necessity for product-specific prompts. Then, we propose a novel Post-VCP module, that adjusts the text em- beddings utilizing the fine-grained features of the images. In extensive experiments conducted on 10 real-world industrial anomaly segmentation datasets, VCP-CLIP achieved state-of-the-art performance in ZSAS task. The code is available at https://github.com/xiaozhen228/VCP-CLIP.

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

- PDF: [`Qu_2024_VCP-CLIP.pdf`](../PDFs/Qu_2024_VCP-CLIP.pdf)
- Extracted text: [`qu-2024-vcp-clip.txt`](../text/qu-2024-vcp-clip.txt)
- Suggested grep queries:
  - `VCP-CLIP`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
