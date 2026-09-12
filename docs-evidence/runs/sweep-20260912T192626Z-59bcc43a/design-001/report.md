# Rocket Workbench report

Run: `design-001`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `bf3d38be3d2b17f89051fd42bf26fa762bdfe47d192cca025ad1157c7d3e5e4c`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-C5-3-wind0 | completed / incomplete inputs | 108.25 | 14.33 | 1.04 | 2.23 | 5.11 | 0.05 |
| empty-C5-3-wind2 | completed / outside configured limits | 106.73 | 14.32 | 0.84 | 3.33 | 5.11 | 26.73 |
| dummy-C5-3-wind0 | completed / incomplete inputs | 87.99 | 13.62 | 1.44 | 1.21 | 5.48 | 0.04 |
| dummy-C5-3-wind2 | completed / incomplete inputs | 86.23 | 13.62 | 1.24 | 3.65 | 5.48 | 13.93 |
| actual-C5-3-wind0 | completed / incomplete inputs | 87.99 | 13.62 | 1.44 | 1.21 | 5.48 | 0.04 |
| actual-C5-3-wind2 | completed / incomplete inputs | 86.23 | 13.62 | 1.24 | 3.65 | 5.48 | 13.93 |

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
- empty-C5-3-wind2: minimum_ascent_stability_cal=0.8369215721238373 cal (allowed 1.0 … None)
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
