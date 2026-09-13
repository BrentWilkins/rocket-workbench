# Rocket Workbench report

Run: `ogive-n50-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `3ea51953d8bb72ada4710afb52f0768bb1d07028aa9c88321368964f9efdabae`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.03 |      6.57 |           2.17 | unavailable |       10.68 |    0.32 |            5.30 |             6.30 |              8.31 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.00 |      6.56 |           1.07 | unavailable |       10.06 |    0.22 |            5.30 |             6.30 |              8.28 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.79 |      8.28 |           2.05 |       16.03 |        5.33 |    0.04 |            7.12 |             8.11 |             16.99 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.95 |      8.27 |           1.23 | unavailable |       20.51 |    9.89 |            7.11 |             8.11 |             16.76 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.48 |      9.05 |           2.01 |        1.65 |        4.85 |    0.04 |            7.76 |             8.76 |             34.64 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.27 |      9.05 |           1.46 |        6.60 |        4.85 |    4.78 |            7.75 |             8.75 |             34.49 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.49 |      9.05 |           1.90 |       12.59 |        4.85 |    0.54 |            7.76 |             8.76 |             34.64 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.27 |      9.05 |           1.46 |       19.06 |        4.85 |   14.83 |            7.75 |             8.75 |             34.49 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.72 |     13.14 |           1.37 |        4.51 |        4.85 |    0.01 |           11.73 |            12.73 |             26.65 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    69.91 |     13.13 |           1.57 |        5.87 |        4.85 |   10.48 |           11.72 |            12.72 |             26.49 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.16 |      5.66 |           2.61 | unavailable |        9.73 |    0.15 |            4.57 |             5.57 |              6.68 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.15 |      5.65 |           1.54 | unavailable |        9.29 |    0.22 |            4.57 |             5.57 |              6.66 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.72 |      7.32 |           2.58 | unavailable |       16.22 |    0.74 |            6.19 |             7.19 |             14.04 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.96 |      7.32 |           1.81 | unavailable |       18.09 |    8.31 |            6.19 |             7.19 |             13.79 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.17 |      8.12 |           2.39 |        2.18 |        5.16 |    0.03 |            6.78 |             7.78 |             29.32 |
| dummy-C6-3-wind2  | completed / outside configured limits |    65.55 |      8.11 |           1.89 |        8.08 |        5.16 |    7.15 |            6.78 |             7.78 |             29.22 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.17 |      8.12 |           2.39 |       17.34 |        5.16 |    1.26 |            6.78 |             7.78 |             29.32 |
| dummy-C6-5-wind2  | completed / outside configured limits |    65.55 |      8.11 |           1.89 |       22.83 |        5.16 |   30.60 |            6.78 |             7.78 |             29.22 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.13 |     12.40 |           2.28 |        8.17 |        5.17 |    0.14 |           10.31 |            11.31 |             22.06 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.08 |     12.39 |           2.07 |        9.67 |        5.17 |    0.50 |           10.30 |            11.30 |             21.91 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.16 |      5.66 |           2.61 | unavailable |        9.73 |    0.15 |            4.57 |             5.57 |              6.68 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.15 |      5.65 |           1.54 | unavailable |        9.29 |    0.22 |            4.57 |             5.57 |              6.66 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.72 |      7.32 |           2.58 | unavailable |       16.22 |    0.74 |            6.19 |             7.19 |             14.04 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.96 |      7.32 |           1.81 | unavailable |       18.09 |    8.31 |            6.19 |             7.19 |             13.79 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.17 |      8.12 |           2.39 |        2.18 |        5.16 |    0.03 |            6.78 |             7.78 |             29.32 |
| actual-C6-3-wind2 | completed / outside configured limits |    65.55 |      8.11 |           1.89 |        8.08 |        5.16 |    7.15 |            6.78 |             7.78 |             29.22 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.17 |      8.12 |           2.39 |       17.34 |        5.16 |    1.26 |            6.78 |             7.78 |             29.32 |
| actual-C6-5-wind2 | completed / outside configured limits |    65.55 |      8.11 |           1.89 |       22.83 |        5.16 |   30.60 |            6.78 |             7.78 |             29.22 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.13 |     12.40 |           2.28 |        8.17 |        5.17 |    0.14 |           10.31 |            11.31 |             22.06 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.08 |     12.39 |           2.07 |        9.67 |        5.17 |    0.50 |           10.30 |            11.30 |             21.91 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.8 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.8 m/s): "Nominal 457 mm parachute and lines"
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings

## Missing measurements / physical checks

- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: 18 mm motor mount tube, thrust ring, hook, two centering rings and adhesive
- Measured mass and balance: Nominal 457 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks
- V2 saddle bond strength and adhesive mass require physical checks; saddle-specific aerodynamic drag is unresolved
- Avionics board/antenna/battery masses, stack clearances, retention, wiring and power must be measured; vendor CAD is
  not physical validation
- Static-port drilling/alignment, bulkhead and screw seals, pressure lag and aerodynamic pressure bias require
  bench/flight validation

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=158.5923871264199 g (allowed None … 85.0); apogee_m=7.034611743390924 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.567612304823352 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.6778041304333 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=158.5923871264199 g (allowed None … 85.0); apogee_m=6.998657473515858 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.561106829436491 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.056627700256445 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=161.1423871264199 g (allowed None … 99.0); apogee_m=24.792285402320385 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.28023192439915 m/s (allowed 12.0 … None); deployment_speed_m_s=16.033975249761184 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=161.1423871264199 g (allowed None … 99.0); apogee_m=23.952302358070924 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.273236311072035 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=20.510207456099753 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=165.3423871264199 g (allowed None … 113.0); guide_departure_m_s=9.052089059420352 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=165.3423871264199 g (allowed None … 113.0); guide_departure_m_s=9.045398302626975 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=165.3423871264199 g (allowed None … 113.0); guide_departure_m_s=9.052089059420352 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.59230770860679 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=165.3423871264199 g (allowed None … 113.0); guide_departure_m_s=9.045398302626975 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.058714649956162 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=179.2423871264199 g (allowed None … 85.0); apogee_m=5.164801275711603 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.656989245820221 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.72947119279474 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=179.2423871264199 g (allowed None … 85.0); apogee_m=5.154281082656766 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.651598142275072 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.286534950064443 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=181.7923871264199 g (allowed None … 99.0); apogee_m=18.724853747693867 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.321291915689283 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.223208637632236 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=181.7923871264199 g (allowed None … 99.0); apogee_m=17.960820783463234 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.315248638860712 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.09416221899629 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.120875213816667 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.114978907185584 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.120875213816667 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.341151460043605 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.114978907185584 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.833298454947847 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=179.2423871264199 g (allowed None … 85.0); apogee_m=5.164801275711603 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.656989245820221 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.72947119279474 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=179.2423871264199 g (allowed None … 85.0); apogee_m=5.154281082656766 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.651598142275072 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.286534950064443 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=181.7923871264199 g (allowed None … 99.0); apogee_m=18.724853747693867 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.321291915689283 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.223208637632226 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=181.7923871264199 g (allowed None … 99.0); apogee_m=17.960820783463234 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.315248638860712 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.094162218996605 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.120875213816667 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.114978907185584 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.120875213816667 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.3411514600436 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=185.9923871264199 g (allowed None … 113.0); guide_departure_m_s=8.114978907185584 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.83329845494805 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is
  scenario-dependent.
- Native OpenRocket aerodynamics; configured axisymmetric nose, cylindrical sections, three flat trapezoidal fins and
  tapered collar fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in
  collar override.
- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful
  view.
- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using
  (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.
- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground
  event, not a structural impact assessment.
- Powered peaks use positive-thrust samples from liftoff strictly before first burnout, deployment, abort or ground
  contact. Missing events/data yield unavailable metrics; peak times and sample coverage are in JSON. These are sampled
  single-stage maxima, not continuous-time bounds.
- Powered acceleration is trajectory acceleration magnitude / 9.80665. Estimated load is hypot(lateral acceleration,
  vertical acceleration + local gravity) / 9.80665 at the center of mass. Coriolis correction, sensor-offset rotation,
  vibration and deployment/impact shock are excluded; this is not a per-axis IMU prediction or a hardware survival
  rating.
- Recovery is motor-ejection deployment with configured Cd; packing envelope, ejection seal, thermal protection and
  attachment loads require physical checks.
- Reference mode preserves upstream geometry and masses; demonstration CAD and baseline mass assumptions do not apply to
  that reference.

## Configured criteria

- apogee_m: 30.0 … 120.0 m; engineering assumption; Project engineering assumption for demonstration screening; not a
  launch clearance
- guide_departure_m_s: 12.0 … None m/s; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance
- minimum_ascent_stability_cal: 1.0 … None cal; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance
- deployment_speed_m_s: None … 10.0 m/s; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance
- landing_descent_m_s: None … 6.0 m/s; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance

## Reproducibility

```json
{
  "openrocket": "24.12",
  "java": "21.0.3+7-LTS-152",
  "python": "3.14.6",
  "bridge_revision": "fb132c49e661bb00c5586cce6a4ac0c655425197",
  "jar_sha256": "4959b72f52f5f607941e9722abbb7b7f0c4a38ebbbf84204a329db9f31c4f897",
  "packages": {
    "orhelper": "0.1.5",
    "jpype1": "1.7.1",
    "numpy": "2.5.3",
    "pydantic": "2.13.5",
    "cadquery": "2.8.0"
  },
  "repository_revision": "d2e7da5d4632c052bc516be47ba0e99b609fb176"
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
