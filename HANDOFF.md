# R-HNA Research Handoff: From Zero to One

> 接手人只需本文件 + `results/` 下的权威 CSV,即可从零完成论文写作。
> 当前已有:`results/zero_shot_industry_benchmark_ours.csv`;其余消融表与主表待补跑(见第 4 节)。
> 规则一:论文中任何数字只能来自这些 CSV;CSV 里空缺的数值标记为 TODO 并安排补实验,**严禁编造或沿用旧稿数字**。
> 规则二:仓库历史与本文件冲突时,以本文件为准。

---

## 1. Idea:一句话与问题重构

**核心论点**:在 CLIP 零样本异常检测中,当前方法用单个文本 anchor 代表正常性(正常性是点状的),但真实的正常 patch 在特征空间中分布在一个区域上,单点 anchor 无法捕获这个分布。

```
旧假设:normality is a point (one text anchor represents all normal patches)
新假设:normality is a region (normal patches form a distribution that needs structured geometric modeling)
```

为什么重构成立:CLIP 的文本编码器把"a photo of a good X"编码为特征空间中的一个点,但真实的正常 patch 有无数种变体(光照、角度、纹理的细微差异),它们在特征空间中分布在一个区域上。用一个点去代表一个区域,必然有信息损失,导致 patch 级打分不稳定。

## 2. 组件分解(A+B+C+D)

| 组件 | 内容 | 来源 | 角色 | 验证表 |
| --- | --- | --- | --- | --- |
| A | AnomalyCLIP 式可学习正常提示词(冻结 CLIP 视觉塔提 patch 特征) | 现成借用,未改动 | 定义正常性参考锚点 T={t_j},作为区域的"骨架" | TODO:anchor_controls |
| B | 双曲锥接受区域:Exp_0 映射后以 V(z_i, Cone(u_j)) 为代价 | 已有几何工具的新用法 | 把点 anchor 扩展为结构化区域,锥的各向异性捕获正常分布的方向特性 | TODO:cost_type |
| C | UOT 鲁棒匹配:熵正则非平衡 OT,KL 松弛允许质量不被传输 | 已有优化工具的新用法 | 鲁棒匹配——异常 patch 不被强制匹配到正常区域,避免污染正常模型;未传输质量是鲁棒匹配的副产品 | TODO:transport_mode |
| D | 双信号读出:score_i = α·unaccepted_i/(a_i+eps) + β·Norm(conditional_cost_i) | 本文新增设计(轻量) | 两路证据融合:unaccepted mass 反映"有多不正常",acceptance cost 反映"哪些方面偏离正常" | TODO:signal_decomposition |

四张消融表按 A→B→C→D 依赖链环环相扣(详见第 3 节机制链)。

## 3. 机制链与声明边界

```
learned normal prompt (点 anchor)
  -> hyperbolic cone (点 → 区域,各向异性几何)
    -> UOT robust matching (鲁棒匹配,异常 patch 不被强制对齐)
      -> unaccepted mass (不匹配程度,反映异常严重性)
      + conditional acceptance cost (匹配代价,反映异常性质)
        -> anomaly map
```

**可以声称**:
- CLIP ZSAD 的瓶颈在于单点 anchor 无法捕获正常 patch 的分布多样性;
- 双曲锥把点 anchor 扩展为结构化区域,锥的各向异性捕获正常分布的方向特性;
- UOT 提供鲁棒匹配,避免异常 patch 扭曲正常区域边界;
- 两路信号互补:unaccepted mass 主导异常严重性判断,acceptance cost 主导异常性质区分(消融待补)。

**禁止声称**:
- 首次把 OT / 双曲几何 / CLIP 用于异常检测;
- 双曲空间普遍优越;
- 提出了新的 prompt 学习方法;
- "拒绝"是核心创新(unaccepted mass 是鲁棒匹配的副产品,不是设计目标)。

## 4. 证据地图(研究问题 -> 数据文件)

> **当前状态**:仅有 `zero_shot_industry_benchmark_ours.csv`,消融表与主表均待补跑。以下保留问题框架与解读句模板,数字待填入。

| 问题 | 文件 | 关键数字 | 解读句 |
| --- | --- | --- | --- |
| Q1 区域建模有效吗 | TODO:main_table | TODO | 与单点 anchor 方法(AnomalyCLIP)对比,验证区域建模是否带来增益 |
| Q2 UOT 鲁棒匹配必要吗 | TODO:transport_mode | TODO | balanced OT 强制全匹配,异常 patch 扭曲正常边界;UOT 允许不匹配,正常模型更干净 |
| Q3 锥的各向异性有贡献吗 | TODO:cost_type | TODO | 各向同性(球)vs 各向异性(锥)对比,验证锥的方向特性是否捕获正常分布的真实结构 |
| Q4 双信号互补吗 | TODO:signal_decomposition | TODO | 单信号 vs 双信号对比,验证两路证据是否提供不同维度的异常信息 |
| Q5 锚点选对了吗 | TODO:anchor_controls | TODO | 方法依赖正确的学习正常参考:anomaly 锚 FPR 远高于 normal 锚;任意锚点不 work |

