# Rocket Workbench report

Run: `design-003`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `c4f0b13ba226b96661e86038f9213c9e91cd1faebbaaa6138f12bf79b1af1791`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-C5-3-wind0 | completed / incomplete inputs | 105.25 | 14.37 | 1.34 | 1.69 | 5.15 | 0.05 |
| empty-C5-3-wind2 | completed / incomplete inputs | 103.75 | 14.36 | 1.07 | 3.03 | 5.15 | 25.28 |
| dummy-C5-3-wind0 | completed / incomplete inputs | 85.58 | 13.67 | 1.74 | 1.71 | 5.52 | 0.04 |
| dummy-C5-3-wind2 | completed / incomplete inputs | 83.83 | 13.66 | 1.53 | 3.83 | 5.52 | 12.88 |
| actual-C5-3-wind0 | completed / incomplete inputs | 85.58 | 13.67 | 1.74 | 1.71 | 5.52 | 0.04 |
| actual-C5-3-wind2 | completed / incomplete inputs | 83.83 | 13.66 | 1.53 | 3.83 | 5.52 | 12.88 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings

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

## Per-case criterion failures

- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is scenario-dependent.
- Native OpenRocket aerodynamics; conical nose, cylindrical sections, three flat trapezoidal fins and tapered collar fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in collar override.
- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful view.
- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.
- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground event, not a structural impact assessment.
- Recovery is motor-ejection deployment with configured Cd; packing envelope, ejection seal, thermal protection and attachment loads require physical checks.
- Reference mode preserves upstream geometry and masses; demonstration CAD and baseline mass assumptions do not apply to that reference.

## Configured criteria

- apogee_m: 30.0 … 120.0 m; engineering assumption; Project engineering assumption for demonstration screening; not a launch clearance
- guide_departure_m_s: 12.0 … None m/s; engineering assumption; Project engineering assumption for demonstration screening; not a launch clearance
- minimum_ascent_stability_cal: 1.0 … None cal; engineering assumption; Project engineering assumption for demonstration screening; not a launch clearance
- deployment_speed_m_s: None … 10.0 m/s; engineering assumption; Project engineering assumption for demonstration screening; not a launch clearance
- landing_descent_m_s: None … 6.0 m/s; engineering assumption; Project engineering assumption for demonstration screening; not a launch clearance

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
  "repository_revision": null
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the table.
