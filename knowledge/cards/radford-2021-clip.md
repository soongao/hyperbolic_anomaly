---
id: radford-2021-clip
title: "Learning Transferable Visual Models From Natural Language Supervision"
year: "2021"
area: "CLIP / ZSAD"
priority: "supporting"
tags: ["clip", "clip-zsad", "zsad"]
status: unread
pdf: "PDFs/Radford_2021_CLIP.pdf"
text: "text/radford-2021-clip.txt"
source: "https://arxiv.org/pdf/2103.00020"
pages: 48
bytes: 6813639
sha256: 6478b6e571a7d6fcd846d8ef77bfd60c285f1986abb8f475eedc43de403074f5
---

# Learning Transferable Visual Models From Natural Language Supervision

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `supporting`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

language modeling have scaled across many orders of magState-of-the-art computer vision systems are nitude in compute, model capacity, and data, steadily imtrained to predict a fixed set of predetermined proving capabilities. The development of “text-to-text” as object categories. This restricted form of supera standardized input-output interface (McCann et al., 2018; vision limits their generality and usability since Radford et al., 2019; Raffel et al., 2019) has enabled taskadditional labeled data is needed to specify any agnostic architectures to zero-shot transfer to downstream other visual concept. Learning directly from raw datasets removing the need for specialized output heads or text about images is a promising alternative which dataset specific customization. Flagship systems like GPT-3 leverages a much broader source of supervision. (Brown et al., 2020) are now competitive across many tasks We demonstrate that the simple pre-training task with bespoke models while requiring little to no dataset of predicting which caption goes with which imspecific training data. age is an efficient and scalable way to learn SOTA image representations from scratch on a dataset These results suggest that the aggregate supervision accesof 400 million (image, text) pairs collected from sible to modern pre-training methods within web-scale colthe internet. After pre-training, natural language lections of text surpasses that of high-quality crowd-labeled is used to reference learned visual concepts (or NLP datasets. However, in other fields such as computer describe new ones) enabling zero-shot transfer vision it is still standard practice to pre-train models on of the model to downstream tasks. We study crowd-labeled datasets such as ImageNet (Deng et al., 2009). the performance of this approach by benchmarkCould scalable pre-training methods which learn directly ing on over 30 different existing computer vifrom web text result in a similar breakthrough in computer sion datasets, spanning tasks such as OCR, acvision? Prior work is encouraging. tion recognition in videos, geo-localization, and Over 20 years ago Mori et al. (1999) explored improving many types of fine-grained object classification. content based image retrieval by training a model to preThe model transfers non-trivially to most tasks dict the nouns and adjectives in text documents paired with and is often competitive with a fully supervised images. Quattoni et al. (2007) demonstrated it was possibasel

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

- PDF: [`Radford_2021_CLIP.pdf`](../PDFs/Radford_2021_CLIP.pdf)
- Extracted text: [`radford-2021-clip.txt`](../text/radford-2021-clip.txt)
- Suggested grep queries:
  - `Learning Transferable Visual Models From Natural Language Supervision`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
