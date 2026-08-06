# ZSAD Knowledge Base

Generated: 2026-08-06

This knowledge base is organized for both human reading and agent retrieval.

## Fast Entry Points

- `PDFs/`: original downloaded PDFs.
- `text/`: extracted full text, one file per PDF, optimized for `rg` search.
- `cards/`: one Markdown card per paper with metadata, abstract, and reading-note slots.
- `metadata/papers.jsonl`: agent-friendly paper registry.
- `metadata/papers.csv`: spreadsheet-friendly paper registry.
- `agent_guide.md`: rules for future agents using this knowledge base.
- `human_guide.md`: practical reading workflow for humans.
- `taxonomy.md`: topic clusters and recommended first-pass reading order.

## Papers By Area

### CLIP / ZSAD

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `core` | 2023 | APRIL-GAN: A Zero-/Few-Shot Anomaly Classification and Segmentation Method for CVPR 2023 VAND Workshop Challenge | [card](cards/chen-2023-april-gan.md) | [pdf](PDFs/Chen_2023_APRIL-GAN.pdf) | [text](text/chen-2023-april-gan.txt) |
| `core` | 2023 | WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation | [card](cards/jeong-2023-winclip.md) | [pdf](PDFs/Jeong_2023_WinCLIP.pdf) | [text](text/jeong-2023-winclip.txt) |
| `core` | 2024 | AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection | [card](cards/yao-2024-adaclip.md) | [pdf](PDFs/Yao_2024_AdaCLIP.pdf) | [text](text/yao-2024-adaclip.txt) |
| `core` | 2024 | AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection | [card](cards/zhou-2024-anomalyclip.md) | [pdf](PDFs/Zhou_2024_AnomalyCLIP.pdf) | [text](text/zhou-2024-anomalyclip.txt) |
| `core` | 2024 | FiLo: Zero-Shot Anomaly Detection by Fine-Grained Description and High-Quality Localization | [card](cards/gu-2024-filo.md) | [pdf](PDFs/Gu_2024_FiLo.pdf) | [text](text/gu-2024-filo.txt) |
| `core` | 2024 | PromptAD: Learning Prompts with only Normal Samples for Few-Shot Anomaly Detection | [card](cards/li-2024-promptad.md) | [pdf](PDFs/Li_2024_PromptAD.pdf) | [text](text/li-2024-promptad.txt) |
| `core` | 2024 | VCP-CLIP: A Visual Context Prompting Model for Zero-Shot Anomaly Segmentation | [card](cards/qu-2024-vcp-clip.md) | [pdf](PDFs/Qu_2024_VCP-CLIP.pdf) | [text](text/qu-2024-vcp-clip.txt) |
| `core` | 2025 | AA-CLIP: Enhancing Zero-shot Anomaly Detection via Anomaly-Aware CLIP | [card](cards/ma-2025-aa-clip.md) | [pdf](PDFs/Ma_2025_AA-CLIP.pdf) | [text](text/ma-2025-aa-clip.txt) |
| `supporting` | 2021 | Learning Transferable Visual Models From Natural Language Supervision | [card](cards/radford-2021-clip.md) | [pdf](PDFs/Radford_2021_CLIP.pdf) | [text](text/radford-2021-clip.txt) |
| `supporting` | 2026 | DevPrompt: Deviation-Based Prompt Learning for One-Normal Shot Image Anomaly Detection | [card](cards/poudineh-2026-devprompt.md) | [pdf](PDFs/Poudineh_2026_DevPrompt.pdf) | [text](text/poudineh-2026-devprompt.txt) |

### Dataset / benchmark

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `background` | 2024 | Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection | [card](cards/wang-2024-real-iad.md) | [pdf](PDFs/Wang_2024_Real-IAD.pdf) | [text](text/wang-2024-real-iad.txt) |

### Frequency / ZSAD

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `core` | 2026 | FreqAnchorAD: Language-Free Zero-Shot Anomaly Detection via Frequency-Deviation Anchoring | [card](cards/qiu-2026-freqanchorad.md) | [pdf](PDFs/Qiu_2026_FreqAnchorAD.pdf) | [text](text/qiu-2026-freqanchorad.txt) |

