# 面向 CLIP 零样本异常定位的双曲非平衡语义传输

> 中文初稿版本：v0.1  
> 状态：方法与写作框架初稿，实验结果与引用尚未补齐。  
> 写作约束：本文所有性能结论均以 `[结果待填]` 标注，所有未核验文献均以 `[引用待核验]` 标注。

## 摘要

基于 CLIP 的零样本异常检测通常通过比较图像 patch 与正常/异常文本提示之间的相似度来生成异常分数。然而，这类平坦的 patch-wise prompt scoring 主要给出 patch 到文本原型的相对相似度，缺少显式机制判断某个局部区域是否应被正常语义拒绝解释。本文将 CLIP 零样本异常定位重新表述为一个可拒绝的语义传输问题：正常 patch 应当能够以较低代价传输到正常性语义锚点，而异常 patch 则表现为高传输代价或未匹配质量。为此，我们提出双曲非平衡语义传输框架。该框架首先利用 CLIP 提取图像 patch 特征与正常性文本锚点特征，并在双曲空间中构造 patch 到正常性锚点的语义代价；随后通过非平衡最优传输放松质量守恒约束，使无法被正常性锚点解释的区域以未匹配质量的形式显现。最终，本文将未匹配质量与匹配代价结合为像素级异常分数。实验设计围绕三个问题展开：非平衡传输是否优于平衡传输，双曲正常性代价是否优于平坦距离代价，以及未匹配质量是否能够作为有效异常证据。实验结果将在 MVTec AD、VisA 及其他零样本异常检测基准上进行验证 `[结果待填]`。

关键词：零样本异常检测；CLIP；非平衡最优传输；双曲空间；异常定位

## 1. 引言

零样本异常检测旨在目标类别缺乏异常样本的情况下完成异常图像识别与像素级定位。该任务在工业质检和医学影像分析等场景中具有实际价值，因为异常样本往往稀缺、形态多样，并且难以在训练阶段完整枚举。近年来，CLIP 等视觉语言模型通过大规模图文预训练获得了开放词汇语义对齐能力，为零样本异常检测提供了新的技术路径 `[引用待核验]`。代表性方法通常设计或学习正常/异常文本提示，并将图像 patch 与文本特征进行相似度比较，从而得到图像级或像素级异常分数 `[引用待核验]`。

尽管基于 CLIP 的方法在零样本迁移方面具有优势，现有异常打分机制仍然主要依赖平坦的正常/异常 prompt 比较。给定一个 patch 特征，常见做法是计算其与正常文本提示和异常文本提示的相似度，再通过 softmax、能量差或相似度变换得到异常分数。这种范式能够提供有效的局部判别信号，但通常没有显式建模“该 patch 是否应该被正常性语义接收”这一拒绝问题。工业异常通常并不是一个与正常状态并列的完整语义类别。划痕、缺口、污渍、压痕或结构不连续往往是对正常对象局部结构、纹理或材料状态的破坏。对于这类异常，关键问题并不只是一个 patch 更接近 “normal” 还是 “anomaly”，而是它是否仍然能够被正常性语义合理解释。

这一观察提示我们，CLIP 零样本异常定位可以被重新理解为一个可拒绝的语义匹配问题。正常区域应当能够被匹配到某些正常性语义锚点，例如正常表面、完整结构、规则纹理或未损坏状态；相反，异常区域不应被强制解释为某个正常语义锚点的实例。换言之，异常证据可以来自两类信号：一类是匹配代价高，即 patch 即使被匹配也难以与正常性锚点对齐；另一类是未匹配质量高，即 patch 的质量在语义传输过程中被部分拒绝。普通的独立相似度打分难以表达这种“拒绝匹配”的机制。

最优传输为上述问题提供了经典的分布匹配工具。给定图像 patch 分布和正常性锚点分布，最优传输可以寻找从 patch 到锚点的最小代价匹配。然而，标准平衡最优传输要求源分布和目标分布的质量完全守恒，这与异常定位的需求并不一致：如果所有 patch 质量都必须被传输，那么异常区域也会被强制匹配到某个正常性锚点。为避免这种过度解释，本文引入非平衡最优传输。非平衡最优传输通过软化质量守恒约束，允许部分 patch 质量不被正常性锚点接收，从而自然形成未匹配质量这一异常证据。

