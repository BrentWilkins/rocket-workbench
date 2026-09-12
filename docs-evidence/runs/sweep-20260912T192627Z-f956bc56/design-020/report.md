# Rocket Workbench report

Run: `design-020`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `9445520803fa08082fa9263e37143d3b667b33bfca98df33e3d5b1f73d0c22ad`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    12.73 |      8.60 |           0.73 | unavailable |       13.80 |    0.97 |
| empty-A8-3-wind2  | completed / outside configured limits |    12.67 |      8.59 |           0.11 | unavailable |       14.59 |    1.68 |
| empty-B4-4-wind0  | completed / outside configured limits |    41.99 |     10.43 |           0.59 |       14.21 |        4.27 |    1.57 |
| empty-B4-4-wind2  | completed / outside configured limits |    41.38 |     10.42 |           0.11 |       15.09 |        4.27 |    7.61 |
| empty-C6-3-wind0  | completed / outside configured limits |   130.36 |     11.13 |           0.58 |        9.13 |        4.26 |    0.04 |
| empty-C6-3-wind2  | completed / outside configured limits |   128.36 |     11.12 |           0.27 |        9.45 |        4.26 |   42.08 |
| empty-C6-5-wind0  | completed / outside configured limits |   133.09 |     11.13 |           0.32 |       10.19 |        4.26 |    0.20 |
| empty-C6-5-wind2  | completed / outside configured limits |   131.00 |     11.12 |           0.19 |        9.23 |        4.26 |   34.30 |
| dummy-A8-3-wind0  | completed / outside configured limits |     9.28 |      7.47 |           1.19 | unavailable |       12.10 |    0.40 |
| dummy-A8-3-wind2  | completed / outside configured limits |     9.24 |      7.46 |           0.57 | unavailable |       12.04 |    0.79 |
| dummy-B4-4-wind0  | completed / outside configured limits |    31.90 |      9.23 |           0.85 |       13.98 |        4.58 |    2.46 |
| dummy-B4-4-wind2  | completed / outside configured limits |    31.19 |      9.23 |           0.57 |       16.15 |        4.58 |    0.53 |
| dummy-C6-3-wind0  | completed / outside configured limits |   108.58 |      9.95 |           1.04 |        5.58 |        4.57 |    0.04 |
| dummy-C6-3-wind2  | completed / outside configured limits |   105.50 |      9.94 |           0.70 |        7.14 |        4.57 |   21.81 |
| dummy-C6-5-wind0  | completed / outside configured limits |   109.27 |      9.95 |           0.99 |       12.24 |        4.57 |    0.71 |
| dummy-C6-5-wind2  | completed / outside configured limits |   106.17 |      9.94 |           0.70 |       14.68 |        4.57 |    7.90 |
| actual-A8-3-wind0 | completed / outside configured limits |     9.28 |      7.47 |           1.19 | unavailable |       12.10 |    0.40 |
| actual-A8-3-wind2 | completed / outside configured limits |     9.24 |      7.46 |           0.57 | unavailable |       12.04 |    0.79 |
| actual-B4-4-wind0 | completed / outside configured limits |    31.90 |      9.23 |           0.85 |       13.98 |        4.58 |    2.46 |
| actual-B4-4-wind2 | completed / outside configured limits |    31.19 |      9.23 |           0.57 |       16.15 |        4.58 |    0.53 |
| actual-C6-3-wind0 | completed / outside configured limits |   108.58 |      9.95 |           1.04 |        5.58 |        4.57 |    0.04 |
| actual-C6-3-wind2 | completed / outside configured limits |   105.50 |      9.94 |           0.70 |        7.14 |        4.57 |   21.81 |
| actual-C6-5-wind0 | completed / outside configured limits |   109.27 |      9.95 |           0.99 |       12.24 |        4.57 |    0.71 |
| actual-C6-5-wind2 | completed / outside configured limits |   106.17 |      9.94 |           0.70 |       14.68 |        4.57 |    7.90 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
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
- Measured mass and balance: Nominal 457 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=123.61916825296501 g (allowed None … 85.0); apogee_m=12.730689570403525 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.59807175270046 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7324024393579931 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=13.796825917826691 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=123.61916825296501 g (allowed None … 85.0); apogee_m=12.665760751051454 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.590243871522462 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.10974836057783034 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=14.592641994254237 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=126.16916825296501 g (allowed None … 99.0); guide_departure_m_s=10.430869301171334 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.5892625328306468 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.207399051854534 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=126.16916825296501 g (allowed None … 99.0); guide_departure_m_s=10.42299043623463 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.11154697285431985 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.085318390215523 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=130.369168252965 g (allowed None … 113.0); apogee_m=130.35642130756753 m (allowed 30.0
  … 120.0); guide_departure_m_s=11.128419779101845 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5798036755084107 cal (allowed 1.0 … None)
