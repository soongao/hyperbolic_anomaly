# Introduction Template

Use this for a 5-7 paragraph Introduction.

## Paragraph 1: Task And Practical Constraint

Role: define ZSAD through operational need.

```text
[Application context] requires detecting anomalous samples and localizing defective regions under limited target data. In zero-shot anomaly detection, the model must [task output] for unseen target categories without [target-domain training samples]. This setting is important when [data privacy/new product line/annotation scarcity], but difficult because [variation axes].
```

## Paragraph 2: Prior Capability

Role: acknowledge what existing methods made possible.

```text
Recent [foundation model / CLIP-based / prompt-based] methods have improved [capability] by [mechanism]. For example, [method family] constructs [textual/visual/reference] representations for normal and anomalous states, enabling [zero-shot/few-shot] inference.
```

## Paragraph 3: Concrete Gap

Role: state the mismatch, not just "performance is poor".

```text
However, [prior mechanism] is not fully aligned with [needed anomaly evidence]. In particular, [failure mode 1] and [failure mode 2] make it difficult to [localize subtle defects/generalize across categories/handle logical anomalies]. This gap suggests that [new evidence or formulation] should be modeled explicitly.
```

## Paragraph 4: Key Insight

Role: bridge the gap to the new method.

```text
Motivated by this observation, we view [task] as [new formulation]. The key insight is that [normality/abnormality/deviation/hierarchy/matching] can be represented by [core design] rather than [prior assumption]. This allows [method] to [specific benefit] under [setting].
```

## Paragraph 5: Method Overview

Role: give a readable pipeline.

```text
We propose [METHOD], which consists of [module A], [module B], and [module C]. Given [input], [module A] [function]. [Module B] then [function], and [module C/objective] [function]. The final anomaly score/map is produced by [aggregation/scoring].
```

## Paragraph 6: Evidence And Contributions

Role: summarize what is proven.

```text
We evaluate [METHOD] on [benchmarks] under [protocol]. The results show [main evidence], and ablations confirm [module role]. Our contributions are:
1. [insight contribution]
2. [method contribution]
3. [objective/module contribution]
4. [experimental contribution]
```

## Optional Paragraph 7: Scope

Use when the method has a notable boundary.

```text
The scope of this work is [setting]. We do not assume [unavailable resource], but [method] still requires [actual resource]. Failure cases remain when [condition], which motivates [future direction].
```

