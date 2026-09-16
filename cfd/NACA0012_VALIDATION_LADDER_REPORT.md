# OpenFOAM NACA 0012 validation ladder

**Result:** the strict ladder fails at the documented Spalart–Allmaras control. The downstream stock-SST, exact-SSTm, and compressible comparisons are complete, reproducible relative diagnostics; they do not convert the failed control into validation and are not approved for rocket aerodynamics.

## What was actually reproducible

OpenFOAM v2512's packaged `tutorials/incompressible/simpleFoam/airFoil2D` case ran with all 18 upstream inputs unchanged and reached solver-reported convergence at iteration 308. That proves the pinned installation can execute the official tutorial.

It does **not** reproduce the documented NASA comparison. The packaged tutorial is a different case: 10,720 cells, 78 wall faces, 8.002 degrees angle of attack, 26.0032 m/s, `nu=1e-5 m2/s`, and no `forceCoeffs` object. The documentation describes the NASA 897x257 grid, 513 surface points, 0/10/15 degrees, 51.4815 m/s, and `nu=8.58e-6 m2/s`. The complete plot-generating OpenFOAM case and raw force tables are absent from the packaged tutorial and documentation history.

The marker digitized from the official plot is consistent with NASA at its one-pixel uncertainty: `Cd = 0.00813559 ± 0.00010169`. Our reconstructed documented-grid SA case did not reproduce it.

## Gate results

| Gate | Change | Mean Cd | Reference delta | Result |
| --- | --- | ---: | ---: | --- |
| 0 | Run packaged v2512 `airFoil2D` unchanged | — | — | Pass as installation control only; NASA comparison is not applicable |
| 1 | Reconstruct documented NASA 897x257 SA case | 0.0084913754 | +0.0002989078 vs CFL3D SA | **Fail**; outside the predeclared ±0.0002 Cd limit |
| 2a | Change SA to stock `kOmegaSST` only | 0.0196564740 after 10,000 iterations | +0.0115627448 vs CFL3D SST | **Fail** numerical entry: asymmetric branch and force disagreement |
| 2b | Predeclared bounded-upwind `k/omega` remediation, restarted from original SA `U/p` | 0.0081442443 | +0.0000505150 vs CFL3D SST | Diagnostic pass; strict Gate 2 remains blocked by Gate 1 |
| 3 | Stock SST to exact NASA `TmrSSTmExactProduction` only | 0.0081212871 | +0.0000275578 vs CFL3D SST | Diagnostic pass; `Delta Cd = -0.0000229572` (-0.282%) |
| 4 | `simpleFoam` to matched `rhoSimpleFoam` closure | 0.0081220316 | +0.0000283024 vs CFL3D SST | Diagnostic pass; `Delta Cd = +0.0000007445` (+0.0092%) |

The Gate-2b SA-to-stock difference is `-0.0003471312` (-4.088%), but it is **not** a pure turbulence-model effect because the accepted stock branch also uses the separately declared `k/omega` convection remediation. Gates 3 and 4 are clean one-component comparisons from numerically accepted sources.

## Fixed numerical gates

Thresholds were declared before observing each retained endpoint:

- 5,000 iterations per retained rung; the accepted stock endpoint uses one unchanged 5,000-iteration continuation, 10,000 cumulative.
- Final-100 peak-to-peak for `Cd`, `Cl`, and quarter-chord `Cm` no greater than `max(0.001, 1% of |mean|)`.
- Projected absolute change over 500 iterations no greater than `0.0002 Cd`, `0.004 Cl`, and `0.0002 Cm`.
- Final-100 maximum initial residual no greater than `1e-5` for every solved equation. The compressible rung adds energy.
- At zero angle, `|mean Cl| <= 0.004` and `|mean Cm| <= 0.0002`.
- NASA force screen: `|mean Cd - CFL3D Cd| <= 0.0002`.

The accepted final-100 residual maxima were:

| Rung | p | Ux | Uy | e | k | omega |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Stock SST | 1.26e-7 | 1.91e-8 | 4.43e-6 | — | 1.71e-8 | 9.99e-10 |
| Exact SSTm incompressible | 5.24e-8 | 1.67e-8 | 1.24e-6 | — | 1.14e-8 | 9.98e-10 |
| Exact SSTm compressible | 2.18e-7 | 1.57e-8 | 3.43e-7 | 1.05e-7 | 3.71e-8 | 9.34e-8 |

## Compressible mapping

Gate 4 preserved the exact-SSTm mesh, `U/k/omega/nut` fields, `U` linear-upwind convection, `k/omega` bounded-upwind convection, overlapping relaxation, force axes, area, length, and quarter-chord center. It used:

- `U = 51.4815 m/s`, `M = 0.15`, `nu_inf = 8.58e-6 m2/s`, `Re = 6,000,174.825`.
- Perfect gas at `p_inf = 101325 Pa`; `T_inf = 293.1609639 K` is derived so the preserved velocity is exactly Mach 0.15.
- `rho_inf = 1.2042725343 kg/m3`, `mu_inf = 1.0332658344e-5 Pa s`.
- Exact Sutherland transport with `As = 8.3073404427e-7`, `Ts = 110.4 K`, molecular `Pr = 0.72`, turbulent `Prt = 0.9`.
- Cellwise pressure initialization `p_abs = p_inf + rho_inf*p_kinematic`; new `T` and `alphat` fields; `rhoSimpleFoam` and its energy/pressure-density terms.

The final 100 iterations activated no temperature limiter cells. This is a reported diagnostic, not an added acceptance threshold.

## Reproduction artifacts

Machine-readable result: [`naca0012-validation-ladder-outcome-v1.json`](naca0012-validation-ladder-outcome-v1.json).

Key audits:

- Packaged tutorial: `runs/cfd-openfoam-airfoil2d-sa-control-audit-v1-20260914/openfoam-airfoil2d-control-audit.json`
- SA diagnosis: `cfd/naca0012-sa-control-diagnosis-v3.json`
- Stock SST: `runs/cfd-openfoam-naca0012-stock-sst-upwind-continuation-audit-v2-20260915/naca0012-stock-sst-continuation-audit.json`
- Exact SSTm: `runs/cfd-openfoam-naca0012-exact-sstm-incompressible-from-stock-upwind-audit-v1-20260915/naca0012-exact-sstm-incompressible-audit.json`
- Compressible: `runs/cfd-openfoam-naca0012-exact-sstm-compressible-from-incompressible-audit-v2-20260915/naca0012-exact-sstm-compressible-audit.json`

Plans and builders record exact source case specifications, source-audit hashes, image identities, copied-file hashes, copied-field hashes, resources, and runtime model selection. Runs used 12 MPI ranks, a 12-CPU/24-GB Docker limit, no network, and no GPU. Invalid verifier attempts are retained with `INVALID-AUDIT.txt`; no solver case was overwritten to repair an audit.

## Claim boundary

This work supports three narrow conclusions:

1. The packaged v2512 tutorial executes unchanged, but it is not the documented NASA validation case.
2. On the explicitly remediated, accepted stock-SST branch, exact NASA SSTm changes alpha-zero drag by about -0.282%.
3. At matched Mach and Reynolds number, the compressible solver changes that exact-SSTm drag by about +0.009%, so compressibility is negligible for this one operating point.

It does not reproduce strict Gate 1, identify the unpublished official OpenFOAM setup, establish grid/domain independence for this remediated branch, validate other angles or separated flow, or authorize transferring any coefficient to the rocket model.
