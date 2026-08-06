# Experiment And Ablation Language

Use this file when writing Experiments, Results, Ablation Study, and qualitative analysis.

## Core Move

Tie each experiment to a claim.

Reusable pattern:

```text
To evaluate [claim], we compare [method] with [baselines] on [benchmarks] under [protocol]. The results show [specific effect], indicating [interpretation within boundary].
```

## Claim-Evidence Map

| Claim type | Evidence to report | Safer wording |
|---|---|---|
| Cross-category generalization | unseen target categories, source-target split | `generalizes across the evaluated unseen categories` |
| Cross-domain generalization | industrial + medical datasets | `transfers across the evaluated industrial and medical domains` |
| Localization quality | pixel AUROC, PRO/AUPRO, AP, qualitative maps | `improves defect localization` |
| Classification quality | image AUROC, F1-max, AP | `improves image-level anomaly recognition` |
| Module usefulness | ablation removing module | `the drop after removing [module] confirms its contribution` |
| Efficiency | latency, trainable parameters, update steps | `resource-efficient under the reported setup` |

## Main Result Paragraph

Reusable template:

```text
Table [x] compares [method] with [baseline families] on [datasets]. Under the [zero-shot/few-shot/source-free] protocol, [method] achieves [result]. The gains are most visible on [subset/metric], suggesting that [mechanism] helps [specific difficulty]. The conclusion is limited to [evaluated setting].
```

## Ablation Paragraph

Sources: [AnomalyCLIP](../../cards/zhou-2024-anomalyclip.md), [AdaCLIP](../../cards/yao-2024-adaclip.md), [FreqAnchorAD](../../cards/qiu-2026-freqanchorad.md), [AA-CLIP](../../cards/ma-2025-aa-clip.md)

Reusable template:

```text
We ablate [module/objective] to isolate its effect from the rest of the framework. Removing [module] leads to [metric change], which indicates that [module function] is necessary for [claim]. Combining [module A] and [module B] gives the strongest result, supporting the design choice that [interpretation].
```

Good phrases:

- `isolates the effect of`
- `validates the necessity of`
- `contributes mainly to image-level discrimination`
- `benefits localization more strongly`
- `the combined variant performs best`
- `the performance does not monotonically improve with`

## Qualitative Analysis Paragraph

Reusable template:

```text
Figure [x] visualizes [anomaly maps/features/embeddings] for representative categories. Compared with [baseline], [method] produces [sharper/fewer false positives/more complete] responses around [defect type]. These cases illustrate [mechanism], but they should be interpreted together with the quantitative metrics.
```

## Negative Or Mixed Result Wording

Reusable patterns:

```text
The method improves [metric A] but shows smaller gains on [metric B], suggesting that [module] primarily affects [capability] rather than [other capability].
```

```text
The failure cases concentrate on [condition], where [assumption] is weak. This points to [future component/evidence] rather than invalidating the main result under [setting].
```

## Avoid

- Do not write `proves` for empirical tables. Use `shows`, `indicates`, `supports`, or `suggests`.
- Do not report only averages when the method fails badly on important categories.
- Do not claim `robust` unless tested across perturbations, splits, domains, or seeds.
- Do not hide additional inference-time costs from TTA, prompt tuning, or multi-view augmentation.

