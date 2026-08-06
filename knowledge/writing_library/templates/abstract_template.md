# Abstract Template

Use this for ZSAD-style papers. Keep it to 5-7 sentences.

## Five-Sentence Structure

```text
1. Task and setting:
[Task] aims to [detect/localize] anomalies in [unseen target domains/categories] without [target-domain training samples].

2. Gap:
Although [prior family/foundation model] provides [capability], it remains limited because [mechanism mismatch].

3. Method:
We propose [method], a [descriptor] framework that [core mechanism] by [module A] and [module B].

4. Technical advantage:
Unlike [prior assumption], [method] [new representation/adaptation/matching], enabling [specific capability] under [setting].

5. Evidence:
Experiments on [benchmarks] show that [method] [supported result], and ablations verify [module/evidence].
```

## Optional Sixth Sentence

Use when there is a real limitation or deployment-relevant property:

```text
[Method] requires [resource] and does not require [unavailable resource], making it suitable for [bounded setting].
```

or:

```text
Failure cases remain on [condition], suggesting [future direction].
```

## Fill-In Example Skeleton

```text
Zero-shot anomaly detection aims to recognize anomalous images and localize defective regions in unseen target categories without target-domain training samples. Although CLIP-based methods provide transferable image-text alignment, their object-level semantics can be misaligned with the fine-grained normal-abnormal evidence required for anomaly localization. We propose [METHOD], a [frequency/geometry/prompt/reference]-aware framework that [CORE MECHANISM]. Specifically, [METHOD] first [MODULE A], then [MODULE B], and finally [SCORING/OUTPUT]. Experiments on [DATASETS] demonstrate [SUPPORTED CLAIM], while ablations show that [MODULE] contributes primarily to [CAPABILITY].
```

## Claim Checks

- If using `zero-shot`, specify no target-domain training samples.
- If using `language-free`, confirm no text encoder or prompt is used for the anomaly decision.
- If using `state-of-the-art`, confirm same protocol and baselines.
- If using `generalization`, name evaluated domains or categories.