同时，传输代价的设计直接决定语义匹配是否合理。若使用余弦距离或欧氏距离，正常性锚点通常被视为平坦特征空间中的原型点，难以表达正常对象、局部部件、纹理状态之间的层级关系。双曲空间长期用于表示层级结构和非欧几何关系 `[引用待核验]`，因此适合作为正常性语义代价的几何基础。本文在双曲空间中构造 patch 到正常性锚点的距离或锥违背代价，使传输过程不仅考虑特征相近性，也考虑 patch 是否符合正常性锚点所诱导的语义约束。

基于上述动机，本文提出双曲非平衡语义传输方法。给定图像 patch 特征和正常性文本锚点，我们首先将二者映射到双曲空间，并计算 patch 到锚点的正常性代价矩阵。随后，我们求解非平衡最优传输问题，得到 patch 到正常性锚点的传输计划。每个 patch 的异常分数由两部分组成：未匹配质量和匹配代价。前者衡量该 patch 在多大程度上被正常性语义拒绝，后者衡量该 patch 即使被匹配时仍需要付出的语义代价。

本文的贡献可以概括如下：

1. 我们将 CLIP 零样本异常定位重新表述为可拒绝的 patch-to-normality 语义传输问题，区别于现有平坦的 patch-wise normal/anomaly prompt scoring 范式。
2. 我们提出双曲非平衡语义传输框架，利用双曲正常性代价构造 patch 到正常性锚点的语义成本，并通过非平衡最优传输产生未匹配质量作为异常证据。
3. 我们设计系统消融以分别检验质量松弛、双曲语义代价和异常分数组成的作用，包括无传输打分、平衡传输、部分传输、非平衡传输，以及余弦、欧氏、双曲距离和双曲锥违背代价 `[结果待填]`。

## 2. 相关工作

### 2.1 基于 CLIP 的零样本异常检测

基于 CLIP 的零样本异常检测方法利用视觉语言模型的开放词汇能力，将异常检测转化为图像特征与文本提示之间的匹配问题。早期方法通常构造人工正常/异常 prompt，并直接使用图文相似度进行异常打分 `[引用待核验]`。后续方法进一步学习对象无关的正常/异常 prompt，或引入局部 patch 特征以提高异常区域定位能力 `[引用待核验]`。这些方法的共同优势是避免依赖目标类别异常样本，并能够在不同工业或医学数据集之间迁移。

然而，多数 CLIP 异常检测方法仍然保留了平坦 prompt scoring 的基本形式。无论 prompt 是手工构造还是可学习的，patch 通常都被独立比较到正常和异常文本原型。这种机制在语义上更接近 normal/anomaly 原型比较，但实际异常往往是正常对象局部状态的破坏。本文与这类方法的区别在于，我们不把重点放在 patch 与异常 prompt 的相对相似度上，而是判断 patch 是否能被正常性锚点以较低代价解释，并允许无法解释的质量被拒绝。

### 2.2 双曲表征与视觉语言层级建模

双曲空间因其负曲率几何结构，常被用于表示树状或层级语义关系 `[引用待核验]`。在视觉和视觉语言任务中，双曲空间被用于增强类别层级建模、图文蕴含关系建模或安全/风险语义关系建模 `[引用待核验]`。在异常检测领域，已有工作也探索了双曲表征、双曲距离或双曲 prompt learning 对异常检测的作用 `[引用待核验]`。

本文不将新颖性建立在“首次使用双曲空间”之上。相反，我们将双曲空间限定为语义传输中的代价函数：它用于刻画 patch 到正常性锚点之间的层级正常性代价，而不是单独作为表征空间或距离替换。这样的收窄有助于区分本文与已有双曲异常检测或双曲 CLIP 方法之间的边界。

### 2.3 最优传输与非平衡最优传输