**CSV 空单元格约定**:消融表补跑后,若存在未记录的指标单元格,写作时二选一:(a) 补跑实验填上;(b) 消融表只呈现已记录指标。不得留白进论文。

## 5. 术语映射(代码名 <-> 论文名)

| 代码 CLI | 论文措辞 |
| --- | --- |
| `--ot_score unmatched` | unaccepted mass (不匹配质量,反映异常严重性) |
| `--ot_score cost` | conditional acceptance cost (匹配代价,反映异常性质) |
| `--ot_cost hyperbolic_cone` | hyperbolic normality acceptance cone (双曲正常性接受锥) |
| `--ot_mode unbalanced` | robust matching via UOT (基于非平衡 OT 的鲁棒匹配) |

正文一律用论文措辞;方法节首次出现时给公式定义,避免口语化直直译。

## 6. 论文规划

**类型**:Reframing 型技术论文(Technique)。成败在 Introduction 能否让审稿人接受第 1 节的前提。

**标题候选**:
- Hyperbolic Normality Regions for CLIP-based Zero-shot Anomaly Detection(工作标题)
- 备选强调区域:From Points to Regions: Structured Normality Modeling for Zero-shot Anomaly Localization

**Introduction 六段逻辑链**:
1. 背景:CLIP ZSAD 兴起,prompt 打分是主流范式(运行例子:MVTec 划痕);
2. 认知裂缝:单点 anchor 代表正常性——一个文本 anchor 是一个点,但真实正常 patch 分布在一个区域上,点无法代表区域;
3. 问题重构:正常性不是点状的,而是区域性的;我们需要建模正常 patch 的分布区域;
4. 挑战:如何定义区域的几何形状(锥的各向异性)、如何鲁棒匹配不污染正常模型(UOT)、两路证据如何融合;
5. 方案概览:双曲锥定义区域 + UOT 鲁棒匹配 + 双信号融合;
6. 负献三条:区域建模 insight;双曲锥实例化;UOT 鲁棒匹配 + 双信号分解。

**章节骨架**:
1 Introduction -> 2 Related Work(CLIP-ZSAD / OT 与异常检测 / 双曲表征,三小节各自"借了什么、留下什么缺口")->
3 Method(3.1 区域建模形式化,3.2 双曲锥,3.3 UOT 鲁棒匹配,3.4 双信号)-> 4 Experiments
(4.1 设置,4.2 主表=Q1,4.3-4.6 四张消融=Q2-Q5,4.7 机制可视化)->
5 Discussion(边界与失败案例)> 6 Conclusion。

**图规划**:
Fig1 动机(点 anchor vs 区域 anchor 的对比,直观展示信息损失);
Fig2 方法总览(对应组件 A/B/C/D 四块);Fig3 机制可视化(acceptance cost / unaccepted mass / final score 三联图);
Fig4 unaccepted mass 在正常/异常像素上的分布;
Fig5 复杂正常结构上的失败案例。

## 7. 写作期必须处理的缺口(诚实清单)

| 缺口 | 处理建议 |
| --- | --- |
| 无外部 SOTA 对比(如 APRIL-GAN、AdaCLIP、VCP-CLIP 等) | 最优解:补一张外部对比表;次优:Related Work 正面对话 + 说明协议差异,并在 Discussion 承认范围 |
| severity sweep 曾列入计划但无数据 | 要么补跑(合成缺陷 0.25/0.5/0.75/1.0 四档),要么从叙事中整体删除,不留残迹 |
| 全部单次运行、无方差 | 补跑后实验设置明确写出协议;若可能补 3 seeds |
| 消融表全部缺失 | 补跑四张消融表(transport_mode/cost_type/signal_decomposition/anchor_controls) |

## 8. 从零到一执行清单

1. 通读本文件与已有 CSV(`zero_shot_industry_benchmark_ours.csv`),理解当前数据状态;
2. 决定第 7 节各项取舍(建议先定外部对比策略,影响 Intro 与 RW 写法);
3. 按 3 Method -> 4 Experiments -> 2 Related Work -> 1 Introduction -> 5/6 顺序起草
   (Method/实验最确定先写,Intro 最后写才能与全文对齐);
4. 每张表配一段"机制解读"而非数字复述(模板见第 4 节解读句);
5. 内审清单:数字全部可溯源到 CSV?声明边界违规?术语映射一致?每条贡献都有对应证据表?
6. 定稿前用 pre-submission review 流程过一遍宏观逻辑与语言。
