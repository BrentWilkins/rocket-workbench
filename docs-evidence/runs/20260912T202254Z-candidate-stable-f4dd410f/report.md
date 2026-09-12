# Rocket Workbench report

Run: `20260912T202254Z-candidate-stable-f4dd410f`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `25d20856fa4255e7167852be16b7bd016bc736b76574ee683c98d79163405703`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 11.88 | 8.36 | 1.73 | unavailable | 11.17 | 0.97 |
| empty-A8-3-wind2 | completed / outside configured limits | 11.73 | 8.35 | 0.82 | unavailable | 11.43 | 0.69 |
| empty-B4-4-wind0 | completed / outside configured limits | 39.05 | 10.20 | 1.70 | 11.32 | 5.20 | 1.39 |
| empty-B4-4-wind2 | completed / outside configured limits | 38.14 | 10.19 | 0.99 | 15.03 | 5.20 | 2.28 |
| empty-C6-3-wind0 | completed / outside configured limits | 121.11 | 10.86 | 1.62 | 6.91 | 5.19 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 117.60 | 10.85 | 1.20 | 8.10 | 5.19 | 18.41 |
| empty-C6-5-wind0 | completed / outside configured limits | 122.22 | 10.86 | 1.01 | 10.70 | 5.19 | 0.84 |
| empty-C6-5-wind2 | completed / outside configured limits | 118.66 | 10.85 | 1.20 | 13.58 | 5.19 | 5.74 |
| empty-C5-3-wind0 | completed / incomplete inputs | 102.36 | 14.12 | 1.62 | 1.17 | 5.20 | 0.04 |
| empty-C5-3-wind2 | completed / incomplete inputs | 100.87 | 14.11 | 1.19 | 2.81 | 5.20 | 23.86 |
| dummy-A8-3-wind0 | completed / outside configured limits | 8.73 | 7.27 | 2.31 | unavailable | 10.99 | 0.49 |
| dummy-A8-3-wind2 | completed / outside configured limits | 8.63 | 7.26 | 1.34 | unavailable | 10.79 | 0.13 |
| dummy-B4-4-wind0 | completed / outside configured limits | 29.93 | 9.01 | 2.25 | 16.00 | 5.57 | 1.21 |
| dummy-B4-4-wind2 | completed / outside configured limits | 28.98 | 9.00 | 1.59 | 19.34 | 5.51 | 9.27 |
| dummy-C6-3-wind0 | completed / outside configured limits | 101.14 | 9.73 | 2.14 | 3.78 | 5.55 | 0.04 |
| dummy-C6-3-wind2 | completed / outside configured limits | 96.93 | 9.72 | 1.69 | 6.86 | 5.55 | 4.50 |
| dummy-C6-5-wind0 | completed / outside configured limits | 101.31 | 9.73 | 2.00 | 12.23 | 5.55 | 0.43 |
| dummy-C6-5-wind2 | completed / outside configured limits | 97.08 | 9.72 | 1.69 | 16.98 | 5.55 | 11.84 |
| dummy-C5-3-wind0 | completed / incomplete inputs | 83.26 | 13.46 | 2.05 | 2.20 | 5.56 | 0.03 |
| dummy-C5-3-wind2 | completed / incomplete inputs | 81.52 | 13.45 | 1.78 | 4.05 | 5.56 | 11.87 |
| actual-A8-3-wind0 | completed / outside configured limits | 8.73 | 7.27 | 2.31 | unavailable | 10.99 | 0.49 |
| actual-A8-3-wind2 | completed / outside configured limits | 8.63 | 7.26 | 1.34 | unavailable | 10.79 | 0.13 |
| actual-B4-4-wind0 | completed / outside configured limits | 29.93 | 9.01 | 2.25 | 16.00 | 5.57 | 1.21 |
| actual-B4-4-wind2 | completed / outside configured limits | 28.98 | 9.00 | 1.59 | 19.34 | 5.51 | 9.27 |
| actual-C6-3-wind0 | completed / outside configured limits | 101.14 | 9.73 | 2.14 | 3.78 | 5.55 | 0.04 |
| actual-C6-3-wind2 | completed / outside configured limits | 96.93 | 9.72 | 1.69 | 6.86 | 5.55 | 4.50 |
| actual-C6-5-wind0 | completed / outside configured limits | 101.31 | 9.73 | 2.00 | 12.23 | 5.55 | 0.43 |
| actual-C6-5-wind2 | completed / outside configured limits | 97.08 | 9.72 | 1.69 | 16.98 | 5.55 | 11.84 |
| actual-C5-3-wind0 | completed / incomplete inputs | 83.26 | 13.46 | 2.05 | 2.20 | 5.56 | 0.03 |
| actual-C5-3-wind2 | completed / incomplete inputs | 81.52 | 13.45 | 1.78 | 4.05 | 5.56 | 11.87 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-A8-3-wind2: Large angle of attack encountered (22.4°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (16.3°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-A8-3-wind2: Large angle of attack encountered (16.3°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: no engine warnings
- actual-B4-4-wind2: no engine warnings
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
- Measured mass and balance: Nominal 381 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=127.04663094721322 g (allowed None … 85.0); apogee_m=11.88422413580308 m (allowed 30.0 … 120.0); guide_departure_m_s=8.357306598637745 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.16744750520849 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=127.04663094721322 g (allowed None … 85.0); apogee_m=11.727581173842163 m (allowed 30.0 … 120.0); guide_departure_m_s=8.348283601242853 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8212623853419848 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.426832690259422 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=129.59663094721324 g (allowed None … 99.0); guide_departure_m_s=10.203498199936671 m/s (allowed 12.0 … None); deployment_speed_m_s=11.315085671840258 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=129.59663094721324 g (allowed None … 99.0); guide_departure_m_s=10.194209130005927 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9850960729548883 cal (allowed 1.0 … None); deployment_speed_m_s=15.032761878104864 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=133.79663094721323 g (allowed None … 113.0); apogee_m=121.10601777187443 m (allowed 30.0 … 120.0); guide_departure_m_s=10.85554190894195 m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=133.79663094721323 g (allowed None … 113.0); guide_departure_m_s=10.846964207727314 m/s (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=133.79663094721323 g (allowed None … 113.0); apogee_m=122.2207268760588 m (allowed 30.0 … 120.0); guide_departure_m_s=10.85554190894195 m/s (allowed 12.0 … None); deployment_speed_m_s=10.702896195468774 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=133.79663094721323 g (allowed None … 113.0); guide_departure_m_s=10.846964207727314 m/s (allowed 12.0 … None); deployment_speed_m_s=13.575317684193278 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=145.0466309472132 g (allowed None … 85.0); apogee_m=8.72653712005462 m (allowed 30.0 … 120.0); guide_departure_m_s=7.269804613650658 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.993925802972374 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=145.0466309472132 g (allowed None … 85.0); apogee_m=8.628553923969358 m (allowed 30.0 … 120.0); guide_departure_m_s=7.261935749845939 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.786904100555926 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=147.5966309472132 g (allowed None … 99.0); apogee_m=29.933574110711003 m (allowed 30.0 … 120.0); guide_departure_m_s=9.005630830695473 m/s (allowed 12.0 … None); deployment_speed_m_s=15.995837517615469 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=147.5966309472132 g (allowed None … 99.0); apogee_m=28.982476405865185 m (allowed 30.0 … 120.0); guide_departure_m_s=8.997534380307227 m/s (allowed 12.0 … None); deployment_speed_m_s=19.338020899655472 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.72939973337637 m/s (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.721763107527972 m/s (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.72939973337637 m/s (allowed 12.0 … None); deployment_speed_m_s=12.226733527329253 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.721763107527972 m/s (allowed 12.0 … None); deployment_speed_m_s=16.983453410124156 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=145.0466309472132 g (allowed None … 85.0); apogee_m=8.72653712005462 m (allowed 30.0 … 120.0); guide_departure_m_s=7.269804613650658 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.993925802972374 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=145.0466309472132 g (allowed None … 85.0); apogee_m=8.628553923969358 m (allowed 30.0 … 120.0); guide_departure_m_s=7.261935749845939 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.786904100555926 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=147.5966309472132 g (allowed None … 99.0); apogee_m=29.933574110711003 m (allowed 30.0 … 120.0); guide_departure_m_s=9.005630830695473 m/s (allowed 12.0 … None); deployment_speed_m_s=15.995837517615474 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=147.5966309472132 g (allowed None … 99.0); apogee_m=28.982476405865174 m (allowed 30.0 … 120.0); guide_departure_m_s=8.997534380307227 m/s (allowed 12.0 … None); deployment_speed_m_s=19.33802089965545 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.72939973337637 m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.721763107527972 m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.72939973337637 m/s (allowed 12.0 … None); deployment_speed_m_s=12.226733527329253 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=151.7966309472132 g (allowed None … 113.0); guide_departure_m_s=9.721763107527972 m/s (allowed 12.0 … None); deployment_speed_m_s=16.98345341012648 m/s (allowed None … 10.0)
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