最优传输是一类用于比较和匹配分布的经典方法，已被广泛用于计算机视觉、域适应、图文匹配和表示学习等任务 `[引用待核验]`。标准平衡最优传输要求源分布和目标分布的质量完全守恒，这适合两个完整分布之间的匹配，但不一定适合包含异常或离群区域的场景。部分最优传输允许仅匹配固定比例的质量，而非平衡最优传输进一步通过惩罚项软化质量守恒约束，使传输计划能够自动调整被匹配的质量 `[引用待核验]`。

异常定位天然包含拒绝匹配的需求，因为异常区域可能不应被正常语义解释。本文利用非平衡最优传输建模这种拒绝机制：正常 patch 被传输到正常性锚点，异常 patch 则表现为高代价匹配或未匹配质量。与将 OT 作为通用后处理或平滑工具不同，本文关注的是未匹配质量本身能否成为异常证据。

### 2.4 一类异常检测与拒绝机制

传统一类异常检测通常只建模正常样本分布，并将偏离正常分布的样本视为异常 `[引用待核验]`。从这个角度看，本文的非平衡语义传输也具有一类建模思想：正常性锚点定义可解释区域，无法被正常性传输解释的 patch 被视为潜在异常。不同之处在于，本文的正常分布不是由目标域正常图像直接估计，而是由 CLIP 文本语义和预训练视觉特征共同定义，因此更适合零样本设定。

## 3. 方法

### 3.1 问题定义与方法概览

给定测试图像 \(x\)，CLIP 图像编码器输出一组 patch 特征：

```text
P = {p_i}_{i=1}^N,  p_i in R^d.
```

同时，文本编码器或 AnomalyCLIP 的 prompt learner 输出正常性文本锚点：

```text
T = {t_j}_{j=1}^M,  t_j in R^d.
```

本文目标是为每个 patch 生成异常分数：

```text
S = {s_i}_{i=1}^N.
```

本文方法包含三个步骤。第一步，构造 patch 到正常性锚点的语义代价矩阵。第二步，求解非平衡最优传输，得到 patch 到锚点的软匹配计划。第三步，根据每个 patch 的未匹配质量和匹配代价生成异常分数。该流程的核心是将异常定位从独立的 patch-wise prompt scoring 转化为可拒绝的 patch-to-normality matching。

### 3.2 正常性锚点

正常性锚点用于定义 patch 可以被哪些正常语义解释。在最简实现中，正常性锚点来自 AnomalyCLIP 已学习的 normal text feature。为了进行对照实验，也可以使用 normal/anomaly 两类文本锚点，或仅使用 anomaly anchor 作为 negative control。若进一步扩展，正常性锚点可以来自更细粒度的文本提示，例如：

```text
normal object
normal surface
normal texture
normal structure
normal boundary
intact state
regular pattern
```

当前代码版本主要支持 `normal`、`anomaly` 和 `both` 三种锚点模式。更复杂的 prompt bank 设计应作为后续实验扩展，而不应在当前版本中过度声明。

### 3.3 双曲正常性代价

为了构造语义传输代价，我们将 patch 特征和文本锚点映射到 Poincare ball：

```text
z_i = Exp_0(p_i),
u_j = Exp_0(t_j).
```

一种直接的代价定义是双曲距离：

```text
C_ij = d_H(z_i, u_j).
```

该代价衡量 patch 与正常性锚点在双曲空间中的几何距离。进一步地，若将正常性锚点视为语义锥的锚点，则可以使用双曲锥违背代价：

```text
C_ij = V(z_i, Cone(u_j)).
```

其中 \(V(\cdot)\) 衡量 patch 是否落在由正常性锚点诱导的语义约束范围内。直观上，正常 patch 应具有较低的锥违背代价；异常 patch 则更可能偏离正常性锥，从而产生较高代价。本文实验将比较余弦代价、欧氏代价、双曲距离代价和双曲锥违背代价，以验证双曲正常性代价是否具有必要性。

### 3.4 非平衡语义传输

给定 patch 分布 \(a\)、正常性锚点分布 \(b\) 和代价矩阵 \(C\)，标准平衡最优传输求解：

