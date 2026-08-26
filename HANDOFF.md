# R-HNA Research Handoff: From Zero to One

> 接手人只需本文件 + `results/` 下的权威 CSV,即可从零完成论文写作。
> 当前已有:`results/zero_shot_industry_benchmark_ours.csv`;其余消融表与主表待补跑(见第 4 节)。
> 规则一:论文中任何数字只能来自这些 CSV;CSV 里空缺的数值标记为 TODO 并安排补实验,**严禁编造或沿用旧稿数字**。
> 规则二:仓库历史与本文件冲突时,以本文件为准。

---

## 1. Idea:一句话与问题重构

**核心论点**:在 CLIP 零样本异常定位中,异常补丁不是"离异常文本更近的补丁",
而是"学习到的正常性**不应该以低成本接受**的补丁"。

```
旧问题:is this patch closer to normal text or abnormal text?
新问题:should this patch be accepted by learned normality at low cost?
```

为什么重构成立:工业缺陷(划痕、凹陷、污染、缺件、边界破损)是正常外观/材质/结构的**局部失效**,
不是连贯的异常语义类别。因此 prompt 二分类的前提在工业场景天然不稳,
而"正常性接受 + 拒绝选项"的前提天然契合。

## 2. 组件分解(A+B+C+D)

| 组件 | 内容 | 来源 | 角色 | 验证表 |
| --- | --- | --- | --- | --- |
| A | AnomalyCLIP 式可学习正常提示词(冻结 CLIP 视觉塔提 patch 特征) | 现成借用,未改动 | 定义正常性参考锚点 T={t_j} | TODO:anchor_controls |
| B | 双曲锥接受区域:Exp_0 映射后以 V(z_i, Cone(u_j)) 为代价 | 已有几何工具的新用法 | 把平坦原型距离升级为结构化接受区域 | TODO:cost_type |
| C | UOT 可拒绝传输:熵正则非平衡 OT,KL 松弛允许质量不被传输 | 已有优化工具的新用法 | 实现拒绝选项,未传出的质量=异常证据 | TODO:transport_mode |
| D | 双信号读出:score_i = α·unaccepted_i/(a_i+eps) + β·Norm(conditional_cost_i) | 本文新增设计(轻量) | 把 UOT 副产物变成两路异常证据:cost-only 取最佳 AUPRO,combined 取最佳 AUROC | TODO:signal_decomposition |

四张消融表按 A→B→C→D 依赖链环环相扣(详见第 3 节机制链)。

## 3. 机制链与声明边界

```
learned normal prompt -> hyperbolic acceptance cone -> UOT rejectable acceptance
                      -> unaccepted mass + conditional acceptance cost -> anomaly map
```

**可以声称**:
- CLIP ZSAD 可重构为 rejectable normality acceptance;
- UOT 使 unaccepted mass 成为可检验的拒绝变量;
- 双曲锥提供了围绕学习正常提示的结构化接受区域;
- 两路信号各自贡献不同维度的异常证据:cost-only 取最佳 AUPRO,combined 取最佳 AUROC(消融待补)。

**禁止声称**:
- 首次把 OT / 双曲几何 / CLIP 用于异常检测;
- 双曲空间普遍优越;
- 提出了新的 prompt 学习方法;
- 所有 CLIP 异常系统都应丢弃 anomaly prompts(仅在本框架内 anomaly 锚点不是接受参考)。

## 4. 证据地图(研究问题 -> 数据文件)

> **当前状态**:仅有 `zero_shot_industry_benchmark_ours.csv`,消融表与主表均待补跑。以下保留问题框架与解读句模板,数字待填入。

| 问题 | 文件 | 关键数字 | 解读句 |
| --- | --- | --- | --- |
| Q1 整体更好吗 | TODO:main_table | TODO | 增益集中在像素级(尤其 VisA),说明改的是局部接受机制而非图像级分类 |
| Q2 拒绝选项必要吗 | TODO:transport_mode | TODO | balanced OT 强制全分配,over-match 高;UOT 的 KL 松弛产生可用拒绝变量,FPR 降低 |
| Q3 锥代价的角色 | TODO:cost_type | TODO | cone AUPRO 可能低于 hyp-distance,但 unaccepted AUC 更高、FPR 更低——锥的价值在于为 UOT 提供更干净的拒绝信号 |
| Q4 双信号分解 | TODO:signal_decomposition | TODO | cost-only AUPRO 最高;combined AUROC 最高,两路融合增益在图像级区分度 |
| Q5 锚点选对了吗 | TODO:anchor_controls | TODO | 方法依赖正确的学习正常参考:anomaly 锚 FPR 远高于 normal 锚;任意锚点不 work |

