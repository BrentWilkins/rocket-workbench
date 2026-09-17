# Rocket Workbench report

Run: `bt60-24-cd-inert-plus40`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `2b0067912a892293255174cffdff933e9236906ceebb845706d02834ddb7bea0`

## Cases

| Case               | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------ | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-C11-3-wind0  | completed / outside configured limits |    88.47 |     12.47 |           1.30 |       6.77 |        5.01 |    0.02 |           11.79 |            12.79 |             42.24 |
| empty-C11-3-wind2  | completed / outside configured limits |    87.79 |     12.46 |           0.87 |       6.74 |        5.01 |   29.02 |           11.78 |            12.78 |             42.12 |
| empty-C11-3-wind4  | completed / outside configured limits |    86.22 |     12.46 |           0.61 |       6.62 |        5.01 |   58.74 |           11.77 |            12.76 |             41.83 |
| empty-C11-5-wind0  | completed / outside configured limits |    89.56 |     12.47 |           0.52 |      11.77 |        5.01 |    0.61 |           11.79 |            12.79 |             42.24 |
| empty-C11-5-wind2  | completed / outside configured limits |    88.91 |     12.46 |           0.42 |      11.22 |        5.01 |   24.36 |           11.78 |            12.78 |             42.12 |
| empty-C11-5-wind4  | completed / outside configured limits |    87.30 |     12.46 |           0.61 |      12.40 |        5.01 |   47.33 |           11.77 |            12.76 |             41.83 |
| empty-D12-3-wind0  | completed / outside configured limits |   201.33 |     13.64 |           1.17 |      21.95 |        4.98 |    0.05 |           15.80 |            16.80 |             70.44 |
| empty-D12-3-wind2  | completed / outside configured limits |   200.21 |     13.63 |           0.77 |      21.87 |        4.98 |   66.21 |           15.79 |            16.79 |             70.30 |
| empty-D12-3-wind4  | completed / outside configured limits |   197.37 |     13.63 |           0.51 |      21.64 |        4.98 |  132.67 |           15.78 |            16.78 |             69.95 |
| empty-D12-5-wind0  | completed / incomplete inputs         |   220.65 |     13.64 |           1.17 |       1.34 |        4.98 |    0.10 |           15.80 |            16.80 |             70.44 |
| empty-D12-5-wind2  | completed / outside configured limits |   219.15 |     13.63 |           0.65 |       2.41 |        4.98 |   67.34 |           15.79 |            16.79 |             70.30 |
| empty-D12-5-wind4  | completed / outside configured limits |   215.30 |     13.63 |           0.51 |       3.97 |        4.98 |  135.88 |           15.78 |            16.78 |             69.95 |
| empty-D12-7-wind0  | completed / outside configured limits |   220.65 |     13.64 |           0.94 |      14.21 |        4.98 |    2.06 |           15.80 |            16.80 |             70.44 |
| empty-D12-7-wind2  | completed / outside configured limits |   219.17 |     13.63 |           0.48 |      15.04 |        4.98 |   59.70 |           15.79 |            16.79 |             70.30 |
| empty-D12-7-wind4  | completed / outside configured limits |   215.30 |     13.63 |           0.51 |      18.22 |        4.98 |  113.61 |           15.78 |            16.78 |             69.95 |
| dummy-C11-3-wind0  | completed / outside configured limits |    53.46 |     11.14 |           2.46 |       1.51 |        5.85 |    0.01 |            8.49 |             9.49 |             29.84 |
| dummy-C11-3-wind2  | completed / outside configured limits |    52.83 |     11.14 |           1.62 |       2.19 |        5.85 |   10.66 |            8.48 |             9.48 |             29.71 |
| dummy-C11-3-wind4  | completed / outside configured limits |    51.10 |     11.14 |           1.76 |       3.66 |        5.85 |   21.37 |            8.48 |             9.47 |             29.34 |
| dummy-C11-5-wind0  | completed / outside configured limits |    53.46 |     11.14 |           2.46 |      16.70 |        5.85 |    1.20 |            8.49 |             9.49 |             29.84 |
| dummy-C11-5-wind2  | completed / outside configured limits |    52.83 |     11.14 |           1.62 |      19.00 |        5.85 |    0.88 |            8.48 |             9.48 |             29.71 |
| dummy-C11-5-wind4  | completed / outside configured limits |    51.10 |     11.14 |           1.76 |      20.95 |        5.85 |    0.63 |            8.48 |             9.47 |             29.34 |
| dummy-D12-3-wind0  | completed / outside configured limits |   149.12 |     12.47 |           2.36 |      14.69 |        5.83 |    0.05 |           11.59 |            12.59 |             51.93 |
| dummy-D12-3-wind2  | completed / outside configured limits |   147.30 |     12.47 |           1.93 |      14.82 |        5.83 |   31.73 |           11.58 |            12.58 |             51.78 |
| dummy-D12-3-wind4  | completed / outside configured limits |   142.43 |     12.47 |           1.67 |      15.20 |        5.83 |   62.42 |           11.58 |            12.58 |             51.37 |
| dummy-D12-5-wind0  | completed / incomplete inputs         |   156.61 |     12.47 |           2.03 |       5.13 |        5.83 |    0.05 |           11.59 |            12.59 |             51.93 |
| dummy-D12-5-wind2  | completed / incomplete inputs         |   154.51 |     12.47 |           1.93 |       6.26 |        5.83 |   25.15 |           11.58 |            12.58 |             51.78 |
| dummy-D12-5-wind4  | completed / incomplete inputs         |   148.65 |     12.47 |           1.67 |       9.53 |        5.83 |   48.45 |           11.58 |            12.58 |             51.37 |
| dummy-D12-7-wind0  | completed / outside configured limits |   156.61 |     12.47 |           2.03 |      19.43 |        5.83 |    1.93 |           11.59 |            12.59 |             51.93 |
| dummy-D12-7-wind2  | completed / outside configured limits |   154.51 |     12.47 |           1.93 |      23.55 |        5.83 |    9.19 |           11.58 |            12.58 |             51.78 |
| dummy-D12-7-wind4  | completed / outside configured limits |   148.65 |     12.47 |           1.67 |      25.45 |        5.83 |   13.39 |           11.58 |            12.58 |             51.37 |
| actual-C11-3-wind0 | completed / outside configured limits |    53.46 |     11.14 |           2.46 |       1.51 |        5.85 |    0.01 |            8.49 |             9.49 |             29.84 |
| actual-C11-3-wind2 | completed / outside configured limits |    52.83 |     11.14 |           1.62 |       2.19 |        5.85 |   10.66 |            8.48 |             9.48 |             29.71 |
| actual-C11-3-wind4 | completed / outside configured limits |    51.10 |     11.14 |           1.76 |       3.66 |        5.85 |   21.37 |            8.48 |             9.47 |             29.34 |
| actual-C11-5-wind0 | completed / outside configured limits |    53.46 |     11.14 |           2.46 |      16.70 |        5.85 |    1.20 |            8.49 |             9.49 |             29.84 |
| actual-C11-5-wind2 | completed / outside configured limits |    52.83 |     11.14 |           1.62 |      19.00 |        5.85 |    0.88 |            8.48 |             9.48 |             29.71 |
| actual-C11-5-wind4 | completed / outside configured limits |    51.10 |     11.14 |           1.76 |      20.95 |        5.85 |    0.63 |            8.48 |             9.47 |             29.34 |
| actual-D12-3-wind0 | completed / outside configured limits |   149.12 |     12.47 |           2.36 |      14.69 |        5.83 |    0.05 |           11.59 |            12.59 |             51.93 |
| actual-D12-3-wind2 | completed / outside configured limits |   147.30 |     12.47 |           1.93 |      14.82 |        5.83 |   31.73 |           11.58 |            12.58 |             51.78 |
| actual-D12-3-wind4 | completed / outside configured limits |   142.43 |     12.47 |           1.67 |      15.20 |        5.83 |   62.42 |           11.58 |            12.58 |             51.37 |
| actual-D12-5-wind0 | completed / incomplete inputs         |   156.61 |     12.47 |           2.03 |       5.13 |        5.83 |    0.05 |           11.59 |            12.59 |             51.93 |
| actual-D12-5-wind2 | completed / incomplete inputs         |   154.51 |     12.47 |           1.93 |       6.26 |        5.83 |   25.15 |           11.58 |            12.58 |             51.78 |
| actual-D12-5-wind4 | completed / incomplete inputs         |   148.65 |     12.47 |           1.67 |       9.53 |        5.83 |   48.45 |           11.58 |            12.58 |             51.37 |
| actual-D12-7-wind0 | completed / outside configured limits |   156.61 |     12.47 |           2.03 |      19.43 |        5.83 |    1.93 |           11.59 |            12.59 |             51.93 |
| actual-D12-7-wind2 | completed / outside configured limits |   154.51 |     12.47 |           1.93 |      23.55 |        5.83 |    9.19 |           11.58 |            12.58 |             51.78 |
| actual-D12-7-wind4 | completed / outside configured limits |   148.65 |     12.47 |           1.67 |      25.45 |        5.83 |   13.39 |           11.58 |            12.58 |             51.37 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-C11-3-wind0: no engine warnings
- empty-C11-3-wind2: no engine warnings
- empty-C11-3-wind4: no engine warnings
- empty-C11-5-wind0: no engine warnings
- empty-C11-5-wind2: no engine warnings
- empty-C11-5-wind4: no engine warnings
- empty-D12-3-wind0: Recovery device deployment at high speed (22 m/s): "Nominal 457 mm parachute and lines"
- empty-D12-3-wind2: Recovery device deployment at high speed (21.9 m/s): "Nominal 457 mm parachute and lines"
- empty-D12-3-wind4: Recovery device deployment at high speed (21.6 m/s): "Nominal 457 mm parachute and lines"
- empty-D12-5-wind0: no engine warnings
- empty-D12-5-wind2: no engine warnings
- empty-D12-5-wind4: no engine warnings
- empty-D12-7-wind0: no engine warnings
- empty-D12-7-wind2: no engine warnings
- empty-D12-7-wind4: no engine warnings
- dummy-C11-3-wind0: no engine warnings
- dummy-C11-3-wind2: no engine warnings
- dummy-C11-3-wind4: no engine warnings
- dummy-C11-5-wind0: no engine warnings
- dummy-C11-5-wind2: no engine warnings
- dummy-C11-5-wind4: Recovery device deployment at high speed (21 m/s): "Nominal 457 mm parachute and lines"
- dummy-D12-3-wind0: no engine warnings
- dummy-D12-3-wind2: no engine warnings
- dummy-D12-3-wind4: no engine warnings
- dummy-D12-5-wind0: no engine warnings
- dummy-D12-5-wind2: no engine warnings
- dummy-D12-5-wind4: no engine warnings
- dummy-D12-7-wind0: no engine warnings
- dummy-D12-7-wind2: Recovery device deployment at high speed (23.6 m/s): "Nominal 457 mm parachute and lines"
- dummy-D12-7-wind4: Recovery device deployment at high speed (25.5 m/s): "Nominal 457 mm parachute and lines"
- actual-C11-3-wind0: no engine warnings
- actual-C11-3-wind2: no engine warnings
- actual-C11-3-wind4: no engine warnings
- actual-C11-5-wind0: no engine warnings
- actual-C11-5-wind2: no engine warnings
- actual-C11-5-wind4: Recovery device deployment at high speed (21 m/s): "Nominal 457 mm parachute and lines"
- actual-D12-3-wind0: no engine warnings
- actual-D12-3-wind2: no engine warnings
- actual-D12-3-wind4: no engine warnings
- actual-D12-5-wind0: no engine warnings
- actual-D12-5-wind2: no engine warnings
- actual-D12-5-wind4: no engine warnings
- actual-D12-7-wind0: no engine warnings
- actual-D12-7-wind2: Recovery device deployment at high speed (23.6 m/s): "Nominal 457 mm parachute and lines"
- actual-D12-7-wind4: Recovery device deployment at high speed (25.5 m/s): "Nominal 457 mm parachute and lines"

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

