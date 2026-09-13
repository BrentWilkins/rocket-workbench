# Rocket Workbench report

Run: `conical-n90-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `06533caf1a8b8f6fcb01f68146b9478402da3d1b302f771731fabbd1fa3375f5`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.40 |      6.73 |           1.80 | unavailable |       11.20 |    0.29 |            5.44 |             6.44 |              8.61 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.38 |      6.72 |           0.65 | unavailable |       10.56 |    0.68 |            5.43 |             6.43 |              8.58 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.97 |      8.44 |           1.67 |       15.39 |        4.80 |    3.79 |            7.28 |             8.28 |             17.53 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.30 |      8.43 |           0.69 |       16.08 |        4.81 |    4.04 |            7.28 |             8.28 |             17.32 |
| empty-C6-3-wind0  | completed / outside configured limits |    92.01 |      9.18 |           1.64 |        2.36 |        4.80 |    0.04 |            7.93 |             8.93 |             35.62 |
| empty-C6-3-wind2  | completed / outside configured limits |    88.56 |      9.17 |           1.04 |        5.95 |        4.80 |   10.43 |            7.93 |             8.93 |             35.46 |
| empty-C6-5-wind0  | completed / outside configured limits |    92.05 |      9.18 |           0.95 |       12.68 |        4.80 |    1.66 |            7.93 |             8.93 |             35.62 |
| empty-C6-5-wind2  | completed / outside configured limits |    88.60 |      9.17 |           1.04 |       17.85 |        4.80 |    6.80 |            7.93 |             8.93 |             35.46 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    74.75 |     13.22 |           1.04 |        3.82 |        4.80 |    0.02 |           11.99 |            12.99 |             27.49 |
| empty-C5-3-wind2  | completed / outside configured limits |    73.10 |     13.22 |           0.95 |        4.96 |        4.80 |   13.47 |           11.98 |            12.98 |             27.33 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.41 |      5.78 |           2.28 | unavailable |       10.06 |    0.12 |            4.68 |             5.68 |              6.91 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.40 |      5.78 |           1.13 | unavailable |        9.39 |    0.43 |            4.68 |             5.67 |              6.89 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.56 |      7.47 |           2.21 | unavailable |       15.57 |    0.50 |            6.32 |             7.32 |             14.46 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.97 |      7.46 |           1.25 | unavailable |       18.14 |    7.19 |            6.32 |             7.32 |             14.25 |
| dummy-C6-3-wind0  | completed / outside configured limits |    72.95 |      8.23 |           1.81 |        1.53 |        5.11 |    0.03 |            6.92 |             7.92 |             30.12 |
| dummy-C6-3-wind2  | completed / outside configured limits |    69.03 |      8.22 |           1.47 |        7.03 |        5.11 |    2.39 |            6.91 |             7.91 |             29.99 |
| dummy-C6-5-wind0  | completed / outside configured limits |    72.95 |      8.23 |           1.81 |       15.46 |        5.11 |    0.25 |            6.92 |             7.92 |             30.12 |
| dummy-C6-5-wind2  | completed / outside configured limits |    69.03 |      8.22 |           1.47 |       21.86 |        5.11 |   23.85 |            6.91 |             7.91 |             29.99 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    58.42 |     12.49 |           1.98 |        7.62 |        5.12 |    0.07 |           10.51 |            11.51 |             22.75 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    56.57 |     12.49 |           1.61 |        8.75 |        5.12 |    2.16 |           10.50 |            11.50 |             22.61 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.41 |      5.78 |           2.28 | unavailable |       10.06 |    0.12 |            4.68 |             5.68 |              6.91 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.40 |      5.78 |           1.13 | unavailable |        9.39 |    0.43 |            4.68 |             5.67 |              6.89 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.56 |      7.47 |           2.21 | unavailable |       15.57 |    0.50 |            6.32 |             7.32 |             14.46 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.97 |      7.46 |           1.25 | unavailable |       18.14 |    7.19 |            6.32 |             7.32 |             14.25 |
| actual-C6-3-wind0 | completed / outside configured limits |    72.95 |      8.23 |           1.81 |        1.53 |        5.11 |    0.03 |            6.92 |             7.92 |             30.12 |
| actual-C6-3-wind2 | completed / outside configured limits |    69.03 |      8.22 |           1.47 |        7.03 |        5.11 |    2.39 |            6.91 |             7.91 |             29.99 |
| actual-C6-5-wind0 | completed / outside configured limits |    72.95 |      8.23 |           1.81 |       15.46 |        5.11 |    0.25 |            6.92 |             7.92 |             30.12 |
| actual-C6-5-wind2 | completed / outside configured limits |    69.03 |      8.22 |           1.47 |       21.86 |        5.11 |   23.85 |            6.91 |             7.91 |             29.99 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    58.42 |     12.49 |           1.98 |        7.62 |        5.12 |    0.07 |           10.51 |            11.51 |             22.75 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    56.57 |     12.49 |           1.61 |        8.75 |        5.12 |    2.16 |           10.50 |            11.50 |             22.61 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (19.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (21.9 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (19.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (21.9 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=155.36749838731117 g (allowed None … 85.0); apogee_m=7.4024110723255845 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.725820707841142 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.20086983089045 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=155.36749838731117 g (allowed None … 85.0); apogee_m=7.379333698788802 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.7192650424485745 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6537170772881369 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.564651581453985 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=157.91749838731118 g (allowed None … 99.0); apogee_m=25.9744138844202 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.43652432444126 m/s (allowed 12.0 … None); deployment_speed_m_s=15.393925463970616 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=157.91749838731118 g (allowed None … 99.0); apogee_m=25.29874784071331 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.429591364831797 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6925395134055644 cal (allowed 1.0 … None); deployment_speed_m_s=16.077785577005823 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=162.11749838731117 g (allowed None … 113.0); guide_departure_m_s=9.177194919335193 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=162.11749838731117 g (allowed None … 113.0); guide_departure_m_s=9.170623091631231 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=162.11749838731117 g (allowed None … 113.0); guide_departure_m_s=9.177194919335193 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.9455717807633072 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.678352618948344 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=162.11749838731117 g (allowed None … 113.0); guide_departure_m_s=9.170623091631231 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.848100182688782 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: minimum_ascent_stability_cal=0.9455109346696201 cal (allowed 1.0 … None)
- dummy-A8-3-wind0: launch_mass_g=176.01749838731118 g (allowed None … 85.0); apogee_m=5.413153539188998 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.781170693346842 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.063180047427192 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=176.01749838731118 g (allowed None … 85.0); apogee_m=5.402899482915511 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.775805310594923 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.385608418806418 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=178.56749838731116 g (allowed None … 99.0); apogee_m=19.558220902798276 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4706464327674835 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.569207399486945 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=178.56749838731116 g (allowed None … 99.0); apogee_m=18.97346657883099 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.464546845283779 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.139592077873722 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.22711786847155 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.221315228448345 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.22711786847155 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.463637505386025 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.221315228448345 m/s
  (allowed 12.0 … None); deployment_speed_m_s=21.8601413614656 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=176.01749838731118 g (allowed None … 85.0); apogee_m=5.413153539188998 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.781170693346842 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.063180047427192 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=176.01749838731118 g (allowed None … 85.0); apogee_m=5.402899482915511 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.775805310594923 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.385608418806418 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=178.56749838731116 g (allowed None … 99.0); apogee_m=19.558220902798276 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.4706464327674835 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.569207399486945 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=178.56749838731116 g (allowed None … 99.0); apogee_m=18.97346657883099 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.464546845283779 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.139592077873633 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.22711786847155 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.221315228448345
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.22711786847155 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.46363750538603 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=182.76749838731118 g (allowed None … 113.0); guide_departure_m_s=8.221315228448345
  m/s (allowed 12.0 … None); deployment_speed_m_s=21.860141361466244 m/s (allowed None … 10.0)
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
