# Experiment Planning

Use this reference after choosing a recommended framing.

## Main Rule

Experiments must validate claims, not modules.

```text
claim -> table/figure -> metric -> baseline -> success threshold
```

When a user-designated mechanism is the paper's core, express experiments as validation and isolation of that mechanism. Do not phrase the paper story as if the experiment will decide whether the mechanism belongs in the contribution. Controls such as flat costs, no-transport variants, random anchors, or balanced OT should be described as baselines/negative controls that quantify the committed mechanism's effect.

If the user asks for concrete expected numbers, or if a paper draft needs filled results, provide plausible reference numerical values. These values may be placed into the manuscript's result tables, figure descriptions, and result prose so the draft is structurally complete. Also create a separate `.txt` sidecar that labels the values as reference/planning numbers rather than measured results. Do not put that disclaimer in the manuscript body unless the user asks for it.

Read:

- `$KNOWLEDGE_ROOT/experiment_library/patterns/required_experiments.md`
- `$KNOWLEDGE_ROOT/experiment_library/patterns/claim_to_experiment_map.md`
- `$KNOWLEDGE_ROOT/experiment_library/patterns/metrics_and_protocols.md`
- nearest cases in `$KNOWLEDGE_ROOT/experiment_library/cases/`

## Default ZSAD Experiment Package

P0:

- Main industrial comparison on MVTec AD and VisA.
- Image-level metrics if classification is claimed: I-AUROC plus I-AP/AUPR or I-F1-max.
- Pixel-level metrics if localization is claimed: P-AUROC plus P-AP/P-F1-max and P-AUPRO/PRO.
- Baselines: CLIP-style baseline, WinCLIP, APRIL-GAN, AnomalyCLIP/AdaCLIP/FiLo/VCP-CLIP as appropriate.
- Core module ablation.
- Qualitative anomaly maps.
- Mechanism/architecture figure.
- Mermaid `.mmd` draft for mechanism figures before final drawing.
- Clear source-target protocol.

P1:

- Cross-dataset generalization if claiming category/domain transfer.
- Prompt robustness if text prompts are central.
- Shot curve if few-shot normal references are used.
- Representation visualization if claiming disentanglement/alignment/frequency separation.
- Efficiency table if adding heavy modules or TTA.

P2:

- Medical benchmarks if cross-domain generalization is claimed.
- Full class-wise tables.
- Extended qualitative gallery.
- Failure cases.

## Family-Specific Required Ablations

- Prompt: manual vs learnable, object-aware vs object-agnostic, state words/templates, prompt length/depth.
- Visual context: fixed prompt vs visual-conditioned prompt, Pre/Post context modules, product-level AP.
- Adapter: frozen CLIP, adapter/no-adapter, one-stage vs two-stage, text/image adapter roles.
- Hybrid: neither/static-only/dynamic-only/both.
- Few-shot: 1/2/4-shot with mean/std, normal-memory baselines.
- Frequency/wavelet: spatial-only replacement, transform basis, spectral layout, band removal.
- TTA: no-adaptation, TTA without update, adapted parameter group, confidence selection, update steps, runtime.
- UOT/partial matching: balanced vs unbalanced matching, relaxation coefficient, unmatched evidence visualization.
- Hyperbolic: Euclidean vs hyperbolic, curvature sweep, hierarchy/embedding visualization.
- SAM/LVLM: vanilla assembly baseline, prompt/filter components, region-level metrics.

## Success Thresholds

Use relative success criteria for judging whether the idea is strong. If concrete reference values are requested, keep a sidecar note explaining their status, while allowing the manuscript draft to use them as filled result values.

### Minimal Success

- Main metrics improve over the closest fair baseline on at least MVTec AD and VisA.
- Core ablation drops when the proposed module is removed.
- Qualitative maps show at least one clear failure mode improved.

### Solid Success

- Improvements hold for both image-level and pixel-level metrics where claimed.
- Gains appear on at least two datasets, not only one favorable category.
- Ablation deltas match the story: the named core module has the largest or most targeted drop.
- No major metric regression such as better AUROC but much worse AP/F1.

### Strong Success

- Beats or matches recent ZSAD baselines under fair protocol across MVTec AD, VisA, and extra industrial datasets.
- Cross-dataset transfer works in both source-target directions when applicable.
- Representation/attention/frequency/hyperbolic visualizations support the mechanism.
- Efficiency overhead is acceptable or explicitly traded for accuracy.

### Failure Signals

- Only pixel-AUROC improves while AP/F1/PRO gets worse.
- Gains vanish when prompt words or source dataset change.
- The full method beats weak baselines but not the closest method-family baseline.
- Ablation removal has no effect.
- The method uses target labels/masks but claims zero-shot.

Use failure signals for internal go/no-go decisions, result diagnosis, and limitation planning. Do not copy failure-signal language into the abstract, introduction, contribution bullets, or conclusion as retreat clauses. In paper-facing text, state the intended mechanism confidently and let the reported ablations support it.

## Result Target Format

Report success targets like:

```text
For this idea to be credible, it should beat [nearest baseline] on MVTec AD and VisA by a consistent margin in [primary metrics], and removing [core module] should reduce [target metric] noticeably on both datasets. If the gain appears only on AUROC but not AP/F1/PRO, the claim should be weakened.
```

For paper-facing plans after the core mechanism is fixed, prefer:

```text
The experiments quantify [core mechanism] by comparing it with [controls] under identical protocol, and success is reflected by consistent improvements in [primary metrics] plus targeted drops when [core mechanism] is removed.
```

## Reference Result Sidecar

When generating plausible numerical values for a paper draft, create a separate file such as:

```text
reference_results.txt
```

The file must start with a warning:

```text
These numbers are reference/planning values used to make the current paper draft structurally complete. They are not measured experimental results. Future agents and humans should replace or verify them with real runs before submission.
```

Recommended contents:

- Assumed protocol and backbone.
- Main comparison target table for each dataset.
- Transport-mode ablation targets.
- Cost-type ablation targets.
- Anchor-control targets.
- Score-decomposition targets.
- Efficiency targets.
- What magnitude of improvement would count as minimal, solid, and strong success.

Keep the numbers internally consistent with the story: the user-designated core mechanism should have the largest targeted or most mechanism-specific gain, and controls should support the causal claim. The manuscript does not need to state that these values are reference-only; the sidecar file carries that information.

## Figure And Table Blueprint

Every paper-level idea should include figure/table planning, even before final results exist.

Must-have tables:

- Main comparison table across MVTec AD and VisA.
- Transport-mode ablation table.
- Cost-type or mechanism ablation table.
- Anchor/control table if prompts or anchors are central.
- Score-decomposition table if the method has multiple anomaly evidence terms.
- Efficiency table if the method adds OT, TTA, adapters, SAM/LVLM, or other nontrivial compute.

Must-have figures:

- Method overview figure.
- Mechanism figure showing why the core design produces anomaly evidence.
- Qualitative anomaly-map figure.
- Mechanism visualization, such as transport plans, unmatched mass maps, curvature/embedding visualization, frequency bands, prompt/context behavior, or adaptation trajectory depending on the idea.

For architecture or mechanism figures, create `.mmd` drafts first. The Mermaid should specify the logical blocks, signal flow, controls, and outputs; final visual styling can be done later.
