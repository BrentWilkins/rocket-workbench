# Rocket Workbench report

Run: `ogive-n70-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `6744de52e3505d07ed85353ceb8a1e8b910140428cfed0e84da2a59ab6c7cccd`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.97 |      6.53 |           2.08 | unavailable |       11.00 |    0.24 |            5.28 |             6.28 |              8.25 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.95 |      6.52 |           0.86 | unavailable |       10.19 |    0.63 |            5.28 |             6.27 |              8.23 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.63 |      8.24 |           2.07 |       13.74 |        4.89 |    3.07 |            7.08 |             8.08 |             16.91 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.99 |      8.23 |           0.93 |       17.55 |        6.54 |    9.44 |            7.08 |             8.08 |             16.70 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.62 |      9.01 |           1.96 |        1.77 |        4.86 |    0.04 |            7.72 |             8.72 |             34.58 |
| empty-C6-3-wind2  | completed / outside configured limits |    85.12 |      9.00 |           1.27 |        5.95 |        4.86 |    8.18 |            7.72 |             8.72 |             34.42 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.63 |      9.01 |           1.23 |       12.28 |        4.86 |    1.55 |            7.72 |             8.72 |             34.58 |
| empty-C6-5-wind2  | completed / outside configured limits |    85.14 |      9.00 |           1.27 |       18.49 |        4.86 |    9.69 |            7.72 |             8.72 |             34.42 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.68 |     13.08 |           1.73 |        4.45 |        4.87 |    0.01 |           11.68 |            12.68 |             26.61 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.00 |     13.07 |           1.20 |        5.50 |        4.87 |   11.36 |           11.67 |            12.67 |             26.45 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.12 |      5.63 |           2.63 | unavailable |        9.83 |    0.11 |            4.55 |             5.55 |              6.64 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.11 |      5.62 |           1.35 | unavailable |        9.19 |    0.44 |            4.55 |             5.55 |              6.62 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.60 |      7.29 |           2.22 | unavailable |       15.67 |    0.57 |            6.16 |             7.16 |             13.97 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.06 |      7.28 |           1.42 | unavailable |       17.71 |    6.59 |            6.16 |             7.16 |             13.77 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.10 |      8.08 |           1.90 |        2.14 |        5.17 |    0.03 |            6.75 |             7.75 |             29.24 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.18 |      8.08 |           1.70 |        7.33 |        5.17 |    3.95 |            6.75 |             7.75 |             29.12 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.10 |      8.08 |           1.90 |       16.40 |        5.17 |    0.70 |            6.75 |             7.75 |             29.24 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.18 |      8.08 |           1.70 |       22.47 |        5.17 |   25.90 |            6.75 |             7.75 |             29.12 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.98 |     12.35 |           2.15 |        8.21 |        5.18 |    0.10 |           10.27 |            11.27 |             22.00 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.10 |     12.34 |           1.85 |        9.35 |        5.18 |    0.45 |           10.26 |            11.26 |             21.86 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.12 |      5.63 |           2.63 | unavailable |        9.83 |    0.11 |            4.55 |             5.55 |              6.64 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.11 |      5.62 |           1.35 | unavailable |        9.19 |    0.44 |            4.55 |             5.55 |              6.62 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.60 |      7.29 |           2.22 | unavailable |       15.67 |    0.57 |            6.16 |             7.16 |             13.97 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.06 |      7.28 |           1.42 | unavailable |       17.71 |    6.59 |            6.16 |             7.16 |             13.77 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.10 |      8.08 |           1.90 |        2.14 |        5.17 |    0.03 |            6.75 |             7.75 |             29.24 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.18 |      8.08 |           1.70 |        7.33 |        5.17 |    3.95 |            6.75 |             7.75 |             29.12 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.10 |      8.08 |           1.90 |       16.40 |        5.17 |    0.70 |            6.75 |             7.75 |             29.24 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.18 |      8.08 |           1.70 |       22.47 |        5.17 |   25.90 |            6.75 |             7.75 |             29.12 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.98 |     12.35 |           2.15 |        8.21 |        5.18 |    0.10 |           10.27 |            11.27 |             22.00 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.10 |     12.34 |           1.85 |        9.35 |        5.18 |    0.45 |           10.26 |            11.26 |             21.86 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (22°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.5 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (22°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.5 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=159.2551260081617 g (allowed None … 85.0); apogee_m=6.968423096985641 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.529482734302411 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.999781488745185 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=159.2551260081617 g (allowed None … 85.0); apogee_m=6.950590586464664 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.52338629698911 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8632444987490623 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.19155708227217 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=161.80512600816172 g (allowed None … 99.0); apogee_m=24.63427601330262 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.2381069691742 m/s (allowed 12.0 … None); deployment_speed_m_s=13.73962142530486 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=161.80512600816172 g (allowed None … 99.0); apogee_m=23.993315713810258 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.23153563086666 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.927392934319244 cal (allowed 1.0 … None); deployment_speed_m_s=17.554573129581556 m/s
  (allowed None … 10.0); landing_descent_m_s=6.537288884029982 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=166.0051260081617 g (allowed None … 113.0); guide_departure_m_s=9.00744437246509 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=166.0051260081617 g (allowed None … 113.0); guide_departure_m_s=9.001156275197246 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=166.0051260081617 g (allowed None … 113.0); guide_departure_m_s=9.00744437246509 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.279342134902796 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=166.0051260081617 g (allowed None … 113.0); guide_departure_m_s=9.001156275197246 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.486000462825356 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=179.90512600816172 g (allowed None … 85.0); apogee_m=5.118570337816008 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.625731264994399 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.829878479388523 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=179.90512600816172 g (allowed None … 85.0); apogee_m=5.11045713314208 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.620675449577399 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.186203051092122 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=182.45512600816173 g (allowed None … 99.0); apogee_m=18.597458675256984 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2868292292821355 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.669174585873765 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=182.45512600816173 g (allowed None … 99.0); apogee_m=18.055072411462174 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.281150410765847 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.714346171839583 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.083938769462181 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.078392518219593 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.083938769462181 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.396242877206138 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.078392518219593 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.466823463058297 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=179.90512600816172 g (allowed None … 85.0); apogee_m=5.118570337816008 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.625731264994399 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.829878479388523 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=179.90512600816172 g (allowed None … 85.0); apogee_m=5.11045713314208 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.620675449577399 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.186203051092122 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=182.45512600816173 g (allowed None … 99.0); apogee_m=18.597458675256984 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2868292292821355 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.669174585873765 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=182.45512600816173 g (allowed None … 99.0); apogee_m=18.055072411462174 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.281150410765847 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.714346171839587 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.083938769462181
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.078392518219593
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.083938769462181
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.396242877206134 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=186.65512600816172 g (allowed None … 113.0); guide_departure_m_s=8.078392518219593
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.4668234630583 m/s (allowed None … 10.0)
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
