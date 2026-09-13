# Rocket Workbench report

Run: `ellipsoid-n70-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `b67b6b4b05617c39f7fd3c35bf97c466276ca7d137e4eb34732875e1c91a308a`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.62 |      6.39 |           2.23 | unavailable |       10.58 |    0.28 |            5.15 |             6.15 |              7.97 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.60 |      6.38 |           1.04 | unavailable |        9.85 |    0.33 |            5.15 |             6.15 |              7.95 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.47 |      8.09 |           2.18 |       13.77 |        6.52 |    0.10 |            6.92 |             7.92 |             16.38 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.69 |      8.09 |           1.18 | unavailable |       19.87 |    9.53 |            6.92 |             7.92 |             16.14 |
| empty-C6-3-wind0  | completed / outside configured limits |    84.63 |      8.84 |           2.10 |        0.88 |        4.91 |    0.04 |            7.55 |             8.55 |             33.55 |
| empty-C6-3-wind2  | completed / outside configured limits |    80.48 |      8.83 |           1.47 |        6.56 |        4.91 |    2.96 |            7.55 |             8.55 |             33.40 |
| empty-C6-5-wind0  | completed / outside configured limits |    84.64 |      8.84 |           1.35 |       12.45 |        4.91 |    0.69 |            7.55 |             8.55 |             33.55 |
| empty-C6-5-wind2  | completed / outside configured limits |    80.48 |      8.83 |           1.47 |       19.71 |        4.91 |   17.07 |            7.55 |             8.55 |             33.40 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    68.42 |     12.89 |           1.75 |        5.26 |        4.92 |    0.01 |           11.44 |            12.43 |             25.70 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    66.59 |     12.88 |           1.60 |        6.52 |        4.92 |    8.38 |           11.43 |            12.43 |             25.54 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.89 |      5.49 |           2.70 | unavailable |        9.50 |    0.12 |            4.46 |             5.45 |              6.42 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.88 |      5.49 |           1.48 | unavailable |        9.02 |    0.30 |            4.45 |             5.45 |              6.40 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.79 |      7.17 |           2.64 | unavailable |       15.70 |    0.55 |            6.04 |             7.04 |             13.55 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.10 |      7.16 |           1.77 | unavailable |       17.63 |    7.64 |            6.04 |             7.04 |             13.31 |
| dummy-C6-3-wind0  | completed / outside configured limits |    67.12 |      7.94 |           2.31 |        2.89 |        5.22 |    0.02 |            6.62 |             7.62 |             28.41 |
| dummy-C6-3-wind2  | completed / outside configured limits |    62.60 |      7.94 |           1.87 |        8.35 |        5.22 |    8.35 |            6.62 |             7.62 |             28.32 |
| dummy-C6-5-wind0  | completed / outside configured limits |    67.12 |      7.94 |           2.31 |       17.80 |        5.22 |    1.11 |            6.62 |             7.62 |             28.41 |
| dummy-C6-5-wind2  | completed / outside configured limits |    62.60 |      7.94 |           1.87 |       23.41 |        5.22 |   32.07 |            6.62 |             7.62 |             28.32 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    53.59 |     12.25 |           2.32 |        8.79 |        5.22 |    0.19 |           10.07 |            11.07 |             21.27 |
| dummy-C5-3-wind2  | completed / outside configured limits |    51.55 |     12.24 |           2.08 |       10.30 |        5.22 |    1.98 |           10.07 |            11.07 |             21.14 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.89 |      5.49 |           2.70 | unavailable |        9.50 |    0.12 |            4.46 |             5.45 |              6.42 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.88 |      5.49 |           1.48 | unavailable |        9.02 |    0.30 |            4.45 |             5.45 |              6.40 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.79 |      7.17 |           2.64 | unavailable |       15.70 |    0.55 |            6.04 |             7.04 |             13.55 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.10 |      7.16 |           1.77 | unavailable |       17.63 |    7.64 |            6.04 |             7.04 |             13.31 |
| actual-C6-3-wind0 | completed / outside configured limits |    67.12 |      7.94 |           2.31 |        2.89 |        5.22 |    0.02 |            6.62 |             7.62 |             28.41 |
| actual-C6-3-wind2 | completed / outside configured limits |    62.60 |      7.94 |           1.87 |        8.35 |        5.22 |    8.35 |            6.62 |             7.62 |             28.32 |
| actual-C6-5-wind0 | completed / outside configured limits |    67.12 |      7.94 |           2.31 |       17.80 |        5.22 |    1.11 |            6.62 |             7.62 |             28.41 |
| actual-C6-5-wind2 | completed / outside configured limits |    62.60 |      7.94 |           1.87 |       23.41 |        5.22 |   32.07 |            6.62 |             7.62 |             28.32 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    53.59 |     12.25 |           2.32 |        8.79 |        5.22 |    0.19 |           10.07 |            11.07 |             21.27 |
| actual-C5-3-wind2 | completed / outside configured limits |    51.55 |     12.24 |           2.08 |       10.30 |        5.22 |    1.98 |           10.07 |            11.07 |             21.14 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (17.5°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.4 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (17.5°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.4 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=162.4779731446486 g (allowed None … 85.0); apogee_m=6.623970989339565 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.388262867945296 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.580412284720156 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=162.4779731446486 g (allowed None … 85.0); apogee_m=6.5994709702603975 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.381911003480262 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.84714594462039 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=165.0279731446486 g (allowed None … 99.0); apogee_m=23.473437246352113 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.092686513184988 m/s (allowed 12.0 … None); deployment_speed_m_s=13.771520012975861 m/s
  (allowed None … 10.0); landing_descent_m_s=6.517571785179306 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=165.0279731446486 g (allowed None … 99.0); apogee_m=22.685535775623823 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.087831583404823 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.86947164264392 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=169.22797314464862 g (allowed None … 113.0); guide_departure_m_s=8.837656880373341 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=169.22797314464862 g (allowed None … 113.0); guide_departure_m_s=8.831157321885044 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=169.22797314464862 g (allowed None … 113.0); guide_departure_m_s=8.837656880373341 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.450555214500342 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=169.22797314464862 g (allowed None … 113.0); guide_departure_m_s=8.831157321885044 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.70664935234578 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=183.1279731446486 g (allowed None … 85.0); apogee_m=4.8850536762191 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.49339292387023 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=9.503753981463205 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=183.1279731446486 g (allowed None … 85.0); apogee_m=4.877512107457537 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.4882113548397395 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.01725153614508 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=185.6779731446486 g (allowed None … 99.0); apogee_m=17.790798691402166 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.166798821543204 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.697389350177401 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=185.6779731446486 g (allowed None … 99.0); apogee_m=17.098735897278058 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.160855241993055 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.632073810919053 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.94179120207299 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.9360603212817145 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.94179120207299 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.798291405656325 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.9360603212817145 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.412146103198797 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.29538197866521 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=183.1279731446486 g (allowed None … 85.0); apogee_m=4.8850536762191 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.49339292387023 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=9.503753981463205 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=183.1279731446486 g (allowed None … 85.0); apogee_m=4.877512107457537 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.4882113548397395 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.01725153614508 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=185.6779731446486 g (allowed None … 99.0); apogee_m=17.790798691402166 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.166798821543204 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.697389350177406 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=185.6779731446486 g (allowed None … 99.0); apogee_m=17.098735897278058 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.160855241993055 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.632073810919028 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.94179120207299 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.9360603212817145
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.94179120207299 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.798291405656318 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=189.8779731446486 g (allowed None … 113.0); guide_departure_m_s=7.9360603212817145
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.412146103198825 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.295381978663096 m/s (allowed None … 10.0)

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
