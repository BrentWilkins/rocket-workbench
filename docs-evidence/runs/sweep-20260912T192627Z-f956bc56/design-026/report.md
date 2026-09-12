# Rocket Workbench report

Run: `design-026`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `65c8b5988428208c901cd2e47783d32d73002c2c853c92d9160ae4debf5a0203`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    11.46 |      8.21 |           1.46 | unavailable |       11.28 |    0.90 |
| empty-A8-3-wind2  | completed / outside configured limits |    11.30 |      8.20 |           0.68 | unavailable |       11.86 |    0.51 |
| empty-B4-4-wind0  | completed / outside configured limits |    37.93 |     10.06 |           1.29 |       11.79 |        4.37 |    1.60 |
| empty-B4-4-wind2  | completed / outside configured limits |    36.99 |     10.05 |           0.85 |       16.10 |        4.37 |    1.64 |
| empty-C6-3-wind0  | completed / outside configured limits |   119.15 |     10.72 |           1.33 |        6.76 |        4.36 |    0.04 |
| empty-C6-3-wind2  | completed / outside configured limits |   115.52 |     10.72 |           0.99 |        8.12 |        4.36 |   25.82 |
| empty-C6-5-wind0  | completed / outside configured limits |   120.38 |     10.72 |           1.18 |       10.75 |        4.36 |    0.72 |
| empty-C6-5-wind2  | completed / outside configured limits |   116.63 |     10.72 |           0.99 |       13.92 |        4.36 |   11.63 |
| dummy-A8-3-wind0  | completed / outside configured limits |     8.43 |      7.15 |           1.93 | unavailable |       10.99 |    0.44 |
| dummy-A8-3-wind2  | completed / outside configured limits |     8.34 |      7.14 |           1.14 | unavailable |       10.71 |    0.22 |
| dummy-B4-4-wind0  | completed / outside configured limits |    29.09 |      8.89 |           1.87 |       16.55 |        4.67 |    0.97 |
| dummy-B4-4-wind2  | completed / outside configured limits |    28.11 |      8.88 |           1.36 |       19.78 |        4.67 |    9.67 |
| dummy-C6-3-wind0  | completed / outside configured limits |    99.34 |      9.62 |           1.78 |        3.54 |        4.66 |    0.04 |
| dummy-C6-3-wind2  | completed / outside configured limits |    94.94 |      9.62 |           1.41 |        6.99 |        4.66 |   10.19 |
| dummy-C6-5-wind0  | completed / outside configured limits |    99.51 |      9.62 |           1.38 |       12.63 |        4.66 |    0.33 |
| dummy-C6-5-wind2  | completed / outside configured limits |    95.07 |      9.62 |           1.41 |       17.38 |        4.66 |    8.22 |
| actual-A8-3-wind0 | completed / outside configured limits |     8.43 |      7.15 |           1.93 | unavailable |       10.99 |    0.44 |
| actual-A8-3-wind2 | completed / outside configured limits |     8.34 |      7.14 |           1.14 | unavailable |       10.71 |    0.22 |
| actual-B4-4-wind0 | completed / outside configured limits |    29.09 |      8.89 |           1.87 |       16.55 |        4.67 |    0.97 |
| actual-B4-4-wind2 | completed / outside configured limits |    28.11 |      8.88 |           1.36 |       19.78 |        4.67 |    9.67 |
| actual-C6-3-wind0 | completed / outside configured limits |    99.34 |      9.62 |           1.78 |        3.54 |        4.66 |    0.04 |
| actual-C6-3-wind2 | completed / outside configured limits |    94.94 |      9.62 |           1.41 |        6.99 |        4.66 |   10.19 |
| actual-C6-5-wind0 | completed / outside configured limits |    99.51 |      9.62 |           1.38 |       12.63 |        4.66 |    0.33 |
| actual-C6-5-wind2 | completed / outside configured limits |    95.07 |      9.62 |           1.41 |       17.38 |        4.66 |    8.22 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Large angle of attack encountered (23.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (16.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (16.4°); Flight Event occurred after landing: Ejection charge;
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
- Measured mass and balance: Nominal 457 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=129.15442992598224 g (allowed None … 85.0); apogee_m=11.45597684349531 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.210527592303768 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.282321009435016 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=129.15442992598224 g (allowed None … 85.0); apogee_m=11.300381578190779 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.201829914282577 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.676776765114159 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=11.862489193087704 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=131.70442992598225 g (allowed None … 99.0); guide_departure_m_s=10.059219550173253 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.794237564139587 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=131.70442992598225 g (allowed None … 99.0); guide_departure_m_s=10.050262447172821 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8480609157637873 cal (allowed 1.0 … None);
  deployment_speed_m_s=16.096511727193715 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=135.90442992598224 g (allowed None … 113.0); guide_departure_m_s=10.724237749603507
  m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=135.90442992598224 g (allowed None … 113.0); guide_departure_m_s=10.715926522013964
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9864333848686423 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=135.90442992598224 g (allowed None … 113.0); apogee_m=120.37925085779986 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.724237749603507 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.747927218485634 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=135.90442992598224 g (allowed None … 113.0); guide_departure_m_s=10.715926522013964
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9864333848686423 cal (allowed 1.0 … None);
  deployment_speed_m_s=13.92200545852278 m/s (allowed None … 10.0)
- dummy-A8-3-wind0: launch_mass_g=147.15442992598224 g (allowed None … 85.0); apogee_m=8.434873205405617 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.149623140173775 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.988973880054688 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=147.15442992598224 g (allowed None … 85.0); apogee_m=8.33642193184141 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.142111961001205 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.708800598968756 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=149.70442992598223 g (allowed None … 99.0); apogee_m=29.085332846271832 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.888015525648045 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.545987801045047 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=149.70442992598223 g (allowed None … 99.0); apogee_m=28.10965951894014 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.880196859719359 m/s (allowed 12.0 … None); deployment_speed_m_s=19.776013007116113 m/s
  (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.62244937618144 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.615052699101858 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.62244937618144 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.630498671357781 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.615052699101858 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.38117951035471 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=147.15442992598224 g (allowed None … 85.0); apogee_m=8.434873205405617 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.149623140173775 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.988973880054687 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=147.15442992598224 g (allowed None … 85.0); apogee_m=8.33642193184141 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.142111961001205 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.708800598968756 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=149.70442992598223 g (allowed None … 99.0); apogee_m=29.085332846271832 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.888015525648045 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.545987801045055 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=149.70442992598223 g (allowed None … 99.0); apogee_m=28.109659518940177 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.880196859719359 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.776013007115992 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.62244937618144 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.615052699101858
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.62244937618144 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.630498671357785 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=153.90442992598224 g (allowed None … 113.0); guide_departure_m_s=9.615052699101858
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.381179510354695 m/s (allowed None … 10.0)

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
