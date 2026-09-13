# Rocket Workbench report

Run: `conical-n70-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `f0cc85a5bec29970149276cb6f74cb89002b32a16bfb539016a21e69c47b213b`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.38 |      6.72 |           1.96 | unavailable |       10.98 |    0.33 |            5.43 |             6.43 |              8.59 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.34 |      6.71 |           0.86 | unavailable |       10.27 |    0.43 |            5.43 |             6.43 |              8.56 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.82 |      8.43 |           1.88 |       13.39 |        4.79 |    2.53 |            7.28 |             8.27 |             17.48 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.03 |      8.42 |           0.94 |       19.27 |        6.70 |    9.81 |            7.27 |             8.27 |             17.25 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.75 |      9.17 |           1.82 |        1.98 |        4.80 |    0.04 |            7.93 |             8.92 |             35.41 |
| empty-C6-3-wind2  | completed / outside configured limits |    86.91 |      9.16 |           1.25 |        6.19 |        4.80 |    7.99 |            7.92 |             8.92 |             35.24 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.78 |      9.17 |           1.37 |       12.02 |        4.80 |    1.28 |            7.93 |             8.92 |             35.41 |
| empty-C6-5-wind2  | completed / outside configured limits |    86.92 |      9.16 |           1.25 |       18.43 |        4.80 |   10.33 |            7.92 |             8.92 |             35.24 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.88 |     13.21 |           1.42 |        4.10 |        4.81 |    0.02 |           11.97 |            12.97 |             27.29 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    72.14 |     13.20 |           1.26 |        5.33 |        4.81 |   12.54 |           11.96 |            12.96 |             27.12 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.40 |      5.77 |           2.45 | unavailable |        9.99 |    0.15 |            4.67 |             5.67 |              6.90 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.39 |      5.78 |           1.35 | unavailable |        9.36 |    0.30 |            4.67 |             5.67 |              6.88 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.47 |      7.46 |           2.27 | unavailable |       16.29 |    0.57 |            6.31 |             7.31 |             14.43 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.77 |      7.46 |           1.56 | unavailable |       18.32 |    7.99 |            6.31 |             7.31 |             14.19 |
| dummy-C6-3-wind0  | completed / outside configured limits |    72.19 |      8.22 |           2.21 |        1.79 |        5.11 |    0.03 |            6.91 |             7.91 |             29.97 |
| dummy-C6-3-wind2  | completed / outside configured limits |    67.90 |      8.21 |           1.69 |        7.47 |        5.11 |    4.37 |            6.91 |             7.91 |             29.85 |
| dummy-C6-5-wind0  | completed / outside configured limits |    72.19 |      8.22 |           2.21 |       16.56 |        5.11 |    0.87 |            6.91 |             7.91 |             29.97 |
| dummy-C6-5-wind2  | completed / outside configured limits |    67.90 |      8.21 |           1.69 |       22.19 |        5.11 |   26.64 |            6.91 |             7.91 |             29.85 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.92 |     12.48 |           2.23 |        7.78 |        5.12 |    0.10 |           10.50 |            11.50 |             22.61 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.97 |     12.47 |           1.87 |        9.09 |        5.12 |    1.33 |           10.49 |            11.49 |             22.46 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.40 |      5.77 |           2.45 | unavailable |        9.99 |    0.15 |            4.67 |             5.67 |              6.90 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.39 |      5.78 |           1.35 | unavailable |        9.36 |    0.30 |            4.67 |             5.67 |              6.88 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.47 |      7.46 |           2.27 | unavailable |       16.29 |    0.57 |            6.31 |             7.31 |             14.43 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.77 |      7.46 |           1.56 | unavailable |       18.32 |    7.99 |            6.31 |             7.31 |             14.19 |
| actual-C6-3-wind0 | completed / outside configured limits |    72.19 |      8.22 |           2.21 |        1.79 |        5.11 |    0.03 |            6.91 |             7.91 |             29.97 |
| actual-C6-3-wind2 | completed / outside configured limits |    67.90 |      8.21 |           1.69 |        7.47 |        5.11 |    4.37 |            6.91 |             7.91 |             29.85 |
| actual-C6-5-wind0 | completed / outside configured limits |    72.19 |      8.22 |           2.21 |       16.56 |        5.11 |    0.87 |            6.91 |             7.91 |             29.97 |
| actual-C6-5-wind2 | completed / outside configured limits |    67.90 |      8.21 |           1.69 |       22.19 |        5.11 |   26.64 |            6.91 |             7.91 |             29.85 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.92 |     12.48 |           2.23 |        7.78 |        5.12 |    0.10 |           10.50 |            11.50 |             22.61 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.97 |     12.47 |           1.87 |        9.09 |        5.12 |    1.33 |           10.49 |            11.49 |             22.46 |

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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.2 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (22.2 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=155.49195587730776 g (allowed None … 85.0); apogee_m=7.378606532212038 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.717180574368516 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.978470064296811 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=155.49195587730776 g (allowed None … 85.0); apogee_m=7.344865479491873 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.710190261882487 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8631738489749784 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.270916957661406 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=158.04195587730777 g (allowed None … 99.0); apogee_m=25.82211604948627 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.426870479277454 m/s (allowed 12.0 … None); deployment_speed_m_s=13.392228934333211 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=158.04195587730777 g (allowed None … 99.0); apogee_m=25.031630341818428 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.419476272183106 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9411892649310247 cal (allowed 1.0 … None); deployment_speed_m_s=19.27170299120555 m/s
  (allowed None … 10.0); landing_descent_m_s=6.696866064880757 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=162.2419558773078 g (allowed None … 113.0); guide_departure_m_s=9.167086190417963 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=162.2419558773078 g (allowed None … 113.0); guide_departure_m_s=9.16006762119375 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=162.2419558773078 g (allowed None … 113.0); guide_departure_m_s=9.167086190417963 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.023631664572509 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=162.2419558773078 g (allowed None … 113.0); guide_departure_m_s=9.16006762119375 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.43330120707557 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=176.14195587730777 g (allowed None … 85.0); apogee_m=5.39907519250868 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.774189546373305 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.991375556933784 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=176.14195587730777 g (allowed None … 85.0); apogee_m=5.386877350078938 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.780025920251697 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.359408489369619 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=178.69195587730778 g (allowed None … 99.0); apogee_m=19.47301531085778 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.462770169675041 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.292186780395976 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=178.69195587730778 g (allowed None … 99.0); apogee_m=18.770072175199804 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4562601931861385 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.31824995777124 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.218807807493594 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.212612101301138 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.218807807493594 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.558299432066562 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.212612101301138 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.194939446593597 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=176.14195587730777 g (allowed None … 85.0); apogee_m=5.39907519250868 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.774189546373305 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.991375556933784 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=176.14195587730777 g (allowed None … 85.0); apogee_m=5.386877350078938 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.780025920251697 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.359408489369619 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=178.69195587730778 g (allowed None … 99.0); apogee_m=19.47301531085778 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.462770169675041 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.292186780395976 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=178.69195587730778 g (allowed None … 99.0); apogee_m=18.770072175199804 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4562601931861385 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.318249957771275 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.218807807493594
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.212612101301138
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.218807807493594
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.55829943205021 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=182.89195587730777 g (allowed None … 113.0); guide_departure_m_s=8.212612101301138
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.19493944659361 m/s (allowed None … 10.0)
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
