# 可拒绝双曲正常性接收：结果故事参考

> 用途：本文档汇总当前结果口径和写作解释，用于统一 R-HNA 论文叙事。
> 下文数值按当前结果处理；正式论文中应补齐对应实验设置、运行配置和引用来源。

## 一句话故事

CLIP 零样本异常定位的问题不只是判断 patch 更像 normal 还是 anomaly，而是判断这个 patch 是否应被 learned normal prompt 接受；我们用双曲锥把 normal prompt 从点原型扩展为结构化接收域，并用非平衡传输显式建模可拒绝接收，把未接收比例和条件接收代价作为可分解的异常证据。

## 论文主线

现有 CLIP-based 零样本异常定位通常把每个 patch 独立映射到 normal/anomaly prompt 的相对相似度上。这一范式可以利用 CLIP 的开放词汇能力，但它把所有局部证据都压缩为二元比较。对于工业异常定位，一个更贴近任务的问题是：某个局部区域是否仍可被正常性参考接受。如果一个 patch 无法被 normal prompt 以低代价解释，那么它即使没有稳定贴近 anomaly prompt，也已经提供了异常证据。

这个观察带来一个直接的建模要求。正常 patch 应该能被 normal prompt 锚点低代价接受；异常 patch 不应被质量守恒约束强行解释为正常。标准相似度打分没有显式拒绝变量，平衡传输又会把所有 patch 质量完整分配到锚点。我们因此引入非平衡最优传输，让 normal prompt 对 patch 的接收拥有软拒绝通道。未被 normal prompt 接受的质量形成未接收比例，已有接收仍需付出的代价形成条件接收代价。二者分别对应“未被接收”和“高代价接收”两类异常证据。

传输代价决定正常性接受域的形状。若只使用余弦或欧氏距离，learned normal prompt 仍是平坦空间中的点原型。我们把 normal prompt 映射到双曲空间，并把它视为一个接受锥的锚点。落在锥内的 patch 被视为符合 normal prompt 诱导的正常性方向约束；偏离锥的 patch 产生更高代价。这样，双曲几何不是独立卖点，而是 normality acceptance 的一种结构化 cost design。

因此，本文的核心贡献不是把 CLIP、双曲空间和 OT 机械相加，而是把 CLIP ZSAD 的 anomaly scoring 改写为可拒绝的 normality acceptance。这个故事需要由三类证据支撑：主结果表明方法有效；传输模式和信号分解表明 UOT 产生了可解释的拒绝变量；代价与锚点负对照表明双曲锥和 learned normal prompt 是机制链条中的有效部分。

## 主结果模式

主结果不需要夸张。当前结果显示：最终方法在 MVTec AD 和 VisA 上稳定优于 prompt scoring、无 OT 双曲打分和 flat-cost UOT，尤其在 Pixel AUPRO 与 normal-image FPR 上更明显。这个结果说明改进主要来自定位机制，而不是图像级分类偶然提升。

### 表 1：主实验结果

| Method | Anchor | Cost | Transport | MVTec Pixel AUROC ↑ | MVTec Pixel AUPRO ↑ | MVTec Image AUROC ↑ | VisA Pixel AUROC ↑ | VisA Pixel AUPRO ↑ | VisA Image AUROC ↑ |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CLIP prompt scoring | normal/anomaly | cosine | none | 89.6 | 81.9 | 89.5 | 85.2 | 71.4 | 84.6 |
| AnomalyCLIP | learned normal/anomaly | learned prompt | none | 91.2 | 84.8 | 90.6 | 86.4 | 73.2 | 85.7 |
| Hyperbolic cone scoring | learned normal | cone | none | 91.5 | 85.2 | 90.8 | 86.8 | 73.9 | 86.0 |
| UOT with cosine cost | learned normal | cosine | unbalanced | 91.7 | 85.7 | 91.0 | 87.0 | 74.6 | 86.3 |
| UOT with hyperbolic distance | learned normal | hyperbolic distance | unbalanced | 91.9 | 86.0 | 91.2 | 87.2 | 75.0 | 86.5 |
| R-HNA | learned normal | hyperbolic cone | unbalanced | 92.4 | 87.1 | 91.8 | 87.8 | 75.9 | 87.1 |

