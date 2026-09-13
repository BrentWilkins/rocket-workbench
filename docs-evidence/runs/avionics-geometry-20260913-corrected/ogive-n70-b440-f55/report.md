# Rocket Workbench report

Run: `ogive-n70-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `8493bc486317589d071f3bcdfacd1c90d294cf52e612a540adcb1f49d1a2a92a`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.67 |      6.40 |           2.52 | unavailable |       10.58 |    0.28 |            5.17 |             6.17 |              8.01 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.64 |      6.39 |           1.19 | unavailable |        9.86 |    0.33 |            5.17 |             6.17 |              7.99 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.61 |      8.09 |           2.31 |       16.31 |        8.78 |    0.26 |            6.95 |             7.94 |             16.44 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.82 |      8.09 |           1.33 | unavailable |       19.94 |    9.45 |            6.94 |             7.94 |             16.21 |
| empty-C6-3-wind0  | completed / outside configured limits |    84.86 |      8.87 |           2.35 |        0.90 |        4.90 |    0.04 |            7.58 |             8.58 |             33.64 |
| empty-C6-3-wind2  | completed / outside configured limits |    80.77 |      8.86 |           1.66 |        6.48 |        4.90 |    3.39 |            7.57 |             8.57 |             33.48 |
| empty-C6-5-wind0  | completed / outside configured limits |    84.86 |      8.87 |           1.84 |       12.84 |        4.90 |    0.52 |            7.58 |             8.58 |             33.64 |
| empty-C6-5-wind2  | completed / outside configured limits |    80.77 |      8.86 |           1.66 |       19.62 |        4.90 |   16.45 |            7.57 |             8.57 |             33.48 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    68.66 |     12.93 |           2.19 |        5.22 |        4.91 |    0.01 |           11.47 |            12.47 |             25.78 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    66.85 |     12.92 |           1.78 |        6.42 |        4.91 |    8.69 |           11.46 |            12.46 |             25.61 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.92 |      5.51 |           3.01 | unavailable |        9.57 |    0.13 |            4.47 |             5.47 |              6.45 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.91 |      5.51 |           1.67 | unavailable |        8.98 |    0.32 |            4.47 |             5.47 |              6.43 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.89 |      7.19 |           2.88 | unavailable |       15.71 |    0.62 |            6.06 |             7.05 |             13.60 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.21 |      7.18 |           1.97 | unavailable |       17.65 |    7.55 |            6.05 |             7.05 |             13.36 |
| dummy-C6-3-wind0  | completed / outside configured limits |    67.35 |      7.97 |           2.74 |        2.86 |        5.21 |    0.02 |            6.64 |             7.64 |             28.50 |
| dummy-C6-3-wind2  | completed / outside configured limits |    62.90 |      7.96 |           2.10 |        8.24 |        5.21 |    7.87 |            6.63 |             7.63 |             28.40 |
| dummy-C6-5-wind0  | completed / outside configured limits |    67.35 |      7.97 |           2.74 |       17.74 |        5.21 |    1.22 |            6.64 |             7.64 |             28.50 |
| dummy-C6-5-wind2  | completed / outside configured limits |    62.90 |      7.96 |           2.10 |       23.31 |        5.21 |   31.37 |            6.63 |             7.63 |             28.40 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    53.80 |     12.28 |           1.71 |        8.76 |        5.22 |    0.19 |           10.10 |            11.10 |             21.34 |
| dummy-C5-3-wind2  | completed / outside configured limits |    51.79 |     12.28 |           2.32 |       10.19 |        5.22 |    1.65 |           10.09 |            11.09 |             21.21 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.92 |      5.51 |           3.01 | unavailable |        9.57 |    0.13 |            4.47 |             5.47 |              6.45 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.91 |      5.51 |           1.67 | unavailable |        8.98 |    0.32 |            4.47 |             5.47 |              6.43 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.89 |      7.19 |           2.88 | unavailable |       15.71 |    0.62 |            6.06 |             7.05 |             13.60 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.21 |      7.18 |           1.97 | unavailable |       17.65 |    7.55 |            6.05 |             7.05 |             13.36 |
| actual-C6-3-wind0 | completed / outside configured limits |    67.35 |      7.97 |           2.74 |        2.86 |        5.21 |    0.02 |            6.64 |             7.64 |             28.50 |
| actual-C6-3-wind2 | completed / outside configured limits |    62.90 |      7.96 |           2.10 |        8.24 |        5.21 |    7.87 |            6.63 |             7.63 |             28.40 |
| actual-C6-5-wind0 | completed / outside configured limits |    67.35 |      7.97 |           2.74 |       17.74 |        5.21 |    1.22 |            6.64 |             7.64 |             28.50 |
| actual-C6-5-wind2 | completed / outside configured limits |    62.90 |      7.96 |           2.10 |       23.31 |        5.21 |   31.37 |            6.63 |             7.63 |             28.40 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    53.80 |     12.28 |           1.71 |        8.76 |        5.22 |    0.19 |           10.10 |            11.10 |             21.34 |
| actual-C5-3-wind2 | completed / outside configured limits |    51.79 |     12.28 |           2.32 |       10.19 |        5.22 |    1.65 |           10.09 |            11.09 |             21.21 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (17.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.3 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (17.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.3 m/s): "Nominal 457 mm parachute and lines"
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings

## Missing measurements / physical checks

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
- V2 saddle bond strength and adhesive mass require physical checks; saddle-specific aerodynamic drag is unresolved
- Avionics board/antenna/battery masses, stack clearances, retention, wiring and power must be measured; vendor CAD is
  not physical validation
- Static-port drilling/alignment, bulkhead and screw seals, pressure lag and aerodynamic pressure bias require
  bench/flight validation

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=162.02276769753826 g (allowed None … 85.0); apogee_m=6.668831090027761 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.39794089015058 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.57658255307398 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=162.02276769753826 g (allowed None … 85.0); apogee_m=6.6437364227045554 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.391545749703551 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.861471261426692 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=164.57276769753827 g (allowed None … 99.0); apogee_m=23.608615182569753 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.09204166435695 m/s (allowed 12.0 … None); deployment_speed_m_s=16.305414663955563
  m/s (allowed None … 10.0); landing_descent_m_s=8.777189872074098 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=164.57276769753827 g (allowed None … 99.0); apogee_m=22.820295914734007 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.085132684895688 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=19.93838570304184 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=168.77276769753826 g (allowed None … 113.0); guide_departure_m_s=8.867655077994197 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=168.77276769753826 g (allowed None … 113.0); guide_departure_m_s=8.861012885402731 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=168.77276769753826 g (allowed None … 113.0); guide_departure_m_s=8.867655077994197 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.835839453678407 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=168.77276769753826 g (allowed None … 113.0); guide_departure_m_s=8.861012885402731 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.62134887479358 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=182.67276769753826 g (allowed None … 85.0); apogee_m=4.91613030919518 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.514435040531673 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.568606507702773 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=182.67276769753826 g (allowed None … 85.0); apogee_m=4.908421965920693 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.5091293248818705 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.979822849107677 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=185.22276769753827 g (allowed None … 99.0); apogee_m=17.88757668820643 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.190107207184924 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.709791915001643 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=185.22276769753827 g (allowed None … 99.0); apogee_m=17.208759373777 m (allowed 30.0 …
  120.0); guide_departure_m_s=7.184032659933875 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=17.646438707578167 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.966700471398768 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.960845267319018 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.966700471398768 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.737867514753244 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.960845267319018 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.307270382287307 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.191465573291804 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=182.67276769753826 g (allowed None … 85.0); apogee_m=4.91613030919518 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.514435040531673 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.568606507702773 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=182.67276769753826 g (allowed None … 85.0); apogee_m=4.908421965920693 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.5091293248818705 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=8.979822849107677 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=185.22276769753827 g (allowed None … 99.0); apogee_m=17.88757668820643 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.190107207184924 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.709791915001643 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=185.22276769753827 g (allowed None … 99.0); apogee_m=17.208759373776992 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.184032659933875 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.64643870757814 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.966700471398768
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.960845267319018
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.966700471398768
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.73786751475325 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=189.42276769753826 g (allowed None … 113.0); guide_departure_m_s=7.960845267319018
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.30727038228734 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.191465573291783 m/s (allowed None … 10.0)

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is
  scenario-dependent.
- Native OpenRocket aerodynamics; configured axisymmetric nose, cylindrical sections, three flat trapezoidal fins and
  tapered collar fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in
  collar override.
- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful
  view.
- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using
  (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.
- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground
  event, not a structural impact assessment.
- Powered peaks use positive-thrust samples from liftoff strictly before first burnout, deployment, abort or ground
  contact. Missing events/data yield unavailable metrics; peak times and sample coverage are in JSON. These are sampled
  single-stage maxima, not continuous-time bounds.
- Powered acceleration is trajectory acceleration magnitude / 9.80665. Estimated load is hypot(lateral acceleration,
  vertical acceleration + local gravity) / 9.80665 at the center of mass. Coriolis correction, sensor-offset rotation,
  vibration and deployment/impact shock are excluded; this is not a per-axis IMU prediction or a hardware survival
  rating.
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
  "repository_revision": "d2e7da5d4632c052bc516be47ba0e99b609fb176"
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
