# Rocket Workbench report

Run: `design-025`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `46cb377744304802a46c1be6194b16f808763b5e11857f8ecb5c02785d99f618`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    12.33 |      8.50 |           1.34 | unavailable |       11.28 |    1.02 |
| empty-A8-3-wind2  | completed / outside configured limits |    12.16 |      8.49 |           0.69 | unavailable |       12.07 |    0.62 |
| empty-B4-4-wind0  | completed / outside configured limits |    40.36 |     10.34 |           1.14 |       11.43 |        5.16 |    1.49 |
| empty-B4-4-wind2  | completed / outside configured limits |    39.41 |     10.33 |           0.85 |       15.14 |        5.16 |    1.92 |
| empty-C6-3-wind0  | completed / outside configured limits |   124.12 |     10.98 |           1.33 |        7.44 |        5.14 |    0.05 |
| empty-C6-3-wind2  | completed / outside configured limits |   120.56 |     10.97 |           1.00 |        8.55 |        5.14 |   19.51 |
| empty-C6-5-wind0  | completed / outside configured limits |   125.51 |     10.98 |           1.12 |       10.49 |        5.14 |    0.73 |
| empty-C6-5-wind2  | completed / outside configured limits |   121.85 |     10.97 |           1.00 |       13.22 |        5.14 |    6.88 |
| dummy-A8-3-wind0  | completed / outside configured limits |     9.03 |      7.36 |           1.85 | unavailable |       11.14 |    0.48 |
| dummy-A8-3-wind2  | completed / outside configured limits |     8.91 |      7.36 |           1.16 | unavailable |       10.91 |    0.29 |
| dummy-B4-4-wind0  | completed / outside configured limits |    30.87 |      9.12 |           1.87 |       15.95 |        5.53 |    1.07 |
| dummy-B4-4-wind2  | completed / outside configured limits |    29.88 |      9.11 |           1.36 |       19.15 |        5.53 |    9.13 |
| dummy-C6-3-wind0  | completed / outside configured limits |   103.77 |      9.83 |           1.80 |        4.29 |        5.51 |    0.04 |
| dummy-C6-3-wind2  | completed / outside configured limits |    99.41 |      9.82 |           1.43 |        7.20 |        5.51 |    4.97 |
| dummy-C6-5-wind0  | completed / outside configured limits |   104.02 |      9.83 |           1.74 |       12.01 |        5.51 |    0.39 |
| dummy-C6-5-wind2  | completed / outside configured limits |    99.63 |      9.82 |           1.43 |       16.66 |        5.51 |   11.48 |
| actual-A8-3-wind0 | completed / outside configured limits |     9.03 |      7.36 |           1.85 | unavailable |       11.14 |    0.48 |
| actual-A8-3-wind2 | completed / outside configured limits |     8.91 |      7.36 |           1.16 | unavailable |       10.91 |    0.29 |
| actual-B4-4-wind0 | completed / outside configured limits |    30.87 |      9.12 |           1.87 |       15.95 |        5.53 |    1.07 |
| actual-B4-4-wind2 | completed / outside configured limits |    29.88 |      9.11 |           1.36 |       19.15 |        5.53 |    9.13 |
| actual-C6-3-wind0 | completed / outside configured limits |   103.77 |      9.83 |           1.80 |        4.29 |        5.51 |    0.04 |
| actual-C6-3-wind2 | completed / outside configured limits |    99.41 |      9.82 |           1.43 |        7.20 |        5.51 |    4.97 |
| actual-C6-5-wind0 | completed / outside configured limits |   104.02 |      9.83 |           1.74 |       12.01 |        5.51 |    0.39 |
| actual-C6-5-wind2 | completed / outside configured limits |    99.63 |      9.82 |           1.43 |       16.66 |        5.51 |   11.48 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Large angle of attack encountered (21.8°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (19°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (19°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=125.0466309472131 g (allowed None … 85.0); apogee_m=12.330894729940423 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.500065684026053 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.282861879148092 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=125.0466309472131 g (allowed None … 85.0); apogee_m=12.158708788814474 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.490997172661192 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6903955928506635 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=12.07489764339619 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=127.59663094721313 g (allowed None … 99.0); guide_departure_m_s=10.342164786549672 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.43409030287064 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=127.59663094721313 g (allowed None … 99.0); guide_departure_m_s=10.332988763560278 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8521597229179102 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.138455307539232 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=124.1245109826305 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.980537639429194 m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=120.56391361194709 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.972077614174976 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9971041226792579 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=125.50745670833277 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.980537639429194 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.491994352257183 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=121.85260418418248 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.972077614174976 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9971041226792579 cal (allowed 1.0 … None); deployment_speed_m_s=13.216632520222914 m/s
  (allowed None … 10.0)
- dummy-A8-3-wind0: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=9.025341910013676 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.363271703590972 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.138762260078416 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=8.90750786716924 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.355562876760579 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.910996453499466 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=145.59663094721313 g (allowed None … 99.0); guide_departure_m_s=9.118282704660938 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.946526331997635 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=145.59663094721313 g (allowed None … 99.0); apogee_m=29.87891693311239 m (allowed 30.0
  … 120.0); guide_departure_m_s=9.110287425180893 m/s (allowed 12.0 … None); deployment_speed_m_s=19.15103332231615 m/s
  (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.013984783198728 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.656789649377814 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=9.025341910013676 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.363271703590972 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.138762260078416 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=8.90750786716924 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.355562876760579 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.910996453499465 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=145.59663094721313 g (allowed None … 99.0); guide_departure_m_s=9.118282704660938 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.946526331997644 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=145.59663094721313 g (allowed None … 99.0); apogee_m=29.87891693311241 m (allowed
  30.0 … 120.0); guide_departure_m_s=9.110287425180893 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.151033322316298 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788
  m/s (allowed 12.0 … None); deployment_speed_m_s=12.013984783198726 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.656789649377856 m/s (allowed None … 10.0)

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is
  scenario-dependent.
- Native OpenRocket aerodynamics; conical nose, cylindrical sections, three flat trapezoidal fins and tapered collar
  fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in
  collar override.
- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful
  view.
- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using
  (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.
- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground
  event, not a structural impact assessment.
- Recovery is motor-ejection deployment with configured Cd; packing envelope, ejection seal, thermal protection and
  attachment loads require physical checks.
- Reference mode preserves upstream geometry and masses; demonstration CAD and baseline mass assumptions do not apply to
  that reference.

## Configured criteria

- apogee_m: 30.0 … 120.0 m; engineering assumption; Project engineering assumption for demonstration screening; not a
  launch clearance
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
  "repository_revision": null
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
