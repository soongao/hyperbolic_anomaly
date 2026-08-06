---
name: zsad-idea-sop
description: Evaluate, refine, package, and experiment-plan rough ZSAD research ideas. Use when a user proposes a naive method such as "add module A+B", adapters, prompts, visual-context prompting, wavelet/frequency features, TTA, OT/UOT, hyperbolic space, SAM/LVLM components, or any rough zero-shot/few-shot anomaly detection improvement and wants to know whether it is reasonable, novel, already done, how to improve and frame it, and what experiments and success thresholds are needed.
---

# ZSAD Idea SOP

## Overview

Use this skill to turn a rough ZSAD idea into an evidence-grounded research plan. The workflow is: clarify the raw move, check feasibility, search for prior overlap, judge novelty, improve the idea, package it into a reviewer-facing story, design experiments, and define success thresholds.

Do not start by naming or polishing the idea. Start by exposing the raw technical move and checking whether the idea is already covered by nearby work.

## Writing Stance

Keep a strict separation between internal audit and paper-facing narration.

- During triage, be honest about feasibility, overlap, protocol leakage, and the experiments needed to support the idea.
- When the user explicitly marks a mechanism as core, such as "there must be hyperbolic space" or "this paper is about UOT + hyperbolic ZSAD", treat that mechanism as the intended design premise in the paper story.
- Do not write the abstract, introduction, contribution bullets, conclusion, or recommended framing as if the user-designated core mechanism is still waiting to earn its existence. Experiments validate, quantify, and isolate the contribution; they do not decide whether the core should be demoted.
- Use ablations as controls that support the central claim. For example, cosine/Euclidean costs are flat-geometry controls for a hyperbolic method, not equally plausible alternatives that may replace the hyperbolic contribution in the story.
- Put risk boundaries in protocol, ablation design, limitations, or internal notes. Do not turn them into retreat clauses such as "if this fails, weaken the claim" inside the main narrative.

## Knowledge Roots

Default local knowledge root:

```text
/Users/bytedance/code/anomalyclip_new/knowledge
```

When running shell searches, set:

```bash
KNOWLEDGE_ROOT=/Users/bytedance/code/anomalyclip_new/knowledge
```

Use these libraries in order:

1. `cards/`, `text/`, `metadata/papers.jsonl`: prior-work facts and overlap checks.
2. `idea_packaging_library/`: raw move -> paper framing -> contribution packaging.
3. `experiment_library/`: required experiments, tables, figures, protocols, and success thresholds.
4. `writing_library/`: final wording, contribution language, claim boundaries, and section templates.

If the knowledge root is unavailable, ask the user for the project path before proceeding.

## Core Workflow

### 1. Normalize The Raw Idea

Rewrite the user's proposal as:

```text
Raw move: use/add/replace [module A] + [module B] to change [model component/objective/protocol].
Naive story: "we just add/use [A+B]."
Intended claim: improve [image-level detection / pixel localization / transfer / robustness / efficiency].
Protocol: zero-shot / auxiliary-data ZSAD / few-shot normal-only / test-time adaptation / other.
```

Load `references/idea_triage.md` for detailed scoring.

### 2. Check Prior Overlap

Search the local knowledge before judging novelty.

Recommended commands:

```bash
rg -n "keyword1|keyword2|module name|method family" "$KNOWLEDGE_ROOT"/cards "$KNOWLEDGE_ROOT"/metadata "$KNOWLEDGE_ROOT"/idea_packaging_library
rg -n "keyword1|keyword2|module name|method family" "$KNOWLEDGE_ROOT"/text
```

Use `references/retrieval_map.md` to choose search terms and nearest papers.

### 3. Judge Reasonableness And Novelty

Classify the idea:

- `reject`: violates protocol, requires unavailable labels, or is already identical to prior work.
- `weak`: technically plausible but only module stacking or renaming.
- `salvageable`: prior modules exist, but a real ZSAD mismatch can be built.
- `promising`: has a clear mismatch, mechanism, and testable claim.

Always state what is not novel before proposing a better framing.

### 4. Improve And Package The Idea

Use `references/packaging_workflow.md` and `$KNOWLEDGE_ROOT/idea_packaging_library/` to produce:

- the corrected problem construction;
- 2-3 possible framings;
- one recommended framing;
- method/module name candidates;
- risk boundaries and forbidden claims.

### 5. Design Experiments And Success Thresholds

Use `references/experiment_planning.md` and `$KNOWLEDGE_ROOT/experiment_library/` to produce:

- must-have main tables;
- required ablations;
- qualitative figures;
- optional appendix experiments;
- experiments to skip;
- success thresholds as relative criteria, not fabricated SOTA numbers.

### 6. Return A Decision-Oriented Answer

Use `references/output_schema.md` for the final structure. Keep the answer concrete enough that the user can decide whether to implement the idea.

## Output Principles

- Separate `raw technical move`, `novelty`, `packaging`, and `experiments`.
- Prefer "this is already close to X" over vague praise.
- Give a salvage path when an idea is weak.
- Do not invent numerical results. Define success as deltas over relevant baselines and ablation drops.
- Treat protocol leakage as a hard failure.
- If evidence is insufficient, say exactly which papers or text files need to be checked next.

## Reference Files

- `references/idea_triage.md`: feasibility, prior-overlap, and novelty grading.
- `references/retrieval_map.md`: which local knowledge files to consult by idea family.
- `references/packaging_workflow.md`: how to turn raw modules into a paper story.
- `references/experiment_planning.md`: required experiments and success thresholds.
- `references/output_schema.md`: response template.
