# Rocket Workbench report

Run: `ellipsoid-n90-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `70061ae5dee9faa4867a9c36f9e4c055e0b4717fa54fc6ff8261da76b0906738`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.37 |      6.26 |           2.25 | unavailable |       10.48 |    0.25 |            5.06 |             6.06 |              7.76 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.35 |      6.26 |           1.02 | unavailable |        9.76 |    0.40 |            5.06 |             6.05 |              7.74 |
| empty-B4-4-wind0  | completed / outside configured limits |    22.67 |      7.97 |           2.00 |       12.63 |        7.94 |    1.40 |            6.80 |             7.80 |             16.00 |
| empty-B4-4-wind2  | completed / outside configured limits |    21.92 |      7.96 |           1.14 | unavailable |       19.37 |    9.22 |            6.80 |             7.80 |             15.76 |
| empty-C6-3-wind0  | completed / outside configured limits |    82.18 |      8.72 |           2.15 |        0.38 |        4.95 |    0.04 |            7.43 |             8.43 |             32.85 |
| empty-C6-3-wind2  | completed / outside configured limits |    78.12 |      8.71 |           1.47 |        6.53 |        4.95 |    2.06 |            7.42 |             8.42 |             32.70 |
| empty-C6-5-wind0  | completed / outside configured limits |    82.18 |      8.72 |           2.03 |       12.13 |        4.95 |    1.02 |            7.43 |             8.43 |             32.85 |
| empty-C6-5-wind2  | completed / outside configured limits |    78.12 |      8.71 |           1.47 |       20.10 |        4.95 |   18.14 |            7.42 |             8.42 |             32.70 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    66.34 |     12.82 |           1.73 |        5.74 |        4.95 |    0.02 |           11.25 |            12.25 |             25.10 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    64.51 |     12.81 |           1.60 |        6.91 |        4.95 |    7.17 |           11.24 |            12.24 |             24.94 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.71 |      5.40 |           2.74 | unavailable |        9.41 |    0.12 |            4.38 |             5.38 |              6.25 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.71 |      5.39 |           1.43 | unavailable |        8.85 |    0.36 |            4.38 |             5.38 |              6.24 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.21 |      7.06 |           2.68 | unavailable |       15.40 |    0.47 |            5.94 |             6.94 |             13.24 |
| dummy-B4-4-wind2  | completed / outside configured limits |    16.57 |      7.06 |           1.69 | unavailable |       17.30 |    7.20 |            5.94 |             6.94 |             13.01 |
| dummy-C6-3-wind0  | completed / outside configured limits |    65.19 |      7.84 |           2.44 |        3.36 |        5.25 |    0.02 |            6.52 |             7.52 |             27.84 |
| dummy-C6-3-wind2  | completed / outside configured limits |    60.78 |      7.84 |           1.85 |        8.52 |        5.25 |    8.92 |            6.52 |             7.52 |             27.75 |
| dummy-C6-5-wind0  | completed / outside configured limits |    65.19 |      7.84 |           2.44 |       17.99 |        5.25 |    0.94 |            6.52 |             7.52 |             27.84 |
| dummy-C6-5-wind2  | completed / outside configured limits |    60.78 |      7.84 |           1.85 |       23.76 |        5.25 |   32.75 |            6.52 |             7.52 |             27.75 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    51.99 |     12.06 |           1.49 |        9.18 |        5.26 |    0.23 |            9.93 |            10.93 |             20.78 |
| dummy-C5-3-wind2  | completed / outside configured limits |    49.98 |     12.05 |           2.07 |       10.68 |        5.26 |    2.88 |            9.92 |            10.92 |             20.65 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.71 |      5.40 |           2.74 | unavailable |        9.41 |    0.12 |            4.38 |             5.38 |              6.25 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.71 |      5.39 |           1.43 | unavailable |        8.85 |    0.36 |            4.38 |             5.38 |              6.24 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.21 |      7.06 |           2.68 | unavailable |       15.40 |    0.47 |            5.94 |             6.94 |             13.24 |
| actual-B4-4-wind2 | completed / outside configured limits |    16.57 |      7.06 |           1.69 | unavailable |       17.30 |    7.20 |            5.94 |             6.94 |             13.01 |
| actual-C6-3-wind0 | completed / outside configured limits |    65.19 |      7.84 |           2.44 |        3.36 |        5.25 |    0.02 |            6.52 |             7.52 |             27.84 |
| actual-C6-3-wind2 | completed / outside configured limits |    60.78 |      7.84 |           1.85 |        8.52 |        5.25 |    8.92 |            6.52 |             7.52 |             27.75 |
| actual-C6-5-wind0 | completed / outside configured limits |    65.19 |      7.84 |           2.44 |       17.99 |        5.25 |    0.94 |            6.52 |             7.52 |             27.84 |
| actual-C6-5-wind2 | completed / outside configured limits |    60.78 |      7.84 |           1.85 |       23.76 |        5.25 |   32.75 |            6.52 |             7.52 |             27.75 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    51.99 |     12.06 |           1.49 |        9.18 |        5.26 |    0.23 |            9.93 |            10.93 |             20.78 |
| actual-C5-3-wind2 | completed / outside configured limits |    49.98 |     12.05 |           2.07 |       10.68 |        5.26 |    2.88 |            9.92 |            10.92 |             20.65 |

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
- empty-C6-5-wind2: Recovery device deployment at high speed (20.1 m/s): "Nominal 457 mm parachute and lines"
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (20.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.8 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (20.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.8 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=164.99595818152437 g (allowed None … 85.0); apogee_m=6.373727771649321 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.262866860445194 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.476274438471558 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=164.99595818152437 g (allowed None … 85.0); apogee_m=6.3547079260887065 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.256676111079573 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.75772236020231 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=167.54595818152438 g (allowed None … 99.0); apogee_m=22.668730119891602 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.969103090918679 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.632888627758863 m/s (allowed None … 10.0); landing_descent_m_s=7.939539676017781 m/s (allowed
  None … 6.0)
- empty-B4-4-wind2: launch_mass_g=167.54595818152438 g (allowed None … 99.0); apogee_m=21.91850000231753 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.9622821216203485 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=19.36993370590842 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=171.74595818152437 g (allowed None … 113.0); guide_departure_m_s=8.719507835445578 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=171.74595818152437 g (allowed None … 113.0); guide_departure_m_s=8.713054200352284 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=171.74595818152437 g (allowed None … 113.0); guide_departure_m_s=8.719507835445578 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.130613090462678 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=171.74595818152437 g (allowed None … 113.0); guide_departure_m_s=8.713054200352284 m/s
  (allowed 12.0 … None); deployment_speed_m_s=20.09514233086945 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=185.64595818152438 g (allowed None … 85.0); apogee_m=4.713810633136712 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.396362371718809 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.413246035401595 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=185.64595818152438 g (allowed None … 85.0); apogee_m=4.707556282906599 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.3912505433929425 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.845909030079598 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=188.1959581815244 g (allowed None … 99.0); apogee_m=17.213951699797345 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.061997566925749 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.400263264633898 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=188.1959581815244 g (allowed None … 99.0); apogee_m=16.573416211016074 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.05614675123802 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.297927747007915 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.842299323970344 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.836614362587255 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.842299323970344 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.991955971337614 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.836614362587255 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.764427858288734 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.676988714821398 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=185.64595818152438 g (allowed None … 85.0); apogee_m=4.713810633136712 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.396362371718809 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.413246035401595 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=185.64595818152438 g (allowed None … 85.0); apogee_m=4.707556282906599 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.3912505433929425 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=8.845909030079598 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=188.1959581815244 g (allowed None … 99.0); apogee_m=17.213951699797345 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.061997566925749 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.400263264633901 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=188.1959581815244 g (allowed None … 99.0); apogee_m=16.573416211016074 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.05614675123802 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.29792774700792 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.842299323970344
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.836614362587255
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.842299323970344
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.991955971337617 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=192.39595818152438 g (allowed None … 113.0); guide_departure_m_s=7.836614362587255
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.76442785828882 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.676988714821313 m/s (allowed None … 10.0)

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
