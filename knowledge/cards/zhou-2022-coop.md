---
id: zhou-2022-coop
title: "Learning to Prompt for Vision-Language Models"
year: "2022"
area: "Prompt / VLM support"
priority: "background"
tags: ["prompt-learning", "prompt-vlm-support", "vlm"]
status: unread
pdf: "PDFs/Zhou_2022_CoOp.pdf"
text: "text/zhou-2022-coop.txt"
source: "https://arxiv.org/pdf/2109.01134"
pages: 13
bytes: 1465481
sha256: 12970ca0d5d19aef15bcdd327a7af279c74ed07d4b924e44e6c01640c3dcb05c
---

# Learning to Prompt for Vision-Language Models

## Why This Paper Is Here

- Area: `Prompt / VLM support`
- Priority: `background`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

like CLIP have shown great potential in learning represpecific context. Through extensive experiments on 11 sentations that are transferable across a wide range of datasets, we demonstrate that CoOp requires as few as downstream tasks. Different from the traditional repreone or two shots to beat hand-crafted prompts with a sentation learning that is based mostly on discretized decent margin and is able to gain significant improvelabels, vision-language pre-training aligns images and ments over prompt engineering with more shots, e.g., texts in a common feature space, which allows zerowith 16 shots the average gain is around 15% (with the shot transfer to a downstream task via prompting, i.e., highest reaching over 45%). Despite being a learningclassification weights are synthesized from natural lanbased approach, CoOp achieves superb domain generalguage describing classes of interest. In this work, we ization performance compared with the zero-shot model show that a major challenge for deploying such modusing hand-crafted prompts. els in practice is prompt engineering, which requires domain expertise and is extremely time-consuming— one needs to spend a significant amount of time on 1 Introduction words tuning since a slight change in wording could have a huge impact on performance. Inspired by reA common approach for building state-of-the-art visual cent advances in prompt learning research in natural recognition systems is to train vision models to predict language processing (NLP), we propose Context Opfor a fixed set of object categories using discrete latimization (CoOp), a simple approach specifically for bels (He et al., 2016; Dosovitskiy et al., 2021). From adapting CLIP-like vision-language models for downa technical point of view, this is achieved by matchstream image recognition. Concretely, CoOp models a ing image features—produced by a vision model like prompt’s context words with learnable vectors while the ResNet (He et al., 2016) or ViT (Dosovitskiy et al., entire pre-trained parameters are kept fixed. To han2021)—with a fixed set of weights that are seen as visual dle different image recognition tasks, we provide two concepts and initialized randomly. Although training categories often have a textual form, such as “goldfish” Kaiyang Zhou or “toilet paper,” they will be converted into discrete laS-Lab, Nanyang Technological University, Singapore bels just for easing the computation of the cross-entropy E-mail: kaiyang.zhou@ntu.edu.sg loss, 

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

- PDF: [`Zhou_2022_CoOp.pdf`](../PDFs/Zhou_2022_CoOp.pdf)
- Extracted text: [`zhou-2022-coop.txt`](../text/zhou-2022-coop.txt)
- Suggested grep queries:
  - `Learning to Prompt for Vision-Language Models`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
