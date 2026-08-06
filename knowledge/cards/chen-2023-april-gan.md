---
id: chen-2023-april-gan
title: "APRIL-GAN: A Zero-/Few-Shot Anomaly Classification and Segmentation Method for CVPR 2023 VAND Workshop Challenge"
year: "2023"
area: "CLIP / ZSAD"
priority: "core"
tags: ["anomaly-detection", "clip", "clip-zsad", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Chen_2023_APRIL-GAN.pdf"
text: "text/chen-2023-april-gan.txt"
source: "https://arxiv.org/pdf/2305.17382"
pages: 10
bytes: 3161643
sha256: 33c2229ae178eddb5f1881eb49289145b6326b6e66bc3683ed01953df1bf3d4a
---

# APRIL-GAN: A Zero-/Few-Shot Anomaly Classification and Segmentation Method for CVPR 2023 VAND Workshop Challenge

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

each category. As a result, the zero/few-shot setting plays a In this technical report, we briefly introduce our solution crucial role in bringing AD to practical applications. for the Zero/Few-shot Track of the Visual Anomaly and Novelty Detection (VAND) 2023 Challenge. For industrial viWinCLIP [8], built on the open-source vision-language sual inspection, building a single model that can be rapidly model CLIP [3, 13], is a model that can be rapidly adapted adapted to numerous categories without or with only a few to abundant categories without or with only a handful of normal reference images is a promising research direction. normal images. It assumes that language is able to aid This is primarily because of the vast variety of the product zero/few-shot AD and proposes a window-based strategy to types. For the zero-shot track, we propose a solution based perform segmentation. Taking inspiration from it, we also on the CLIP model by adding extra linear layers. These layfollowed the pattern of language guided AD and employed ers are used to map the image features to the joint embedCLIP as our baseline. ding space, so that they can compare with the text features to generate the anomaly maps. Besides, when the reference Specifically, we adhere to the overall framework of CLIP images are available, we utilize multiple memory banks to for zero-shot classification and employ a combination of store their features and compare them with the features of state and template ensembles to craft our text prompts. In the test images during the testing phase. In this challenge, order to locate the abnormal regions, we introduce extra our method achieved first place in the zero-shot track, espelinear layers to map the image features extracted from the cially excelling in segmentation with an impressive F1 score CLIP image encoder to the linear space where the text feaimprovement of 0.0489 over the second-ranked participant. tures are located. Then, we make similarity comparison beFurthermore, in the few-shot track, we secured the fourth tween the mapped image features and the text features, so position overall, with our classification F1 score of 0.8687 as to obtain the corresponding anomaly maps. For the fewranking first among all participating teams1 . shot case, we retain the extra linear layers of the zero-shot phase and maintain their weights. In addition, we use the image encoder to extract the features of the reference im-

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

- PDF: [`Chen_2023_APRIL-GAN.pdf`](../PDFs/Chen_2023_APRIL-GAN.pdf)
- Extracted text: [`chen-2023-april-gan.txt`](../text/chen-2023-april-gan.txt)
- Suggested grep queries:
  - `APRIL-GAN`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
