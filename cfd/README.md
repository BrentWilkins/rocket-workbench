# Passive fin aerodynamic cross-check

## Completed NACA 0012 ladder outcome

The strict ladder and its downstream relative diagnostics are now complete. See
the [publication-ready report](NACA0012_VALIDATION_LADDER_REPORT.md), the
[machine-readable outcome](naca0012-validation-ladder-outcome-v1.json), and the
[SHA-256 manifest](naca0012-validation-ladder-manifest-v1.json). Strict
validation failed at the documented SA reproduction; the accepted downstream
stock-SST, exact-SSTm, and compressible cases are diagnostics only and remain
blocked from rocket use.

## NACA 0012 validation ladder

The current external-body investigation is split into a one-change-at-a-time ladder documented in
[`naca0012-validation-ladder-plan.json`](naca0012-validation-ladder-plan.json):

1. Execute the exact packaged OpenFOAM v2512 `airFoil2D` tutorial as an installation control.
2. Reconstruct the separately documented NASA 897x257 Spalart-Allmaras case and compare it with
   the pinned CFL3D SA force, pressure, and skin-friction results.
3. Change only SA to stock OpenFOAM `kOmegaSST`.
4. Change only stock SST to the source-audited exact NASA SSTm implementation.
5. Change only `simpleFoam` and its transport closure to the compressible `rhoSimpleFoam` path.

The exact packaged v2512 tutorial passed its installation control in 308 iterations with all 18
upstream files byte-identical to tag `OpenFOAM-v2512`, commit
`87ed40d256d22ea38fcc648dfc82a22162427b18`. It is not the case described by OpenFOAM's NACA 0012
validation page: the package contains 10,720 cells, 78 airfoil faces, velocity `(25.75 3.62 0)`,
kinematic viscosity `1e-5`, and no force-coefficient function. The documentation specifies the NASA
897x257 grid with 513 airfoil points, velocity magnitude `51.4815`, kinematic viscosity `8.58e-6`,
and comparison angles 0, 10, and 15 degrees. Accordingly, the unchanged packaged run is retained as
an installation/tutorial-integrity control and makes no NASA-agreement claim.

Generate the documented zero-angle SA control only from a checksum-verified benchmark bundle:

```sh
uv run --frozen python scripts/cfd_naca0012_sa_control_case.py \
  --grid-archive runs/cfd-benchmark-data-v6-sa-20260914/naca0012-grids.zip \
  --output runs/cfd-openfoam-naca0012-897x257-a0-sa-doc-control-UNIQUE \
  --iterations 5000
```

Run it with the CPU-only pinned solver image. The RTX 4090 is not used because this image and solver
have no GPU backend; switching implementations would invalidate the intended control.

```sh
uv run --frozen python scripts/cfd_run.py \
  --case runs/cfd-openfoam-naca0012-897x257-a0-sa-doc-control-UNIQUE \
  --image rocket-workbench-cfd:2512-native --prebuilt-mesh \
  --mpi-ranks 12 --cpus 12 --memory 24g
```

Audit the completed control against the pinned NASA CFL3D SA coefficient table:

```sh
uv run --frozen python scripts/cfd_naca0012_sa_control_audit.py \
  --case runs/cfd-openfoam-naca0012-897x257-a0-sa-doc-control-UNIQUE \
  --benchmark-data runs/cfd-benchmark-data-v6-sa-20260914 \
  --output runs/cfd-openfoam-naca0012-sa-control-audit-UNIQUE
```

