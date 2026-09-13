# Rocket Workbench report

Run: `ogive-n90-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `d21be4d5964c73ff74ea2b272156b5b15d6b6061c11b74bc853c19b78966bff9`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.77 |      6.45 |           2.08 | unavailable |       10.78 |    0.26 |            5.21 |             6.20 |              8.09 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.75 |      6.45 |           0.85 | unavailable |       10.04 |    0.52 |            5.20 |             6.20 |              8.07 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.97 |      8.15 |           1.49 |       14.41 |        5.70 |    3.12 |            6.99 |             7.99 |             16.61 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.26 |      8.14 |           0.93 |       19.38 |       18.12 |    9.62 |            6.99 |             7.99 |             16.38 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.43 |      8.93 |           1.93 |        1.30 |        4.89 |    0.04 |            7.63 |             8.62 |             34.00 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.65 |      8.92 |           1.28 |        6.21 |        4.89 |    5.57 |            7.62 |             8.62 |             33.85 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.44 |      8.93 |           1.47 |       12.24 |        4.89 |    1.60 |            7.63 |             8.62 |             34.00 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.65 |      8.92 |           1.28 |       19.13 |        4.89 |   13.36 |            7.62 |             8.62 |             33.85 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    69.87 |     13.01 |           1.28 |        4.89 |        4.89 |    0.00 |           11.54 |            12.54 |             26.10 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.12 |     13.01 |           1.30 |        6.02 |        4.89 |    9.73 |           11.53 |            12.53 |             25.94 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.98 |      5.55 |           2.53 | unavailable |        9.64 |    0.11 |            4.50 |             5.50 |              6.51 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.98 |      5.54 |           1.29 | unavailable |        9.10 |    0.39 |            4.50 |             5.49 |              6.50 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.14 |      7.21 |           2.47 | unavailable |       15.56 |    0.47 |            6.09 |             7.09 |             13.73 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.53 |      7.21 |           1.47 | unavailable |       17.68 |    7.19 |            6.09 |             7.09 |             13.51 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.44 |      8.02 |           1.52 |        2.55 |        5.20 |    0.03 |            6.68 |             7.67 |             28.78 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.27 |      8.01 |           1.67 |        7.83 |        5.20 |    6.11 |            6.67 |             7.67 |             28.67 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.44 |      8.02 |           1.52 |       16.81 |        5.20 |    0.68 |            6.68 |             7.67 |             28.78 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.27 |      8.01 |           1.67 |       22.97 |        5.20 |   28.95 |            6.67 |             7.67 |             28.67 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.63 |     12.20 |           2.19 |        8.54 |        5.20 |    0.14 |           10.16 |            11.15 |             21.59 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    52.70 |     12.20 |           1.88 |        9.85 |        5.20 |    0.83 |           10.15 |            11.15 |             21.46 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.98 |      5.55 |           2.53 | unavailable |        9.64 |    0.11 |            4.50 |             5.50 |              6.51 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.98 |      5.54 |           1.29 | unavailable |        9.10 |    0.39 |            4.50 |             5.49 |              6.50 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.14 |      7.21 |           2.47 | unavailable |       15.56 |    0.47 |            6.09 |             7.09 |             13.73 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.53 |      7.21 |           1.47 | unavailable |       17.68 |    7.19 |            6.09 |             7.09 |             13.51 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.44 |      8.02 |           1.52 |        2.55 |        5.20 |    0.03 |            6.68 |             7.67 |             28.78 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.27 |      8.01 |           1.67 |        7.83 |        5.20 |    6.11 |            6.67 |             7.67 |             28.67 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.44 |      8.02 |           1.52 |       16.81 |        5.20 |    0.68 |            6.68 |             7.67 |             28.78 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.27 |      8.01 |           1.67 |       22.97 |        5.20 |   28.95 |            6.67 |             7.67 |             28.67 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.63 |     12.20 |           2.19 |        8.54 |        5.20 |    0.14 |           10.16 |            11.15 |             21.59 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    52.70 |     12.20 |           1.88 |        9.85 |        5.20 |    0.83 |           10.15 |            11.15 |             21.46 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (20.2°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (20.2°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=161.0989943321967 g (allowed None … 85.0); apogee_m=6.76956888832635 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.451390924052176 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=10.781584074058445 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=161.0989943321967 g (allowed None … 85.0); apogee_m=6.750146359669755 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.445186827010516 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.853192442284977 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=10.036965021893339 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=163.6489943321967 g (allowed None … 99.0); apogee_m=23.974907545172705 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.151259665776758 m/s (allowed 12.0 … None); deployment_speed_m_s=14.405039206795609 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=163.6489943321967 g (allowed None … 99.0); apogee_m=23.26298338238013 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.144582045455545 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9308907682171712 cal (allowed 1.0 … None); deployment_speed_m_s=19.37755322981637 m/s
  (allowed None … 10.0); landing_descent_m_s=18.120727912496662 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=167.84899433219672 g (allowed None … 113.0); guide_departure_m_s=8.930459870444297 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=167.84899433219672 g (allowed None … 113.0); guide_departure_m_s=8.924047847662578 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=167.84899433219672 g (allowed None … 113.0); guide_departure_m_s=8.930459870444297 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.242487476025456 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=167.84899433219672 g (allowed None … 113.0); guide_departure_m_s=8.924047847662578 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.13107714108476 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=181.7489943321967 g (allowed None … 85.0); apogee_m=4.983759725622666 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.548339003643651 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.638100711752855 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=181.7489943321967 g (allowed None … 85.0); apogee_m=4.976415843209677 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.543272274952189 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.095195771243045 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=184.2989943321967 g (allowed None … 99.0); apogee_m=18.135927260262896 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.214480728884048 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.558567247222896 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=184.2989943321967 g (allowed None … 99.0); apogee_m=17.527021986016834 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.208720140573214 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.680482782751287 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.018791322005612 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.013141356458558 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.018791322005612 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.813444832624857 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.013141356458558 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.967351176366098 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=181.7489943321967 g (allowed None … 85.0); apogee_m=4.983759725622666 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.548339003643651 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.638100711752855 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=181.7489943321967 g (allowed None … 85.0); apogee_m=4.976415843209677 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.543272274952189 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.095195771243045 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=184.2989943321967 g (allowed None … 99.0); apogee_m=18.135927260262896 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.214480728884048 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.558567247222896 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=184.2989943321967 g (allowed None … 99.0); apogee_m=17.527021986016834 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.208720140573214 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.680482782751287 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.018791322005612
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.013141356458558
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.018791322005612
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.813444832624857 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=188.49899433219673 g (allowed None … 113.0); guide_departure_m_s=8.013141356458558
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.967351176366098 m/s (allowed None … 10.0)
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
