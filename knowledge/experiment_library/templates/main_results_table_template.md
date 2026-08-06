# Main Results Table Template

## Industrial ZSAD Table

```latex
\begin{table}[t]
\caption{Zero-shot anomaly detection and localization on industrial benchmarks. Image-level metrics are AUROC/AP; pixel-level metrics are AUROC/AP/AUPRO.}
\label{tab:main_industrial}
\centering
\begin{tabular}{lcccccc}
\toprule
\multirow{2}{*}{Method} &
\multicolumn{2}{c}{MVTec AD} &
\multicolumn{2}{c}{VisA} &
\multicolumn{2}{c}{Average} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
& I-AUROC $\uparrow$ & P-AUROC $\uparrow$
& I-AUROC $\uparrow$ & P-AUROC $\uparrow$
& I-AUROC $\uparrow$ & P-AUROC $\uparrow$ \\
\midrule
CLIP & & & & & & \\
WinCLIP & & & & & & \\
APRIL-GAN & & & & & & \\
AnomalyCLIP & & & & & & \\
Ours & & & & & & \\
\bottomrule
\end{tabular}
\end{table}
```

## Notes

- Add AP/F1/AUPRO columns if space allows; otherwise use a second table.
- Keep full class-wise tables in appendix.
- Use the same source-target protocol for all comparable methods.
