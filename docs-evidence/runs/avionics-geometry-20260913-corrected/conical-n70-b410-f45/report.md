# Rocket Workbench report

Run: `conical-n70-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `8b3d8e89369426d36dd70a07a26a96118c0d5220546ccf4ccc511e61f60b190d`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.55 |      6.78 |           1.78 | unavailable |       11.21 |    0.30 |            5.49 |             6.49 |              8.72 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.52 |      6.78 |           0.70 | unavailable |       10.62 |    0.63 |            5.49 |             6.48 |              8.70 |
| empty-B4-4-wind0  | completed / outside configured limits |    26.39 |      8.50 |           1.43 |       14.93 |        4.78 |    3.49 |            7.35 |             8.35 |             17.73 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.68 |      8.50 |           0.73 |       15.81 |        4.74 |    4.58 |            7.35 |             8.35 |             17.51 |
| empty-C6-3-wind0  | completed / outside configured limits |    92.75 |      9.27 |           1.62 |        2.43 |        4.78 |    0.04 |            8.00 |             9.00 |             35.91 |
| empty-C6-3-wind2  | completed / outside configured limits |    89.25 |      9.26 |           1.05 |        5.96 |        4.78 |   10.77 |            8.00 |             9.00 |             35.74 |
| empty-C6-5-wind0  | completed / outside configured limits |    92.79 |      9.27 |           1.48 |       12.48 |        4.78 |    1.54 |            8.00 |             9.00 |             35.91 |
| empty-C6-5-wind2  | completed / outside configured limits |    89.29 |      9.26 |           1.05 |       17.79 |        4.78 |    6.43 |            8.00 |             9.00 |             35.74 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    75.51 |     13.17 |           1.30 |        3.70 |        4.78 |    0.02 |           12.09 |            13.09 |             27.73 |
| empty-C5-3-wind2  | completed / outside configured limits |    73.84 |     13.16 |           0.99 |        4.90 |        4.78 |   13.93 |           12.08 |            13.08 |             27.56 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.51 |      5.84 |           2.26 | unavailable |       10.13 |    0.13 |            4.72 |             5.72 |              7.00 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.50 |      5.84 |           1.18 | unavailable |        9.44 |    0.39 |            4.72 |             5.72 |              6.98 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.86 |      7.51 |           2.03 | unavailable |       16.18 |    0.48 |            6.37 |             7.37 |             14.62 |
| dummy-B4-4-wind2  | completed / outside configured limits |    19.24 |      7.51 |           1.31 | unavailable |       18.36 |    7.44 |            6.37 |             7.37 |             14.40 |
| dummy-C6-3-wind0  | completed / outside configured limits |    73.67 |      8.30 |           1.94 |        1.41 |        5.09 |    0.03 |            6.97 |             7.97 |             30.37 |
| dummy-C6-3-wind2  | completed / outside configured limits |    69.70 |      8.29 |           1.49 |        7.00 |        5.09 |    2.13 |            6.97 |             7.97 |             30.23 |
| dummy-C6-5-wind0  | completed / outside configured limits |    73.67 |      8.30 |           1.94 |       15.90 |        5.09 |    0.41 |            6.97 |             7.97 |             30.37 |
| dummy-C6-5-wind2  | completed / outside configured limits |    69.70 |      8.29 |           1.49 |       21.74 |        5.09 |   23.53 |            6.97 |             7.97 |             30.23 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    59.10 |     12.59 |           1.68 |        7.48 |        5.10 |    0.06 |           10.59 |            11.59 |             22.96 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    57.24 |     12.59 |           1.66 |        8.65 |        5.10 |    2.59 |           10.58 |            11.58 |             22.81 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.51 |      5.84 |           2.26 | unavailable |       10.13 |    0.13 |            4.72 |             5.72 |              7.00 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.50 |      5.84 |           1.18 | unavailable |        9.44 |    0.39 |            4.72 |             5.72 |              6.98 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.86 |      7.51 |           2.03 | unavailable |       16.18 |    0.48 |            6.37 |             7.37 |             14.62 |
| actual-B4-4-wind2 | completed / outside configured limits |    19.24 |      7.51 |           1.31 | unavailable |       18.36 |    7.44 |            6.37 |             7.37 |             14.40 |
| actual-C6-3-wind0 | completed / outside configured limits |    73.67 |      8.30 |           1.94 |        1.41 |        5.09 |    0.03 |            6.97 |             7.97 |             30.37 |
| actual-C6-3-wind2 | completed / outside configured limits |    69.70 |      8.29 |           1.49 |        7.00 |        5.09 |    2.13 |            6.97 |             7.97 |             30.23 |
| actual-C6-5-wind0 | completed / outside configured limits |    73.67 |      8.30 |           1.94 |       15.90 |        5.09 |    0.41 |            6.97 |             7.97 |             30.37 |
| actual-C6-5-wind2 | completed / outside configured limits |    69.70 |      8.29 |           1.49 |       21.74 |        5.09 |   23.53 |            6.97 |             7.97 |             30.23 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    59.10 |     12.59 |           1.68 |        7.48 |        5.10 |    0.06 |           10.59 |            11.59 |             22.96 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    57.24 |     12.59 |           1.66 |        8.65 |        5.10 |    2.59 |           10.58 |            11.58 |             22.81 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (18.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (21.7 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (21.7 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=154.108136936726 g (allowed None … 85.0); apogee_m=7.546955859499258 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.784042852270746 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=11.20580460544907 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=154.108136936726 g (allowed None … 85.0); apogee_m=7.51974846095261 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.777226507852196 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.698688284950668 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=10.621509583869264 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=156.658136936726 g (allowed None … 99.0); apogee_m=26.390372462334913 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.5043702893207 m/s (allowed 12.0 … None); deployment_speed_m_s=14.932036499836409 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=156.658136936726 g (allowed None … 99.0); apogee_m=25.678249326718333 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.497132172193945 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7346059744315167 cal (allowed 1.0 … None); deployment_speed_m_s=15.806559300829408 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=160.85813693672603 g (allowed None … 113.0); guide_departure_m_s=9.266754028025117 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=160.85813693672603 g (allowed None … 113.0); guide_departure_m_s=9.259838103108754 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=160.85813693672603 g (allowed None … 113.0); guide_departure_m_s=9.266754028025117 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.480061410279257 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=160.85813693672603 g (allowed None … 113.0); guide_departure_m_s=9.259838103108754 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.794758240573447 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: minimum_ascent_stability_cal=0.9913782254631266 cal (allowed 1.0 … None)
- dummy-A8-3-wind0: launch_mass_g=174.758136936726 g (allowed None … 85.0); apogee_m=5.511598757794435 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.843667167526893 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=10.134586020187458 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=174.758136936726 g (allowed None … 85.0); apogee_m=5.499841317052784 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.8379921706802635 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.44431972901429 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=177.30813693672602 g (allowed None … 99.0); apogee_m=19.863962328130153 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.513418736491408 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.178544500837308 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=177.30813693672602 g (allowed None … 99.0); apogee_m=19.242221455902637 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.507118432183771 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.36444735309837 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.300807880558807 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.294707336771765 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.300807880558807 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.898546404730865 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.294707336771765 m/s
  (allowed 12.0 … None); deployment_speed_m_s=21.737025410117674 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=174.758136936726 g (allowed None … 85.0); apogee_m=5.511598757794435 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.843667167526893 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.134586020187458 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=174.758136936726 g (allowed None … 85.0); apogee_m=5.499841317052784 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.8379921706802635 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.444319729014289 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=177.30813693672602 g (allowed None … 99.0); apogee_m=19.863962328130153 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.513418736491408 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.178544500837308 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=177.30813693672602 g (allowed None … 99.0); apogee_m=19.242221455902634 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.507118432183771 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.36444735309836 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.300807880558807 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.294707336771765 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.300807880558807 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.898546404730865 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=181.508136936726 g (allowed None … 113.0); guide_departure_m_s=8.294707336771765 m/s
  (allowed 12.0 … None); deployment_speed_m_s=21.737025410117713 m/s (allowed None … 10.0)
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
