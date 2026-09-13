# Rocket Workbench report

Run: `ogive-n90-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `dbf962e3f059907fb3c943d21ce8140a3649c98660d4dbab6e12a14f0123a39f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.62 |      6.39 |           2.22 | unavailable |       10.60 |    0.28 |            5.15 |             6.15 |              7.97 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.60 |      6.38 |           0.99 | unavailable |        9.84 |    0.38 |            5.15 |             6.15 |              7.95 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.47 |      8.09 |           2.17 |       12.47 |        5.77 |    1.38 |            6.92 |             7.92 |             16.38 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.70 |      8.09 |           1.13 | unavailable |       19.78 |    9.54 |            6.92 |             7.92 |             16.14 |
| empty-C6-3-wind0  | completed / outside configured limits |    84.59 |      8.84 |           2.09 |        0.87 |        4.91 |    0.04 |            7.55 |             8.55 |             33.54 |
| empty-C6-3-wind2  | completed / outside configured limits |    80.51 |      8.83 |           1.45 |        6.50 |        4.91 |    3.24 |            7.55 |             8.55 |             33.39 |
| empty-C6-5-wind0  | completed / outside configured limits |    84.59 |      8.84 |           1.97 |       12.08 |        4.91 |    1.01 |            7.55 |             8.55 |             33.54 |
| empty-C6-5-wind2  | completed / outside configured limits |    80.51 |      8.83 |           1.45 |       19.66 |        4.91 |   16.64 |            7.55 |             8.55 |             33.39 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    68.39 |     12.89 |           1.63 |        5.27 |        4.92 |    0.01 |           11.44 |            12.43 |             25.70 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    66.58 |     12.88 |           1.56 |        6.47 |        4.92 |    8.48 |           11.43 |            12.43 |             25.53 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.88 |      5.49 |           2.69 | unavailable |        9.51 |    0.12 |            4.46 |             5.45 |              6.41 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.88 |      5.49 |           1.45 | unavailable |        9.00 |    0.33 |            4.45 |             5.45 |              6.40 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.79 |      7.17 |           2.64 | unavailable |       15.66 |    0.50 |            6.04 |             7.04 |             13.55 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.11 |      7.16 |           1.71 | unavailable |       17.61 |    7.58 |            6.04 |             7.04 |             13.31 |
| dummy-C6-3-wind0  | completed / outside configured limits |    67.09 |      7.94 |           2.24 |        2.90 |        5.22 |    0.02 |            6.62 |             7.62 |             28.41 |
| dummy-C6-3-wind2  | completed / outside configured limits |    62.64 |      7.94 |           1.85 |        8.29 |        5.22 |    8.09 |            6.62 |             7.62 |             28.32 |
| dummy-C6-5-wind0  | completed / outside configured limits |    67.09 |      7.94 |           2.24 |       17.70 |        5.22 |    0.95 |            6.62 |             7.62 |             28.41 |
| dummy-C6-5-wind2  | completed / outside configured limits |    62.64 |      7.94 |           1.85 |       23.37 |        5.22 |   31.68 |            6.62 |             7.62 |             28.32 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    53.57 |     12.25 |           2.26 |        8.80 |        5.22 |    0.19 |           10.07 |            11.07 |             21.27 |
| dummy-C5-3-wind2  | completed / outside configured limits |    51.56 |     12.24 |           2.05 |       10.26 |        5.22 |    1.87 |           10.07 |            11.07 |             21.14 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.88 |      5.49 |           2.69 | unavailable |        9.51 |    0.12 |            4.46 |             5.45 |              6.41 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.88 |      5.49 |           1.45 | unavailable |        9.00 |    0.33 |            4.45 |             5.45 |              6.40 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.79 |      7.17 |           2.64 | unavailable |       15.66 |    0.50 |            6.04 |             7.04 |             13.55 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.11 |      7.16 |           1.71 | unavailable |       17.61 |    7.58 |            6.04 |             7.04 |             13.31 |
| actual-C6-3-wind0 | completed / outside configured limits |    67.09 |      7.94 |           2.24 |        2.90 |        5.22 |    0.02 |            6.62 |             7.62 |             28.41 |
| actual-C6-3-wind2 | completed / outside configured limits |    62.64 |      7.94 |           1.85 |        8.29 |        5.22 |    8.09 |            6.62 |             7.62 |             28.32 |
| actual-C6-5-wind0 | completed / outside configured limits |    67.09 |      7.94 |           2.24 |       17.70 |        5.22 |    0.95 |            6.62 |             7.62 |             28.41 |
| actual-C6-5-wind2 | completed / outside configured limits |    62.64 |      7.94 |           1.85 |       23.37 |        5.22 |   31.68 |            6.62 |             7.62 |             28.32 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    53.57 |     12.25 |           2.26 |        8.80 |        5.22 |    0.19 |           10.07 |            11.07 |             21.27 |
| actual-C5-3-wind2 | completed / outside configured limits |    51.56 |     12.24 |           2.05 |       10.26 |        5.22 |    1.87 |           10.07 |            11.07 |             21.14 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (18.1°); Flight Event occurred after landing: Ejection charge;
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
- actual-A8-3-wind2: Large angle of attack encountered (18.1°); Flight Event occurred after landing: Ejection charge;
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

