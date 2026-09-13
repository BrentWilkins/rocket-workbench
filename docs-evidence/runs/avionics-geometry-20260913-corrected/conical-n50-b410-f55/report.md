# Rocket Workbench report

Run: `conical-n50-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `d1fb8f1a1646a8131a5b4ac26f6e8e5024f5203cd62cc1d5f338add165258754`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.35 |      6.71 |           2.06 | unavailable |       10.76 |    0.36 |            5.42 |             6.42 |              8.57 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.30 |      6.70 |           1.03 | unavailable |       10.15 |    0.21 |            5.42 |             6.42 |              8.54 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.61 |      8.42 |           1.97 |       15.61 |        4.82 |    0.10 |            7.27 |             8.27 |             17.41 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.74 |      8.41 |           1.22 |       20.34 |       12.89 |    9.87 |            7.27 |             8.27 |             17.17 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.88 |      9.16 |           1.94 |        1.41 |        4.80 |    0.04 |            7.92 |             8.92 |             35.08 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.77 |      9.15 |           1.42 |        6.26 |        4.80 |    6.12 |            7.91 |             8.91 |             34.92 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.89 |      9.16 |           1.70 |       12.61 |        4.80 |    0.51 |            7.92 |             8.92 |             35.08 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.77 |      9.15 |           1.42 |       18.97 |        4.80 |   12.93 |            7.91 |             8.91 |             34.92 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |        4.52 |        4.81 |    0.01 |           11.96 |            12.96 |             26.99 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |        5.70 |        4.81 |   11.84 |           11.95 |            12.95 |             26.82 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.38 |      5.78 |           2.56 | unavailable |        9.84 |    0.16 |            4.67 |             5.67 |              6.88 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.37 |      5.77 |           1.53 | unavailable |        9.39 |    0.17 |            4.67 |             5.67 |              6.86 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.36 |      7.45 |           2.50 | unavailable |       16.59 |    0.82 |            6.31 |             7.31 |             14.38 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.55 |      7.45 |           1.77 | unavailable |       18.31 |    8.55 |            6.31 |             7.31 |             14.13 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.07 |      8.25 |           2.39 |        2.17 |        5.12 |    0.03 |            6.91 |             7.90 |             29.75 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.50 |      8.24 |           1.87 |        7.82 |        5.12 |    5.92 |            6.90 |             7.90 |             29.63 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.07 |      8.25 |           2.39 |       17.28 |        5.12 |    1.23 |            6.91 |             7.90 |             29.75 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.50 |      8.24 |           1.87 |       22.50 |        5.12 |   28.75 |            6.90 |             7.90 |             29.63 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.18 |     12.47 |           1.75 |        8.02 |        5.12 |    0.13 |           10.49 |            11.49 |             22.41 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.15 |     12.46 |           2.04 |        9.41 |        5.12 |    0.68 |           10.48 |            11.48 |             22.25 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.38 |      5.78 |           2.56 | unavailable |        9.84 |    0.16 |            4.67 |             5.67 |              6.88 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.37 |      5.77 |           1.53 | unavailable |        9.39 |    0.17 |            4.67 |             5.67 |              6.86 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.36 |      7.45 |           2.50 | unavailable |       16.59 |    0.82 |            6.31 |             7.31 |             14.38 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.55 |      7.45 |           1.77 | unavailable |       18.31 |    8.55 |            6.31 |             7.31 |             14.13 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.07 |      8.25 |           2.39 |        2.17 |        5.12 |    0.03 |            6.91 |             7.90 |             29.75 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.50 |      8.24 |           1.87 |        7.82 |        5.12 |    5.92 |            6.90 |             7.90 |             29.63 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.07 |      8.25 |           2.39 |       17.28 |        5.12 |    1.23 |            6.91 |             7.90 |             29.75 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.50 |      8.24 |           1.87 |       22.50 |        5.12 |   28.75 |            6.90 |             7.90 |             29.63 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.18 |     12.47 |           1.75 |        8.02 |        5.12 |    0.13 |           10.49 |            11.49 |             22.41 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.15 |     12.46 |           2.04 |        9.41 |        5.12 |    0.68 |           10.48 |            11.48 |             22.25 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Recovery device deployment at high speed (20.3 m/s): "Nominal 457 mm parachute and lines"
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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.5 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (22.5 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=155.6164171755174 g (allowed None … 85.0); apogee_m=7.349516689346761 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.707919892726095 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.764886246922348 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=155.6164171755174 g (allowed None … 85.0); apogee_m=7.300620794318915 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.700222824827839 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.150735931966958 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=158.16641717551738 g (allowed None … 99.0); apogee_m=25.607648640645127 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.416384462095527 m/s (allowed 12.0 … None); deployment_speed_m_s=15.60912969760064
  m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=158.16641717551738 g (allowed None … 99.0); apogee_m=24.743621153826464 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.408321930279248 m/s (allowed 12.0 … None);
  deployment_speed_m_s=20.340234711611483 m/s (allowed None … 10.0); landing_descent_m_s=12.88726728930536 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=162.3664171755174 g (allowed None … 113.0); guide_departure_m_s=9.156224760073432 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=162.3664171755174 g (allowed None … 113.0); guide_departure_m_s=9.148480508590959 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=162.3664171755174 g (allowed None … 113.0); guide_departure_m_s=9.156224760073432 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.609503382218858 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=162.3664171755174 g (allowed None … 113.0); guide_departure_m_s=9.148480508590959 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.968248528618275 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=176.26641717551738 g (allowed None … 85.0); apogee_m=5.382609007746974 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.7783291614661 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=9.842544130563674 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=176.26641717551738 g (allowed None … 85.0); apogee_m=5.366294689323653 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.771935985010656 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.390296409158523 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=178.8164171755174 g (allowed None … 99.0); apogee_m=19.356855280903666 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.4542869574816555 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.591988345643678 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=178.8164171755174 g (allowed None … 99.0); apogee_m=18.553161834577388 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.4471111152991725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.312501077503835 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.25057197374773 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.243594094965925 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.25057197374773 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.278467973009583 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.243594094965925 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.50457660008101 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=176.26641717551738 g (allowed None … 85.0); apogee_m=5.382609007746974 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.7783291614661 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.842544130563674 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=176.26641717551738 g (allowed None … 85.0); apogee_m=5.366294689323653 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.771935985010656 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.390296409158521 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=178.8164171755174 g (allowed None … 99.0); apogee_m=19.356855280903666 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4542869574816555 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=16.591988345643685 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=178.8164171755174 g (allowed None … 99.0); apogee_m=18.553161834577377 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4471111152991725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.312501077504198 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.25057197374773 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.243594094965925 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.25057197374773 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.27846797300958 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=183.0164171755174 g (allowed None … 113.0); guide_departure_m_s=8.243594094965925 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.504576600081062 m/s (allowed None … 10.0)
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
