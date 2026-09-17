# CFD background-grid diagnostics

Diagnostic only: spacing is the background grid, not a measured effective mesh size. No Richardson extrapolation or
grid-convergence index is claimed. Check symmetry, iterative convergence, wall resolution, domain sensitivity and
benchmarks separately.

| Background spacing mm | Cd       | Change from coarser % | Settled | Zero-angle symmetry |
| --------------------- | -------- | --------------------- | ------- | ------------------- |
| 30                    | 0.597994 | —                     | True    | False               |
| 20                    | 0.583297 | -2.458                | True    | False               |
| 15                    | 0.539508 | -7.507                | True    | False               |

Source cases:

- `runs/cfd-rocket-pilot-v2512-clean-20260913`
- `runs/cfd-baseline-fine20-20260913`
- `runs/cfd-baseline-fine15-20260913`