Current Gate 1 status is fail-closed. The best-settled documented setup gives
`Cd=0.00849138`, 3.65% above pinned CFL3D SA. Serial execution changes mean drag by only
`-0.00000208` and fails the same residual gate, ruling out 12-rank Scotch decomposition as the
dominant cause. Separate parity runs then change only `nuTilda/nu` from 4 to 3 and only `ft2`
from false to true. Exact standard SA gives `Cd=0.00846906`, still 3.38% high, with the residual,
moment-symmetry, and force-agreement gates failing. Surface integration attributes about 85% of
the remaining `0.00027659` drag excess to pressure and 15% to viscous shear; it reconstructs both
the logged OpenFOAM drag and NASA tabulated drag closely. See
[`naca0012-sa-control-diagnosis-v3.json`](naca0012-sa-control-diagnosis-v3.json).

Two additional predeclared screens close plausible undocumented mechanisms. Four SIMPLE
non-orthogonal correctors change settled Cd by `-0.000002077`; the digest-pinned official
OpenFOAM Foundation 4.1 lineage changes it by `-0.000001995`. Each closes less than 0.7% of
the NASA gap and is a declared null effect, so neither run is extended. Direct official-PLOT3D
conversion also matches all 460,672 points and all 918,464 face-connectivity sets. The official
alpha-zero raster marker is NASA-consistent at one-pixel resolution, but the raw plot-generating
OpenFOAM case and result tables remain unpublished.

The official validation page's tutorial link is not reproducible as an unchanged NASA-grid
control: it points to the materially different packaged `airFoil2D` case, while the plot-generating
case and all of its controls are not shipped there. The documentation source's reference to four
non-orthogonal correctors is commented out, so it is not silently adopted as a missing setting.
Gate 2 is therefore blocked for validation; subsequent model swaps must remain explicitly labelled
relative diagnostics unless the original plot-generating case is obtained.

Independent prior work materially corroborates the earlier SST result. Ye Zhang's 2017 Delft
dissertation reports OpenFOAM SST drag of `0.00870783` on the 449x129 TMR grid and a second-order
extrapolation of `0.008696367`, with OpenFOAM skin friction slightly above CFL3D. The retained
exact-SSTm result `0.00875224` differs from those values by only `0.00004441` and `0.00005587`,
respectively. This establishes that elevated OpenFOAM drag is reproducible prior work, while not
turning either calculation into accepted rocket-design evidence.

## TMR flat-plate validation environment

The current SSTm validation path uses OpenCFD OpenFOAM v2512 package version `2512.0-2`. Build the source-capable base and the derived runtime model in order:

```sh
docker build --pull=false -f cfd/Dockerfile.2512-dev -t rocket-workbench-cfd:2512-dev cfd
docker build --pull=false -f cfd/Dockerfile.2512-sstm -t rocket-workbench-cfd:2512-sstm cfd
```

The observed immutable development/model image IDs and SHA-256 hashes for every build input are recorded in [`sstm-image-provenance.json`](sstm-image-provenance.json). A rebuilt tag is not accepted merely because its name matches; refresh provenance deliberately and rerun the model audit if any build input or resolved image changes.

Future flat-plate cases use the boundary conditions in the published TMR/OpenFOAM table: transported fields fixed at the inlet and zero-gradient at the outlet/top; inlet `nut` consistent with the declared `nut/nu=0.009`; pressure zero-gradient at inlet/top and fixed only at the outlet; wall `k` and turbulent viscosity fixed to zero; and wall omega fixed by the TMR factor-10 formula. `cfd_flat_plate_boundary_audit.py` enforces both patch types and scalar values. Older retained cases used fixed top values, fixed pressure at multiple boundaries, zero inlet `nut`, or high-Re `k`/`nut` wrappers; they are preserved as failed evidence and must not be used for acceptance.

The `TmrSSTm` runtime model is CPU-only in this environment. It derives from the exact packaged v2512 source, applies the standard-SSTm F1/F2 and vorticity-limiter differences, and still requires the independent mesh, scheme, near-wall, domain, outer-flow, and benchmark gates. Building or loading the model does not validate rocket aerodynamics.

