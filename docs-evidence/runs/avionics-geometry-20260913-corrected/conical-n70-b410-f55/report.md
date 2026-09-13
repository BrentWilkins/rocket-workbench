# Rocket Workbench report

Run: `conical-n70-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `a0f881ca5196571c16b672722c3fa53ca53ceca14e6b65b85b4d8146b4c82517`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.21 |      6.65 |           2.06 | unavailable |       10.74 |    0.34 |            5.37 |             6.37 |              8.46 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.17 |      6.64 |           1.00 | unavailable |       10.11 |    0.27 |            5.37 |             6.37 |              8.43 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.27 |      8.36 |           1.91 |       13.23 |        4.49 |    0.03 |            7.20 |             8.20 |             17.23 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.44 |      8.35 |           1.16 |       20.07 |       11.86 |   10.01 |            7.20 |             8.20 |             17.00 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.83 |      9.12 |           1.97 |        1.55 |        4.82 |    0.04 |            7.85 |             8.85 |             34.92 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.73 |      9.11 |           1.41 |        6.36 |        4.82 |    5.84 |            7.84 |             8.84 |             34.76 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.84 |      9.12 |           1.86 |       12.19 |        4.82 |    0.77 |            7.85 |             8.85 |             34.92 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.74 |      9.11 |           1.41 |       18.94 |        4.82 |   13.30 |            7.84 |             8.84 |             34.76 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    72.31 |     13.08 |           1.60 |        4.48 |        4.83 |    0.01 |           11.86 |            12.86 |             26.86 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.53 |     13.07 |           1.48 |        5.71 |        4.83 |   11.35 |           11.85 |            12.85 |             26.70 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.29 |      5.72 |           2.60 | unavailable |        9.85 |    0.16 |            4.63 |             5.63 |              6.80 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.28 |      5.71 |           1.50 | unavailable |        9.31 |    0.22 |            4.63 |             5.63 |              6.78 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.09 |      7.39 |           2.47 | unavailable |       16.45 |    0.69 |            6.26 |             7.26 |             14.24 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.32 |      7.38 |           1.74 | unavailable |       18.20 |    8.42 |            6.26 |             7.26 |             13.99 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.76 |      8.18 |           1.90 |        2.15 |        5.14 |    0.03 |            6.85 |             7.85 |             29.58 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.21 |      8.17 |           1.85 |        7.88 |        5.14 |    6.25 |            6.85 |             7.85 |             29.47 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.76 |      8.18 |           1.90 |       17.26 |        5.14 |    1.08 |            6.85 |             7.85 |             29.58 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.21 |      8.17 |           1.85 |       22.60 |        5.14 |   29.26 |            6.85 |             7.85 |             29.47 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.78 |     12.37 |           2.29 |        8.07 |        5.14 |    0.13 |           10.41 |            11.41 |             22.27 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.76 |     12.36 |           2.03 |        9.47 |        5.14 |    0.25 |           10.40 |            11.40 |             22.12 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.29 |      5.72 |           2.60 | unavailable |        9.85 |    0.16 |            4.63 |             5.63 |              6.80 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.28 |      5.71 |           1.50 | unavailable |        9.31 |    0.22 |            4.63 |             5.63 |              6.78 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.09 |      7.39 |           2.47 | unavailable |       16.45 |    0.69 |            6.26 |             7.26 |             14.24 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.32 |      7.38 |           1.74 | unavailable |       18.20 |    8.42 |            6.26 |             7.26 |             13.99 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.76 |      8.18 |           1.90 |        2.15 |        5.14 |    0.03 |            6.85 |             7.85 |             29.58 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.21 |      8.17 |           1.85 |        7.88 |        5.14 |    6.25 |            6.85 |             7.85 |             29.47 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.76 |      8.18 |           1.90 |       17.26 |        5.14 |    1.08 |            6.85 |             7.85 |             29.58 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.21 |      8.17 |           1.85 |       22.60 |        5.14 |   29.26 |            6.85 |             7.85 |             29.47 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.78 |     12.37 |           2.29 |        8.07 |        5.14 |    0.13 |           10.41 |            11.41 |             22.27 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.76 |     12.36 |           2.03 |        9.47 |        5.14 |    0.25 |           10.40 |            11.40 |             22.12 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Recovery device deployment at high speed (20.1 m/s): "Nominal 457 mm parachute and lines"
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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.6 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=156.87577862610243 g (allowed None … 85.0); apogee_m=7.211493979214078 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.648307942284777 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.737222044348371 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=156.87577862610243 g (allowed None … 85.0); apogee_m=7.174538367418497 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.643822709481437 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.105248629840684 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=159.42577862610244 g (allowed None … 99.0); apogee_m=25.271800309935895 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.35887660305947 m/s (allowed 12.0 … None); deployment_speed_m_s=13.226186047504491
  m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=159.42577862610244 g (allowed None … 99.0); apogee_m=24.435870214325856 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.35125177015898 m/s (allowed 12.0 … None); deployment_speed_m_s=20.073297502824786
  m/s (allowed None … 10.0); landing_descent_m_s=11.863474440830933 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=163.62577862610246 g (allowed None … 113.0); guide_departure_m_s=9.119941886598713 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=163.62577862610246 g (allowed None … 113.0); guide_departure_m_s=9.112666979953248 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=163.62577862610246 g (allowed None … 113.0); guide_departure_m_s=9.119941886598713 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.192198027683897 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=163.62577862610246 g (allowed None … 113.0); guide_departure_m_s=9.112666979953248 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.93587219665796 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=177.52577862610244 g (allowed None … 85.0); apogee_m=5.288835418015122 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.716701333931301 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.849653223211348 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=177.52577862610244 g (allowed None … 85.0); apogee_m=5.276416310986506 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.711457344129102 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.306926115596216 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=180.07577862610245 g (allowed None … 99.0); apogee_m=19.092670968770296 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.386719330591868 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.454033869242092 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=180.07577862610245 g (allowed None … 99.0); apogee_m=18.321333772923804 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.380163391238045 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.201046497855867 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.178364635395281 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.171949620377902 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.178364635395281 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.262244168107326 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.171949620377902 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.601637951353272 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=177.52577862610244 g (allowed None … 85.0); apogee_m=5.288835418015122 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.716701333931301 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.849653223211348 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=177.52577862610244 g (allowed None … 85.0); apogee_m=5.276416310986506 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.711457344129102 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.306926115596216 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=180.07577862610245 g (allowed None … 99.0); apogee_m=19.092670968770296 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.386719330591868 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.454033869242092 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=180.07577862610245 g (allowed None … 99.0); apogee_m=18.3213337729238 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.380163391238045 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.201046497855987 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.178364635395281
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.171949620377902
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.178364635395281
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.262244168107326 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=184.27577862610244 g (allowed None … 113.0); guide_departure_m_s=8.171949620377902
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.6016379513533 m/s (allowed None … 10.0)
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
