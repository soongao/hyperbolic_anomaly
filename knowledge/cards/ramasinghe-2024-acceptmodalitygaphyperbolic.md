---
id: ramasinghe-2024-acceptmodalitygaphyperbolic
title: "Accept the Modality Gap: An Exploration in the Hyperbolic Space"
year: "2024"
area: "Hyperbolic VLM"
priority: "supporting"
tags: ["hyperbolic", "hyperbolic-vlm"]
status: unread
pdf: "PDFs/Ramasinghe_2024_AcceptModalityGapHyperbolic.pdf"
text: "text/ramasinghe-2024-acceptmodalitygaphyperbolic.txt"
source: "https://openaccess.thecvf.com/content/CVPR2024/papers/Ramasinghe_Accept_the_Modality_Gap_An_Exploration_in_the_Hyperbolic_Space_CVPR_2024_paper.pdf"
pages: 10
bytes: 1293383
sha256: c76ea0a1199044c5272c10720b20685e750f207997a13e02fcd2c481dc52d346
---

# Accept the Modality Gap: An Exploration in the Hyperbolic Space

## Why This Paper Is Here

- Area: `Hyperbolic VLM`
- Priority: `supporting`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Recent advancements in machine learning have spotlighted the potential of hyperbolic spaces as they effectively learn hierarchical feature representations. While there has been progress in leveraging hyperbolic spaces in singlemodality contexts, its exploration in multimodal settings remains under explored. A recent work has sought to transpose Euclidean multimodal learning techniques to hyperbolic spaces, by adopting a geodesic distance based contrastive loss. However, we show both theoretically and emangle-based contrastive losses (right) in the hyperbolic space. pirically that such spatial proximity based contrastive loss Only the space component is shown for clarity. In our angle-based significantly disrupts hierarchies in the latent space. To contrastive loss (details in Fig. 3), the images can be placed anyremedy this, we advocate that the cross-modal representawhere along the axis emanating from the text embedding (hightions should accept the inherent modality gap between text lighted in yellow), which allows hierarchy among images. and images, and introduce a novel approach to measure cross-modal similarity that does not enforce spatial proxembeddings through spatial proximity in the underlying imity. Our approach shows remarkable capabilities in preshared embedding space. Such spatial proximity based conserving unimodal hierarchies while aligning the two modaltrastive loss clusters matching concepts across modalities ities. Our experiments on a series of downstream tasks together, while pushing apart non-matching ones. Despite demonstrate that a better latent structure emerges with our wide-spread usage, the alignment between image and text objective function while being superior in text-to-image and modalities is an ill-posed problem, and these learned repreimage-to-text retrieval tasks. sentations are shown to have misalignment between modalities, defined as the modality-gap [23]. We argue that modality gap is rooted in the intrinsic dif-

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

- PDF: [`Ramasinghe_2024_AcceptModalityGapHyperbolic.pdf`](../PDFs/Ramasinghe_2024_AcceptModalityGapHyperbolic.pdf)
- Extracted text: [`ramasinghe-2024-acceptmodalitygaphyperbolic.txt`](../text/ramasinghe-2024-acceptmodalitygaphyperbolic.txt)
- Suggested grep queries:
  - `Accept the Modality Gap`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
