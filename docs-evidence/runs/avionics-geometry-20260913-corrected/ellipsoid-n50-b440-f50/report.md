# Rocket Workbench report

Run: `ellipsoid-n50-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `109bf0f08b233e664b19951814779e5b600bc3c4e4d43fddd47ea256932aaa9d`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.88 |      6.49 |           2.33 | unavailable |       10.81 |    0.27 |            5.25 |             6.24 |              8.18 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.85 |      6.49 |           1.09 | unavailable |       10.02 |    0.42 |            5.24 |             6.24 |              8.16 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.31 |      8.22 |           2.20 |       14.42 |        5.35 |    0.02 |            7.04 |             8.04 |             16.76 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.56 |      8.21 |           1.18 | unavailable |       19.99 |    9.31 |            7.04 |             8.04 |             16.53 |
| empty-C6-3-wind0  | completed / outside configured limits |    87.32 |      8.95 |           2.17 |        1.46 |        4.87 |    0.04 |            7.68 |             8.68 |             34.27 |
| empty-C6-3-wind2  | completed / outside configured limits |    83.42 |      8.94 |           1.51 |        6.32 |        4.87 |    5.57 |            7.68 |             8.67 |             34.12 |
| empty-C6-5-wind0  | completed / outside configured limits |    87.33 |      8.95 |           1.11 |       12.33 |        4.87 |    0.88 |            7.68 |             8.68 |             34.27 |
| empty-C6-5-wind2  | completed / outside configured limits |    83.43 |      8.94 |           1.51 |       19.06 |        4.87 |   13.47 |            7.68 |             8.67 |             34.12 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    70.66 |     13.00 |           2.06 |        4.72 |        4.88 |    0.01 |           11.62 |            12.62 |             26.33 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.89 |     13.00 |           1.58 |        5.95 |        4.88 |   10.09 |           11.61 |            12.61 |             26.17 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.06 |      5.60 |           2.79 | unavailable |        9.74 |    0.12 |            4.53 |             5.53 |              6.58 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.05 |      5.59 |           1.58 | unavailable |        9.12 |    0.35 |            4.53 |             5.53 |              6.56 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.38 |      7.27 |           2.78 | unavailable |       15.81 |    0.62 |            6.13 |             7.13 |             13.85 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.74 |      7.26 |           1.79 | unavailable |       17.84 |    7.26 |            6.13 |             7.13 |             13.63 |
| dummy-C6-3-wind0  | completed / outside configured limits |    69.18 |      8.04 |           2.50 |        2.39 |        5.18 |    0.03 |            6.72 |             7.72 |             29.00 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.91 |      8.03 |           1.95 |        7.83 |        5.18 |    6.11 |            6.72 |             7.71 |             28.90 |
| dummy-C6-5-wind0  | completed / outside configured limits |    69.18 |      8.04 |           2.50 |       17.10 |        5.18 |    1.28 |            6.72 |             7.72 |             29.00 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.91 |      8.03 |           1.95 |       22.86 |        5.18 |   28.99 |            6.72 |             7.71 |             28.90 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.26 |     12.28 |           2.24 |        8.39 |        5.19 |    0.13 |           10.22 |            11.22 |             21.79 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.31 |     12.27 |           2.16 |        9.74 |        5.19 |    0.50 |           10.21 |            11.21 |             21.65 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.06 |      5.60 |           2.79 | unavailable |        9.74 |    0.12 |            4.53 |             5.53 |              6.58 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.05 |      5.59 |           1.58 | unavailable |        9.12 |    0.35 |            4.53 |             5.53 |              6.56 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.38 |      7.27 |           2.78 | unavailable |       15.81 |    0.62 |            6.13 |             7.13 |             13.85 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.74 |      7.26 |           1.79 | unavailable |       17.84 |    7.26 |            6.13 |             7.13 |             13.63 |
| actual-C6-3-wind0 | completed / outside configured limits |    69.18 |      8.04 |           2.50 |        2.39 |        5.18 |    0.03 |            6.72 |             7.72 |             29.00 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.91 |      8.03 |           1.95 |        7.83 |        5.18 |    6.11 |            6.72 |             7.71 |             28.90 |
| actual-C6-5-wind0 | completed / outside configured limits |    69.18 |      8.04 |           2.50 |       17.10 |        5.18 |    1.28 |            6.72 |             7.72 |             29.00 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.91 |      8.03 |           1.95 |       22.86 |        5.18 |   28.99 |            6.72 |             7.71 |             28.90 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.26 |     12.28 |           2.24 |        8.39 |        5.19 |    0.13 |           10.22 |            11.22 |             21.79 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.31 |     12.27 |           2.16 |        9.74 |        5.19 |    0.50 |           10.21 |            11.21 |             21.65 |

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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.9 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=160.07604645749495 g (allowed None … 85.0); apogee_m=6.8763552077846875 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.49375329248393 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.809431769293939 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=160.07604645749495 g (allowed None … 85.0); apogee_m=6.853659979716499 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.487563461687445 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.01761841419904 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=162.62604645749497 g (allowed None … 99.0); apogee_m=24.31051536711991 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.216519891443765 m/s (allowed 12.0 … None); deployment_speed_m_s=14.419695189041356 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=162.62604645749497 g (allowed None … 99.0); apogee_m=23.559730577262147 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.209680277326653 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=19.987441763385103 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=166.82604645749495 g (allowed None … 113.0); guide_departure_m_s=8.950908263862535 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=166.82604645749495 g (allowed None … 113.0); guide_departure_m_s=8.944489720578982 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=166.82604645749495 g (allowed None … 113.0); guide_departure_m_s=8.950908263862535 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.331476059141306 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=166.82604645749495 g (allowed None … 113.0); guide_departure_m_s=8.944489720578982 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.058667886018803 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=180.72604645749496 g (allowed None … 85.0); apogee_m=5.056884820716603 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.59663721986512 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.742415965490173 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=180.72604645749496 g (allowed None … 85.0); apogee_m=5.048774096511326 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.591421887189912 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.117676672338968 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=183.27604645749494 g (allowed None … 99.0); apogee_m=18.376396966454855 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.267946704121982 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.808281090994805 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=183.27604645749494 g (allowed None … 99.0); apogee_m=17.737520527700834 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.262045589813809 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.841142964288647 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.03714085307185 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.031478032840267 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.03714085307185 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.103152716336357 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.031478032840267 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.86443808457844 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=180.72604645749496 g (allowed None … 85.0); apogee_m=5.056884820716603 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.59663721986512 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.742415965490173 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=180.72604645749496 g (allowed None … 85.0); apogee_m=5.048774096511326 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.591421887189912 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.117676672338968 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=183.27604645749494 g (allowed None … 99.0); apogee_m=18.376396966454855 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.267946704121982 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.808281090994807 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=183.27604645749494 g (allowed None … 99.0); apogee_m=17.737520527700838 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.262045589813809 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.84114296428866 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.03714085307185 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.031478032840267
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.03714085307185 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.103152716336364 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=187.47604645749496 g (allowed None … 113.0); guide_departure_m_s=8.031478032840267
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.864438084578307 m/s (allowed None … 10.0)
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
