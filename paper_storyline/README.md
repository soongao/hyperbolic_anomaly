# Hyperbolic Contrastive Normality Entailment 故事线

## 1. 一句话主张

异常检测不应被建模成普通的“normal vs anomaly”平坦分类问题，而应被建模成一个语义蕴含问题：正常区域应当能被正常语义锥解释，异常区域则表现为对正常语义锥的违背，并且更容易被异常语义锥解释。

因此，本文方法可以命名为：

**Hyperbolic Contrastive Normality Entailment**

一句英文主张可写为：

> We model anomaly detection as contrastive semantic entailment in hyperbolic space: a region is anomalous not merely because it is dissimilar to normal text, but because it violates the normality cone while being better explained by the anomaly cone.

## 2. 论文切入点

现有 CLIP 异常检测方法通常将正常 prompt 和异常 prompt 当成两个并列类别，然后用 cosine similarity 做二分类。这种做法有一个隐含假设：异常是一个与正常并列的语义类别。

但工业异常并不总是一个完整的新类别。多数异常是局部纹理、形状、结构或材料状态对正常对象语义的破坏。例如 pill、capsule、screw、toothbrush 这类对象中，异常区域往往只是局部划痕、压痕、污渍、缺口或几何不连续。它们的关键不是“像不像 anomaly 这个词”，而是“这个局部区域是否仍然能被 normal object 的语义结构解释”。

所以本文的切入点是：

**从平坦相似度分类转向层级语义蕴含判别。**

## 3. 为什么使用双曲空间

双曲空间的作用不是简单替换 cosine distance，而是给正常语义提供一种层级约束表达。

在 Poincare ball 中，语义可以表示为具有包含关系的几何结构。正常文本特征不再只是一个点，而可以作为一个 normality cone 的锚点。正常 patch 应落在 normality cone 内，表示它能被正常语义解释；异常 patch 会偏离该锥，表示它破坏了正常语义。

这与工业异常检测的任务本质一致：

- 正常区域：局部外观可被对象正常语义解释。
- 异常区域：局部外观破坏正常语义约束。
- 细粒度异常：不是新类别，而是正常结构中的局部违背。

## 4. 为什么不是 normal-only

最初的 normal-only 设计只计算 patch 对 normality cone 的违背程度：

```text
score = violation(patch, normal_cone)
```

这个设计在概念上合理，但实验暴露出问题：复杂正常结构也可能偏离 normal prompt。比如 screw 的螺纹、pill 的纹理边界、capsule 的局部形态变化，本身就是正常对象的一部分，但它们在局部 patch 级别可能不像一个干净的 normal prompt。

因此，只看 normal cone violation 会把“复杂但正常的局部结构”误判成异常。

这解释了 normal-only 在弱类上的表现不足：

| class | old pixel AUROC | old pixel AUPRO |
|---|---:|---:|
| capsule | 73.2 | 77.9 |
| pill | 57.5 | 81.0 |
| transistor | 69.3 | 55.4 |
| screw | 83.4 | 63.0 |
| toothbrush | 77.7 | 80.0 |

## 5. 最终机制：normal cone vs anomaly cone

最终方法不是只建 normal cone，而是同时建立 normal cone 和 anomaly cone。一个 patch 是否异常，由两种解释能力的相对关系决定：

```text
normal_energy  = violation(patch, normal_cone)
anomaly_energy = violation(patch, anomaly_cone)
anomaly_score  = softmax(-normal_energy, -anomaly_energy)[anomaly]
```

如果一个 patch 既违背 normal cone，又更容易被 anomaly cone 解释，它才被判为异常。

这个设计保留了 anomaly prompt，但不把它当成普通分类标签，而是作为异常解释锚点参与双曲蕴含判断。这样故事线是自洽的：

- normal prompt 定义“正常语义可解释区域”。
- anomaly prompt 定义“异常语义可解释区域”。
- patch 的异常性来自两个语义锥之间的相对蕴含关系。

## 6. 为什么去掉 patch context cone

实验中发现 `context_weight=0` 更适合弱类。原因是工业异常检测关注局部缺陷，而不是强制每个 patch 都服从整图上下文。

全局图像上下文对一些对象是有帮助的，但对多部件、细结构或形态变化明显的对象会制造误报。例如 transistor 有多个正常部件，局部 patch 与全局图像语义天然存在差异；pill 和 capsule 也有局部纹理、边缘、形态变化。若强行加入 image-level context cone，容易把这些正常局部差异看成异常。

因此本文可以将最终推理 recipe 设为：

```text
features_list = [24]
entailment_mode = contrastive
context_weight = 0.0
patch_score_space = prob
```