- empty-C11-3-wind0: launch_mass_g=176.7987754861409 g (allowed None … 170.0)
- empty-C11-3-wind2: launch_mass_g=176.7987754861409 g (allowed None … 170.0);
  minimum_ascent_stability_cal=0.8725245292701027 cal (allowed 1.0 … None)
- empty-C11-3-wind4: launch_mass_g=176.7987754861409 g (allowed None … 170.0);
  minimum_ascent_stability_cal=0.6088368987618805 cal (allowed 1.0 … None)
- empty-C11-5-wind0: launch_mass_g=176.7987754861409 g (allowed None … 142.0);
  minimum_ascent_stability_cal=0.5246398166729466 cal (allowed 1.0 … None); deployment_speed_m_s=11.769103224595435 m/s
  (allowed None … 10.0)
- empty-C11-5-wind2: launch_mass_g=176.7987754861409 g (allowed None … 142.0);
  minimum_ascent_stability_cal=0.4162405796050484 cal (allowed 1.0 … None); deployment_speed_m_s=11.22397727133237 m/s
  (allowed None … 10.0)
- empty-C11-5-wind4: launch_mass_g=176.7987754861409 g (allowed None … 142.0);
  minimum_ascent_stability_cal=0.6088368987618805 cal (allowed 1.0 … None); deployment_speed_m_s=12.395605363866053 m/s
  (allowed None … 10.0)