The validation campaign is complete at the checkpoint recorded in
[`NACA0012_VALIDATION_LADDER_REPORT.md`](NACA0012_VALIDATION_LADDER_REPORT.md). No CFD result is
accepted as validated rocket-design evidence. Downstream SST/SSTm results may be used only for
explicitly exploratory, matched comparisons whose numerical sensitivity and claim limits are
reported.

The current native AMD64 environment uses OpenCFD OpenFOAM v2512 on Ubuntu 24.04, built with `Dockerfile.2512`. The
image base digest and OpenFOAM packages (2512.0-2) are pinned; transitive Ubuntu dependencies are not independently
locked. Every executed case records the resolved image ID. Keep container CPU/memory limits explicit. Mount only the
individual study directory, never the Docker socket.

For another host, build a native image and pass its tag explicitly with `--image`. The APT source uses the native
package architecture. The retained AMD64 installation smoke and MPI plumbing runs passed
their execution checks; this is not aerodynamic validation. The runner sources the explicit
`--openfoam-bashrc` path (default `/usr/lib/openfoam/openfoam2512/etc/bashrc`) independently of image tag. Use an empty
value only for an image whose environment is already configured. The runner defaults to serial execution; a Docker CPU
quota alone does not enable MPI or GPU acceleration. Record architecture, image identity and resource allocation before
comparing results across machines.

The retained v1912 Dockerfile documents the first installation attempt. Its upstream cavity smoke test passed, but the
rocket run failed in function-object initialization. It is not the default solver environment. Failed cases are
retained, including the initial degenerate nose-apex STL and the mesh-quality failure that returned exit status zero.
The runner checks diagnostic text as well as process status so those failures cannot silently become accepted runs.

## Reproduce a diagnostic case

The runner defaults to a serial solve at two CPUs and 4 GiB. Parallel runs require an explicit
`--mpi-ranks N` together with `--cpus N` (or more); the runner records and executes `decomposePar`,
`mpirun ... simpleFoam -parallel`, and `reconstructPar`. The image has no GPU-enabled solver setup, and
resource limits are not scaling evidence.

First run the packaged upstream cavity as an installation-only diagnostic:

```sh
uv run --frozen python scripts/cfd_smoke.py \
  --output runs/cfd-installation-smoke-UNIQUE \
  --image rocket-workbench-cfd:2512-native
```

This retains the copied tutorial, log, image identity, and resource limits. It is not a rocket or
aerodynamic validation benchmark. After verifying host and Docker resources, a parallel rocket run can
explicitly request, for example, `--mpi-ranks 8 --cpus 8 --memory 24g`. These are proposed starting limits,
not benchmark results.

Before meshing, audit a newly generated surface without modifying it:

```sh
uv run --frozen python scripts/cfd_geometry_audit.py --case CASE --output GEOMETRY_AUDIT
```

The audit checks the source STEP solid, STL size, closure, winding, signed volume, SI dimensions, reference area
and length, lateral volume centroid, and the expected three-fold rotation and mirror symmetry. It reports CAD
solid and tessellated-surface symmetry separately. A failed surface result is retained for diagnosis; it is not
relaxed merely because the exact CAD solid is symmetric.

Use `scripts/cfd_case.py --axisymmetric-control` for the zero-angle implementation-bias control. This removes
the fin collar from the external surface while retaining the same axis, domain, reference quantities, flow
conditions, and numerical setup. It is a diagnostic control, not a rocket benchmark.

The axisymmetric control uses an analytic 192-sector surface of revolution so its STL
topology is divisible by both four and twelve and its maximum radial chord error is
recorded. A retained 50 mm background-grid run (15,536 cells, 140 rocket-wall faces)
failed the provisional zero-angle screen: Cd 0.69646, Cl 0.03460, CmPitch 0.54424.
The otherwise matched 25 mm run (247,912 cells) passed that screen: Cd 0.42379,
|Cl| 0.00010, |CmPitch| 0.00063. The large Cd change is a mesh-independence failure,
so neither drag result is accepted. These controls isolate coarse volume/surface mesh
bias; they do not validate the finned surface, wall treatment, or turbulence model.

