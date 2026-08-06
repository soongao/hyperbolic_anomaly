---
id: gu-2023-anomalygpt
title: "AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models"
year: "2023"
area: "LVLM / SAM anomaly"
priority: "background"
tags: ["anomaly-detection", "industrial-ad", "lvlm", "lvlm-sam-anomaly", "vlm"]
status: unread
pdf: "PDFs/Gu_2023_AnomalyGPT.pdf"
text: "text/gu-2023-anomalygpt.txt"
source: "https://arxiv.org/pdf/2308.15366"
pages: 19
bytes: 14894050
sha256: f05615c13f01c8bd38cb1718e2a7000530402923984b2a2137ee9fbc275e7341
---

# AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models

## Why This Paper Is Here

- Area: `LVLM / SAM anomaly`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Large Vision-Language Models (LVLMs) such as MiniGPT-4 and LLaVA have demonstrated the capability of understanding images and achieved remarkable performance in various visual tasks. Despite their strong abilities in recognizing common objects due to extensive training datasets, they lack specific domain knowledge and have a weaker understanding of localized details within objects, which hinders their effectiveness in the Industrial Anomaly Detection (IAD) task. On the other hand, most existing IAD methods only provide anomaly scores and necessitate the manual setting of thresholds to distinguish between normal and abnormal samples, which restricts their practical implementation. In this paper, we explore the utilization of LVLM to address the IAD problem and propose AnomalyGPT, a novel IAD approach based on LVLM. We generate training data by simulating anomalous images and producing corresponding textual descriptions for each image. We methods and existing LVLMs. Existing IAD methods can only also employ an image decoder to provide fine-grained seprovide anomaly scores and need manually threshold setting, mantic and design a prompt learner to fine-tune the LVLM while existing LVLMs cannot detect anomalies in the image. AnomalyGPT can not only provide information about the image using prompt embeddings. Our AnomalyGPT eliminates but also indicate the presence and location of anomaly. the need for manual threshold adjustments, thus directly assesses the presence and locations of anomalies. Additionally, AnomalyGPT supports multi-turn dialogues and exhibits impressive few-shot in-context learning capabilion a range of Natural Language Processing (NLP) tasks. ties. With only one normal shot, AnomalyGPT achieves the More recently, novel methods including MiniGPT-4 [36], state-of-the-art performance with an accuracy of 86.1%, an BLIP-2 [15], and PandaGPT [25] have further extended the image-level AUC of 94.1%, and a pixel-level AUC of 95.3% ability of LLMs into visual processing by aligning visual on the MVTec-AD dataset. Code is available at https: features with text features, bringing a significant revolu//github.com/CASIA-IVA-Lab/AnomalyGPT. tion in the domain of Artificial General Intelligence (AGI). While LVLMs are pre-trained on amounts of data sourced from the Internet, their domain-specific knowledge is rela-

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

- PDF: [`Gu_2023_AnomalyGPT.pdf`](../PDFs/Gu_2023_AnomalyGPT.pdf)
- Extracted text: [`gu-2023-anomalygpt.txt`](../text/gu-2023-anomalygpt.txt)
- Suggested grep queries:
  - `AnomalyGPT`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