### Hyperbolic

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `core` | 2024 | Hyperbolic Anomaly Detection | [card](cards/li-2024-hypad.md) | [pdf](PDFs/Li_2024_HypAD.pdf) | [text](text/li-2024-hypad.txt) |
| `core` | 2025 | HADNet: Hyperbolic Geometry Enhanced Feature Filtering Network for Industrial Anomaly Detection | [card](cards/hadnet-2025-scientificreports.md) | [pdf](PDFs/HADNet_2025_ScientificReports.pdf) | [text](text/hadnet-2025-scientificreports.txt) |
| `method` | 2017 | Poincare Embeddings for Learning Hierarchical Representations | [card](cards/nickel-2017-poincareembeddings.md) | [pdf](PDFs/Nickel_2017_PoincareEmbeddings.pdf) | [text](text/nickel-2017-poincareembeddings.txt) |
| `method` | 2018 | Hyperbolic Entailment Cones for Learning Hierarchical Embeddings | [card](cards/ganea-2018-hyperbolicentailmentcones.md) | [pdf](PDFs/Ganea_2018_HyperbolicEntailmentCones.pdf) | [text](text/ganea-2018-hyperbolicentailmentcones.txt) |
| `supporting` | 2018 | Hyperbolic Neural Networks | [card](cards/ganea-2018-hyperbolicneuralnetworks.md) | [pdf](PDFs/Ganea_2018_HyperbolicNeuralNetworks.pdf) | [text](text/ganea-2018-hyperbolicneuralnetworks.txt) |
| `supporting` | 2020 | Searching for Actions on the Hyperbole | [card](cards/long-2020-searchingactionshyperbole.md) | [pdf](PDFs/Long_2020_SearchingActionsHyperbole.pdf) | [text](text/long-2020-searchingactionshyperbole.txt) |

### Hyperbolic VLM

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `supporting` | 2023 | MERU: Multimodal Poincare Embeddings for Text-Image Representation | [card](cards/desai-2023-meru.md) | [pdf](PDFs/Desai_2023_MERU.pdf) | [text](text/desai-2023-meru.txt) |
| `supporting` | 2024 | Accept the Modality Gap: An Exploration in the Hyperbolic Space | [card](cards/ramasinghe-2024-acceptmodalitygaphyperbolic.md) | [pdf](PDFs/Ramasinghe_2024_AcceptModalityGapHyperbolic.pdf) | [text](text/ramasinghe-2024-acceptmodalitygaphyperbolic.txt) |
| `supporting` | 2024 | Compositional Entailment Learning for Hyperbolic Vision-Language Models | [card](cards/compositional-2024-hyperbolicvlmentailment.md) | [pdf](PDFs/Compositional_2024_HyperbolicVLMEntailment.pdf) | [text](text/compositional-2024-hyperbolicvlmentailment.txt) |

### Industrial AD baseline

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `background` | 2021 | DRAEM: A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection | [card](cards/zavrtanik-2021-draem.md) | [pdf](PDFs/Zavrtanik_2021_DRAEM.pdf) | [text](text/zavrtanik-2021-draem.txt) |
| `background` | 2021 | PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization | [card](cards/defard-2021-padim.md) | [pdf](PDFs/Defard_2021_PaDiM.pdf) | [text](text/defard-2021-padim.txt) |
| `background` | 2022 | A Unified Model for Multi-class Anomaly Detection | [card](cards/you-2022-uniad.md) | [pdf](PDFs/You_2022_UniAD.pdf) | [text](text/you-2022-uniad.txt) |
| `background` | 2022 | Anomaly Detection via Reverse Distillation from One-Class Embedding | [card](cards/deng-2022-reversedistillation.md) | [pdf](PDFs/Deng_2022_ReverseDistillation.pdf) | [text](text/deng-2022-reversedistillation.txt) |
| `background` | 2022 | Towards Total Recall in Industrial Anomaly Detection | [card](cards/roth-2022-patchcore.md) | [pdf](PDFs/Roth_2022_PatchCore.pdf) | [text](text/roth-2022-patchcore.txt) |
| `background` | 2024 | EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies | [card](cards/batzner-2024-efficientad.md) | [pdf](PDFs/Batzner_2024_EfficientAD.pdf) | [text](text/batzner-2024-efficientad.txt) |

### LVLM / SAM anomaly

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `background` | 2023 | 2nd Place Winning Solution for the CVPR2023 VAND Challenge: Multimodal Prompting for Data-centric Anomaly Detection | [card](cards/cao-2023-vand-saa-report.md) | [pdf](PDFs/Cao_2023_VAND_SAA_Report.pdf) | [text](text/cao-2023-vand-saa-report.txt) |
| `background` | 2023 | AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models | [card](cards/gu-2023-anomalygpt.md) | [pdf](PDFs/Gu_2023_AnomalyGPT.pdf) | [text](text/gu-2023-anomalygpt.txt) |
| `background` | 2023 | Segment Any Anomaly without Training via Hybrid Prompt Regularization | [card](cards/cao-2023-segmentanyanomaly.md) | [pdf](PDFs/Cao_2023_SegmentAnyAnomaly.pdf) | [text](text/cao-2023-segmentanyanomaly.txt) |
| `background` | 2025 | MetaUAS: Universal Anomaly Segmentation with One-Prompt Meta-Learning | [card](cards/gao-2025-metauas.md) | [pdf](PDFs/Gao_2025_MetaUAS.pdf) | [text](text/gao-2025-metauas.txt) |

