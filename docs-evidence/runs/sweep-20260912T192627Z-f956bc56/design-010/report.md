# Rocket Workbench report

Run: `design-010`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `cf837a40bc243350939a99fc8807159c0cf26e6d8629351848a453e8c5b798e7`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 14.29 | 9.06 | 0.52 | 14.51 | 9.78 | 1.23 |
| empty-A8-3-wind2 | completed / outside configured limits | 14.20 | 9.05 | 0.04 | 15.06 | 11.40 | 1.89 |
| empty-B4-4-wind0 | completed / outside configured limits | 46.38 | 10.90 | 0.47 | 13.47 | 4.99 | 1.29 |
| empty-B4-4-wind2 | completed / outside configured limits | 45.77 | 10.89 | 0.04 | 14.26 | 4.99 | 7.88 |
| empty-C6-3-wind0 | completed / outside configured limits | 139.50 | 11.60 | 0.39 | 10.53 | 4.98 | 0.04 |
| empty-C6-3-wind2 | completed / outside configured limits | 137.71 | 11.60 | 0.15 | 10.69 | 4.98 | 38.26 |
| empty-C6-5-wind0 | completed / outside configured limits | 143.06 | 11.60 | 0.11 | 9.00 | 4.98 | 0.12 |
| empty-C6-5-wind2 | completed / outside configured limits | 141.18 | 11.60 | 0.08 | 8.52 | 4.98 | 32.02 |
| dummy-A8-3-wind0 | completed / outside configured limits | 10.30 | 7.82 | 0.90 | unavailable | 12.36 | 0.54 |
| dummy-A8-3-wind2 | completed / outside configured limits | 10.25 | 7.81 | 0.45 | unavailable | 13.06 | 0.75 |
| dummy-B4-4-wind0 | completed / outside configured limits | 35.04 | 9.60 | 0.87 | 14.42 | 5.37 | 2.38 |
| dummy-B4-4-wind2 | completed / outside configured limits | 34.27 | 9.59 | 0.46 | 15.82 | 5.37 | 1.04 |
| dummy-C6-3-wind0 | completed / outside configured limits | 116.58 | 10.28 | 0.80 | 7.01 | 5.36 | 0.05 |
| dummy-C6-3-wind2 | completed / outside configured limits | 113.47 | 10.28 | 0.54 | 8.19 | 5.36 | 17.19 |
| dummy-C6-5-wind0 | completed / outside configured limits | 117.71 | 10.28 | 0.59 | 11.56 | 5.36 | 0.53 |
| dummy-C6-5-wind2 | completed / outside configured limits | 114.57 | 10.28 | 0.54 | 13.42 | 5.36 | 4.90 |
| actual-A8-3-wind0 | completed / outside configured limits | 10.30 | 7.82 | 0.90 | unavailable | 12.36 | 0.54 |
| actual-A8-3-wind2 | completed / outside configured limits | 10.25 | 7.81 | 0.45 | unavailable | 13.06 | 0.75 |
| actual-B4-4-wind0 | completed / outside configured limits | 35.04 | 9.60 | 0.87 | 14.42 | 5.37 | 2.38 |
| actual-B4-4-wind2 | completed / outside configured limits | 34.27 | 9.59 | 0.46 | 15.82 | 5.37 | 1.04 |
| actual-C6-3-wind0 | completed / outside configured limits | 116.58 | 10.28 | 0.80 | 7.01 | 5.36 | 0.05 |
| actual-C6-3-wind2 | completed / outside configured limits | 113.47 | 10.28 | 0.54 | 8.19 | 5.36 | 17.19 |
| actual-C6-5-wind0 | completed / outside configured limits | 117.71 | 10.28 | 0.59 | 11.56 | 5.36 | 0.53 |
| actual-C6-5-wind2 | completed / outside configured limits | 114.57 | 10.28 | 0.54 | 13.42 | 5.36 | 4.90 |

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
- Measured mass and balance: Nominal 381 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=117.51136927419589 g (allowed None … 85.0); apogee_m=14.285712878308047 m (allowed 30.0 … 120.0); guide_departure_m_s=9.0577227322081 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5231799610533094 cal (allowed 1.0 … None); deployment_speed_m_s=14.50996171057995 m/s (allowed None … 10.0); landing_descent_m_s=9.776380916802193 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=117.51136927419589 g (allowed None … 85.0); apogee_m=14.20026842252072 m (allowed 30.0 … 120.0); guide_departure_m_s=9.049823291794487 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.03908600708665686 cal (allowed 1.0 … None); deployment_speed_m_s=15.064243027795309 m/s (allowed None … 10.0); landing_descent_m_s=11.39930950044891 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=120.06136927419588 g (allowed None … 99.0); guide_departure_m_s=10.898728815317362 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.4734527661881305 cal (allowed 1.0 … None); deployment_speed_m_s=13.468349606428909 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=120.06136927419588 g (allowed None … 99.0); guide_departure_m_s=10.890797931803153 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.04244693891971796 cal (allowed 1.0 … None); deployment_speed_m_s=14.256461514937053 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=124.26136927419589 g (allowed None … 113.0); apogee_m=139.49879575979386 m (allowed 30.0 … 120.0); guide_departure_m_s=11.602905511848746 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.387318772941912 cal (allowed 1.0 … None); deployment_speed_m_s=10.533614776809776 m/s (allowed None … 10.0)
- empty-C6-3-wind2: launch_mass_g=124.26136927419589 g (allowed None … 113.0); apogee_m=137.71004473961966 m (allowed 30.0 … 120.0); guide_departure_m_s=11.595340637505547 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.15460649559849746 cal (allowed 1.0 … None); deployment_speed_m_s=10.691698122453102 m/s (allowed None … 10.0)
- empty-C6-5-wind0: launch_mass_g=124.26136927419589 g (allowed None … 113.0); apogee_m=143.0558837589687 m (allowed 30.0 … 120.0); guide_departure_m_s=11.602905511848746 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.11385872701810298 cal (allowed 1.0 … None)
- empty-C6-5-wind2: launch_mass_g=124.26136927419589 g (allowed None … 113.0); apogee_m=141.18019913411405 m (allowed 30.0 … 120.0); guide_departure_m_s=11.595340637505547 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.07978720250318953 cal (allowed 1.0 … None)
- dummy-A8-3-wind0: launch_mass_g=135.51136927419589 g (allowed None … 85.0); apogee_m=10.304855972036702 m (allowed 30.0 … 120.0); guide_departure_m_s=7.818893337497441 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9010818470623249 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.360096937048542 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=135.51136927419589 g (allowed None … 85.0); apogee_m=10.245397906652958 m (allowed 30.0 … 120.0); guide_departure_m_s=7.811967251950935 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.45394555543161774 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=13.0629211026684 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=138.06136927419587 g (allowed None … 99.0); guide_departure_m_s=9.59986812252156 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8715031862718765 cal (allowed 1.0 … None); deployment_speed_m_s=14.422165526369241 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=138.06136927419587 g (allowed None … 99.0); guide_departure_m_s=9.592824560865202 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.4584697206289515 cal (allowed 1.0 … None); deployment_speed_m_s=15.820222518212699 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.282535032491102 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7992288657963099 cal (allowed 1.0 … None)
- dummy-C6-3-wind2: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.275964010557724 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5449534117552509 cal (allowed 1.0 … None)
- dummy-C6-5-wind0: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.282535032491102 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5897578521910132 cal (allowed 1.0 … None); deployment_speed_m_s=11.560016195008041 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.275964010557724 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5449534117552509 cal (allowed 1.0 … None); deployment_speed_m_s=13.41878551978765 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=135.51136927419589 g (allowed None … 85.0); apogee_m=10.304855972036702 m (allowed 30.0 … 120.0); guide_departure_m_s=7.818893337497441 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9010818470623249 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.360096937048542 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=135.51136927419589 g (allowed None … 85.0); apogee_m=10.245397906652958 m (allowed 30.0 … 120.0); guide_departure_m_s=7.811967251950935 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.45394555543161774 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=13.0629211026684 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=138.06136927419587 g (allowed None … 99.0); guide_departure_m_s=9.59986812252156 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8715031862718765 cal (allowed 1.0 … None); deployment_speed_m_s=14.422165526369241 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=138.06136927419587 g (allowed None … 99.0); guide_departure_m_s=9.592824560865202 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.45846972062895286 cal (allowed 1.0 … None); deployment_speed_m_s=15.820222518212693 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.282535032491102 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7992288657963099 cal (allowed 1.0 … None)
- actual-C6-3-wind2: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.275964010557724 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5449534117552509 cal (allowed 1.0 … None)
- actual-C6-5-wind0: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.282535032491102 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5897578521910145 cal (allowed 1.0 … None); deployment_speed_m_s=11.560016195008041 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=142.26136927419589 g (allowed None … 113.0); guide_departure_m_s=10.275964010557724 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5449534117552509 cal (allowed 1.0 … None); deployment_speed_m_s=13.418785519787683 m/s (allowed None … 10.0)

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
