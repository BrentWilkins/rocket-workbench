# Rocket Workbench report

Run: `design-018`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `f013dd94c3cf5b9d77222d5c17374db0a78b5a464182a58cc875b1daaacdff2a`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 14.64 | 9.15 | 0.73 | 13.95 | 9.55 | 1.37 |
| empty-A8-3-wind2 | completed / outside configured limits | 14.55 | 9.15 | 0.11 | 14.85 | 10.78 | 1.96 |
| empty-B4-4-wind0 | completed / outside configured limits | 47.23 | 11.01 | 0.42 | 13.04 | 6.20 | 1.51 |
| empty-B4-4-wind2 | completed / outside configured limits | 46.59 | 11.01 | 0.11 | 13.97 | 6.20 | 5.17 |
| empty-C6-3-wind0 | completed / outside configured limits | 140.85 | 11.67 | 0.57 | 10.49 | 6.19 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 138.89 | 11.66 | 0.27 | 10.67 | 6.19 | 26.30 |
| empty-C6-5-wind0 | completed / outside configured limits | 143.87 | 11.67 | 0.46 | 9.05 | 6.19 | 0.16 |
| empty-C6-5-wind2 | completed / outside configured limits | 141.87 | 11.66 | 0.17 | 8.25 | 6.19 | 20.10 |
| dummy-A8-3-wind0 | completed / outside configured limits | 10.54 | 7.90 | 1.22 | unavailable | 12.24 | 0.57 |
| dummy-A8-3-wind2 | completed / outside configured limits | 10.48 | 7.89 | 0.59 | unavailable | 12.77 | 0.89 |
| dummy-B4-4-wind0 | completed / outside configured limits | 35.69 | 9.72 | 1.15 | 13.02 | 6.68 | 2.40 |
| dummy-B4-4-wind2 | completed / outside configured limits | 34.93 | 9.71 | 0.60 | 14.64 | 6.68 | 1.85 |
| dummy-C6-3-wind0 | completed / outside configured limits | 117.82 | 10.40 | 1.05 | 7.08 | 6.66 | 0.05 |
| dummy-C6-3-wind2 | completed / outside configured limits | 114.74 | 10.40 | 0.72 | 8.17 | 6.66 | 8.61 |
| dummy-C6-5-wind0 | completed / outside configured limits | 118.74 | 10.40 | 1.03 | 11.54 | 6.66 | 0.66 |
| dummy-C6-5-wind2 | completed / outside configured limits | 115.68 | 10.40 | 0.72 | 13.18 | 6.66 | 2.26 |
| actual-A8-3-wind0 | completed / outside configured limits | 10.54 | 7.90 | 1.22 | unavailable | 12.24 | 0.57 |
| actual-A8-3-wind2 | completed / outside configured limits | 10.48 | 7.89 | 0.59 | unavailable | 12.77 | 0.89 |
| actual-B4-4-wind0 | completed / outside configured limits | 35.69 | 9.72 | 1.15 | 13.02 | 6.68 | 2.40 |
| actual-B4-4-wind2 | completed / outside configured limits | 34.93 | 9.71 | 0.60 | 14.64 | 6.68 | 1.85 |
| actual-C6-3-wind0 | completed / outside configured limits | 117.82 | 10.40 | 1.05 | 7.08 | 6.66 | 0.05 |
| actual-C6-3-wind2 | completed / outside configured limits | 114.74 | 10.40 | 0.72 | 8.17 | 6.66 | 8.61 |
| actual-C6-5-wind0 | completed / outside configured limits | 118.74 | 10.40 | 1.03 | 11.54 | 6.66 | 0.66 |
| actual-C6-5-wind2 | completed / outside configured limits | 115.68 | 10.40 | 0.72 | 13.18 | 6.66 | 2.26 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: no engine warnings
- empty-A8-3-wind2: no engine warnings
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
- Measured mass and balance: Nominal 305 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=116.14866032498867 g (allowed None … 85.0); apogee_m=14.64440793865788 m (allowed 30.0 … 120.0); guide_departure_m_s=9.154131226821498 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.731557790823719 cal (allowed 1.0 … None); deployment_speed_m_s=13.94676326887392 m/s (allowed None … 10.0); landing_descent_m_s=9.545912829103768 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=116.14866032498867 g (allowed None … 85.0); apogee_m=14.547401382282095 m (allowed 30.0 … 120.0); guide_departure_m_s=9.14578473466578 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.111824911980636 cal (allowed 1.0 … None); deployment_speed_m_s=14.849155762768008 m/s (allowed None … 10.0); landing_descent_m_s=10.77743662443988 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=118.69866032498865 g (allowed None … 99.0); guide_departure_m_s=11.014408348556973 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.4235120791252737 cal (allowed 1.0 … None); deployment_speed_m_s=13.042870696656626 m/s (allowed None … 10.0); landing_descent_m_s=6.202017308204712 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=118.69866032498865 g (allowed None … 99.0); guide_departure_m_s=11.00612027329066 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.11368333272805302 cal (allowed 1.0 … None); deployment_speed_m_s=13.96956760948108 m/s (allowed None … 10.0); landing_descent_m_s=6.201946544260916 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=122.89866032498865 g (allowed None … 113.0); apogee_m=140.85176473756636 m (allowed 30.0 … 120.0); guide_departure_m_s=11.670856260410304 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5686602186514161 cal (allowed 1.0 … None); deployment_speed_m_s=10.48924689320095 m/s (allowed None … 10.0); landing_descent_m_s=6.18548253804513 m/s (allowed None … 6.0)
- empty-C6-3-wind2: launch_mass_g=122.89866032498865 g (allowed None … 113.0); apogee_m=138.89306245213186 m (allowed 30.0 … 120.0); guide_departure_m_s=11.663086282341425 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.2665692447272477 cal (allowed 1.0 … None); deployment_speed_m_s=10.667677338010122 m/s (allowed None … 10.0); landing_descent_m_s=6.185411982750022 m/s (allowed None … 6.0)
- empty-C6-5-wind0: launch_mass_g=122.89866032498865 g (allowed None … 113.0); apogee_m=143.8668604747416 m (allowed 30.0 … 120.0); guide_departure_m_s=11.670856260410304 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.45728190020509235 cal (allowed 1.0 … None); landing_descent_m_s=6.185482521906761 m/s (allowed None … 6.0)
- empty-C6-5-wind2: launch_mass_g=122.89866032498865 g (allowed None … 113.0); apogee_m=141.86946231959183 m (allowed 30.0 … 120.0); guide_departure_m_s=11.663086282341425 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.1701525310651688 cal (allowed 1.0 … None); landing_descent_m_s=6.1854120161392405 m/s (allowed None … 6.0)
- dummy-A8-3-wind0: launch_mass_g=134.14866032498864 g (allowed None … 85.0); apogee_m=10.543867208624638 m (allowed 30.0 … 120.0); guide_departure_m_s=7.896942610652079 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.242479103186861 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=134.14866032498864 g (allowed None … 85.0); apogee_m=10.48171447139457 m (allowed 30.0 … 120.0); guide_departure_m_s=7.889761350931691 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5930324990755812 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.771780591367495 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=136.69866032498865 g (allowed None … 99.0); guide_departure_m_s=9.715679658022912 m/s (allowed 12.0 … None); deployment_speed_m_s=13.020572387876499 m/s (allowed None … 10.0); landing_descent_m_s=6.679065823657938 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=136.69866032498865 g (allowed None … 99.0); guide_departure_m_s=9.708261515079913 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6001936771242905 cal (allowed 1.0 … None); deployment_speed_m_s=14.636242773922731 m/s (allowed None … 10.0); landing_descent_m_s=6.678990394238424 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.402853355866595 m/s (allowed 12.0 … None); landing_descent_m_s=6.663715036254858 m/s (allowed None … 6.0)
- dummy-C6-3-wind2: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.395943829874504 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7249998026618771 cal (allowed 1.0 … None); landing_descent_m_s=6.663639016093933 m/s (allowed None … 6.0)
- dummy-C6-5-wind0: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.402853355866595 m/s (allowed 12.0 … None); deployment_speed_m_s=11.535517347799692 m/s (allowed None … 10.0); landing_descent_m_s=6.663715081278648 m/s (allowed None … 6.0)
- dummy-C6-5-wind2: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.395943829874504 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7249998026618771 cal (allowed 1.0 … None); deployment_speed_m_s=13.180416786090772 m/s (allowed None … 10.0); landing_descent_m_s=6.663639101530316 m/s (allowed None … 6.0)
- actual-A8-3-wind0: launch_mass_g=134.14866032498864 g (allowed None … 85.0); apogee_m=10.543867208624638 m (allowed 30.0 … 120.0); guide_departure_m_s=7.896942610652079 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.242479103186861 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=134.14866032498864 g (allowed None … 85.0); apogee_m=10.48171447139457 m (allowed 30.0 … 120.0); guide_departure_m_s=7.889761350931691 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5930324990755812 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.771780591367495 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=136.69866032498865 g (allowed None … 99.0); guide_departure_m_s=9.715679658022912 m/s (allowed 12.0 … None); deployment_speed_m_s=13.020572387876497 m/s (allowed None … 10.0); landing_descent_m_s=6.679065823657938 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=136.69866032498865 g (allowed None … 99.0); guide_departure_m_s=9.708261515079913 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6001936771242665 cal (allowed 1.0 … None); deployment_speed_m_s=14.63624277392366 m/s (allowed None … 10.0); landing_descent_m_s=6.678990394238424 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.402853355866595 m/s (allowed 12.0 … None); landing_descent_m_s=6.663715036254858 m/s (allowed None … 6.0)
- actual-C6-3-wind2: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.395943829874504 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7249998026618771 cal (allowed 1.0 … None); landing_descent_m_s=6.663639016093933 m/s (allowed None … 6.0)
- actual-C6-5-wind0: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.402853355866595 m/s (allowed 12.0 … None); deployment_speed_m_s=11.535517347799695 m/s (allowed None … 10.0); landing_descent_m_s=6.663715081278648 m/s (allowed None … 6.0)
- actual-C6-5-wind2: launch_mass_g=140.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.395943829874504 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7249998026618771 cal (allowed 1.0 … None); deployment_speed_m_s=13.180416786090948 m/s (allowed None … 10.0); landing_descent_m_s=6.663639101530316 m/s (allowed None … 6.0)

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
