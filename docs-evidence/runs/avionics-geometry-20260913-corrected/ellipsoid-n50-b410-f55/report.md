# Rocket Workbench report

Run: `ellipsoid-n50-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `b31016f581ccdd3b8fa4fb0f0a37cda4ca6d1967d7829891b5317254283cadba`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.89 |      6.50 |           2.19 | unavailable |       10.62 |    0.30 |            5.25 |             6.25 |              8.19 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.85 |      6.49 |           1.08 | unavailable |        9.99 |    0.24 |            5.25 |             6.25 |              8.16 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.32 |      8.22 |           2.08 |       16.19 |        6.21 |    0.08 |            7.05 |             8.05 |             16.77 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.49 |      8.22 |           1.22 | unavailable |       20.31 |    9.81 |            7.05 |             8.04 |             16.54 |
| empty-C6-3-wind0  | completed / outside configured limits |    87.15 |      8.96 |           2.04 |        1.39 |        4.87 |    0.04 |            7.69 |             8.68 |             34.26 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.92 |      8.95 |           1.47 |        6.62 |        4.87 |    3.98 |            7.68 |             8.68 |             34.11 |
| empty-C6-5-wind0  | completed / outside configured limits |    87.15 |      8.96 |           1.58 |       12.73 |        4.87 |    0.49 |            7.69 |             8.68 |             34.26 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.92 |      8.95 |           1.47 |       19.31 |        4.87 |   15.85 |            7.68 |             8.68 |             34.11 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    70.57 |     13.01 |           1.79 |        4.76 |        4.88 |    0.00 |           11.63 |            12.62 |             26.32 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.74 |     13.01 |           1.60 |        6.10 |        4.88 |    9.70 |           11.62 |            12.62 |             26.16 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.06 |      5.59 |           2.64 | unavailable |        9.66 |    0.14 |            4.53 |             5.53 |              6.59 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.05 |      5.60 |           1.54 | unavailable |        9.21 |    0.24 |            4.53 |             5.53 |              6.57 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.39 |      7.27 |           2.61 | unavailable |       16.01 |    0.69 |            6.14 |             7.13 |             13.86 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.65 |      7.27 |           1.83 | unavailable |       17.95 |    8.10 |            6.13 |             7.13 |             13.62 |
| dummy-C6-3-wind0  | completed / outside configured limits |    69.10 |      8.04 |           2.16 |        2.42 |        5.18 |    0.03 |            6.72 |             7.72 |             29.00 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.48 |      8.04 |           1.89 |        8.20 |        5.18 |    7.72 |            6.72 |             7.72 |             28.90 |
| dummy-C6-5-wind0  | completed / outside configured limits |    69.10 |      8.04 |           2.16 |       17.51 |        5.18 |    1.27 |            6.72 |             7.72 |             29.00 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.48 |      8.04 |           1.89 |       23.06 |        5.18 |   31.34 |            6.72 |             7.72 |             28.90 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.23 |     12.29 |           1.80 |        8.39 |        5.19 |    0.16 |           10.22 |            11.22 |             21.78 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.18 |     12.28 |           2.08 |        9.90 |        5.19 |    1.11 |           10.22 |            11.22 |             21.64 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.06 |      5.59 |           2.64 | unavailable |        9.66 |    0.14 |            4.53 |             5.53 |              6.59 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.05 |      5.60 |           1.54 | unavailable |        9.21 |    0.24 |            4.53 |             5.53 |              6.57 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.39 |      7.27 |           2.61 | unavailable |       16.01 |    0.69 |            6.14 |             7.13 |             13.86 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.65 |      7.27 |           1.83 | unavailable |       17.95 |    8.10 |            6.13 |             7.13 |             13.62 |
| actual-C6-3-wind0 | completed / outside configured limits |    69.10 |      8.04 |           2.16 |        2.42 |        5.18 |    0.03 |            6.72 |             7.72 |             29.00 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.48 |      8.04 |           1.89 |        8.20 |        5.18 |    7.72 |            6.72 |             7.72 |             28.90 |
| actual-C6-5-wind0 | completed / outside configured limits |    69.10 |      8.04 |           2.16 |       17.51 |        5.18 |    1.27 |            6.72 |             7.72 |             29.00 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.48 |      8.04 |           1.89 |       23.06 |        5.18 |   31.34 |            6.72 |             7.72 |             28.90 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.23 |     12.29 |           1.80 |        8.39 |        5.19 |    0.16 |           10.22 |            11.22 |             21.78 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.18 |     12.28 |           2.08 |        9.90 |        5.19 |    1.11 |           10.22 |            11.22 |             21.64 |

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
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.1 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
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

- empty-A8-3-wind0: launch_mass_g=159.95986920628968 g (allowed None … 85.0); apogee_m=6.886439157483706 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.500076220992002 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.618977267566084 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=159.95986920628968 g (allowed None … 85.0); apogee_m=6.854683793563472 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.493904093015702 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.985282292261102 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=162.5098692062897 g (allowed None … 99.0); apogee_m=24.323973083442276 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.22366369155601 m/s (allowed 12.0 … None); deployment_speed_m_s=16.19483294918264 m/s
  (allowed None … 10.0); landing_descent_m_s=6.214673818260553 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=162.5098692062897 g (allowed None … 99.0); apogee_m=23.493862096403788 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.216680348901027 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=20.31463176857348 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=166.70986920628968 g (allowed None … 113.0); guide_departure_m_s=8.958457530881446 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=166.70986920628968 g (allowed None … 113.0); guide_departure_m_s=8.951903979947287 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=166.70986920628968 g (allowed None … 113.0); guide_departure_m_s=8.958457530881446 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.725797860646685 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=166.70986920628968 g (allowed None … 113.0); guide_departure_m_s=8.951903979947287 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.305426332914923 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=180.6098692062897 g (allowed None … 85.0); apogee_m=5.064320534359908 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.591551106509042 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.660417637803107 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=180.6098692062897 g (allowed None … 85.0); apogee_m=5.054902822362224 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.596633487100388 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.21017384148613 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=183.15986920628967 g (allowed None … 99.0); apogee_m=18.391485052934275 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.273804625888392 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.01133801019764 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=183.15986920628967 g (allowed None … 99.0); apogee_m=17.6479417627958 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.267780636564675 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.95481222379164 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.043400599921414 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.037619841071193 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.043400599921414 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.50852492561765 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.037619841071193 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.055323339913485 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=180.6098692062897 g (allowed None … 85.0); apogee_m=5.064320534359908 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.591551106509042 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.660417637803109 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=180.6098692062897 g (allowed None … 85.0); apogee_m=5.054902822362224 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.596633487100388 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.21017384148613 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=183.15986920628967 g (allowed None … 99.0); apogee_m=18.391485052934275 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.273804625888392 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.011338010197644 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=183.15986920628967 g (allowed None … 99.0); apogee_m=17.6479417627958 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.267780636564675 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.95481222379169 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.043400599921414 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.037619841071193 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.043400599921414 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.508524925617635 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=187.3598692062897 g (allowed None … 113.0); guide_departure_m_s=8.037619841071193 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.05532333991345 m/s (allowed None … 10.0)
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
