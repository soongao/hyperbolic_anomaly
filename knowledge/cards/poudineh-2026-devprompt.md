---
id: poudineh-2026-devprompt
title: "DevPrompt: Deviation-Based Prompt Learning for One-Normal Shot Image Anomaly Detection"
year: "2026"
area: "CLIP / ZSAD"
priority: "supporting"
tags: ["anomaly-detection", "clip", "clip-zsad", "prompt-learning", "zsad"]
status: unread
pdf: "PDFs/Poudineh_2026_DevPrompt.pdf"
text: "text/poudineh-2026-devprompt.txt"
source: "https://arxiv.org/pdf/2601.15453"
pages: 9
bytes: 806112
sha256: 8c49b6f649679d573508893050ddabf51dad1d9160c5ef2a3511c5c2d0f1bcba
---

# DevPrompt: Deviation-Based Prompt Learning for One-Normal Shot Image Anomaly Detection

## Why This Paper Is Here

- Area: `CLIP / ZSAD`
- Priority: `supporting`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Few-normal shot anomaly detection (FNSAD) aims to detect abnormal regions in images using only a few normal training samples, making the task highly challenging due to limited supervision and the diversity of potential defects. Recent approaches leverage vision-language models such as CLIP with prompt-based learning to align image and text features. However, existing methods often exhibit weak discriminability between normal and abnormal prompts and lack principled scoring mechanisms for patch-level anomalies. We propose a deviation-guided prompt learning framework that integrates the semantic power of vision-language models with the statistical re- liability of deviation-based scoring. Specifically, we replace fixed prompt prefixes with learnable context vectors shared across normal and abnormal prompts, while anomaly-specific suﬀix to- kens enable class-aware alignment. To enhance separability, we introduce a deviation loss with Top-K Multiple Instance Learning (MIL), modeling patch-level features as Gaussian deviations from the normal distribution. This allows the network to assign higher anomaly scores to patches with statistically significant deviations, improving localization and interpretability. Experiments on the MVTecAD and VISA benchmarks demonstrate superior pixel-level detection performance compared to PromptAD and other baselines. Ablation studies further validate the effectiveness of learnable prompts, deviation-based scoring, and the Top-K MIL strategy.

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

- PDF: [`Poudineh_2026_DevPrompt.pdf`](../PDFs/Poudineh_2026_DevPrompt.pdf)
- Extracted text: [`poudineh-2026-devprompt.txt`](../text/poudineh-2026-devprompt.txt)
- Suggested grep queries:
  - `DevPrompt`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
