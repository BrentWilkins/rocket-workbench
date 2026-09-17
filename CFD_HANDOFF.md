# CFD validation handoff — 2026-09-15

## Current checkpoint

The validation campaign described below has now completed. Its authoritative endpoint is
`cfd/NACA0012_VALIDATION_LADDER_REPORT.md`, with the machine-readable decision in
`cfd/naca0012-validation-ladder-outcome-v1.json`. The strict ladder failed at the documented Spalart–Allmaras
reproduction gate. Downstream stock-SST, exact-SSTm, and compressible runs are retained as reproducible relative
diagnostics, not validated rocket coefficients.

No CFD coefficient has been transferred into a flight model. The next authorized use is an explicitly exploratory,
matched fin-design comparison that reports numerical sensitivity and only calls a winner or loser when the ordering
survives those checks. Preserve every failed run and keep the ranking campaign separate from this validation checkpoint.

The original September 13 transfer instructions remain below as historical setup context. Several of their future-tense
tasks are complete; do not treat them as current status when they disagree with the ladder report.

## Prompt for the next coding agent

Continue the CFD-validation work in this repository. Read this note and `cfd/README.md`, inspect the current code and
retained evidence, then work toward the acceptance gates below. Do not assume this conversation or its active goal
transfers to another machine. Establish a new CFD-validation goal there when the user asks you to start.

The objective is to validate the aerodynamic workflow before using it for rocket optimization—not to make the current
rocket pass by tuning drag or relaxing checks. Retain failed evidence, label engineering assumptions, and document the
different results. Do not purchase hardware, operate a printer, claim physical validation or use unvalidated CFD
coefficients in flight predictions. Ask before publishing new results unless the user explicitly authorizes it there.

## Destination and resource policy

- User reports AMD64, approximately 12 cores / 24 threads, 64 GB system RAM and an NVIDIA RTX 4090. OS is not confirmed.
- Verify OS, Docker availability and Docker's actual CPU/RAM allocation. On Windows, prefer a Linux/WSL2 filesystem for
  case data; do not assume host RAM is available to Docker. Record the observed environment.
- Current `simpleFoam` runner is serial, with a two-CPU quota and 4 GiB memory cap. A quota is not MPI parallelism. The
  provided Docker image has no GPU-enabled solver setup; do not promise acceleration from the 4090.
- First reproduce one small diagnostic under the existing limits. Then implement and test configurable resource limits
  and a genuine `decomposePar` / MPI solver / reconstruction workflow before claiming CPU scaling. Start with one case,
  about 8 physical-core ranks and at most 24 GiB after checking available resources; these are proposed starting limits,
  not benchmarks. Reserve memory for the desktop and avoid simultaneous large meshes.
- Containers stay network-disabled during simulation, with only the individual case directory mounted. Never mount the
  Docker socket. Do not alter sealed runs or retry into directories that already contain execution evidence.

## Get the code and inputs

Repository: https://github.com/BrentWilkins/rocket-workbench

```sh
git pull --ff-only
uv python install 3.14.6
uv sync --locked --extra cad
uv run --frozen pytest -q tests/test_cfd_checks.py tests/test_cfd_audit.py tests/test_cfd_compare.py
docker info
docker build -f cfd/Dockerfile.2512 -t rocket-workbench-cfd:2512-native cfd
docker image inspect rocket-workbench-cfd:2512-native
```

Follow the repository's `rtk` command-prefix instructions if it is installed. It was unavailable on the source Mac. Use
native AMD64 Docker, not ARM emulation. The Dockerfile pins Ubuntu and OpenCFD 2512.0-2 packages; inspect the image
architecture and resolved digest. This AMD64 build has not been tested on the source Mac. If the pinned base or package
version cannot be resolved natively, investigate and document the replacement; do not silently change solver version.
The APT source now uses the native package architecture, and runner environment setup no longer depends on image tag.
Use `--openfoam-bashrc` for a different explicit installation path, or an empty string for a preconfigured image.

`runs/` and `deliverables/` are deliberately ignored by Git. Brent can copy local CFD evidence rather than committing
large meshes. Useful source directories, relative to the source checkout:

- `runs/cfd-rocket-pilot-v2512-clean-20260913` — completed old 30 mm baseline.
- `runs/cfd-baseline-fine20-20260913` and `runs/cfd-baseline-fine15-20260913` — completed refinements.
- `runs/ring-cfd-absolute-inputs-20260913` — corrected-surface planar case (completed) and 5/10 mm ring inputs (unrun).
- `runs/sourced24-insert-corrected-20260913/apogee24-body500-heavy0-cd053-insert-trial/config.yaml` — current review
  rocket configuration. This is NOT the same geometry as the earlier CFD baseline; do not call the change a mesh-only
  comparison. Copy the config when preparing the eventual current-rocket validation cases.

Preserve source directory names and contents. At minimum retain `case-spec.json`, initial fields, dictionaries, surface
geometry, image/execution metadata, stage logs and coefficient output. Full mesh/field folders permit deeper
diagnostics. Git contains compact audit reports under `docs-evidence/runs/`; it does not contain all raw CFD data.

After copying a chosen config, generate a NEW case, for example:

```sh
uv run --frozen python scripts/cfd_case.py --config PATH_TO_CONFIG --output runs/cfd-validation-new-baseline \
  --cell-mm 20 --speed 40 --alpha 0 --iterations 600
uv run --frozen python scripts/cfd_run.py --case runs/cfd-validation-new-baseline \
  --image rocket-workbench-cfd:2512-native
uv run --frozen python scripts/cfd_audit.py --case runs/cfd-validation-new-baseline \
  --output runs/cfd-validation-new-baseline-audit
```