- empty-D12-3-wind0: deployment_speed_m_s=21.953560020180202 m/s (allowed None … 10.0)
- empty-D12-3-wind2: minimum_ascent_stability_cal=0.7696940909901994 cal (allowed 1.0 … None);
  deployment_speed_m_s=21.87356638450768 m/s (allowed None … 10.0)
- empty-D12-3-wind4: minimum_ascent_stability_cal=0.5133969559955419 cal (allowed 1.0 … None);
  deployment_speed_m_s=21.640279609899025 m/s (allowed None … 10.0)
- empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-D12-5-wind2: minimum_ascent_stability_cal=0.6501936367240699 cal (allowed 1.0 … None)
- empty-D12-5-wind4: minimum_ascent_stability_cal=0.5133969559955419 cal (allowed 1.0 … None)
- empty-D12-7-wind0: minimum_ascent_stability_cal=0.940589732860348 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.212988032012925 m/s (allowed None … 10.0)
- empty-D12-7-wind2: minimum_ascent_stability_cal=0.4839275554746494 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.036727874889165 m/s (allowed None … 10.0)
- empty-D12-7-wind4: minimum_ascent_stability_cal=0.5133969559955419 cal (allowed 1.0 … None);
  deployment_speed_m_s=18.22299770519219 m/s (allowed None … 10.0)
