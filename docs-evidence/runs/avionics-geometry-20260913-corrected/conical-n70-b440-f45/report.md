# Rocket Workbench report

Run: `conical-n70-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `06d20dd77cd758499c50f6a781632055683aaf97dc2f0063d4e67872d38c1f7d`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.37 |      6.71 |           2.04 | unavailable |       11.16 |    0.28 |            5.43 |             6.42 |              8.58 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.34 |      6.70 |           0.85 | unavailable |       10.39 |    0.63 |            5.42 |             6.42 |              8.56 |
| empty-B4-4-wind0  | completed / outside configured limits |    25.81 |      8.42 |           1.96 |       13.59 |        4.78 |    3.03 |            7.27 |             8.27 |             17.47 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.12 |      8.41 |           0.88 |       12.02 |        4.81 |    7.87 |            7.27 |             8.27 |             17.25 |
| empty-C6-3-wind0  | completed / outside configured limits |    90.95 |      9.16 |           1.89 |        2.06 |        4.80 |    0.04 |            7.92 |             8.92 |             35.42 |
| empty-C6-3-wind2  | completed / outside configured limits |    87.48 |      9.15 |           1.23 |        5.85 |        4.80 |    9.91 |            7.91 |             8.91 |             35.26 |
| empty-C6-5-wind0  | completed / outside configured limits |    90.98 |      9.16 |           1.03 |       12.24 |        4.80 |    1.50 |            7.92 |             8.92 |             35.42 |
| empty-C6-5-wind2  | completed / outside configured limits |    87.50 |      9.15 |           1.23 |       18.09 |        4.80 |    7.45 |            7.91 |             8.91 |             35.26 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    73.99 |     13.20 |           1.73 |        4.05 |        4.81 |    0.02 |           11.97 |            12.96 |             27.31 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    72.32 |     13.19 |           1.14 |        5.10 |        4.81 |   13.15 |           11.96 |            12.96 |             27.14 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.39 |      5.78 |           2.56 | unavailable |       10.01 |    0.12 |            4.67 |             5.67 |              6.89 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.38 |      5.77 |           1.34 | unavailable |        9.38 |    0.42 |            4.67 |             5.67 |              6.87 |
| dummy-B4-4-wind0  | completed / outside configured limits |    19.46 |      7.46 |           2.32 | unavailable |       16.05 |    0.57 |            6.31 |             7.31 |             14.42 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.87 |      7.45 |           1.46 | unavailable |       18.18 |    7.03 |            6.31 |             7.31 |             14.21 |
| dummy-C6-3-wind0  | completed / outside configured limits |    72.28 |      8.21 |           1.95 |        1.74 |        5.12 |    0.03 |            6.91 |             7.91 |             29.97 |
| dummy-C6-3-wind2  | completed / outside configured limits |    68.37 |      8.25 |           1.70 |        7.04 |        5.12 |    2.50 |            6.90 |             7.90 |             29.84 |
| dummy-C6-5-wind0  | completed / outside configured limits |    72.28 |      8.21 |           1.95 |       16.17 |        5.12 |    0.67 |            6.91 |             7.91 |             29.97 |
| dummy-C6-5-wind2  | completed / outside configured limits |    68.37 |      8.25 |           1.70 |       21.96 |        5.12 |   23.92 |            6.90 |             7.90 |             29.84 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    57.96 |     12.47 |           1.71 |        7.77 |        5.12 |    0.08 |           10.49 |            11.49 |             22.62 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    56.10 |     12.46 |           1.84 |        8.87 |        5.12 |    2.00 |           10.48 |            11.48 |             22.48 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.39 |      5.78 |           2.56 | unavailable |       10.01 |    0.12 |            4.67 |             5.67 |              6.89 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.38 |      5.77 |           1.34 | unavailable |        9.38 |    0.42 |            4.67 |             5.67 |              6.87 |
| actual-B4-4-wind0 | completed / outside configured limits |    19.46 |      7.46 |           2.32 | unavailable |       16.05 |    0.57 |            6.31 |             7.31 |             14.42 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.87 |      7.45 |           1.46 | unavailable |       18.18 |    7.03 |            6.31 |             7.31 |             14.21 |
| actual-C6-3-wind0 | completed / outside configured limits |    72.28 |      8.21 |           1.95 |        1.74 |        5.12 |    0.03 |            6.91 |             7.91 |             29.97 |
| actual-C6-3-wind2 | completed / outside configured limits |    68.37 |      8.25 |           1.70 |        7.04 |        5.12 |    2.50 |            6.90 |             7.90 |             29.84 |
| actual-C6-5-wind0 | completed / outside configured limits |    72.28 |      8.21 |           1.95 |       16.17 |        5.12 |    0.67 |            6.91 |             7.91 |             29.97 |
| actual-C6-5-wind2 | completed / outside configured limits |    68.37 |      8.25 |           1.70 |       21.96 |        5.12 |   23.92 |            6.90 |             7.90 |             29.84 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    57.96 |     12.47 |           1.71 |        7.77 |        5.12 |    0.08 |           10.49 |            11.49 |             22.62 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    56.10 |     12.46 |           1.84 |        8.87 |        5.12 |    2.00 |           10.48 |            11.48 |             22.48 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (19.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (22 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=155.60813693672594 g (allowed None … 85.0); apogee_m=7.36755504331416 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.710397237542181 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.155605862190946 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=155.60813693672594 g (allowed None … 85.0); apogee_m=7.342742876985022 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.70354411876075 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8459606223307108 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.385829565768834 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=158.15813693672595 g (allowed None … 99.0); apogee_m=25.809428293621696 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.419335364259407 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.594609070538668 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=158.15813693672595 g (allowed None … 99.0); apogee_m=25.120110904142358 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.412160492369813 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8811607889438328 cal (allowed 1.0 … None); deployment_speed_m_s=12.024757150663074 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=162.35813693672597 g (allowed None … 113.0); guide_departure_m_s=9.159197482187166 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=162.35813693672597 g (allowed None … 113.0); guide_departure_m_s=9.152315511633034 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=162.35813693672597 g (allowed None … 113.0); guide_departure_m_s=9.159197482187166 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.236826459005274 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=162.35813693672597 g (allowed None … 113.0); guide_departure_m_s=9.152315511633034 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.085759207869746 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=176.25813693672595 g (allowed None … 85.0); apogee_m=5.391111061403019 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.780294237717576 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.006137623802775 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=176.25813693672595 g (allowed None … 85.0); apogee_m=5.379920170456994 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.774597720097029 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.380342246004302 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=178.80813693672596 g (allowed None … 99.0); apogee_m=19.45771438289639 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.456661076592219 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.046644825040296 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=178.80813693672596 g (allowed None … 99.0); apogee_m=18.869231043866527 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.450276672920578 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.177547227854568 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.212303570935306 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.246835341206971 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.212303570935306 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.17232631450479 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.246835341206971 m/s
  (allowed 12.0 … None); deployment_speed_m_s=21.963546903851313 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=176.25813693672595 g (allowed None … 85.0); apogee_m=5.391111061403019 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.780294237717576 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.006137623802775 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=176.25813693672595 g (allowed None … 85.0); apogee_m=5.379920170456994 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.774597720097029 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.380342246004302 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=178.80813693672596 g (allowed None … 99.0); apogee_m=19.45771438289639 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.456661076592219 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.046644825040296 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=178.80813693672596 g (allowed None … 99.0); apogee_m=18.869231043866534 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.450276672920578 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.17754722785456 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.212303570935306
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.246835341206971
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.212303570935306
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.17232631450479 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=183.00813693672598 g (allowed None … 113.0); guide_departure_m_s=8.246835341206971
  m/s (allowed 12.0 … None); deployment_speed_m_s=21.96354690385125 m/s (allowed None … 10.0)
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
