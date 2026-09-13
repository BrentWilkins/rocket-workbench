# Rocket Workbench report

Run: `conical-n70-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `6348808d0d889aa4418087466f777926777ae2d15a28f805442fd9bacadeba51`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.20 |      6.64 |           2.16 | unavailable |       10.94 |    0.31 |            5.37 |             6.37 |              8.45 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.17 |      6.64 |           1.00 | unavailable |       10.12 |    0.45 |            5.37 |             6.36 |              8.42 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.26 |      8.35 |           2.02 |       12.21 |        4.44 |    1.19 |            7.20 |             8.20 |             17.22 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.49 |      8.34 |           1.09 |       19.52 |        9.71 |    9.57 |            7.20 |             8.19 |             16.99 |
| empty-C6-3-wind0  | completed / outside configured limits |    89.01 |      9.11 |           2.10 |        1.62 |        4.82 |    0.04 |            7.84 |             8.84 |             34.93 |
| empty-C6-3-wind2  | completed / outside configured limits |    85.22 |      9.11 |           1.44 |        6.09 |        4.82 |    7.35 |            7.84 |             8.84 |             34.77 |
| empty-C6-5-wind0  | completed / outside configured limits |    89.02 |      9.11 |           1.84 |       12.03 |        4.82 |    1.12 |            7.84 |             8.84 |             34.93 |
| empty-C6-5-wind2  | completed / outside configured limits |    85.23 |      9.11 |           1.44 |       18.69 |        4.82 |   11.05 |            7.84 |             8.84 |             34.77 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    72.41 |     13.07 |           1.95 |        4.44 |        4.83 |    0.01 |           11.85 |            12.85 |             26.88 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.67 |     13.06 |           1.45 |        5.57 |        4.83 |   11.71 |           11.84 |            12.84 |             26.71 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.28 |      5.71 |           2.76 | unavailable |        9.87 |    0.13 |            4.62 |             5.62 |              6.79 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.27 |      5.72 |           1.52 | unavailable |        9.29 |    0.35 |            4.62 |             5.62 |              6.77 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.08 |      7.38 |           2.59 | unavailable |       16.07 |    0.62 |            6.25 |             7.25 |             14.23 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.41 |      7.37 |           1.74 | unavailable |       18.17 |    7.63 |            6.25 |             7.25 |             13.99 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.84 |      8.17 |           2.38 |        2.11 |        5.14 |    0.03 |            6.85 |             7.85 |             29.58 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.64 |      8.17 |           1.91 |        7.51 |        5.14 |    4.63 |            6.84 |             7.84 |             29.47 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.84 |      8.17 |           2.38 |       16.78 |        5.14 |    1.05 |            6.85 |             7.85 |             29.58 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.64 |      8.17 |           1.91 |       22.40 |        5.14 |   26.89 |            6.84 |             7.84 |             29.47 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.81 |     12.36 |           2.50 |        8.06 |        5.14 |    0.11 |           10.40 |            11.40 |             22.28 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.88 |     12.35 |           2.11 |        9.32 |        5.14 |    0.81 |           10.40 |            11.40 |             22.13 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.28 |      5.71 |           2.76 | unavailable |        9.87 |    0.13 |            4.62 |             5.62 |              6.79 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.27 |      5.72 |           1.52 | unavailable |        9.29 |    0.35 |            4.62 |             5.62 |              6.77 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.08 |      7.38 |           2.59 | unavailable |       16.07 |    0.62 |            6.25 |             7.25 |             14.23 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.41 |      7.37 |           1.74 | unavailable |       18.17 |    7.63 |            6.25 |             7.25 |             13.99 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.84 |      8.17 |           2.38 |        2.11 |        5.14 |    0.03 |            6.85 |             7.85 |             29.58 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.64 |      8.17 |           1.91 |        7.51 |        5.14 |    4.63 |            6.84 |             7.84 |             29.47 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.84 |      8.17 |           2.38 |       16.78 |        5.14 |    1.05 |            6.85 |             7.85 |             29.58 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.64 |      8.17 |           1.91 |       22.40 |        5.14 |   26.89 |            6.84 |             7.84 |             29.47 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.81 |     12.36 |           2.50 |        8.06 |        5.14 |    0.11 |           10.40 |            11.40 |             22.28 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.88 |     12.35 |           2.11 |        9.32 |        5.14 |    0.81 |           10.40 |            11.40 |             22.13 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (17.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.4 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (17.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.4 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=156.99195587730773 g (allowed None … 85.0); apogee_m=7.204528587802903 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.644259255894776 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.93893016438472 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=156.99195587730773 g (allowed None … 85.0); apogee_m=7.174848737084509 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.637270376878143 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.12068393133572 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=159.54195587730774 g (allowed None … 99.0); apogee_m=25.25886764443267 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.351520617032588 m/s (allowed 12.0 … None); deployment_speed_m_s=12.214078826091985 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=159.54195587730774 g (allowed None … 99.0); apogee_m=24.491427510538486 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.344039179874336 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.523675989060127 m/s (allowed None … 10.0); landing_descent_m_s=9.707473238344786 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=163.74195587730776 g (allowed None … 113.0); guide_departure_m_s=9.112143082821671 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=163.74195587730776 g (allowed None … 113.0); guide_departure_m_s=9.105005211692854 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=163.74195587730776 g (allowed None … 113.0); guide_departure_m_s=9.112143082821671 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.034212885830774 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=163.74195587730776 g (allowed None … 113.0); guide_departure_m_s=9.105005211692854 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.690409541880598 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=177.64195587730774 g (allowed None … 85.0); apogee_m=5.281724041680323 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.7117794304085265 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.86950834541292 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=177.64195587730774 g (allowed None … 85.0); apogee_m=5.270675659761092 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.717239593615723 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.286040083982005 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=180.19195587730775 g (allowed None … 99.0); apogee_m=19.077461712934454 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.380726499420578 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.06989530460328 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=180.19195587730775 g (allowed None … 99.0); apogee_m=18.409633969574248 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.374269103125347 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.165516053963074 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.171928904607482 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.16563338139713 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.171928904607482 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.78427110112237 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.16563338139713 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.402586130154305 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=177.64195587730774 g (allowed None … 85.0); apogee_m=5.281724041680323 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.7117794304085265 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=9.86950834541292 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=177.64195587730774 g (allowed None … 85.0); apogee_m=5.270675659761092 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.717239593615723 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.286040083982005 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=180.19195587730775 g (allowed None … 99.0); apogee_m=19.077461712934454 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.380726499420578 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.069895304603275 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=180.19195587730775 g (allowed None … 99.0); apogee_m=18.409633969574248 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.374269103125347 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.16551605396306 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.171928904607482
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.16563338139713 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.171928904607482
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.784271101122357 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=184.39195587730774 g (allowed None … 113.0); guide_departure_m_s=8.16563338139713 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.402586130154187 m/s (allowed None … 10.0)
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
