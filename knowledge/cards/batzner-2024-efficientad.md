---
id: batzner-2024-efficientad
title: "EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies"
year: "2024"
area: "Industrial AD baseline"
priority: "background"
tags: ["anomaly-detection", "industrial-ad", "industrial-ad-baseline"]
status: unread
pdf: "PDFs/Batzner_2024_EfficientAD.pdf"
text: "text/batzner-2024-efficientad.txt"
source: "https://arxiv.org/pdf/2303.14535"
pages: 27
bytes: 13042722
sha256: d7658c53a9ccdbcd3a5bc56f1943b42c912f74c4a792c6498985a52b9135b5b6
---

# EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies

## Why This Paper Is Here

- Area: `Industrial AD baseline`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

EfficientAD-S Detecting anomalies in images is an important task, es94 AU-ROC [%] pecially in real-time computer vision applications. In this work, we focus on computational efficiency and propose AST PatchCoreEns 92 a lightweight feature extractor that processes an image in PatchCore less than a millisecond on a modern GPU. We then use a DSR 90 FastFlow student–teacher approach to detect anomalous features. We train a student network to predict the extracted features of S-T 88 SimpleNet normal, i.e., anomaly-free training images. The detection of anomalies at test time is enabled by the student failing to 100 101 102 103 predict their features. We propose a training loss that hinLatency [ms] ders the student from imitating the teacher feature extractor beyond the normal images. It allows us to drastically reduce the computational cost of the student–teacher model, while an NVIDIA RTX A6000 GPU. Each AU-ROC value is an average of the image-level detection AU-ROC values on the MVTec AD improving the detection of anomalous features. We further[7, 9], VisA [74], and MVTec LOCO [8] dataset collections. more address the detection of challenging logical anomalies that involve invalid combinations of normal local features, for example, a wrong ordering of objects. We detect these putational requirements remain suitable for real-world apanomalies by efficiently incorporating an autoencoder that plications. The field of visual anomaly detection has also analyzes images globally. We evaluate our method, called seen rapid progress in the recent past, especially on indusEfficientAD, on 32 datasets from three industrial anomaly trial anomaly detection benchmarks [7, 9, 51, 54]. State-ofdetection dataset collections. EfficientAD sets new stanthe-art anomaly detection methods, however, often sacrifice dards for both the detection and the localization of anomacomputational efficiency for an increased anomaly deteclies. At a latency of two milliseconds and a throughput of tion performance. Common techniques are ensembling, the six hundred images per second, it enables a fast handling use of large backbones, and increasing the input image resof anomalies. Together with its low error rate, this makes olution to up to 768×768 pixels. it an economical solution for real-world applications and a Real-world anomaly detection applications frequently fruitful basis for future research. put constraints on the computational requirements of a method. There are cases where detecting an

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

- PDF: [`Batzner_2024_EfficientAD.pdf`](../PDFs/Batzner_2024_EfficientAD.pdf)
- Extracted text: [`batzner-2024-efficientad.txt`](../text/batzner-2024-efficientad.txt)
- Suggested grep queries:
  - `EfficientAD`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
