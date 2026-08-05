# Task Plan: Chinese Draft and Independent Idea Review

## Goal
Create a Chinese first draft for the hyperbolic UOT ZSAD idea and collect an independent read-only review from a separate Codex agent.

## Phases
- [x] Phase 1: Create `zh_draft/` workspace
- [x] Phase 2: Read writing guides and current storyline
- [x] Phase 3: Draft Chinese manuscript
- [x] Phase 4: Request independent Codex review
- [x] Phase 5: Save and summarize review feedback

## Key Questions
1. How can the Chinese draft state the idea without unsupported result claims?
2. Which claims must remain marked as hypotheses until experiments finish?
3. What risks should an independent reviewer pressure-test?

## Decisions Made
- The draft will use `[结果待填]` and `[引用待核验]` placeholders rather than inventing results or citations.
- The main framing is "可拒绝的 patch-to-normality 语义传输", not "双曲空间 + OT 的简单组合".

## Errors Encountered
- Initial multi-agent spawn attempts failed because the tool rejected simultaneous `message` and `items` fields. Retry after the draft file is complete with a minimal request.

## Review Summary
- Independent verdict: `promising but risky`.
- Highest-risk point: the method must prove both UOT necessity and hyperbolic-cost necessity; otherwise it looks like complex score stacking.
- Key negative control to keep: replace normality anchors with random, unrelated, or shuffled text anchors under the same UOT settings.
- Draft adjustment made after review: soften the claim that existing methods "force" every patch into a hard class, and emphasize missing explicit rejection instead.

## Status
**Complete** - Chinese draft created and independent review saved.
