# Rocket Workbench report

Run: `20260912T192553Z-candidate-recovery-7f53a228`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `ffc49cba86df36e14ad63fe0a0ef534a1c5d25b3865b1a6a8f1167534269bb4f`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 11.05 | 8.08 | 1.79 | unavailable | 11.18 | 0.86 |
| empty-A8-3-wind2 | completed / outside configured limits | 10.91 | 8.07 | 0.83 | unavailable | 11.35 | 0.56 |
| empty-B4-4-wind0 | completed / outside configured limits | 36.72 | 9.88 | 1.43 | 11.46 | 4.41 | 1.36 |
| empty-B4-4-wind2 | completed / outside configured limits | 35.80 | 9.87 | 0.97 | 15.60 | 4.41 | 2.07 |
| empty-C6-3-wind0 | completed / outside configured limits | 116.25 | 10.60 | 1.63 | 6.23 | 4.40 | 0.04 |
| empty-C6-3-wind2 | completed / outside configured limits | 112.67 | 10.60 | 1.20 | 7.70 | 4.40 | 24.50 |
| empty-C6-5-wind0 | completed / outside configured limits | 117.22 | 10.60 | 1.22 | 10.90 | 4.40 | 0.82 |
| empty-C6-5-wind2 | completed / outside configured limits | 113.57 | 10.60 | 1.20 | 14.29 | 4.40 | 10.19 |
| empty-C5-3-wind0 | completed / incomplete inputs | 97.72 | 13.92 | 1.64 | 0.41 | 4.40 | 0.04 |
| empty-C5-3-wind2 | completed / incomplete inputs | 96.19 | 13.91 | 1.15 | 2.78 | 4.40 | 28.69 |
| dummy-A8-3-wind0 | completed / outside configured limits | 8.16 | 7.04 | 2.30 | unavailable | 10.89 | 0.44 |
| dummy-A8-3-wind2 | completed / outside configured limits | 8.08 | 7.03 | 1.34 | unavailable | 10.63 | 0.11 |
| dummy-B4-4-wind0 | completed / outside configured limits | 28.22 | 8.78 | 2.12 | 16.63 | 4.71 | 1.13 |
| dummy-B4-4-wind2 | completed / outside configured limits | 27.28 | 8.77 | 1.62 | 20.01 | 4.68 | 9.85 |
| dummy-C6-3-wind0 | completed / outside configured limits | 96.82 | 9.52 | 2.14 | 3.04 | 4.70 | 0.04 |
| dummy-C6-3-wind2 | completed / outside configured limits | 92.56 | 9.52 | 1.67 | 6.71 | 4.70 | 9.52 |
| dummy-C6-5-wind0 | completed / outside configured limits | 96.92 | 9.52 | 1.50 | 12.93 | 4.70 | 0.39 |
| dummy-C6-5-wind2 | completed / outside configured limits | 92.64 | 9.52 | 1.67 | 17.71 | 4.70 | 8.87 |
| dummy-C5-3-wind0 | completed / incomplete inputs | 79.36 | 13.54 | 2.06 | 2.98 | 4.70 | 0.03 |
| dummy-C5-3-wind2 | completed / incomplete inputs | 77.59 | 13.53 | 1.78 | 4.61 | 4.70 | 15.65 |
| actual-A8-3-wind0 | completed / outside configured limits | 8.16 | 7.04 | 2.30 | unavailable | 10.89 | 0.44 |
| actual-A8-3-wind2 | completed / outside configured limits | 8.08 | 7.03 | 1.34 | unavailable | 10.63 | 0.11 |
| actual-B4-4-wind0 | completed / outside configured limits | 28.22 | 8.78 | 2.12 | 16.63 | 4.71 | 1.13 |
| actual-B4-4-wind2 | completed / outside configured limits | 27.28 | 8.77 | 1.62 | 20.01 | 4.68 | 9.85 |
| actual-C6-3-wind0 | completed / outside configured limits | 96.82 | 9.52 | 2.14 | 3.04 | 4.70 | 0.04 |
| actual-C6-3-wind2 | completed / outside configured limits | 92.56 | 9.52 | 1.67 | 6.71 | 4.70 | 9.52 |
| actual-C6-5-wind0 | completed / outside configured limits | 96.92 | 9.52 | 1.50 | 12.93 | 4.70 | 0.39 |
| actual-C6-5-wind2 | completed / outside configured limits | 92.64 | 9.52 | 1.67 | 17.71 | 4.70 | 8.87 |
| actual-C5-3-wind0 | completed / incomplete inputs | 79.36 | 13.54 | 2.06 | 2.98 | 4.70 | 0.03 |
| actual-C5-3-wind2 | completed / incomplete inputs | 77.59 | 13.53 | 1.78 | 4.61 | 4.70 | 15.65 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-A8-3-wind2: Large angle of attack encountered (21°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: Recovery device deployment at high speed (20 m/s):  "Nominal 457 mm parachute and lines"
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: no engine warnings
- actual-B4-4-wind2: Recovery device deployment at high speed (20 m/s):  "Nominal 457 mm parachute and lines"
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: no engine warnings
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings

## Missing measurements / physical checks

- Exact XIAO board/camera/antenna identity and measured envelope
- Battery identity, connector/wire envelopes and retention measurements
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

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=131.15442992598236 g (allowed None … 85.0); apogee_m=11.049973547422695 m (allowed 30.0 … 120.0); guide_departure_m_s=8.075275768666675 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.1767512839107 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=131.15442992598236 g (allowed None … 85.0); apogee_m=10.909237186802905 m (allowed 30.0 … 120.0); guide_departure_m_s=8.066550946699374 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8284993943476885 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.351272541108685 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=133.70442992598237 g (allowed None … 99.0); guide_departure_m_s=9.877725718165646 m/s (allowed 12.0 … None); deployment_speed_m_s=11.46462652893735 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=133.70442992598237 g (allowed None … 99.0); guide_departure_m_s=9.868848679630979 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9702237188156377 cal (allowed 1.0 … None); deployment_speed_m_s=15.597888064886012 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=137.90442992598236 g (allowed None … 113.0); guide_departure_m_s=10.604715676590803 m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=137.90442992598236 g (allowed None … 113.0); guide_departure_m_s=10.596281814064993 m/s (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=137.90442992598236 g (allowed None … 113.0); guide_departure_m_s=10.604715676590803 m/s (allowed 12.0 … None); deployment_speed_m_s=10.90022866584811 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=137.90442992598236 g (allowed None … 113.0); guide_departure_m_s=10.596281814064993 m/s (allowed 12.0 … None); deployment_speed_m_s=14.28945509970674 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=149.15442992598236 g (allowed None … 85.0); apogee_m=8.160892667786667 m (allowed 30.0 … 120.0); guide_departure_m_s=7.038293073133446 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.887578428533354 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=149.15442992598236 g (allowed None … 85.0); apogee_m=8.07982143012499 m (allowed 30.0 … 120.0); guide_departure_m_s=7.030776909286571 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.634894170108785 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=151.70442992598234 g (allowed None … 99.0); apogee_m=28.216605215332844 m (allowed 30.0 … 120.0); guide_departure_m_s=8.779395801025897 m/s (allowed 12.0 … None); deployment_speed_m_s=16.629913907686557 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=151.70442992598234 g (allowed None … 99.0); apogee_m=27.28120702416898 m (allowed 30.0 … 120.0); guide_departure_m_s=8.771480288227597 m/s (allowed 12.0 … None); deployment_speed_m_s=20.01441171543533 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.524665828531809 m/s (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.51715457124424 m/s (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.524665828531809 m/s (allowed 12.0 … None); deployment_speed_m_s=12.932800337845451 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.51715457124424 m/s (allowed 12.0 … None); deployment_speed_m_s=17.709238141820634 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=149.15442992598236 g (allowed None … 85.0); apogee_m=8.160892667786667 m (allowed 30.0 … 120.0); guide_departure_m_s=7.038293073133446 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.887578428533352 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=149.15442992598236 g (allowed None … 85.0); apogee_m=8.07982143012499 m (allowed 30.0 … 120.0); guide_departure_m_s=7.030776909286571 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.634894170108785 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=151.70442992598234 g (allowed None … 99.0); apogee_m=28.216605215332844 m (allowed 30.0 … 120.0); guide_departure_m_s=8.779395801025897 m/s (allowed 12.0 … None); deployment_speed_m_s=16.62991390768654 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=151.70442992598234 g (allowed None … 99.0); apogee_m=27.28120702416897 m (allowed 30.0 … 120.0); guide_departure_m_s=8.771480288227597 m/s (allowed 12.0 … None); deployment_speed_m_s=20.0144117154353 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.524665828531809 m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.51715457124424 m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.524665828531809 m/s (allowed 12.0 … None); deployment_speed_m_s=12.932800337845448 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=155.90442992598236 g (allowed None … 113.0); guide_departure_m_s=9.51715457124424 m/s (allowed 12.0 … None); deployment_speed_m_s=17.709238141820585 m/s (allowed None … 10.0)
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
