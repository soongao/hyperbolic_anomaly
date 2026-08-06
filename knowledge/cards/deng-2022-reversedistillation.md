---
id: deng-2022-reversedistillation
title: "Anomaly Detection via Reverse Distillation from One-Class Embedding"
year: "2022"
area: "Industrial AD baseline"
priority: "background"
tags: ["anomaly-detection", "industrial-ad", "industrial-ad-baseline"]
status: unread
pdf: "PDFs/Deng_2022_ReverseDistillation.pdf"
text: "text/deng-2022-reversedistillation.txt"
source: "https://arxiv.org/pdf/2201.10703"
pages: 10
bytes: 5889718
sha256: fae710735be6abc8615d5ffc1105951d1b93e1a17eb3f6f9db981f867fb42952
---

# Anomaly Detection via Reverse Distillation from One-Class Embedding

## Why This Paper Is Here

- Area: `Industrial AD baseline`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Knowledge distillation (KD) achieves promising results on the challenging problem of unsupervised anomaly detection (AD). The representation discrepancy of anomalies in the teacher-student (T-S) model provides essential evidence for AD. However, using similar or identical architectures to build the teacher and student models in previous studies hinders the diversity of anomalous representations. To tackle this problem, we propose a novel T-S model consisting of a teacher encoder and a student decoder and introduce a simple yet effective ”reverse distillation” paradigm olution Knowledge Distillation (MKD) [33] adopts the convenaccordingly. Instead of receiving raw images directly, the tional KD architecture in Fig. Fig. 2(a). Our reverse distillation student network takes teacher model’s one-class embedmethod is capable of precisely localising a variate of anomalies. ding as input and targets to restore the teacher’s multiscale representations. Inherently, knowledge distillation in this study starts from abstract, high-level presentations to tation [23, 42, 46], knowledge distillation [4, 33, 39], etc. low-level features. In addition, we introduce a trainable In this study, we tackle the problem of unsupervised one-class bottleneck embedding (OCBE) module in our T-S anomaly detection from the knowledge distillation-based model. The obtained compact embedding effectively prepoint of view. In knowledge distillation (KD) [6, 15], serves essential information on normal patterns, but abanknowledge is transferred within a teacher-student (T-S) pair. dons anomaly perturbations. Extensive experimentation on In the context of unsupervised AD, since the student expeAD and one-class novelty detection benchmarks shows that riences only normal samples during training, it is likely to our method surpasses SOTA performance, demonstrating generate discrepant representations from the teacher when our proposed approach’s effectiveness and generalizability. a query is anomalous. This hypothesis forms the basis of KD-based methods for anomaly detection. However, this hypothesis is not always true in practice due to (1) the identical or similar architectures of the teacher and student

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

- PDF: [`Deng_2022_ReverseDistillation.pdf`](../PDFs/Deng_2022_ReverseDistillation.pdf)
- Extracted text: [`deng-2022-reversedistillation.txt`](../text/deng-2022-reversedistillation.txt)
- Suggested grep queries:
  - `Anomaly Detection via Reverse Distillation from One-Class Embedding`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
