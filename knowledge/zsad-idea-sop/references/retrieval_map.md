# Retrieval Map

Use this file to decide which local knowledge to read.

Default root:

```text
/Users/bytedance/code/anomalyclip_new/knowledge
```

Use this shell variable in commands:

```bash
KNOWLEDGE_ROOT=/Users/bytedance/code/anomalyclip_new/knowledge
```

## Always Read First

- `README.md`: paper inventory by area.
- `metadata/papers.jsonl`: machine-readable paper registry.
- `idea_packaging_library/README.md`: available packaging cases.
- `experiment_library/README.md`: available experiment cases.

## By Idea Family

### Prompt Learning / Object-Agnostic / Text Prompts

Search:

```bash
rg -n "prompt|object-agnostic|state words|template|CoOp|CoCoOp" "$KNOWLEDGE_ROOT"/cards "$KNOWLEDGE_ROOT"/idea_packaging_library "$KNOWLEDGE_ROOT"/experiment_library
```

Nearest papers:

- AnomalyCLIP
- WinCLIP
- AdaCLIP
- PromptAD
- VCP-CLIP
- CoOp / CoCoOp

### Visual Context / Image-Conditioned Prompt

Search:

```bash
rg -n "visual context|image-specific|conditional prompt|CoCoOp|context prompting" "$KNOWLEDGE_ROOT"
```

Nearest papers:

- VCP-CLIP
- CoCoOp
- AdaCLIP

### Adapter / Fine-Tuning / Lightweight Adaptation

Search:

```bash
rg -n "adapter|residual adapter|fine-tune|anomaly-aware|two-stage|align" "$KNOWLEDGE_ROOT"
```

Nearest papers:

- AA-CLIP
- AdaCLIP
- AnomalyCLIP

### Frequency / Wavelet / Multiscale Evidence

Search:

```bash
rg -n "frequency|wavelet|DCT|spectral|scattering|multiscale|band" "$KNOWLEDGE_ROOT"
```

Nearest papers:

- FreqAnchorAD
- Wavelet / Scattering case in `idea_packaging_library`
- FcaNet
- Mallat scattering
- Multi-Level Wavelet-CNN

### Test-Time Adaptation / Test-Time Prompt Tuning

Search:

```bash
rg -n "test-time|TTA|entropy|minimization|augmentation|confidence selection|prompt tuning" "$KNOWLEDGE_ROOT"
```

Nearest papers:

- TPT
- Tent
- MEMO
- CoTTA / SAR

### OT / UOT / Matching

Search:

```bash
rg -n "optimal transport|unbalanced|Sinkhorn|partial matching|marginal|transport plan" "$KNOWLEDGE_ROOT"
```

Nearest papers:

- Sinkhorn Distances
- Unbalanced OT
- Optimal Transport for Domain Adaptation
- UOT case in `idea_packaging_library`

### Hyperbolic / Geometry

Search:

```bash
rg -n "hyperbolic|Poincare|curvature|hierarchy|entailment|geometry" "$KNOWLEDGE_ROOT"
```

Nearest papers:

- HypAD
- HADNet
- Poincare Embeddings
- Hyperbolic Entailment Cones
- MERU / Hyperbolic VLM papers

### SAM / LVLM / Foundation Model Assembly

Search:

```bash
rg -n "SAM|LVLM|AnomalyGPT|Segment Any|MetaUAS|candidate|mask|prompt regularization" "$KNOWLEDGE_ROOT"
```

Nearest papers:

- SAA+
- AnomalyGPT
- MetaUAS
- VAND SAA report

## Evidence Discipline

Prefer `cards/` for fast paper identity and `text/` for exact evidence. Use `idea_packaging_library` and `experiment_library` for distilled patterns, but verify strong novelty claims in the original `text/` files.
