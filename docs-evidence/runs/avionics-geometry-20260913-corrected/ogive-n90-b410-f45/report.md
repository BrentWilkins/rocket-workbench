# Rocket Workbench report

Run: `ogive-n90-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `827b432aa79a30a1568f8f4d4accaf7f2e9d1f03b95254e97d98ec3710c7a43f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.92 |      6.52 |           1.89 | unavailable |       10.97 |    0.24 |            5.26 |             6.26 |              8.21 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.90 |      6.51 |           0.68 | unavailable |       10.33 |    0.70 |            5.26 |             6.26 |              8.19 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.49 |      8.21 |           1.70 |       15.72 |        5.69 |    3.84 |            7.06 |             8.06 |             16.84 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.88 |      8.20 |           0.74 |       16.29 |        5.97 |    5.01 |            7.06 |             8.06 |             16.63 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.34 |      8.98 |           1.72 |        1.74 |        4.86 |    0.04 |            7.70 |             8.70 |             34.48 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.90 |      8.97 |           1.07 |        5.91 |        4.86 |    8.27 |            7.69 |             8.69 |             34.32 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.35 |      8.98 |           1.54 |       12.88 |        4.86 |    1.85 |            7.70 |             8.70 |             34.48 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.92 |      8.97 |           1.07 |       18.48 |        4.86 |    9.52 |            7.69 |             8.69 |             34.32 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.40 |     13.04 |           1.08 |        4.50 |        4.87 |    0.01 |           11.65 |            12.65 |             26.52 |
| empty-C5-3-wind2  | completed / outside configured limits |    69.73 |     13.03 |           0.99 |        5.52 |        4.87 |   11.22 |           11.64 |            12.64 |             26.36 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.09 |      5.60 |           2.32 | unavailable |        9.77 |    0.10 |            4.54 |             5.54 |              6.61 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.08 |      5.60 |           1.11 | unavailable |        9.18 |    0.46 |            4.54 |             5.54 |              6.59 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.49 |      7.29 |           2.24 | unavailable |       14.43 |    0.64 |            6.15 |             7.14 |             13.91 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.97 |      7.28 |           1.17 | unavailable |       17.63 |    6.62 |            6.14 |             7.14 |             13.72 |
| dummy-C6-3-wind0  | completed / outside configured limits |    69.84 |      8.06 |           2.00 |        2.19 |        5.18 |    0.03 |            6.73 |             7.73 |             29.16 |
| dummy-C6-3-wind2  | completed / outside configured limits |    65.95 |      8.05 |           1.46 |        7.33 |        5.18 |    3.97 |            6.73 |             7.73 |             29.03 |
| dummy-C6-5-wind0  | completed / outside configured limits |    69.84 |      8.06 |           2.00 |       15.54 |        5.18 |    0.16 |            6.73 |             7.73 |             29.16 |
| dummy-C6-5-wind2  | completed / outside configured limits |    65.95 |      8.05 |           1.46 |       22.51 |        5.18 |   25.92 |            6.73 |             7.73 |             29.03 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.74 |     12.31 |           2.06 |        8.26 |        5.18 |    0.10 |           10.24 |            11.24 |             21.92 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.86 |     12.30 |           1.59 |        9.40 |        5.18 |    0.29 |           10.23 |            11.23 |             21.79 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.09 |      5.60 |           2.32 | unavailable |        9.77 |    0.10 |            4.54 |             5.54 |              6.61 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.08 |      5.60 |           1.11 | unavailable |        9.18 |    0.46 |            4.54 |             5.54 |              6.59 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.49 |      7.29 |           2.24 | unavailable |       14.43 |    0.64 |            6.15 |             7.14 |             13.91 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.97 |      7.28 |           1.17 | unavailable |       17.63 |    6.62 |            6.14 |             7.14 |             13.72 |
| actual-C6-3-wind0 | completed / outside configured limits |    69.84 |      8.06 |           2.00 |        2.19 |        5.18 |    0.03 |            6.73 |             7.73 |             29.16 |
| actual-C6-3-wind2 | completed / outside configured limits |    65.95 |      8.05 |           1.46 |        7.33 |        5.18 |    3.97 |            6.73 |             7.73 |             29.03 |
| actual-C6-5-wind0 | completed / outside configured limits |    69.84 |      8.06 |           2.00 |       15.54 |        5.18 |    0.16 |            6.73 |             7.73 |             29.16 |
| actual-C6-5-wind2 | completed / outside configured limits |    65.95 |      8.05 |           1.46 |       22.51 |        5.18 |   25.92 |            6.73 |             7.73 |             29.03 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.74 |     12.31 |           2.06 |        8.26 |        5.18 |    0.10 |           10.24 |            11.24 |             21.92 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.86 |     12.30 |           1.59 |        9.40 |        5.18 |    0.29 |           10.23 |            11.23 |             21.79 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (23°); Flight Event occurred after landing: Ejection charge;
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
- actual-A8-3-wind2: Large angle of attack encountered (23°); Flight Event occurred after landing: Ejection charge;
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

