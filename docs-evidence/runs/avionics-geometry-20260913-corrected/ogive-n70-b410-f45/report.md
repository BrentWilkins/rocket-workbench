# Rocket Workbench report

Run: `ogive-n70-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `7169f735e5de8a908ca50960465dff4ab4435ebe6892abe6da7cdbc8d5bb1c46`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.14 |      6.60 |           1.85 | unavailable |       11.06 |    0.26 |            5.34 |             6.34 |              8.39 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.12 |      6.59 |           0.71 | unavailable |       10.38 |    0.63 |            5.34 |             6.33 |              8.37 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.18 |      8.34 |           1.66 |       15.18 |        4.90 |    3.61 |            7.16 |             8.16 |             17.16 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.52 |      8.33 |           0.78 |       15.72 |        4.70 |    5.61 |            7.16 |             8.16 |             16.94 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.40 |      9.06 |           1.69 |        2.15 |        4.83 |    0.04 |            7.80 |             8.80 |             35.06 |
| empty-C6-3-wind2  | completed / outside configured limits |    86.87 |      9.06 |           1.08 |        6.05 |        4.83 |    8.96 |            7.80 |             8.80 |             34.90 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.43 |      9.06 |           0.80 |       12.55 |        4.83 |    1.61 |            7.80 |             8.80 |             35.06 |
| empty-C6-5-wind2  | completed / outside configured limits |    86.90 |      9.06 |           1.08 |       18.20 |        4.83 |    8.77 |            7.80 |             8.80 |             34.90 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.17 |     13.22 |           1.24 |        4.10 |        4.84 |    0.02 |           11.80 |            12.80 |             27.02 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    71.49 |     13.21 |           1.02 |        5.26 |        4.84 |   12.16 |           11.79 |            12.79 |             26.86 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.23 |      5.69 |           2.31 | unavailable |        9.89 |    0.11 |            4.60 |             5.60 |              6.74 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.22 |      5.68 |           1.17 | unavailable |        9.31 |    0.42 |            4.60 |             5.60 |              6.73 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.98 |      7.37 |           1.78 | unavailable |       15.67 |    0.50 |            6.22 |             7.22 |             14.16 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.41 |      7.36 |           1.27 | unavailable |       17.98 |    6.92 |            6.22 |             7.22 |             13.96 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.46 |      8.13 |           1.95 |        1.81 |        5.15 |    0.03 |            6.82 |             7.81 |             29.63 |
| dummy-C6-3-wind2  | completed / outside configured limits |    67.48 |      8.12 |           1.50 |        7.27 |        5.15 |    3.57 |            6.81 |             7.81 |             29.50 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.46 |      8.13 |           1.95 |       16.07 |        5.15 |    0.38 |            6.82 |             7.81 |             29.63 |
| dummy-C6-5-wind2  | completed / outside configured limits |    67.48 |      8.12 |           1.50 |       22.24 |        5.15 |   25.49 |            6.81 |             7.81 |             29.50 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.08 |     12.46 |           1.95 |        7.92 |        5.16 |    0.08 |           10.36 |            11.36 |             22.33 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.20 |     12.46 |           1.65 |        9.11 |        5.16 |    1.07 |           10.35 |            11.35 |             22.19 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.23 |      5.69 |           2.31 | unavailable |        9.89 |    0.11 |            4.60 |             5.60 |              6.74 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.22 |      5.68 |           1.17 | unavailable |        9.31 |    0.42 |            4.60 |             5.60 |              6.73 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.98 |      7.37 |           1.78 | unavailable |       15.67 |    0.50 |            6.22 |             7.22 |             14.16 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.41 |      7.36 |           1.27 | unavailable |       17.98 |    6.92 |            6.22 |             7.22 |             13.96 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.46 |      8.13 |           1.95 |        1.81 |        5.15 |    0.03 |            6.82 |             7.81 |             29.63 |
| actual-C6-3-wind2 | completed / outside configured limits |    67.48 |      8.12 |           1.50 |        7.27 |        5.15 |    3.57 |            6.81 |             7.81 |             29.50 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.46 |      8.13 |           1.95 |       16.07 |        5.15 |    0.38 |            6.82 |             7.81 |             29.63 |
| actual-C6-5-wind2 | completed / outside configured limits |    67.48 |      8.12 |           1.50 |       22.24 |        5.15 |   25.49 |            6.81 |             7.81 |             29.50 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.08 |     12.46 |           1.95 |        7.92 |        5.16 |    0.08 |           10.36 |            11.36 |             22.33 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.20 |     12.46 |           1.65 |        9.11 |        5.16 |    1.07 |           10.35 |            11.35 |             22.19 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (20.8°); Flight Event occurred after landing: Ejection charge;
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
- actual-A8-3-wind2: Large angle of attack encountered (20.8°); Flight Event occurred after landing: Ejection charge;
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

- empty-A8-3-wind0: launch_mass_g=157.75512600816177 g (allowed None … 85.0); apogee_m=7.135631337046885 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.600824699608215 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.063659137701718 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=157.75512600816177 g (allowed None … 85.0); apogee_m=7.116307418575283 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.59476788092187 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7144263451212443 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.377167161752984 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=160.30512600816178 g (allowed None … 99.0); apogee_m=25.184608105159516 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.33639339709666 m/s (allowed 12.0 … None); deployment_speed_m_s=15.1826002346948
  m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=160.30512600816178 g (allowed None … 99.0); apogee_m=24.523353991766637 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.32979318761986 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.775148567673568 cal (allowed 1.0 … None); deployment_speed_m_s=15.720438169932553 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=164.50512600816177 g (allowed None … 113.0); guide_departure_m_s=9.061363385767663 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=164.50512600816177 g (allowed None … 113.0); guide_departure_m_s=9.05521009748861 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=164.50512600816177 g (allowed None … 113.0); guide_departure_m_s=9.061363385767663 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.796561213296546 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.553330547913653 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=164.50512600816177 g (allowed None … 113.0); guide_departure_m_s=9.05521009748861 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.198323022190525 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=178.40512600816177 g (allowed None … 85.0); apogee_m=5.231585720002267 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.6874610451343885 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.891468812925197 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=178.40512600816177 g (allowed None … 85.0); apogee_m=5.223138754671219 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.682430935305439 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.313806753263819 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=180.95512600816178 g (allowed None … 99.0); apogee_m=18.982459108275506 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.367140926107582 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.672115516851882 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=180.95512600816178 g (allowed None … 99.0); apogee_m=18.4145292683329 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.361438781475866 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.9831351548678 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.13002502625824 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.124581180365322 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.13002502625824 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.068415472251502 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.124581180365322 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.240624244442845 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=178.40512600816177 g (allowed None … 85.0); apogee_m=5.231585720002267 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.6874610451343885 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=9.891468812925197 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=178.40512600816177 g (allowed None … 85.0); apogee_m=5.223138754671219 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.682430935305439 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.313806753263819 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=180.95512600816178 g (allowed None … 99.0); apogee_m=18.982459108275506 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.367140926107582 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.672115516851882 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=180.95512600816178 g (allowed None … 99.0); apogee_m=18.4145292683329 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.361438781475866 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.9831351548678 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.13002502625824 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.124581180365322
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.13002502625824 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.068415472251502 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=185.15512600816177 g (allowed None … 113.0); guide_departure_m_s=8.124581180365322
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.240624244442845 m/s (allowed None … 10.0)
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
