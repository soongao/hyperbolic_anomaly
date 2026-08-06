---
id: zhang-2022-memo
title: "MEMO: Test Time Robustness via Adaptation and Augmentation"
year: "2022"
area: "TTA"
priority: "background"
tags: ["tta"]
status: unread
pdf: "PDFs/Zhang_2022_MEMO.pdf"
text: "text/zhang-2022-memo.txt"
source: "https://arxiv.org/pdf/2110.09506"
pages: 17
bytes: 2208864
sha256: a3a238dbe414fa40ec19e444b24af34853565d88173539017cd2a15fef88fbe6
---

# MEMO: Test Time Robustness via Adaptation and Augmentation

## Why This Paper Is Here

- Area: `TTA`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

While deep neural networks can attain good accuracy on in-distribution test points, many applications require robustness even in the face of unexpected perturbations in the input, changes in the domain, or other sources of distribution shift. We study the problem of test time robustification, i.e., using the test input to improve model robustness. Recent prior works have proposed methods for test time adaptation, however, they each introduce additional assumptions, such as access to multiple test points, that prevent widespread adoption. In this work, we aim to study and devise methods that make no assumptions about the model training process and are broadly applicable at test time. We propose a simple approach that can be used in any test setting where the model is probabilistic and adaptable: when presented with a test example, perform different data augmentations on the data point, and then adapt (all of) the model parameters by minimizing the entropy of the model’s average, or marginal, output distribution across the augmentations. Intuitively, this objective encourages the model to make the same prediction across different augmentations, thus enforcing the invariances encoded in these augmentations, while also maintaining confidence in its predictions. In our experiments, we evaluate two baseline ResNet models, two robust ResNet-50 models, and a robust vision transformer model, and we demonstrate that this approach achieves accuracy gains of 1-8% over standard model evaluation and also generally outperforms prior augmentation and adaptation strategies. For the setting in which only one test point is available, we achieve state-of-the-art results on the ImageNet-C, ImageNet-R, and, among ResNet-50 models, ImageNet-A distribution shift benchmarks.

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

- PDF: [`Zhang_2022_MEMO.pdf`](../PDFs/Zhang_2022_MEMO.pdf)
- Extracted text: [`zhang-2022-memo.txt`](../text/zhang-2022-memo.txt)
- Suggested grep queries:
  - `MEMO`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
