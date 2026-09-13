# Rocket Workbench report

Run: `ogive-n50-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `bc982e1e1b0ccdc8a6a5b5de6b5a51436549d0e76b42411ba6537e54192c53e8`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.18 |      6.63 |           2.11 | unavailable |       11.09 |    0.27 |            5.36 |             6.35 |              8.43 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.16 |      6.62 |           0.91 | unavailable |       10.26 |    0.58 |            5.35 |             6.35 |              8.41 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.32 |      8.33 |           2.03 |       12.85 |        4.80 |    2.39 |            7.18 |             8.18 |             17.22 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.63 |      8.33 |           0.96 |       18.47 |        6.33 |    9.21 |            7.18 |             8.18 |             17.00 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.63 |      9.09 |           1.93 |        2.17 |        4.83 |    0.04 |            7.83 |             8.82 |             35.15 |
| empty-C6-3-wind2  | completed / outside configured limits |    87.06 |      9.08 |           1.28 |        6.08 |        4.83 |    8.90 |            7.82 |             8.82 |             34.99 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.66 |      9.09 |           1.33 |       12.16 |        4.83 |    1.33 |            7.83 |             8.82 |             35.15 |
| empty-C6-5-wind2  | completed / outside configured limits |    87.09 |      9.08 |           1.28 |       18.20 |        4.83 |    8.89 |            7.82 |             8.82 |             34.99 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.41 |     13.04 |           1.73 |        4.06 |        4.83 |    0.02 |           11.83 |            12.83 |             27.09 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    71.72 |     13.03 |           1.24 |        5.25 |        4.83 |   12.25 |           11.82 |            12.82 |             26.93 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.26 |      5.71 |           2.55 | unavailable |        9.95 |    0.12 |            4.61 |             5.61 |              6.77 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.25 |      5.70 |           1.41 | unavailable |        9.28 |    0.41 |            4.61 |             5.61 |              6.76 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.08 |      7.36 |           2.50 | unavailable |       16.00 |    0.59 |            6.24 |             7.24 |             14.21 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.50 |      7.36 |           1.52 | unavailable |       18.08 |    6.92 |            6.24 |             7.24 |             14.01 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.69 |      8.15 |           1.49 |        1.77 |        5.14 |    0.03 |            6.83 |             7.83 |             29.71 |
| dummy-C6-3-wind2  | completed / outside configured limits |    67.69 |      8.15 |           1.74 |        7.26 |        5.14 |    3.51 |            6.83 |             7.83 |             29.58 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.69 |      8.15 |           1.49 |       16.32 |        5.14 |    0.86 |            6.83 |             7.83 |             29.71 |
| dummy-C6-5-wind2  | completed / outside configured limits |    67.69 |      8.15 |           1.74 |       22.20 |        5.14 |   25.40 |            6.83 |             7.83 |             29.58 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.30 |     12.33 |           1.58 |        7.88 |        5.15 |    0.08 |           10.39 |            11.39 |             22.40 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.41 |     12.33 |           1.91 |        9.07 |        5.15 |    1.18 |           10.38 |            11.38 |             22.26 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.26 |      5.71 |           2.55 | unavailable |        9.95 |    0.12 |            4.61 |             5.61 |              6.77 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.25 |      5.70 |           1.41 | unavailable |        9.28 |    0.41 |            4.61 |             5.61 |              6.76 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.08 |      7.36 |           2.50 | unavailable |       16.00 |    0.59 |            6.24 |             7.24 |             14.21 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.50 |      7.36 |           1.52 | unavailable |       18.08 |    6.92 |            6.24 |             7.24 |             14.01 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.69 |      8.15 |           1.49 |        1.77 |        5.14 |    0.03 |            6.83 |             7.83 |             29.71 |
| actual-C6-3-wind2 | completed / outside configured limits |    67.69 |      8.15 |           1.74 |        7.26 |        5.14 |    3.51 |            6.83 |             7.83 |             29.58 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.69 |      8.15 |           1.49 |       16.32 |        5.14 |    0.86 |            6.83 |             7.83 |             29.71 |
| actual-C6-5-wind2 | completed / outside configured limits |    67.69 |      8.15 |           1.74 |       22.20 |        5.14 |   25.40 |            6.83 |             7.83 |             29.58 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.30 |     12.33 |           1.58 |        7.88 |        5.15 |    0.08 |           10.39 |            11.39 |             22.40 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.41 |     12.33 |           1.91 |        9.07 |        5.15 |    1.18 |           10.38 |            11.38 |             22.26 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (19.9°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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
- actual-A8-3-wind2: Large angle of attack encountered (19.9°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=157.32474543704342 g (allowed None … 85.0); apogee_m=7.182192125648956 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.626206626684631 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.086428511851766 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=157.32474543704342 g (allowed None … 85.0); apogee_m=7.161355327372258 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.6200091835351165 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9056663618650799 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.261122215930829 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=159.8747454370434 g (allowed None … 99.0); apogee_m=25.31946671791676 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.331713870682997 m/s (allowed 12.0 … None); deployment_speed_m_s=12.85460394526655 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=159.8747454370434 g (allowed None … 99.0); apogee_m=24.634434795384642 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.325108917336523 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9611424167491109 cal (allowed 1.0 … None); deployment_speed_m_s=18.47232377175527 m/s
  (allowed None … 10.0); landing_descent_m_s=6.327016284855251 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=164.07474543704342 g (allowed None … 113.0); guide_departure_m_s=9.091083910861633 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=164.07474543704342 g (allowed None … 113.0); guide_departure_m_s=9.084785698076594 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=164.07474543704342 g (allowed None … 113.0); guide_departure_m_s=9.091083910861633 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.160193325957083 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=164.07474543704342 g (allowed None … 113.0); guide_departure_m_s=9.084785698076594 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.200950379980515 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=177.97474543704342 g (allowed None … 85.0); apogee_m=5.2634003858058875 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.708216102386902 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.952460688956242 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=177.97474543704342 g (allowed None … 85.0); apogee_m=5.254561469561474 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.703077609206654 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.275819701900232 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=180.5247454370434 g (allowed None … 99.0); apogee_m=19.081673286309556 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.364508095040785 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.003993606363387 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=180.5247454370434 g (allowed None … 99.0); apogee_m=18.499940895572934 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.3587937627791185 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.076956764074684 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.154532940054017 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.148972552373483 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.154532940054017 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.31880910693686 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.148972552373483 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.19773594703818 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=177.97474543704342 g (allowed None … 85.0); apogee_m=5.2634003858058875 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.708216102386902 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.952460688956242 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=177.97474543704342 g (allowed None … 85.0); apogee_m=5.254561469561474 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.703077609206654 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.275819701900232 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=180.5247454370434 g (allowed None … 99.0); apogee_m=19.081673286309556 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.364508095040785 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.003993606363384 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=180.5247454370434 g (allowed None … 99.0); apogee_m=18.499940895572934 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.3587937627791185 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.076956764074836 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.154532940054017
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.148972552373483
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.154532940054017
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.318809106936865 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=184.72474543704342 g (allowed None … 113.0); guide_departure_m_s=8.148972552373483
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.19773594703817 m/s (allowed None … 10.0)
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
