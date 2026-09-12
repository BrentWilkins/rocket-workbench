# Rocket Workbench report

Run: `design-019`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `e9fc61a0c6e8c69cec4f70607658b1c4cc6659f0e34ef1b5cea43c97861a9535`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 13.74 | 8.90 | 0.75 | 14.34 | 13.32 | 1.19 |
| empty-A8-3-wind2 | completed / outside configured limits | 13.66 | 8.89 | 0.13 | unavailable | 14.79 | 1.77 |
| empty-B4-4-wind0 | completed / outside configured limits | 44.78 | 10.73 | 0.69 | 13.51 | 5.04 | 1.49 |
| empty-B4-4-wind2 | completed / outside configured limits | 44.15 | 10.72 | 0.13 | 14.53 | 5.04 | 6.66 |
| empty-C6-3-wind0 | completed / outside configured limits | 135.95 | 11.38 | 0.59 | 9.89 | 5.03 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 133.94 | 11.38 | 0.28 | 10.14 | 5.03 | 34.80 |
| empty-C6-5-wind0 | completed / outside configured limits | 138.96 | 11.38 | 0.51 | 9.56 | 5.03 | 0.17 |
| empty-C6-5-wind2 | completed / outside configured limits | 136.88 | 11.38 | 0.20 | 8.62 | 5.03 | 27.73 |
| dummy-A8-3-wind0 | completed / outside configured limits | 9.95 | 7.69 | 1.22 | unavailable | 12.18 | 0.49 |
| dummy-A8-3-wind2 | completed / outside configured limits | 9.90 | 7.69 | 0.60 | unavailable | 12.39 | 0.82 |
| dummy-B4-4-wind0 | completed / outside configured limits | 33.92 | 9.48 | 1.11 | 13.28 | 5.41 | 2.31 |
| dummy-B4-4-wind2 | completed / outside configured limits | 33.17 | 9.47 | 0.60 | 15.44 | 5.41 | 0.97 |
| dummy-C6-3-wind0 | completed / outside configured limits | 113.54 | 10.17 | 1.06 | 6.41 | 5.40 | 0.04 |
| dummy-C6-3-wind2 | completed / outside configured limits | 110.43 | 10.17 | 0.73 | 7.71 | 5.40 | 15.88 |
| dummy-C6-5-wind0 | completed / outside configured limits | 114.40 | 10.17 | 0.74 | 11.87 | 5.40 | 0.66 |
| dummy-C6-5-wind2 | completed / outside configured limits | 111.29 | 10.17 | 0.73 | 13.88 | 5.40 | 3.44 |
| actual-A8-3-wind0 | completed / outside configured limits | 9.95 | 7.69 | 1.22 | unavailable | 12.18 | 0.49 |
| actual-A8-3-wind2 | completed / outside configured limits | 9.90 | 7.69 | 0.60 | unavailable | 12.39 | 0.82 |
| actual-B4-4-wind0 | completed / outside configured limits | 33.92 | 9.48 | 1.11 | 13.28 | 5.41 | 2.31 |
| actual-B4-4-wind2 | completed / outside configured limits | 33.17 | 9.47 | 0.60 | 15.44 | 5.41 | 0.97 |
| actual-C6-3-wind0 | completed / outside configured limits | 113.54 | 10.17 | 1.06 | 6.41 | 5.40 | 0.04 |
| actual-C6-3-wind2 | completed / outside configured limits | 110.43 | 10.17 | 0.73 | 7.71 | 5.40 | 15.88 |
| actual-C6-5-wind0 | completed / outside configured limits | 114.40 | 10.17 | 0.74 | 11.87 | 5.40 | 0.66 |
| actual-C6-5-wind2 | completed / outside configured limits | 111.29 | 10.17 | 0.73 | 13.88 | 5.40 | 3.44 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: no engine warnings
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=119.51136927419587 g (allowed None … 85.0); apogee_m=13.74046834066997 m (allowed 30.0 … 120.0); guide_departure_m_s=8.900721340924486 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7463317181758523 cal (allowed 1.0 … None); deployment_speed_m_s=14.337581027788962 m/s (allowed None … 10.0); landing_descent_m_s=13.32347335384011 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=119.51136927419587 g (allowed None … 85.0); apogee_m=13.65679794036082 m (allowed 30.0 … 120.0); guide_departure_m_s=8.89258611528369 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.12514742589533462 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=14.788757969802864 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=122.06136927419587 g (allowed None … 99.0); guide_departure_m_s=10.73208183114015 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6893788925733145 cal (allowed 1.0 … None); deployment_speed_m_s=13.512282567942817 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=122.06136927419587 g (allowed None … 99.0); guide_departure_m_s=10.724023540630865 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.12763223330474277 cal (allowed 1.0 … None); deployment_speed_m_s=14.532766413257871 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=126.26136927419587 g (allowed None … 113.0); apogee_m=135.949881438402 m (allowed 30.0 … 120.0); guide_departure_m_s=11.384574191130811 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5881918415394345 cal (allowed 1.0 … None)
- empty-C6-3-wind2: launch_mass_g=126.26136927419587 g (allowed None … 113.0); apogee_m=133.94030237217552 m (allowed 30.0 … 120.0); guide_departure_m_s=11.37704903565239 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.2805428766922736 cal (allowed 1.0 … None); deployment_speed_m_s=10.138409346663664 m/s (allowed None … 10.0)
- empty-C6-5-wind0: launch_mass_g=126.26136927419587 g (allowed None … 113.0); apogee_m=138.96165511732735 m (allowed 30.0 … 120.0); guide_departure_m_s=11.384574191130811 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5123201573003148 cal (allowed 1.0 … None)
- empty-C6-5-wind2: launch_mass_g=126.26136927419587 g (allowed None … 113.0); apogee_m=136.87622392504264 m (allowed 30.0 … 120.0); guide_departure_m_s=11.37704903565239 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.19787017074626312 cal (allowed 1.0 … None)
- dummy-A8-3-wind0: launch_mass_g=137.51136927419586 g (allowed None … 85.0); apogee_m=9.948180613366617 m (allowed 30.0 … 120.0); guide_departure_m_s=7.692887439945073 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.177889635641035 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=137.51136927419586 g (allowed None … 85.0); apogee_m=9.896725985405842 m (allowed 30.0 … 120.0); guide_departure_m_s=7.685903145050529 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5981025444619377 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.393469762310122 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=140.06136927419584 g (allowed None … 99.0); guide_departure_m_s=9.47759352180218 m/s (allowed 12.0 … None); deployment_speed_m_s=13.278985580568705 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=140.06136927419584 g (allowed None … 99.0); guide_departure_m_s=9.47041202319086 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5986416399208656 cal (allowed 1.0 … None); deployment_speed_m_s=15.443507053823767 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.172095980141888 m/s (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.165651329107247 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7253878056957566 cal (allowed 1.0 … None)
- dummy-C6-5-wind0: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.172095980141888 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.736559718733212 cal (allowed 1.0 … None); deployment_speed_m_s=11.868366128247049 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.165651329107247 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7253878056957566 cal (allowed 1.0 … None); deployment_speed_m_s=13.880853963092573 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=137.51136927419586 g (allowed None … 85.0); apogee_m=9.948180613366617 m (allowed 30.0 … 120.0); guide_departure_m_s=7.692887439945073 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.177889635641035 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=137.51136927419586 g (allowed None … 85.0); apogee_m=9.896725985405842 m (allowed 30.0 … 120.0); guide_departure_m_s=7.685903145050529 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5981025444619377 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.393469762310124 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=140.06136927419584 g (allowed None … 99.0); guide_departure_m_s=9.47759352180218 m/s (allowed 12.0 … None); deployment_speed_m_s=13.278985580568706 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=140.06136927419584 g (allowed None … 99.0); guide_departure_m_s=9.47041202319086 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5986416399208656 cal (allowed 1.0 … None); deployment_speed_m_s=15.443507053823769 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.172095980141888 m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.165651329107247 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7253878056957552 cal (allowed 1.0 … None)
- actual-C6-5-wind0: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.172095980141888 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7365597187332107 cal (allowed 1.0 … None); deployment_speed_m_s=11.868366128247049 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=144.26136927419586 g (allowed None … 113.0); guide_departure_m_s=10.165651329107247 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7253878056957552 cal (allowed 1.0 … None); deployment_speed_m_s=13.880853963092424 m/s (allowed None … 10.0)

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
