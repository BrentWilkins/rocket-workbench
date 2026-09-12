# Bounded nose comparison

The best fit-check candidate from this search is the **50 mm cone**, not a claim of globally optimal aerodynamics. It
removes 20 mm and approximately 1.26 g from the 70 mm cone while preserving the 65 mm internal bay. The existing body,
fins, revised lug saddles, and 18-inch parachute remain unchanged.

## Scope and outcome

We tested conical, tangent-ogive, and ellipsoidal noses at 50, 70, and 90 mm. Each design used the same C5-3 curve,
three loadings, and winds 0/2 m/s: **54 nominal simulations**. All nine designs met the nominal numerical gates. We did
not maximize altitude: the goal remains the configured 30–120 m flight envelope with adequate margins.

The three short candidates received the same 72-case sensitivity study each: print mass +0/+20%, payload CG offset ±5
mm, chute Cd 0.6/0.9, winds 0/2/4 m/s, and all three loadings. These are deliberate corner cases, not probabilities.
Purchased adhesive/mount mass variation and saddle drag remain unresolved.

| Nose                | Printed nose/bay mass | Nominal cases |        Stress cases meeting gates | Interpretation                                                                        |
| ------------------- | --------------------: | ------------: | --------------------------------: | ------------------------------------------------------------------------------------- |
| 50 mm cone          |               16.13 g |           6/6 |                             72/72 | Lightest and shortest of the tested cones; preferred fit-check candidate              |
| 70 mm cone          |               17.38 g |           6/6 | 72/72 in preceding saddle recheck | Existing baseline; no compelling nominal advantage from the extra length              |
| 50 mm tangent ogive |               19.10 g |           6/6 |                             64/72 | Better nominal minimum stability, but fails the deployment-speed gate in stress cases |
| 50 mm ellipsoid     |               20.47 g |           6/6 |                             64/72 | Rounded alternative, but heavier and fails the deployment-speed gate in stress cases  |

- [All nine candidates](../runs/nose-study-20260912T225633Z/report.md)
- [50 mm cone stress report](../runs/stress-20260912T225746Z-07a27129/report.md)
- [50 mm ogive stress report](../runs/stress-20260912T225842Z-effd8a91/report.md)
- [50 mm ellipsoid stress report](../runs/stress-20260912T225747Z-ffb7a9c8/report.md)
- [50 mm cone STEP](../runs/nose-study-20260912T225633Z/nose-conical-50/cad/nose-bay.step)
- [50 mm cone STL](../runs/nose-study-20260912T225633Z/nose-conical-50/cad/nose-bay.stl)
- [50 mm cone loaded flight model](../runs/nose-study-20260912T225633Z/nose-conical-50/actual-C5-3-wind2.ork)

A local **nose-only**, unsliced X1C/0.4 mm/PLA/Textured PEI project is in `deliverables/nose-conical-50-fit-check/`. It
intentionally excludes the fin assembly whose print orientation needs review. No physical print, fit, strength, or
flight qualification is implied.

## Geometry and verification

Curved outer profiles use smooth CAD splines sampled from analytic ogive/ellipse equations, then revolved. Tests compare
CAD volume against independent cross-section integration and compare radius stations against the loaded/saved OpenRocket
component. The existing conical CAD retains its 0.01 mm tip radius. The hollow interior uses the same profile family
with reduced radius and length, shifted aft by twice the wall parameter; this is not a mathematically
constant-normal-thickness shell. All candidates use that declared shell construction rule. Mass/CG comes from the actual
CAD solids, not an assumed equal mass between profiles. Every purchased component and payload CG shifts with the
changing tip origin, keeping its position relative to the bay/body.

The finite search does not prove optimality, and has not explored other thickness rules, coatings, rounded cone tips,
shape parameters, more lengths, or different motors. Geometric feasibility is not printability; see the orientation
study.

## Current OpenRocket and CFD

As checked on 2026-09-12, the [official latest stable release](https://github.com/openrocket/openrocket/releases/latest)
is still **24.12**. The workbench already has an adapter for it, pinned by JAR checksum and bridge revision. There is no
newer stable-release adapter to add at present.

[Issue #2998](https://github.com/openrocket/openrocket/issues/2998) and
[fix #2999](https://github.com/openrocket/openrocket/pull/2999) document a tangent-ogive pressure-drag correction in
development after the pinned release. Ogive results here use unmodified 24.12 and carry that limitation. Do not treat
small shape-dependent performance differences as definitive.

**No CFD or machine move is needed for this decision.** The bounded system-level comparison already identifies mass and
deployment margins that matter more to this selection than claiming a tiny drag advantage. A future CFD study should
answer a named question (for example, saddle drag or a close profile comparison), with documented speed/Reynolds/AOA
conditions, domain/mesh convergence, turbulence/transition assumptions, and a benchmark. A faster computer does not
replace that validation. A pinned development engine could be evaluated separately before CFD; it must pass adapter
acceptance checks without overwriting the stable baseline.
