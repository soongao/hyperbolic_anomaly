# Metrics And Protocols

## Common ZSAD Tasks

### Image-Level Anomaly Detection

Goal: classify an image as normal or anomalous.

Common metrics:

- `I-AUROC`: standard ranking metric.
- `I-AP` or `I-AUPR`: more sensitive to imbalance.
- `I-F1-max`: best threshold F1, often used in challenge or practical reporting.

### Pixel-Level Anomaly Localization / Segmentation

Goal: produce anomaly maps or masks.

Common metrics:

- `P-AUROC` or `pAUROC`: pixel ranking.
- `P-AP` or pixel AUPR: precision under imbalance.
- `P-F1-max`: best threshold segmentation F1.
- `P-PRO` or `AUPRO`: region-level overlap quality.
- `IoU` / `mIoU`: more common in defect segmentation papers than ZSAD benchmark papers.

## Protocol Types

### Zero-Shot ZSAD / ZSAS

Allowed:

- pretrained CLIP/VLM/SAM;
- fixed prompts or no target training;
- auxiliary non-target datasets only if clearly declared.

Risk:

- if auxiliary anomaly data is used, the paper is not pure no-training zero-shot; call it auxiliary-data ZSAD or cross-dataset ZSAD.

### Auxiliary-Data ZSAD

Allowed:

- train prompt/adapters/modules on a source anomaly dataset;
- evaluate on target datasets with disjoint object categories.

Expected protocol:

- use VisA as source for non-VisA targets;
- use MVTec AD as source when evaluating VisA;
- report the source dataset explicitly in setup.

### Few-Shot Normal-Only AD

Allowed:

- use K normal images from the target class;
- store memory features or tune prompts using normal samples.

Expected reporting:

- 1-shot, 2-shot, 4-shot;
- mean and standard deviation over random seeds;
- compare with SPADE, PaDiM, PatchCore, WinCLIP+, PromptAD as appropriate.

### Test-Time Adaptation

Allowed:

- use the current unlabeled test sample or batch;
- use augmentations and self-supervised objectives;
- update a restricted parameter group if protocol allows.

Expected reporting:

- state what data is visible at test time;
- compare no-adaptation baseline;
- report runtime overhead.

## Dataset Roles

### Main Industrial Benchmarks

- MVTec AD: standard industrial benchmark with object and texture categories.
- VisA: strong complement to MVTec; product names can be ambiguous and categories are disjoint from MVTec.

### Broader Industrial Generalization

- MPDD, BTAD, SDD/KSDD/KSDD2, DAGM, DTD-Synthetic, BTech, Road, RSDD, MSD, GC.

Use these when claiming broad industrial transfer.

### Medical / Cross-Domain Benchmarks

- BrainMRI/HeadCT/Br35H for image-level.
- ISIC, ColonDB, ClinicDB, Kvasir, TN3K for pixel-level.

Use these when claiming object-agnostic or cross-domain abnormality transfer.

## Metric Reporting Rules

- Put metric direction in headers: `AUROC ↑`, `AP ↑`, `AUPRO ↑`.
- Do not compare image-level and pixel-level values in the same column.
- Use consistent decimal precision.
- If reporting `max-F1`, say it uses the best threshold and is not a deployment threshold.
- If using `PRO/AUPRO`, explain that it evaluates region overlap rather than only pixel ranking.
