---
id: yao-2024-adaclip
title: "AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection"
year: "2024"
area: "CLIP / ZSAD"
priority: "core"
tags: ["anomaly-detection", "clip", "clip-zsad", "prompt-learning", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Yao_2024_AdaCLIP.pdf"
text: "text/yao-2024-adaclip.txt"
source: "https://arxiv.org/pdf/2407.15795"
pages: 41
bytes: 20439732
sha256: 07d2d55154ddc8df4cc14fc2461ddda5a7124cc92416954bb737cc9f0a4fbe3e
---

# AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Zero-shot anomaly detection (ZSAD) targets the identifica- tion of anomalies within images from arbitrary novel categories. This study introduces AdaCLIP for the ZSAD task, leveraging a pre-trained vision- language model (VLM), CLIP. AdaCLIP incorporates learnable prompts into CLIP and optimizes them through training on auxiliary annotated anomaly detection data. Two types of learnable prompts are proposed: static and dynamic. Static prompts are shared across all images, serving to preliminarily adapt CLIP for ZSAD. In contrast, dynamic prompts are generated for each test image, providing CLIP with dynamic adaptation capabilities. The combination of static and dynamic prompts is referred to as hybrid prompts, and yields enhanced ZSAD performance. Extensive experiments conducted across 14 real-world anomaly detection datasets from industrial and medical domains indicate that AdaCLIP outperforms other ZSAD methods and can generalize better to different categories and even domains. Finally, our analysis highlights the importance of diverse auxiliary data and optimized prompts for enhanced generalization capac- ity. Code is available at https://github.com/caoyunkang/AdaCLIP.

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

- PDF: [`Yao_2024_AdaCLIP.pdf`](../PDFs/Yao_2024_AdaCLIP.pdf)
- Extracted text: [`yao-2024-adaclip.txt`](../text/yao-2024-adaclip.txt)
- Suggested grep queries:
  - `AdaCLIP`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
