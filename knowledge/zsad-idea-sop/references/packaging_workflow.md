# Packaging Workflow

Use this reference after the prior-overlap and novelty check.

## Packaging Rule

A good package is not a better name for a module. It is a causal story:

```text
prior assumption -> why it fails in ZSAD -> design principle -> technical mechanism -> measurable effect
```

## Exemplar-Level Packaging Test

Before writing a draft, compare the proposed story against the user's three canonical packaging examples:

| Example | Raw move | Deep package |
|---|---|---|
| AnomalyCLIP | learn normal/abnormal prompts | object-agnostic abnormality because object identity is a nuisance variable |
| VCP-CLIP | CoCoOp-like conditioning | visual context prompting because category/context is unavailable as reliable text |
| AA-CLIP | two lightweight adapters | concept-first anomaly awareness because CLIP must learn the anomaly concept before visual alignment |

The new idea must reach the same abstraction level:

```text
Raw move -> naive story -> failed prior assumption -> task-level problem reconstruction -> mechanism becomes necessary -> concept-level method name.
```

Reject shallow packages such as:

- "we combine A and B";
- "we replace Euclidean distance with hyperbolic distance";
- "we add UOT for better matching";
- "we add an adapter/prompt/module and improve performance".

Accept only packages where the raw move becomes the natural solution to a ZSAD-specific mismatch.
If a deeper story is identified after a draft exists, rewrite the title, abstract, introduction, contributions, method overview, and figures to follow that deeper story.

This is a hard gate, not a style preference. A draft fails the gate if the reader can summarize the contribution as "use module A plus module B" after reading the title, abstract, and first page.

When the raw move is `hyperbolic + UOT` for CLIP-ZSAD, do not leave the paper at `hyperbolic semantic transport` unless the task reconstruction truly makes transport the deepest concept. The stronger default reconstruction is:

```text
Failed prior assumption: patch-wise normal/abnormal prompt comparison assumes anomalies are stable semantic alternatives to normality.
Task-level reconstruction: anomaly localization should ask whether local evidence can be accepted by normality.
Mechanism necessity: hyperbolic geometry gives normality a structured acceptance space; UOT makes acceptance rejectable by exposing unaccepted mass and high-cost accepted evidence.
Packaged concept: hyperbolic normality acceptance.
```

Under this package, transport is the implementation of rejectable acceptance, not the paper's outer identity.

## Narrative Commitment Rule

If the user has explicitly chosen a mechanism as the paper's core, write the paper-facing story from that commitment.

Good paper-facing stance:

```text
Hyperbolic normality geometry is the core design that structures patch-to-anchor acceptance; UOT realizes rejectable acceptance; flat costs and balanced transport are ablation controls used to isolate these contributions.
```

Bad paper-facing stance:

```text
The transport cost can be flat or hyperbolic; whether hyperbolic becomes the core contribution depends on controlled ablation.
```

The bad version is acceptable only as an internal planning note before the user has committed to the mechanism. Once the user has committed, the job is to make the strongest coherent version of that mechanism and design experiments that verify it. Do not ask the reader to decide whether the paper's own core idea should exist.

## Draft Rewrite Rule

When revising an existing paper, rewrite in this order:

1. Replace the method name and title with the concept-level package.
2. Rewrite the abstract around the failed assumption and task reconstruction.
3. Rewrite the introduction so the mechanism follows from the reconstructed task.
4. Rewrite contributions so each one maps to problem reformulation, core geometry, and rejectable evidence.
5. Rename method subsections and figure captions so modules serve the concept rather than define it.
6. Update result prose, table row names, sidecar result notes, and Mermaid diagrams to remove old-story residue.

Do not leave a hybrid draft where the abstract claims a deep package but figures, tables, or conclusion still use the old module-stack story.

## Common Packaging Moves

Read `$KNOWLEDGE_ROOT/idea_packaging_library/patterns/packaging_primitives.md` for details. Use this quick map:

- Remove nuisance variable -> object/category/domain-agnostic evidence.
- Infer unavailable variable -> visual context prompting/adaptation.
- Fine-tuning -> concept acquisition then representation alignment.
- Combine two modules -> split a real tradeoff into complementary roles.
- Add frequency/wavelet -> structured multiscale evidence, not "high-frequency defects".
- Relax matching constraint -> partial/unbalanced evidence matching.
- Use hyperbolic geometry -> hierarchy/scale/asymmetry, not arbitrary metric replacement.
- TTA -> adaptation under zero-label deployment constraints.

## Candidate Framing Generation

Generate 2-3 framings:

```text
Framing A: [problem construction] -> [mechanism name]
Framing B: [different assumption failure] -> [mechanism name]
Framing C: [more conservative story] -> [mechanism name]
```

Then recommend one and explain why it has the best evidence path.

When recommending a framing, avoid defensive alternatives like "if the core mechanism underperforms, demote it." Instead, state the committed framing and list ablations as evidence routes:

```text
Recommended framing: [core mechanism] addresses [assumption failure].
Evidence route: compare against [control A/B] to quantify the contribution of [core mechanism].
```

The recommended framing should be phrased at the concept level. For example, if the raw move is `hyperbolic cost + UOT`, the package should not be `hyperbolic semantic transport` unless transport is truly the paper's deepest concept. A stronger package may be `normality acceptance`, where hyperbolic geometry defines the acceptance structure and UOT implements rejectable evidence.

## Naming Rules

Good names encode:

- the failed assumption;
- the mechanism;
- the target evidence.

Examples:

- `object-agnostic prompt learning`
- `visual context prompting`
- `anomaly-aware CLIP`
- `frequency-deviation anchoring`
- `multiscale stable evidence`
- `partial anomaly transport`
- `test-instance prompt adaptation`
- `hierarchy-aware anomaly representation`

Avoid:

- `A+B network`
- `enhanced CLIP`
- `novel adapter`
- `frequency-aware module` without defining the frequency claim
- `universal` unless cross-domain evidence is planned

## Claim Boundaries

Use `$KNOWLEDGE_ROOT/idea_packaging_library/patterns/risk_boundaries.md` and `$KNOWLEDGE_ROOT/writing_library/patterns/claim_boundaries.md`.

Common boundaries:

- Do not claim "knows the category" unless category recovery is measured.
- Do not claim "anomaly-aware" unless representation separation or staged alignment is shown.
- Do not claim "language-free generality" if text prompts or object names are still used.
- Do not claim "all anomalies are high-frequency"; say scale-frequency deviations instead.
- Do not claim "hyperbolic is better" without hierarchy/curvature evidence. If hyperbolic geometry is the user-designated core, phrase this as an evidence requirement for the claim, not as doubt about whether hyperbolic belongs in the method.
- Do not claim "zero-shot" if target labels/masks are used.

## Packaging Output

Return:

1. raw move and naive story;
2. why naive story is weak;
3. prior-overlap warning;
4. recommended framing;
5. method/module name candidates;
6. contribution bullets;
7. risk boundaries.
