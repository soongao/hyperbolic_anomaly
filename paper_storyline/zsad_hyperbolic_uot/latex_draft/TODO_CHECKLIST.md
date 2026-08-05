# Fill-in Checklist

## Must Fill Before Submission

- [ ] Replace every `\needcite{...}` with verified citations.
- [ ] Populate `references.bib` with real BibTeX entries only after verification.
- [ ] Fill Table 1: main benchmark.
- [ ] Fill Table 2: transport mode ablation.
- [ ] Fill Table 3: cost type ablation.
- [ ] Fill Table 4: anomaly signal decomposition.
- [ ] Fill Table 5: anchor negative controls.
- [ ] Fill Table 6: runtime and sensitivity.
- [ ] Insert Figure 1: motivation from flat scoring to UOT rejection.
- [ ] Insert Figure 2: method pipeline.
- [ ] Insert mechanism visualization: transport mass, unmatched mass, matched cost, final score.
- [ ] Insert failure-mode visualization on complex normal structures.
- [ ] Remove or rewrite every `\resulttodo{...}` marker.
- [ ] Decide final claim strength based on the ablation outcomes.

## Claim Rules

- If UOT does not beat balanced/partial OT, weaken the mass-relaxation claim.
- If UOT with cosine cost matches hyperbolic UOT, demote hyperbolic geometry to an optional cost variant.
- If random or shuffled anchors match normality anchors, remove the semantic-normality explanation.
- If unmatched mass does not align with anomaly masks, do not claim a rejection mechanism.
- If improvements only occur on weak/failure-prone classes, write the contribution as failure-mode repair rather than general superiority.

## Safe Main Claim

`We formulate CLIP-based zero-shot anomaly localization as rejectable patch-to-normality semantic transport, where anomalous regions are identified by high-cost or unmatched transport to normality anchors.`
