---
id: wang-2022-cotta
title: "Continual Test-Time Domain Adaptation"
year: "2022"
area: "TTA"
priority: "background"
tags: ["domain-adaptation", "tta"]
status: unread
pdf: "PDFs/Wang_2022_CoTTA.pdf"
text: "text/wang-2022-cotta.txt"
source: "https://arxiv.org/pdf/2203.13591"
pages: 11
bytes: 730640
sha256: 1ea9b03876b9db4df6575dccefc1c6032da4165ad0a00ea5bbf3176fc5adc50e
---

# Continual Test-Time Domain Adaptation

## Why This Paper Is Here

- Area: `TTA`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Test-time domain adaptation aims to adapt a source pretrained model to a target domain without using any source data. Existing works mainly consider the case where the target domain is static. However, real-world machine perception systems are running in non-stationary and continually changing environments where the target domain distribution can change over time. Existing methods, which are mostly based on self-training and entropy regularization, can suffer from these non-stationary environments. Due to the distribution shift over time in the target domain, pseudo-labels become unreliable. The noisy pseudolabels can further lead to error accumulation and catastrophic forgetting. To tackle these issues, we propose a continual test-time adaptation approach (CoTTA) which comprises two parts. Firstly, we propose to reduce the error accumulation by using weight-averaged and augmentationscenario. The target data is provided in a sequence and from a averaged predictions which are often more accurate. On continually changing environment. An off-the-shelf source pretrained network is used to initialize the target network. The model the other hand, to avoid catastrophic forgetting, we prois updated online based on the current target data, and the predicpose to stochastically restore a small part of the neurons to tions are given in an online fashion. The adaptation of the target the source pre-trained weights during each iteration to help network does not rely on any source data. Existing methods often preserve source knowledge in the long-term. The proposed suffer from error accumulation and forgetting which result in permethod enables the long-term adaptation for all parameformance deterioration over time. Our method enables long-term ters in the network. CoTTA is easy to implement and can be test-time adaptation under continually changing environments. readily incorporated in off-the-shelf pre-trained models. We demonstrate the effectiveness of our approach on four clasclear weather conditions can suffer significant performance sification tasks and a segmentation task for continual testdeterioration when tested on snowy night conditions [50]. time adaptation, on which we outperform existing methods. Similarly, a pre-trained image classification model can also Our code is available at https://qin.ee/cotta. suffer this phenomenon when tested on corrupted images resulting from sensor degradation. Due to privacy concerns or legal constraints, the source data is gen

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

- PDF: [`Wang_2022_CoTTA.pdf`](../PDFs/Wang_2022_CoTTA.pdf)
- Extracted text: [`wang-2022-cotta.txt`](../text/wang-2022-cotta.txt)
- Suggested grep queries:
  - `Continual Test-Time Domain Adaptation`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