## 7. 为什么不采用当前多尺度求和

多尺度本身是合理方向，但当前直接把多个层级 patch map 求和，会放大浅层 patch 的几何噪声。实验中 `features_list=[6,12,18,24]` 明显退化，说明浅层局部特征在双曲锥判别中还不够稳定。

这个结果不能写成“多尺度无效”，而应该写成：

**naive multi-layer aggregation is not suitable for hyperbolic entailment scoring without scale calibration.**

也就是说，多尺度不是被否定，而是需要额外的尺度校准或层级门控。当前论文版本应先保留最稳定的单层高语义 patch 特征。

## 8. 关键实验支撑

采用 `contrastive + context_weight=0` 后，弱类结果明显提升：

| class | pixel AUROC | pixel AUPRO | image AUROC | image AP |
|---|---:|---:|---:|---:|
| capsule | 96.7 | 93.0 | 90.3 | 98.0 |
| pill | 90.9 | 94.4 | 81.9 | 95.2 |
| transistor | 73.1 | 57.8 | 86.8 | 82.6 |
| screw | 97.2 | 90.3 | 83.7 | 93.4 |
| toothbrush | 94.2 | 89.1 | 91.9 | 97.0 |
| weak mean | 90.4 | 84.9 | 86.9 | 93.2 |

替换弱类后的 MVTec 全量均值为：

| metric | mean |
|---|---:|
| pixel AUROC | 91.7 |
| pixel AUPRO | 85.6 |
| image AUROC | 92.6 |
| image AP | 96.5 |

## 9. Ablation 叙事

建议 ablation 按下面顺序组织，而不是罗列参数：

1. **Normal-only entailment**  
   证明只建 normal cone 会误伤复杂正常局部结构。

2. **Contrastive entailment**  
   加入 anomaly cone 后，异常 prompt 从分类标签变成异常解释锚点，弱类显著提升。

3. **Patch context cone**  
   `context_weight=0` 更好，说明局部异常判别不应强制绑定全局图像语义。

4. **Naive multi-scale aggregation**  
   多尺度直接求和退化，说明双曲 entailment map 需要尺度校准；当前采用单层高语义 patch 作为稳定配置。

## 10. Introduction 可用段落骨架

第一段：指出 CLIP 异常检测的主流做法。

> Recent CLIP-based anomaly detection methods commonly formulate anomaly scoring as a flat similarity comparison between normal and abnormal text prompts. While effective, this formulation implicitly treats anomalies as a semantic category parallel to normality.

第二段：指出工业异常的本质不是新类别，而是正常语义破坏。

> However, industrial anomalies are often not independent semantic categories. They are local violations of the expected appearance, structure, or material state of a normal object.

第三段：引出双曲语义蕴含。

> This motivates us to reinterpret anomaly detection as a semantic entailment problem: a normal region should be entailed by the normal object semantics, whereas an anomalous region violates such normality constraints.

第四段：引出 contrastive cone。

> To avoid confusing complex normal structures with anomalies, we further introduce contrastive entailment between normal and anomaly cones, where the anomaly score is determined by their relative explanatory energies.

## 11. Method 可用公式描述

给定 patch feature `p`、normal text feature `t_n`、anomaly text feature `t_a`，先映射到 Poincare ball：

```text
z_p = Exp_0(p), z_n = Exp_0(t_n), z_a = Exp_0(t_a)
```

定义 patch 对正常锥和异常锥的违背能量：

```text
E_n(p) = V(z_p, Cone(z_n))
E_a(p) = V(z_p, Cone(z_a))
```

最终异常概率：

```text
P_anom(p) = exp(-E_a(p)) / (exp(-E_n(p)) + exp(-E_a(p)))
```

这里 `E_a` 越小，说明 patch 越容易被 anomaly cone 解释；`E_n` 越大，说明 patch 越违背 normal cone。两者共同决定异常性。

## 12. Claim 边界

可以主张：

- 本方法将异常检测从平坦 prompt 相似度转化为双曲语义蕴含判别。
- normal/anomaly cone 的 contrastive 设计能缓解 normal-only 对复杂正常局部结构的误判。
- 对弱类的提升支持该机制对细粒度局部异常更有效。

不要过度主张：

- 不要说多尺度无效，只能说 naive multi-scale aggregation 在当前双曲 entailment score 下不稳定。
- 不要说双曲空间天然优于欧式空间，应强调“与正常语义蕴含建模相匹配”。
- 不要说 anomaly prompt 只是辅助分类器，应强调它是 contrastive entailment 中的异常解释锚点。