- empty-C6-3-wind2: launch_mass_g=130.369168252965 g (allowed None … 113.0); apogee_m=128.3562711657922 m (allowed 30.0
  … 120.0); guide_departure_m_s=11.12098562658469 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.2670436353072888 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=130.369168252965 g (allowed None … 113.0); apogee_m=133.0881867243984 m (allowed 30.0
  … 120.0); guide_departure_m_s=11.128419779101845 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.31559893841381037 cal (allowed 1.0 … None); deployment_speed_m_s=10.185397994379434 m/s
  (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=130.369168252965 g (allowed None … 113.0); apogee_m=131.00146947937822 m (allowed 30.0
  … 120.0); guide_departure_m_s=11.12098562658469 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.18801318745413126 cal (allowed 1.0 … None)
- dummy-A8-3-wind0: launch_mass_g=141.619168252965 g (allowed None … 85.0); apogee_m=9.277769875786188 m (allowed 30.0 …
  120.0); guide_departure_m_s=7.466685121732084 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=12.102662611151624 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=141.619168252965 g (allowed None … 85.0); apogee_m=9.238696872407514 m (allowed 30.0 …
  120.0); guide_departure_m_s=7.459868264698415 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5692461215404266 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=12.037804632383489 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=144.169168252965 g (allowed None … 99.0); guide_departure_m_s=9.23275069733587 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8518083059463655 cal (allowed 1.0 … None);
  deployment_speed_m_s=13.982522981623744 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=144.169168252965 g (allowed None … 99.0); guide_departure_m_s=9.22574438090513 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.5688724164350948 cal (allowed 1.0 … None);
  deployment_speed_m_s=16.148858015783436 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.950528957089947 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.94393129799338 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.6996379768724633 cal (allowed 1.0 … None)
- dummy-C6-5-wind0: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.950528957089947 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.9900876923549334 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.238676934039338 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.94393129799338 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.6996379768724633 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.67819502665381 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=141.619168252965 g (allowed None … 85.0); apogee_m=9.277769875786188 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.466685121732084 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=12.102662611151624 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=141.619168252965 g (allowed None … 85.0); apogee_m=9.238696872407514 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.459868264698415 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5692461215404266 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=12.037804632383489 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=144.169168252965 g (allowed None … 99.0); guide_departure_m_s=9.23275069733587 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8518083059463655 cal (allowed 1.0 … None);
  deployment_speed_m_s=13.982522981623747 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=144.169168252965 g (allowed None … 99.0); guide_departure_m_s=9.22574438090513 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.5688724164350948 cal (allowed 1.0 … None);
  deployment_speed_m_s=16.148858015783425 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.950528957089947 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.94393129799338 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.6996379768724633 cal (allowed 1.0 … None)
- actual-C6-5-wind0: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.950528957089947 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.9900876923549334 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.238676934039338 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=148.369168252965 g (allowed None … 113.0); guide_departure_m_s=9.94393129799338 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.6996379768724633 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.67819502665364 m/s (allowed None … 10.0)

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