### OT / UOT

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `background` | 2017 | Optimal Transport for Domain Adaptation | [card](cards/courty-2017-optimaltransportdomainadaptation.md) | [pdf](PDFs/Courty_2017_OptimalTransportDomainAdaptation.pdf) | [text](text/courty-2017-optimaltransportdomainadaptation.txt) |
| `method` | 2013 | Sinkhorn Distances: Lightspeed Computation of Optimal Transport | [card](cards/cuturi-2013-sinkhorndistances.md) | [pdf](PDFs/Cuturi_2013_SinkhornDistances.pdf) | [text](text/cuturi-2013-sinkhorndistances.txt) |
| `method` | 2018 | Scaling Algorithms for Unbalanced Optimal Transport Problems | [card](cards/chizat-2018-unbalancedoptimaltransport.md) | [pdf](PDFs/Chizat_2018_UnbalancedOptimalTransport.pdf) | [text](text/chizat-2018-unbalancedoptimaltransport.txt) |
| `method` | 2019 | Computational Optimal Transport | [card](cards/peyre-2019-computationaloptimaltransport.md) | [pdf](PDFs/Peyre_2019_ComputationalOptimalTransport.pdf) | [text](text/peyre-2019-computationaloptimaltransport.txt) |

### Prompt / VLM support

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `background` | 2022 | Conditional Prompt Learning for Vision-Language Models | [card](cards/zhou-2022-cocoop.md) | [pdf](PDFs/Zhou_2022_CoCoOp.pdf) | [text](text/zhou-2022-cocoop.txt) |
| `background` | 2022 | Learning to Prompt for Vision-Language Models | [card](cards/zhou-2022-coop.md) | [pdf](PDFs/Zhou_2022_CoOp.pdf) | [text](text/zhou-2022-coop.txt) |

### TTA

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `background` | 2022 | Continual Test-Time Domain Adaptation | [card](cards/wang-2022-cotta.md) | [pdf](PDFs/Wang_2022_CoTTA.pdf) | [text](text/wang-2022-cotta.txt) |
| `background` | 2022 | MEMO: Test Time Robustness via Adaptation and Augmentation | [card](cards/zhang-2022-memo.md) | [pdf](PDFs/Zhang_2022_MEMO.pdf) | [text](text/zhang-2022-memo.txt) |
| `background` | 2023 | Towards Stable Test-Time Adaptation in Dynamic Wild World | [card](cards/niu-2023-sar.md) | [pdf](PDFs/Niu_2023_SAR.pdf) | [text](text/niu-2023-sar.txt) |
| `method` | 2021 | Tent: Fully Test-Time Adaptation by Entropy Minimization | [card](cards/wang-2021-tent.md) | [pdf](PDFs/Wang_2021_TENT.pdf) | [text](text/wang-2021-tent.txt) |

### TTA / VLM

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `method` | 2022 | Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models | [card](cards/shu-2022-tpt.md) | [pdf](PDFs/Shu_2022_TPT.pdf) | [text](text/shu-2022-tpt.txt) |

### Wavelet / frequency

| Priority | Year | Paper | Card | PDF | Text |
|---|---:|---|---|---|---|
| `supporting` | 2011 | Synchrosqueezed Wavelet Transforms: An Empirical Mode Decomposition-like Tool | [card](cards/daubechies-2011-synchrosqueezedwavelettransforms.md) | [pdf](PDFs/Daubechies_2011_SynchrosqueezedWaveletTransforms.pdf) | [text](text/daubechies-2011-synchrosqueezedwavelettransforms.txt) |
| `supporting` | 2012 | Group Invariant Scattering | [card](cards/mallat-2012-groupinvariantscattering.md) | [pdf](PDFs/Mallat_2012_GroupInvariantScattering.pdf) | [text](text/mallat-2012-groupinvariantscattering.txt) |
| `supporting` | 2018 | Multi-Level Wavelet-CNN for Image Restoration | [card](cards/liu-2018-multilevelwaveletcnn.md) | [pdf](PDFs/Liu_2018_MultiLevelWaveletCNN.pdf) | [text](text/liu-2018-multilevelwaveletcnn.txt) |
| `supporting` | 2021 | FcaNet: Frequency Channel Attention Networks | [card](cards/qin-2021-fcanet.md) | [pdf](PDFs/Qin_2021_FcaNet.pdf) | [text](text/qin-2021-fcanet.txt) |
