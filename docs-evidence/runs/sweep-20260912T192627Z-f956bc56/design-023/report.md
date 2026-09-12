# Rocket Workbench report

Run: `design-023`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `0f253b033e9e6506e76cfc9daa6fbef442b99430e5364fbc0e63eee32fada19d`

## Cases

| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m |
|---|---|---:|---:|---:|---:|---:|---:|
| empty-A8-3-wind0 | completed / outside configured limits | 12.07 | 8.42 | 1.18 | unavailable | 12.34 | 1.05 |
| empty-A8-3-wind2 | completed / outside configured limits | 11.95 | 8.41 | 0.43 | unavailable | 13.26 | 0.97 |
| empty-B4-4-wind0 | completed / outside configured limits | 39.88 | 10.22 | 0.88 | 13.18 | 4.32 | 1.96 |
| empty-B4-4-wind2 | completed / outside configured limits | 39.01 | 10.21 | 0.47 | 13.96 | 4.32 | 3.05 |
| empty-C6-3-wind0 | completed / outside configured limits | 124.57 | 10.92 | 1.05 | 7.89 | 4.31 | 0.05 |
| empty-C6-3-wind2 | completed / outside configured limits | 121.51 | 10.91 | 0.70 | 8.78 | 4.31 | 31.88 |
| empty-C6-5-wind0 | completed / outside configured limits | 126.43 | 10.92 | 0.99 | 10.74 | 4.31 | 0.48 |
| empty-C6-5-wind2 | completed / outside configured limits | 123.24 | 10.91 | 0.70 | 12.46 | 4.31 | 19.81 |
| dummy-A8-3-wind0 | completed / outside configured limits | 8.84 | 7.29 | 1.66 | unavailable | 11.36 | 0.44 |
| dummy-A8-3-wind2 | completed / outside configured limits | 8.77 | 7.29 | 0.89 | unavailable | 10.98 | 0.22 |
| dummy-B4-4-wind0 | completed / outside configured limits | 30.44 | 9.06 | 1.49 | 14.27 | 4.63 | 0.14 |
| dummy-B4-4-wind2 | completed / outside configured limits | 29.55 | 9.05 | 1.04 | 18.99 | 4.63 | 7.59 |
| dummy-C6-3-wind0 | completed / outside configured limits | 103.81 | 9.78 | 1.51 | 4.52 | 4.62 | 0.04 |
| dummy-C6-3-wind2 | completed / outside configured limits | 99.90 | 9.78 | 1.13 | 7.08 | 4.62 | 14.84 |
| dummy-C6-5-wind0 | completed / outside configured limits | 104.18 | 9.78 | 1.05 | 11.78 | 4.62 | 0.74 |
| dummy-C6-5-wind2 | completed / outside configured limits | 100.23 | 9.78 | 1.13 | 16.28 | 4.62 | 1.95 |
| actual-A8-3-wind0 | completed / outside configured limits | 8.84 | 7.29 | 1.66 | unavailable | 11.36 | 0.44 |
| actual-A8-3-wind2 | completed / outside configured limits | 8.77 | 7.29 | 0.89 | unavailable | 10.98 | 0.22 |
| actual-B4-4-wind0 | completed / outside configured limits | 30.44 | 9.06 | 1.49 | 14.27 | 4.63 | 0.14 |
| actual-B4-4-wind2 | completed / outside configured limits | 29.55 | 9.05 | 1.04 | 18.99 | 4.63 | 7.59 |
| actual-C6-3-wind0 | completed / outside configured limits | 103.81 | 9.78 | 1.51 | 4.52 | 4.62 | 0.04 |
| actual-C6-3-wind2 | completed / outside configured limits | 99.90 | 9.78 | 1.13 | 7.08 | 4.62 | 14.84 |
| actual-C6-5-wind0 | completed / outside configured limits | 104.18 | 9.78 | 1.05 | 11.78 | 4.62 | 0.74 |
| actual-C6-5-wind2 | completed / outside configured limits | 100.23 | 9.78 | 1.13 | 16.28 | 4.62 | 1.95 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
- empty-A8-3-wind2: Large angle of attack encountered (18.7°); Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery device deployment
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
- Measured mass and balance: Nominal 457 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=126.3867882366058 g (allowed None … 85.0); apogee_m=12.069801718747952 m (allowed 30.0 … 120.0); guide_departure_m_s=8.416257831697893 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=12.336944708355029 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=126.3867882366058 g (allowed None … 85.0); apogee_m=11.946776357406616 m (allowed 30.0 … 120.0); guide_departure_m_s=8.407882976430438 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.4338930186911289 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=13.256145825745953 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=128.9367882366058 g (allowed None … 99.0); guide_departure_m_s=10.21582868027794 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8772131149527269 cal (allowed 1.0 … None); deployment_speed_m_s=13.17939624113594 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=128.9367882366058 g (allowed None … 99.0); guide_departure_m_s=10.20749335785235 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.47037482074766634 cal (allowed 1.0 … None); deployment_speed_m_s=13.95609043194522 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=133.1367882366058 g (allowed None … 113.0); apogee_m=124.56556452006954 m (allowed 30.0 … 120.0); guide_departure_m_s=10.92267011618245 m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=133.1367882366058 g (allowed None … 113.0); apogee_m=121.50559542644352 m (allowed 30.0 … 120.0); guide_departure_m_s=10.91478624996427 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7009532971192936 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=133.1367882366058 g (allowed None … 113.0); apogee_m=126.43367974014875 m (allowed 30.0 … 120.0); guide_departure_m_s=10.92267011618245 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9876869357595484 cal (allowed 1.0 … None); deployment_speed_m_s=10.741015164964962 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=133.1367882366058 g (allowed None … 113.0); apogee_m=123.24411898713694 m (allowed 30.0 … 120.0); guide_departure_m_s=10.91478624996427 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.7009532971192936 cal (allowed 1.0 … None); deployment_speed_m_s=12.460265614884639 m/s (allowed None … 10.0)
- dummy-A8-3-wind0: launch_mass_g=144.38678823660578 g (allowed None … 85.0); apogee_m=8.84266192581769 m (allowed 30.0 … 120.0); guide_departure_m_s=7.2945533124810105 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.358739720667597 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=144.38678823660578 g (allowed None … 85.0); apogee_m=8.770727732368034 m (allowed 30.0 … 120.0); guide_departure_m_s=7.287443334582304 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8938963679453366 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.981629622208182 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=146.93678823660576 g (allowed None … 99.0); guide_departure_m_s=9.057721085327389 m/s (allowed 12.0 … None); deployment_speed_m_s=14.273480238708263 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=146.93678823660576 g (allowed None … 99.0); apogee_m=29.549009825465305 m (allowed 30.0 … 120.0); guide_departure_m_s=9.050288374134784 m/s (allowed 12.0 … None); deployment_speed_m_s=18.989144045130164 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.783923325974802 m/s (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.776915513211437 m/s (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.783923325974802 m/s (allowed 12.0 … None); deployment_speed_m_s=11.778735354777943 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.776915513211437 m/s (allowed 12.0 … None); deployment_speed_m_s=16.275297030851217 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=144.38678823660578 g (allowed None … 85.0); apogee_m=8.84266192581769 m (allowed 30.0 … 120.0); guide_departure_m_s=7.2945533124810105 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=11.358739720667597 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=144.38678823660578 g (allowed None … 85.0); apogee_m=8.770727732368034 m (allowed 30.0 … 120.0); guide_departure_m_s=7.287443334582304 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8938963679453352 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=10.981629622208182 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=146.93678823660576 g (allowed None … 99.0); guide_departure_m_s=9.057721085327389 m/s (allowed 12.0 … None); deployment_speed_m_s=14.273480238708261 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=146.93678823660576 g (allowed None … 99.0); apogee_m=29.549009825465255 m (allowed 30.0 … 120.0); guide_departure_m_s=9.050288374134784 m/s (allowed 12.0 … None); deployment_speed_m_s=18.989144045130306 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.783923325974802 m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.776915513211437 m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.783923325974802 m/s (allowed 12.0 … None); deployment_speed_m_s=11.778735354777941 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=151.13678823660578 g (allowed None … 113.0); guide_departure_m_s=9.776915513211437 m/s (allowed 12.0 … None); deployment_speed_m_s=16.275297030851192 m/s (allowed None … 10.0)

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
