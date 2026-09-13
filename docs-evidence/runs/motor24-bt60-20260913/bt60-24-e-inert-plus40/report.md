# Rocket Workbench report

Run: `bt60-24-e-inert-plus40`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `6b0e0999c016a5656fd0e4bd50c3423703146f00145bd2da3e1de8bc5c7ff0a4`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| empty-E12-4-wind0 | completed / outside configured limits | 348.28 | 13.81 | 1.00 | 20.10 | 5.00 | 0.13 | 16.21 | 17.21 | 95.29 |
| empty-E12-4-wind2 | completed / outside configured limits | 346.51 | 13.80 | 0.60 | 20.04 | 5.00 | 112.35 | 16.20 | 17.20 | 95.17 |
| empty-E12-4-wind4 | completed / outside configured limits | 342.10 | 13.80 | 0.34 | 19.86 | 5.00 | 225.89 | 16.18 | 17.18 | 94.82 |
| empty-E12-6-wind0 | completed / outside configured limits | 364.27 | 13.81 | 0.48 | 0.27 | 5.00 | 0.20 | 16.21 | 17.21 | 95.29 |
| empty-E12-6-wind2 | completed / outside configured limits | 362.17 | 13.80 | 0.51 | 2.29 | 5.00 | 111.72 | 16.20 | 17.20 | 95.17 |
| empty-E12-6-wind4 | completed / outside configured limits | 356.79 | 13.80 | 0.34 | 4.38 | 5.00 | 225.59 | 16.18 | 17.18 | 94.82 |
| empty-E12-8-wind0 | completed / outside configured limits | 364.27 | 13.81 | 0.48 | 15.39 | 5.00 | 2.58 | 16.21 | 17.21 | 95.29 |
| empty-E12-8-wind2 | completed / outside configured limits | 362.17 | 13.80 | 0.51 | 16.05 | 5.00 | 103.20 | 16.20 | 17.20 | 95.17 |
| empty-E12-8-wind4 | completed / outside configured limits | 356.79 | 13.80 | 0.34 | 19.84 | 5.00 | 200.45 | 16.18 | 17.18 | 94.82 |
| dummy-E12-4-wind0 | completed / outside configured limits | 283.97 | 12.55 | 2.15 | 17.26 | 5.85 | 0.13 | 12.15 | 13.15 | 75.13 |
| dummy-E12-4-wind2 | completed / outside configured limits | 280.82 | 12.54 | 1.72 | 17.51 | 5.85 | 59.40 | 12.15 | 13.15 | 74.99 |
| dummy-E12-4-wind4 | completed / outside configured limits | 272.24 | 12.54 | 1.46 | 18.18 | 5.85 | 116.39 | 12.14 | 13.14 | 74.61 |
| dummy-E12-6-wind0 | completed / incomplete inputs | 294.91 | 12.55 | 1.71 | 2.71 | 5.85 | 0.18 | 12.15 | 13.15 | 75.13 |
| dummy-E12-6-wind2 | completed / incomplete inputs | 291.27 | 12.54 | 1.72 | 5.50 | 5.85 | 51.73 | 12.15 | 13.15 | 74.99 |
| dummy-E12-6-wind4 | completed / incomplete inputs | 281.03 | 12.54 | 1.46 | 9.98 | 5.85 | 100.83 | 12.14 | 13.14 | 74.61 |
| dummy-E12-8-wind0 | completed / outside configured limits | 294.91 | 12.55 | 1.71 | 17.51 | 5.85 | 1.43 | 12.15 | 13.15 | 75.13 |
| dummy-E12-8-wind2 | completed / outside configured limits | 291.27 | 12.54 | 1.72 | 21.97 | 5.85 | 35.21 | 12.15 | 13.15 | 74.99 |
| dummy-E12-8-wind4 | completed / outside configured limits | 281.03 | 12.54 | 1.46 | 24.27 | 5.85 | 64.68 | 12.14 | 13.14 | 74.61 |
| actual-E12-4-wind0 | completed / outside configured limits | 283.97 | 12.55 | 2.15 | 17.26 | 5.85 | 0.13 | 12.15 | 13.15 | 75.13 |
| actual-E12-4-wind2 | completed / outside configured limits | 280.82 | 12.54 | 1.72 | 17.51 | 5.85 | 59.40 | 12.15 | 13.15 | 74.99 |
| actual-E12-4-wind4 | completed / outside configured limits | 272.24 | 12.54 | 1.46 | 18.18 | 5.85 | 116.39 | 12.14 | 13.14 | 74.61 |
| actual-E12-6-wind0 | completed / incomplete inputs | 294.91 | 12.55 | 1.71 | 2.71 | 5.85 | 0.18 | 12.15 | 13.15 | 75.13 |
| actual-E12-6-wind2 | completed / incomplete inputs | 291.27 | 12.54 | 1.72 | 5.50 | 5.85 | 51.73 | 12.15 | 13.15 | 74.99 |
| actual-E12-6-wind4 | completed / incomplete inputs | 281.03 | 12.54 | 1.46 | 9.98 | 5.85 | 100.83 | 12.14 | 13.14 | 74.61 |
| actual-E12-8-wind0 | completed / outside configured limits | 294.91 | 12.55 | 1.71 | 17.51 | 5.85 | 1.43 | 12.15 | 13.15 | 75.13 |
| actual-E12-8-wind2 | completed / outside configured limits | 291.27 | 12.54 | 1.72 | 21.97 | 5.85 | 35.21 | 12.15 | 13.15 | 74.99 |
| actual-E12-8-wind4 | completed / outside configured limits | 281.03 | 12.54 | 1.46 | 24.27 | 5.85 | 64.68 | 12.14 | 13.14 | 74.61 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-E12-4-wind0: Recovery device deployment at high speed (20.1 m/s):  "Nominal 457 mm parachute and lines"
- empty-E12-4-wind2: Recovery device deployment at high speed (20 m/s):  "Nominal 457 mm parachute and lines"
- empty-E12-4-wind4: no engine warnings
- empty-E12-6-wind0: no engine warnings
- empty-E12-6-wind2: no engine warnings
- empty-E12-6-wind4: no engine warnings
- empty-E12-8-wind0: no engine warnings
- empty-E12-8-wind2: no engine warnings
- empty-E12-8-wind4: no engine warnings
- dummy-E12-4-wind0: no engine warnings
- dummy-E12-4-wind2: no engine warnings
- dummy-E12-4-wind4: no engine warnings
- dummy-E12-6-wind0: no engine warnings
- dummy-E12-6-wind2: no engine warnings
- dummy-E12-6-wind4: no engine warnings
- dummy-E12-8-wind0: no engine warnings
- dummy-E12-8-wind2: Recovery device deployment at high speed (22 m/s):  "Nominal 457 mm parachute and lines"
- dummy-E12-8-wind4: Recovery device deployment at high speed (24.3 m/s):  "Nominal 457 mm parachute and lines"
- actual-E12-4-wind0: no engine warnings
- actual-E12-4-wind2: no engine warnings
- actual-E12-4-wind4: no engine warnings
- actual-E12-6-wind0: no engine warnings
- actual-E12-6-wind2: no engine warnings
- actual-E12-6-wind4: no engine warnings
- actual-E12-8-wind0: no engine warnings
- actual-E12-8-wind2: Recovery device deployment at high speed (22 m/s):  "Nominal 457 mm parachute and lines"
- actual-E12-8-wind4: Recovery device deployment at high speed (24.3 m/s):  "Nominal 457 mm parachute and lines"

