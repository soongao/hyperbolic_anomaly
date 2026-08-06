---
id: zavrtanik-2021-draem
title: "DRAEM: A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection"
year: "2021"
area: "Industrial AD baseline"
priority: "background"
tags: ["anomaly-detection", "industrial-ad", "industrial-ad-baseline"]
status: unread
pdf: "PDFs/Zavrtanik_2021_DRAEM.pdf"
text: "text/zavrtanik-2021-draem.txt"
source: "https://arxiv.org/pdf/2108.07610"
pages: 10
bytes: 21228840
sha256: 6836e5fdf46f3aa8f2f4dc2d016170b14d627c751eb9d38d72fda71d7526cbc2
---

# DRAEM: A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection

## Why This Paper Is Here

- Area: `Industrial AD baseline`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Visual surface anomaly detection aims to detect local image regions that significantly deviate from normal appearance. Recent surface anomaly detection methods rely on generative models to accurately reconstruct the normal areas and to fail on anomalies. These methods are trained only on anomaly-free images, and often require hand-crafted post-processing steps to localize the anomalies, which prohibits optimizing the feature extraction for maximal detection capability. In addition to reconstructive approach, we cast surface anomaly detection primarily as a discriminative problem and propose a discriminatively trained reconstruction anomaly embedding model (DRÆM). The proposed method learns a joint representation of an anomalous image and its anomaly-free reconstruction, while simultaneously learning a decision boundary between normal and anomalous examples. The method normal an anomalous pixels solely by training on synthetic anomaenables direct anomaly localization without the need for lies automatically generated on anomaly-free images (left) and additional complicated post-processing of the network outgeneralizes to a variety of real-world anomalies (right). The reput and can be trained using simple and general anomaly sult (Mo ) closely matches the ground truth (GT). simulations. On the challenging MVTec anomaly detection dataset, DRÆM outperforms the current state-of-theart unsupervised methods by a large margin and even delarly challenging task, which is common in quality control livers detection performance close to the fully-supervised and surface defect localization applications. methods on the widely used DAGM surface-defect detection In practice, anomaly appearances may significantly vary, dataset, while substantially outperforming them in localizaand in applications like quality control, images with anomation accuracy. lies present are rare and manual annotation may be overly time consuming. This leads to highly imbalanced training sets, often containing only anomaly-free images. Signifi-

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

- PDF: [`Zavrtanik_2021_DRAEM.pdf`](../PDFs/Zavrtanik_2021_DRAEM.pdf)
- Extracted text: [`zavrtanik-2021-draem.txt`](../text/zavrtanik-2021-draem.txt)
- Suggested grep queries:
  - `DRAEM`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
