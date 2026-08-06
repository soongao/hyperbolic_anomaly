# Packaging Primitives

These are reusable transformations from raw implementation to paper story.

## Primitive 1: Remove A Misleading Variable

Seed case: [AnomalyCLIP](../cases/anomalyclip_object_agnostic_prompt.md)

```text
Raw move: remove/replace/mask [variable].
Packaging: [variable]-agnostic [representation] for [task-level evidence].
Problem: prior methods over-condition on a factor that does not transfer.
```

Use when object category, domain, texture, background, or class name is a nuisance variable.

## Primitive 2: Infer An Unavailable Variable From The Input

Seed case: [VCP-CLIP](../cases/vcpclip_visual_context_prompting.md)

```text
Raw move: condition module on image/test input.
Packaging: [input]-context prompting/adaptation.
Problem: prior methods require a variable unavailable in the target setting.
```

Use when category, prompt, normal reference, or context cannot be provided explicitly.

## Primitive 3: Turn Fine-Tuning Into Concept Acquisition Then Alignment

Seed case: [AA-CLIP](../cases/aaclip_anomaly_aware_two_stage.md)

```text
Raw move: adapter/LoRA/prompt/projection tuning.
Packaging: first establish [task concept], then align [visual/local] evidence to it.
Problem: direct adaptation entangles concepts or damages pretrained knowledge.
```

Use when you have staged optimization or two parameter groups.

## Primitive 4: Split A Tradeoff Into Complementary Components

Seed case: [AdaCLIP](../cases/adaclip_hybrid_prompts.md)

```text
Raw move: combine two variants.
Packaging: hybrid [mechanism] balances [stable/global] and [adaptive/local].
Problem: either component alone solves only one side of the tradeoff.
```

Use for static/dynamic, global/local, semantic/visual, source/target, frequency/spatial.

## Primitive 5: Manufacture Missing Supervision In Representation Space

Seed case: [PromptAD](../cases/promptad_one_class_prompt_learning.md)

```text
Raw move: synthesize labels/prompts/anchors/prototypes.
Packaging: construct the missing contrast/reference needed by [standard method].
Problem: the target setting lacks negatives, labels, or references.
```

Use when data is absent but a semantic or geometric surrogate can be justified.

## Primitive 6: Turn Extra Evidence Into Structured Evidence

Seed case: [FreqAnchorAD](../cases/freqanchorad_frequency_deviation.md)

```text
Raw move: add frequency/edge/texture/statistical features.
Packaging: organize [evidence] in [coordinate/anchor/space] for relative discrimination.
Problem: prior evidence space misses subtle or distributed signals.
```

Use when adding modalities, frequency, wavelets, gradients, uncertainty, or local statistics.

## Primitive 7: Relax An Unrealistic Constraint

Seed case: [UOT/Sinkhorn](../cases/uot_relaxed_matching.md)

```text
Raw move: relax matching/alignment/normalization constraint.
Packaging: partial/unbalanced/mass-relaxed [matching].
Problem: prior objective forces full correspondence where only partial evidence exists.
```

Use for patch matching, prototype matching, distribution alignment, source-target adaptation.

## Primitive 8: Change Geometry Only For A Structural Reason

Seed case: [Hyperbolic](../cases/hyperbolic_hierarchy_geometry.md)

```text
Raw move: replace Euclidean metric/space.
Packaging: geometry-aware representation for hierarchy/scale/asymmetry.
Problem: flat similarity is a poor inductive bias for structured relations.
```

Use only if the structure is measured or directly used.

## Primitive 9: Move Adaptation To The Test Instance

Seed case: [TPT](../cases/tpt_single_sample_prompt_adaptation.md)

```text
Raw move: optimize at inference.
Packaging: test-time adaptive context under zero-label constraints.
Problem: training-time adaptation violates the target protocol or overfits source data.
```

Use for TTA, prompt tuning, self-consistency, augmentation-based objectives.

## Primitive 10: Turn A Frequency Add-On Into Multiscale Evidence

Seed case: [Wavelet / Scattering](../cases/wavelet_multiscale_stable_evidence.md)

```text
Raw move: add wavelet/Fourier/DCT/scattering/local statistics.
Packaging: multiscale [evidence] exposes [subtle/local/scale-dependent deviation].
Problem: a single spatial or semantic representation smooths away weak anomaly cues.
```

Use for wavelets, scattering transforms, frequency attention, texture cues, edge cues, and scale-space features.
