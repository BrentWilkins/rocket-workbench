# Rocket Workbench report

Run: `bt60-24-e-inert-plus20`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `2a75ad8fca25bb125c90a3b4b3c2f13201fdb82259ccc57d156dfb21bc2a05e4`

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
| dummy-E12-4-wind0 | completed / outside configured limits | 305.38 | 12.99 | 1.84 | 18.75 | 5.58 | 0.13 | 13.26 | 14.26 | 81.28 |
| dummy-E12-4-wind2 | completed / outside configured limits | 302.68 | 12.98 | 1.42 | 18.85 | 5.58 | 74.65 | 13.26 | 14.25 | 81.14 |
| dummy-E12-4-wind4 | completed / outside configured limits | 295.34 | 12.98 | 1.16 | 19.13 | 5.58 | 147.27 | 13.24 | 14.24 | 80.75 |
| dummy-E12-6-wind0 | completed / incomplete inputs | 318.78 | 12.99 | 1.77 | 1.36 | 5.58 | 0.19 | 13.26 | 14.26 | 81.28 |
| dummy-E12-6-wind2 | completed / incomplete inputs | 315.59 | 12.98 | 1.42 | 4.21 | 5.58 | 69.25 | 13.26 | 14.25 | 81.14 |
| dummy-E12-6-wind4 | completed / incomplete inputs | 306.68 | 12.98 | 1.16 | 8.13 | 5.58 | 136.64 | 13.24 | 14.24 | 80.75 |
| dummy-E12-8-wind0 | completed / outside configured limits | 318.78 | 12.99 | 1.77 | 16.57 | 5.58 | 0.50 | 13.26 | 14.26 | 81.28 |
| dummy-E12-8-wind2 | completed / outside configured limits | 315.59 | 12.98 | 1.42 | 20.33 | 5.58 | 54.80 | 13.26 | 14.25 | 81.14 |
| dummy-E12-8-wind4 | completed / outside configured limits | 306.68 | 12.98 | 1.16 | 22.46 | 5.58 | 104.14 | 13.24 | 14.24 | 80.75 |
| actual-E12-4-wind0 | completed / outside configured limits | 305.38 | 12.99 | 1.84 | 18.75 | 5.58 | 0.13 | 13.26 | 14.26 | 81.28 |
| actual-E12-4-wind2 | completed / outside configured limits | 302.68 | 12.98 | 1.42 | 18.85 | 5.58 | 74.65 | 13.26 | 14.25 | 81.14 |
| actual-E12-4-wind4 | completed / outside configured limits | 295.34 | 12.98 | 1.16 | 19.13 | 5.58 | 147.27 | 13.24 | 14.24 | 80.75 |
| actual-E12-6-wind0 | completed / incomplete inputs | 318.78 | 12.99 | 1.77 | 1.36 | 5.58 | 0.19 | 13.26 | 14.26 | 81.28 |
| actual-E12-6-wind2 | completed / incomplete inputs | 315.59 | 12.98 | 1.42 | 4.21 | 5.58 | 69.25 | 13.26 | 14.25 | 81.14 |
| actual-E12-6-wind4 | completed / incomplete inputs | 306.68 | 12.98 | 1.16 | 8.13 | 5.58 | 136.64 | 13.24 | 14.24 | 80.75 |
| actual-E12-8-wind0 | completed / outside configured limits | 318.78 | 12.99 | 1.77 | 16.57 | 5.58 | 0.50 | 13.26 | 14.26 | 81.28 |
| actual-E12-8-wind2 | completed / outside configured limits | 315.59 | 12.98 | 1.42 | 20.33 | 5.58 | 54.80 | 13.26 | 14.25 | 81.14 |
| actual-E12-8-wind4 | completed / outside configured limits | 306.68 | 12.98 | 1.16 | 22.46 | 5.58 | 104.14 | 13.24 | 14.24 | 80.75 |

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
- dummy-E12-8-wind2: Recovery device deployment at high speed (20.3 m/s):  "Nominal 457 mm parachute and lines"
- dummy-E12-8-wind4: Recovery device deployment at high speed (22.5 m/s):  "Nominal 457 mm parachute and lines"
- actual-E12-4-wind0: no engine warnings
- actual-E12-4-wind2: no engine warnings
- actual-E12-4-wind4: no engine warnings
- actual-E12-6-wind0: no engine warnings
- actual-E12-6-wind2: no engine warnings
- actual-E12-6-wind4: no engine warnings
- actual-E12-8-wind0: no engine warnings
- actual-E12-8-wind2: Recovery device deployment at high speed (20.3 m/s):  "Nominal 457 mm parachute and lines"
- actual-E12-8-wind4: Recovery device deployment at high speed (22.5 m/s):  "Nominal 457 mm parachute and lines"

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

