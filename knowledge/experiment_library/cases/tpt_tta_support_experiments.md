# TPT / TTA Support Experiments

Sources: [TPT card](../../cards/shu-2022-tpt.md), [Tent card](../../cards/wang-2021-tent.md), [MEMO card](../../cards/zhang-2022-memo.md)

## Experiment Claim

Test-time prompt/adaptation methods can improve zero-shot robustness by optimizing only allowed test-time signals, usually a single unlabeled sample or its augmented views.

## Scope Warning

TPT, Tent, and MEMO are not ZSAD papers. Use this case when a ZSAD idea includes test-time prompt tuning, test-time adaptation, confidence selection, augmentation consistency, or entropy minimization.

## Main Experiment Package

- TPT evaluates CLIP prompt tuning on natural distribution shifts and cross-dataset generalization.
- TPT uses ImageNet variants such as ImageNet-A, ImageNet-V2, ImageNet-R, and ImageNet-Sketch.
- Baselines include zero-shot CLIP, prompt ensemble, CoOp, CoCoOp, and TPT.
- MEMO/Tent evaluate test-time adaptation on corruption/OOD benchmarks and compare against no-adaptation, test-time augmentation, batch normalization adaptation, and entropy objectives.
- Metrics are usually top-1 accuracy or error, but the experimental logic transfers to ZSAD metrics.

## Tables And Figures

- TPT Table 1: robustness to natural distribution shifts.
- TPT Table 2: cross-dataset generalization.
- TPT Table 3: context-dependent visual reasoning.
- TPT Table 4: confidence selection ablation.
- TPT Figure 1: test-time prompt tuning overview.
- TPT Figure 3: cross-dataset improvement matrix.
- TPT Figure 4: ablation of parameter groups and confidence threshold.
- TPT Figure 5: efficiency versus accuracy with augmented views and update steps.
- MEMO Table 4: adaptation objective ablation.
- Tent Figures 6-7: entropy/loss reduction and adapted feature visualization.

## What Is Required To Borrow

If a new ZSAD paper uses TTA or test-time prompt tuning:

- Define exactly what is visible at test time: single image, batch, augmentations, normal references, or unlabeled target stream.
- Include no-adaptation baseline.
- Compare against test-time augmentation without parameter updates.
- Ablate the adapted parameter group: prompt only, adapter only, visual encoder, full model, or normalization parameters.
- Ablate confidence selection or sample filtering if used.
- Report inference overhead, number of augmented views, and number of update steps.
- Use ZSAD metrics instead of classification accuracy: I-AUROC/I-AP and P-AUROC/P-AP/P-AUPRO.

## What Is Optional

- ImageNet OOD benchmarks are not necessary for a ZSAD paper unless the paper also claims generic CLIP robustness.
- Tent/MEMO corruption benchmarks can be cited as motivation rather than reproduced.

## Do Not Copy Blindly

Do not call a method zero-shot if it adapts on target batches with hidden labels, masks, or category-specific target statistics. Test-time adaptation is acceptable only when the allowed signal is explicit and label-free.

## Transfer Checklist

- Main table: ZSAD with and without test-time adaptation.
- Ablation: adapted parameter group, entropy objective, confidence selection, augmentations, update steps.
- Figure: adaptation pipeline and efficiency-performance curve.
