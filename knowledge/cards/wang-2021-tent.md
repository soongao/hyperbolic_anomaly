---
id: wang-2021-tent
title: "Tent: Fully Test-Time Adaptation by Entropy Minimization"
year: "2021"
area: "TTA"
priority: "method"
tags: ["tta"]
status: unread
pdf: "PDFs/Wang_2021_TENT.pdf"
text: "text/wang-2021-tent.txt"
source: "https://arxiv.org/pdf/2006.10726"
pages: 15
bytes: 6448675
sha256: 215223e9885dd7208cad9dbff2cf315f1cc96554fedc4660d0d2c4932364e5f7
---

# Tent: Fully Test-Time Adaptation by Entropy Minimization

## Why This Paper Is Here

- Area: `TTA`
- Priority: `method`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

A model must adapt itself to generalize to new and different data during testing. In this setting of fully test-time adaptation the model has only the test data and its own parameters. We propose to adapt by test entropy minimization (tent1 ): we optimize the model for confidence as measured by the entropy of its predictions. Our method estimates normalization statistics and optimizes channel-wise affine transformations to update online on each batch. Tent reduces generalization error for image classification on corrupted ImageNet and CIFAR-10/100 and reaches a new state-of-the-art error on ImageNet-C. Tent handles source-free domain adaptation on digit recognition from SVHN to MNIST/MNIST-M/USPS, on semantic segmentation from GTA to Cityscapes, and on the VisDA-C benchmark. These results are achieved in one epoch of test-time optimization without altering training.

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

- PDF: [`Wang_2021_TENT.pdf`](../PDFs/Wang_2021_TENT.pdf)
- Extracted text: [`wang-2021-tent.txt`](../text/wang-2021-tent.txt)
- Suggested grep queries:
  - `Tent`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
