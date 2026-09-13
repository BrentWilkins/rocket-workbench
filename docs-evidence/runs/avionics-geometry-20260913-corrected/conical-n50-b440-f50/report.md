# Rocket Workbench report

Run: `conical-n50-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `36b3d9edfc07132731f1094e8b2ad1b27434e96b62f2c09c54b58db3d00abcd7`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.34 |      6.70 |           2.17 | unavailable |       10.94 |    0.32 |            5.42 |             6.42 |              8.56 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.30 |      6.69 |           1.04 | unavailable |       10.20 |    0.40 |            5.42 |             6.42 |              8.53 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.59 |      8.41 |           2.09 |       13.48 |        4.80 |    0.18 |            7.26 |             8.26 |             17.40 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.80 |      8.40 |           1.13 |       19.61 |        8.86 |    9.52 |            7.26 |             8.26 |             17.16 |
| empty-C6-3-wind0  | completed / outside configured limits |    89.07 |      9.15 |           2.07 |        1.48 |        4.80 |    0.04 |            7.91 |             8.91 |             35.10 |
| empty-C6-3-wind2  | completed / outside configured limits |    85.27 |      9.19 |           1.45 |        5.97 |        4.80 |    7.69 |            7.91 |             8.90 |             34.93 |
| empty-C6-5-wind0  | completed / outside configured limits |    89.08 |      9.15 |           1.53 |       12.23 |        4.80 |    0.89 |            7.91 |             8.91 |             35.10 |
| empty-C6-5-wind2  | completed / outside configured limits |    85.27 |      9.19 |           1.45 |       18.73 |        4.80 |   10.60 |            7.91 |             8.90 |             34.93 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    72.70 |     13.19 |           1.79 |        4.47 |        4.81 |    0.01 |           11.95 |            12.95 |             27.01 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.96 |     13.18 |           1.47 |        5.57 |        4.81 |   12.17 |           11.94 |            12.94 |             26.83 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.37 |      5.77 |           2.72 | unavailable |        9.94 |    0.14 |            4.66 |             5.66 |              6.88 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.36 |      5.77 |           1.57 | unavailable |        9.38 |    0.31 |            4.66 |             5.66 |              6.86 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.34 |      7.45 |           2.65 | unavailable |       16.19 |    0.72 |            6.30 |             7.30 |             14.37 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.64 |      7.44 |           1.80 | unavailable |       18.21 |    7.76 |            6.30 |             7.30 |             14.13 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.16 |      8.24 |           2.27 |        2.12 |        5.12 |    0.03 |            6.90 |             7.90 |             29.76 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.93 |      8.24 |           1.93 |        7.45 |        5.12 |    4.32 |            6.90 |             7.90 |             29.63 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.16 |      8.24 |           2.27 |       16.87 |        5.12 |    1.23 |            6.90 |             7.90 |             29.76 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.93 |      8.24 |           1.93 |       22.31 |        5.12 |   26.41 |            6.90 |             7.90 |             29.63 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.21 |     12.46 |           2.22 |        8.01 |        5.13 |    0.11 |           10.48 |            11.48 |             22.42 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.27 |     12.45 |           2.12 |        9.26 |        5.13 |    1.21 |           10.47 |            11.47 |             22.27 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.37 |      5.77 |           2.72 | unavailable |        9.94 |    0.14 |            4.66 |             5.66 |              6.88 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.36 |      5.77 |           1.57 | unavailable |        9.38 |    0.31 |            4.66 |             5.66 |              6.86 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.34 |      7.45 |           2.65 | unavailable |       16.19 |    0.72 |            6.30 |             7.30 |             14.37 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.64 |      7.44 |           1.80 | unavailable |       18.21 |    7.76 |            6.30 |             7.30 |             14.13 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.16 |      8.24 |           2.27 |        2.12 |        5.12 |    0.03 |            6.90 |             7.90 |             29.76 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.93 |      8.24 |           1.93 |        7.45 |        5.12 |    4.32 |            6.90 |             7.90 |             29.63 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.16 |      8.24 |           2.27 |       16.87 |        5.12 |    1.23 |            6.90 |             7.90 |             29.76 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.93 |      8.24 |           1.93 |       22.31 |        5.12 |   26.41 |            6.90 |             7.90 |             29.63 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.21 |     12.46 |           2.22 |        8.01 |        5.13 |    0.11 |           10.48 |            11.48 |             22.42 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.27 |     12.45 |           2.12 |        9.26 |        5.13 |    1.21 |           10.47 |            11.47 |             22.27 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (16.2°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.3 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (16.2°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.3 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=155.73259442672267 g (allowed None … 85.0); apogee_m=7.338614841429144 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.701154594402646 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.939605896952962 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=155.73259442672267 g (allowed None … 85.0); apogee_m=7.302612643261626 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.693596776619148 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.195892365230057 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=158.28259442672265 g (allowed None … 99.0); apogee_m=25.593825049380108 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.408326104994424 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.481171988180872 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=158.28259442672265 g (allowed None … 99.0); apogee_m=24.796143000621864 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.401027468553128 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.610481506251688 m/s (allowed None … 10.0); landing_descent_m_s=8.859430499007798 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=162.48259442672267 g (allowed None … 113.0); guide_departure_m_s=9.148355844385556 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=162.48259442672267 g (allowed None … 113.0); guide_departure_m_s=9.191848164269631 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=162.48259442672267 g (allowed None … 113.0); guide_departure_m_s=9.148355844385556 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.230291534230668 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=162.48259442672267 g (allowed None … 113.0); guide_departure_m_s=9.191848164269631 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.72684688505709 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=176.38259442672265 g (allowed None … 85.0); apogee_m=5.374682564399159 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.772801775607946 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.940491836751763 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=176.38259442672265 g (allowed None … 85.0); apogee_m=5.360977673125478 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.766522964214083 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.384544993326305 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=178.93259442672266 g (allowed None … 99.0); apogee_m=19.341738842988676 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.448192485488128 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.187540494282466 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=178.93259442672266 g (allowed None … 99.0); apogee_m=18.641660162604193 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4411438878809495 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.205579232118996 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.244051513740123 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.237197039668102 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.244051513740123 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.87049499415483 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.237197039668102 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.312125777117878 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=176.38259442672265 g (allowed None … 85.0); apogee_m=5.374682564399159 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.772801775607946 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.940491836751763 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=176.38259442672265 g (allowed None … 85.0); apogee_m=5.360977673125478 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.766522964214083 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.384544993326305 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=178.93259442672266 g (allowed None … 99.0); apogee_m=19.341738842988676 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.448192485488128 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.187540494282466 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=178.93259442672266 g (allowed None … 99.0); apogee_m=18.641660162604193 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4411438878809495 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.205579232119003 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.244051513740123
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.237197039668102
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.244051513740123
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.870494994154846 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=183.13259442672268 g (allowed None … 113.0); guide_departure_m_s=8.237197039668102
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.312125777117902 m/s (allowed None … 10.0)
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
