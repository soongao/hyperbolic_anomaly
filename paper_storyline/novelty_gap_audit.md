# Novelty Gap Audit: Hyperbolic Contrastive Normality Entailment

检索日期：2026-08-04

## 1. 结论

广义上，`hyperbolic + anomaly detection`、`hyperbolic + CLIP/VLM`、以及 `hyperbolic + CLIP zero-shot anomaly detection` 都已经有人做过。因此不能把论文主张写成：

- 第一个把双曲空间用于 anomaly detection。
- 第一个把双曲空间用于 CLIP/VLM。
- 第一个把双曲空间用于 CLIP zero-shot anomaly detection。

但当前检索到的相邻工作并没有直接覆盖我们的窄主张：

> Industrial anomaly scoring should be modeled as patch-level contrastive semantic entailment: an anomalous patch is not only far from normal text, but violates a normality cone while being better explained by an anomaly cone.

因此这个方向不能走“开荒式 novelty”，而应走“机制差异式 novelty”：已有工作证明双曲空间可用于层级视觉/视觉语言建模，我们的贡献必须落在 **normality violation 的任务建模、normal/anomaly cone 的相对解释机制、以及 flat prompt scoring 失败模式的实验证明**。

## 2. 相邻工作矩阵

| Work | Year | What it covers | Relationship to our idea | Risk level |
|---|---:|---|---|---|
| Hyperbolic Anomaly Detection (HypAD), CVPR 2024, DOI: 10.1109/CVPR52733.2024.01658 | 2024 | 将工业异常检测特征映射到双曲空间，用双曲距离优化 anomaly detection。 | 覆盖 `hyperbolic + anomaly detection`，但不涉及 CLIP prompt、normal/anomaly text cones、semantic entailment。 | High for broad claim |
| HADNet: Hyperbolic geometry enhanced feature filtering network for industrial anomaly detection, Scientific Reports 2025, DOI: 10.1038/s41598-025-07550-0 | 2025 | 双曲特征映射、异常相关特征选择、残差判别。 | 覆盖工业缺陷中的双曲特征过滤，但不是 CLIP/VLM，也不是 text-guided cone entailment。 | Medium |
| HPL-CLIP: hyperbolic prompt learning for zero-shot anomaly detection, Measurement Science and Technology 2026, DOI: 10.1088/1361-6501/ae8713 | 2026 | CLIP ZSAD 中学习 normality/abnormality generic states，并在双曲空间对齐多层视觉特征；有 pixel adapter 和 hierarchical hinge loss。 | 最接近。覆盖 `hyperbolic + CLIP + ZSAD + normal/abnormal states`。但摘要没有显示 normal cone violation、anomaly cone explanation、patch-level contrastive entailment energy 的机制。 | Very high |
| Hyperbolic Safety-Aware Vision-Language Models (HySAC), CVPR 2025, DOI: 10.1109/CVPR52734.2025.00399 | 2025 | 将 safe/unsafe content 建成双曲 entailment hierarchy，用 entailment losses 建模非对称 image-text 关系。 | 覆盖 `CLIP/VLM + hyperbolic entailment + binary semantic safety relation`。不是 anomaly detection，但机制会被审稿人拿来类比。 | High for mechanism novelty |
| Compositional Entailment Learning for Hyperbolic Vision-Language Models, arXiv 2024, DOI: 10.48550/arXiv.2410.06912 | 2024 | 用 image、object boxes、text descriptions 做 compositional entailment learning。 | 覆盖 `hyperbolic VLM + entailment objective`。不是 normality/anomaly，也不是工业 patch anomaly scoring。 | Medium-high |
| Searching for Actions on the Hyperbole, CVPR 2020, DOI: 10.1109/CVPR42600.2020.00122 | 2020 | 使用 hyperbolic embedding 和 entailment cones 做层级 action search。 | 说明 entailment cone 不是新工具。我们只能主张它在 CLIP anomaly normality violation 中的新任务化使用。 | Medium |
| AnomalyCLIP, arXiv 2023, DOI: 10.48550/arXiv.2310.18961 | 2023 | 学习 object-agnostic normal/abnormal prompts，用 CLIP 做 ZSAD。 | 我们的直接 baseline。它仍主要是 flat prompt similarity / prompt learning，而不是 hyperbolic cone entailment。 | High baseline |
| PromptAD, WACV 2024, DOI: 10.1109/WACV57701.2024.00113 | 2024 | 用 normality 和 abnormality text prompts 建双分支 ZSAD。 | 覆盖 normal/abnormal prompt 双视角，但不在双曲空间，也不是 cone violation。 | Medium |

