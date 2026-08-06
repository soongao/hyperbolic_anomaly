---
id: ma-2025-aa-clip
title: "AA-CLIP: Enhancing Zero-shot Anomaly Detection via Anomaly-Aware CLIP"
year: "2025"
area: "CLIP / ZSAD"
priority: "core"
tags: ["anomaly-detection", "clip", "clip-zsad", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Ma_2025_AA-CLIP.pdf"
text: "text/ma-2025-aa-clip.txt"
source: "https://arxiv.org/pdf/2503.06661"
pages: 11
bytes: 21572952
sha256: f8e29127a8cf054624d9f70289748d8997d12112ae5e903ff90a9fa08ef82b93
---

# AA-CLIP: Enhancing Zero-shot Anomaly Detection via Anomaly-Aware CLIP

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

knowledge. Extensive experiments validate AA-CLIP as a Anomaly detection (AD) identifies outliers for applications resource-efficient solution for zero-shot AD tasks, achievlike defect and lesion detection. While CLIP shows promise ing state-of-the-art results in industrial and medical applifor zero-shot AD tasks due to its strong generalization cacations. The code is available at https://github. pabilities, its inherent Anomaly-Unawareness leads to limcom/Mwxinnn/AA-CLIP. ited discrimination between normal and abnormal features. To address this problem, we propose Anomaly-Aware CLIP 1. Introduction (AA-CLIP), which enhances CLIP’s anomaly discriminaAnomaly detection (AD) involves modeling the distribution tion ability in both text and visual spaces while preserving of a dataset to identify outliers, such as defects in industrial its generalization capability. AA-CLIP is achieved through products [2] or lesions in medical images [12]. Despite that a straightforward yet effective two-stage approach: it first previous AD frameworks [9, 10, 14, 22, 30, 56] effectively creates anomaly-aware text anchors to differentiate normal detect anomalies when sufficient labeled data is available and abnormal semantics clearly, then aligns patch-level vifor specific classes, their high resource demands often limit sual features with these anchors for precise anomaly lotheir generalization ability to novel and rare classes. This calization. This two-stage strategy, with the help of residlimitation is particularly challenging in real-world scenarios ual adapters, gradually adapts CLIP in a controlled manwhere collecting comprehensive labeled datasets for AD is * Corresponding author. often infeasible, necessitating the exploration of low-shot 1 learning and transfer learning approaches. hancing its capability to handle fine-grained AD tasks withContrastive Language-Image Pretraining (CLIP) model out sacrificing its generalization ability. has emerged as a promising solution, demonstrating reOur extensive experiments in both industrial and medimarkable generalization capabilities across various zerocal domains demonstrate that our straightforward approach shot tasks [23–25, 41]. Building upon CLIP’s success, equips CLIP with improved zero-shot AD ability, even in several recent studies have adapted CLIP for few/zero-shot data-limited scenarios. By training with a minimal samAD tasks by utilizing anomaly-related descriptions to guide ple — such as one normal sample and one an

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

- PDF: [`Ma_2025_AA-CLIP.pdf`](../PDFs/Ma_2025_AA-CLIP.pdf)
- Extracted text: [`ma-2025-aa-clip.txt`](../text/ma-2025-aa-clip.txt)
- Suggested grep queries:
  - `AA-CLIP`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
