# Output Schema

Use this structure for the final answer unless the user asks for a different format.

## Short Form

```text
结论：

原始做法：
已有工作相似度：
合理性：
新颖性：
建议包装：
必须做的实验：
成功标准：
主要风险：
```

## Full Form

```text
结论：
[reject / weak / salvageable / promising]，一句话说明原因。

1. 朴素做法还原
- Raw move:
- Naive story:
- Target protocol:
- Intended claim:

2. 合理性判断
- What works:
- What breaks:
- Protocol risks:

3. 已有工作与新颖性
- Closest papers:
- What is already done:
- What may still be new:
- Novelty grade: N0/N1/N2/N3

4. 优化后的 idea
- Design principle:
- Modules:
- Why A and B are complementary:
- What to remove or simplify:

5. 推荐包装
- Packaging-depth check:
- Framing:
- Method name candidates:
- Contribution bullets:
- Claims to avoid:

6. 实验计划
- Main tables:
- Ablations:
- Figures:
- Mermaid mechanism drafts:
- Reference-only result file:
- Optional:
- Skip:

7. 成功标准
- Minimal success:
- Solid success:
- Strong success:
- Failure signals:

8. 下一步
- First experiment to run:
- First prior-work text to verify:
```

## Tone Rules

- Be direct about weak novelty.
- Give a salvage path if possible.
- Avoid long generic background.
- Use paper names and file paths when evidence comes from local knowledge.
- Say "需要查证" when the current evidence is insufficient.
- If the user has explicitly committed to a core mechanism, do not make the answer sound as if that mechanism is optional or awaiting permission to be the contribution. State the committed framing, then describe ablations as evidence used to validate and quantify it.
- Keep defensive risk language out of proposed abstract/introduction/contribution wording. Put risks under `主要风险`, `实验计划`, or `局限性`.
- When concrete result numbers are useful, they may be used in manuscript tables, figure callouts, and result prose for a complete draft. Also create a separate reference `.txt` file stating that the numbers are planning/reference values, not measured results. Do not put that disclaimer inside the manuscript body unless asked.
- Always include table and figure planning for paper drafts. For mechanism or architecture figures, create Mermaid `.mmd` drafts before final artwork.
- Do not accept a module-stack package if a deeper assumption-failure package is available. If the answer says the current story is shallow, immediately provide or implement the deeper rewrite.
- For draft-revision tasks, explicitly remove old-story residue from title, macro/method name, abstract, introduction, contribution bullets, method subsection names, table row names, figure captions, Mermaid labels, conclusion, and reference-result sidecars.
