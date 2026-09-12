# Rocket Workbench report

Run: `design-022`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `e1d87b3a0dddaa54ee24f4c1df8bc0b1ab6b47c13f3ab319912c8030d81623f8`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    13.01 |      8.69 |           1.16 | unavailable |       12.52 |    1.27 |
| empty-A8-3-wind2  | completed / outside configured limits |    12.87 |      8.68 |           0.45 | unavailable |       13.40 |    1.14 |
| empty-B4-4-wind0  | completed / outside configured limits |    42.48 |     10.56 |           1.00 |       12.56 |        5.10 |    1.87 |
| empty-B4-4-wind2  | completed / outside configured limits |    41.61 |     10.55 |           0.49 |       12.93 |        5.10 |    2.40 |
| empty-C6-3-wind0  | completed / outside configured limits |   129.83 |     11.19 |           1.06 |        8.61 |        5.09 |    0.05 |
| empty-C6-3-wind2  | completed / outside configured limits |   126.81 |     11.18 |           0.71 |        9.32 |        5.09 |   25.17 |
| empty-C6-5-wind0  | completed / outside configured limits |   131.91 |     11.19 |           0.55 |       10.31 |        5.09 |    0.44 |
| empty-C6-5-wind2  | completed / outside configured limits |   128.78 |     11.18 |           0.71 |       11.70 |        5.09 |   14.36 |
| dummy-A8-3-wind0  | completed / outside configured limits |     9.47 |      7.54 |           1.66 | unavailable |       11.43 |    0.51 |
| dummy-A8-3-wind2  | completed / outside configured limits |     9.38 |      7.53 |           0.92 | unavailable |       11.18 |    0.23 |
| dummy-B4-4-wind0  | completed / outside configured limits |    32.34 |      9.30 |           1.53 |       14.13 |        5.47 |    0.15 |
| dummy-B4-4-wind2  | completed / outside configured limits |    31.42 |      9.29 |           1.07 |       18.30 |        5.47 |    7.47 |
| dummy-C6-3-wind0  | completed / outside configured limits |   108.50 |     10.00 |           1.53 |        5.31 |        5.46 |    0.04 |
| dummy-C6-3-wind2  | completed / outside configured limits |   104.62 |      9.99 |           1.15 |        7.44 |        5.46 |    9.38 |
| dummy-C6-5-wind0  | completed / outside configured limits |   108.98 |     10.00 |           1.04 |       11.52 |        5.46 |    0.78 |
| dummy-C6-5-wind2  | completed / outside configured limits |   105.08 |      9.99 |           1.15 |       15.51 |        5.46 |    5.62 |
| actual-A8-3-wind0 | completed / outside configured limits |     9.47 |      7.54 |           1.66 | unavailable |       11.43 |    0.51 |
| actual-A8-3-wind2 | completed / outside configured limits |     9.38 |      7.53 |           0.92 | unavailable |       11.18 |    0.23 |
| actual-B4-4-wind0 | completed / outside configured limits |    32.34 |      9.30 |           1.53 |       14.13 |        5.47 |    0.15 |
| actual-B4-4-wind2 | completed / outside configured limits |    31.42 |      9.29 |           1.07 |       18.30 |        5.47 |    7.47 |
| actual-C6-3-wind0 | completed / outside configured limits |   108.50 |     10.00 |           1.53 |        5.31 |        5.46 |    0.04 |
| actual-C6-3-wind2 | completed / outside configured limits |   104.62 |      9.99 |           1.15 |        7.44 |        5.46 |    9.38 |
| actual-C6-5-wind0 | completed / outside configured limits |   108.98 |     10.00 |           1.04 |       11.52 |        5.46 |    0.78 |
| actual-C6-5-wind2 | completed / outside configured limits |   105.08 |      9.99 |           1.15 |       15.51 |        5.46 |    5.62 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Large angle of attack encountered (20.3°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
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

- empty-A8-3-wind0: launch_mass_g=122.27898925783664 g (allowed None … 85.0); apogee_m=13.008678486120246 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.6927825530641 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=12.521557849386344 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=122.27898925783664 g (allowed None … 85.0); apogee_m=12.866324171178807 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.684189323139071 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.45025436452762374 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=13.400589509105064 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=124.82898925783664 g (allowed None … 99.0); guide_departure_m_s=10.562244189834049 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.563115098227874 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=124.82898925783664 g (allowed None … 99.0); guide_departure_m_s=10.55351538232931 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.4858389893909532 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.92527727095782 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=129.02898925783666 g (allowed None … 113.0); apogee_m=129.83051297315234 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.188553241426606 m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=129.02898925783666 g (allowed None … 113.0); apogee_m=126.81192978647451 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.180551054269126 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7137080794617974 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=129.02898925783666 g (allowed None … 113.0); apogee_m=131.90917263248767 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.188553241426606 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5474220113134087 cal (allowed 1.0 … None); deployment_speed_m_s=10.309058202139251 m/s
  (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=129.02898925783666 g (allowed None … 113.0); apogee_m=128.7799681438096 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.180551054269126 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7137080794617974 cal (allowed 1.0 … None); deployment_speed_m_s=11.704001515469693 m/s
  (allowed None … 10.0)
- dummy-A8-3-wind0: launch_mass_g=140.27898925783663 g (allowed None … 85.0); apogee_m=9.47135975418653 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.537660577408493 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.42781764327833 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=140.27898925783663 g (allowed None … 85.0); apogee_m=9.38174390537488 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.530226526937471 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9170730075493795 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.182103034430323 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=142.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.295061459983305 m/s
  (allowed 12.0 … None); deployment_speed_m_s=14.125319427411219 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=142.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.287460838932867 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.303286189669436 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.998948155359745 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.991822453035935 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.998948155359745 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.523471071308709 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.991822453035935 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.507655990723103 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=140.27898925783663 g (allowed None … 85.0); apogee_m=9.47135975418653 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.537660577408493 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.427817643278328 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=140.27898925783663 g (allowed None … 85.0); apogee_m=9.38174390537488 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.530226526937471 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9170730075493795 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.182103034430321 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=142.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.295061459983305 m/s
  (allowed 12.0 … None); deployment_speed_m_s=14.125319427411211 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=142.82898925783664 g (allowed None … 99.0); guide_departure_m_s=9.287460838932867 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.30328618966943 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.998948155359745
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.991822453035935
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.998948155359745
  m/s (allowed 12.0 … None); deployment_speed_m_s=11.523471071308709 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=147.02898925783663 g (allowed None … 113.0); guide_departure_m_s=9.991822453035935
  m/s (allowed 12.0 … None); deployment_speed_m_s=15.507655990723695 m/s (allowed None … 10.0)

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
