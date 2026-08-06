---
id: defard-2021-padim
title: "PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization"
year: "2021"
area: "Industrial AD baseline"
priority: "background"
tags: ["anomaly-detection", "industrial-ad", "industrial-ad-baseline"]
status: unread
pdf: "PDFs/Defard_2021_PaDiM.pdf"
text: "text/defard-2021-padim.txt"
source: "https://arxiv.org/pdf/2011.08785"
pages: 7
bytes: 1201762
sha256: f00a3650715b1478784d93be1ad365e9dbb8bcb7381433404bbaa6b227650bed
---

# PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization

## Why This Paper Is Here

- Area: `Industrial AD baseline`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Modeling, PaDiM, to concurrently detect and localize anomalies in images in a one-class learning setting. PaDiM makes use of a pretrained convolutional neural network (CNN) for patch embedding, and of multivariate Gaussian distributions to get a probabilistic representation of the normal class. It also exploits correlations between the different semantic levels of CNN to better localize anomalies. PaDiM outperforms current state-ofthe-art approaches for both anomaly detection and localization on the MVTec AD and STC datasets. To match real-world visual industrial inspection, we extend the evaluation protocol to assess performance of anomaly localization algorithms on non-aligned dataset. The state-of-the-art performance and low complexity of PaDiM make it a good candidate for many industrial applications. I. I NTRODUCTION Humans are able to detect heterogeneous or unexpected patterns in a set of homogeneous natural images. This task is known as anomaly or novelty detection and has a large number of applications, among which visual industrial inspections. However, anomalies are very rare events on manufacturing Fig. 1. Image samples from the MVTec AD [1]. Left column: normal images lines and cumbersome to detect manually. Therefore, anomaly of Transistor, Capsule and Wood classes. Middle column: images of the same detection automation would enable a constant quality control classes with the ground truth anomalies highlighted in yellow. Right column: by avoiding reduced attention span and facilitating human anomaly heatmaps obtained by our PaDiM model. Yellow areas correspond to the detected anomalies, whereas the blue areas indicate the normality zones. operator work. In this paper, we focus on anomaly detection Best viewed in color. and, in particular, on anomaly localization, mainly in an industrial inspection context. In computer vision, anomaly detection consists in giving an anomaly score to images. Recently, several methods have been proposed to combine Anomaly localization is a more complex task which assigns anomaly localization and detection tasks in a one-class learneach pixel, or each patch of pixels, an anomaly score to ing setting [2]–[5]. However, either they require deep neural output an anomaly map. Thus, anomaly localization yields network training [3], [6] which might be cumbersome, or they more precise and interpretable results. Examples of anomaly use a K-nearest-neighbor (K-NN) algorithm [7] on the entire maps produced by our method to 

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

- PDF: [`Defard_2021_PaDiM.pdf`](../PDFs/Defard_2021_PaDiM.pdf)
- Extracted text: [`defard-2021-padim.txt`](../text/defard-2021-padim.txt)
- Suggested grep queries:
  - `PaDiM`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
