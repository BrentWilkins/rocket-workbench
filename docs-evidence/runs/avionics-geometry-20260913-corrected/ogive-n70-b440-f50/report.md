# Rocket Workbench report

Run: `ogive-n70-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `808d115268e79c87a3f52a8819d6dd5826f0f4927c9dd0061c2bf056ae477dfd`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.82 |      6.46 |           2.35 | unavailable |       10.81 |    0.27 |            5.22 |             6.22 |              8.13 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.80 |      6.46 |           1.03 | unavailable |       10.00 |    0.47 |            5.22 |             6.22 |              8.11 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.11 |      8.18 |           2.23 |       12.30 |        5.14 |    1.04 |            7.01 |             8.01 |             16.67 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.39 |      8.17 |           1.13 | unavailable |       19.83 |    9.28 |            7.01 |             8.01 |             16.45 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.70 |      8.91 |           2.18 |        1.33 |        4.88 |    0.04 |            7.65 |             8.65 |             34.10 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.87 |      8.91 |           1.48 |        6.25 |        4.88 |    5.53 |            7.65 |             8.64 |             33.95 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.71 |      8.91 |           1.93 |       12.12 |        4.88 |    1.10 |            7.65 |             8.65 |             34.10 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.87 |      8.91 |           1.48 |       19.12 |        4.88 |   13.45 |            7.65 |             8.64 |             33.95 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    70.14 |     12.95 |           1.95 |        4.84 |        4.89 |    0.00 |           11.57 |            12.57 |             26.19 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.38 |     12.95 |           1.52 |        6.00 |        4.89 |    9.89 |           11.57 |            12.57 |             26.02 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.02 |      5.57 |           2.84 | unavailable |        9.70 |    0.12 |            4.51 |             5.51 |              6.54 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.01 |      5.56 |           1.53 | unavailable |        9.07 |    0.38 |            4.51 |             5.51 |              6.53 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.24 |      7.24 |           2.62 | unavailable |       15.76 |    0.56 |            6.11 |             7.11 |             13.78 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.62 |      7.23 |           1.71 | unavailable |       17.77 |    7.14 |            6.11 |             7.11 |             13.56 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.70 |      8.04 |           2.39 |        2.50 |        5.19 |    0.03 |            6.69 |             7.69 |             28.87 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.51 |      8.04 |           1.92 |        7.80 |        5.19 |    5.98 |            6.69 |             7.69 |             28.76 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.70 |      8.04 |           2.39 |       17.09 |        5.19 |    1.10 |            6.69 |             7.69 |             28.87 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.51 |      8.04 |           1.92 |       22.91 |        5.19 |   28.75 |            6.69 |             7.69 |             28.76 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.87 |     12.24 |           2.05 |        8.49 |        5.20 |    0.14 |           10.18 |            11.18 |             21.67 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    52.93 |     12.23 |           2.14 |        9.79 |        5.20 |    0.63 |           10.18 |            11.18 |             21.53 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.02 |      5.57 |           2.84 | unavailable |        9.70 |    0.12 |            4.51 |             5.51 |              6.54 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.01 |      5.56 |           1.53 | unavailable |        9.07 |    0.38 |            4.51 |             5.51 |              6.53 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.24 |      7.24 |           2.62 | unavailable |       15.76 |    0.56 |            6.11 |             7.11 |             13.78 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.62 |      7.23 |           1.71 | unavailable |       17.77 |    7.14 |            6.11 |             7.11 |             13.56 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.70 |      8.04 |           2.39 |        2.50 |        5.19 |    0.03 |            6.69 |             7.69 |             28.87 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.51 |      8.04 |           1.92 |        7.80 |        5.19 |    5.98 |            6.69 |             7.69 |             28.76 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.70 |      8.04 |           2.39 |       17.09 |        5.19 |    1.10 |            6.69 |             7.69 |             28.87 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.51 |      8.04 |           1.92 |       22.91 |        5.19 |   28.75 |            6.69 |             7.69 |             28.76 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.87 |     12.24 |           2.05 |        8.49 |        5.20 |    0.14 |           10.18 |            11.18 |             21.67 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    52.93 |     12.23 |           2.14 |        9.79 |        5.20 |    0.63 |           10.18 |            11.18 |             21.53 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (19.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.9 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (19.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.9 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=160.6389449487435 g (allowed None … 85.0); apogee_m=6.816423324528452 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.461238417733417 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.80570434932369 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=160.6389449487435 g (allowed None … 85.0); apogee_m=6.795368902455499 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.455003777560298 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.995997958868545 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=163.1889449487435 g (allowed None … 99.0); apogee_m=24.113503773211928 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.180341210069235 m/s (allowed 12.0 … None); deployment_speed_m_s=12.299844679817479 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=163.1889449487435 g (allowed None … 99.0); apogee_m=23.3855120801099 m (allowed 30.0 …
  120.0); guide_departure_m_s=8.173527382455319 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=19.825998308815766 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=167.3889449487435 g (allowed None … 113.0); guide_departure_m_s=8.912771691198722 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=167.3889449487435 g (allowed None … 113.0); guide_departure_m_s=8.906374215128938 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=167.3889449487435 g (allowed None … 113.0); guide_departure_m_s=8.912771691198722 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.11838931443287 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=167.3889449487435 g (allowed None … 113.0); guide_departure_m_s=8.906374215128938 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.116248582166296 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=181.2889449487435 g (allowed None … 85.0); apogee_m=5.015966323140885 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.569814999088812 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.698988596173672 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=181.2889449487435 g (allowed None … 85.0); apogee_m=5.008310019729688 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.564698996985576 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.06616277521673 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=183.83894494874352 g (allowed None … 99.0); apogee_m=18.237732395091523 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.238317516464488 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.757079591831246 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=183.83894494874352 g (allowed None … 99.0); apogee_m=17.62063371821098 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.232438774405496 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.76705920630883 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.044368693269469 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.038606626123965 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.044368693269469 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.090733652397162 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.038606626123965 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.909784925010623 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=181.2889449487435 g (allowed None … 85.0); apogee_m=5.015966323140885 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.569814999088812 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.698988596173672 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=181.2889449487435 g (allowed None … 85.0); apogee_m=5.008310019729688 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.564698996985576 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.06616277521673 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=183.83894494874352 g (allowed None … 99.0); apogee_m=18.237732395091523 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.238317516464488 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.757079591831252 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=183.83894494874352 g (allowed None … 99.0); apogee_m=17.620633718210975 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.232438774405496 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.767059206308772 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.044368693269469 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.038606626123965 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.044368693269469 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.090733652397173 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=188.0389449487435 g (allowed None … 113.0); guide_departure_m_s=8.038606626123965 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.909784925010587 m/s (allowed None … 10.0)
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
