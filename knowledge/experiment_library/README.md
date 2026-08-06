# ZSAD Experiment Library

Generated: 2026-08-06

This library extracts the experiment logic of ZSAD and CLIP-based anomaly detection papers. It is not a result leaderboard. It answers what experiment types are expected, which claims they support, which tables/figures usually appear, and which experiments are optional or low-value for a new paper.

## What This Library Answers

1. What experiments do ZSAD papers usually run?
2. Which experiments are required for reviewer trust?
3. Which experiments are optional, supplementary, or not worth doing first?
4. What should main tables and qualitative figures contain?
5. Which ablations are needed for prompt, adapter, visual-context, frequency, TTA, or hyperbolic-style claims?

## Directory Map

- `cases/`: paper-by-paper experiment package analysis.
- `patterns/`: reusable experiment requirements, metric/protocol rules, table and figure inventories.
- `templates/`: experiment planning templates for a new ZSAD paper.
- `metadata/experiments.jsonl`: machine-readable registry.
- `usage.md`: quick workflow for human and agent use.
- `AGENTS.md`: maintenance and retrieval rules.

## Core Reading Order

If planning a new ZSAD paper:

1. Read [required_experiments.md](patterns/required_experiments.md).
2. Read [metrics_and_protocols.md](patterns/metrics_and_protocols.md).
3. Pick 2-4 nearest cases from `cases/`.
4. Fill [new_zsad_experiment_plan.md](templates/new_zsad_experiment_plan.md).
5. Use [optional_and_avoid.md](patterns/optional_and_avoid.md) to remove low-value experiments.

## Case Index

- [AnomalyCLIP](cases/anomalyclip_experiments.md): broad zero-shot transfer, object-agnostic prompt evidence, industrial and medical domains.
- [WinCLIP](cases/winclip_experiments.md): zero-/few-shot baseline package, prompt ensemble, window/local evidence, failure cases.
- [VCP-CLIP](cases/vcpclip_experiments.md): segmentation-focused visual context prompting, AP/product-level analysis, efficiency.
- [AA-CLIP](cases/aaclip_experiments.md): two-stage adapter training, anomaly-aware text space, data efficiency.
- [AdaCLIP](cases/adaclip_experiments.md): hybrid static/dynamic prompts, auxiliary training domain, backbone and prompt-depth sensitivity.
- [FiLo](cases/filo_experiments.md): fine-grained anomaly descriptions, HQ localization, text-template and module ablations.
- [PromptAD](cases/promptad_experiments.md): few-shot normal-only prompt learning, shot curves, prompt suffix and margin ablations.
- [APRIL-GAN](cases/april_gan_experiments.md): challenge-style zero-/few-shot protocol, F1-oriented leaderboard, cross-dataset training.
- [FreqAnchorAD](cases/freqanchorad_experiments.md): language-free frequency deviation, industrial/medical benchmark sweep, spectral ablations.
- [DevPrompt](cases/devprompt_experiments.md): one-normal/few-shot deviation prompt, class-wise AUROC, sensitivity analysis.
- [SAA+](cases/saa_experiments.md): zero-shot SAM/CLIP segmentation, hybrid prompt regularization, max-F1 region/pixel metrics.
- [MetaUAS](cases/metauas_experiments.md): one-prompt meta-learning, zero/few/full comparison, complexity and universal setting.
- [TPT / TTA](cases/tpt_tta_support_experiments.md): support case for test-time prompt/adaptation experiment design.
- [HypAD](cases/hypad_support_experiments.md): non-ZSAD hyperbolic support case for geometry-specific experiment claims.

## High-Level Rule

For ZSAD, a convincing experiment package must prove three things:

```text
effectiveness on standard benchmarks -> causality of the proposed design -> generalization under the promised protocol
```

Do not add experiments merely because another paper has them. Add an experiment only if it validates a claim your paper makes.
