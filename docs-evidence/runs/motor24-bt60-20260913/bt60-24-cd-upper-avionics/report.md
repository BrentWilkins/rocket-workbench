# Rocket Workbench report

Run: `bt60-24-cd-upper-avionics`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `6283812178945c30171a90f2630b7af0db3a1ddb0691d931e97dfca851053558`

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
| dummy-C11-3-wind0  | completed / outside configured limits |    69.56 |     11.85 |           1.97 |       2.57 |        5.43 |    0.02 |            9.95 |            10.95 |             35.40 |
| dummy-C11-3-wind2  | completed / outside configured limits |    68.85 |     11.85 |           1.48 |       2.83 |        5.43 |   18.17 |            9.95 |            10.95 |             35.27 |
| dummy-C11-3-wind4  | completed / outside configured limits |    67.06 |     11.84 |           1.26 |       3.42 |        5.43 |   36.84 |            9.94 |            10.94 |             34.94 |
| dummy-C11-5-wind0  | completed / outside configured limits |    69.60 |     11.85 |           1.80 |      12.99 |        5.43 |    0.85 |            9.95 |            10.95 |             35.40 |
| dummy-C11-5-wind2  | completed / outside configured limits |    68.92 |     11.85 |           1.08 |      14.44 |        5.43 |   10.01 |            9.95 |            10.95 |             35.27 |
| dummy-C11-5-wind4  | completed / outside configured limits |    67.12 |     11.84 |           1.26 |      16.99 |        5.43 |   19.20 |            9.94 |            10.94 |             34.94 |
| dummy-D12-3-wind0  | completed / outside configured limits |   175.02 |     12.90 |           1.84 |      18.76 |        5.41 |    0.05 |           13.47 |            14.47 |             60.58 |
| dummy-D12-3-wind2  | completed / outside configured limits |   173.54 |     12.89 |           1.42 |      18.74 |        5.41 |   47.37 |           13.47 |            14.47 |             60.44 |
| dummy-D12-3-wind4  | completed / outside configured limits |   169.59 |     12.89 |           1.15 |      18.71 |        5.41 |   93.77 |           13.46 |            14.46 |             60.04 |
| dummy-D12-5-wind0  | completed / incomplete inputs         |   188.58 |     12.90 |           1.64 |       1.39 |        5.41 |    0.09 |           13.47 |            14.47 |             60.58 |
| dummy-D12-5-wind2  | completed / incomplete inputs         |   186.72 |     12.89 |           1.30 |       3.23 |        5.41 |   44.26 |           13.47 |            14.47 |             60.44 |
| dummy-D12-5-wind4  | completed / incomplete inputs         |   181.57 |     12.89 |           1.15 |       6.21 |        5.41 |   87.74 |           13.46 |            14.46 |             60.04 |
| dummy-D12-7-wind0  | completed / outside configured limits |   188.58 |     12.90 |           1.64 |      15.78 |        5.41 |    0.23 |           13.47 |            14.47 |             60.58 |
| dummy-D12-7-wind2  | completed / outside configured limits |   186.72 |     12.89 |           1.30 |      19.48 |        5.41 |   31.57 |           13.47 |            14.47 |             60.44 |
| dummy-D12-7-wind4  | completed / outside configured limits |   181.57 |     12.89 |           1.15 |      21.62 |        5.41 |   58.72 |           13.46 |            14.46 |             60.04 |
| actual-C11-3-wind0 | completed / outside configured limits |    69.56 |     11.85 |           1.97 |       2.57 |        5.43 |    0.02 |            9.95 |            10.95 |             35.40 |
| actual-C11-3-wind2 | completed / outside configured limits |    68.85 |     11.85 |           1.48 |       2.83 |        5.43 |   18.17 |            9.95 |            10.95 |             35.27 |
| actual-C11-3-wind4 | completed / outside configured limits |    67.06 |     11.84 |           1.26 |       3.42 |        5.43 |   36.84 |            9.94 |            10.94 |             34.94 |
| actual-C11-5-wind0 | completed / outside configured limits |    69.60 |     11.85 |           1.80 |      12.99 |        5.43 |    0.85 |            9.95 |            10.95 |             35.40 |
| actual-C11-5-wind2 | completed / outside configured limits |    68.92 |     11.85 |           1.08 |      14.44 |        5.43 |   10.01 |            9.95 |            10.95 |             35.27 |
| actual-C11-5-wind4 | completed / outside configured limits |    67.12 |     11.84 |           1.26 |      16.99 |        5.43 |   19.20 |            9.94 |            10.94 |             34.94 |
| actual-D12-3-wind0 | completed / outside configured limits |   175.02 |     12.90 |           1.84 |      18.76 |        5.41 |    0.05 |           13.47 |            14.47 |             60.58 |
| actual-D12-3-wind2 | completed / outside configured limits |   173.54 |     12.89 |           1.42 |      18.74 |        5.41 |   47.37 |           13.47 |            14.47 |             60.44 |
| actual-D12-3-wind4 | completed / outside configured limits |   169.59 |     12.89 |           1.15 |      18.71 |        5.41 |   93.77 |           13.46 |            14.46 |             60.04 |
| actual-D12-5-wind0 | completed / incomplete inputs         |   188.58 |     12.90 |           1.64 |       1.39 |        5.41 |    0.09 |           13.47 |            14.47 |             60.58 |
| actual-D12-5-wind2 | completed / incomplete inputs         |   186.72 |     12.89 |           1.30 |       3.23 |        5.41 |   44.26 |           13.47 |            14.47 |             60.44 |
| actual-D12-5-wind4 | completed / incomplete inputs         |   181.57 |     12.89 |           1.15 |       6.21 |        5.41 |   87.74 |           13.46 |            14.46 |             60.04 |
| actual-D12-7-wind0 | completed / outside configured limits |   188.58 |     12.90 |           1.64 |      15.78 |        5.41 |    0.23 |           13.47 |            14.47 |             60.58 |
| actual-D12-7-wind2 | completed / outside configured limits |   186.72 |     12.89 |           1.30 |      19.48 |        5.41 |   31.57 |           13.47 |            14.47 |             60.44 |
| actual-D12-7-wind4 | completed / outside configured limits |   181.57 |     12.89 |           1.15 |      21.62 |        5.41 |   58.72 |           13.46 |            14.46 |             60.04 |

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
- dummy-C11-5-wind4: no engine warnings
- dummy-D12-3-wind0: no engine warnings
- dummy-D12-3-wind2: no engine warnings
- dummy-D12-3-wind4: no engine warnings
- dummy-D12-5-wind0: no engine warnings
- dummy-D12-5-wind2: no engine warnings
- dummy-D12-5-wind4: no engine warnings
- dummy-D12-7-wind0: no engine warnings
- dummy-D12-7-wind2: no engine warnings
- dummy-D12-7-wind4: Recovery device deployment at high speed (21.6 m/s): "Nominal 457 mm parachute and lines"
- actual-C11-3-wind0: no engine warnings
- actual-C11-3-wind2: no engine warnings
- actual-C11-3-wind4: no engine warnings
- actual-C11-5-wind0: no engine warnings
- actual-C11-5-wind2: no engine warnings
- actual-C11-5-wind4: no engine warnings
- actual-D12-3-wind0: no engine warnings
- actual-D12-3-wind2: no engine warnings
- actual-D12-3-wind4: no engine warnings
- actual-D12-5-wind0: no engine warnings
- actual-D12-5-wind2: no engine warnings
- actual-D12-5-wind4: no engine warnings
- actual-D12-7-wind0: no engine warnings
- actual-D12-7-wind2: no engine warnings
- actual-D12-7-wind4: Recovery device deployment at high speed (21.6 m/s): "Nominal 457 mm parachute and lines"

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
  minimum_ascent_stability_cal=0.872524529270104 cal (allowed 1.0 … None)
