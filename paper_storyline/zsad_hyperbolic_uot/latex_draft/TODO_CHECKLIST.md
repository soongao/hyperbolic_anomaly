# R-HNA Manuscript Checklist

## Before Submission

- [ ] Replace every `\needcite{...}` with verified citations.
- [ ] Populate `references.bib` with verified BibTeX entries.
- [x] Fill Table 1: main benchmark.
- [x] Fill Table 2: rejectable acceptance ablation.
- [x] Fill Table 3: acceptance-region cost ablation.
- [x] Fill Table 4: anomaly evidence decomposition.
- [x] Fill Table 5: learned normal prompt anchor controls.
- [ ] Insert Figure 1: flat prompt scoring vs balanced acceptance vs rejectable acceptance.
- [ ] Insert Figure 2: learned normal prompt, hyperbolic cone, UOT, evidence decomposition.
- [ ] Insert mechanism visualization: accepted mass, unaccepted mass, conditional acceptance cost, final score.
- [ ] Insert failure-mode visualization on complex normal structures.
- [ ] Add runtime and memory measurements relative to direct prompt scoring.

## Claim Rules

- The outer story is rejectable hyperbolic normality acceptance.
- UOT is the rejectable acceptance mechanism, not the paper identity.
- Hyperbolic cones define the structured acceptance region around learned normal prompts.
- Unaccepted mass and conditional acceptance cost are complementary anomaly evidence.
- The contribution is bounded to CLIP ZSAD normality acceptance, not universal superiority of hyperbolic geometry.

## Main Claim

```text
We formulate CLIP-based zero-shot anomaly localization as rejectable normality
acceptance, where anomalous regions are identified as patch evidence that
learned normality rejects or accepts only at high conditional cost.
```
