---
id: qiu-2026-freqanchorad
title: "FreqAnchorAD: Language-Free Zero-Shot Anomaly Detection via Frequency-Deviation Anchoring"
year: "2026"
area: "Frequency / ZSAD"
priority: "core"
tags: ["anomaly-detection", "frequency", "frequency-zsad", "zero-shot", "zsad"]
status: unread
pdf: "PDFs/Qiu_2026_FreqAnchorAD.pdf"
text: "text/qiu-2026-freqanchorad.txt"
source: "https://arxiv.org/pdf/2608.00695"
pages: 9
bytes: 3810236
sha256: 5d5e40297b6613bb775a0fad8995ad24ac3eac5fcfb12ed1b28a4bd35cd75302
---

# FreqAnchorAD: Language-Free Zero-Shot Anomaly Detection via Frequency-Deviation Anchoring

## Why This Paper Is Here

- Area: `Frequency / ZSAD`
- Priority: `core`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

collecting sufficient and clean normal data for each target cat- egory is often challenging in real-world deployments. This Zero-shot anomaly detection (ZSAD) aims to detect anoma- lous samples and localize defective regions in unseen tar- motivates zero-shot anomaly detection (ZSAD), which aims get domains without using target training data. Many recent to detect and localize anomalies without using any target- ZSAD methods build on pretrained vision models, particularly domain training samples (Li et al. 2024; Cao et al. 2023). CLIP, and construct normal and anomaly references using tex- This problem is challenging due to domain shifts across arXiv:2608.00695v1 [cs.CV] 1 Aug 2026 tual prompts or learnable visual representations. Text-guided unseen categories, diverse anomaly appearances, and subtle and visual-reference methods perform anomaly discrimina- local defects. Most ZSAD methods build on CLIP (Radford tion primarily in spatial feature spaces, where subtle changes et al. 2021), whose transferable representations provide use- in texture, boundaries, and local structures are difficult to dis- tinguish from normal appearance variations. Although such ful priors for unseen categories. Text-guided methods (Jeong defects are inconspicuous in the spatial domain, they can dis- et al. 2023; Chen, Han, and Zhang 2023; Chen et al. 2023; Qu rupt local texture regularity or boundary continuity, thereby et al. 2024; Gu et al. 2024; Cao et al. 2024; Ma et al. 2025) inducing distinguishable response deviations across different construct normal and anomaly references through textual frequency bands. However, these frequency-dependent char- prompts. In contrast, VisualAD (Hou et al. 2026) removes the acteristics are not explicitly modeled by existing ZSAD meth- language branch and learns purely visual references, result- ods. Our image-domain analysis reveals that local defects ing in a simpler framework with strong ZSAD performance. exhibit spatial-frequency deviations from their normal ref- Despite their different reference construction strategies, both erences across low-, middle-, and high-frequency bands, indi- paradigms discriminate anomalies primarily in spatial fea- cating that anomaly evidence is not universally dominated by ture spaces. In these spaces, subtle texture, boundary, and high-frequency responses. Motivated by this observation, we propose FreqAnchorAD, a frequency-aware framework cen- local structural changes can be difficult to distinguish fro

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

- PDF: [`Qiu_2026_FreqAnchorAD.pdf`](../PDFs/Qiu_2026_FreqAnchorAD.pdf)
- Extracted text: [`qiu-2026-freqanchorad.txt`](../text/qiu-2026-freqanchorad.txt)
- Suggested grep queries:
  - `FreqAnchorAD`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
