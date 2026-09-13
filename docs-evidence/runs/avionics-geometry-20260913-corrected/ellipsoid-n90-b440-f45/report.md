# Rocket Workbench report

Run: `ellipsoid-n90-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `011303dbdf50252c3de01237ebb1a5b0829ce26fad4471f4d43e2461d8e9381e`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.50 |      6.32 |           2.19 | unavailable |       10.80 |    0.20 |            5.11 |             6.10 |              7.87 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.49 |      6.31 |           0.83 | unavailable |       10.01 |    0.70 |            5.10 |             6.10 |              7.85 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.13 |      8.02 |           2.02 |       14.78 |        8.88 |    3.31 |            6.86 |             7.86 |             16.21 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.57 |      8.01 |           0.89 |       12.66 |        6.20 |    7.76 |            6.86 |             7.86 |             16.01 |
| empty-C6-3-wind0  | completed / outside configured limits |    84.11 |      8.80 |           2.05 |        0.86 |        4.93 |    0.04 |            7.49 |             8.49 |             33.31 |
| empty-C6-3-wind2  | completed / outside configured limits |    80.72 |      8.80 |           1.27 |        5.81 |        4.93 |    6.27 |            7.49 |             8.49 |             33.16 |
| empty-C6-5-wind0  | completed / outside configured limits |    84.11 |      8.80 |           1.85 |       12.59 |        4.93 |    1.96 |            7.49 |             8.49 |             33.31 |
| empty-C6-5-wind2  | completed / outside configured limits |    80.72 |      8.80 |           1.27 |       19.24 |        4.93 |   11.99 |            7.49 |             8.49 |             33.16 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    67.84 |     12.93 |           1.71 |        5.34 |        4.93 |    0.00 |           11.35 |            12.34 |             25.51 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    66.17 |     12.92 |           1.21 |        6.16 |        4.93 |    9.18 |           11.34 |            12.34 |             25.36 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.80 |      5.45 |           2.68 | unavailable |        9.60 |    0.09 |            4.42 |             5.42 |              6.33 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.79 |      5.44 |           1.27 | unavailable |        8.99 |    0.49 |            4.42 |             5.42 |              6.32 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.53 |      7.10 |           2.60 | unavailable |       14.38 |    0.70 |            5.99 |             6.99 |             13.41 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.06 |      7.10 |           1.28 | unavailable |       16.90 |    6.09 |            5.99 |             6.99 |             13.23 |
| dummy-C6-3-wind0  | completed / outside configured limits |    66.55 |      7.91 |           2.27 |        2.98 |        5.24 |    0.02 |            6.57 |             7.57 |             28.20 |
| dummy-C6-3-wind2  | completed / outside configured limits |    62.77 |      7.91 |           1.67 |        7.64 |        5.24 |    5.17 |            6.57 |             7.57 |             28.08 |
| dummy-C6-5-wind0  | completed / outside configured limits |    66.55 |      7.91 |           2.27 |       16.51 |        5.24 |    0.47 |            6.57 |             7.57 |             28.20 |
| dummy-C6-5-wind2  | completed / outside configured limits |    62.77 |      7.91 |           1.67 |       23.14 |        5.24 |   27.41 |            6.57 |             7.57 |             28.08 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    53.04 |     12.15 |           2.00 |        8.96 |        5.24 |    0.14 |           10.00 |            11.00 |             21.10 |
| dummy-C5-3-wind2  | completed / outside configured limits |    51.16 |     12.15 |           1.85 |       10.10 |        5.24 |    1.35 |           10.00 |            10.99 |             20.96 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.80 |      5.45 |           2.68 | unavailable |        9.60 |    0.09 |            4.42 |             5.42 |              6.33 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.79 |      5.44 |           1.27 | unavailable |        8.99 |    0.49 |            4.42 |             5.42 |              6.32 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.53 |      7.10 |           2.60 | unavailable |       14.38 |    0.70 |            5.99 |             6.99 |             13.41 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.06 |      7.10 |           1.28 | unavailable |       16.90 |    6.09 |            5.99 |             6.99 |             13.23 |
| actual-C6-3-wind0 | completed / outside configured limits |    66.55 |      7.91 |           2.27 |        2.98 |        5.24 |    0.02 |            6.57 |             7.57 |             28.20 |
| actual-C6-3-wind2 | completed / outside configured limits |    62.77 |      7.91 |           1.67 |        7.64 |        5.24 |    5.17 |            6.57 |             7.57 |             28.08 |
| actual-C6-5-wind0 | completed / outside configured limits |    66.55 |      7.91 |           2.27 |       16.51 |        5.24 |    0.47 |            6.57 |             7.57 |             28.20 |
| actual-C6-5-wind2 | completed / outside configured limits |    62.77 |      7.91 |           1.67 |       23.14 |        5.24 |   27.41 |            6.57 |             7.57 |             28.08 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    53.04 |     12.15 |           2.00 |        8.96 |        5.24 |    0.14 |           10.00 |            11.00 |             21.10 |
| actual-C5-3-wind2 | completed / outside configured limits |    51.16 |     12.15 |           1.85 |       10.10 |        5.24 |    1.35 |           10.00 |            10.99 |             20.96 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (25.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Large angle of attack encountered (19°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.1 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (25.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Large angle of attack encountered (19°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.1 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=163.72831649214797 g (allowed None … 85.0); apogee_m=6.503195794249384 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.3186246961076975 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.798677079848328 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=163.72831649214797 g (allowed None … 85.0); apogee_m=6.4894692659180695 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.312727268239836 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8298304505946259 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.013334727410287 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=166.27831649214798 g (allowed None … 99.0); apogee_m=23.13275932979653 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.01773304625176 m/s (allowed 12.0 … None); deployment_speed_m_s=14.780934969003384 m/s
  (allowed None … 10.0); landing_descent_m_s=8.87933746577784 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=166.27831649214798 g (allowed None … 99.0); apogee_m=22.57070364836595 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.011282105463378 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8858810418278769 cal (allowed 1.0 … None); deployment_speed_m_s=12.657563741960654 m/s
  (allowed None … 10.0); landing_descent_m_s=6.20238781114316 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=170.47831649214797 g (allowed None … 113.0); guide_departure_m_s=8.80313942482062 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=170.47831649214797 g (allowed None … 113.0); guide_departure_m_s=8.796927539123995 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=170.47831649214797 g (allowed None … 113.0); guide_departure_m_s=8.80313942482062 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.58718656207221 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=170.47831649214797 g (allowed None … 113.0); guide_departure_m_s=8.796927539123995 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.23511905891707 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=184.37831649214795 g (allowed None … 85.0); apogee_m=4.801457557445727 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.445701585504483 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.60129378690908 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=184.37831649214795 g (allowed None … 85.0); apogee_m=4.79430154947291 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.4408070506189405 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.987107420774372 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=186.92831649214796 g (allowed None … 99.0); apogee_m=17.53200370449328 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.103409696775249 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=14.37856662947616 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=186.92831649214796 g (allowed None … 99.0); apogee_m=17.05692863307504 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.097858650512673 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.90014565824361 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.911793312513369 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.906334458196072 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.911793312513369 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.511606912386487 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.906334458196072 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.138525447160678 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.101274264354217 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=184.37831649214795 g (allowed None … 85.0); apogee_m=4.801457557445727 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.445701585504483 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.60129378690908 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=184.37831649214795 g (allowed None … 85.0); apogee_m=4.79430154947291 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.4408070506189405 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.98710742077437 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=186.92831649214796 g (allowed None … 99.0); apogee_m=17.53200370449328 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.103409696775249 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=14.378566629476163 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=186.92831649214796 g (allowed None … 99.0); apogee_m=17.05692863307504 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.097858650512673 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.900145658243552 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.911793312513369
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.906334458196072
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.911793312513369
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.51160691238649 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=191.12831649214795 g (allowed None … 113.0); guide_departure_m_s=7.906334458196072
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.13852544716072 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.101274264354231 m/s (allowed None … 10.0)

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