- dummy-C11-3-wind0: launch_mass_g=237.44877548614087 g (allowed None … 170.0); guide_departure_m_s=11.143118786216577
  m/s (allowed 12.0 … None)
- dummy-C11-3-wind2: launch_mass_g=237.44877548614087 g (allowed None … 170.0); guide_departure_m_s=11.138334802910082
  m/s (allowed 12.0 … None)
- dummy-C11-3-wind4: launch_mass_g=237.44877548614087 g (allowed None … 170.0); guide_departure_m_s=11.13721449094316
  m/s (allowed 12.0 … None)
- dummy-C11-5-wind0: launch_mass_g=237.44877548614087 g (allowed None … 142.0); guide_departure_m_s=11.143118786216577
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.701179916815555 m/s (allowed None … 10.0)
- dummy-C11-5-wind2: launch_mass_g=237.44877548614087 g (allowed None … 142.0); guide_departure_m_s=11.138334802910082
  m/s (allowed 12.0 … None); deployment_speed_m_s=18.997740238486497 m/s (allowed None … 10.0)
- dummy-C11-5-wind4: launch_mass_g=237.44877548614087 g (allowed None … 142.0); guide_departure_m_s=11.13721449094316
  m/s (allowed 12.0 … None); deployment_speed_m_s=20.953577226974915 m/s (allowed None … 10.0)
