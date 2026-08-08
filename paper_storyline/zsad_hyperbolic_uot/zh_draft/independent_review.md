# 独立 Codex 审稿意见

> 来源：只读审稿进程
> 审稿范围：`README.md`、`experiment_design.md`、`writing_outline.md`、`zh_draft/draft_zh.md`  
> 文件修改：无，审稿进程只读。本文档已按 R-HNA 术语统一。

## 总体 Verdict

`promising but risky`

## 主要风险

1. **机制 claim 需要被消融链条同时支撑。** 如果 `UOT + cosine`、无拒绝双曲接收或 balanced/partial OT 接近最终方法，审稿人会认为 R-HNA 只是复杂打分组合，而不是必要的正常性接收机制。
2. **双曲接收域的必要性最脆弱。** CLIP 特征经过指数映射后未必自然具备可利用的层级结构；必须证明 hyperbolic cone 优于 cosine、Euclidean 和 hyperbolic distance，而不是距离重标定或超参效果。
3. **UOT 容易被视为后处理。** 未接收比例必须独立对齐 GT mask，并降低复杂正常结构误报，否则审稿人会把它看成 anomaly map 的平滑、归一化或置信度校准。
4. **正常性锚点存在 prompt engineering 风险。** 如果锚点依赖手工文本、数量过多或类别相关，零样本设定会被质疑。当前稿使用 AnomalyCLIP learned normal prompt 是更干净的主设定，但仍需要 anomaly prompt、normal+anomaly、shuffled normal 等负对照。
5. **对既有 CLIP ZSAD 的批评不能过强。** 现代方法不一定把每个 patch 硬分类到 normal/anomaly；更准确的表述是：它们通常缺少显式的正常性接收状态和软拒绝变量。
6. **异常定位未必总适合高层语义接收。** 很多工业缺陷是低层纹理或几何扰动；如果细小划痕、污染、边界缺陷无提升，核心动机会受损。
7. **超参数与计算开销可能削弱实用价值。** 质量松弛强度、熵正则、曲率、锚点数量和 Sinkhorn 迭代次数如果需要按数据集细调，会削弱零样本、公平性和可复现性。
8. **新颖性边界必须谨慎。** OT、UOT、open-set rejection、hyperbolic anomaly detection 和 CLIP anomaly detection 都有相关脉络；论文应把贡献收窄到正常性接收表述及其 R-HNA 实例化。

## 建议强化的核心 Claim

不要主张“hyperbolic UOT 普遍提升 CLIP ZSAD”。更强也更安全的主张是：

```text
在 CLIP 零样本异常定位中，R-HNA 将 anomaly scoring 改写为可拒绝正常性接收；
UOT 给出未接收比例这一可检验拒绝变量，双曲锥给出 learned normal prompt 的结构化接收域。
```

## 必须保留的实验

- transport mode 消融：no transport / balanced OT / partial OT / UOT；
- cost 消融：cosine / Euclidean / hyperbolic distance / hyperbolic cone；
- signal 消融：未接收比例 / 条件接收代价 / combined score；
- anchor 消融：learned normal prompt / learned anomaly prompt / normal+anomaly / shuffled normal；
- MVTec AD + VisA 主表；
- 复杂正常结构的 failure-mode 误报分析；
- 质量松弛、熵正则、曲率、锚点数量和迭代次数敏感性；
- runtime 和 memory。

## 一句论文主张

本文将 CLIP 零样本异常定位表述为可拒绝正常性接收，并通过双曲接收域与非平衡质量松弛，把异常区域刻画为未被 learned normal prompt 接收或只能高代价接收的局部证据。