```text
min_gamma <gamma, C>
s.t. gamma 1 = a, gamma^T 1 = b.
```

该约束要求所有 patch 质量都必须被完整传输到锚点。然而，在异常定位中，异常 patch 不应被强制解释为正常语义。为此，本文采用非平衡最优传输：

```text
min_gamma <gamma, C>
        + tau_p D(gamma 1 || a)
        + tau_t D(gamma^T 1 || b)
        + epsilon H(gamma).
```

其中，\(\gamma\) 是传输计划，\(<\gamma, C>\) 是总传输代价，\(D(\cdot || \cdot)\) 是质量偏离惩罚项，\(H(\gamma)\) 是熵正则项，\(\tau_p\) 和 \(\tau_t\) 控制源端和目标端质量守恒的强度。与平衡传输相比，非平衡传输允许部分 patch 质量不被锚点接收，因此能够产生未匹配质量。

### 3.5 异常分数

对于第 \(i\) 个 patch，其被传输的质量为：

```text
m_i = sum_j gamma_ij.
```

未匹配质量定义为：

```text
u_i = a_i - m_i.
```

匹配代价定义为：

```text
c_i = sum_j gamma_ij C_ij / (m_i + eps).
```

最终异常分数为：

```text
s_i = alpha * u_i / a_i + beta * c_i.
```

其中，未匹配质量表示 patch 被正常性锚点拒绝的程度，匹配代价表示 patch 即使被匹配时仍需要付出的语义代价。二者分别对应异常检测中的两类证据：无法解释和难以解释。实验部分将分别评估仅使用未匹配质量、仅使用匹配代价以及二者组合的效果。

### 3.6 实现细节

当前实现不引入额外最优传输依赖，而是在 PyTorch 中实现 Sinkhorn 风格求解器。实现支持三种传输模式：

```text
balanced
partial
unbalanced
```

同时支持四种代价：

```text
cosine
euclidean
hyperbolic_distance
hyperbolic_cone
```

推理阶段通过 `--score_mode hyperbolic_uot` 启用本文方法，并通过 `--ot_mode`、`--ot_cost`、`--ot_score` 等参数控制传输模式、代价函数和异常分数组成。默认设置使用非平衡传输、双曲锥违背代价和未匹配质量加匹配代价的组合分数。

## 4. 实验设计

### 4.1 实验问题

由于本文初稿尚未填入最终实验结果，本节先明确实验要验证的核心问题。

**Q1：非平衡传输是否必要？**  
如果平衡最优传输已经能够取得相同效果，则“拒绝匹配”不是必要贡献。为此，需要比较无传输打分、平衡最优传输、部分最优传输和非平衡最优传输。

**Q2：双曲正常性代价是否必要？**  
如果非平衡传输配合余弦代价即可达到相同效果，则双曲空间不应作为核心贡献。为此，需要在相同 UOT 框架下比较余弦代价、欧氏代价、双曲距离代价和双曲锥违背代价。

**Q3：未匹配质量是否真能作为异常证据？**  
如果未匹配质量与真实异常区域没有对应关系，则 UOT 只是复杂的后处理。为此，需要比较未匹配质量、匹配代价和组合分数，并分析它们在正常像素与异常像素上的分布。

### 4.2 数据集与评价指标

主实验应至少包含 MVTec AD 和 VisA，以覆盖工业异常检测中的多类别对象和多样缺陷类型 `[引用待核验]`。若时间允许，可进一步加入 MPDD、BTAD、SDD、DAGM 等工业数据集，以及 AnomalyCLIP 中使用的医学数据集，测试跨域泛化能力。

标准指标包括：

```text
Pixel AUROC
Pixel AUPRO
Image AUROC
Image AP
```

机制指标包括：

```text
normal_fpr_at_target_tpr
unmatched_mass_gap
unmatched_mass_auc
matched_cost_gap
overmatch_rate
transport_entropy
runtime / memory
```

