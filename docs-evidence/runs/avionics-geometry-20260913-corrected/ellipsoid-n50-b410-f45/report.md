# Rocket Workbench report

Run: `ellipsoid-n50-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `fac69fe3015c157bdf0ca67f83bac9e6d67d36de23a4b58521aac509451dadbb`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.20 |      6.63 |           1.77 | unavailable |       11.07 |    0.27 |            5.36 |             6.36 |              8.44 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.18 |      6.63 |           0.76 | unavailable |       10.36 |    0.58 |            5.36 |             6.36 |              8.42 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.39 |      8.34 |           1.61 |       14.56 |        4.83 |    3.23 |            7.19 |             8.19 |             17.25 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.70 |      8.33 |           0.82 |       12.56 |        4.70 |    7.96 |            7.19 |             8.18 |             17.03 |
| empty-C6-3-wind0  | completed / outside configured limits |    91.05 |      9.10 |           1.69 |        2.29 |        4.82 |    0.04 |            7.83 |             8.83 |             35.23 |
| empty-C6-3-wind2  | completed / outside configured limits |    87.45 |      9.09 |           1.11 |        6.15 |        4.82 |    8.95 |            7.83 |             8.83 |             35.07 |
| empty-C6-5-wind0  | completed / outside configured limits |    91.09 |      9.10 |           1.33 |       12.35 |        4.82 |    1.44 |            7.83 |             8.83 |             35.23 |
| empty-C6-5-wind2  | completed / outside configured limits |    87.49 |      9.09 |           1.11 |       18.15 |        4.82 |    8.88 |            7.83 |             8.83 |             35.07 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.73 |     13.05 |           1.49 |        3.97 |        4.83 |    0.02 |           11.84 |            12.84 |             27.17 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    72.02 |     13.05 |           1.09 |        5.23 |        4.83 |   12.30 |           11.84 |            12.83 |             27.01 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.27 |      5.71 |           2.29 | unavailable |        9.93 |    0.12 |            4.62 |             5.62 |              6.78 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.27 |      5.71 |           1.22 | unavailable |        9.28 |    0.39 |            4.62 |             5.62 |              6.77 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.13 |      7.37 |           2.26 | unavailable |       16.03 |    0.50 |            6.25 |             7.25 |             14.24 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.53 |      7.37 |           1.35 | unavailable |       18.06 |    7.08 |            6.25 |             7.24 |             14.03 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.97 |      8.16 |           2.05 |        1.69 |        5.14 |    0.03 |            6.84 |             7.84 |             29.77 |
| dummy-C6-3-wind2  | completed / outside configured limits |    67.92 |      8.16 |           1.53 |        7.30 |        5.14 |    3.63 |            6.84 |             7.84 |             29.65 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.97 |      8.16 |           2.05 |       16.27 |        5.14 |    0.62 |            6.84 |             7.84 |             29.77 |
| dummy-C6-5-wind2  | completed / outside configured limits |    67.92 |      8.16 |           1.53 |       22.19 |        5.14 |   25.63 |            6.84 |             7.84 |             29.65 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.50 |     12.35 |           2.03 |        7.81 |        5.15 |    0.08 |           10.40 |            11.39 |             22.45 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.60 |     12.34 |           1.71 |        9.07 |        5.15 |    1.16 |           10.39 |            11.39 |             22.32 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.27 |      5.71 |           2.29 | unavailable |        9.93 |    0.12 |            4.62 |             5.62 |              6.78 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.27 |      5.71 |           1.22 | unavailable |        9.28 |    0.39 |            4.62 |             5.62 |              6.77 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.13 |      7.37 |           2.26 | unavailable |       16.03 |    0.50 |            6.25 |             7.25 |             14.24 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.53 |      7.37 |           1.35 | unavailable |       18.06 |    7.08 |            6.25 |             7.24 |             14.03 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.97 |      8.16 |           2.05 |        1.69 |        5.14 |    0.03 |            6.84 |             7.84 |             29.77 |
| actual-C6-3-wind2 | completed / outside configured limits |    67.92 |      8.16 |           1.53 |        7.30 |        5.14 |    3.63 |            6.84 |             7.84 |             29.65 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.97 |      8.16 |           2.05 |       16.27 |        5.14 |    0.62 |            6.84 |             7.84 |             29.77 |
| actual-C6-5-wind2 | completed / outside configured limits |    67.92 |      8.16 |           1.53 |       22.19 |        5.14 |   25.63 |            6.84 |             7.84 |             29.65 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.50 |     12.35 |           2.03 |        7.81 |        5.15 |    0.08 |           10.40 |            11.39 |             22.45 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.60 |     12.34 |           1.71 |        9.07 |        5.15 |    1.16 |           10.39 |            11.39 |             22.32 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (19.3°); Flight Event occurred after landing: Ejection charge;
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
- actual-A8-3-wind2: Large angle of attack encountered (19.3°); Flight Event occurred after landing: Ejection charge;
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

- empty-A8-3-wind0: launch_mass_g=157.1922275169132 g (allowed None … 85.0); apogee_m=7.199479660962971 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.634406931499694 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.067158210107575 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=157.1922275169132 g (allowed None … 85.0); apogee_m=7.178696035005729 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.628316991156 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7594003329457133 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.355440196424063 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=159.7422275169132 g (allowed None … 99.0); apogee_m=25.39360882947095 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.340802345376861 m/s (allowed 12.0 … None); deployment_speed_m_s=14.560988802415569 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=159.7422275169132 g (allowed None … 99.0); apogee_m=24.700867891830747 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.334313212191903 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8233574801969256 cal (allowed 1.0 … None); deployment_speed_m_s=12.556563721146864 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=163.9422275169132 g (allowed None … 113.0); guide_departure_m_s=9.100686443914336 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=163.9422275169132 g (allowed None … 113.0); guide_departure_m_s=9.094498792264663 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=163.9422275169132 g (allowed None … 113.0); guide_departure_m_s=9.100686443914336 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.353163576692847 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=163.9422275169132 g (allowed None … 113.0); guide_departure_m_s=9.094498792264663 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.1541022573346 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=177.8422275169132 g (allowed None … 85.0); apogee_m=5.2745361534616615 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.714864488991854 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.934071894837045 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=177.8422275169132 g (allowed None … 85.0); apogee_m=5.265869079379431 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.70986672263464 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.283844869106947 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=180.39222751691318 g (allowed None … 99.0); apogee_m=19.1285821649301 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.371928884150159 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.02516149949033 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=180.39222751691318 g (allowed None … 99.0); apogee_m=18.534125126676713 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.366316374303708 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.058321159906153 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.162449884732943 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.156987701297425 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.162449884732943 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.269982009501973 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.156987701297425 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.18862422650141 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=177.8422275169132 g (allowed None … 85.0); apogee_m=5.2745361534616615 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.714864488991854 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.934071894837045 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=177.8422275169132 g (allowed None … 85.0); apogee_m=5.265869079379431 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.70986672263464 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.283844869106948 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=180.39222751691318 g (allowed None … 99.0); apogee_m=19.1285821649301 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.371928884150159 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.025161499490334 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=180.39222751691318 g (allowed None … 99.0); apogee_m=18.534125126676713 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.366316374303708 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.05832115990616 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.162449884732943 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.156987701297425 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.162449884732943 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.26998200950197 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=184.5922275169132 g (allowed None … 113.0); guide_departure_m_s=8.156987701297425 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.188624226501013 m/s (allowed None … 10.0)
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
