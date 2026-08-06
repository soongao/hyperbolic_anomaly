---
id: zhou-2024-anomalyclip
title: "AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection"
year: "2024"
area: "CLIP / ZSAD"
priority: "core"
tags: ["anomaly-detection", "clip", "clip-zsad", "prompt-learning", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Zhou_2024_AnomalyCLIP.pdf"
text: "text/zhou-2024-anomalyclip.txt"
source: "https://arxiv.org/pdf/2310.18961"
pages: 31
bytes: 43655054
sha256: 866380d391bd39c304153aa19ac8520aba412d5615c74a9d542170f7c4c8a7b4
---

# AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Zero-shot anomaly detection (ZSAD) requires detection models trained using auxiliary data to detect anomalies without any training sample in a target dataset. It is a crucial task when training data is not accessible due to various concerns, e.g., data privacy, yet it is challenging since the models need to generalize to anomalies across different domains where the appearance of foreground objects, abnormal regions, and background features, such as defects/tumors on different products/organs, can vary significantly. Recently large pre-trained vision-language models (VLMs), such as CLIP, have demonstrated strong zero-shot recognition ability in various vision tasks, including anomaly detection. However, their ZSAD performance is weak since the VLMs focus more on modeling the class semantics of the foreground objects rather than the abnormality/normality in the images. In this paper we introduce a novel approach, namely AnomalyCLIP, to adapt CLIP for accurate ZSAD across different domains. The key insight of AnomalyCLIP is to learn object-agnostic text prompts that capture generic normality and abnormality in an image regardless of its foreground objects. This allows our model to focus on the abnormal image regions rather than the object semantics, enabling generalized normality and abnormality recognition on diverse types of objects. Large-scale experiments on 17 real-world anomaly detection datasets show that AnomalyCLIP achieves superior zero-shot performance of detecting and segmenting anomalies in datasets of highly diverse class semantics from various defect inspection and medical imaging domains. Code will be made available at https://github.com/zqhang/AnomalyCLIP.

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

- PDF: [`Zhou_2024_AnomalyCLIP.pdf`](../PDFs/Zhou_2024_AnomalyCLIP.pdf)
- Extracted text: [`zhou-2024-anomalyclip.txt`](../text/zhou-2024-anomalyclip.txt)
- Suggested grep queries:
  - `AnomalyCLIP`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