其中，`normal_fpr_at_target_tpr` 用于衡量复杂正常结构上的误报，`unmatched_mass_gap` 用于衡量未匹配质量在异常区域和正常区域之间的差异，`overmatch_rate` 用于检验平衡传输是否强制将异常区域匹配到正常性锚点。

### 4.3 主实验

主实验比较本文方法与现有 CLIP ZSAD 打分机制：

```text
cosine prompt scoring
euclidean contrastive energy
hyperbolic distance scoring
hyperbolic cone contrastive scoring
hyperbolic cone scoring without OT
UOT with cosine cost
UOT with hyperbolic distance cost
UOT with hyperbolic cone cost
```

该实验的目标不是单纯证明某个平均指标最高，而是验证本文方法是否同时改善定位指标和失败模式。如果 `uot_hyperbolic_cone` 在 Pixel AUPRO、normal FPR 或弱类定位上优于 `cone_contrastive` 和 `uot_cosine`，则可以支持“质量松弛 + 双曲代价”共同有效的主张 `[结果待填]`。

### 4.4 传输模式消融

为了验证非平衡传输的必要性，在相同双曲锥代价下比较：

```text
no OT cone scoring
balanced OT
partial OT
unbalanced OT
```

预期观察是：平衡 OT 由于必须保持质量守恒，会将异常区域也强制匹配到正常性锚点；部分 OT 可以拒绝一部分质量，但对预设匹配比例敏感；非平衡 OT 则应更稳定地生成与异常区域相关的未匹配质量 `[结果待填]`。

### 4.5 代价函数消融

为了验证双曲代价的必要性，在相同 UOT 设置下比较：

```text
cosine cost
euclidean cost
hyperbolic distance cost
hyperbolic cone violation cost
```

若 UOT + cosine cost 已经达到与 UOT + hyperbolic cone 相同的效果，则论文应将主要贡献收窄为“非平衡语义传输”，而不是强调双曲空间。如果双曲锥代价在复杂正常结构和细粒度缺陷上更稳定，则可以支持“正常性结构代价”这一主张 `[结果待填]`。

### 4.6 锚点负对照

为了排除 prompt engineering 或锚点数量带来的伪增益，需要在完全相同的 UOT 设置、超参数和锚点数量下比较：

```text
learned normal anchors
generic normality anchors
random text anchors
unrelated text anchors
shuffled class anchors
anomaly-only anchors
```

如果随机、无关或错配文本锚点接近正常性锚点的效果，则“normality semantic transport”的解释不成立，论文应退回到更弱的分数校准或后处理表述。若正常性锚点稳定优于这些负对照，才可以支持本文关于 patch-to-normality 语义传输的机制主张 `[结果待填]`。

### 4.7 异常信号分解

为了分析异常分数的来源，需要比较：

```text
score = unmatched mass
score = matched cost
score = unmatched mass + matched cost
```

该实验可以回答：异常区域主要表现为无法匹配，还是表现为高代价匹配。若未匹配质量单独具有较强定位能力，则 UOT 的拒绝机制更有说服力；若匹配代价与未匹配质量互补，则组合分数更合理 `[结果待填]`。

### 4.8 失败模式可视化

本文需要重点展示复杂正常结构上的误报修复，而不仅是平均指标提升。建议选取 MVTec 中的 capsule、pill、screw、toothbrush 和 transistor 等类别，展示以下对比：

```text
原图
GT mask
cosine anomaly map
cone contrastive anomaly map
balanced OT map
UOT unmatched mass map
UOT matched cost map
final UOT anomaly map
```

该可视化应回答：UOT 是否减少了正常图像中复杂局部结构的误报，同时保留真实缺陷区域的响应 `[结果待填]`。

### 4.9 敏感性与效率

UOT 引入了额外超参数，包括熵正则 `epsilon`、质量松弛参数 `tau_patch` 和 `tau_anchor`。因此需要报告超参数敏感性和推理开销。若方法对超参数高度敏感，审稿人可能认为其实际价值不足。建议报告：

```text
AUPRO vs epsilon
AUPRO vs tau_patch / tau_anchor
runtime vs number of anchors
memory usage
Sinkhorn iterations
```