- empty-A8-3-wind0: launch_mass_g=162.4828170809913 g (allowed None … 85.0); apogee_m=6.6232725976870395 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.387962504767407 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.599216470232198 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=162.4828170809913 g (allowed None … 85.0); apogee_m=6.599990622310525 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.381597987246607 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9930533601497038 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.839254338691537 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=165.0328170809913 g (allowed None … 99.0); apogee_m=23.46861404142813 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.092347762400248 m/s (allowed 12.0 … None); deployment_speed_m_s=12.470980982552927 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=165.0328170809913 g (allowed None … 99.0); apogee_m=22.698266167933944 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.087477949301237 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.778511557147137 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=169.2328170809913 g (allowed None … 113.0); guide_departure_m_s=8.837299765403175 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=169.2328170809913 g (allowed None … 113.0); guide_departure_m_s=8.830786052010568 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=169.2328170809913 g (allowed None … 113.0); guide_departure_m_s=8.837299765403175 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.082317724438923 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=169.2328170809913 g (allowed None … 113.0); guide_departure_m_s=8.830786052010568 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.661193450387046 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=183.1328170809913 g (allowed None … 85.0); apogee_m=4.884625898286162 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.493148948668728 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.50874254702935 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=183.1328170809913 g (allowed None … 85.0); apogee_m=4.877314882756445 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.487957414241756 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.997789970900225 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=185.6828170809913 g (allowed None … 99.0); apogee_m=17.788200293950872 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.166522374462013 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.655096658284497 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=185.6828170809913 g (allowed None … 99.0); apogee_m=17.113558942767536 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.160566552777515 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.60708480818775 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.941496366371386 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.93575332927911 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.941496366371386 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.702671582526754 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.93575332927911 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.373840445378136 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.258563047817253 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=183.1328170809913 g (allowed None … 85.0); apogee_m=4.884625898286162 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.493148948668728 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.50874254702935 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=183.1328170809913 g (allowed None … 85.0); apogee_m=4.877314882756445 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.487957414241756 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.997789970900225 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=185.6828170809913 g (allowed None … 99.0); apogee_m=17.788200293950872 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.166522374462013 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.655096658284496 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=185.6828170809913 g (allowed None … 99.0); apogee_m=17.113558942767536 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.160566552777515 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.60708480818757 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.941496366371386
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.93575332927911 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.941496366371386
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.70267158252676 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=189.88281708099132 g (allowed None … 113.0); guide_departure_m_s=7.93575332927911 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.373840445378214 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.258563047817214 m/s (allowed None … 10.0)

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