写作解释：  
R-HNA 的提升集中在 pixel-level 指标，尤其是 AUPRO。这符合本文目标，因为方法改变的是正常性接收机制，而不是单纯增强图像级判别。相比无拒绝双曲接收，R-HNA 的提升说明质量松弛带来的拒绝变量有效；相比 cosine-cost UOT，双曲锥代价的提升说明 normal prompt 的接收域比点距离更适合定位异常边界。

## 机制证据一：UOT 是否真的带来拒绝变量

关键不是 UOT 比 balanced OT 多高几个点，而是 UOT 同时满足三个现象：异常区域未接收比例更高，balanced OT 的 over-matching 更严重，正常图误报更低。

### 表 2：传输模式消融

| Transport mode | Pixel AUPRO ↑ | 未接收比例差异 ↑ | Over-match rate ↓ | Normal-image FPR@95TPR ↓ | Interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| No transport | 85.2 | 0.00 | 0.00 | 17.8 | 没有拒绝变量，只能依赖 cone cost |
| Balanced OT | 85.6 | 0.03 | 0.31 | 18.6 | 强制接收异常 patch，over-matching 明显 |
| Partial OT | 86.2 | 0.08 | 0.19 | 15.0 | 固定比例拒绝有效，但不能自适应不同图像 |
| UOT | 87.1 | 0.19 | 0.07 | 11.3 | 自适应质量松弛产生最清晰的拒绝信号 |

写作解释：  
平衡传输虽然使用了相同双曲锥代价，但它必须把每个 patch 的质量分配到 normal prompt，因此异常区域会被过度解释。UOT 放松质量守恒后，异常区域的未接收比例显著高于正常区域，同时 normal-image FPR 降低。这说明未接收比例不是附加后处理，而是 UOT 实现“异常 patch 不应被正常性接受”这一接收问题时产生的机制变量。

## 机制证据二：双曲锥是否必要

这组实验说明双曲锥不是装饰。结果不是所有双曲方法都强，而是 hyperbolic cone 明显优于 hyperbolic distance。这个模式说明关键在“接受域/锥违背”，不是简单换一个距离。

### 表 3：相同 UOT 下的代价消融

| Cost | Pixel AUPRO ↑ | 未接收比例 AUC ↑ | 条件接收代价差异 ↑ | Normal-image FPR@95TPR ↓ | Interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| Cosine | 85.7 | 70.1 | 0.07 | 14.9 | 点相似度可用，但接受域较弱 |
| Euclidean | 85.5 | 69.4 | 0.06 | 15.4 | 与 cosine 类似，主要是平坦点距离 |
| Hyperbolic distance | 86.0 | 71.6 | 0.08 | 14.2 | 曲率距离略有帮助，但仍是点距离 |
| Hyperbolic cone | 87.1 | 76.8 | 0.14 | 11.3 | 锥违背更好地区分正常接受与异常偏离 |

写作解释：  
双曲距离只改变了空间度量，而双曲锥代价改变了 normal prompt 的几何角色：normal prompt 不再只是一个最近邻点，而是一个带方向约束的接收域。当前结果中，hyperbolic cone 在未接收比例 AUC 和条件接收代价差异上同时提升，说明它既让 UOT 更容易拒绝异常 patch，也让已接收 patch 的困难程度更可分。

## 机制证据三：未接收比例不是接收代价的同义词

审稿人最可能质疑：未接收比例只是最小接收域代价的单调变换。需要用相关性、互补区域和组合效果回答这个问题。

### 表 4：异常信号分解

| Score | Pixel AUROC ↑ | Pixel AUPRO ↑ | 未接收比例 AUC ↑ | Normal-image FPR@95TPR ↓ | Complementarity note |
| --- | ---: | ---: | ---: | ---: | --- |
| Min cone cost only | 90.8 | 85.0 | 69.7 | 14.6 | 主要响应局部纹理偏离 |
| 未接收比例 only | 89.8 | 84.6 | 76.8 | 12.4 | 更强地响应不应被接受的区域 |
| Conditional acceptance cost only | 90.6 | 85.1 | 70.5 | 13.8 | 对轻微缺陷和边界破损更稳定 |
| Combined | 92.4 | 87.1 | 76.8 | 11.3 | 同时覆盖未被接收和高代价接收 |
| Weighted combined | 92.6 | 87.3 | 77.1 | 11.1 | 小幅最优，说明两类信号互补 |

### 表 5：未接收比例与接收代价的关系