From the repository root, build the current image with
`docker build -f cfd/Dockerfile.2512 -t rocket-workbench-cfd:2512-arm64 cfd`. Generate a unique case directory using
`scripts/cfd_case.py --config CONFIG --output CASE --cell-mm 20`, then run `scripts/cfd_run.py --case CASE` and
`scripts/cfd_audit.py --case CASE --output AUDIT` with the project Python. The runner limits each container to two CPUs
and 4 GiB with networking disabled. Do not run multiple heavy cases concurrently on the current workstation. Do not
reuse or edit completed case directories to represent a new mesh.

The initial clean 30 mm background-grid case reached 600 iterations but failed the zero-angle force/moment symmetry
screen. The 20 mm case is a refinement diagnostic, not a validated baseline. Both use level-four surface refinement, no
inflation layers, steady incompressible SST and a simplified sealed exterior. A third grid and wall/domain checks are
required before interpreting drag differences; small residuals alone do not establish aerodynamic accuracy.

## Acceptance sequence

Benchmark definitions, predeclared uncertainty rules, and the current fail-closed gate matrix are retained in
[`validation-plan.json`](validation-plan.json).

Surface-preparation update: relative-deflection tessellation produced 22 open edges at the clipped-delta root/collar
junction. Absolute-deflection trials at 10 and 1 micrometres closed; a 0.1 micrometre trial failed again. The generator
now clears cached triangulations and uses explicit 10 micrometre absolute deflection, retaining the hard closure gate.
Matched planar and 5/10 mm ring-tail surfaces were prepared successfully. This does not establish aerodynamic accuracy.
Do not replace geometry in the retained three-grid baseline study: its surface hashes differ from these new inputs.

1. Run an upstream tutorial to check the solver installation; this is not a rocket benchmark.
2. Generate a closed external aerodynamic surface for the conventional baseline, with explicit reference area, length,
   moment origin, flow direction and units. Do not use the hollow print assembly as a sealed external flow surface.
3. Compare baseline force and moment coefficients with OpenRocket over relevant speed and angle-of-attack cases. A
   drag-only adjustment cannot establish restoring moments or dynamic stability for a nonplanar fin.
4. Assess iterative convergence, three systematically refined meshes, domain extent, wall resolution, and turbulence
   assumptions. Retain rejected runs. Agreement between two models alone is not experimental validation.
5. Only then compare an explicitly defined ring-tail or curved-tube candidate with equivalent mass and packaging
   accounting. Any integration into flight dynamics must preserve coefficient axes, reference quantities and validity
   bounds. Unimplemented forces/moments must remain marked unsupported.

Design choice must consider altitude, speed, stability, recovery, mass, print orientation, structural uncertainty and
manufacturing effort. A colorful flow plot or lower computed drag is not sufficient to select a flight design.

