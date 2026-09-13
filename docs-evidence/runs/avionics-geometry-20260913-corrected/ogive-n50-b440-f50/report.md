# Rocket Workbench report

Run: `ogive-n50-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `e07d23e6e05b2a3471678408225290a24dd57d59b9a80471144463dd943cf46c`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.02 |      6.56 |           2.31 | unavailable |       10.88 |    0.29 |            5.30 |             6.30 |              8.30 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.00 |      6.55 |           1.07 | unavailable |       10.05 |    0.40 |            5.30 |             6.30 |              8.28 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.78 |      8.27 |           2.17 |       14.14 |        4.98 |    0.03 |            7.11 |             8.11 |             16.98 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.01 |      8.27 |           1.16 |       20.03 |       16.17 |    9.49 |            7.11 |             8.11 |             16.75 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.66 |      9.04 |           2.14 |        1.72 |        4.85 |    0.04 |            7.75 |             8.75 |             34.66 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.77 |      9.04 |           1.49 |        6.32 |        4.85 |    6.34 |            7.75 |             8.75 |             34.50 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.68 |      9.04 |           1.89 |       12.24 |        4.85 |    0.90 |            7.75 |             8.75 |             34.66 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.78 |      9.04 |           1.49 |       18.81 |        4.85 |   12.48 |            7.75 |             8.75 |             34.50 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.82 |     13.13 |           1.90 |        4.46 |        4.86 |    0.01 |           11.72 |            12.72 |             26.67 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.06 |     13.12 |           1.55 |        5.73 |        4.86 |   10.86 |           11.71 |            12.71 |             26.50 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.16 |      5.65 |           2.75 | unavailable |        9.82 |    0.13 |            4.57 |             5.57 |              6.67 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.15 |      5.65 |           1.57 | unavailable |        9.19 |    0.33 |            4.57 |             5.57 |              6.66 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.71 |      7.32 |           2.73 | unavailable |       15.94 |    0.65 |            6.19 |             7.18 |             14.03 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.05 |      7.31 |           1.80 | unavailable |       18.02 |    7.48 |            6.18 |             7.18 |             13.80 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.25 |      8.11 |           2.11 |        2.14 |        5.16 |    0.03 |            6.77 |             7.77 |             29.32 |
| dummy-C6-3-wind2  | completed / outside configured limits |    65.98 |      8.11 |           1.95 |        7.70 |        5.16 |    5.52 |            6.77 |             7.77 |             29.21 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.25 |      8.11 |           2.11 |       16.91 |        5.16 |    1.25 |            6.77 |             7.77 |             29.32 |
| dummy-C6-5-wind2  | completed / outside configured limits |    65.98 |      8.11 |           1.95 |       22.63 |        5.16 |   28.22 |            6.77 |             7.77 |             29.21 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.16 |     12.39 |           2.51 |        8.17 |        5.17 |    0.12 |           10.30 |            11.30 |             22.06 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.21 |     12.38 |           2.15 |        9.51 |        5.17 |    0.08 |           10.29 |            11.29 |             21.92 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.16 |      5.65 |           2.75 | unavailable |        9.82 |    0.13 |            4.57 |             5.57 |              6.67 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.15 |      5.65 |           1.57 | unavailable |        9.19 |    0.33 |            4.57 |             5.57 |              6.66 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.71 |      7.32 |           2.73 | unavailable |       15.94 |    0.65 |            6.19 |             7.18 |             14.03 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.05 |      7.31 |           1.80 | unavailable |       18.02 |    7.48 |            6.18 |             7.18 |             13.80 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.25 |      8.11 |           2.11 |        2.14 |        5.16 |    0.03 |            6.77 |             7.77 |             29.32 |
| actual-C6-3-wind2 | completed / outside configured limits |    65.98 |      8.11 |           1.95 |        7.70 |        5.16 |    5.52 |            6.77 |             7.77 |             29.21 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.25 |      8.11 |           2.11 |       16.91 |        5.16 |    1.25 |            6.77 |             7.77 |             29.32 |
| actual-C6-5-wind2 | completed / outside configured limits |    65.98 |      8.11 |           1.95 |       22.63 |        5.16 |   28.22 |            6.77 |             7.77 |             29.21 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.16 |     12.39 |           2.51 |        8.17 |        5.17 |    0.12 |           10.30 |            11.30 |             22.06 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.21 |     12.38 |           2.15 |        9.51 |        5.17 |    0.08 |           10.29 |            11.29 |             21.92 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Recovery device deployment at high speed (20 m/s): "Nominal 457 mm parachute and lines"
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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.6 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (22.6 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=158.70856437762518 g (allowed None … 85.0); apogee_m=7.024107414011808 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.561046313141838 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.877628076295741 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=158.70856437762518 g (allowed None … 85.0); apogee_m=6.998677616845056 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.554675116232577 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.047988649721448 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=161.25856437762516 g (allowed None … 99.0); apogee_m=24.779091781790232 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.272998628489761 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.144393721511262 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=161.25856437762516 g (allowed None … 99.0); apogee_m=24.01293631427321 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.266146504772147 m/s (allowed 12.0 … None); deployment_speed_m_s=20.0302551270774 m/s
  (allowed None … 10.0); landing_descent_m_s=16.165421572545753 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=165.45856437762518 g (allowed None … 113.0); guide_departure_m_s=9.044417897213252 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=165.45856437762518 g (allowed None … 113.0); guide_departure_m_s=9.037864151814917 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=165.45856437762518 g (allowed None … 113.0); guide_departure_m_s=9.044417897213252 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.24121960823776 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=165.45856437762518 g (allowed None … 113.0); guide_departure_m_s=9.037864151814917 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.81009209174829 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=179.35856437762519 g (allowed None … 85.0); apogee_m=5.157198863547066 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.6516015602415015 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.817800923489122 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=179.35856437762519 g (allowed None … 85.0); apogee_m=5.148399966556456 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.646320319486221 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.18564525071165 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=181.90856437762517 g (allowed None … 99.0); apogee_m=18.709676924091 m (allowed 30.0 …
  120.0); guide_departure_m_s=7.315370689201041 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=15.935839775391965 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=181.90856437762517 g (allowed None … 99.0); apogee_m=18.051427090049224 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.309450235679446 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.023463627672967 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.114526662484614 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.108748926118453 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.114526662484614 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.913724585960153 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.108748926118453 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.6336433516111 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=179.35856437762519 g (allowed None … 85.0); apogee_m=5.157198863547066 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.6516015602415015 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=9.817800923489122 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=179.35856437762519 g (allowed None … 85.0); apogee_m=5.148399966556456 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.646320319486221 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.18564525071165 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=181.90856437762517 g (allowed None … 99.0); apogee_m=18.709676924091 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.315370689201041 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.935839775391967 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=181.90856437762517 g (allowed None … 99.0); apogee_m=18.051427090049224 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.309450235679446 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.023463627672903 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.114526662484614
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.108748926118453
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.114526662484614
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.913724585960153 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=186.10856437762519 g (allowed None … 113.0); guide_departure_m_s=8.108748926118453
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.633643351611138 m/s (allowed None … 10.0)
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