## 3. 论文必须收窄的主张

不能写：

> We are the first to use hyperbolic space for anomaly detection.

不能写：

> We are the first to learn normality and abnormality in hyperbolic CLIP space.

更稳的主张是：

> Existing hyperbolic anomaly detection methods mainly treat hyperbolic geometry as a feature metric or prompt-alignment space. In contrast, we formulate industrial anomaly scoring as patch-level contrastive normality entailment: normal regions are expected to be entailed by a normality cone, while anomalous regions are identified by a relative explanatory gap between normal and anomaly cones.

这句话把贡献落在任务建模和 scoring mechanism 上，而不是落在“用了双曲空间”。

## 4. 还没有被直接覆盖的差距

### Gap A: 从 hyperbolic representation 到 hyperbolic semantic decision rule

HypAD/HADNet 主要强调双曲距离和特征空间；HPL-CLIP 强调 hyperbolic prompt learning 和多层视觉对齐。我们的差异点必须是：

- anomaly score 不是距离 normal prototype 的远近；
- anomaly score 是 normality cone violation 与 anomaly cone explanation 的相对能量；
- anomaly prompt 的角色不是分类标签，而是异常解释锚点。

### Gap B: 从 image/text alignment 到 patch-level normality violation

HySAC 和 compositional entailment 学的是通用 VLM 或安全内容的层级关系。我们的任务差异是：

- 决策对象是 patch，而不是整图 image-text pair；
- 正常对象内部存在复杂但合法的局部结构；
- normal-only violation 会误伤复杂正常局部，必须由 anomaly cone 做 contrastive calibration。

### Gap C: 从“结果提升”到“失败模式解释”

当前结果能说明弱类提升，但还不足以说服审稿人机制成立。必须补上：

- normal-only 在 capsule/pill/screw/toothbrush 等复杂正常区域上的 false positive 可视化；
- contrastive cone 如何降低这些 false positives；
- normal patch 和 anomaly patch 的 `E_normal - E_anomaly` 分布分离。

## 5. 必补实验

### Experiment 1: Geometry necessity

目标：证明不是随便换个 scoring 就能涨。

需要比较：

| Variant | Purpose |
|---|---|
| Cosine similarity, AnomalyCLIP original | 原始 flat prompt baseline |
| Euclidean normal/anomaly energy | 排除“只是 energy softmax 有效” |
| Hyperbolic distance to normal/anomaly prototypes | 排除“只是双曲距离有效” |
| Hyperbolic cone normal-only | 验证 normality violation 的优缺点 |
| Hyperbolic contrastive cones | 证明最终机制必要 |

### Experiment 2: Contrastive explanation necessity

目标：证明 anomaly cone 不是普通异常分类器。

需要比较：

| Variant | Expected interpretation |
|---|---|
| Normal cone only | 容易把复杂正常结构判成异常 |
| Anomaly cone only | 容易依赖异常 prompt 语义，缺少 normality violation |
| Flat normal/anomaly prompt softmax | 只有并列分类，没有 entailment |
| Contrastive cone energy | 同时要求违背 normality 且更符合 anomaly explanation |

### Experiment 3: Failure-mode visualization

目标：把故事中的“复杂正常局部结构”变成证据。

最少需要：

- 每个弱类给 1-2 张 normal image 的 anomaly map，对比 normal-only vs contrastive。
- 每个弱类给 1-2 张 defect image 的 anomaly map，对比定位是否保留。
- 画 normal pixels 与 anomalous pixels 的 `E_normal`、`E_anomaly`、`E_normal - E_anomaly` 直方图。

