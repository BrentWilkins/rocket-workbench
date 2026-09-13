# Rocket Workbench report

Run: `ogive-n50-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `470c93f70cc07661c024fd95a2f3d594ebd2d1de0971c8008aff43711a2b4481`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.19 |      6.63 |           1.88 | unavailable |       10.92 |    0.31 |            5.36 |             6.36 |              8.44 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.16 |      6.63 |           0.92 | unavailable |       10.16 |    0.38 |            5.36 |             6.36 |              8.41 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.33 |      8.34 |           1.95 |       12.59 |        4.82 |    1.61 |            7.19 |             8.19 |             17.23 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.54 |      8.33 |           1.00 |       19.81 |       10.51 |    9.83 |            7.18 |             8.18 |             17.00 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.43 |      9.10 |           1.86 |        2.09 |        4.83 |    0.04 |            7.83 |             8.83 |             35.13 |
| empty-C6-3-wind2  | completed / outside configured limits |    86.47 |      9.09 |           1.29 |        6.43 |        4.83 |    6.95 |            7.83 |             8.83 |             34.97 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.46 |      9.10 |           1.53 |       12.05 |        4.83 |    1.05 |            7.83 |             8.83 |             35.13 |
| empty-C6-5-wind2  | completed / outside configured limits |    86.50 |      9.09 |           1.29 |       18.54 |        4.83 |   11.81 |            7.83 |             8.83 |             34.97 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.31 |     13.05 |           1.31 |        4.11 |        4.83 |    0.01 |           11.84 |            12.84 |             27.08 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    71.53 |     13.04 |           1.36 |        5.50 |        4.83 |   11.61 |           11.83 |            12.83 |             26.91 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.27 |      5.71 |           2.46 | unavailable |        9.87 |    0.13 |            4.62 |             5.62 |              6.78 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.26 |      5.71 |           1.40 | unavailable |        9.33 |    0.29 |            4.62 |             5.62 |              6.76 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.10 |      7.37 |           2.41 | unavailable |       16.17 |    0.62 |            6.25 |             7.24 |             14.22 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.40 |      7.36 |           1.63 | unavailable |       18.22 |    7.90 |            6.24 |             7.24 |             13.99 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.61 |      8.16 |           2.14 |        1.81 |        5.14 |    0.03 |            6.84 |             7.84 |             29.70 |
| dummy-C6-3-wind2  | completed / outside configured limits |    67.24 |      8.16 |           1.72 |        7.66 |        5.14 |    5.27 |            6.84 |             7.83 |             29.59 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.61 |      8.16 |           2.14 |       16.70 |        5.14 |    1.07 |            6.84 |             7.84 |             29.70 |
| dummy-C6-5-wind2  | completed / outside configured limits |    67.24 |      8.16 |           1.72 |       22.42 |        5.14 |   27.98 |            6.84 |             7.83 |             29.59 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.26 |     12.34 |           2.24 |        7.88 |        5.15 |    0.10 |           10.39 |            11.39 |             22.39 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.28 |     12.34 |           1.90 |        9.29 |        5.15 |    0.52 |           10.39 |            11.39 |             22.25 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.27 |      5.71 |           2.46 | unavailable |        9.87 |    0.13 |            4.62 |             5.62 |              6.78 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.26 |      5.71 |           1.40 | unavailable |        9.33 |    0.29 |            4.62 |             5.62 |              6.76 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.10 |      7.37 |           2.41 | unavailable |       16.17 |    0.62 |            6.25 |             7.24 |             14.22 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.40 |      7.36 |           1.63 | unavailable |       18.22 |    7.90 |            6.24 |             7.24 |             13.99 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.61 |      8.16 |           2.14 |        1.81 |        5.14 |    0.03 |            6.84 |             7.84 |             29.70 |
| actual-C6-3-wind2 | completed / outside configured limits |    67.24 |      8.16 |           1.72 |        7.66 |        5.14 |    5.27 |            6.84 |             7.83 |             29.59 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.61 |      8.16 |           2.14 |       16.70 |        5.14 |    1.07 |            6.84 |             7.84 |             29.70 |
| actual-C6-5-wind2 | completed / outside configured limits |    67.24 |      8.16 |           1.72 |       22.42 |        5.14 |   27.98 |            6.84 |             7.83 |             29.59 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.26 |     12.34 |           2.24 |        7.88 |        5.15 |    0.10 |           10.39 |            11.39 |             22.39 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.28 |     12.34 |           1.90 |        9.29 |        5.15 |    0.52 |           10.39 |            11.39 |             22.25 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.4 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (22.4 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=157.20856437762518 g (allowed None … 85.0); apogee_m=7.192910374214057 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.63286225029199 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.917040587762894 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=157.20856437762518 g (allowed None … 85.0); apogee_m=7.163782893734881 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.626531426771467 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9230902133029045 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.163187179380465 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=159.75856437762516 g (allowed None … 99.0); apogee_m=25.332281107421565 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.33904084990465 m/s (allowed 12.0 … None); deployment_speed_m_s=12.585277093096163
  m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=159.75856437762516 g (allowed None … 99.0); apogee_m=24.539686914033503 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.332292487554433 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.814567179750224 m/s (allowed None … 10.0); landing_descent_m_s=10.514435047995294 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=163.95856437762518 g (allowed None … 113.0); guide_departure_m_s=9.098852947519008 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=163.95856437762518 g (allowed None … 113.0); guide_departure_m_s=9.092417280087677 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=163.95856437762518 g (allowed None … 113.0); guide_departure_m_s=9.098852947519008 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.048345063980113 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=163.95856437762518 g (allowed None … 113.0); guide_departure_m_s=9.092417280087677 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.54354255191897 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=177.85856437762519 g (allowed None … 85.0); apogee_m=5.271127056932075 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.71363492486324 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.867615574563514 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=177.85856437762519 g (allowed None … 85.0); apogee_m=5.261452271847988 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.7084203244450435 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.33153842468115 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=180.40856437762517 g (allowed None … 99.0); apogee_m=19.09692141307722 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.370502631829074 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.16738666309225 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=180.40856437762517 g (allowed None … 99.0); apogee_m=18.3991592881343 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.364666614469407 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.22119184628487 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.160946227562235 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.155265929311252 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.160946227562235 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.697591975165622 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.155265929311252 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.418005916215417 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=177.85856437762519 g (allowed None … 85.0); apogee_m=5.271127056932075 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.71363492486324 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.867615574563514 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=177.85856437762519 g (allowed None … 85.0); apogee_m=5.261452271847988 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.7084203244450435 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=9.33153842468115 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=180.40856437762517 g (allowed None … 99.0); apogee_m=19.09692141307722 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.370502631829074 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.167386663092344 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=180.40856437762517 g (allowed None … 99.0); apogee_m=18.3991592881343 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.364666614469407 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.221191846284878 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.160946227562235
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.155265929311252
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.160946227562235
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.697591975165615 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=184.60856437762519 g (allowed None … 113.0); guide_departure_m_s=8.155265929311252
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.4180059162154 m/s (allowed None … 10.0)
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
