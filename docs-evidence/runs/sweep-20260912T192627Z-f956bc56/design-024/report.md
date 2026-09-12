# Rocket Workbench report

Run: `design-024`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `72b22f60c7490fcfc799c44a1c458f71fdd1f66d9d4e805ecd7cc28307011e88`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 13.11 | 8.73 | 1.46 | 11.43 | 11.07 | 1.17 |
| empty-A8-3-wind2 | completed / outside configured limits | 12.93 | 8.72 | 0.67 | 12.73 | 12.07 | 0.70 |
| empty-B4-4-wind0 | completed / outside configured limits | 42.48 | 10.56 | 1.28 | 11.28 | 6.35 | 1.61 |
| empty-B4-4-wind2 | completed / outside configured limits | 41.52 | 10.55 | 0.81 | 13.04 | 6.35 | 3.58 |
| empty-C6-3-wind0 | completed / outside configured limits | 128.41 | 11.25 | 1.31 | 7.98 | 6.34 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 124.93 | 11.24 | 0.98 | 8.90 | 6.34 | 11.63 |
| empty-C6-5-wind0 | completed / outside configured limits | 129.79 | 11.25 | 1.23 | 10.28 | 6.34 | 0.79 |
| empty-C6-5-wind2 | completed / outside configured limits | 126.26 | 11.24 | 0.98 | 12.62 | 6.34 | 0.54 |
| dummy-A8-3-wind0 | completed / outside configured limits | 9.55 | 7.56 | 1.94 | unavailable | 11.35 | 0.52 |
| dummy-A8-3-wind2 | completed / outside configured limits | 9.42 | 7.55 | 1.15 | unavailable | 11.09 | 0.33 |
| dummy-B4-4-wind0 | completed / outside configured limits | 32.43 | 9.34 | 1.79 | 15.36 | 6.82 | 1.13 |
| dummy-B4-4-wind2 | completed / outside configured limits | 31.44 | 9.33 | 1.36 | 18.66 | 6.82 | 9.19 |
| dummy-C6-3-wind0 | completed / outside configured limits | 107.55 | 10.05 | 1.79 | 4.90 | 6.80 | 0.05 |
| dummy-C6-3-wind2 | completed / outside configured limits | 103.25 | 10.04 | 1.43 | 7.39 | 6.80 | 1.66 |
| dummy-C6-5-wind0 | completed / outside configured limits | 107.83 | 10.05 | 1.77 | 11.56 | 6.80 | 0.52 |
| dummy-C6-5-wind2 | completed / outside configured limits | 103.53 | 10.04 | 1.43 | 16.04 | 6.80 | 16.08 |
| actual-A8-3-wind0 | completed / outside configured limits | 9.55 | 7.56 | 1.94 | unavailable | 11.35 | 0.52 |
| actual-A8-3-wind2 | completed / outside configured limits | 9.42 | 7.55 | 1.15 | unavailable | 11.09 | 0.33 |
| actual-B4-4-wind0 | completed / outside configured limits | 32.43 | 9.34 | 1.79 | 15.36 | 6.82 | 1.13 |
| actual-B4-4-wind2 | completed / outside configured limits | 31.44 | 9.33 | 1.36 | 18.66 | 6.82 | 9.19 |
| actual-C6-3-wind0 | completed / outside configured limits | 107.55 | 10.05 | 1.79 | 4.90 | 6.80 | 0.05 |
| actual-C6-3-wind2 | completed / outside configured limits | 103.25 | 10.04 | 1.43 | 7.39 | 6.80 | 1.66 |
| actual-C6-5-wind0 | completed / outside configured limits | 107.83 | 10.05 | 1.77 | 11.56 | 6.80 | 0.52 |
| actual-C6-5-wind2 | completed / outside configured limits | 103.53 | 10.04 | 1.43 | 16.04 | 6.80 | 16.08 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: no engine warnings
- empty-A8-3-wind2: Large angle of attack encountered (20°)
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (21°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-A8-3-wind2: Large angle of attack encountered (21°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
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
- Measured mass and balance: Nominal 305 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=121.68392199800591 g (allowed None … 85.0); apogee_m=13.111097896512689 m (allowed 30.0 … 120.0); guide_departure_m_s=8.728761958853513 m/s (allowed 12.0 … None); deployment_speed_m_s=11.429182528270298 m/s (allowed None … 10.0); landing_descent_m_s=11.070755310966899 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=121.68392199800591 g (allowed None … 85.0); apogee_m=12.927315207113788 m (allowed 30.0 … 120.0); guide_departure_m_s=8.719505534245144 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6731520056054863 cal (allowed 1.0 … None); deployment_speed_m_s=12.72942496510848 m/s (allowed None … 10.0); landing_descent_m_s=12.069168428401547 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=124.23392199800591 g (allowed None … 99.0); guide_departure_m_s=10.563421537509658 m/s (allowed 12.0 … None); deployment_speed_m_s=11.283901335836015 m/s (allowed None … 10.0); landing_descent_m_s=6.3525294301519635 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=124.23392199800591 g (allowed None … 99.0); guide_departure_m_s=10.554155079138276 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8055338053149097 cal (allowed 1.0 … None); deployment_speed_m_s=13.036125466994118 m/s (allowed None … 10.0); landing_descent_m_s=6.352456990628609 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=128.4339219980059 g (allowed None … 113.0); apogee_m=128.40939953242446 m (allowed 30.0 … 120.0); guide_departure_m_s=11.248286210636286 m/s (allowed 12.0 … None); landing_descent_m_s=6.336387160062263 m/s (allowed None … 6.0)
- empty-C6-3-wind2: launch_mass_g=128.4339219980059 g (allowed None … 113.0); apogee_m=124.92570608838648 m (allowed 30.0 … 120.0); guide_departure_m_s=11.239564609352003 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9815687946609812 cal (allowed 1.0 … None); landing_descent_m_s=6.336314816660561 m/s (allowed None … 6.0)
- empty-C6-5-wind0: launch_mass_g=128.4339219980059 g (allowed None … 113.0); apogee_m=129.78696263446315 m (allowed 30.0 … 120.0); guide_departure_m_s=11.248286210636286 m/s (allowed 12.0 … None); deployment_speed_m_s=10.281073890175163 m/s (allowed None … 10.0); landing_descent_m_s=6.336387167347037 m/s (allowed None … 6.0)
- empty-C6-5-wind2: launch_mass_g=128.4339219980059 g (allowed None … 113.0); apogee_m=126.25607160161118 m (allowed 30.0 … 120.0); guide_departure_m_s=11.239564609352003 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9815687946609812 cal (allowed 1.0 … None); deployment_speed_m_s=12.617773770649098 m/s (allowed None … 10.0); landing_descent_m_s=6.3363149032037205 m/s (allowed None … 6.0)
- dummy-A8-3-wind0: launch_mass_g=139.6839219980059 g (allowed None … 85.0); apogee_m=9.548242055916061 m (allowed 30.0 … 120.0); guide_departure_m_s=7.555020811846815 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.3469238066729 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=139.6839219980059 g (allowed None … 85.0); apogee_m=9.416316946516027 m (allowed 30.0 … 120.0); guide_departure_m_s=7.547094070130438 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.085175353502123 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=142.23392199800588 g (allowed None … 99.0); guide_departure_m_s=9.341052038717686 m/s (allowed 12.0 … None); deployment_speed_m_s=15.358407781395805 m/s (allowed None … 10.0); landing_descent_m_s=6.819017456447315 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=142.23392199800588 g (allowed None … 99.0); guide_departure_m_s=9.332793007811778 m/s (allowed 12.0 … None); deployment_speed_m_s=18.661267540854634 m/s (allowed None … 10.0); landing_descent_m_s=6.816189840747177 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.047053382714644 m/s (allowed 12.0 … None); landing_descent_m_s=6.804029879880361 m/s (allowed None … 6.0)
- dummy-C6-3-wind2: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.039312659766379 m/s (allowed 12.0 … None); landing_descent_m_s=6.803952270962378 m/s (allowed None … 6.0)
- dummy-C6-5-wind0: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.047053382714644 m/s (allowed 12.0 … None); deployment_speed_m_s=11.56415939172971 m/s (allowed None … 10.0); landing_descent_m_s=6.804029936884105 m/s (allowed None … 6.0)
- dummy-C6-5-wind2: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.039312659766379 m/s (allowed 12.0 … None); deployment_speed_m_s=16.038044327305332 m/s (allowed None … 10.0); landing_descent_m_s=6.803952290630037 m/s (allowed None … 6.0)
- actual-A8-3-wind0: launch_mass_g=139.6839219980059 g (allowed None … 85.0); apogee_m=9.548242055916061 m (allowed 30.0 … 120.0); guide_departure_m_s=7.555020811846815 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.3469238066729 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=139.6839219980059 g (allowed None … 85.0); apogee_m=9.416316946516027 m (allowed 30.0 … 120.0); guide_departure_m_s=7.547094070130438 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.085175353502121 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=142.23392199800588 g (allowed None … 99.0); guide_departure_m_s=9.341052038717686 m/s (allowed 12.0 … None); deployment_speed_m_s=15.358407781395796 m/s (allowed None … 10.0); landing_descent_m_s=6.819017456447315 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=142.23392199800588 g (allowed None … 99.0); guide_departure_m_s=9.332793007811778 m/s (allowed 12.0 … None); deployment_speed_m_s=18.661267540854585 m/s (allowed None … 10.0); landing_descent_m_s=6.816189840747176 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.047053382714644 m/s (allowed 12.0 … None); landing_descent_m_s=6.804029879880361 m/s (allowed None … 6.0)
- actual-C6-3-wind2: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.039312659766379 m/s (allowed 12.0 … None); landing_descent_m_s=6.803952270962378 m/s (allowed None … 6.0)
- actual-C6-5-wind0: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.047053382714644 m/s (allowed 12.0 … None); deployment_speed_m_s=11.564159391729714 m/s (allowed None … 10.0); landing_descent_m_s=6.804029936884105 m/s (allowed None … 6.0)
- actual-C6-5-wind2: launch_mass_g=146.4339219980059 g (allowed None … 113.0); guide_departure_m_s=10.039312659766379 m/s (allowed 12.0 … None); deployment_speed_m_s=16.03804432730534 m/s (allowed None … 10.0); landing_descent_m_s=6.803952290630037 m/s (allowed None … 6.0)

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