- empty-A8-3-wind0: launch_mass_g=159.71517539161496 g (allowed None … 85.0); apogee_m=6.920332391459583 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.515492568686073 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.973067681722542 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=159.71517539161496 g (allowed None … 85.0); apogee_m=6.903918678560223 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.509459007175667 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6823574423560033 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.334179429811448 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=162.26517539161495 g (allowed None … 99.0); apogee_m=24.4920027211926 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.208663730940522 m/s (allowed 12.0 … None); deployment_speed_m_s=15.72468842579719 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=162.26517539161495 g (allowed None … 99.0); apogee_m=23.875069244850735 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.202227218832833 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7396705609835537 cal (allowed 1.0 … None); deployment_speed_m_s=16.292181280831937 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=166.46517539161496 g (allowed None … 113.0); guide_departure_m_s=8.97624826436247 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=166.46517539161496 g (allowed None … 113.0); guide_departure_m_s=8.970086400310311 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=166.46517539161496 g (allowed None … 113.0); guide_departure_m_s=8.97624826436247 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.88459370399255 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=166.46517539161496 g (allowed None … 113.0); guide_departure_m_s=8.970086400310311 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.48132047660784 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: minimum_ascent_stability_cal=0.9902649846954895 cal (allowed 1.0 … None)
- dummy-A8-3-wind0: launch_mass_g=180.36517539161494 g (allowed None … 85.0); apogee_m=5.085479065303943 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.603930414311126 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.76997706851393 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=180.36517539161494 g (allowed None … 85.0); apogee_m=5.077701539154225 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.598988849432147 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.17515564083861 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=182.91517539161495 g (allowed None … 99.0); apogee_m=18.493178479967227 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.287652302493082 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=14.428716146702874 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=182.91517539161495 g (allowed None … 99.0); apogee_m=17.967032485683784 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.281985759983079 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.62688117596309 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.058119074394067 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.052683520530042 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.058119074394067 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.539965632117998 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.052683520530042 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.50866628086823 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=180.36517539161494 g (allowed None … 85.0); apogee_m=5.085479065303943 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.603930414311126 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.76997706851393 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=180.36517539161494 g (allowed None … 85.0); apogee_m=5.077701539154225 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.598988849432147 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.17515564083861 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=182.91517539161495 g (allowed None … 99.0); apogee_m=18.493178479967227 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.287652302493082 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=14.42871614670287 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=182.91517539161495 g (allowed None … 99.0); apogee_m=17.967032485683784 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.281985759983079 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.626881175963113 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.058119074394067
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.052683520530042
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.058119074394067
  m/s (allowed 12.0 … None); deployment_speed_m_s=15.539965632118 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=187.11517539161497 g (allowed None … 113.0); guide_departure_m_s=8.052683520530042
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.508666280868216 m/s (allowed None … 10.0)
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
