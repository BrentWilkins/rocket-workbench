# TMR NACA 0012 SSTm mapping

This mapping applies only to the compressible TMR NACA 0012 validation path in
the pinned OpenFOAM v2512 package image. It does not establish benchmark
agreement or rocket validity.

## Force and moment convention

OpenFOAM v2512 `forceCoeffs` constructs its local Cartesian frame from
`liftDir` as local e3 and `dragDir` as local e1. The right-handed local e2 is
therefore `liftDir cross dragDir`. For this two-dimensional x-y setup that is
negative global z, exactly as recorded by the generated `coefficient.dat`
header. `CmPitch` is the moment component along that negative-z axis about
quarter chord. Because the airfoil nose lies toward negative x from that
reference point, negative-z rotation raises the nose: `CmPitch` is already
nose-up-positive. The audit checks the recorded pitch axis before comparing
moments; absolute settling and zero-angle symmetry checks are unaffected.

The generator does not write a `pitchAxis` dictionary entry because v2512
derives that axis from `liftDir` and `dragDir`; an explicit entry would be
misleading and is not used by this implementation.

## Governing model

The original runtime class is the same source-derived `TmrSSTm` template accepted for
the flat-plate subsystem. `libTmrSSTmCompressible.so` registers that template
against OpenFOAM's `fluidThermoCompressibleTurbulenceModel`; it does not fork
or reimplement the transport equations. Cases set the accepted SSTm
`gamma1`, `gamma2`, and `c1=20` values explicitly and the solver log must
report them.

The TMR SST page defines the “m” variant by omitting the isotropic
`2/3 rho k` term from the momentum and energy equations. The exact packaged
v2512 source was checked for the compressible registration:

- `rhoSimpleFoam/UEqn.H` assembles momentum with
  `turbulence->divDevRhoReff(U)`.
- `linearViscousStress::divDevRhoReff` contains the effective viscous
  deviatoric terms and no isotropic `k` term.
- `rhoSimpleFoam/EEqn.H` uses convective kinetic/pressure energy and
  `alphaEff` diffusion; it does not add Reynolds-stress work or an isotropic
  `k` term.
- `eddyViscosity::R()` does contain `2/3 k I`, but that diagnostic Reynolds
  tensor is not the momentum operator used by `rhoSimpleFoam`.

The custom `correct()` retains conservation-form compressible transport
through `alpha`, `rho`, and `alphaRhoPhi`, while omitting the generic
v2512 dilatation-source additions, matching the SSTm convention.

The NACA source re-audit found two additional production-equation deltas in
that first compatibility class. OpenFOAM v2512 applies `GbyNu()` before the
omega equation, which limits omega production, while the NASA standard SSTm
reference limits production only in the k equation. NASA also defines the
SSTm approximation as `P = mu_t S^2`; v2512 `GbyNu0()` instead uses the
deviatoric velocity-gradient contraction. The immutable diagnostic class
`TmrSSTmExactProduction` corrects both: unlimited `S^2` production in omega
and `min(P, 20 betaStar rho omega k)` in k. Its converged same-grid result
changes Cd by only -0.00002658 relative to the exact-Pr baseline and leaves a
0.00065851 CFL3D drag gap, so the correction is required for fidelity but is
not the dominant benchmark discrepancy.

## Pinned packaged-source hashes

| Source | SHA-256 |
| --- | --- |
| `linearViscousStress.C` | `f28f4a6bb9a5d4448226fa6407f505808fb2c2840b224a435d36fa898d30ea5f` |
| `eddyViscosity.C` | `4c3340144b68e35576ba46cedfab3e010029a99a76bb864832ab6e4635fe6498` |
| `rhoSimpleFoam/EEqn.H` | `59f0cab95246ea9d88efff8e8455c03668b2acb576d5af24466ece21471101cf` |
| `rhoSimpleFoam/UEqn.H` | `c732faac7af8983ee48cc1576798aaa3ee95e1223b95895c49d685e25f81c471` |

These hashes are evidence for package `openfoam2512-source=2512.0-2` in
compressible image
`sha256:143e0e81aa690349714910f096ef1a2dc5fbc723a27355f5078839503a9b7634`.

## Boundary and condition mapping

The official TMR altered closed-airfoil C-grid is used directly. The paired
wake cut is merged from the supplied neutral-map 3:8:3 index split. The
farfield is approximately 500 chords away. Cases use Mach 0.15, chord Reynolds
number 6 million and perfect-gas thermodynamics. The published CFL3D comparison
uses nominal molecular Prandtl number 0.72, whereas the generated OpenFOAM
Sutherland closure has an effective freestream Prandtl number
0.6903347705666375. A provenance-pinned same-grid sensitivity using exact
Sutherland viscosity and constant `Pr=0.72` passes all solver gates but changes
Cd by only -0.00000588, or 0.83% of the Ladson discrepancy, and changes the
mean OpenFOAM/CFL3D skin-friction ratio from 1.10939 to 1.10736. The mismatch is
therefore not the dominant explanation and correcting it does not accept the
benchmark. The baseline cases use the
published CFL3D comparison inflow definitions `k/a_inf^2 = 9e-9` and
`omega*mu_inf/(rho_inf*a_inf^2) = 1e-6` (equivalently about 0.052% turbulence
intensity and `nut/nu = 0.009`). They use fixed wall
`k=0`, fixed wall `nut=0`, and the factor-10 TMR wall-`omega` formula
evaluated per airfoil face.

The current force cases use Sutherland transport calibrated at 300 K to satisfy
the declared Reynolds number exactly, with the TMR compressible implementation's
`Pr_t = 0.90`. This mapping is recorded in every generated case manifest.
