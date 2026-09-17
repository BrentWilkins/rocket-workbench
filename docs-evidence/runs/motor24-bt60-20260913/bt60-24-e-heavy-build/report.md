# Rocket Workbench report

Run: `bt60-24-e-heavy-build`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `d9fa2880d9a504ba8606b9f67dbacfc2df429cc6d7c2be7a5be1975a1551a778`

## Cases

| Case               | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------ | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-E12-4-wind0  | completed / outside configured limits |   325.76 |     13.26 |           1.05 |      19.71 |        5.32 |    0.13 |           14.51 |            15.51 |             87.61 |
| empty-E12-4-wind2  | completed / outside configured limits |   323.72 |     13.25 |           0.64 |      19.70 |        5.32 |   93.38 |           14.50 |            15.50 |             87.47 |
| empty-E12-4-wind4  | completed / outside configured limits |   318.59 |     13.25 |           0.38 |      19.63 |        5.32 |  187.88 |           14.49 |            15.49 |             87.12 |
| empty-E12-6-wind0  | completed / outside configured limits |   340.91 |     13.26 |           0.64 |       0.54 |        5.32 |    0.20 |           14.51 |            15.51 |             87.61 |
| empty-E12-6-wind2  | completed / outside configured limits |   338.49 |     13.25 |           0.56 |       2.92 |        5.32 |   90.85 |           14.50 |            15.50 |             87.47 |
| empty-E12-6-wind4  | completed / outside configured limits |   332.24 |     13.25 |           0.38 |       5.60 |        5.32 |  183.81 |           14.49 |            15.49 |             87.12 |
| empty-E12-8-wind0  | completed / outside configured limits |   340.91 |     13.26 |           0.64 |      15.81 |        5.32 |    2.59 |           14.51 |            15.51 |             87.61 |
| empty-E12-8-wind2  | completed / outside configured limits |   338.49 |     13.25 |           0.56 |      15.63 |        5.32 |   80.90 |           14.50 |            15.50 |             87.47 |
| empty-E12-8-wind4  | completed / outside configured limits |   332.24 |     13.25 |           0.38 |      20.64 |        5.32 |  156.66 |           14.49 |            15.49 |             87.12 |
| dummy-E12-4-wind0  | completed / outside configured limits |   294.48 |     12.90 |           1.63 |      18.04 |        5.72 |    0.13 |           12.68 |            13.68 |             78.09 |
| dummy-E12-4-wind2  | completed / outside configured limits |   291.75 |     12.89 |           1.21 |      18.19 |        5.72 |   68.39 |           12.67 |            13.67 |             77.95 |
| dummy-E12-4-wind4  | completed / outside configured limits |   284.43 |     12.89 |           0.95 |      18.54 |        5.72 |  135.47 |           12.66 |            13.66 |             77.57 |
| dummy-E12-6-wind0  | completed / incomplete inputs         |   306.69 |     12.90 |           1.32 |       1.99 |        5.72 |    0.19 |           12.68 |            13.68 |             78.09 |
| dummy-E12-6-wind2  | completed / incomplete inputs         |   303.50 |     12.89 |           1.21 |       4.54 |        5.72 |   62.32 |           12.67 |            13.67 |             77.95 |
| dummy-E12-6-wind4  | completed / outside configured limits |   294.71 |     12.89 |           0.95 |       8.53 |        5.72 |  123.47 |           12.66 |            13.66 |             77.57 |
| dummy-E12-8-wind0  | completed / outside configured limits |   306.69 |     12.90 |           1.32 |      15.52 |        5.72 |    0.09 |           12.68 |            13.68 |             78.09 |
| dummy-E12-8-wind2  | completed / outside configured limits |   303.50 |     12.89 |           1.21 |      20.82 |        5.72 |   47.58 |           12.67 |            13.67 |             77.95 |
| dummy-E12-8-wind4  | completed / outside configured limits |   294.71 |     12.89 |           0.95 |      23.08 |        5.72 |   90.29 |           12.66 |            13.66 |             77.57 |
| actual-E12-4-wind0 | completed / outside configured limits |   294.48 |     12.90 |           1.63 |      18.04 |        5.72 |    0.13 |           12.68 |            13.68 |             78.09 |
| actual-E12-4-wind2 | completed / outside configured limits |   291.75 |     12.89 |           1.21 |      18.19 |        5.72 |   68.39 |           12.67 |            13.67 |             77.95 |
| actual-E12-4-wind4 | completed / outside configured limits |   284.43 |     12.89 |           0.95 |      18.54 |        5.72 |  135.47 |           12.66 |            13.66 |             77.57 |
| actual-E12-6-wind0 | completed / incomplete inputs         |   306.69 |     12.90 |           1.32 |       1.99 |        5.72 |    0.19 |           12.68 |            13.68 |             78.09 |
| actual-E12-6-wind2 | completed / incomplete inputs         |   303.50 |     12.89 |           1.21 |       4.54 |        5.72 |   62.32 |           12.67 |            13.67 |             77.95 |
| actual-E12-6-wind4 | completed / outside configured limits |   294.71 |     12.89 |           0.95 |       8.53 |        5.72 |  123.47 |           12.66 |            13.66 |             77.57 |
| actual-E12-8-wind0 | completed / outside configured limits |   306.69 |     12.90 |           1.32 |      15.52 |        5.72 |    0.09 |           12.68 |            13.68 |             78.09 |
| actual-E12-8-wind2 | completed / outside configured limits |   303.50 |     12.89 |           1.21 |      20.82 |        5.72 |   47.58 |           12.67 |            13.67 |             77.95 |
| actual-E12-8-wind4 | completed / outside configured limits |   294.71 |     12.89 |           0.95 |      23.08 |        5.72 |   90.29 |           12.66 |            13.66 |             77.57 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-E12-4-wind0: no engine warnings
- empty-E12-4-wind2: no engine warnings
- empty-E12-4-wind4: no engine warnings
- empty-E12-6-wind0: no engine warnings
- empty-E12-6-wind2: no engine warnings
- empty-E12-6-wind4: no engine warnings
- empty-E12-8-wind0: no engine warnings
- empty-E12-8-wind2: no engine warnings
- empty-E12-8-wind4: Recovery device deployment at high speed (20.6 m/s): "Nominal 457 mm parachute and lines"
- dummy-E12-4-wind0: no engine warnings
- dummy-E12-4-wind2: no engine warnings
- dummy-E12-4-wind4: no engine warnings
- dummy-E12-6-wind0: no engine warnings
- dummy-E12-6-wind2: no engine warnings
- dummy-E12-6-wind4: no engine warnings
- dummy-E12-8-wind0: no engine warnings
- dummy-E12-8-wind2: Recovery device deployment at high speed (20.8 m/s): "Nominal 457 mm parachute and lines"
- dummy-E12-8-wind4: Recovery device deployment at high speed (23.1 m/s): "Nominal 457 mm parachute and lines"
- actual-E12-4-wind0: no engine warnings
- actual-E12-4-wind2: no engine warnings
- actual-E12-4-wind4: no engine warnings
- actual-E12-6-wind0: no engine warnings
- actual-E12-6-wind2: no engine warnings
- actual-E12-6-wind4: no engine warnings
- actual-E12-8-wind0: no engine warnings
- actual-E12-8-wind2: Recovery device deployment at high speed (20.8 m/s): "Nominal 457 mm parachute and lines"
- actual-E12-8-wind4: Recovery device deployment at high speed (23.1 m/s): "Nominal 457 mm parachute and lines"

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
- Avionics board/antenna/battery masses, stack clearances, retention, wiring and power must be measured; vendor CAD is
  not physical validation
