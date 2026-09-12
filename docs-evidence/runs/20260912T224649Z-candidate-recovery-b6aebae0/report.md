# Rocket Workbench report

Run: `20260912T224649Z-candidate-recovery-b6aebae0`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `ffc49cba86df36e14ad63fe0a0ef534a1c5d25b3865b1a6a8f1167534269bb4f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    10.94 |      8.06 |           1.73 | unavailable |       11.17 |    0.84 |
| empty-A8-3-wind2  | completed / outside configured limits |    10.80 |      8.05 |           0.82 | unavailable |       11.33 |    0.55 |
| empty-B4-4-wind0  | completed / outside configured limits |    36.40 |      9.88 |           1.70 |       11.49 |        4.42 |    1.37 |
| empty-B4-4-wind2  | completed / outside configured limits |    35.49 |      9.87 |           0.97 |       15.56 |        4.42 |    2.27 |
| empty-C6-3-wind0  | completed / outside configured limits |   115.60 |     10.55 |           1.63 |        6.13 |        4.41 |    0.04 |
| empty-C6-3-wind2  | completed / outside configured limits |   112.00 |     10.54 |           1.20 |        7.65 |        4.41 |   23.98 |
| empty-C6-5-wind0  | completed / outside configured limits |   116.53 |     10.55 |           1.24 |       10.93 |        4.41 |    0.83 |
| empty-C6-5-wind2  | completed / outside configured limits |   112.85 |     10.54 |           1.20 |       14.39 |        4.41 |    9.54 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    97.08 |     14.13 |           1.64 |        0.30 |        4.41 |    0.04 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    95.55 |     14.12 |           1.14 |        2.78 |        4.41 |   28.27 |
| dummy-A8-3-wind0  | completed / outside configured limits |     8.08 |      7.00 |           2.17 | unavailable |       10.85 |    0.42 |
| dummy-A8-3-wind2  | completed / outside configured limits |     8.01 |      6.99 |           1.33 | unavailable |       10.58 |    0.11 |
| dummy-B4-4-wind0  | completed / outside configured limits |    27.98 |      8.74 |           2.16 |       16.72 |        4.72 |    1.14 |
| dummy-B4-4-wind2  | completed / outside configured limits |    27.05 |      8.73 |           1.62 |       20.11 |        4.94 |   10.01 |
| dummy-C6-3-wind0  | completed / outside configured limits |    96.22 |      9.48 |           2.14 |        2.93 |        4.71 |    0.04 |
| dummy-C6-3-wind2  | completed / outside configured limits |    91.95 |      9.47 |           1.67 |        6.70 |        4.71 |    9.11 |
| dummy-C6-5-wind0  | completed / outside configured limits |    96.31 |      9.48 |           1.37 |       13.04 |        4.71 |    0.38 |
| dummy-C6-5-wind2  | completed / outside configured limits |    92.02 |      9.47 |           1.67 |       17.81 |        4.71 |    9.40 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    78.82 |     13.48 |           2.02 |        3.09 |        4.71 |    0.03 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    77.05 |     13.47 |           1.78 |        4.70 |        4.71 |   15.29 |
| actual-A8-3-wind0 | completed / outside configured limits |     8.08 |      7.00 |           2.17 | unavailable |       10.85 |    0.42 |
| actual-A8-3-wind2 | completed / outside configured limits |     8.01 |      6.99 |           1.33 | unavailable |       10.58 |    0.11 |
| actual-B4-4-wind0 | completed / outside configured limits |    27.98 |      8.74 |           2.16 |       16.72 |        4.72 |    1.14 |
| actual-B4-4-wind2 | completed / outside configured limits |    27.05 |      8.73 |           1.62 |       20.11 |        4.94 |   10.01 |
| actual-C6-3-wind0 | completed / outside configured limits |    96.22 |      9.48 |           2.14 |        2.93 |        4.71 |    0.04 |
| actual-C6-3-wind2 | completed / outside configured limits |    91.95 |      9.47 |           1.67 |        6.70 |        4.71 |    9.11 |
| actual-C6-5-wind0 | completed / outside configured limits |    96.31 |      9.48 |           1.37 |       13.04 |        4.71 |    0.38 |
| actual-C6-5-wind2 | completed / outside configured limits |    92.02 |      9.47 |           1.67 |       17.81 |        4.71 |    9.40 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    78.82 |     13.48 |           2.02 |        3.09 |        4.71 |    0.03 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    77.05 |     13.47 |           1.78 |        4.70 |        4.71 |   15.29 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Large angle of attack encountered (21.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: Recovery device deployment at high speed (20.1 m/s): "Nominal 457 mm parachute and lines"
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind0: no engine warnings
- actual-B4-4-wind2: Recovery device deployment at high speed (20.1 m/s): "Nominal 457 mm parachute and lines"
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: no engine warnings
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings

## Missing measurements / physical checks

- Exact XIAO board/camera/antenna identity and measured envelope
- Battery identity, connector/wire envelopes and retention measurements
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

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=131.7346665945891 g (allowed None … 85.0); apogee_m=10.938176381973593 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.056794338126513 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.173523075552733 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=131.7346665945891 g (allowed None … 85.0); apogee_m=10.800229074387628 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.047991435711891 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.82252927206797 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=11.331843718901075 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=134.28466659458908 g (allowed None … 99.0); guide_departure_m_s=9.875044175608963 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.486208833664316 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=134.28466659458908 g (allowed None … 99.0); guide_departure_m_s=9.866047876637488 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.9719821811105833 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.562954311288443 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=138.4846665945891 g (allowed None … 113.0); guide_departure_m_s=10.551043029068472 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=138.4846665945891 g (allowed None … 113.0); guide_departure_m_s=10.542692248630162 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=138.4846665945891 g (allowed None … 113.0); guide_departure_m_s=10.551043029068472 m/s
  (allowed 12.0 … None); deployment_speed_m_s=10.927144883104582 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=138.4846665945891 g (allowed None … 113.0); guide_departure_m_s=10.542692248630162 m/s
  (allowed 12.0 … None); deployment_speed_m_s=14.394898657325259 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=149.73466659458913 g (allowed None … 85.0); apogee_m=8.084826888061409 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.000644839904449 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.851540074354935 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=149.73466659458913 g (allowed None … 85.0); apogee_m=8.005787195879414 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.99321453996971 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.58123690051014 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=152.2846665945891 g (allowed None … 99.0); apogee_m=27.983683455054297 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.737754531446551 m/s (allowed 12.0 … None); deployment_speed_m_s=16.71743556230739 m/s
  (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=152.2846665945891 g (allowed None … 99.0); apogee_m=27.04983577499488 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.729910976197406 m/s (allowed 12.0 … None); deployment_speed_m_s=20.106242598759238 m/s
  (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.48080630341206 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.47336096961069 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.48080630341206 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.037818140296855 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.47336096961069 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.81445795159754 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=149.73466659458913 g (allowed None … 85.0); apogee_m=8.084826888061409 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.000644839904449 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.851540074354935 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=149.73466659458913 g (allowed None … 85.0); apogee_m=8.005787195879414 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.99321453996971 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.58123690051014 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=152.2846665945891 g (allowed None … 99.0); apogee_m=27.983683455054297 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.737754531446551 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.717435562307394 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=152.2846665945891 g (allowed None … 99.0); apogee_m=27.04983577499487 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.729910976197406 m/s (allowed 12.0 … None); deployment_speed_m_s=20.10624259875921 m/s
  (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.48080630341206 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.47336096961069 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.48080630341206 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.037818140296848 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=156.48466659458913 g (allowed None … 113.0); guide_departure_m_s=9.47336096961069 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.81445795159757 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is
  scenario-dependent.
- Native OpenRocket aerodynamics; conical nose, cylindrical sections, three flat trapezoidal fins and tapered collar
  fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in
  collar override.
- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful
  view.
- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using
  (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.
- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground
  event, not a structural impact assessment.
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
  "repository_revision": "18a0c3b671a46369804f7a5dbba68c724ffe34c2"
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
