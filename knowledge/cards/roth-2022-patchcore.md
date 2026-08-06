---
id: roth-2022-patchcore
title: "Towards Total Recall in Industrial Anomaly Detection"
year: "2022"
area: "Industrial AD baseline"
priority: "background"
tags: ["anomaly-detection", "industrial-ad", "industrial-ad-baseline"]
status: unread
pdf: "PDFs/Roth_2022_PatchCore.pdf"
text: "text/roth-2022-patchcore.txt"
source: "https://arxiv.org/pdf/2106.08265"
pages: 18
bytes: 15850530
sha256: 371ef2388859aa2a102442c37f55cc6f4a87350ae83036b3174ea0726c3ccddd
---

# Towards Total Recall in Industrial Anomaly Detection

## Why This Paper Is Here

- Area: `Industrial AD baseline`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Being able to spot defective parts is a critical component in large-scale industrial manufacturing. A particular challenge that we address in this work is the cold-start problem: fit a model using nominal (non-defective) example images only. While handcrafted solutions per class are possible, the goal is to build systems that work well simultaneously on many different tasks automatically. The best peforming approaches combine embeddings from ImageNet models with an outlier detection model. In this paper, we extend on this line of work and propose PatchCore, which uses a maximally representative memory bank of nominal patchfeatures. PatchCore offers competitive inference times while achieving state-of-the-art performance for both detection imposed on the images are the segmentation results from Patchand localization. On the challenging, widely used MVTec Core. The orange boundary denotes anomaly contours of actual AD benchmark PatchCore achieves an image-level anomaly segmentation maps for anomalies such as broken glass, scratches, detection AUROC score of up to 99.6%, more than halving burns or structural changes in blue-orange color gradients. the error compared to the next best competitor. We further report competitive results on two additional datasets and also find competitive results in the few samples regime. vary from subtle changes such as thin scratches to larger Code: github.com/amazon-research/patchcore-inspection. structural defects like missing components [5]. Some examples from the MVTec AD benchmark along with results from our proposed method are shown in work on cold-start, industrial visual anomaly detection re-

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

- PDF: [`Roth_2022_PatchCore.pdf`](../PDFs/Roth_2022_PatchCore.pdf)
- Extracted text: [`roth-2022-patchcore.txt`](../text/roth-2022-patchcore.txt)
- Suggested grep queries:
  - `Towards Total Recall in Industrial Anomaly Detection`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
