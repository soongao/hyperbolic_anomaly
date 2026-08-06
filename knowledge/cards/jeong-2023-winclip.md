---
id: jeong-2023-winclip
title: "WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation"
year: "2023"
area: "CLIP / ZSAD"
priority: "core"
tags: ["anomaly-detection", "clip", "clip-zsad", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Jeong_2023_WinCLIP.pdf"
text: "text/jeong-2023-winclip.txt"
source: "https://arxiv.org/pdf/2303.14814"
pages: 21
bytes: 22852859
sha256: 7c8b42bc0a3c5c22fef0550686b8a63be2cd1bb9a9b9c77b3f9184260f4b9d34
---

# WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Visual anomaly classification and segmentation are vital for automating industrial quality inspection. The focus of prior research in the field has been on training custom models for each quality inspection task, which requires task-specific images and annotation. In this paper we move away from this regime, addressing zero-shot and few-normal-shot anomaly classification and segmentation. Recently CLIP, a vision-language model, has shown revolutionary generality with competitive zero-/few-shot performance in comparison to full-supervision. But CLIP falls short on anomaly classification and segmentation tasks. Hence, we propose window-based CLIP (WinCLIP) with (1) a compositional ensemble on state words and prompt templates and (2) efficient extraction and aggregation of window/patch/image-level features aligned with from WinCLIP/WinCLIP+. Best viewed in color and zoom in. text. We also propose its few-normal-shot extension WinCLIP+, which uses complementary information from nortraining data. Consequently, existing works have mainly mal images. In MVTec-AD (and VisA), without further tunfocused on one-class or unsupervised anomaly detection ing, WinCLIP achieves 91.8%/85.1% (78.1%/79.6%) AU[2,7,8,20,29,31,53,59], which only requires normal images. ROC in zero-shot anomaly classification and segmentation These methods typically fit a model to the normal images and while WinCLIP+ does 93.1%/95.2% (83.8%/96.4%) in 1treat any deviations from it as anomalous. When hundreds normal-shot, surpassing state-of-the-art by large margins. or thousands of normal images are available, many methods achieve high-accuracy on public benchmarks [3, 8, 31]. But in the few-normal-shot regime, there is still room to improve

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

- PDF: [`Jeong_2023_WinCLIP.pdf`](../PDFs/Jeong_2023_WinCLIP.pdf)
- Extracted text: [`jeong-2023-winclip.txt`](../text/jeong-2023-winclip.txt)
- Suggested grep queries:
  - `WinCLIP`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
