# Rocket Workbench report

Run: `stress-20260912T192230Z-f253babf`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `8d929056fdda5a983779186e4424634032aa32c05694fdb4ccced41da8560371`

## Cases

| Case                | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
| ------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: |
| 0-empty-C5-3-wind0  | completed / incomplete inputs         |   102.36 |     14.12 |           1.62 |       1.17 |        5.81 |    0.04 |
| 0-empty-C5-3-wind2  | completed / incomplete inputs         |   100.88 |     14.11 |           1.19 |       2.81 |        5.81 |   19.40 |
| 0-empty-C5-3-wind4  | completed / incomplete inputs         |    96.94 |     14.11 |           1.05 |       5.06 |        5.81 |   39.53 |
| 0-dummy-C5-3-wind0  | completed / outside configured limits |    83.26 |     13.46 |           2.06 |       2.20 |        6.22 |    0.03 |
| 0-dummy-C5-3-wind2  | completed / outside configured limits |    81.52 |     13.45 |           1.80 |       4.05 |        6.22 |    8.40 |
| 0-dummy-C5-3-wind4  | completed / outside configured limits |    76.94 |     13.45 |           1.57 |       7.36 |        6.22 |   17.04 |
| 0-actual-C5-3-wind0 | completed / outside configured limits |    83.26 |     13.46 |           2.06 |       2.20 |        6.22 |    0.03 |
| 0-actual-C5-3-wind2 | completed / outside configured limits |    81.52 |     13.45 |           1.80 |       4.05 |        6.22 |    8.40 |
| 0-actual-C5-3-wind4 | completed / outside configured limits |    76.94 |     13.45 |           1.57 |       7.36 |        6.22 |   17.04 |
| 1-empty-C5-3-wind0  | completed / incomplete inputs         |   102.36 |     14.12 |           1.62 |       1.17 |        4.74 |    0.04 |
| 1-empty-C5-3-wind2  | completed / incomplete inputs         |   100.87 |     14.11 |           1.19 |       2.81 |        4.74 |   27.81 |
| 1-empty-C5-3-wind4  | completed / incomplete inputs         |    96.94 |     14.11 |           1.05 |       5.06 |        4.74 |   55.41 |
| 1-dummy-C5-3-wind0  | completed / incomplete inputs         |    83.26 |     13.46 |           2.06 |       2.20 |        5.08 |    0.03 |
| 1-dummy-C5-3-wind2  | completed / incomplete inputs         |    81.52 |     13.45 |           1.80 |       4.05 |        5.08 |   14.95 |
| 1-dummy-C5-3-wind4  | completed / incomplete inputs         |    76.94 |     13.45 |           1.57 |       7.36 |        5.08 |   29.10 |
| 1-actual-C5-3-wind0 | completed / incomplete inputs         |    83.26 |     13.46 |           2.06 |       2.20 |        5.08 |    0.03 |
| 1-actual-C5-3-wind2 | completed / incomplete inputs         |    81.52 |     13.45 |           1.80 |       4.05 |        5.08 |   14.95 |
| 1-actual-C5-3-wind4 | completed / incomplete inputs         |    76.94 |     13.45 |           1.57 |       7.36 |        5.08 |   29.10 |
| 2-empty-C5-3-wind0  | completed / incomplete inputs         |   102.36 |     14.12 |           1.62 |       1.17 |        5.81 |    0.04 |
| 2-empty-C5-3-wind2  | completed / incomplete inputs         |   100.88 |     14.11 |           1.19 |       2.81 |        5.81 |   19.40 |
| 2-empty-C5-3-wind4  | completed / incomplete inputs         |    96.94 |     14.11 |           1.05 |       5.06 |        5.81 |   39.53 |
| 2-dummy-C5-3-wind0  | completed / outside configured limits |    83.26 |     13.46 |           2.03 |       2.20 |        6.22 |    0.03 |
| 2-dummy-C5-3-wind2  | completed / outside configured limits |    81.52 |     13.45 |           1.77 |       4.05 |        6.22 |    8.39 |
| 2-dummy-C5-3-wind4  | completed / outside configured limits |    76.94 |     13.45 |           1.54 |       7.36 |        6.22 |   17.04 |
| 2-actual-C5-3-wind0 | completed / outside configured limits |    83.26 |     13.46 |           2.03 |       2.20 |        6.22 |    0.03 |
| 2-actual-C5-3-wind2 | completed / outside configured limits |    81.52 |     13.45 |           1.77 |       4.05 |        6.22 |    8.39 |
| 2-actual-C5-3-wind4 | completed / outside configured limits |    76.94 |     13.45 |           1.54 |       7.36 |        6.22 |   17.04 |
| 3-empty-C5-3-wind0  | completed / incomplete inputs         |   102.36 |     14.12 |           1.62 |       1.17 |        4.74 |    0.04 |
| 3-empty-C5-3-wind2  | completed / incomplete inputs         |   100.87 |     14.11 |           1.19 |       2.81 |        4.74 |   27.81 |
| 3-empty-C5-3-wind4  | completed / incomplete inputs         |    96.94 |     14.11 |           1.05 |       5.06 |        4.74 |   55.41 |
| 3-dummy-C5-3-wind0  | completed / incomplete inputs         |    83.26 |     13.46 |           2.03 |       2.20 |        5.08 |    0.03 |
| 3-dummy-C5-3-wind2  | completed / incomplete inputs         |    81.52 |     13.45 |           1.77 |       4.05 |        5.08 |   14.95 |
| 3-dummy-C5-3-wind4  | completed / incomplete inputs         |    76.94 |     13.45 |           1.54 |       7.36 |        5.08 |   29.10 |
| 3-actual-C5-3-wind0 | completed / incomplete inputs         |    83.26 |     13.46 |           2.03 |       2.20 |        5.08 |    0.03 |
| 3-actual-C5-3-wind2 | completed / incomplete inputs         |    81.52 |     13.45 |           1.77 |       4.05 |        5.08 |   14.95 |
| 3-actual-C5-3-wind4 | completed / incomplete inputs         |    76.94 |     13.45 |           1.54 |       7.36 |        5.08 |   29.10 |
| 4-empty-C5-3-wind0  | completed / outside configured limits |    89.72 |     13.89 |           1.14 |       0.99 |        6.08 |    0.04 |
| 4-empty-C5-3-wind2  | completed / outside configured limits |    88.13 |     13.88 |           1.14 |       3.13 |        6.08 |   12.52 |
| 4-empty-C5-3-wind4  | completed / outside configured limits |    83.93 |     13.88 |           1.08 |       6.14 |        6.08 |   25.66 |
| 4-dummy-C5-3-wind0  | completed / outside configured limits |    72.71 |     13.10 |           1.95 |       4.38 |        6.47 |    0.00 |
| 4-dummy-C5-3-wind2  | completed / outside configured limits |    70.89 |     13.10 |           1.81 |       5.75 |        6.47 |    2.97 |
| 4-dummy-C5-3-wind4  | completed / outside configured limits |    66.18 |     13.09 |           1.56 |       9.16 |        6.47 |    6.09 |
| 4-actual-C5-3-wind0 | completed / outside configured limits |    72.71 |     13.10 |           1.95 |       4.38 |        6.47 |    0.00 |
| 4-actual-C5-3-wind2 | completed / outside configured limits |    70.89 |     13.10 |           1.81 |       5.75 |        6.47 |    2.97 |
| 4-actual-C5-3-wind4 | completed / outside configured limits |    66.18 |     13.09 |           1.56 |       9.16 |        6.47 |    6.09 |
| 5-empty-C5-3-wind0  | completed / incomplete inputs         |    89.72 |     13.89 |           1.14 |       0.99 |        4.96 |    0.04 |
| 5-empty-C5-3-wind2  | completed / incomplete inputs         |    88.13 |     13.88 |           1.14 |       3.13 |        4.96 |   19.68 |
| 5-empty-C5-3-wind4  | completed / incomplete inputs         |    83.93 |     13.88 |           1.08 |       6.14 |        4.96 |   39.02 |
| 5-dummy-C5-3-wind0  | completed / incomplete inputs         |    72.71 |     13.10 |           1.95 |       4.38 |        5.28 |    0.01 |
| 5-dummy-C5-3-wind2  | completed / incomplete inputs         |    70.89 |     13.10 |           1.81 |       5.75 |        5.28 |    8.54 |
| 5-dummy-C5-3-wind4  | completed / incomplete inputs         |    66.18 |     13.09 |           1.56 |       9.16 |        5.28 |   16.12 |
| 5-actual-C5-3-wind0 | completed / incomplete inputs         |    72.71 |     13.10 |           1.95 |       4.38 |        5.28 |    0.01 |
| 5-actual-C5-3-wind2 | completed / incomplete inputs         |    70.89 |     13.10 |           1.81 |       5.75 |        5.28 |    8.54 |
| 5-actual-C5-3-wind4 | completed / incomplete inputs         |    66.18 |     13.09 |           1.56 |       9.16 |        5.28 |   16.12 |
| 6-empty-C5-3-wind0  | completed / outside configured limits |    89.72 |     13.89 |           1.14 |       0.99 |        6.08 |    0.04 |
| 6-empty-C5-3-wind2  | completed / outside configured limits |    88.13 |     13.88 |           1.14 |       3.13 |        6.08 |   12.52 |
| 6-empty-C5-3-wind4  | completed / outside configured limits |    83.93 |     13.88 |           1.08 |       6.14 |        6.08 |   25.66 |
| 6-dummy-C5-3-wind0  | completed / outside configured limits |    72.71 |     13.10 |           1.92 |       4.38 |        6.47 |    0.00 |
| 6-dummy-C5-3-wind2  | completed / outside configured limits |    70.89 |     13.10 |           1.78 |       5.75 |        6.47 |    2.97 |
| 6-dummy-C5-3-wind4  | completed / outside configured limits |    66.19 |     13.09 |           1.53 |       9.15 |        6.47 |    6.12 |
| 6-actual-C5-3-wind0 | completed / outside configured limits |    72.71 |     13.10 |           1.92 |       4.38 |        6.47 |    0.00 |
| 6-actual-C5-3-wind2 | completed / outside configured limits |    70.89 |     13.10 |           1.78 |       5.75 |        6.47 |    2.97 |
| 6-actual-C5-3-wind4 | completed / outside configured limits |    66.19 |     13.09 |           1.53 |       9.15 |        6.47 |    6.12 |
| 7-empty-C5-3-wind0  | completed / incomplete inputs         |    89.72 |     13.89 |           1.14 |       0.99 |        4.96 |    0.04 |
| 7-empty-C5-3-wind2  | completed / incomplete inputs         |    88.13 |     13.88 |           1.14 |       3.13 |        4.96 |   19.68 |
| 7-empty-C5-3-wind4  | completed / incomplete inputs         |    83.93 |     13.88 |           1.08 |       6.14 |        4.96 |   39.02 |
| 7-dummy-C5-3-wind0  | completed / incomplete inputs         |    72.71 |     13.10 |           1.92 |       4.38 |        5.28 |    0.01 |
| 7-dummy-C5-3-wind2  | completed / incomplete inputs         |    70.89 |     13.10 |           1.78 |       5.75 |        5.28 |    8.54 |
| 7-dummy-C5-3-wind4  | completed / incomplete inputs         |    66.19 |     13.09 |           1.53 |       9.15 |        5.28 |   16.15 |
| 7-actual-C5-3-wind0 | completed / incomplete inputs         |    72.71 |     13.10 |           1.92 |       4.38 |        5.28 |    0.01 |
| 7-actual-C5-3-wind2 | completed / incomplete inputs         |    70.89 |     13.10 |           1.78 |       5.75 |        5.28 |    8.54 |
| 7-actual-C5-3-wind4 | completed / incomplete inputs         |    66.19 |     13.09 |           1.53 |       9.15 |        5.28 |   16.15 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- 0-empty-C5-3-wind0: no engine warnings
- 0-empty-C5-3-wind2: no engine warnings
- 0-empty-C5-3-wind4: no engine warnings
- 0-dummy-C5-3-wind0: no engine warnings
- 0-dummy-C5-3-wind2: no engine warnings
- 0-dummy-C5-3-wind4: no engine warnings
- 0-actual-C5-3-wind0: no engine warnings
- 0-actual-C5-3-wind2: no engine warnings
- 0-actual-C5-3-wind4: no engine warnings
- 1-empty-C5-3-wind0: no engine warnings
- 1-empty-C5-3-wind2: no engine warnings
- 1-empty-C5-3-wind4: no engine warnings
- 1-dummy-C5-3-wind0: no engine warnings
- 1-dummy-C5-3-wind2: no engine warnings
- 1-dummy-C5-3-wind4: no engine warnings
- 1-actual-C5-3-wind0: no engine warnings
- 1-actual-C5-3-wind2: no engine warnings
- 1-actual-C5-3-wind4: no engine warnings
- 2-empty-C5-3-wind0: no engine warnings
- 2-empty-C5-3-wind2: no engine warnings
- 2-empty-C5-3-wind4: no engine warnings
- 2-dummy-C5-3-wind0: no engine warnings
- 2-dummy-C5-3-wind2: no engine warnings
- 2-dummy-C5-3-wind4: no engine warnings
- 2-actual-C5-3-wind0: no engine warnings
- 2-actual-C5-3-wind2: no engine warnings
- 2-actual-C5-3-wind4: no engine warnings
- 3-empty-C5-3-wind0: no engine warnings
- 3-empty-C5-3-wind2: no engine warnings
- 3-empty-C5-3-wind4: no engine warnings
- 3-dummy-C5-3-wind0: no engine warnings
- 3-dummy-C5-3-wind2: no engine warnings
- 3-dummy-C5-3-wind4: no engine warnings
- 3-actual-C5-3-wind0: no engine warnings
- 3-actual-C5-3-wind2: no engine warnings
- 3-actual-C5-3-wind4: no engine warnings
- 4-empty-C5-3-wind0: no engine warnings
- 4-empty-C5-3-wind2: no engine warnings
- 4-empty-C5-3-wind4: no engine warnings
- 4-dummy-C5-3-wind0: no engine warnings
- 4-dummy-C5-3-wind2: no engine warnings
- 4-dummy-C5-3-wind4: no engine warnings
- 4-actual-C5-3-wind0: no engine warnings
- 4-actual-C5-3-wind2: no engine warnings
- 4-actual-C5-3-wind4: no engine warnings
- 5-empty-C5-3-wind0: no engine warnings
- 5-empty-C5-3-wind2: no engine warnings
- 5-empty-C5-3-wind4: no engine warnings
- 5-dummy-C5-3-wind0: no engine warnings
- 5-dummy-C5-3-wind2: no engine warnings
- 5-dummy-C5-3-wind4: no engine warnings
- 5-actual-C5-3-wind0: no engine warnings
- 5-actual-C5-3-wind2: no engine warnings
- 5-actual-C5-3-wind4: no engine warnings
- 6-empty-C5-3-wind0: no engine warnings
- 6-empty-C5-3-wind2: no engine warnings
- 6-empty-C5-3-wind4: no engine warnings
- 6-dummy-C5-3-wind0: no engine warnings
- 6-dummy-C5-3-wind2: no engine warnings
- 6-dummy-C5-3-wind4: no engine warnings
- 6-actual-C5-3-wind0: no engine warnings
- 6-actual-C5-3-wind2: no engine warnings
- 6-actual-C5-3-wind4: no engine warnings
- 7-empty-C5-3-wind0: no engine warnings
- 7-empty-C5-3-wind2: no engine warnings
- 7-empty-C5-3-wind4: no engine warnings
- 7-dummy-C5-3-wind0: no engine warnings
- 7-dummy-C5-3-wind2: no engine warnings
- 7-dummy-C5-3-wind4: no engine warnings
- 7-actual-C5-3-wind0: no engine warnings
- 7-actual-C5-3-wind2: no engine warnings
- 7-actual-C5-3-wind4: no engine warnings

## Missing measurements / physical checks

- Exact XIAO board/camera/antenna identity and measured envelope
- Battery identity, connector/wire envelopes and retention measurements
- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: 18 mm motor mount tube, thrust ring, hook, two centering rings and adhesive
- Measured mass and balance: Nominal 381 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

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
    "pydantic": "2.13.5"
  }
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