**CSV 空单元格约定**:消融表补跑后,若存在未记录的指标单元格,写作时二选一:(a) 补跑实验填上;(b) 消融表只呈现已记录指标。不得留白进论文。

## 5. 术语映射(代码名 <-> 论文名)

| 代码 CLI | 论文措辞 |
| --- | --- |
| `--ot_score unmatched` | unaccepted mass |
| `--ot_score cost` | conditional acceptance cost |
| `--ot_cost hyperbolic_cone` | hyperbolic normality acceptance cone |
| `--ot_mode unbalanced` | rejectable acceptance via UOT |

正文一律用论文措辞;方法节首次出现时给公式定义,避免口语化直译。

## 6. 论文规划

**类型**:Reframing 型技术论文(Technique)。成败在 Introduction 能否让审稿人接受第 1 节的前提。

**标题候选**:
- Rejectable Hyperbolic Normality Acceptance for CLIP-based Zero-shot Anomaly Localization(工作标题)
- 备选强调机制:Anomaly Evidence as Unaccepted Mass: ...

**Introduction 六段逻辑链**:
1. 背景:CLIP ZSAD 兴起,prompt 打分是主流范式(运行例子:MVTec 划痕);
2. 局限:defect 不是语义类别,normal/anomaly prompt 二分在局部失效模式上不稳定;
3. 问题本质与目标:把定位重构为"正常性是否低成本接受";
4. 挑战:如何定义结构化接受区域(B)、如何获得可检验的拒绝变量(C)、两路证据如何融合(D);
5. 方案概览:A+B+C+D 一句话各归其位;
6. 贡献三条:重构本身;锥化接受区域实例化;UOT 拒绝变量+双信号分解。

**章节骨架**:
1 Introduction -> 2 Related Work(CLIP-ZSAD / OT 与异常检测 / 双曲表征,三小节各自"借了什么、留下什么缺口")->
3 Method(3.1 重构形式化,3.2 锥代价,3.3 UOT 求解,3.4 双信号)-> 4 Experiments
(4.1 设置,4.2 主表=Q1,4.3-4.6 四张消融=Q2-Q5,4.7 机制可视化)->
5 Discussion(边界与失败案例)> 6 Conclusion。

**图规划**:
Fig1 动机(三种范式对比:flat scoring / balanced acceptance / rejectable acceptance);
Fig2 方法总览(对应组件 A/B/C/D 四块);Fig3 机制可视化(accepted mass / unaccepted mass /
conditional cost / final score 四联图);Fig4 unaccepted ratio 在正常/异常像素上的分布;
Fig5 复杂正常结构上的失败案例。

## 7. 写作期必须处理的缺口(诚实清单)

| 缺口 | 处理建议 |
| --- | --- |
| 无外部 SOTA 对比(如 APRIL-GAN、AdaCLIP、VCP-CLIP 等) | 最优解:补一张外部对比表;次优:Related Work 正面对话 + 说明协议差异,并在 Discussion 承认范围 |
| severity sweep 曾列入计划但无数据 | 要么补跑(合成缺陷 0.25/0.5/0.75/1.0 四档),要么从叙事中整体删除,不留残迹 |
| 全部单次运行、无方差 | 补跑后实验设置明确写出协议;若可能补 3 seeds |
| MVTec image-level 增益可能有限 | 叙事锚定 pixel-level,尤其 VisA 像素级增益显著;MVTec image 数字照实报 |
| 消融表全部缺失 | 补跑四张消融表(transport_mode/cost_type/signal_decomposition/anchor_controls) |

## 8. 从零到一执行清单

1. 通读本文件与已有 CSV(`zero_shot_industry_benchmark_ours.csv`),理解当前数据状态;
2. 决定第 7 节各项取舍(建议先定外部对比策略,影响 Intro 与 RW 写法);
3. 按 3 Method -> 4 Experiments -> 2 Related Work -> 1 Introduction -> 5/6 顺序起草
   (Method/实验最确定先写,Intro 最后写才能与全文对齐);
4. 每张表配一段"机制解读"而非数字复述(模板见第 4 节解读句);
5. 内审清单:数字全部可溯源到 CSV?声明边界违规?术语映射一致?每条贡献都有对应证据表?
6. 定稿前用 pre-submission review 流程过一遍宏观逻辑与语言。