## 5. 讨论

本文方法的核心价值不在于简单叠加 CLIP、双曲空间和最优传输，而在于将 CLIP 零样本异常定位解释为可拒绝的语义匹配问题。这个建模方式改变了异常证据的来源：异常不再只是与 abnormal prompt 更相似，而是可以表现为无法被正常性锚点低代价接收的未匹配质量。

然而，该主张必须通过实验严格限定。若 UOT 与平衡 OT 的差异不明显，则质量松弛并非必要；若 UOT + cosine cost 与双曲 UOT 表现相同，则双曲几何不应作为核心贡献；若未匹配质量不能与真实异常区域对齐，则 UOT 更可能只是复杂的分数变换。因此，本文的最终写作应根据实验结果调整主张强度。

## 6. 局限性

本文目前存在若干明确局限。第一，正常性锚点的质量会直接影响语义传输效果。如果锚点过少或语义过粗，UOT 可能无法产生有意义的未匹配质量。第二，非平衡最优传输引入了额外超参数，若超参数需要针对不同数据集频繁调节，则方法的实用性会下降。第三，双曲代价是否优于平坦代价需要通过严格消融验证，不能在实验前假定。第四，Sinkhorn 求解带来额外推理开销，需要报告运行时间和内存成本。第五，本文相关工作中的具体文献和引用尚未完成程序化核验，所有引用均需在正式稿前补齐。

## 7. 结论

本文提出一种面向 CLIP 零样本异常定位的双曲非平衡语义传输框架。该框架将异常定位从独立的 patch-wise prompt scoring 重新表述为可拒绝的 patch-to-normality matching：正常 patch 应能够被正常性锚点低代价解释，而异常 patch 则表现为高匹配代价或未匹配质量。方法上，本文利用双曲空间构造正常性语义代价，并通过非平衡最优传输生成未匹配质量和匹配代价作为异常证据。后续实验将系统验证质量松弛、双曲代价和异常分数组成的作用，并根据实验结果进一步收窄或强化论文主张。

## 8. Claim-Evidence Map

| Claim | Evidence | Status |
|---|---|---|
| CLIP ZSAD 的平坦 prompt scoring 会强制每个 patch 进入 normal/anomaly 分类。 | 方法定义和现有范式分析；需在相关工作中引用具体方法。 | needs citation |
| 异常 patch 可以被建模为无法被正常性锚点解释的未匹配质量。 | 本文方法假设；需通过 unmatched mass 与 GT mask 的相关性验证。 | needs experiment |
| UOT 比 balanced OT 更适合异常定位。 | 需要 balanced/partial/unbalanced OT 消融和 overmatch_rate 指标。 | needs experiment |
| 双曲代价比余弦/欧氏代价更适合正常性传输。 | 需要 UOT 下的 cost-type ablation。 | needs experiment |
| 正常性锚点是机制必要部分，而非任意文本锚点均可。 | 需要 random/unrelated/shuffled anchor negative control。 | needs experiment |
| 组合未匹配质量和匹配代价能够生成更稳定的异常图。 | 需要 score decomposition ablation。 | needs experiment |
| 方法能降低复杂正常结构上的误报。 | 需要 failure-mode benchmark 和 normal_fpr_at_target_tpr。 | needs experiment |

## 9. 图表占位

| 编号 | 内容 | 状态 |
|---|---|---|
| Figure 1 | 从 flat prompt scoring 到 unbalanced semantic transport 的动机图 | 待画 |
| Figure 2 | 方法流程图：CLIP patch/text features -> hyperbolic cost -> UOT -> anomaly map | 待画 |
| Figure 3 | UOT 机制图：transport mass / unmatched mass / matched cost / final score | 待实验 |
| Figure 4 | 复杂正常结构 failure-mode 可视化 | 待实验 |
| Table 1 | 主实验对比 | 待实验 |
| Table 2 | transport mode ablation | 待实验 |
| Table 3 | cost type ablation | 待实验 |
| Table 4 | score decomposition | 待实验 |
| Table 5 | sensitivity and runtime | 待实验 |
