# Rocket Workbench report

Run: `design-021`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `2a6255aa67072281e3693f1baf207efed8e19bc0a7783fdbbab5d2420eb23a9f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    13.85 |      8.96 |           1.12 |       12.75 |       10.39 |    1.48 |
| empty-A8-3-wind2  | completed / outside configured limits |    13.69 |      8.95 |           0.43 |       13.96 |       12.30 |    1.35 |
| empty-B4-4-wind0  | completed / outside configured limits |    44.75 |     10.79 |           0.88 |       12.23 |        6.28 |    1.92 |
| empty-B4-4-wind2  | completed / outside configured limits |    43.88 |     10.78 |           0.47 |       12.23 |        6.28 |    0.99 |
| empty-C6-3-wind0  | completed / outside configured limits |   134.41 |     11.45 |           1.04 |        9.18 |        6.26 |    0.05 |
| empty-C6-3-wind2  | completed / outside configured limits |   131.44 |     11.44 |           0.70 |        9.76 |        6.26 |   16.88 |
| empty-C6-5-wind0  | completed / outside configured limits |   136.48 |     11.45 |           0.91 |        9.94 |        6.26 |    0.45 |
| empty-C6-5-wind2  | completed / outside configured limits |   133.45 |     11.44 |           0.70 |       11.04 |        6.26 |    7.26 |
| dummy-A8-3-wind0  | completed / outside configured limits |    10.03 |      7.74 |           1.63 | unavailable |       11.50 |    0.57 |
| dummy-A8-3-wind2  | completed / outside configured limits |     9.93 |      7.73 |           0.92 | unavailable |       11.33 |    0.27 |
| dummy-B4-4-wind0  | completed / outside configured limits |    34.00 |      9.53 |           1.51 |       13.51 |        6.75 |    0.16 |
| dummy-B4-4-wind2  | completed / outside configured limits |    33.07 |      9.52 |           1.04 |       17.52 |        6.75 |    7.88 |
| dummy-C6-3-wind0  | completed / outside configured limits |   112.51 |     10.22 |           1.52 |        5.95 |        6.73 |    0.05 |
| dummy-C6-3-wind2  | completed / outside configured limits |   108.68 |     10.21 |           1.15 |        7.75 |        6.73 |    2.48 |
| dummy-C6-5-wind0  | completed / outside configured limits |   113.04 |     10.22 |           1.36 |       11.33 |        6.73 |    0.89 |
| dummy-C6-5-wind2  | completed / outside configured limits |   109.22 |     10.21 |           1.15 |       14.86 |        6.73 |   10.68 |
| actual-A8-3-wind0 | completed / outside configured limits |    10.03 |      7.74 |           1.63 | unavailable |       11.50 |    0.57 |
| actual-A8-3-wind2 | completed / outside configured limits |     9.93 |      7.73 |           0.92 | unavailable |       11.33 |    0.27 |
| actual-B4-4-wind0 | completed / outside configured limits |    34.00 |      9.53 |           1.51 |       13.51 |        6.75 |    0.16 |
| actual-B4-4-wind2 | completed / outside configured limits |    33.07 |      9.52 |           1.04 |       17.52 |        6.75 |    7.88 |
| actual-C6-3-wind0 | completed / outside configured limits |   112.51 |     10.22 |           1.52 |        5.95 |        6.73 |    0.05 |
| actual-C6-3-wind2 | completed / outside configured limits |   108.68 |     10.21 |           1.15 |        7.75 |        6.73 |    2.48 |
| actual-C6-5-wind0 | completed / outside configured limits |   113.04 |     10.22 |           1.36 |       11.33 |        6.73 |    0.89 |
| actual-C6-5-wind2 | completed / outside configured limits |   109.22 |     10.21 |           1.15 |       14.86 |        6.73 |   10.68 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: no engine warnings
- empty-A8-3-wind2: Large angle of attack encountered (20.8°)
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
- Measured mass and balance: Nominal 305 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=118.91628030862944 g (allowed None … 85.0); apogee_m=13.847690650486854 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.955535463430305 m/s (allowed 12.0 … None); deployment_speed_m_s=12.75342036553257
  m/s (allowed None … 10.0); landing_descent_m_s=10.394153838364774 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=118.91628030862944 g (allowed None … 85.0); apogee_m=13.693060027646643 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.946620357337896 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.4290373589067397 cal (allowed 1.0 … None); deployment_speed_m_s=13.963404664504028 m/s
  (allowed None … 10.0); landing_descent_m_s=12.30251447723629 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=121.46628030862944 g (allowed None … 99.0); guide_departure_m_s=10.79212253905011 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8848898155211905 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.232216400630866 m/s (allowed None … 10.0); landing_descent_m_s=6.277723797980269 m/s (allowed
  None … 6.0)
- empty-B4-4-wind2: launch_mass_g=121.46628030862944 g (allowed None … 99.0); guide_departure_m_s=10.783306190238823 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.4747192870314462 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.231442392850308 m/s (allowed None … 10.0); landing_descent_m_s=6.277652199877205 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=125.66628030862945 g (allowed None … 113.0); apogee_m=134.40681883403144 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.446444603576376 m/s (allowed 12.0 … None); landing_descent_m_s=6.261388793814316
  m/s (allowed None … 6.0)
- empty-C6-3-wind2: launch_mass_g=125.66628030862945 g (allowed None … 113.0); apogee_m=131.44095741069938 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.438212599929653 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6988180217626746 cal (allowed 1.0 … None); landing_descent_m_s=6.261317362540031 m/s
  (allowed None … 6.0)
- empty-C6-5-wind0: launch_mass_g=125.66628030862945 g (allowed None … 113.0); apogee_m=136.4794399109807 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.446444603576376 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9102544805399354 cal (allowed 1.0 … None); landing_descent_m_s=6.261388841886851 m/s
  (allowed None … 6.0)
- empty-C6-5-wind2: launch_mass_g=125.66628030862945 g (allowed None … 113.0); apogee_m=133.45099538608468 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.438212599929653 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6988180217626746 cal (allowed 1.0 … None); deployment_speed_m_s=11.040004208099354 m/s
  (allowed None … 10.0); landing_descent_m_s=6.261317340173698 m/s (allowed None … 6.0)
- dummy-A8-3-wind0: launch_mass_g=136.91628030862944 g (allowed None … 85.0); apogee_m=10.029025816088902 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.736092689494434 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.499088004202079 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=136.91628030862944 g (allowed None … 85.0); apogee_m=9.925488977525312 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.72844247670104 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.918788384701706 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=11.328030324741261 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=139.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.525179230326561 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.513242460566174 m/s (allowed None … 10.0);
  landing_descent_m_s=6.749423377627699 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=139.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.517327908889156 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.523161388590708 m/s (allowed None … 10.0);
  landing_descent_m_s=6.748931458489929 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.222050889182078
  m/s (allowed 12.0 … None); landing_descent_m_s=6.734237353741285 m/s (allowed None … 6.0)
- dummy-C6-3-wind2: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.214717633309009
  m/s (allowed 12.0 … None); landing_descent_m_s=6.734160621485819 m/s (allowed None … 6.0)
- dummy-C6-5-wind0: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.222050889182078
  m/s (allowed 12.0 … None); deployment_speed_m_s=11.331293780821605 m/s (allowed None … 10.0);
  landing_descent_m_s=6.73423734052822 m/s (allowed None … 6.0)
- dummy-C6-5-wind2: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.214717633309009
  m/s (allowed 12.0 … None); deployment_speed_m_s=14.856772469348188 m/s (allowed None … 10.0);
  landing_descent_m_s=6.734160544149599 m/s (allowed None … 6.0)
- actual-A8-3-wind0: launch_mass_g=136.91628030862944 g (allowed None … 85.0); apogee_m=10.029025816088902 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.736092689494434 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.49908800420208 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=136.91628030862944 g (allowed None … 85.0); apogee_m=9.925488977525312 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.72844247670104 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9187883847017047 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.328030324741263 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=139.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.525179230326561 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.513242460566174 m/s (allowed None … 10.0);
  landing_descent_m_s=6.749423377627699 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=139.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.517327908889156 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.523161388590882 m/s (allowed None … 10.0);
  landing_descent_m_s=6.748931458489929 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.222050889182078
  m/s (allowed 12.0 … None); landing_descent_m_s=6.734237353741285 m/s (allowed None … 6.0)
- actual-C6-3-wind2: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.214717633309009
  m/s (allowed 12.0 … None); landing_descent_m_s=6.734160621485819 m/s (allowed None … 6.0)
- actual-C6-5-wind0: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.222050889182078
  m/s (allowed 12.0 … None); deployment_speed_m_s=11.331293780821603 m/s (allowed None … 10.0);
  landing_descent_m_s=6.73423734052822 m/s (allowed None … 6.0)
- actual-C6-5-wind2: launch_mass_g=143.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.214717633309009
  m/s (allowed 12.0 … None); deployment_speed_m_s=14.856772469348225 m/s (allowed None … 10.0);
  landing_descent_m_s=6.734160544149599 m/s (allowed None … 6.0)

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
