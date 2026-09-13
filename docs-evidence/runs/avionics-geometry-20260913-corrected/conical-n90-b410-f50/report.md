# Rocket Workbench report

Run: `conical-n90-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `20c7298c0b2b7d2e66df0948bb5257583aba978ca5509038abe362ac85acc821`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.24 |      6.66 |           1.98 | unavailable |       10.94 |    0.31 |            5.38 |             6.38 |              8.47 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.21 |      6.65 |           0.82 | unavailable |       10.26 |    0.50 |            5.38 |             6.37 |              8.45 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.42 |      8.37 |           1.53 |       14.09 |        4.60 |    3.10 |            7.21 |             8.21 |             17.28 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.66 |      8.36 |           0.89 |       18.79 |        6.70 |    9.90 |            7.21 |             8.21 |             17.06 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.02 |      9.13 |           1.84 |        1.91 |        4.82 |    0.04 |            7.86 |             8.86 |             35.13 |
| empty-C6-3-wind2  | completed / outside configured limits |    86.23 |      9.12 |           1.24 |        6.18 |        4.82 |    7.71 |            7.85 |             8.85 |             34.96 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.04 |      9.13 |           1.56 |       12.13 |        4.82 |    1.48 |            7.86 |             8.86 |             35.13 |
| empty-C6-5-wind2  | completed / outside configured limits |    86.25 |      9.12 |           1.24 |       18.49 |        4.82 |   10.64 |            7.85 |             8.85 |             34.96 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.13 |     13.09 |           1.04 |        4.22 |        4.83 |    0.01 |           11.87 |            12.87 |             27.06 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    71.40 |     13.09 |           1.24 |        5.43 |        4.83 |   11.99 |           11.87 |            12.86 |             26.89 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.30 |      5.72 |           2.47 | unavailable |        9.92 |    0.14 |            4.63 |             5.63 |              6.81 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.29 |      5.72 |           1.30 | unavailable |        9.27 |    0.34 |            4.63 |             5.63 |              6.79 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.17 |      7.39 |           2.42 | unavailable |       16.06 |    0.48 |            6.26 |             7.26 |             14.27 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.50 |      7.39 |           1.50 | unavailable |       18.15 |    7.81 |            6.26 |             7.26 |             14.04 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.48 |      8.19 |           2.12 |        1.91 |        5.13 |    0.03 |            6.86 |             7.86 |             29.72 |
| dummy-C6-3-wind2  | completed / outside configured limits |    67.26 |      8.18 |           1.67 |        7.49 |        5.13 |    4.53 |            6.85 |             7.85 |             29.61 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.48 |      8.19 |           2.12 |       16.44 |        5.13 |    0.67 |            6.86 |             7.86 |             29.72 |
| dummy-C6-5-wind2  | completed / outside configured limits |    67.26 |      8.18 |           1.67 |       22.31 |        5.13 |   26.84 |            6.85 |             7.85 |             29.61 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.26 |     12.38 |           2.00 |        7.92 |        5.14 |    0.10 |           10.42 |            11.42 |             22.40 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.33 |     12.37 |           1.85 |        9.21 |        5.14 |    0.91 |           10.41 |            11.41 |             22.26 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.30 |      5.72 |           2.47 | unavailable |        9.92 |    0.14 |            4.63 |             5.63 |              6.81 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.29 |      5.72 |           1.30 | unavailable |        9.27 |    0.34 |            4.63 |             5.63 |              6.79 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.17 |      7.39 |           2.42 | unavailable |       16.06 |    0.48 |            6.26 |             7.26 |             14.27 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.50 |      7.39 |           1.50 | unavailable |       18.15 |    7.81 |            6.26 |             7.26 |             14.04 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.48 |      8.19 |           2.12 |        1.91 |        5.13 |    0.03 |            6.86 |             7.86 |             29.72 |
| actual-C6-3-wind2 | completed / outside configured limits |    67.26 |      8.18 |           1.67 |        7.49 |        5.13 |    4.53 |            6.85 |             7.85 |             29.61 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.48 |      8.19 |           2.12 |       16.44 |        5.13 |    0.67 |            6.86 |             7.86 |             29.72 |
| actual-C6-5-wind2 | completed / outside configured limits |    67.26 |      8.18 |           1.67 |       22.31 |        5.13 |   26.84 |            6.85 |             7.85 |             29.61 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.26 |     12.38 |           2.00 |        7.92 |        5.14 |    0.10 |           10.42 |            11.42 |             22.40 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.33 |     12.37 |           1.85 |        9.21 |        5.14 |    0.91 |           10.41 |            11.41 |             22.26 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (16.7°); Flight Event occurred after landing: Ejection charge;
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
- actual-A8-3-wind2: Large angle of attack encountered (16.7°); Flight Event occurred after landing: Ejection charge;
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

- empty-A8-3-wind0: launch_mass_g=156.75131732789293 g (allowed None … 85.0); apogee_m=7.237996476467312 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.659446548922071 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.937655570558075 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=156.75131732789293 g (allowed None … 85.0); apogee_m=7.209767724580497 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.652770778423286 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8237909967747589 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.255458513221473 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=159.30131732789295 g (allowed None … 99.0); apogee_m=25.417096676111193 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.368386433332157 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.087166491013658 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=159.30131732789295 g (allowed None … 99.0); apogee_m=24.658299524923066 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.361227310396671 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8924899388249992 cal (allowed 1.0 … None); deployment_speed_m_s=18.79035283512171 m/s
  (allowed None … 10.0); landing_descent_m_s=6.697546325952463 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=163.50131732789293 g (allowed None … 113.0); guide_departure_m_s=9.129949860539892 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=163.50131732789293 g (allowed None … 113.0); guide_departure_m_s=9.123121186595931 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=163.50131732789293 g (allowed None … 113.0); guide_departure_m_s=9.129949860539892 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.132292603512818 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=163.50131732789293 g (allowed None … 113.0); guide_departure_m_s=9.123121186595931 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.49177617129853 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=177.40131732789294 g (allowed None … 85.0); apogee_m=5.303121945150094 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.724149227082414 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.923956734201038 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=177.40131732789294 g (allowed None … 85.0); apogee_m=5.292813391816399 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.718699951824021 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.271310317468464 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=179.95131732789292 g (allowed None … 99.0); apogee_m=19.17010943173217 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.392534814396221 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.064268722168364 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=179.95131732789292 g (allowed None … 99.0); apogee_m=18.504822668640085 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.3883056265457565 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.152550260348292 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.186601608047823 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.180578799692267 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.186601608047823 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.442264348014977 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.180578799692267 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.31109298820372 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=177.40131732789294 g (allowed None … 85.0); apogee_m=5.303121945150094 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.724149227082414 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.923956734201038 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=177.40131732789294 g (allowed None … 85.0); apogee_m=5.292813391816399 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.718699951824021 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.271310317468464 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=179.95131732789292 g (allowed None … 99.0); apogee_m=19.17010943173217 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.392534814396221 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.064268722168364 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=179.95131732789292 g (allowed None … 99.0); apogee_m=18.504822668640085 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.3883056265457565 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=18.152550260348296 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.186601608047823
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.180578799692267
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.186601608047823
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.442264348014984 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=184.15131732789294 g (allowed None … 113.0); guide_departure_m_s=8.180578799692267
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.31109298820372 m/s (allowed None … 10.0)
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
