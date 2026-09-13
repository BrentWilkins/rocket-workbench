# Rocket Workbench report

Run: `ellipsoid-n90-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `03ba60285d55ea3cf13590ed18a96e109e4d6f04b906e5e91275edc8c6c0a58f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.66 |      6.39 |           1.93 | unavailable |       10.89 |    0.22 |            5.16 |             6.16 |              7.99 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.64 |      6.38 |           0.68 | unavailable |       10.19 |    0.70 |            5.16 |             6.16 |              7.98 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.64 |      8.08 |           1.83 |       15.93 |        8.55 |    3.69 |            6.94 |             7.93 |             16.44 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.06 |      8.11 |           0.74 |       16.42 |        8.70 |    5.20 |            6.93 |             7.93 |             16.24 |
| empty-C6-3-wind0  | completed / outside configured limits |    85.79 |      8.86 |           1.77 |        1.23 |        4.90 |    0.04 |            7.57 |             8.57 |             33.76 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.38 |      8.85 |           1.08 |        5.84 |        4.90 |    7.04 |            7.56 |             8.56 |             33.61 |
| empty-C6-5-wind0  | completed / outside configured limits |    85.80 |      8.86 |           1.49 |       13.09 |        4.90 |    2.04 |            7.57 |             8.57 |             33.76 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.39 |      8.85 |           1.08 |       18.94 |        4.90 |   11.03 |            7.56 |             8.56 |             33.61 |
| empty-C5-3-wind0  | completed / outside configured limits |    69.23 |     12.91 |           0.81 |        5.00 |        4.91 |    0.01 |           11.46 |            12.46 |             25.90 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    67.56 |     12.91 |           1.03 |        5.92 |        4.91 |    9.92 |           11.45 |            12.45 |             25.75 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.91 |      5.51 |           2.36 | unavailable |        9.67 |    0.10 |            4.46 |             5.46 |              6.43 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.90 |      5.50 |           1.10 | unavailable |        9.12 |    0.48 |            4.46 |             5.46 |              6.42 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.89 |      7.18 |           2.26 | unavailable |       13.78 |    0.76 |            6.05 |             7.05 |             13.60 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.39 |      7.18 |           1.12 | unavailable |       17.14 |    6.36 |            6.05 |             7.05 |             13.41 |
| dummy-C6-3-wind0  | completed / outside configured limits |    67.83 |      7.96 |           2.08 |        2.66 |        5.21 |    0.03 |            6.63 |             7.63 |             28.57 |
| dummy-C6-3-wind2  | completed / outside configured limits |    63.99 |      7.95 |           1.46 |        7.53 |        5.21 |    4.81 |            6.63 |             7.63 |             28.44 |
| dummy-C6-5-wind0  | completed / outside configured limits |    67.83 |      7.96 |           2.08 |       15.44 |        5.21 |    0.08 |            6.63 |             7.63 |             28.57 |
| dummy-C6-5-wind2  | completed / outside configured limits |    63.99 |      7.95 |           1.46 |       22.91 |        5.21 |   26.98 |            6.63 |             7.63 |             28.44 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.07 |     12.27 |           1.75 |        8.69 |        5.22 |    0.13 |           10.09 |            11.09 |             21.41 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    52.19 |     12.26 |           1.61 |        9.84 |        5.22 |    0.76 |           10.08 |            11.08 |             21.28 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.91 |      5.51 |           2.36 | unavailable |        9.67 |    0.10 |            4.46 |             5.46 |              6.43 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.90 |      5.50 |           1.10 | unavailable |        9.12 |    0.48 |            4.46 |             5.46 |              6.42 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.89 |      7.18 |           2.26 | unavailable |       13.78 |    0.76 |            6.05 |             7.05 |             13.60 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.39 |      7.18 |           1.12 | unavailable |       17.14 |    6.36 |            6.05 |             7.05 |             13.41 |
| actual-C6-3-wind0 | completed / outside configured limits |    67.83 |      7.96 |           2.08 |        2.66 |        5.21 |    0.03 |            6.63 |             7.63 |             28.57 |
| actual-C6-3-wind2 | completed / outside configured limits |    63.99 |      7.95 |           1.46 |        7.53 |        5.21 |    4.81 |            6.63 |             7.63 |             28.44 |
| actual-C6-5-wind0 | completed / outside configured limits |    67.83 |      7.96 |           2.08 |       15.44 |        5.21 |    0.08 |            6.63 |             7.63 |             28.57 |
| actual-C6-5-wind2 | completed / outside configured limits |    63.99 |      7.95 |           1.46 |       22.91 |        5.21 |   26.98 |            6.63 |             7.63 |             28.44 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.07 |     12.27 |           1.75 |        8.69 |        5.22 |    0.13 |           10.09 |            11.09 |             21.41 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    52.19 |     12.26 |           1.61 |        9.84 |        5.22 |    0.76 |           10.08 |            11.08 |             21.28 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (24.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Large angle of attack encountered (17.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.9 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (24.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Large angle of attack encountered (17.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=162.228316492148 g (allowed None … 85.0); apogee_m=6.656228070305346 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.3874474705197075 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.885734974965569 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=162.228316492148 g (allowed None … 85.0); apogee_m=6.64185708919948 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.381572690493153 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6764467523110499 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.185363761852786 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=164.778316492148 g (allowed None … 99.0); apogee_m=23.6401993736006 m (allowed 30.0 …
  120.0); guide_departure_m_s=8.080539710943041 m/s (allowed 12.0 … None); deployment_speed_m_s=15.930627183498762 m/s
  (allowed None … 10.0); landing_descent_m_s=8.552691815697953 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=164.778316492148 g (allowed None … 99.0); apogee_m=23.061972735209523 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.105079937107446 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7412992123456096 cal (allowed 1.0 … None); deployment_speed_m_s=16.42466920851954 m/s
  (allowed None … 10.0); landing_descent_m_s=8.695776785925373 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=168.978316492148 g (allowed None … 113.0); guide_departure_m_s=8.855385003653874 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=168.978316492148 g (allowed None … 113.0); guide_departure_m_s=8.849281701326113 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=168.978316492148 g (allowed None … 113.0); guide_departure_m_s=8.855385003653874 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.09037062347808 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=168.978316492148 g (allowed None … 113.0); guide_departure_m_s=8.849281701326113 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.936623632125954 m/s (allowed None … 10.0)
- empty-C5-3-wind0: minimum_ascent_stability_cal=0.8050957826783904 cal (allowed 1.0 … None)
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=182.878316492148 g (allowed None … 85.0); apogee_m=4.9057368845617555 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.505761799196423 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.673221271229393 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=182.878316492148 g (allowed None … 85.0); apogee_m=4.89845037921775 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.5008859905335346 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.120657352083844 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=185.42831649214799 g (allowed None … 99.0); apogee_m=17.8892127179737 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.1806084475885825 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=13.778521523805942 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=185.42831649214799 g (allowed None … 99.0); apogee_m=17.39493066549944 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.175024962011415 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.14164677568869 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.956496534241872 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.951114908498572 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.956496534241872 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.444125785666692 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.951114908498572 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.910573071459385 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=182.878316492148 g (allowed None … 85.0); apogee_m=4.9057368845617555 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.505761799196423 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.673221271229393 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=182.878316492148 g (allowed None … 85.0); apogee_m=4.89845037921775 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.5008859905335346 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.120657352083844 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=185.42831649214799 g (allowed None … 99.0); apogee_m=17.8892127179737 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.1806084475885825 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=13.778521523805948 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=185.42831649214799 g (allowed None … 99.0); apogee_m=17.39493066549944 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.175024962011415 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.14164677568872 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.956496534241872 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.951114908498572 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.956496534241872 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.444125785666692 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=189.628316492148 g (allowed None … 113.0); guide_departure_m_s=7.951114908498572 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.9105730714594 m/s (allowed None … 10.0)
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
