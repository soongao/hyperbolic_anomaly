# New Idea Packaging Canvas

Fill this before drafting Abstract or Introduction.

## 1. Raw Technical Move

```text
We [add/use/replace/optimize] [technical component].
```

## 2. Naive Story

Write the version that would sound incremental:

```text
We just [plain implementation].
```

## 3. Prior Assumption

```text
Existing methods assume [variable/evidence/constraint/geometry/data] is [available/reliable/sufficient/balanced/flat].
```

## 4. Why The Assumption Fails In ZSAD

```text
In ZSAD, this assumption fails because [target categories unseen / no target training data / anomaly evidence local / defects sparse / domain shifts / category semantics noisy].
```

## 5. Reframed Problem

```text
The core problem is not [naive problem], but [conceptual mismatch].
```

## 6. Packaging Options

Option A:

```text
[variable]-agnostic [mechanism]
```

Option B:

```text
[concept]-aware [model/space]
```

Option C:

```text
[evidence]-deviation [anchoring/scoring]
```

Option D:

```text
[constraint]-relaxed [matching/alignment]
```

## 7. Recommended Story

```text
Because [prior assumption] fails under [ZSAD condition], we [method action]. This creates [new representation/objective] that [reviewer-valued capability].
```

## 8. Method Name Candidates

- `[name 1]`
- `[name 2]`
- `[name 3]`

Each name should encode at least one of:

- removed nuisance variable,
- missing concept,
- new evidence space,
- relaxed constraint,
- geometry change,
- adaptation timing.

## 9. Experiments Needed To Make The Packaging True

- Compare against the raw baseline.
- Ablate the named component.
- Test the assumption failure.
- Test transfer across the variable mentioned in the name.
- Show qualitative evidence if the story is representational.

## 10. Risk Boundary

```text
We can claim [bounded claim].
We cannot claim [stronger unsupported claim].
```

