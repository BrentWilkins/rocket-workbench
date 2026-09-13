# Rocket Workbench report

Run: `conical-n90-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `5887c89647698ccb1dbae2643a9e2322f5d69b95b295e256f066adeac52d581d`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.22 |      6.65 |           2.04 | unavailable |       11.15 |    0.27 |            5.37 |             6.37 |              8.46 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.21 |      6.65 |           0.80 | unavailable |       10.32 |    0.66 |            5.37 |             6.37 |              8.44 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.40 |      8.36 |           1.55 |       14.25 |        4.52 |    3.46 |            7.20 |             8.20 |             17.27 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.75 |      8.35 |           0.85 |       14.31 |        4.38 |    5.50 |            7.20 |             8.20 |             17.06 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.22 |      9.12 |           1.91 |        1.98 |        4.82 |    0.04 |            7.85 |             8.85 |             35.14 |
| empty-C6-3-wind2  | completed / outside configured limits |    86.80 |      9.12 |           1.22 |        5.83 |        4.82 |    9.64 |            7.85 |             8.84 |             34.98 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.24 |      9.12 |           1.38 |       12.39 |        4.82 |    1.65 |            7.85 |             8.85 |             35.14 |
| empty-C6-5-wind2  | completed / outside configured limits |    86.82 |      9.12 |           1.22 |       18.13 |        4.82 |    7.73 |            7.85 |             8.84 |             34.98 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.24 |     13.08 |           1.62 |        4.17 |        4.83 |    0.02 |           11.87 |            12.87 |             27.08 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    71.58 |     13.08 |           1.11 |        5.18 |        4.83 |   12.64 |           11.86 |            12.86 |             26.91 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.29 |      5.72 |           2.58 | unavailable |        9.93 |    0.11 |            4.63 |             5.63 |              6.80 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.29 |      5.71 |           1.30 | unavailable |        9.32 |    0.45 |            4.63 |             5.63 |              6.79 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.16 |      7.39 |           2.52 | unavailable |       15.73 |    0.57 |            6.26 |             7.26 |             14.26 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.60 |      7.38 |           1.39 | unavailable |       17.95 |    6.85 |            6.26 |             7.26 |             14.06 |
| dummy-C6-3-wind0  | completed / outside configured limits |    71.56 |      8.18 |           1.52 |        1.86 |        5.14 |    0.03 |            6.85 |             7.85 |             29.73 |
| dummy-C6-3-wind2  | completed / outside configured limits |    67.70 |      8.17 |           1.67 |        7.08 |        5.14 |    2.79 |            6.85 |             7.85 |             29.60 |
| dummy-C6-5-wind0  | completed / outside configured limits |    71.56 |      8.18 |           1.52 |       16.02 |        5.14 |    0.50 |            6.85 |             7.85 |             29.73 |
| dummy-C6-5-wind2  | completed / outside configured limits |    67.70 |      8.17 |           1.67 |       22.09 |        5.14 |   24.28 |            6.85 |             7.85 |             29.60 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.29 |     12.37 |           2.20 |        7.91 |        5.14 |    0.08 |           10.41 |            11.41 |             22.41 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    55.44 |     12.36 |           1.79 |        8.98 |        5.14 |    1.55 |           10.41 |            11.41 |             22.27 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.29 |      5.72 |           2.58 | unavailable |        9.93 |    0.11 |            4.63 |             5.63 |              6.80 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.29 |      5.71 |           1.30 | unavailable |        9.32 |    0.45 |            4.63 |             5.63 |              6.79 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.16 |      7.39 |           2.52 | unavailable |       15.73 |    0.57 |            6.26 |             7.26 |             14.26 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.60 |      7.38 |           1.39 | unavailable |       17.95 |    6.85 |            6.26 |             7.26 |             14.06 |
| actual-C6-3-wind0 | completed / outside configured limits |    71.56 |      8.18 |           1.52 |        1.86 |        5.14 |    0.03 |            6.85 |             7.85 |             29.73 |
| actual-C6-3-wind2 | completed / outside configured limits |    67.70 |      8.17 |           1.67 |        7.08 |        5.14 |    2.79 |            6.85 |             7.85 |             29.60 |
| actual-C6-5-wind0 | completed / outside configured limits |    71.56 |      8.18 |           1.52 |       16.02 |        5.14 |    0.50 |            6.85 |             7.85 |             29.73 |
| actual-C6-5-wind2 | completed / outside configured limits |    67.70 |      8.17 |           1.67 |       22.09 |        5.14 |   24.28 |            6.85 |             7.85 |             29.60 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.29 |     12.37 |           2.20 |        7.91 |        5.14 |    0.08 |           10.41 |            11.41 |             22.41 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    55.44 |     12.36 |           1.79 |        8.98 |        5.14 |    1.55 |           10.41 |            11.41 |             22.27 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (20.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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
- actual-A8-3-wind2: Large angle of attack encountered (20.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=156.86749838731112 g (allowed None … 85.0); apogee_m=7.2234243746638205 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.65012037441834 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.14531385575483 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=156.86749838731112 g (allowed None … 85.0); apogee_m=7.205913732819476 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.64620097661803 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8026199607393515 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.321618099684265 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=159.41749838731113 g (allowed None … 99.0); apogee_m=25.404041645240756 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.361013670462821 m/s (allowed 12.0 … None); deployment_speed_m_s=14.25313823487154
  m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=159.41749838731113 g (allowed None … 99.0); apogee_m=24.750212152305036 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.353996793500578 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8486888193444078 cal (allowed 1.0 … None); deployment_speed_m_s=14.30967973822273 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=163.61749838731112 g (allowed None … 113.0); guide_departure_m_s=9.122133948187523 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=163.61749838731112 g (allowed None … 113.0); guide_departure_m_s=9.115441309377376 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=163.61749838731112 g (allowed None … 113.0); guide_departure_m_s=9.122133948187523 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.386151517397984 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=163.61749838731112 g (allowed None … 113.0); guide_departure_m_s=9.115441309377376 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.1332041970057 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=177.51749838731112 g (allowed None … 85.0); apogee_m=5.293671578863028 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.717450825169935 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.929899349647485 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=177.51749838731112 g (allowed None … 85.0); apogee_m=5.285496830489617 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.713340584139708 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.32210631782996 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=180.06749838731113 g (allowed None … 99.0); apogee_m=19.159047442015822 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.388427353587301 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.726896487307243 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=180.06749838731113 g (allowed None … 99.0); apogee_m=18.600664444273427 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.382397767045071 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.948363631943543 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.180148956449028 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.174244881392683 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.180148956449028 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.020960963116803 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.174244881392683 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.087975599217806 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=177.51749838731112 g (allowed None … 85.0); apogee_m=5.293671578863028 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.717450825169935 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.929899349647485 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=177.51749838731112 g (allowed None … 85.0); apogee_m=5.285496830489617 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.713340584139708 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.322106317829958 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=180.06749838731113 g (allowed None … 99.0); apogee_m=19.159047442015822 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.388427353587301 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.726896487307247 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=180.06749838731113 g (allowed None … 99.0); apogee_m=18.600664444273427 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.382397767045071 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.948363631943554 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.180148956449028
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.174244881392683
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.180148956449028
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.0209609631168 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=184.26749838731112 g (allowed None … 113.0); guide_departure_m_s=8.174244881392683
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.0879755992178 m/s (allowed None … 10.0)
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
