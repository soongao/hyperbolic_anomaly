---
id: qin-2021-fcanet
title: "FcaNet: Frequency Channel Attention Networks"
year: "2021"
area: "Wavelet / frequency"
priority: "supporting"
tags: ["frequency", "tta", "wavelet-frequency"]
status: unread
pdf: "PDFs/Qin_2021_FcaNet.pdf"
text: "text/qin-2021-fcanet.txt"
source: "https://arxiv.org/pdf/2012.11879"
pages: 10
bytes: 431451
sha256: 4fa7d59499e95d4ca85b7af63ce3dd43e50325e0b26212e913b56676207ffbf5
---

# FcaNet: Frequency Channel Attention Networks

## Why This Paper Is Here

- Area: `Wavelet / frequency`
- Priority: `supporting`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

Ours 80.02 80 SENet 79.63 Attention mechanism, especially channel attention, has ResNet 79.84 gained great success in the computer vision field. Many 79 78.57 79.19 79.39 works focus on how to design efficient channel attention 78.72 78 Top-1 accuracy mechanisms while ignoring a fundamental problem, i.e., 77.86 channel attention mechanism uses scalar to represent chan77 77.27 nel, which is difficult due to massive information loss. In 76 this work, we start from a different view and regard the 75.02 channel representation problem as a compression process 75 74.83 using frequency analysis. Based on the frequency analy74.58 74 sis, we mathematically prove that the conventional global 34-layer 50-layer 101-layer 152-layer average pooling is a special case of the feature decomposi73 10 20 30 40 50 60 70 tion in the frequency domain. With the proof, we naturally Number of parameters (millions) generalize the compression of the channel attention mechanism in the frequency domain and propose our method with the same number of parameters and computational cost, our multi-spectral channel attention, termed as FcaNet. FcaNet method consistently outperforms the baseline SENet. is simple but effective. We can change a few lines of code in the calculation to implement our method within existing channel attention methods. Moreover, the proposed method to different feature dimensions. Due to the simplicity and achieves state-of-the-art results compared with other chaneffectiveness in feature modeling, channel attention directly nel attention methods on image classification, object deteclearns to attach importance weights with different channels, tion, and instance segmentation tasks. Our method could becoming a popular and powerful tool for the deep learning consistently outperform the baseline SENet, with the same community. number of parameters and the same computational cost. Typically, a core step of channel attention approaches Our code and models will are publicly available at https: is to use a scalar for each channel to conduct the calcu//github.com/cfzd/FcaNet. lation due to the constrained computational overhead, and global average pooling (GAP) becomes the de-facto standard choice in the deep learning community because of its

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

- PDF: [`Qin_2021_FcaNet.pdf`](../PDFs/Qin_2021_FcaNet.pdf)
- Extracted text: [`qin-2021-fcanet.txt`](../text/qin-2021-fcanet.txt)
- Suggested grep queries:
  - `FcaNet`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
