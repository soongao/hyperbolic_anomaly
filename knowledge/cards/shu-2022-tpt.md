---
id: shu-2022-tpt
title: "Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models"
year: "2022"
area: "TTA / VLM"
priority: "method"
tags: ["prompt-learning", "tta", "tta-vlm", "vlm", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Shu_2022_TPT.pdf"
text: "text/shu-2022-tpt.txt"
source: "https://arxiv.org/pdf/2209.07511"
pages: 20
bytes: 1673797
sha256: 979895ca50cabd1b55fa86e82f47510cd045b4cd9b741e58e480387a2adff6dd
---

# Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models

## Why This Paper Is Here

- Area: `TTA / VLM`
- Priority: `method`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Pre-trained vision-language models (e.g., CLIP) have shown promising zero-shot generalization in many downstream tasks with properly designed text prompts. Instead of relying on hand-engineered prompts, recent works learn prompts using the training data from downstream tasks. While effective, training on domain- specific data reduces a model’s generalization capability to unseen new domains. In this work, we propose test-time prompt tuning (TPT), a method that can learn adaptive prompts on the fly with a single test sample. For image classification, TPT optimizes the prompt by minimizing the entropy with confidence selection so that the model has consistent predictions across different augmented views of each test sample. In evaluating generalization to natural distribution shifts, TPT improves the zero-shot top-1 accuracy of CLIP by 3.6% on average, surpassing previous prompt tuning approaches that require additional task-specific training data. In evaluating cross-dataset generalization with unseen categories, TPT performs on par with the state-of-the-art approaches that use additional training data. Project page: https://azshue.github.io/TPT/.

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

- PDF: [`Shu_2022_TPT.pdf`](../PDFs/Shu_2022_TPT.pdf)
- Extracted text: [`shu-2022-tpt.txt`](../text/shu-2022-tpt.txt)
- Suggested grep queries:
  - `Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
