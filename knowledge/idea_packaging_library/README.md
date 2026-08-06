# Idea Packaging Library

Generated: 2026-08-06

This library studies how papers turn a low-level technical idea into a reviewer-facing research story. It is different from `../writing_library/`: the writing library stores expressions and section templates, while this library stores "idea -> framing -> contribution" transformations.

## What This Library Answers

For each paper, ask:

1. What is the raw technical move?
2. What would the naive, unimpressive description be?
3. What problem did the paper construct to make the move feel necessary?
4. How did the paper rename or reframe the move?
5. What contribution does the reviewer perceive?
6. Which part of the packaging is transferable to a new ZSAD idea?
7. What boundary prevents the story from becoming overclaiming?

## Directory Map

- `cases/`: paper-by-paper packaging dissections.
- `patterns/`: reusable packaging moves distilled across papers.
- `templates/`: canvases for packaging a new idea.
- `metadata/cases.jsonl`: machine-readable case registry.
- `usage.md`: practical workflow for human and agent use.
- `AGENTS.md`: maintenance and retrieval rules.

## Gold Seed Cases

The user's three examples are treated as gold anchors:

- [AnomalyCLIP](cases/anomalyclip_object_agnostic_prompt.md): prompt learning -> object-agnostic abnormality/normality prompts.
- [VCP-CLIP](cases/vcpclip_visual_context_prompting.md): CoCoOp-like visual conditioning -> category-unknown visual context prompting.
- [AA-CLIP](cases/aaclip_anomaly_aware_two_stage.md): adapter tuning -> concept-first anomaly-aware text anchors, then visual alignment.

## Extended Cases

- [WinCLIP](cases/winclip_state_definition_windowing.md): prompt ensemble + window features -> language-defined anomaly states and local evidence.
- [AdaCLIP](cases/adaclip_hybrid_prompts.md): static/dynamic prompts -> stable task adaptation plus instance-specific adaptation.
- [FiLo](cases/filo_fine_grained_description_hq_loc.md): LLM descriptions + GroundingDINO + multi-scale localization -> fine-grained description and high-quality localization.
- [PromptAD](cases/promptad_one_class_prompt_learning.md): prompt learning with normal samples -> one-class contrast construction.
- [FreqAnchorAD](cases/freqanchorad_frequency_deviation.md): frequency modules -> frequency-deviation anchoring and channel-spectral evidence.
- [Wavelet / Scattering](cases/wavelet_multiscale_stable_evidence.md): wavelet/frequency branch -> multiscale stable anomaly evidence.
- [TPT](cases/tpt_single_sample_prompt_adaptation.md): test-time prompt update -> single-sample adaptive context retrieval.
- [UOT/Sinkhorn](cases/uot_relaxed_matching.md): relaxed OT optimization -> partial correspondence and mass-variation matching.
- [Hyperbolic](cases/hyperbolic_hierarchy_geometry.md): non-Euclidean embedding -> hierarchy-aware representation capacity.

## Fast Start

Use `templates/new_idea_packaging_canvas.md` for a new idea. Fill in the raw move honestly first, then choose one or two packaging patterns from `patterns/packaging_primitives.md`.

Do not start from a cool name. Start from a real mismatch:

```text
Prior assumption -> why it fails in ZSAD -> what your technical move changes -> what new concept name captures that change.
```
