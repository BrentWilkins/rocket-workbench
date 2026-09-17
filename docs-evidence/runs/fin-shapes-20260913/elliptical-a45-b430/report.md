# Rocket Workbench report

Run: `elliptical-a45-b430`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `ad03fa697b2f33ce1c50a8f26d02101ec1095b49f400e5ee04968a03ee31f24d`

## Cases

| Case               | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------ | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-D12-5-wind0  | completed / incomplete inputs         |   221.08 |     13.55 |           1.05 |       1.55 |        4.99 |    0.10 |           15.71 |            16.71 |             70.22 |
| empty-D12-5-wind2  | completed / outside configured limits |   219.72 |     13.54 |           0.51 |       2.37 |        4.99 |   68.85 |           15.70 |            16.70 |             70.09 |
| empty-D12-5-wind4  | completed / outside configured limits |   216.34 |     13.54 |           0.36 |       3.59 |        4.99 |  139.75 |           15.69 |            16.69 |             69.76 |
| dummy-D12-5-wind0  | completed / incomplete inputs         |   197.92 |     13.20 |           1.05 |       0.36 |        5.30 |    0.09 |           14.01 |            15.01 |             63.06 |
| dummy-D12-5-wind2  | completed / outside configured limits |   196.28 |     13.19 |           0.93 |       2.54 |        5.30 |   51.50 |           14.00 |            15.00 |             62.92 |
| dummy-D12-5-wind4  | completed / outside configured limits |   191.79 |     13.19 |           0.86 |       5.08 |        5.30 |  103.00 |           13.99 |            14.99 |             62.55 |
| actual-D12-5-wind0 | completed / incomplete inputs         |   197.92 |     13.20 |           1.05 |       0.36 |        5.30 |    0.09 |           14.01 |            15.01 |             63.06 |
| actual-D12-5-wind2 | completed / outside configured limits |   196.28 |     13.19 |           0.93 |       2.54 |        5.30 |   51.50 |           14.00 |            15.00 |             62.92 |
| actual-D12-5-wind4 | completed / outside configured limits |   191.79 |     13.19 |           0.86 |       5.08 |        5.30 |  103.00 |           13.99 |            14.99 |             62.55 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-D12-5-wind0: no engine warnings
- empty-D12-5-wind2: no engine warnings
- empty-D12-5-wind4: no engine warnings
- dummy-D12-5-wind0: no engine warnings
- dummy-D12-5-wind2: no engine warnings
- dummy-D12-5-wind4: no engine warnings
- actual-D12-5-wind0: no engine warnings
- actual-D12-5-wind2: no engine warnings
- actual-D12-5-wind4: no engine warnings

## Missing measurements / physical checks

- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: Provisional commercial 24 mm mount assembly plus CD spacer
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

- empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-D12-5-wind2: minimum_ascent_stability_cal=0.5083478551193835 cal (allowed 1.0 … None)
- empty-D12-5-wind4: minimum_ascent_stability_cal=0.3633206906070777 cal (allowed 1.0 … None)
- dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-5-wind2: minimum_ascent_stability_cal=0.9264072505653191 cal (allowed 1.0 … None)
- dummy-D12-5-wind4: minimum_ascent_stability_cal=0.8607118021747069 cal (allowed 1.0 … None)
- actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-5-wind2: minimum_ascent_stability_cal=0.9264072505653205 cal (allowed 1.0 … None)
- actual-D12-5-wind4: minimum_ascent_stability_cal=0.8607118021747056 cal (allowed 1.0 … None)

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

- apogee_m: 30.0 … None m; engineering assumption; New motor comparison: report altitude without inherited 120 m
  ceiling; retain 30 m minimum. Site altitude clearance is unassessed.
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
  "repository_revision": "2ca06e7f9c7adcd40d8e6847452df77f6a5b9717"
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
