# CFD pilot audit

Completed flow solution is not accepted design evidence.

Solver completed: True. Last iteration: 600. Last-100-sample settling screen: True. Zero-angle lateral/moment symmetry
screen: False.

| Coefficient | Last-100 mean | Peak-to-peak |
| ----------- | ------------- | ------------ |
| Cd          | 0.597994      | 0.000001     |
| Cl          | 0.146153      | 0.000010     |
| Cs          | 0.049554      | 0.000006     |
| CmPitch     | -0.763640     | 0.000050     |
| CmRoll      | 0.136976      | 0.000003     |
| CmYaw       | 0.270554      | 0.000031     |

Axes are taken from the solver output, not assumed from input keywords. v2512 reports pitch about negative Z for this
drag/lift basis. No coefficients have been transferred to flight models. Grid/wall/domain checks and benchmark
comparison remain outstanding.
