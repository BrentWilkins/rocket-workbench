# Rocket Workbench report

Run: `conical-n50-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `a90adbcb69ac012bddb4257bfd18f1a78dc42279134833b84fcbe1a6ec447550`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.51 |      6.77 |           2.03 | unavailable |       11.20 |    0.31 |            5.48 |             6.48 |              8.69 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.48 |      6.76 |           0.87 | unavailable |       10.39 |    0.58 |            5.47 |             6.47 |              8.67 |
| empty-B4-4-wind0  | completed / outside configured limits |    26.15 |      8.49 |           1.97 |       12.89 |        4.79 |    2.44 |            7.34 |             8.33 |             17.64 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.43 |      8.48 |           0.92 |       17.11 |        4.79 |    8.89 |            7.33 |             8.33 |             17.42 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.98 |      9.25 |           1.87 |        1.91 |        4.78 |    0.04 |            7.99 |             8.99 |             35.59 |
| empty-C6-3-wind2  | completed / outside configured limits |    87.48 |      9.24 |           1.25 |        5.73 |        4.78 |   10.19 |            7.98 |             8.98 |             35.42 |
| empty-C6-5-wind0  | completed / outside configured limits |    91.00 |      9.25 |           1.60 |       12.15 |        4.78 |    1.37 |            7.99 |             8.99 |             35.59 |
| empty-C6-5-wind2  | completed / outside configured limits |    87.50 |      9.24 |           1.25 |       18.15 |        4.78 |    7.11 |            7.98 |             8.98 |             35.42 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    74.27 |     13.15 |           1.52 |        4.09 |        4.79 |    0.02 |           12.06 |            13.06 |             27.44 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    72.59 |     13.14 |           1.17 |        5.12 |        4.79 |   13.52 |           12.05 |            13.05 |             27.26 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.49 |      5.83 |           2.53 | unavailable |       10.08 |    0.13 |            4.71 |             5.71 |              6.98 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.47 |      5.82 |           1.40 | unavailable |        9.45 |    0.39 |            4.71 |             5.71 |              6.96 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.73 |      7.50 |           2.42 | unavailable |       16.20 |    0.62 |            6.36 |             7.36 |             14.56 |
| dummy-B4-4-wind2  | completed / outside configured limits |    19.10 |      7.49 |           1.53 | unavailable |       18.33 |    7.20 |            6.36 |             7.36 |             14.34 |
| dummy-C6-3-wind0  | completed / outside configured limits |    72.59 |      8.29 |           1.58 |        1.77 |        5.10 |    0.03 |            6.96 |             7.96 |             30.15 |
| dummy-C6-3-wind2  | completed / outside configured limits |    68.63 |      8.28 |           1.73 |        7.02 |        5.10 |    2.32 |            6.96 |             7.96 |             30.01 |
| dummy-C6-5-wind0  | completed / outside configured limits |    72.59 |      8.29 |           1.58 |       16.28 |        5.10 |    0.88 |            6.96 |             7.96 |             30.15 |
| dummy-C6-5-wind2  | completed / outside configured limits |    68.63 |      8.28 |           1.73 |       21.90 |        5.10 |   23.65 |            6.96 |             7.96 |             30.01 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    58.36 |     12.57 |           2.20 |        7.72 |        5.11 |    0.07 |           10.57 |            11.57 |             22.76 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    56.50 |     12.57 |           1.88 |        8.82 |        5.11 |    2.41 |           10.56 |            11.56 |             22.61 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.49 |      5.83 |           2.53 | unavailable |       10.08 |    0.13 |            4.71 |             5.71 |              6.98 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.47 |      5.82 |           1.40 | unavailable |        9.45 |    0.39 |            4.71 |             5.71 |              6.96 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.73 |      7.50 |           2.42 | unavailable |       16.20 |    0.62 |            6.36 |             7.36 |             14.56 |
| actual-B4-4-wind2 | completed / outside configured limits |    19.10 |      7.49 |           1.53 | unavailable |       18.33 |    7.20 |            6.36 |             7.36 |             14.34 |
| actual-C6-3-wind0 | completed / outside configured limits |    72.59 |      8.29 |           1.58 |        1.77 |        5.10 |    0.03 |            6.96 |             7.96 |             30.15 |
| actual-C6-3-wind2 | completed / outside configured limits |    68.63 |      8.28 |           1.73 |        7.02 |        5.10 |    2.32 |            6.96 |             7.96 |             30.01 |
| actual-C6-5-wind0 | completed / outside configured limits |    72.59 |      8.29 |           1.58 |       16.28 |        5.10 |    0.88 |            6.96 |             7.96 |             30.15 |
| actual-C6-5-wind2 | completed / outside configured limits |    68.63 |      8.28 |           1.73 |       21.90 |        5.10 |   23.65 |            6.96 |             7.96 |             30.01 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    58.36 |     12.57 |           2.20 |        7.72 |        5.11 |    0.07 |           10.57 |            11.57 |             22.76 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    56.50 |     12.57 |           1.88 |        8.82 |        5.11 |    2.41 |           10.56 |            11.56 |             22.61 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (17.2°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (21.9 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (17.2°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (21.9 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=154.3487754861409 g (allowed None … 85.0); apogee_m=7.505294181008129 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.7677888758123945 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.20325855837286 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=154.3487754861409 g (allowed None … 85.0); apogee_m=7.475174471794999 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.76039647066858 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8718728137157821 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.394962588219702 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=156.8987754861409 g (allowed None … 99.0); apogee_m=26.153409023720396 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.486246154309354 m/s (allowed 12.0 … None); deployment_speed_m_s=12.892158311008457 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=156.8987754861409 g (allowed None … 99.0); apogee_m=25.428118114732374 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.478383078131651 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9181067310029531 cal (allowed 1.0 … None); deployment_speed_m_s=17.108314300106066 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=161.0987754861409 g (allowed None … 113.0); guide_departure_m_s=9.247673455854926 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=161.0987754861409 g (allowed None … 113.0); guide_departure_m_s=9.240155555472422 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=161.0987754861409 g (allowed None … 113.0); guide_departure_m_s=9.247673455854926 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.146464344913413 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=161.0987754861409 g (allowed None … 113.0); guide_departure_m_s=9.240155555472422 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.150883823697303 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=174.99877548614091 g (allowed None … 85.0); apogee_m=5.486389498713076 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.830450406796711 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.07931958505055 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=174.99877548614091 g (allowed None … 85.0); apogee_m=5.472809411951469 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.824298138705506 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.452542767312668 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=177.5487754861409 g (allowed None … 99.0); apogee_m=19.727473525423036 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.4986840614765775 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.200694922021075 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=177.5487754861409 g (allowed None … 99.0); apogee_m=19.102770966634196 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.491841919866087 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.326443207639326 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.28514109457828 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.278511184020514 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.28514109457828 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.275787554771508 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.278511184020514 m/s
  (allowed 12.0 … None); deployment_speed_m_s=21.89880661125713 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=174.99877548614091 g (allowed None … 85.0); apogee_m=5.486389498713076 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.830450406796711 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.07931958505055 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=174.99877548614091 g (allowed None … 85.0); apogee_m=5.472809411951469 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.824298138705506 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.452542767312666 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=177.5487754861409 g (allowed None … 99.0); apogee_m=19.727473525423036 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4986840614765775 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=16.20069492202108 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=177.5487754861409 g (allowed None … 99.0); apogee_m=19.102770966634196 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.491841919866087 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.326443207639336 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.28514109457828 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.278511184020514
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.28514109457828 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.275787554771505 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=181.74877548614091 g (allowed None … 113.0); guide_departure_m_s=8.278511184020514
  m/s (allowed 12.0 … None); deployment_speed_m_s=21.89880661125786 m/s (allowed None … 10.0)
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
