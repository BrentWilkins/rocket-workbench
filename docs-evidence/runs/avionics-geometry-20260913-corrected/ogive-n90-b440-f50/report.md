# Rocket Workbench report

Run: `ogive-n90-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `14dd8fbe716a1c875270627c66a7821d82892da317d7cf3ff016bf9b98d1058f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.61 |      6.38 |           2.34 | unavailable |       10.72 |    0.24 |            5.15 |             6.15 |              7.96 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.60 |      6.38 |           1.00 | unavailable |        9.90 |    0.52 |            5.15 |             6.14 |              7.94 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.46 |      8.09 |           2.29 |       12.69 |        5.93 |    2.11 |            6.92 |             7.92 |             16.37 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.77 |      8.08 |           1.11 | unavailable |       19.39 |    9.02 |            6.92 |             7.92 |             16.14 |
| empty-C6-3-wind0  | completed / outside configured limits |    84.75 |      8.83 |           2.22 |        0.94 |        4.91 |    0.04 |            7.55 |             8.55 |             33.55 |
| empty-C6-3-wind2  | completed / outside configured limits |    81.00 |      8.82 |           1.47 |        6.16 |        4.91 |    4.86 |            7.54 |             8.54 |             33.40 |
| empty-C6-5-wind0  | completed / outside configured limits |    84.75 |      8.83 |           1.93 |       12.06 |        4.91 |    1.37 |            7.55 |             8.55 |             33.55 |
| empty-C6-5-wind2  | completed / outside configured limits |    81.00 |      8.82 |           1.47 |       19.41 |        4.91 |   14.21 |            7.54 |             8.54 |             33.40 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    68.47 |     12.88 |           1.99 |        5.23 |        4.92 |    0.00 |           11.43 |            12.43 |             25.71 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    66.72 |     12.87 |           1.47 |        6.25 |        4.92 |    8.99 |           11.42 |            12.42 |             25.55 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.88 |      5.49 |           2.85 | unavailable |        9.57 |    0.11 |            4.45 |             5.45 |              6.41 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.87 |      5.48 |           1.48 | unavailable |        8.96 |    0.41 |            4.45 |             5.45 |              6.39 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.77 |      7.16 |           2.81 | unavailable |       15.46 |    0.53 |            6.03 |             7.03 |             13.54 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.20 |      7.15 |           1.61 | unavailable |       17.43 |    6.79 |            6.03 |             7.03 |             13.33 |
| dummy-C6-3-wind0  | completed / outside configured limits |    67.16 |      7.94 |           2.53 |        2.87 |        5.22 |    0.02 |            6.61 |             7.61 |             28.41 |
| dummy-C6-3-wind2  | completed / outside configured limits |    63.03 |      7.93 |           1.89 |        7.93 |        5.22 |    6.52 |            6.61 |             7.61 |             28.30 |
| dummy-C6-5-wind0  | completed / outside configured limits |    67.16 |      7.94 |           2.53 |       17.17 |        5.22 |    0.94 |            6.61 |             7.61 |             28.41 |
| dummy-C6-5-wind2  | completed / outside configured limits |    63.03 |      7.93 |           1.89 |       23.19 |        5.22 |   29.40 |            6.61 |             7.61 |             28.30 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    53.59 |     12.24 |           2.48 |        8.82 |        5.23 |    0.16 |           10.07 |            11.07 |             21.27 |
| dummy-C5-3-wind2  | completed / outside configured limits |    51.66 |     12.23 |           2.13 |       10.06 |        5.23 |    1.31 |           10.06 |            11.06 |             21.14 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.88 |      5.49 |           2.85 | unavailable |        9.57 |    0.11 |            4.45 |             5.45 |              6.41 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.87 |      5.48 |           1.48 | unavailable |        8.96 |    0.41 |            4.45 |             5.45 |              6.39 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.77 |      7.16 |           2.81 | unavailable |       15.46 |    0.53 |            6.03 |             7.03 |             13.54 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.20 |      7.15 |           1.61 | unavailable |       17.43 |    6.79 |            6.03 |             7.03 |             13.33 |
| actual-C6-3-wind0 | completed / outside configured limits |    67.16 |      7.94 |           2.53 |        2.87 |        5.22 |    0.02 |            6.61 |             7.61 |             28.41 |
| actual-C6-3-wind2 | completed / outside configured limits |    63.03 |      7.93 |           1.89 |        7.93 |        5.22 |    6.52 |            6.61 |             7.61 |             28.30 |
| actual-C6-5-wind0 | completed / outside configured limits |    67.16 |      7.94 |           2.53 |       17.17 |        5.22 |    0.94 |            6.61 |             7.61 |             28.41 |
| actual-C6-5-wind2 | completed / outside configured limits |    63.03 |      7.93 |           1.89 |       23.19 |        5.22 |   29.40 |            6.61 |             7.61 |             28.30 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    53.59 |     12.24 |           2.48 |        8.82 |        5.23 |    0.16 |           10.07 |            11.07 |             21.27 |
| actual-C5-3-wind2 | completed / outside configured limits |    51.66 |     12.23 |           2.13 |       10.06 |        5.23 |    1.31 |           10.06 |            11.06 |             21.14 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (21.5°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.2 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (21.5°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.2 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=162.59899433219675 g (allowed None … 85.0); apogee_m=6.6134067544946396 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.381644461834454 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.716838880505053 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=162.59899433219675 g (allowed None … 85.0); apogee_m=6.5958360082389556 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.375408862515818 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9989770550100842 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.896253316851089 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=165.14899433219674 g (allowed None … 99.0); apogee_m=23.459225469429125 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.087385641920074 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.692021632953479 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=165.14899433219674 g (allowed None … 99.0); apogee_m=22.77386734450193 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.080658553226952 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.3913819498045 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=169.34899433219675 g (allowed None … 113.0); guide_departure_m_s=8.829922510074926 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=169.34899433219675 g (allowed None … 113.0); guide_departure_m_s=8.823541511057826 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=169.34899433219675 g (allowed None … 113.0); guide_departure_m_s=8.829922510074926 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.064458533692004 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=169.34899433219675 g (allowed None … 113.0); guide_departure_m_s=8.823541511057826 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.409201034670343 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=183.24899433219673 g (allowed None … 85.0); apogee_m=4.877447531725316 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.487949153102757 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.574681399618848 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=183.24899433219673 g (allowed None … 85.0); apogee_m=4.870476165008015 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.4828612948974245 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.96267945703122 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=185.79899433219674 g (allowed None … 99.0); apogee_m=17.773026153351715 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.160790624623979 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.455942503730414 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=185.79899433219674 g (allowed None … 99.0); apogee_m=17.196226092393623 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.154953463436471 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.431271663601965 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.935362237088784 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.929734405247469 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.935362237088784 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.16727320278387 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.929734405247469 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.194133907581364 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.064584933559447 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=183.24899433219673 g (allowed None … 85.0); apogee_m=4.877447531725316 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.487949153102757 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.57468139961885 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=183.24899433219673 g (allowed None … 85.0); apogee_m=4.870476165008015 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.4828612948974245 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=8.96267945703122 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=185.79899433219674 g (allowed None … 99.0); apogee_m=17.773026153351715 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.160790624623979 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.455942503730412 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=185.79899433219674 g (allowed None … 99.0); apogee_m=17.196226092393623 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.154953463436471 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.4312716636022 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.935362237088784
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.929734405247469
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.935362237088784
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.16727320278387 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=189.99899433219676 g (allowed None … 113.0); guide_departure_m_s=7.929734405247469
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.19413390758148 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.064584933559448 m/s (allowed None … 10.0)

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