- Static-port drilling/alignment, bulkhead and screw seals, pressure lag and aerodynamic pressure bias require
  bench/flight validation

## Per-case criterion failures

- empty-E12-4-wind0: deployment_speed_m_s=19.707078091177713 m/s (allowed None … 10.0)
- empty-E12-4-wind2: minimum_ascent_stability_cal=0.6370499959636539 cal (allowed 1.0 … None);
  deployment_speed_m_s=19.699567686893296 m/s (allowed None … 10.0)
- empty-E12-4-wind4: minimum_ascent_stability_cal=0.37798428157132025 cal (allowed 1.0 … None);
  deployment_speed_m_s=19.629524179490897 m/s (allowed None … 10.0)
- empty-E12-6-wind0: minimum_ascent_stability_cal=0.6353612919323489 cal (allowed 1.0 … None)
- empty-E12-6-wind2: minimum_ascent_stability_cal=0.5612775864188072 cal (allowed 1.0 … None)
- empty-E12-6-wind4: minimum_ascent_stability_cal=0.37798428157132025 cal (allowed 1.0 … None)
- empty-E12-8-wind0: minimum_ascent_stability_cal=0.6353612919323489 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.807176707168493 m/s (allowed None … 10.0)
- empty-E12-8-wind2: minimum_ascent_stability_cal=0.5612775864188072 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.631487567367705 m/s (allowed None … 10.0)
- empty-E12-8-wind4: minimum_ascent_stability_cal=0.37798428157132025 cal (allowed 1.0 … None);
  deployment_speed_m_s=20.642602121666297 m/s (allowed None … 10.0)
- dummy-E12-4-wind0: deployment_speed_m_s=18.043602896563975 m/s (allowed None … 10.0)
- dummy-E12-4-wind2: deployment_speed_m_s=18.185180434154955 m/s (allowed None … 10.0)
- dummy-E12-4-wind4: minimum_ascent_stability_cal=0.9454621143129739 cal (allowed 1.0 … None);
  deployment_speed_m_s=18.54438942782475 m/s (allowed None … 10.0)
- dummy-E12-6-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-6-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-E12-6-wind4: minimum_ascent_stability_cal=0.9454621143129739 cal (allowed 1.0 … None)
- dummy-E12-8-wind0: deployment_speed_m_s=15.520938413447384 m/s (allowed None … 10.0)
- dummy-E12-8-wind2: deployment_speed_m_s=20.82137010361233 m/s (allowed None … 10.0)
- dummy-E12-8-wind4: minimum_ascent_stability_cal=0.9454621143129739 cal (allowed 1.0 … None);
  deployment_speed_m_s=23.084810264704867 m/s (allowed None … 10.0)
- actual-E12-4-wind0: deployment_speed_m_s=18.043602896563968 m/s (allowed None … 10.0)
- actual-E12-4-wind2: deployment_speed_m_s=18.18518043415486 m/s (allowed None … 10.0)
- actual-E12-4-wind4: minimum_ascent_stability_cal=0.9454621143129739 cal (allowed 1.0 … None);
  deployment_speed_m_s=18.544389427824715 m/s (allowed None … 10.0)
- actual-E12-6-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-6-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-E12-6-wind4: minimum_ascent_stability_cal=0.9454621143129739 cal (allowed 1.0 … None)
- actual-E12-8-wind0: deployment_speed_m_s=15.520938413446263 m/s (allowed None … 10.0)
- actual-E12-8-wind2: deployment_speed_m_s=20.8213701036108 m/s (allowed None … 10.0)
- actual-E12-8-wind4: minimum_ascent_stability_cal=0.9454621143129739 cal (allowed 1.0 … None);
  deployment_speed_m_s=23.08481026470495 m/s (allowed None … 10.0)

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