### Experiment 4: Comparison to HPL-CLIP

HPL-CLIP 是最接近工作，必须处理。

如果代码/结果可用：

- 直接在 MVTec AD、VisA 上比较 image AUROC/AP、pixel AUROC/PRO。
- 报告参数量、是否训练 prompt、是否需要 adapter、是否需要多层特征训练。

如果暂时无法复现：

- Related Work 中明确引用其公开结果。
- 在实验表中标注 `reported`，避免把 novelty 建在缺失 baseline 上。
- 贡献主张避免写“性能 SOTA”，改写为“mechanistic alternative / scoring formulation”。

## 6. 推荐最终定位

论文题目和贡献不要强调 `Hyperbolic CLIP for Anomaly Detection`，这会被 HPL-CLIP 和 HypAD 压住。

更好的定位：

> Contrastive Normality Entailment for CLIP-based Industrial Anomaly Detection

或者：

> Hyperbolic Contrastive Normality Entailment for Zero-shot Industrial Anomaly Detection

Contribution bullets：

1. We identify a limitation of flat normal/abnormal prompt scoring: it treats anomalies as sibling semantic categories rather than local violations of normality.
2. We formulate patch anomaly scoring as contrastive normality entailment in hyperbolic space, where normal and anomaly prompts define asymmetric explanatory cones.
3. We show that contrastive cone scoring reduces false positives from complex normal local structures, especially in fine-grained MVTec categories.

## 7. Decision

这个 idea 不是“没人做过的大方向”，而是“已有方向中的未充分机制化切口”。

如果保持当前故事不改，审稿风险高：会被认为是 HPL-CLIP/HypAD/HySAC 的组合变体。

如果按上面的 gap 补齐，仍然有投稿价值：新意应锁定在 **patch-level contrastive normality entailment as a decision rule**，并用 failure-mode evidence 证明它不是双曲空间包装。

## 8. 已补齐到代码中的验证接口

为避免 novelty 只停留在叙事层面，当前代码已经加入下列 mechanism ablation 接口：

| Purpose | Command knobs |
|---|---|
| 原始 flat prompt baseline | `--score_mode cosine` |
| 排除“只是 Euclidean energy 有效” | `--score_mode euclidean_energy --entailment_mode contrastive` |
| 排除“只是 hyperbolic distance 有效” | `--score_mode hyperbolic_distance --entailment_mode contrastive` |
| 验证 normality violation 的单独作用 | `--score_mode normality_entailment --entailment_mode normal_only` |
| 验证 anomaly prompt 不能单独解释方法 | `--score_mode normality_entailment --entailment_mode anomaly_only` |
| 最终机制 | `--score_mode normality_entailment --entailment_mode contrastive --context_weight 0.0 --order_weight 0.0` |

主实验入口 `test.py`、训练入口 `train.py`、单图可视化入口 `test_one_example.py` 均支持这些选项。弱类快速验证脚本为：

```bash
scripts/run_gap_ablation_mvtec.sh <mvtec_data_path> <checkpoint_path> [save_root]
```

这组实验的判定标准不是“最终方法必须在每个类别都最高”，而是需要出现清晰的机制证据：

- `hyperbolic_distance` 不能完全替代 cone entailment，否则“锥蕴含”贡献不成立。
- `normal_only` 应暴露复杂正常局部结构上的误报问题，否则 contrastive design 的必要性不足。
- `anomaly_only` 不应系统性优于 contrastive，否则论文应改写成 anomaly explanation，而不是 normality violation。
- `cone_contrastive` 需要在 weak classes 上稳定降低误报或提升 pixel-level 指标，支撑 patch-level decision rule。

结果层面仍需补齐的部分：

- 与 HPL-CLIP 的直接复现或 reported-result 边界表。
- `E_normal`、`E_anomaly`、`E_normal - E_anomaly` 的直方图导出与 failure-mode 可视化。
