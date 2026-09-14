# Passive fin aerodynamic cross-check

This branch is under development. No CFD result is currently accepted as design evidence.

The current native ARM64 environment uses OpenCFD OpenFOAM v2512 on Ubuntu 24.04, built with `Dockerfile.2512`. The
image base digest and OpenFOAM packages (2512.0-2) are pinned; transitive Ubuntu dependencies are not independently
locked. Every executed case records the resolved image ID. Keep container CPU/memory limits explicit. Mount only the
individual study directory, never the Docker socket.

For another host, build a native image and pass its tag explicitly with `--image`. The APT source uses the native
package architecture; AMD64 builds still need verification on the destination. The runner sources the explicit
`--openfoam-bashrc` path (default `/usr/lib/openfoam/openfoam2512/etc/bashrc`) independently of image tag. Use an empty
value only for an image whose environment is already configured. The current solver is serial: a Docker CPU quota does
not enable MPI or GPU acceleration. Record architecture, image identity and resource allocation before comparing results
across machines.

The retained v1912 Dockerfile documents the first installation attempt. Its upstream cavity smoke test passed, but the
rocket run failed in function-object initialization. It is not the default solver environment. Failed cases are
retained, including the initial degenerate nose-apex STL and the mesh-quality failure that returned exit status zero.
The runner checks diagnostic text as well as process status so those failures cannot silently become accepted runs.

## Reproduce a diagnostic case

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
