# Rocket Workbench report

Run: `design-013`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `9f71a52089ab53b106660a84017adc0967c8abb3d4c31e40046f28c748f10ad0`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 13.51 | 8.83 | 0.90 | 13.54 | 12.29 | 1.37 |
| empty-A8-3-wind2 | completed / outside configured limits | 13.36 | 8.82 | 0.33 | unavailable | 13.82 | 1.07 |
| empty-B4-4-wind0 | completed / outside configured limits | 43.95 | 10.71 | 0.85 | 12.85 | 5.05 | 1.74 |
| empty-B4-4-wind2 | completed / outside configured limits | 43.07 | 10.70 | 0.38 | 13.26 | 5.05 | 2.95 |
| empty-C6-3-wind0 | completed / outside configured limits | 133.14 | 11.34 | 0.80 | 9.20 | 5.04 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 130.14 | 11.33 | 0.54 | 9.84 | 5.04 | 26.82 |
| empty-C6-5-wind0 | completed / outside configured limits | 135.64 | 11.34 | 0.77 | 9.89 | 5.04 | 0.36 |
| empty-C6-5-wind2 | completed / outside configured limits | 132.48 | 11.33 | 0.54 | 11.25 | 5.04 | 16.22 |
| dummy-A8-3-wind0 | completed / outside configured limits | 9.80 | 7.66 | 1.34 | unavailable | 11.53 | 0.53 |
| dummy-A8-3-wind2 | completed / outside configured limits | 9.70 | 7.65 | 0.74 | unavailable | 11.64 | 0.17 |
| dummy-B4-4-wind0 | completed / outside configured limits | 33.39 | 9.41 | 1.19 | 12.53 | 5.43 | 0.65 |
| dummy-B4-4-wind2 | completed / outside configured limits | 32.43 | 9.41 | 0.85 | 17.94 | 5.43 | 7.20 |
| dummy-C6-3-wind0 | completed / outside configured limits | 111.37 | 10.17 | 1.21 | 5.87 | 5.42 | 0.05 |
| dummy-C6-3-wind2 | completed / outside configured limits | 107.42 | 10.16 | 0.92 | 7.84 | 5.42 | 10.33 |
| dummy-C6-5-wind0 | completed / outside configured limits | 112.03 | 10.17 | 1.15 | 11.38 | 5.42 | 0.71 |
| dummy-C6-5-wind2 | completed / outside configured limits | 108.04 | 10.16 | 0.92 | 15.11 | 5.42 | 4.58 |
| actual-A8-3-wind0 | completed / outside configured limits | 9.80 | 7.66 | 1.34 | unavailable | 11.53 | 0.53 |
| actual-A8-3-wind2 | completed / outside configured limits | 9.70 | 7.65 | 0.74 | unavailable | 11.64 | 0.17 |
| actual-B4-4-wind0 | completed / outside configured limits | 33.39 | 9.41 | 1.19 | 12.53 | 5.43 | 0.65 |
| actual-B4-4-wind2 | completed / outside configured limits | 32.43 | 9.41 | 0.85 | 17.94 | 5.43 | 7.20 |
| actual-C6-3-wind0 | completed / outside configured limits | 111.37 | 10.17 | 1.21 | 5.87 | 5.42 | 0.05 |
| actual-C6-3-wind2 | completed / outside configured limits | 107.42 | 10.16 | 0.92 | 7.84 | 5.42 | 10.33 |
| actual-C6-5-wind0 | completed / outside configured limits | 112.03 | 10.17 | 1.15 | 11.38 | 5.42 | 0.71 |
| actual-C6-5-wind2 | completed / outside configured limits | 108.04 | 10.16 | 0.92 | 15.11 | 5.42 | 4.58 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: no engine warnings
- empty-A8-3-wind2: Large angle of attack encountered (21.8°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (17.2°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-A8-3-wind2: Large angle of attack encountered (17.2°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: no engine warnings
- actual-B4-4-wind2: no engine warnings
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: no engine warnings

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

- empty-A8-3-wind0: launch_mass_g=120.27898925783664 g (allowed None … 85.0); apogee_m=13.51404451801031 m (allowed 30.0 … 120.0); guide_departure_m_s=8.827186461188829 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8980615532395686 cal (allowed 1.0 … None); deployment_speed_m_s=13.544611143808089 m/s (allowed None … 10.0); landing_descent_m_s=12.290124166796227 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=120.27898925783664 g (allowed None … 85.0); apogee_m=13.360623636900575 m (allowed 30.0 … 120.0); guide_departure_m_s=8.818747937059031 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.3297018770709555 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=13.820753729839318 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=122.82898925783664 g (allowed None … 99.0); guide_departure_m_s=10.70976062077542 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8509832041520772 cal (allowed 1.0 … None); deployment_speed_m_s=12.845643855343468 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=122.82898925783664 g (allowed None … 99.0); guide_departure_m_s=10.701162111153085 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.3825242701681691 cal (allowed 1.0 … None); deployment_speed_m_s=13.260599846882561 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=127.02898925783666 g (allowed None … 113.0); apogee_m=133.14439251339368 m (allowed 30.0 … 120.0); guide_departure_m_s=11.3408502190861 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7985714648151577 cal (allowed 1.0 … None)
- empty-C6-3-wind2: launch_mass_g=127.02898925783666 g (allowed None … 113.0); apogee_m=130.13944079410282 m (allowed 30.0 … 120.0); guide_departure_m_s=11.33290893185162 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5365074001481289 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=127.02898925783666 g (allowed None … 113.0); apogee_m=135.6375971377994 m (allowed 30.0 … 120.0); guide_departure_m_s=11.3408502190861 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7677163862819552 cal (allowed 1.0 … None)
- empty-C6-5-wind2: launch_mass_g=127.02898925783666 g (allowed None … 113.0); apogee_m=132.48319830808666 m (allowed 30.0 … 120.0); guide_departure_m_s=11.33290893185162 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5365074001481289 cal (allowed 1.0 … None); deployment_speed_m_s=11.250256946341512 m/s (allowed None … 10.0)
- dummy-A8-3-wind0: launch_mass_g=138.27898925783663 g (allowed None … 85.0); apogee_m=9.804804915458428 m (allowed 30.0 … 120.0); guide_departure_m_s=7.660033820129566 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.528200883590127 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=138.27898925783663 g (allowed None … 85.0); apogee_m=9.69945178601021 m (allowed 30.0 … 120.0); guide_departure_m_s=7.652637515360459 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7408126332902086 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.643347915796356 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=140.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.413458132988046 m/s (allowed 12.0 … None); deployment_speed_m_s=12.526447025653566 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=140.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.405974933272491 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8496640702920103 cal (allowed 1.0 … None); deployment_speed_m_s=17.940991851862584 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.168404853476348 m/s (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.161239563455197 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9245792305925161 cal (allowed 1.0 … None)
- dummy-C6-5-wind0: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.168404853476348 m/s (allowed 12.0 … None); deployment_speed_m_s=11.383632173027848 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.161239563455197 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9245792305925161 cal (allowed 1.0 … None); deployment_speed_m_s=15.105794352423285 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=138.27898925783663 g (allowed None … 85.0); apogee_m=9.804804915458428 m (allowed 30.0 … 120.0); guide_departure_m_s=7.660033820129566 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.528200883590127 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=138.27898925783663 g (allowed None … 85.0); apogee_m=9.69945178601021 m (allowed 30.0 … 120.0); guide_departure_m_s=7.652637515360459 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7408126332902086 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.643347915796356 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=140.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.413458132988046 m/s (allowed 12.0 … None); deployment_speed_m_s=12.526447025653571 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=140.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.405974933272491 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8496640702920271 cal (allowed 1.0 … None); deployment_speed_m_s=17.94099185186265 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.168404853476348 m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.161239563455197 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9245792305925161 cal (allowed 1.0 … None)
- actual-C6-5-wind0: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.168404853476348 m/s (allowed 12.0 … None); deployment_speed_m_s=11.38363217302403 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=145.02898925783663 g (allowed None … 113.0); guide_departure_m_s=10.161239563455197 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9245792305925161 cal (allowed 1.0 … None); deployment_speed_m_s=15.105794352423263 m/s (allowed None … 10.0)

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
