# Usage

## Workflow: Plan Experiments For A New ZSAD Paper

1. Write the method claim in one sentence.
2. Classify the method family: prompt, adapter, visual-context, few-shot, language-free, frequency, TTA, SAM/LVLM, hyperbolic, or hybrid.
3. Open the closest 2-4 cases in `cases/`.
4. Copy the must-have experiments from `patterns/required_experiments.md`.
5. Add family-specific ablations from the nearest cases.
6. Remove low-value experiments using `patterns/optional_and_avoid.md`.
7. Fill `templates/new_zsad_experiment_plan.md`.

## Query Recipes

Find paper cases by method family:

```bash
rg -n "prompt|adapter|visual context|frequency|few-shot|language-free|SAM|hyperbolic" knowledge/experiment_library/cases
```

Find must-have experiments:

```bash
rg -n "Must|Required|P0|P1|Avoid" knowledge/experiment_library/patterns
```

Find table/figure patterns:

```bash
rg -n "Table|Figure|Qualitative|Ablation|Sensitivity|Failure" knowledge/experiment_library
```

Use the registry:

```bash
rg -n "\"must_do\"|\"tables\"|\"figures\"|\"avoid\"" knowledge/experiment_library/metadata/experiments.jsonl
```

## Agent Prompt

```text
Use knowledge/experiment_library to design experiments for this ZSAD idea:
[method idea]

Return:
1. claims to validate,
2. must-have main tables,
3. required ablations,
4. recommended qualitative figures,
5. optional appendix experiments,
6. experiments to skip,
7. metric/protocol risks,
8. a table/figure checklist.
```
