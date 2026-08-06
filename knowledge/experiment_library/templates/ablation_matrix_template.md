# Ablation Matrix Template

## Core Component Ablation

```latex
\begin{table}[t]
\caption{Ablation of the proposed components. Deltas are computed relative to the full model.}
\label{tab:ablation}
\centering
\begin{tabular}{lcccc}
\toprule
Variant & I-AUROC $\uparrow$ & I-AP $\uparrow$ & P-AUROC $\uparrow$ & P-AUPRO $\uparrow$ \\
\midrule
Full method & & & & \\
w/o component A & & & & \\
w/o component B & & & & \\
w/o component C & & & & \\
Replace A with simple baseline & & & & \\
\bottomrule
\end{tabular}
\end{table}
```

## What To Include

- One row per named contribution.
- One simple replacement for the most important module.
- Deltas in parentheses if the table is not too crowded.
- MVTec AD and VisA in the same table only if columns remain readable.

## What Not To Include

- Random implementation details that are not paper claims.
- More than 8-10 ablation rows in the main paper.
- Hyperparameter sweeps that belong in appendix.