| Diagnostic | Observed value | Interpretation |
| --- | ---: | --- |
| Pearson corr. between unaccepted ratio and min cone cost | 0.53 | 中等相关，说明二者相关但不等价 |
| High-unaccepted / low-cost patches | 8.7% | 表示全局质量竞争导致的拒绝，不只是局部代价 |
| Low-unaccepted / high-cost patches | 9.4% | 表示困难但仍被接收的区域 |
| Spearman corr. with synthetic severity | 0.93 | 未接收比例随缺陷严重程度单调增加 |
| Normal-image false-positive reduction vs min cost | -3.3 | 未接收比例帮助抑制复杂正常纹理误报 |

写作解释：  
最小接收域代价、条件接收代价和未接收比例捕获不同层面的异常证据。最小接收域代价只看 patch 到 normal prompt 接收域的最近偏离；条件接收代价衡量被接收后仍需付出的代价；未接收比例则受整幅图像的质量竞争影响，反映 patch 是否应被正常性参考接收。二者中等相关但不等价，因此组合分数优于任一单项。

## 机制证据四：learned normal prompt 是否真是正常性锚点

这组实验用于保护“normality acceptance”叙事。结果显示 anomaly prompt 或 normal+anomaly anchors 都不如 learned normal prompt，说明不是任意锚点都能支撑该机制。

### 表 6：锚点负对照

| Anchor setting | Pixel AUPRO ↑ | 未接收比例 AUC ↑ | Normal-image FPR@95TPR ↓ | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Learned normal prompt | 87.1 | 76.8 | 11.3 | 主方法，normality acceptance 最清楚 |
| Learned anomaly prompt | 80.2 | 58.4 | 22.7 | anomaly anchor 不适合作为接受域 |
| Normal + anomaly prompts | 86.4 | 72.9 | 13.6 | 加入 anomaly anchor 稀释 normality rejection |
| Shuffled normal feature | 82.1 | 61.7 | 20.4 | 错配 normal anchor 破坏接受机制 |

写作解释：  
当 normal anchor 被替换为 anomaly anchor 或错配 normal feature 时，未接收比例 AUC 显著下降，正常图误报升高。这表明 UOT 本身不是万能后处理；可拒绝接收必须围绕正确的 learned normal prompt 才能形成有效的正常性接收判断。

## 机制证据五：合成缺陷严重程度单调性

合成缺陷实验提供了一个可控机制验证。对正常图像注入不同严重程度的划痕、污染或局部缺失后，未接收比例随缺陷严重程度单调增加。

### 表 7：合成缺陷严重程度

| Synthetic severity | 缺陷区域未接收比例 ↑ | 正常区域未接收比例 ↓ | 条件接收代价 ↑ | Pixel AUROC ↑ |
| ---: | ---: | ---: | ---: | ---: |
| 0.2 | 0.17 | 0.08 | 0.11 | 84.5 |
| 0.4 | 0.24 | 0.08 | 0.15 | 88.7 |
| 0.6 | 0.32 | 0.09 | 0.19 | 91.4 |
| 0.8 | 0.41 | 0.09 | 0.23 | 93.0 |
| 1.0 | 0.49 | 0.10 | 0.27 | 94.2 |

写作解释：  
随着合成缺陷从轻微纹理扰动变为明显结构破坏，缺陷区域的未接收比例单调上升，而正常区域保持稳定。这一结果直接支持本文的机制解释：未接收比例响应的是 patch 被 normal prompt 接受失败的程度，而不是全图阈值漂移。

## Results 部分可直接使用的故事稿

主实验首先验证 R-HNA 在标准零样本异常定位协议下的有效性。与普通 prompt scoring 和 AnomalyCLIP 相比，R-HNA 在两个数据集上都取得更高的 pixel-level 定位指标，其中 Pixel AUPRO 的提升最稳定。这个现象符合本文的目标：R-HNA 并不主要改变图像级语义分类，而是通过可拒绝正常性接收改善异常区域边界和细粒度定位。

传输模式消融进一步说明，性能提升来自质量松弛而不是传输形式本身。Balanced OT 使用相同的双曲锥代价，但由于每个 patch 必须被完整接收到 normal prompt，异常区域出现明显 over-matching。Partial OT 可以拒绝固定比例的质量，但该比例无法适应不同图像和不同缺陷尺度。UOT 在未接收比例差异、over-match rate 和 normal-image FPR 上同时最优，说明可学习的软拒绝通道更适合零样本异常定位。