- empty-C11-3-wind4: launch_mass_g=176.7987754861409 g (allowed None … 170.0);
  minimum_ascent_stability_cal=0.6088368987618832 cal (allowed 1.0 … None)
- empty-C11-5-wind0: launch_mass_g=176.7987754861409 g (allowed None … 142.0);
  minimum_ascent_stability_cal=0.5246398166729479 cal (allowed 1.0 … None); deployment_speed_m_s=11.769103224595435 m/s
  (allowed None … 10.0)
- empty-C11-5-wind2: launch_mass_g=176.7987754861409 g (allowed None … 142.0);
  minimum_ascent_stability_cal=0.416240579604943 cal (allowed 1.0 … None); deployment_speed_m_s=11.223977271334377 m/s
  (allowed None … 10.0)
- empty-C11-5-wind4: launch_mass_g=176.7987754861409 g (allowed None … 142.0);
  minimum_ascent_stability_cal=0.6088368987618832 cal (allowed 1.0 … None); deployment_speed_m_s=12.395605363866029 m/s
  (allowed None … 10.0)
- empty-D12-3-wind0: deployment_speed_m_s=21.953560020180202 m/s (allowed None … 10.0)
- empty-D12-3-wind2: minimum_ascent_stability_cal=0.7696940909901994 cal (allowed 1.0 … None);
  deployment_speed_m_s=21.873566384507868 m/s (allowed None … 10.0)
- empty-D12-3-wind4: minimum_ascent_stability_cal=0.5133969559955419 cal (allowed 1.0 … None);
  deployment_speed_m_s=21.64027960989945 m/s (allowed None … 10.0)
- empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-D12-5-wind2: minimum_ascent_stability_cal=0.6501936367239458 cal (allowed 1.0 … None)
- empty-D12-5-wind4: minimum_ascent_stability_cal=0.5133969559955419 cal (allowed 1.0 … None)
- empty-D12-7-wind0: minimum_ascent_stability_cal=0.9405897328603453 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.212988032012923 m/s (allowed None … 10.0)
- empty-D12-7-wind2: minimum_ascent_stability_cal=0.48392755547459465 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.036727874890811 m/s (allowed None … 10.0)
- empty-D12-7-wind4: minimum_ascent_stability_cal=0.5133969559955419 cal (allowed 1.0 … None);
  deployment_speed_m_s=18.222997705191403 m/s (allowed None … 10.0)
- dummy-C11-3-wind0: launch_mass_g=205.99877548614091 g (allowed None … 170.0); guide_departure_m_s=11.851016279918268
  m/s (allowed 12.0 … None)
- dummy-C11-3-wind2: launch_mass_g=205.99877548614091 g (allowed None … 170.0); guide_departure_m_s=11.845441181702606
  m/s (allowed 12.0 … None)
- dummy-C11-3-wind4: launch_mass_g=205.99877548614091 g (allowed None … 170.0); guide_departure_m_s=11.843736758342146
  m/s (allowed 12.0 … None)
- dummy-C11-5-wind0: launch_mass_g=205.99877548614091 g (allowed None … 142.0); guide_departure_m_s=11.851016279918268
  m/s (allowed 12.0 … None); deployment_speed_m_s=12.99409864656935 m/s (allowed None … 10.0)
- dummy-C11-5-wind2: launch_mass_g=205.99877548614091 g (allowed None … 142.0); guide_departure_m_s=11.845441181702606
  m/s (allowed 12.0 … None); deployment_speed_m_s=14.443933282600847 m/s (allowed None … 10.0)
- dummy-C11-5-wind4: launch_mass_g=205.99877548614091 g (allowed None … 142.0); guide_departure_m_s=11.843736758342146
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.98876689020952 m/s (allowed None … 10.0)
- dummy-D12-3-wind0: deployment_speed_m_s=18.758213043792935 m/s (allowed None … 10.0)
- dummy-D12-3-wind2: deployment_speed_m_s=18.744959765626767 m/s (allowed None … 10.0)
- dummy-D12-3-wind4: deployment_speed_m_s=18.70549421148378 m/s (allowed None … 10.0)
- dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-7-wind0: deployment_speed_m_s=15.779284530621307 m/s (allowed None … 10.0)
- dummy-D12-7-wind2: deployment_speed_m_s=19.475300822693665 m/s (allowed None … 10.0)
- dummy-D12-7-wind4: deployment_speed_m_s=21.616330619982794 m/s (allowed None … 10.0)
- actual-C11-3-wind0: launch_mass_g=205.99877548614091 g (allowed None … 170.0); guide_departure_m_s=11.851016279918268
  m/s (allowed 12.0 … None)
- actual-C11-3-wind2: launch_mass_g=205.99877548614091 g (allowed None … 170.0); guide_departure_m_s=11.845441181702606
  m/s (allowed 12.0 … None)
- actual-C11-3-wind4: launch_mass_g=205.99877548614091 g (allowed None … 170.0); guide_departure_m_s=11.843736758342146
  m/s (allowed 12.0 … None)
- actual-C11-5-wind0: launch_mass_g=205.99877548614091 g (allowed None … 142.0); guide_departure_m_s=11.851016279918268
  m/s (allowed 12.0 … None); deployment_speed_m_s=12.99409864656935 m/s (allowed None … 10.0)
- actual-C11-5-wind2: launch_mass_g=205.99877548614091 g (allowed None … 142.0); guide_departure_m_s=11.845441181702606
  m/s (allowed 12.0 … None); deployment_speed_m_s=14.443933282600847 m/s (allowed None … 10.0)
- actual-C11-5-wind4: launch_mass_g=205.99877548614091 g (allowed None … 142.0); guide_departure_m_s=11.843736758342146
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.98876689020952 m/s (allowed None … 10.0)
- actual-D12-3-wind0: deployment_speed_m_s=18.758213043792935 m/s (allowed None … 10.0)
- actual-D12-3-wind2: deployment_speed_m_s=18.744959765626767 m/s (allowed None … 10.0)
- actual-D12-3-wind4: deployment_speed_m_s=18.70549421148378 m/s (allowed None … 10.0)
- actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-7-wind0: deployment_speed_m_s=15.779284530621307 m/s (allowed None … 10.0)
- actual-D12-7-wind2: deployment_speed_m_s=19.475300822693665 m/s (allowed None … 10.0)
- actual-D12-7-wind4: deployment_speed_m_s=21.616330619982794 m/s (allowed None … 10.0)

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