- empty-E12-4-wind0: minimum_ascent_stability_cal=0.9956563496375204 cal (allowed 1.0 … None); deployment_speed_m_s=20.097417337006558 m/s (allowed None … 10.0)
- empty-E12-4-wind2: minimum_ascent_stability_cal=0.5967489170061687 cal (allowed 1.0 … None); deployment_speed_m_s=20.044188761239788 m/s (allowed None … 10.0)
- empty-E12-4-wind4: minimum_ascent_stability_cal=0.3413475027376409 cal (allowed 1.0 … None); deployment_speed_m_s=19.862886799412525 m/s (allowed None … 10.0)
- empty-E12-6-wind0: minimum_ascent_stability_cal=0.48480712195584347 cal (allowed 1.0 … None)
- empty-E12-6-wind2: minimum_ascent_stability_cal=0.5104232946323428 cal (allowed 1.0 … None)
- empty-E12-6-wind4: minimum_ascent_stability_cal=0.3413475027376409 cal (allowed 1.0 … None)
- empty-E12-8-wind0: minimum_ascent_stability_cal=0.48480712195584347 cal (allowed 1.0 … None); deployment_speed_m_s=15.389153774532437 m/s (allowed None … 10.0)
- empty-E12-8-wind2: minimum_ascent_stability_cal=0.5104232946324335 cal (allowed 1.0 … None); deployment_speed_m_s=16.053095638147134 m/s (allowed None … 10.0)
- empty-E12-8-wind4: minimum_ascent_stability_cal=0.3413475027376409 cal (allowed 1.0 … None); deployment_speed_m_s=19.835320216671715 m/s (allowed None … 10.0)
- dummy-E12-4-wind0: deployment_speed_m_s=18.745864503671203 m/s (allowed None … 10.0)
- dummy-E12-4-wind2: deployment_speed_m_s=18.850955061674657 m/s (allowed None … 10.0)
- dummy-E12-4-wind4: deployment_speed_m_s=19.126597949526463 m/s (allowed None … 10.0)
- dummy-E12-6-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-6-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-6-wind4: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-8-wind0: deployment_speed_m_s=16.574342285746294 m/s (allowed None … 10.0)
- dummy-E12-8-wind2: deployment_speed_m_s=20.327766136532336 m/s (allowed None … 10.0)
- dummy-E12-8-wind4: deployment_speed_m_s=22.456994041250304 m/s (allowed None … 10.0)
- actual-E12-4-wind0: deployment_speed_m_s=18.745864503671225 m/s (allowed None … 10.0)
- actual-E12-4-wind2: deployment_speed_m_s=18.850955061674576 m/s (allowed None … 10.0)
- actual-E12-4-wind4: deployment_speed_m_s=19.12659794952444 m/s (allowed None … 10.0)
- actual-E12-6-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-6-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-6-wind4: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-8-wind0: deployment_speed_m_s=16.57434228574787 m/s (allowed None … 10.0)
- actual-E12-8-wind2: deployment_speed_m_s=20.327766136533427 m/s (allowed None … 10.0)
- actual-E12-8-wind4: deployment_speed_m_s=22.456994041249416 m/s (allowed None … 10.0)

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
