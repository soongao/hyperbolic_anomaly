# 独立 Codex 审稿意见

> 来源：`codex exec --ephemeral` 只读审稿进程  
> 审稿范围：`README.md`、`experiment_design.md`、`writing_outline.md`、`zh_draft/draft_zh.md`  
> 文件修改：无，审稿进程只读。

1. **总体 verdict：promising but risky**

2. **主要风险，按严重程度排序：**

1. **机制 claim 可能被实验反证。** 如果 `UOT + cosine`、`hyperbolic cone without OT` 或 balanced/partial OT 表现接近最终方法，审稿人会认为“UOT + hyperbolic”不是必要机制，而是复杂打分堆叠。
2. **双曲代价的必要性最脆弱。** CLIP 特征本身未必具有清晰层级结构，直接 Exp 映射到双曲空间可能只是距离重标定；审稿人会要求证明它不是 cosine/Euclidean 的单调变换或超参效果。
3. **UOT 容易被视为后处理/阈值化。** 未匹配质量若不能独立对齐 GT mask，并降低正常复杂结构误报，审稿人会说它只是对 anomaly map 做平滑、归一化或置信度校准。
4. **正常性锚点存在 prompt engineering 风险。** 若 anchor bank 手工设计、数量过多或类别相关，零样本设定会被质疑；若只靠 AnomalyCLIP learned prompts，又难证明“normality semantic transport”而不是继承 baseline prompt 能力。
5. **“强制每个 patch 分类”的靶子可能过强。** 现代 CLIP ZSAD 方法不一定都显式硬分配 normal/anomaly；审稿人会要求更精确地区分 soft prompt scoring、open-set rejection、一类建模和你们的 UOT formulation。
6. **异常定位未必适合语义传输。** 很多工业缺陷是低层纹理/几何扰动，CLIP patch-text 语义锚点可能粒度太粗；如果细小划痕、污染、边界缺陷无提升，核心动机会受损。
7. **超参数与计算开销可能削弱实用价值。** `tau_patch/tau_anchor/epsilon/curvature/anchor count` 若需按数据集调参，审稿人会质疑 zero-shot、公平性和可复现性。
8. **新颖性边界需非常小心。** OT、UOT、partial matching、open-set rejection、hyperbolic anomaly/CLIP 都有相关脉络；若 related work 不严谨，“reformulation”贡献会被认为包装大于实质。

3. **最应该收窄或强化的核心 claim：**  
不要主张“hyperbolic UOT 普遍提升 CLIP ZSAD”。应收窄为：**在 CLIP patch-to-text 异常定位中，UOT 提供一种可检验的 rejectable patch-to-normality matching 机制；只有当 unmatched mass 与异常区域稳定对齐，且 hyperbolic cost 在同等 UOT 设置下优于 flat cost 时，才把双曲正常性代价作为核心贡献。**

4. **必须补的实验和最关键 negative control：**  
必须补：transport mode 消融 `no OT / balanced OT / partial OT / UOT`；cost 消融 `cosine / Euclidean / hyperbolic distance / hyperbolic cone`；unmatched mass、matched cost、combined score 分解；anchor ablation；MVTec AD + VisA 全量主表；failure-mode 正常图误报分析；`tau/epsilon/curvature/anchor count` 敏感性与 runtime；与 AnomalyCLIP、WinCLIP、PromptAD/VAND/APRIL-GAN 等强 CLIP ZSAD baseline 公平比较。

最关键 negative control：**在完全相同 UOT、超参数和 anchor 数量下，用 random/unrelated/shuffled text anchors 替换正常性 anchors。** 如果随机或错配 anchors 仍接近最终结果，整套“normality semantic transport”解释基本站不住。

5. **一句建议的论文主张写法：**  
本文将 CLIP 零样本异常定位表述为可拒绝的 patch-to-normality 语义传输，并通过实验证明未匹配质量与高传输代价在特定工业异常场景中比强制 normal/anomaly prompt scoring 更能刻画异常区域。
