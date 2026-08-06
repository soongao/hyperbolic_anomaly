# Query Cookbook

Use these commands from the repository root.

## Baselines And Protocols

```bash
rg -n "MVTec|VisA|MPDD|BTAD|DAGM|Real-IAD" knowledge/text
rg -n "zero-shot|few-shot|one-shot|training-free|train once" knowledge/text
rg -n "image-level|pixel-level|AUROC|AUPRO|PRO|AP" knowledge/text
```

## Mechanism Evidence

```bash
rg -n "prompt|normal prompt|abnormal prompt|state word|template" knowledge/text
rg -n "patch|window|local feature|dense feature|segmentation map" knowledge/text
rg -n "ablation|sensitivity|limitation|failure|false positive" knowledge/text
```

## Candidate Improvement Directions

```bash
rg -n "hyperbolic|Poincare|entailment|cone|hierarchy" knowledge/text
rg -n "optimal transport|unbalanced|Sinkhorn|partial|mass" knowledge/text
rg -n "test-time|entropy|minimization|adaptation|augmentation" knowledge/text
rg -n "frequency|Fourier|wavelet|scattering|high-frequency|low-frequency" knowledge/text
```

## Agent Metadata Queries

```bash
python3 - <<'PY'
import json
for line in open('knowledge/metadata/papers.jsonl'):
    p = json.loads(line)
    if p['priority'] == 'core':
        print(p['id'], '|', p['title'])
PY
```