Sources: [OpenRocket fin limitations](https://wiki.openrocket.info/Fin_Sets_Basics),
[NASA CFD verification and validation](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html),
[OpenFOAM user guide](https://www.openfoam.com/documentation/user-guide).

## Scoped validation status

The retained TMR flat-plate evidence in
`runs/cfd-tmr-flatplate-final-sstm-acceptance-20260913` passes all declared
benchmark, profile, outer-flow, wall-resolution, boundary/model mapping,
three-grid, scheme, and domain checks. This accepts only the attached-wall
SSTm subsystem. It does not accept external-body forces, separation, a rocket,
or flight prediction.

The following section records the completed TMR NACA 0012 external-body campaign and its
reproduction commands. Build its
compressible SSTm registration image on top of the unchanged accepted
flat-plate image:

```sh
docker build --pull=false \
  -f cfd/Dockerfile.2512-sstm-compressible \
  -t rocket-workbench-cfd:2512-sstm-compressible cfd
```

The observed image ID and build hashes are recorded in
[`sstm-compressible-image-provenance.json`](sstm-compressible-image-provenance.json).
Generate cases only from the pinned official archive in a fresh benchmark
bundle:

```sh
uv run --frozen python scripts/cfd_naca0012_case.py \
  --grid-archive runs/cfd-benchmark-data-v4-20260914/naca0012-grids.zip \
  --output runs/cfd-tmr-naca0012-UNIQUE \
  --grid-ni 225 --angle-deg 0 --iterations 3000 \
  --convection first-order-upwind
```

To extend an unconverged case without changing its evidence, generate a new
case with `--initialize-from PATH_TO_PARENT`. The generator accepts only a
fully executed parent with the same grid, angle, scheme, solver, model, and
transport settings. It copies the latest `U`, `p`, `T`, `k`, `omega`, `nut`,
and `alphat` fields into the child's time zero and records every source path,
time, and SHA-256 digest in the child manifest.

The NACA path uses `rhoSimpleFoam` at Mach 0.15 and chord Reynolds number
6 million. The runner selects that solver from the generated manifest through
an explicit solver allowlist. The official C-grid wake cut is merged using the
NASA neutral-map 3:8:3 wake-wall-wake index split. The pinned mesh exception
admits only the exact documented quality diagnostics while still requiring
topology, one connected region, positive cell volumes, face pyramids,
non-orthogonality, and skewness checks to pass.

`cfd_naca0012_force_audit.py` checks recorded image/solver/model selection,
SSTm coefficients, last-window range, a 500-iteration projected-drift gate
tied to experimental repeatability, final and last-100 equation residuals,
limiter inactivity, zero-angle symmetry,
and the recorded pitch-axis convention. OpenFOAM reports `CmPitch` about
negative z in this setup. Since the nose is toward negative x from quarter
chord, this is already the nose-up-positive convention used for comparison.
`cfd_naca0012_pressure_audit.py` extracts wall-adjacent Cp but
deliberately withholds experimental comparison: the retained Gregory pressure
data are Re=2.88 million and the Ladson pressure data are Mach 0.3 with free
transition, so neither may be mislabeled as the Mach 0.15, Re=6 million,
tripped force condition. The v4 bundle also pins NASA TM-4074, and
`cfd_naca0012_ladson_reference.py` emits the visually checked matched force and
quarter-chord moment rows with page provenance.

Gate 3 numerical recovery at zero angle is recorded in
`runs/cfd-tmr-naca0012-gate3-recovery-20260914`. Exact published TMR
freestream turbulence inputs and deterministic adjacent-grid structured
prolongation recover the 225x65, 449x129, and 897x257 force-trend and
equation-residual checks. The finest-pair absolute drag change is 0.00001392,
and the converged fine-grid LUST comparison changes drag by 0.00001105; both
are below the predeclared 0.0002 numerical-independence scale. Solver-context
post-processing gives a fine-grid maximum y-plus of 0.1350 below the
wall-resolved limit of 1.0. Stock OpenFOAM `kOmegaSST` sensitivity is also
characterized on the converged fine grid, with absolute drag change 0.00002803
and no post-hoc pass threshold. The predeclared reduced-domain comparison did
not satisfy the equation-residual gate: both default and 0.5x relaxation grew
an energy residual mode. Thus iterative, grid, scheme, near-wall, and
turbulence-model evidence is complete, but domain sensitivity remains failed.
Benchmark agreement also remains unaccepted: fine linear-upwind drag exceeds
official CFL3D SST by 0.00069097 and the matched Ladson tripped mean by
0.00070870. Same-grid CFL3D diagnostics localize the discrepancy: upper and
lower RMS pressure-coefficient differences are about 0.00325 over
`0.01 <= x/c <= 0.98`, while mean OpenFOAM-to-CFL3D skin friction is 1.1094.
Force-component integration shows the discrepancy is not exclusively viscous:
relative to CFL3D, excess viscous Cd is 0.00045946 (66.5% of the total) and
inferred excess pressure Cd is 0.00023151 (33.5%). Thus systematically high
viscous shear is the larger contributor, while small pointwise Cp differences
still produce a material pressure-drag difference. The generated Sutherland closure's
effective freestream molecular Prandtl number is 0.69033477 versus the
comparison setup's nominal 0.72. A same-grid exact-Sutherland, constant-Pr=0.72
candidate passes all solver gates but changes Cd by only -0.00000588 (0.83% of
the Ladson discrepancy) and changes the mean CFL3D skin-friction ratio only from
1.10939 to 1.10736. This rules out the molecular-Prandtl mismatch as the
dominant shear explanation. The fail-closed
zero-angle acceptance audit grants the full 0.0002 predeclared domain allowance
anyway: its total conservative allowance is 0.00043180, still 0.00027690 below
the observed Ladson drag discrepancy. No NACA result is accepted for rocket use.

A same-grid incompressible `simpleFoam` control also passes its diagnostic gates.
It changes Cd by only -0.00003251 (4.71% of the baseline CFL3D discrepancy),
almost entirely through pressure; viscous Cd changes by just -0.00000115. The
control still exceeds CFL3D by 0.00065846, so compressibility or thermophysical
coupling is not the dominant cause and does not rescue the production workflow.

The solver-path diagnostic does not rescue Gate 3. A bounded five-flow-through
`rhoPimpleFoam` control completed on the 225x65 grid and was flat over its final
flow-through interval, but its drag differed from the accepted steady control
by 0.000309874, above the predeclared 0.000200 repeatability limit. A fine
transient run was therefore not justified.

A source-level re-audit subsequently found that the first `TmrSSTm`
compatibility model inherited two v2512 production choices that are not the
NASA TMR standard SSTm definition: it limited omega production and used the
deviatoric velocity-gradient contraction. The provenance-pinned
`TmrSSTmExactProduction` diagnostic instead uses unlimited omega production,
the factor-20 limiter only in k, and `P = mu_t S^2`. After a fail-closed
residual-only first attempt and a predeclared convergence continuation, all
diagnostic gates pass. Relative to the exact-Sutherland Pr=0.72 baseline, the
full equation correction changes Cd by -0.00002658 (3.88% of that baseline's
CFL3D gap). The corrected mean Cd is 0.00875224 versus CFL3D 0.00809373, and
mean OpenFOAM/CFL3D skin friction remains 1.10021. This improves equation
fidelity but is not a dominant explanation and does not accept Gate 3. Grid,
scheme, wall, and domain evidence affected by the model change must be repeated
before any future acceptance.

The corrected-model numerical refresh now repeats those checks. The direct
449x129-to-897x257 change is 0.00002237 Cd and the fine-grid LUST change is
0.00000774 Cd; all Cd, Cl, and quarter-chord moment changes pass their
predeclared experimental-repeatability limits. Corrected-model maximum y-plus
is 0.13519, also passing. The predeclared ~100-chord retained-row domain case,
however, again develops a late energy-residual mode: final and final-100
maximum energy initial residual are 0.00002098 versus the fixed 0.00001000
limit. Its force history settles, but its coefficients are withheld because
the equation-residual gate fails. Therefore the corrected-model numerical
independence aggregate remains failed on domain sensitivity.

The corrected-model zero-angle acceptance artifact recomputes the conservative
uncertainty sum from the refreshed evidence. Mean Cd differs from the matched
Ladson tripped mean by 0.00067624. Experimental repeatability, corrected-model
finest-pair, LUST, iterative, digitization, and the entire 0.0002 domain budget
sum to 0.00043868; the discrepancy exceeds that allowance by 0.00023756.
Accordingly both domain sensitivity and drag agreement fail independently.
Gate 3 is failed, and downstream rocket/OpenRocket comparison remains blocked.
