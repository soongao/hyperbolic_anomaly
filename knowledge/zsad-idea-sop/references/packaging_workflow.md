# Packaging Workflow

Use this reference after the prior-overlap and novelty check.

## Packaging Rule

A good package is not a better name for a module. It is a causal story:

```text
prior assumption -> why it fails in ZSAD -> design principle -> technical mechanism -> measurable effect
```

## Narrative Commitment Rule

If the user has explicitly chosen a mechanism as the paper's core, write the paper-facing story from that commitment.

Good paper-facing stance:

```text
Hyperbolic normality geometry is the core design that structures patch-to-anchor acceptance; flat costs are ablation controls used to isolate its contribution.
```

Bad paper-facing stance:

```text
The transport cost can be flat or hyperbolic; whether hyperbolic becomes the core contribution depends on controlled ablation.
```

The bad version is acceptable only as an internal planning note before the user has committed to the mechanism. Once the user has committed, the job is to make the strongest coherent version of that mechanism and design experiments that verify it. Do not ask the reader to decide whether the paper's own core idea should exist.

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
