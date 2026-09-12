# Rocket Workbench report

Run: `design-016`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `db7c8e9c77d2b35dd39d59627632812e09f6ddcc8a709100042f273c37f4f049`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 12.80 | 8.62 | 1.16 | unavailable | 11.84 | 1.17 |
| empty-A8-3-wind2 | completed / outside configured limits | 12.61 | 8.61 | 0.55 | unavailable | 12.90 | 0.47 |
| empty-B4-4-wind0 | completed / outside configured limits | 41.72 | 10.48 | 1.08 | 11.84 | 5.11 | 1.67 |
| empty-B4-4-wind2 | completed / outside configured limits | 40.73 | 10.48 | 0.67 | 14.84 | 5.11 | 1.42 |
| empty-C6-3-wind0 | completed / outside configured limits | 127.23 | 11.18 | 1.04 | 7.99 | 5.10 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 123.66 | 11.18 | 0.79 | 9.01 | 5.10 | 20.91 |
| empty-C6-5-wind0 | completed / outside configured limits | 128.93 | 11.18 | 1.01 | 10.25 | 5.10 | 0.63 |
| empty-C6-5-wind2 | completed / outside configured limits | 125.22 | 11.18 | 0.79 | 12.81 | 5.10 | 8.45 |
| dummy-A8-3-wind0 | completed / outside configured limits | 9.34 | 7.48 | 1.57 | unavailable | 11.37 | 0.46 |
| dummy-A8-3-wind2 | completed / outside configured limits | 9.20 | 7.47 | 0.96 | unavailable | 11.00 | 0.43 |
| dummy-B4-4-wind0 | completed / outside configured limits | 31.84 | 9.28 | 1.46 | 15.79 | 5.49 | 0.85 |
| dummy-B4-4-wind2 | completed / outside configured limits | 30.83 | 9.27 | 1.18 | 19.05 | 5.49 | 8.94 |
| dummy-C6-3-wind0 | completed / outside configured limits | 106.48 | 10.00 | 1.45 | 4.82 | 5.47 | 0.05 |
| dummy-C6-3-wind2 | completed / outside configured limits | 102.02 | 9.99 | 1.17 | 7.52 | 5.47 | 5.73 |
| dummy-C6-5-wind0 | completed / outside configured limits | 106.83 | 10.00 | 1.06 | 11.74 | 5.47 | 0.38 |
| dummy-C6-5-wind2 | completed / outside configured limits | 102.33 | 9.99 | 1.17 | 16.29 | 5.47 | 10.68 |
| actual-A8-3-wind0 | completed / outside configured limits | 9.34 | 7.48 | 1.57 | unavailable | 11.37 | 0.46 |
| actual-A8-3-wind2 | completed / outside configured limits | 9.20 | 7.47 | 0.96 | unavailable | 11.00 | 0.43 |
| actual-B4-4-wind0 | completed / outside configured limits | 31.84 | 9.28 | 1.46 | 15.79 | 5.49 | 0.85 |
| actual-B4-4-wind2 | completed / outside configured limits | 30.83 | 9.27 | 1.18 | 19.05 | 5.49 | 8.94 |
| actual-C6-3-wind0 | completed / outside configured limits | 106.48 | 10.00 | 1.45 | 4.82 | 5.47 | 0.05 |
| actual-C6-3-wind2 | completed / outside configured limits | 102.02 | 9.99 | 1.17 | 7.52 | 5.47 | 5.73 |
| actual-C6-5-wind0 | completed / outside configured limits | 106.83 | 10.00 | 1.06 | 11.74 | 5.47 | 0.38 |
| actual-C6-5-wind2 | completed / outside configured limits | 102.33 | 9.99 | 1.17 | 16.29 | 5.47 | 10.68 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-A8-3-wind2: Large angle of attack encountered (19.3°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (22.4°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-A8-3-wind2: Large angle of attack encountered (22.4°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=123.04663094721326 g (allowed None … 85.0); apogee_m=12.799932351017267 m (allowed 30.0 … 120.0); guide_departure_m_s=8.62210122176415 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.840114342762368 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=123.04663094721326 g (allowed None … 85.0); apogee_m=12.612882640512193 m (allowed 30.0 … 120.0); guide_departure_m_s=8.613214214397253 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5492828481375227 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.904802467324341 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=125.59663094721324 g (allowed None … 99.0); guide_departure_m_s=10.483967528174723 m/s (allowed 12.0 … None); deployment_speed_m_s=11.843936828532842 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=125.59663094721324 g (allowed None … 99.0); guide_departure_m_s=10.475005201172289 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6742113039891235 cal (allowed 1.0 … None); deployment_speed_m_s=14.841470707473933 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=129.79663094721326 g (allowed None … 113.0); apogee_m=127.2328650924527 m (allowed 30.0 … 120.0); guide_departure_m_s=11.18362653601408 m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=129.79663094721326 g (allowed None … 113.0); apogee_m=123.66083077602914 m (allowed 30.0 … 120.0); guide_departure_m_s=11.17508228323834 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7860745667675421 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=129.79663094721326 g (allowed None … 113.0); apogee_m=128.92534824530733 m (allowed 30.0 … 120.0); guide_departure_m_s=11.18362653601408 m/s (allowed 12.0 … None); deployment_speed_m_s=10.250481247715284 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=129.79663094721326 g (allowed None … 113.0); apogee_m=125.21960530687855 m (allowed 30.0 … 120.0); guide_departure_m_s=11.17508228323834 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7860745667675421 cal (allowed 1.0 … None); deployment_speed_m_s=12.808925045212943 m/s (allowed None … 10.0)
- dummy-A8-3-wind0: launch_mass_g=141.04663094721323 g (allowed None … 85.0); apogee_m=9.337615771036303 m (allowed 30.0 … 120.0); guide_departure_m_s=7.481521720112544 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.372629036221458 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=141.04663094721323 g (allowed None … 85.0); apogee_m=9.200986690924282 m (allowed 30.0 … 120.0); guide_departure_m_s=7.473832480340398 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.958560785684946 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.99575040039451 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=143.59663094721324 g (allowed None … 99.0); guide_departure_m_s=9.275248888818739 m/s (allowed 12.0 … None); deployment_speed_m_s=15.79257723676151 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=143.59663094721324 g (allowed None … 99.0); guide_departure_m_s=9.267187518665088 m/s (allowed 12.0 … None); deployment_speed_m_s=19.04956360571834 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.995105230636229 m/s (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.98752687444114 m/s (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.995105230636229 m/s (allowed 12.0 … None); deployment_speed_m_s=11.73707469591561 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.98752687444114 m/s (allowed 12.0 … None); deployment_speed_m_s=16.28583339079307 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=141.04663094721323 g (allowed None … 85.0); apogee_m=9.337615771036303 m (allowed 30.0 … 120.0); guide_departure_m_s=7.481521720112544 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.372629036221458 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=141.04663094721323 g (allowed None … 85.0); apogee_m=9.200986690924282 m (allowed 30.0 … 120.0); guide_departure_m_s=7.473832480340398 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.958560785684946 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.995750400394517 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=143.59663094721324 g (allowed None … 99.0); guide_departure_m_s=9.275248888818739 m/s (allowed 12.0 … None); deployment_speed_m_s=15.792577236761517 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=143.59663094721324 g (allowed None … 99.0); guide_departure_m_s=9.267187518665088 m/s (allowed 12.0 … None); deployment_speed_m_s=19.04956360571832 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.995105230636229 m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.98752687444114 m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.995105230636229 m/s (allowed 12.0 … None); deployment_speed_m_s=11.73707469591561 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=147.79663094721323 g (allowed None … 113.0); guide_departure_m_s=9.98752687444114 m/s (allowed 12.0 … None); deployment_speed_m_s=16.28583339079312 m/s (allowed None … 10.0)

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
