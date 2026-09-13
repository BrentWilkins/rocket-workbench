# Rocket Workbench report

Run: `conical-n50-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `6b517352889039486cbb33463b82d0c828cf623738826ee04c3ea7aedbeea9cb`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.52 |      6.77 |           1.95 | unavailable |       10.97 |    0.34 |            5.48 |             6.48 |              8.70 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.48 |      6.77 |           0.90 | unavailable |       10.34 |    0.38 |            5.48 |             6.48 |              8.67 |
| empty-B4-4-wind0  | completed / outside configured limits |    26.17 |      8.49 |           1.89 |       12.62 |        4.79 |    1.73 |            7.34 |             8.34 |             17.65 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.34 |      8.49 |           0.98 |       19.46 |        6.44 |    9.65 |            7.34 |             8.34 |             17.42 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.78 |      9.26 |           1.79 |        1.83 |        4.78 |    0.04 |            7.99 |             8.99 |             35.57 |
| empty-C6-3-wind2  | completed / outside configured limits |    86.92 |      9.25 |           1.26 |        6.07 |        4.78 |    8.32 |            7.99 |             8.99 |             35.40 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.80 |      9.26 |           1.66 |       12.03 |        4.78 |    1.07 |            7.99 |             8.99 |             35.57 |
| empty-C6-5-wind2  | completed / outside configured limits |    86.93 |      9.25 |           1.26 |       18.48 |        4.78 |    9.91 |            7.99 |             8.99 |             35.40 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    74.15 |     13.16 |           1.71 |        4.14 |        4.79 |    0.01 |           12.07 |            13.07 |             27.42 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    72.42 |     13.15 |           1.27 |        5.32 |        4.79 |   12.98 |           12.06 |            13.06 |             27.24 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.49 |      5.84 |           2.42 | unavailable |        9.98 |    0.15 |            4.71 |             5.71 |              6.99 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.48 |      5.83 |           1.39 | unavailable |        9.46 |    0.25 |            4.71 |             5.71 |              6.97 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.74 |      7.50 |           2.33 | unavailable |       16.48 |    0.69 |            6.37 |             7.37 |             14.57 |
| dummy-B4-4-wind2  | completed / outside configured limits |    19.00 |      7.50 |           1.60 | unavailable |       18.43 |    8.18 |            6.37 |             7.36 |             14.33 |
| dummy-C6-3-wind0  | completed / outside configured limits |    72.50 |      8.29 |           2.12 |        1.81 |        5.10 |    0.03 |            6.97 |             7.97 |             30.14 |
| dummy-C6-3-wind2  | completed / outside configured limits |    68.18 |      8.28 |           1.71 |        7.41 |        5.10 |    4.07 |            6.96 |             7.96 |             30.02 |
| dummy-C6-5-wind0  | completed / outside configured limits |    72.50 |      8.29 |           2.12 |       16.68 |        5.10 |    1.08 |            6.97 |             7.97 |             30.14 |
| dummy-C6-5-wind2  | completed / outside configured limits |    68.18 |      8.28 |           1.71 |       22.11 |        5.10 |   26.19 |            6.96 |             7.96 |             30.02 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    58.32 |     12.58 |           1.98 |        7.73 |        5.10 |    0.09 |           10.58 |            11.58 |             22.75 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    56.36 |     12.57 |           1.88 |        9.03 |        5.10 |    1.74 |           10.57 |            11.57 |             22.60 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.49 |      5.84 |           2.42 | unavailable |        9.98 |    0.15 |            4.71 |             5.71 |              6.99 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.48 |      5.83 |           1.39 | unavailable |        9.46 |    0.25 |            4.71 |             5.71 |              6.97 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.74 |      7.50 |           2.33 | unavailable |       16.48 |    0.69 |            6.37 |             7.37 |             14.57 |
| actual-B4-4-wind2 | completed / outside configured limits |    19.00 |      7.50 |           1.60 | unavailable |       18.43 |    8.18 |            6.37 |             7.36 |             14.33 |
| actual-C6-3-wind0 | completed / outside configured limits |    72.50 |      8.29 |           2.12 |        1.81 |        5.10 |    0.03 |            6.97 |             7.97 |             30.14 |
| actual-C6-3-wind2 | completed / outside configured limits |    68.18 |      8.28 |           1.71 |        7.41 |        5.10 |    4.07 |            6.96 |             7.96 |             30.02 |
| actual-C6-5-wind0 | completed / outside configured limits |    72.50 |      8.29 |           2.12 |       16.68 |        5.10 |    1.08 |            6.97 |             7.97 |             30.14 |
| actual-C6-5-wind2 | completed / outside configured limits |    68.18 |      8.28 |           1.71 |       22.11 |        5.10 |   26.19 |            6.96 |             7.96 |             30.02 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    58.32 |     12.58 |           1.98 |        7.73 |        5.10 |    0.09 |           10.58 |            11.58 |             22.75 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    56.36 |     12.57 |           1.88 |        9.03 |        5.10 |    1.74 |           10.57 |            11.57 |             22.60 |

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
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.1 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (22.1 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=154.23259442672267 g (allowed None … 85.0); apogee_m=7.516494824241407 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.77465015672411 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.973048531727567 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=154.23259442672267 g (allowed None … 85.0); apogee_m=7.475532471042908 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.7671176576889165 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8996876257632951 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.3358482093649 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=156.78259442672265 g (allowed None … 99.0); apogee_m=26.1652644340169 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.493805902436074 m/s (allowed 12.0 … None); deployment_speed_m_s=12.616776083792796 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=156.78259442672265 g (allowed None … 99.0); apogee_m=25.34457398725329 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.485794845853988 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9793897887627598 cal (allowed 1.0 … None); deployment_speed_m_s=19.462650701230835 m/s
  (allowed None … 10.0); landing_descent_m_s=6.444595629292348 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=160.98259442672267 g (allowed None … 113.0); guide_departure_m_s=9.255675471381835 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=160.98259442672267 g (allowed None … 113.0); guide_departure_m_s=9.2480166483266 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=160.98259442672267 g (allowed None … 113.0); guide_departure_m_s=9.255675471381835 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.029740705515007 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=160.98259442672267 g (allowed None … 113.0); guide_departure_m_s=9.2480166483266 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.4830341393753 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=174.88259442672265 g (allowed None … 85.0); apogee_m=5.494501108703305 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.836055081670987 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.983583240556705 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=174.88259442672265 g (allowed None … 85.0); apogee_m=5.479408588578435 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.829787578846068 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.464129082383586 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=177.43259442672266 g (allowed None … 99.0); apogee_m=19.74257039783403 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.504847914884496 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.47895568135695 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=177.43259442672266 g (allowed None … 99.0); apogee_m=19.0009660730156 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.497878572383728 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.426629712098137 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.291727681039982 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.284974734386367 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.291727681039982 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.6807866749819 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.284974734386367 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.113310758978614 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=174.88259442672265 g (allowed None … 85.0); apogee_m=5.494501108703305 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.836055081670987 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.983583240556705 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=174.88259442672265 g (allowed None … 85.0); apogee_m=5.479408588578435 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.829787578846068 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.464129082383586 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=177.43259442672266 g (allowed None … 99.0); apogee_m=19.74257039783403 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.504847914884496 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.47895568135695 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=177.43259442672266 g (allowed None … 99.0); apogee_m=19.0009660730156 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.497878572383728 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.426629712098194 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.291727681039982
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.284974734386367
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.291727681039982
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.680786674981874 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=181.63259442672268 g (allowed None … 113.0); guide_departure_m_s=8.284974734386367
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.113310758978585 m/s (allowed None … 10.0)
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