These commands demonstrate the existing diagnostic, not a validated mesh prescription. Read the checks below before
spending time on a large solve. Java/OpenRocket is needed only for the later flight-model cross-check; use README setup.

## Evidence already established

All completed rocket solutions settled but failed the provisional zero-angle symmetry screen. No CFD coefficients were
transferred to OpenRocket.

| Case                                            | Cd       | Key finding                                                  |
| ----------------------------------------------- | -------- | ------------------------------------------------------------ |
| Old baseline, 30 mm background grid             | 0.597994 | Nonzero side forces and moments                              |
| Same baseline, 20 mm                            | 0.583297 | −2.46% drag change; symmetry fails                           |
| Same baseline, 15 mm                            | 0.539508 | Another −7.51%; symmetry fails, not demonstrated convergence |
| Corrected-surface clipped-delta baseline, 20 mm | 0.593827 | Cs 0.022699, yaw moment 0.102051; symmetry fails             |

The last row is different geometry/surface preparation, not a fourth point on the preceding grid curve. Check actual
case specs/hashes before comparisons. `cfd_compare.py` rejects mismatched geometry, physics and force references.

The surface generator once produced 22 open edges with relative tessellation at a thin fin/collar junction. Explicit 10
micrometre absolute tessellation fixed closure for prepared cases, but did NOT fix the aerodynamic asymmetry. Finer
tessellation was not monotonically better. Preserve the hard manifold/closure gate and regression tests.

The old meshes have level-four surface refinement and no inflation layers. The initial baseline reported average y-plus
around 65, with a broad range; neither a universal wall-resolved nor a validated wall-function treatment is established.
Do not confuse small residuals, mesh-check success or surface closure with aerodynamic accuracy.

## Ordered work and acceptance gates

1. **Read-only diagnosis first.** Verify meters versus millimeters, surface normals, geometry/mesh symmetry, closed body
   construction, flow and boundary conditions, force-patch selection, area/length and moment origin. Read the actual
   force-output headers: the existing basis reports drag +X, lift +Y, side −Z and pitch about −Z; do not infer signs
   solely from input keywords. Use an axisymmetric control case and mirrored/rotated geometry/mesh diagnostics to
   isolate implementation bias from the fin configuration. Test transformations and moment translation.
2. **Choose experimental benchmarks before tuning.** Find primary published data with geometry, Reynolds/Mach number,
   boundary conditions and experimental uncertainty. A wall/turbulence benchmark can validate one subsystem; it does not
   validate an entire finned rocket. Add an appropriate external-body force/pressure benchmark. Cite sources, preserve
   input/data provenance and decide comparison quantities and tolerances before seeing solver results.
3. **Verify numerical behavior.** Separate iterative, mesh, near-wall, domain and scheme/turbulence sensitivity. Use
   three systematically refined meshes with measured cell counts and local resolution, not background spacing alone.
   Choose a justified wall treatment and document y-plus distribution. Avoid a nominal GCI/Richardson result unless the
   assumptions and convergence behavior support it. Retain oscillations and failed runs; investigate whether steady RANS
   is appropriate instead of hiding unsteadiness with averaging.
4. **Acceptance is evidence-dependent.** Existing diagnostic screens are last-100 peak-to-peak <= max(0.001, 1% of
   coefficient mean), and absolute zero-angle lateral/moment coefficients <= 0.01. These are provisional screens, not
   experimental uncertainty bounds. Do not loosen them merely to pass. Benchmark agreement must be assessed against
   experimental and numerical uncertainty; predeclare any engineering accuracy targets and explain them. No finite
   universal drag tolerance establishes validity for every condition.
5. **Return to the conventional rocket.** With the numerical/benchmark gates satisfied, compare appropriately normalized
   drag and restoring moments with OpenRocket at relevant speeds and angles. An initial proposed matrix is 20/40/60 m/s
   and 0/2/5 degrees; confirm Reynolds/Mach coverage against the actual flights. Separate cross-model agreement from
   experimental validation, and flag simplified lugs, collar, base/nozzle and surface roughness.
6. **Only then rank novel fins.** Ring tails add 3.55/7.10 g in the 5/10 mm CAD trials. Their flight benefit is unknown.
   Include mass, stability, recovery, printability and uncertainty when comparing them; do not use drag alone.

Record an explicit acceptance matrix and a concise verdict per gate. A failed benchmark or unresolved symmetry is a
result to document, not permission to call the workflow validated. If acceptance requires materially different scope or
resources, explain the issue and request a decision. Never claim physical validation of this particular rocket.

## Deliverables and stopping point

Produce reproducible cases, environment/image provenance, automated integrity and physics checks, cited benchmark data,
mesh/wall/domain studies, force/moment comparisons, and readable reports with machine-readable outputs. Publish only
after authorization on the destination. Keep raw heavy CFD data out of Git unless explicitly asked; commit small
reproduction inputs/scripts, tests and curated evidence. Stop for user review when the declared validation scope is
actually supported, or an essential decision is required—not merely when the solver completes.

Primary methodological reference:
[NASA/NPARC verification and validation tutorial](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html).
Existing reports: `docs/FIN_SHAPES.md`, `cfd/README.md`, and the three-grid/corrected-surface audit snapshots in
`docs-evidence/runs/`. The D12 review is a separate provisional flight/CAD result, not CFD validation.