- dummy-D12-3-wind0: deployment_speed_m_s=14.689208545773218 m/s (allowed None … 10.0)
- dummy-D12-3-wind2: deployment_speed_m_s=14.820844186387468 m/s (allowed None … 10.0)
- dummy-D12-3-wind4: deployment_speed_m_s=15.198544019920847 m/s (allowed None … 10.0)
- dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-7-wind0: launch_mass_g=244.7487754861409 g (allowed None … 226.0); deployment_speed_m_s=19.43255082468205
  m/s (allowed None … 10.0)
- dummy-D12-7-wind2: launch_mass_g=244.7487754861409 g (allowed None … 226.0); deployment_speed_m_s=23.548631561847092
  m/s (allowed None … 10.0)
- dummy-D12-7-wind4: launch_mass_g=244.7487754861409 g (allowed None … 226.0); deployment_speed_m_s=25.451269115341283
  m/s (allowed None … 10.0)
- actual-C11-3-wind0: launch_mass_g=237.44877548614087 g (allowed None … 170.0); guide_departure_m_s=11.143118786216577
  m/s (allowed 12.0 … None)
- actual-C11-3-wind2: launch_mass_g=237.44877548614087 g (allowed None … 170.0); guide_departure_m_s=11.138334802910082
  m/s (allowed 12.0 … None)
- actual-C11-3-wind4: launch_mass_g=237.44877548614087 g (allowed None … 170.0); guide_departure_m_s=11.13721449094316
  m/s (allowed 12.0 … None)
- actual-C11-5-wind0: launch_mass_g=237.44877548614087 g (allowed None … 142.0); guide_departure_m_s=11.143118786216577
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.701179916815562 m/s (allowed None … 10.0)
- actual-C11-5-wind2: launch_mass_g=237.44877548614087 g (allowed None … 142.0); guide_departure_m_s=11.138334802910082
  m/s (allowed 12.0 … None); deployment_speed_m_s=18.99774023848644 m/s (allowed None … 10.0)
- actual-C11-5-wind4: launch_mass_g=237.44877548614087 g (allowed None … 142.0); guide_departure_m_s=11.13721449094316
  m/s (allowed 12.0 … None); deployment_speed_m_s=20.953577226974964 m/s (allowed None … 10.0)
- actual-D12-3-wind0: deployment_speed_m_s=14.689208545773218 m/s (allowed None … 10.0)
- actual-D12-3-wind2: deployment_speed_m_s=14.82084418638847 m/s (allowed None … 10.0)
- actual-D12-3-wind4: deployment_speed_m_s=15.19854401992091 m/s (allowed None … 10.0)
- actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-7-wind0: launch_mass_g=244.7487754861409 g (allowed None … 226.0); deployment_speed_m_s=19.432550824682057
  m/s (allowed None … 10.0)
- actual-D12-7-wind2: launch_mass_g=244.7487754861409 g (allowed None … 226.0); deployment_speed_m_s=23.548631561846253
  m/s (allowed None … 10.0)
- actual-D12-7-wind4: launch_mass_g=244.7487754861409 g (allowed None … 226.0); deployment_speed_m_s=25.4512691153414
  m/s (allowed None … 10.0)

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
