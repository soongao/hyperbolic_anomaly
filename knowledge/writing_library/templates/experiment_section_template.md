# Experiment Section Template

Use this to draft Experiments and Ablation sections.

## Experimental Setup

```text
Datasets. We evaluate on [datasets], covering [industrial/medical/logical/texture] anomalies. [Source-target split] is used for the zero-shot protocol.

Baselines. We compare against [training-free ZSAD], [auxiliary-data ZSAD], [few-shot/unsupervised AD if relevant], and [adjacent method if relevant]. All methods are evaluated under [same protocol].

Metrics. We report [image-level metrics] for anomaly recognition and [pixel-level metrics] for defect localization.

Implementation. [Backbone], [training data], [input resolution], [trainable modules], and [inference-time adaptation or none].
```

## Main Results

```text
Table [x] reports the main comparison. [METHOD] achieves [result] on [dataset/metric], outperforming [baseline] by [number] or obtaining competitive performance under [constraint]. The gains are most pronounced on [category/domain/metric], where [mechanism] is expected to help. On [weaker case], the improvement is smaller, suggesting [boundary].
```

## Cross-Domain Or Cross-Dataset Results

```text
To evaluate transfer, we train on [source] and test on [target]. The results show that [METHOD] maintains [capability] across [domain/category shift]. This supports the claim that [mechanism] captures [generic normality/frequency deviations/anomaly-aware anchors] rather than memorizing target categories.
```

## Ablation Study

```text
We ablate [module A], [module B], and [objective C] to analyze their roles. Removing [module A] mainly reduces [metric], indicating that it contributes to [capability]. Removing [module B] affects [metric], showing that [capability] depends on [mechanism]. The full model performs best, confirming that [modules] are complementary.
```

## Sensitivity Analysis

```text
We further study [hyperparameter]. Performance [trend] as [hyperparameter] changes. The best value is [value], while overly large/small values degrade performance because [interpretation].
```

## Qualitative Results

```text
Figure [x] visualizes anomaly maps on representative samples. [METHOD] produces [behavior] compared with [baseline], especially for [defect type]. Failure cases occur when [condition], where [assumption] is weak.
```

## Limitation Paragraph

```text
Although [METHOD] improves [claim], it remains limited when [failure condition]. This limitation suggests that future work should incorporate [missing evidence/module] and evaluate on [needed benchmark].
```

