# Rocket Workbench report

Run: `bt60-18-c5-heavy-build`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `8f0e4ddf3cafbb73e72b2e692008f4d2eab7623f2a35d533cdd09c433b3bd26d`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| empty-C5-3-wind0 | completed / incomplete inputs | 60.23 | 12.61 | 1.42 | 7.26 | 5.07 | 0.05 | 10.74 | 11.74 | 23.32 |
| empty-C5-3-wind2 | completed / incomplete inputs | 58.47 | 12.60 | 1.04 | 8.02 | 5.07 | 4.34 | 10.73 | 11.73 | 23.16 |
| empty-C5-3-wind4 | completed / outside configured limits | 54.13 | 12.60 | 0.95 | 11.35 | 5.07 | 7.78 | 10.72 | 11.72 | 22.76 |
| dummy-C5-3-wind0 | completed / outside configured limits | 42.97 | 11.49 | 2.17 | 11.34 | 5.49 | 0.44 | 9.08 | 10.08 | 17.85 |
| dummy-C5-3-wind2 | completed / outside configured limits | 40.88 | 11.48 | 1.79 | 13.25 | 5.49 | 8.53 | 9.07 | 10.07 | 17.74 |
| dummy-C5-3-wind4 | completed / outside configured limits | 36.05 | 11.48 | 1.52 | 16.64 | 5.49 | 18.44 | 9.07 | 10.07 | 17.48 |
| actual-C5-3-wind0 | completed / outside configured limits | 42.97 | 11.49 | 2.17 | 11.34 | 5.49 | 0.44 | 9.08 | 10.08 | 17.85 |
| actual-C5-3-wind2 | completed / outside configured limits | 40.88 | 11.48 | 1.79 | 13.25 | 5.49 | 8.53 | 9.07 | 10.07 | 17.74 |
| actual-C5-3-wind4 | completed / outside configured limits | 36.05 | 11.48 | 1.52 | 16.64 | 5.49 | 18.44 | 9.07 | 10.07 | 17.48 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- empty-C5-3-wind4: no engine warnings
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- dummy-C5-3-wind4: no engine warnings
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings
- actual-C5-3-wind4: no engine warnings

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
- Avionics board/antenna/battery masses, stack clearances, retention, wiring and power must be measured; vendor CAD is not physical validation
- Static-port drilling/alignment, bulkhead and screw seals, pressure lag and aerodynamic pressure bias require bench/flight validation

## Per-case criterion failures

- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind4: minimum_ascent_stability_cal=0.946744006174241 cal (allowed 1.0 … None); deployment_speed_m_s=11.347983123418762 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: guide_departure_m_s=11.488878883783299 m/s (allowed 12.0 … None); deployment_speed_m_s=11.338875998302202 m/s (allowed None … 10.0)
- dummy-C5-3-wind2: guide_departure_m_s=11.483366301552094 m/s (allowed 12.0 … None); deployment_speed_m_s=13.248686196439158 m/s (allowed None … 10.0)
- dummy-C5-3-wind4: guide_departure_m_s=11.4815994615015 m/s (allowed 12.0 … None); deployment_speed_m_s=16.63974733628407 m/s (allowed None … 10.0)
- actual-C5-3-wind0: guide_departure_m_s=11.488878883783299 m/s (allowed 12.0 … None); deployment_speed_m_s=11.338875998302202 m/s (allowed None … 10.0)
- actual-C5-3-wind2: guide_departure_m_s=11.483366301552094 m/s (allowed 12.0 … None); deployment_speed_m_s=13.248686196439152 m/s (allowed None … 10.0)
- actual-C5-3-wind4: guide_departure_m_s=11.4815994615015 m/s (allowed 12.0 … None); deployment_speed_m_s=16.63974733628415 m/s (allowed None … 10.0)

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is scenario-dependent.
- Native OpenRocket aerodynamics; configured axisymmetric nose, cylindrical sections, three flat trapezoidal fins and tapered collar fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in collar override.
- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful view.
- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.
- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground event, not a structural impact assessment.
- Powered peaks use positive-thrust samples from liftoff strictly before first burnout, deployment, abort or ground contact. Missing events/data yield unavailable metrics; peak times and sample coverage are in JSON. These are sampled single-stage maxima, not continuous-time bounds.
- Powered acceleration is trajectory acceleration magnitude / 9.80665. Estimated load is hypot(lateral acceleration, vertical acceleration + local gravity) / 9.80665 at the center of mass. Coriolis correction, sensor-offset rotation, vibration and deployment/impact shock are excluded; this is not a per-axis IMU prediction or a hardware survival rating.
- Recovery is motor-ejection deployment with configured Cd; packing envelope, ejection seal, thermal protection and attachment loads require physical checks.
- Reference mode preserves upstream geometry and masses; demonstration CAD and baseline mass assumptions do not apply to that reference.

## Configured criteria

- apogee_m: 30.0 … None m; engineering assumption; New motor comparison: report altitude without inherited 120 m ceiling; retain 30 m minimum. Site altitude clearance is unassessed.
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
  "repository_revision": "2ca06e7f9c7adcd40d8e6847452df77f6a5b9717"
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the table.
