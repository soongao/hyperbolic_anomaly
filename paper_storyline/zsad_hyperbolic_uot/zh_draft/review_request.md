# 子 Codex 审稿请求

请对以下 idea 和中文初稿做只读审稿式评估，不要修改任何文件。

## 工作目录

`/Users/bytedance/code/anomalyclip_new/AnomalyCLIP`

## 重点阅读文件

- `paper_storyline/zsad_hyperbolic_uot/README.md`
- `paper_storyline/zsad_hyperbolic_uot/experiment_design.md`
- `paper_storyline/zsad_hyperbolic_uot/writing_outline.md`
- `paper_storyline/zsad_hyperbolic_uot/zh_draft/draft_zh.md`

## 审稿目标

从顶会审稿人角度评估：

**CLIP-based ZSAD + hyperbolic cost + unbalanced optimal transport**

核心主张是：CLIP 零样本异常定位不应强制每个 patch 进入 normal/anomaly prompt 分类，而应建模为可拒绝的 patch-to-normality 语义传输；异常区域表现为高传输代价或未匹配质量。

## 请输出中文审核意见

1. 总体 verdict：`strong` / `promising but risky` / `weak`。
2. 5-8 条主要风险，按严重程度排序，并说明为什么会被审稿人攻击。
3. 这个 idea 最应该收窄或强化的核心 claim。
4. 必须补的实验和最关键的 negative control。
5. 一句建议的论文主张写法。

只返回评审意见，不写代码，不修改文件。