## Missing measurements / physical checks

- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: Provisional commercial 24 mm mount assembly
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

- empty-E12-4-wind0: minimum_ascent_stability_cal=0.995656349637523 cal (allowed 1.0 … None); deployment_speed_m_s=20.097417337006544 m/s (allowed None … 10.0)
- empty-E12-4-wind2: minimum_ascent_stability_cal=0.59674891700617 cal (allowed 1.0 … None); deployment_speed_m_s=20.044188761239372 m/s (allowed None … 10.0)
- empty-E12-4-wind4: minimum_ascent_stability_cal=0.3413475027376409 cal (allowed 1.0 … None); deployment_speed_m_s=19.86288679941009 m/s (allowed None … 10.0)
- empty-E12-6-wind0: minimum_ascent_stability_cal=0.48480712194620107 cal (allowed 1.0 … None)
- empty-E12-6-wind2: minimum_ascent_stability_cal=0.5104232946306602 cal (allowed 1.0 … None)
- empty-E12-6-wind4: minimum_ascent_stability_cal=0.3413475027376409 cal (allowed 1.0 … None)
- empty-E12-8-wind0: minimum_ascent_stability_cal=0.48480712194620107 cal (allowed 1.0 … None); deployment_speed_m_s=15.389153774524033 m/s (allowed None … 10.0)
- empty-E12-8-wind2: minimum_ascent_stability_cal=0.5104232946307509 cal (allowed 1.0 … None); deployment_speed_m_s=16.053095638166933 m/s (allowed None … 10.0)
- empty-E12-8-wind4: minimum_ascent_stability_cal=0.3413475027376409 cal (allowed 1.0 … None); deployment_speed_m_s=19.835320216686483 m/s (allowed None … 10.0)
- dummy-E12-4-wind0: deployment_speed_m_s=17.258966537772547 m/s (allowed None … 10.0)
- dummy-E12-4-wind2: deployment_speed_m_s=17.5070216608288 m/s (allowed None … 10.0)
- dummy-E12-4-wind4: deployment_speed_m_s=18.175436590496254 m/s (allowed None … 10.0)
- dummy-E12-6-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-6-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-6-wind4: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-8-wind0: deployment_speed_m_s=17.509409843003326 m/s (allowed None … 10.0)
- dummy-E12-8-wind2: deployment_speed_m_s=21.967065185184126 m/s (allowed None … 10.0)
- dummy-E12-8-wind4: deployment_speed_m_s=24.27419408411914 m/s (allowed None … 10.0)
- actual-E12-4-wind0: deployment_speed_m_s=17.258966537772547 m/s (allowed None … 10.0)
- actual-E12-4-wind2: deployment_speed_m_s=17.5070216608288 m/s (allowed None … 10.0)
- actual-E12-4-wind4: deployment_speed_m_s=18.175436590445713 m/s (allowed None … 10.0)
- actual-E12-6-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-6-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-6-wind4: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-8-wind0: deployment_speed_m_s=17.509409843003308 m/s (allowed None … 10.0)
- actual-E12-8-wind2: deployment_speed_m_s=21.967065185183714 m/s (allowed None … 10.0)
- actual-E12-8-wind4: deployment_speed_m_s=24.27419408396563 m/s (allowed None … 10.0)

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
