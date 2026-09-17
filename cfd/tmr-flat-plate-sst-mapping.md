# TMR flat-plate SST mapping

Status: v2512 source-mapped SSTm candidate under numerical test; not yet benchmark acceptance and not rocket validation.
Earlier coefficient-only cases remain partial mappings.

## Sources and target

- NASA TMR validation definition and quantities: <https://tmbwg.github.io/turbmodels/flatplate_val.html>
- NASA TMR SSTm validation results used here: <https://tmbwg.github.io/turbmodels/flatplate_val_sst.html>
- Separate NASA TMR SST-Vm validation results, not used by the retained `sst-*` files:
  <https://tmbwg.github.io/turbmodels/flatplate_val_sstv.html>
- NASA TMR SST-family equations: <https://tmbwg.github.io/turbmodels/sst.html>
- OpenFOAM v2512 `kOmegaSST` source documentation:
  <https://api.openfoam.com/2512/TurbulenceModels_2turbulenceModels_2RAS_2kOmegaSST_2kOmegaSST_8H_source.html>
- OpenFOAM v2512 SST base implementation documentation:
  <https://api.openfoam.com/2512/TurbulenceModels_2turbulenceModels_2Base_2kOmegaSST_2kOmegaSSTBase_8C_source.html>
- OpenFOAM v2512 omega wall-function documentation:
  <https://api.openfoam.com/2512/classFoam_1_1omegaWallFunctionFvPatchScalarField.html>
- NASA TMR's OpenFOAM implementation warning and modification report:
  <https://tmbwg.github.io/turbmodels/openfoam_issues.html> and
  <https://tmbwg.github.io/turbmodels/Papers/ChangesToOpenFOAM.pdf>

The retained CFL3D files `sst-cf_cfl3d.dat` and `sst-upyp_cfl3d.dat` target **SSTm**, not SST-Vm and not an unspecified
generic SST model. TMR publishes separate `sstv-*` files for SST-Vm. Earlier retained manifests mislabeled this target;
those cases remain sealed as failed/sensitivity evidence.

## Explicit mapping

| Item                                          | TMR SSTm                                                                                                                        | OpenFOAM v2512 default                  | Partially mapped flat-plate case                      |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------- |
| Production term                               | exact/strain-rate form with the `m` isotropic contribution omitted                                                              | strain-rate form                        | directionally aligned, subject to exact source review |
| Isotropic `2/3 rho k` production contribution | omitted (`m`)                                                                                                                   | incompressible implementation           | equivalent when velocity divergence is zero           |
| Production limiter multiplier                 | 20                                                                                                                              | `c1=10`                                 | override `c1=20`                                      |
| `gamma1`                                      | derived original-SST value 0.5531666666666668                                                                                   | 5/9                                     | override 0.5531666666666668                           |
| `gamma2`                                      | derived original-SST value 0.4403546666666667                                                                                   | 0.44                                    | override 0.4403546666666667                           |
| Other listed base coefficients                | `sigma_k1=0.85`, `sigma_k2=1`, `sigma_omega1=0.5`, `sigma_omega2=0.856`, `beta1=0.075`, `beta2=0.0828`, `beta*=0.09`, `a1=0.31` | same numeric defaults                   | defaults retained                                     |
| Wall omega                                    | `10*6*nu/(beta1*d1^2)`                                                                                                          | general low/high-Re `omegaWallFunction` | fixed TMR factor-10 value                             |

The current generator variant is named `tmr-sstm-flatplate-partial-map`. It deliberately refuses to generate unless
`tmr-fixed-factor10` is also selected. Earlier retained cases used the erroneous provisional label
`tmr-sst-vm-flatplate-equivalent`; source and reference-file review invalidated that label, so those cases are
sensitivity evidence only and are not silently rewritten.

The partial map does **not** establish equation equivalence. NASA TMR's OpenFOAM note identifies additional changes to
the blending functions, cross-diffusion floor/handling, and vorticity-based eddy-viscosity limiter used by standard
SSTm. Those must be checked against the exact current source or implemented explicitly; coefficient agreement and a good
skin-friction curve are insufficient.

## v2512 source-mapped candidate

`TmrSSTm` derives from the packaged OpenFOAM v2512 `kOmegaSST` model and makes the source-level changes required by the
current TMR standard-SST definition that are not coefficient settings:

- use `1e-20` as the `CD_komega` floor in F1 and remove OpenFOAM's outer F1 argument cap;
- remove OpenFOAM's outer F2 argument cap and exclude the optional F3 multiplier;
- use the vorticity magnitude `sqrt(2)*mag(skew(grad(U)))` in the eddy-viscosity limiter while retaining the strain-rate
  production term.
- use the incompressible SSTm transport equations without v2512's generic isotropic `div(U)` source corrections in the
  `k` and omega equations. The v2512 incompressible momentum stress operator already omits the isotropic `2/3 k` term.

The case supplies the original-SST gamma values and production limiter `c1=20`, and uses the published factor-10 fixed
wall omega. The compiled image and every build-input hash are sealed in `cfd/sstm-image-provenance.json`;
`cfd_flat_plate_model_audit.py` verifies those hashes, the immutable image ID, runtime model selection, coefficients,
and wall value. This establishes the source-map provenance only. Mesh, scheme, outer-flow, profile, and benchmark
comparisons remain independent gates.

The wall-resolved TMR mapping also fixes wall `k=0` and turbulent viscosity `nut=0`, while inlet `nut` must equal the
declared `0.009*nu`. OpenFOAM's `kqRWallFunction` is a high-Re zero-gradient wrapper, not an equivalent statement of
`k_wall=0`; earlier source-model cases using that wrapper or zero inlet `nut` are retained as sensitivity evidence. The
model audit therefore requires the separate published-boundary type-and-value audit to pass before reporting the
equation mapping complete.

## Acceptance consequences

1. Default-OpenFOAM runs remain numerical preflights and sensitivity evidence.
2. Benchmark acceptance requires a complete equation mapping (or an explicitly compiled TMR implementation), a
   systematic grid family, a higher-order velocity scheme, converged residuals, the outer-flow quality gate, and the
   predeclared five-percent comparison screen.
3. The solver log must show the requested coefficient overrides; the case manifest alone is insufficient runtime
   evidence.
4. Passing this benchmark supports only the attached-wall/turbulence subsystem. External-body force, pressure, moment,
   separation, and rocket-specific gates remain open.
