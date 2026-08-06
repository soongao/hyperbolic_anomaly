# Usage

## Workflow: Package A New ZSAD Idea

1. Write the raw technical move in one plain sentence.
2. Write the embarrassing naive story: "we just add/use/replace [X]".
3. Identify the hidden assumption in prior work.
4. Turn that assumption into a problem statement.
5. Choose one packaging primitive from `patterns/packaging_primitives.md`.
6. Choose a naming strategy from `patterns/naming_strategies.md`.
7. Draft the reviewer-facing contribution using `templates/new_idea_packaging_canvas.md`.
8. Run the risk checks in `patterns/risk_boundaries.md`.

## Query Recipes

Find cases by raw move:

```bash
rg -n "Raw Technical Move|adapter|prompt|frequency|wavelet|transport|hyperbolic" knowledge/idea_packaging_library/cases
```

Find packaging patterns:

```bash
rg -n "Primitive|Transfer Pattern|When To Use|Risk Boundary" knowledge/idea_packaging_library/patterns
```

Use the machine-readable registry:

```bash
rg -n "\"raw_move\"|\"packaging\"|\"transfer_pattern\"" knowledge/idea_packaging_library/metadata/cases.jsonl
```

## Agent Prompt

```text
Use knowledge/idea_packaging_library to package this idea:
[raw idea]

Return:
1. raw technical move,
2. naive story,
3. constructed problem,
4. 2-3 possible packaging framings,
5. recommended framing,
6. method/contribution names,
7. risk boundaries,
8. a 6-paragraph introduction outline.
```

## Evaluation Questions

- Does the packaging expose a real mismatch, or only rename an implementation detail?
- Can the reviewer understand why the method is necessary before seeing the module?
- Does the name encode the problem and mechanism?
- Is the claim supported by experiments the user can actually run?
- Is there a simpler competing story that makes the contribution look incremental?