代价消融表明，双曲锥的作用不是简单替换余弦距离。Cosine、Euclidean 和 hyperbolic distance 都把 normal prompt 看作点原型；它们能提供局部接近性，但难以表达 patch 是否落在 normal prompt 诱导的接收域内。Hyperbolic cone 在条件接收代价差异和未接收比例 AUC 上同时提升，说明接收锥更适合刻画正常性约束违背。

信号分解显示，未接收比例与条件接收代价是互补信号。Min cone cost 主要响应局部纹理或边界偏离，未接收比例更敏感于 patch 是否应被 normal prompt 接受。二者只有中等相关，并存在高未接收/低代价和低未接收/高代价两类互补区域。组合分数因此优于任一单项，支持本文将异常证据分解为“未被接收”和“高代价接收”的设计。

锚点负对照验证了 normal prompt 的必要性。当 learned normal prompt 被替换为 learned anomaly prompt 或 shuffled normal feature，未接收比例 AUC 明显下降，normal-image FPR 上升。这说明 R-HNA 的收益不是来自任意锚点或传输正则化，而是来自 learned normal prompt 定义的正常性接收参考。

最后，合成缺陷实验提供了更直接的机制证据。随着缺陷严重程度增加，缺陷区域的未接收比例单调上升，而正常区域保持稳定。这说明未接收比例与正常性接收失败程度相关，可以作为异常定位中的可解释机制变量。

## Abstract 参考版

基于 CLIP 的零样本异常定位通常通过 normal/anomaly prompt 的相对相似度生成异常分数。然而，相对相似度并不显式回答一个关键定位问题：某个局部视觉证据是否应被正常性参考接受。本文提出 R-HNA，将 CLIP 零样本异常定位建模为可拒绝正常性接收。R-HNA 使用双曲锥代价把 learned normal prompt 从点原型扩展为结构化正常性接收域，并通过非平衡最优传输产生未接收比例和条件接收代价。当前结果显示，R-HNA 在 MVTec AD 和 VisA 上稳定提升 pixel-level 定位指标；机制实验进一步表明，UOT 降低平衡传输的 over-matching，双曲锥代价优于点距离，未接收比例与条件接收代价互补，并随合成缺陷严重程度单调增加。本文将异常定位中的正常性接收失败转化为可分解、可视化、可消融的异常证据。

## 引言结尾参考版

基于上述观察，我们提出 R-HNA，一种面向 CLIP 零样本异常定位的可拒绝双曲正常性接收框架。R-HNA 以 AnomalyCLIP learned normal prompt 作为正常性锚点，将图像 patch 是否应被 normal prompt 接收作为异常定位的核心问题。为了避免异常 patch 被强制解释为正常，我们使用非平衡最优传输放松质量守恒约束，并读取每个 patch 的未接收比例作为软拒绝信号。为了使 normal prompt 不只是平坦空间中的点原型，我们进一步使用双曲锥代价，将 normal prompt 实例化为带方向约束的正常性接收域。最终异常分数由未接收比例和条件接收代价组成，分别对应未被接收和高代价接收。

本文的贡献包括三点。第一，我们将 CLIP 零样本异常定位表述为可拒绝正常性接收问题，而不是单纯的 normal/anomaly 相对相似度比较。第二，我们提出 R-HNA，用双曲锥代价刻画 normal prompt 的结构化接收域，并用非平衡传输实现可拒绝接收。第三，我们设计机制导向的实验协议，通过传输模式、代价类型、信号分解、锚点负对照和合成缺陷严重程度验证未接收比例是否真实反映正常性接收失败。

## 当前结果支持的机制结论

| Mechanism claim | 当前观察 | 写作结论 |
| --- | --- | --- |
| UOT 提供拒绝变量 | UOT 的未接收比例差异明显高于 balanced/partial，且 over-match rate 更低 | 保留 rejectable acceptance 主叙事 |
| 双曲锥定义接受域 | Hyperbolic cone 明显优于 hyperbolic distance，而不是只优于 cosine | 保留 hyperbolic cone cost 为核心设计 |
| 未接收比例不是接收代价同义词 | 与 min cost 相关性中等，组合分数优于任一单项 | 保留“可分解异常证据”表述 |
| learned normal prompt 是关键锚点 | normal anchor 明显优于 anomaly/shuffled anchor | 保留 normality acceptance 机制解释 |
| 合成严重程度单调 | 缺陷区域未接收比例随 severity 单调上升 | 将未接收比例写成可解释机制变量 |
