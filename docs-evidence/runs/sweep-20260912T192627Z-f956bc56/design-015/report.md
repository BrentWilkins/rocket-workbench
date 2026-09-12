# Rocket Workbench report

Run: `design-015`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `161331133c816dc68d5c6a12ab5a6d539ce6b29bd28f1ca97f691d13bd539849`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 13.62 | 8.88 | 1.16 | 11.89 | 9.80 | 1.34 |
| empty-A8-3-wind2 | completed / outside configured limits | 13.42 | 8.87 | 0.55 | 13.19 | 10.78 | 0.45 |
| empty-B4-4-wind0 | completed / outside configured limits | 43.93 | 10.77 | 1.11 | 11.51 | 6.30 | 1.70 |
| empty-B4-4-wind2 | completed / outside configured limits | 42.94 | 10.76 | 0.67 | 14.28 | 6.30 | 2.67 |
| empty-C6-3-wind0 | completed / outside configured limits | 131.64 | 11.36 | 1.03 | 8.53 | 6.28 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 128.09 | 11.35 | 0.78 | 9.39 | 6.28 | 12.56 |
| empty-C6-5-wind0 | completed / outside configured limits | 133.32 | 11.36 | 0.77 | 9.99 | 6.28 | 0.67 |
| empty-C6-5-wind2 | completed / outside configured limits | 129.69 | 11.35 | 0.78 | 12.24 | 6.28 | 1.44 |
| dummy-A8-3-wind0 | completed / outside configured limits | 9.88 | 7.68 | 1.54 | unavailable | 11.54 | 0.48 |
| dummy-A8-3-wind2 | completed / outside configured limits | 9.73 | 7.67 | 0.97 | unavailable | 11.21 | 0.56 |
| dummy-B4-4-wind0 | completed / outside configured limits | 33.46 | 9.46 | 1.39 | 15.24 | 6.77 | 0.92 |
| dummy-B4-4-wind2 | completed / outside configured limits | 32.44 | 9.45 | 1.20 | 18.56 | 6.77 | 9.28 |
| dummy-C6-3-wind0 | completed / outside configured limits | 110.36 | 10.15 | 1.45 | 5.43 | 6.75 | 0.05 |
| dummy-C6-3-wind2 | completed / outside configured limits | 105.94 | 10.15 | 1.18 | 7.77 | 6.75 | 1.23 |
| dummy-C6-5-wind0 | completed / outside configured limits | 110.75 | 10.15 | 1.25 | 11.37 | 6.75 | 0.51 |
| dummy-C6-5-wind2 | completed / outside configured limits | 106.31 | 10.15 | 1.18 | 15.68 | 6.75 | 15.76 |
| actual-A8-3-wind0 | completed / outside configured limits | 9.88 | 7.68 | 1.54 | unavailable | 11.54 | 0.48 |
| actual-A8-3-wind2 | completed / outside configured limits | 9.73 | 7.67 | 0.97 | unavailable | 11.21 | 0.56 |
| actual-B4-4-wind0 | completed / outside configured limits | 33.46 | 9.46 | 1.39 | 15.24 | 6.77 | 0.92 |
| actual-B4-4-wind2 | completed / outside configured limits | 32.44 | 9.45 | 1.20 | 18.56 | 6.77 | 9.28 |
| actual-C6-3-wind0 | completed / outside configured limits | 110.36 | 10.15 | 1.45 | 5.43 | 6.75 | 0.05 |
| actual-C6-3-wind2 | completed / outside configured limits | 105.94 | 10.15 | 1.18 | 7.77 | 6.75 | 1.23 |
| actual-C6-5-wind0 | completed / outside configured limits | 110.75 | 10.15 | 1.25 | 11.37 | 6.75 | 0.51 |
| actual-C6-5-wind2 | completed / outside configured limits | 106.31 | 10.15 | 1.18 | 15.68 | 6.75 | 15.76 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (23.7°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- actual-A8-3-wind2: Large angle of attack encountered (23.7°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=119.68392199800606 g (allowed None … 85.0); apogee_m=13.61942695482151 m (allowed 30.0 … 120.0); guide_departure_m_s=8.881289747583109 m/s (allowed 12.0 … None); deployment_speed_m_s=11.887180704613874 m/s (allowed None … 10.0); landing_descent_m_s=9.803128665974976 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=119.68392199800606 g (allowed None … 85.0); apogee_m=13.420405244736653 m (allowed 30.0 … 120.0); guide_departure_m_s=8.87207130416132 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5465383852844913 cal (allowed 1.0 … None); deployment_speed_m_s=13.19107366878719 m/s (allowed None … 10.0); landing_descent_m_s=10.777202890628299 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=122.23392199800605 g (allowed None … 99.0); guide_departure_m_s=10.769339048257645 m/s (allowed 12.0 … None); deployment_speed_m_s=11.505811154491518 m/s (allowed None … 10.0); landing_descent_m_s=6.29856109008643 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=122.23392199800605 g (allowed None … 99.0); guide_departure_m_s=10.759967956161635 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6708773143283484 cal (allowed 1.0 … None); deployment_speed_m_s=14.279680332534143 m/s (allowed None … 10.0); landing_descent_m_s=6.298489231356894 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=126.43392199800604 g (allowed None … 113.0); apogee_m=131.6350314395842 m (allowed 30.0 … 120.0); guide_departure_m_s=11.362672687207613 m/s (allowed 12.0 … None); landing_descent_m_s=6.282280167178577 m/s (allowed None … 6.0)
- empty-C6-3-wind2: launch_mass_g=126.43392199800604 g (allowed None … 113.0); apogee_m=128.09454625996685 m (allowed 30.0 … 120.0); guide_departure_m_s=11.354129602290959 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7808520013427191 cal (allowed 1.0 … None); landing_descent_m_s=6.282208616950233 m/s (allowed None … 6.0)
- empty-C6-5-wind0: launch_mass_g=126.43392199800604 g (allowed None … 113.0); apogee_m=133.3151757137507 m (allowed 30.0 … 120.0); guide_departure_m_s=11.362672687207613 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.767577887005494 cal (allowed 1.0 … None); landing_descent_m_s=6.282280130305741 m/s (allowed None … 6.0)
- empty-C6-5-wind2: launch_mass_g=126.43392199800604 g (allowed None … 113.0); apogee_m=129.68950886683723 m (allowed 30.0 … 120.0); guide_departure_m_s=11.354129602290959 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7808520013427191 cal (allowed 1.0 … None); deployment_speed_m_s=12.243499980585716 m/s (allowed None … 10.0); landing_descent_m_s=6.282208482171864 m/s (allowed None … 6.0)
- dummy-A8-3-wind0: launch_mass_g=137.683921998006 g (allowed None … 85.0); apogee_m=9.884224392334387 m (allowed 30.0 … 120.0); guide_departure_m_s=7.677598571631805 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.540364082595406 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=137.683921998006 g (allowed None … 85.0); apogee_m=9.732846487374214 m (allowed 30.0 … 120.0); guide_departure_m_s=7.669685602108623 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9660555779628733 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.210664760000753 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=140.23392199800605 g (allowed None … 99.0); guide_departure_m_s=9.460509649453446 m/s (allowed 12.0 … None); deployment_speed_m_s=15.236462541444324 m/s (allowed None … 10.0); landing_descent_m_s=6.7688005198991 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=140.23392199800605 g (allowed None … 99.0); guide_departure_m_s=9.452359045689057 m/s (allowed 12.0 … None); deployment_speed_m_s=18.559879652991377 m/s (allowed None … 10.0); landing_descent_m_s=6.767135207166057 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.154711691999442 m/s (allowed 12.0 … None); landing_descent_m_s=6.7536674746420395 m/s (allowed None … 6.0)
- dummy-C6-3-wind2: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.147106330033468 m/s (allowed 12.0 … None); landing_descent_m_s=6.753590471988324 m/s (allowed None … 6.0)
- dummy-C6-5-wind0: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.154711691999442 m/s (allowed 12.0 … None); deployment_speed_m_s=11.369780305463214 m/s (allowed None … 10.0); landing_descent_m_s=6.753667497334963 m/s (allowed None … 6.0)
- dummy-C6-5-wind2: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.147106330033468 m/s (allowed 12.0 … None); deployment_speed_m_s=15.679578178123808 m/s (allowed None … 10.0); landing_descent_m_s=6.7535904857081395 m/s (allowed None … 6.0)
- actual-A8-3-wind0: launch_mass_g=137.683921998006 g (allowed None … 85.0); apogee_m=9.884224392334387 m (allowed 30.0 … 120.0); guide_departure_m_s=7.677598571631805 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.540364082595405 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=137.683921998006 g (allowed None … 85.0); apogee_m=9.732846487374214 m (allowed 30.0 … 120.0); guide_departure_m_s=7.669685602108623 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9660555779628747 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.210664760000753 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=140.23392199800605 g (allowed None … 99.0); guide_departure_m_s=9.460509649453446 m/s (allowed 12.0 … None); deployment_speed_m_s=15.23646254144431 m/s (allowed None … 10.0); landing_descent_m_s=6.7688005198991 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=140.23392199800605 g (allowed None … 99.0); guide_departure_m_s=9.452359045689057 m/s (allowed 12.0 … None); deployment_speed_m_s=18.559879652991366 m/s (allowed None … 10.0); landing_descent_m_s=6.767135207166057 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.154711691999442 m/s (allowed 12.0 … None); landing_descent_m_s=6.7536674746420395 m/s (allowed None … 6.0)
- actual-C6-3-wind2: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.147106330033468 m/s (allowed 12.0 … None); landing_descent_m_s=6.753590471988324 m/s (allowed None … 6.0)
- actual-C6-5-wind0: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.154711691999442 m/s (allowed 12.0 … None); deployment_speed_m_s=11.369780305463212 m/s (allowed None … 10.0); landing_descent_m_s=6.753667497334963 m/s (allowed None … 6.0)
- actual-C6-5-wind2: launch_mass_g=144.43392199800604 g (allowed None … 113.0); guide_departure_m_s=10.147106330033468 m/s (allowed 12.0 … None); deployment_speed_m_s=15.679578178126468 m/s (allowed None … 10.0); landing_descent_m_s=6.7535904857081395 m/s (allowed None … 6.0)

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
