# Task Plan: Hyperbolic UOT Experiment Code

## Goal
Implement experimental code for CLIP-based ZSAD with hyperbolic/cosine/euclidean OT and UOT scoring, then commit it on a new feature branch.

## Phases
- [x] Phase 1: Create feature branch and inspect git state
- [x] Phase 2: Read existing scoring and experiment code
- [x] Phase 3: Implement OT/UOT scoring utilities
- [x] Phase 4: Wire CLI and experiment variants
- [x] Phase 5: Add run scripts and documentation hooks
- [x] Phase 6: Verify with syntax/light tests
- [ ] Phase 7: Stage and commit after message confirmation

## Key Questions
1. Where should OT scoring live so it reuses existing feature extraction?
2. How can balanced, partial, and unbalanced OT be implemented without adding heavy dependencies?
3. What files should be committed without staging unrelated changes?

## Decisions Made
- Branch: `feature/hyperbolic-uot-experiments`.
- Implement the first version in PyTorch with an internal Sinkhorn-style solver to avoid new dependencies.
- UOT image-level score uses the maximum final anomaly map score in evaluation utilities.

## Errors Encountered
- `python` is not available in the shell; use `python3` for verification commands.
- System `python3` can compile files but cannot import `AnomalyCLIP_lib` because `torchvision` is not installed; retry runtime smoke tests with `.venv/bin/python`.

## Status
**Currently in Phase 7** - Ready to stage and commit after commit message confirmation.
