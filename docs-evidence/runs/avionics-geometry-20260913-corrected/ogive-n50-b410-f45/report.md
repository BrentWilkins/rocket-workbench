# Rocket Workbench report

Run: `ogive-n50-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `48f1f3abba1c51f30477e7cf0b9053197d9afae8c3c757dafbbc10a69733e7ad`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.36 |      6.70 |           1.80 | unavailable |       11.14 |    0.29 |            5.42 |             6.42 |              8.57 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.33 |      6.69 |           0.76 | unavailable |       10.46 |    0.58 |            5.41 |             6.41 |              8.55 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.89 |      8.41 |           1.63 |       14.46 |        4.80 |    3.19 |            7.26 |             8.26 |             17.48 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.18 |      8.40 |           0.81 |       13.65 |        4.81 |    6.81 |            7.26 |             8.26 |             17.26 |
| empty-C6-3-wind0  | completed / outside configured limits |    92.45 |      9.20 |           1.66 |        2.55 |        4.80 |    0.04 |            7.91 |             8.91 |             35.63 |
| empty-C6-3-wind2  | completed / outside configured limits |    88.85 |      9.19 |           1.10 |        6.20 |        4.80 |    9.74 |            7.90 |             8.90 |             35.47 |
| empty-C6-5-wind0  | completed / outside configured limits |    92.51 |      9.20 |           1.02 |       12.31 |        4.80 |    1.39 |            7.91 |             8.91 |             35.63 |
| empty-C6-5-wind2  | completed / outside configured limits |    88.91 |      9.19 |           1.10 |       17.90 |        4.80 |    7.87 |            7.90 |             8.90 |             35.47 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    74.95 |     13.18 |           1.31 |        3.70 |        4.81 |    0.02 |           11.95 |            12.95 |             27.51 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    73.25 |     13.18 |           1.08 |        5.04 |        4.81 |   13.07 |           11.94 |            12.94 |             27.35 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.38 |      5.77 |           2.27 | unavailable |       10.01 |    0.12 |            4.66 |             5.66 |              6.88 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.37 |      5.77 |           1.23 | unavailable |        9.41 |    0.38 |            4.66 |             5.66 |              6.86 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.48 |      7.45 |           2.19 | unavailable |       16.18 |    0.51 |            6.30 |             7.30 |             14.42 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.87 |      7.44 |           1.36 | unavailable |       18.26 |    7.27 |            6.30 |             7.30 |             14.20 |
| dummy-C6-3-wind0  | completed / outside configured limits |    73.09 |      8.24 |           1.86 |        1.43 |        5.12 |    0.03 |            6.90 |             7.90 |             30.10 |
| dummy-C6-3-wind2  | completed / outside configured limits |    69.04 |      8.24 |           1.53 |        7.19 |        5.12 |    3.04 |            6.90 |             7.89 |             29.97 |
| dummy-C6-5-wind0  | completed / outside configured limits |    73.09 |      8.24 |           1.86 |       16.14 |        5.12 |    0.60 |            6.90 |             7.90 |             30.10 |
| dummy-C6-5-wind2  | completed / outside configured limits |    69.04 |      8.24 |           1.53 |       21.95 |        5.12 |   24.87 |            6.90 |             7.89 |             29.97 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    58.44 |     12.46 |           1.68 |        7.58 |        5.13 |    0.07 |           10.48 |            11.48 |             22.74 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    56.55 |     12.45 |           1.70 |        8.84 |        5.13 |    1.78 |           10.47 |            11.47 |             22.60 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.38 |      5.77 |           2.27 | unavailable |       10.01 |    0.12 |            4.66 |             5.66 |              6.88 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.37 |      5.77 |           1.23 | unavailable |        9.41 |    0.38 |            4.66 |             5.66 |              6.86 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.48 |      7.45 |           2.19 | unavailable |       16.18 |    0.51 |            6.30 |             7.30 |             14.42 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.87 |      7.44 |           1.36 | unavailable |       18.26 |    7.27 |            6.30 |             7.30 |             14.20 |
| actual-C6-3-wind0 | completed / outside configured limits |    73.09 |      8.24 |           1.86 |        1.43 |        5.12 |    0.03 |            6.90 |             7.90 |             30.10 |
| actual-C6-3-wind2 | completed / outside configured limits |    69.04 |      8.24 |           1.53 |        7.19 |        5.12 |    3.04 |            6.90 |             7.89 |             29.97 |
| actual-C6-5-wind0 | completed / outside configured limits |    73.09 |      8.24 |           1.86 |       16.14 |        5.12 |    0.60 |            6.90 |             7.90 |             30.10 |
| actual-C6-5-wind2 | completed / outside configured limits |    69.04 |      8.24 |           1.53 |       21.95 |        5.12 |   24.87 |            6.90 |             7.89 |             29.97 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    58.44 |     12.46 |           1.68 |        7.58 |        5.13 |    0.07 |           10.48 |            11.48 |             22.74 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    56.55 |     12.45 |           1.70 |        8.84 |        5.13 |    1.78 |           10.47 |            11.47 |             22.60 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (18.6°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (18.6°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=155.82474543704342 g (allowed None … 85.0); apogee_m=7.355939212684242 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.69880617579626 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.139326957023265 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=155.82474543704342 g (allowed None … 85.0); apogee_m=7.332994106443793 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.6926486353146215 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7564665266675197 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.456078210552306 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=158.3747454370434 g (allowed None … 99.0); apogee_m=25.889421429089644 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.406727927415805 m/s (allowed 12.0 … None); deployment_speed_m_s=14.462433671199985 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=158.3747454370434 g (allowed None … 99.0); apogee_m=25.179260061913766 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.40024646709665 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8089318162045601 cal (allowed 1.0 … None); deployment_speed_m_s=13.646277487792757 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=162.57474543704342 g (allowed None … 113.0); guide_departure_m_s=9.19708850313099 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=162.57474543704342 g (allowed None … 113.0); guide_departure_m_s=9.190768269348013 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=162.57474543704342 g (allowed None … 113.0); guide_departure_m_s=9.19708850313099 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.310659893562379 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=162.57474543704342 g (allowed None … 113.0); guide_departure_m_s=9.190768269348013 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.897702794064983 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=176.47474543704342 g (allowed None … 85.0); apogee_m=5.38038209615896 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.770799490617582 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.007758205276122 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=176.47474543704342 g (allowed None … 85.0); apogee_m=5.371021056905533 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.765676605204525 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.405005532957299 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=179.0247454370434 g (allowed None … 99.0); apogee_m=19.479665635591378 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.446289052837752 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.175720259607967 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=179.0247454370434 g (allowed None … 99.0); apogee_m=18.868693787956826 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.440549659434545 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.255843974808013 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.241902771248647 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.236327060747424 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.241902771248647 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.136847216935433 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.236327060747424 m/s
  (allowed 12.0 … None); deployment_speed_m_s=21.953408683836948 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=176.47474543704342 g (allowed None … 85.0); apogee_m=5.38038209615896 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.770799490617582 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.007758205276122 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=176.47474543704342 g (allowed None … 85.0); apogee_m=5.371021056905533 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.765676605204525 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.405005532957299 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=179.0247454370434 g (allowed None … 99.0); apogee_m=19.479665635591378 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.446289052837752 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.175720259607974 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=179.0247454370434 g (allowed None … 99.0); apogee_m=18.868693787956826 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.440549659434545 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.25584397480799 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.241902771248647
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.236327060747424
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.241902771248647
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.13684721693543 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=183.22474543704342 g (allowed None … 113.0); guide_departure_m_s=8.236327060747424
  m/s (allowed 12.0 … None); deployment_speed_m_s=21.953408683837093 m/s (allowed None … 10.0)
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
