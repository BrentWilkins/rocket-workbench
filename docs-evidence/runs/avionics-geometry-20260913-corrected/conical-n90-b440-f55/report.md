# Rocket Workbench report

Run: `conical-n90-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `0ee104cc7332f2c19ad0968476e4c6e5b7044ede407bbf446b06d18de4fd322a`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.91 |      6.52 |           2.46 | unavailable |       10.70 |    0.31 |            5.26 |             6.26 |              8.21 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.88 |      6.51 |           1.12 | unavailable |        9.97 |    0.37 |            5.26 |             6.26 |              8.19 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.34 |      8.21 |           2.26 |       14.59 |        5.30 |    0.05 |            7.06 |             8.06 |             16.80 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.55 |      8.20 |           1.26 | unavailable |       20.12 |    9.64 |            7.06 |             8.06 |             16.56 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.42 |      8.98 |           2.29 |        1.12 |        4.86 |    0.04 |            7.70 |             8.70 |             34.18 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.41 |      8.97 |           1.61 |        6.31 |        4.86 |    4.79 |            7.70 |             8.70 |             34.02 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.42 |      8.98 |           1.96 |       12.31 |        4.86 |    0.81 |            7.70 |             8.70 |             34.18 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.41 |      8.97 |           1.61 |       19.28 |        4.86 |   14.54 |            7.70 |             8.70 |             34.02 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    70.15 |     13.04 |           2.07 |        4.94 |        4.87 |    0.00 |           11.65 |            12.65 |             26.24 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.38 |     13.03 |           1.66 |        6.05 |        4.87 |   10.03 |           11.64 |            12.64 |             26.07 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.08 |      5.61 |           2.95 | unavailable |        9.66 |    0.14 |            4.54 |             5.54 |              6.61 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.07 |      5.60 |           1.64 | unavailable |        9.12 |    0.32 |            4.54 |             5.54 |              6.59 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.42 |      7.29 |           2.41 | unavailable |       15.92 |    0.61 |            6.15 |             7.15 |             13.89 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.73 |      7.28 |           1.90 | unavailable |       17.85 |    7.80 |            6.15 |             7.15 |             13.65 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.76 |      8.06 |           2.62 |        2.58 |        5.18 |    0.03 |            6.74 |             7.73 |             28.96 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.36 |      8.05 |           2.06 |        7.97 |        5.18 |    6.73 |            6.73 |             7.73 |             28.86 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.76 |      8.06 |           2.62 |       17.45 |        5.18 |    1.07 |            6.74 |             7.73 |             28.96 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.36 |      8.05 |           2.06 |       22.93 |        5.18 |   29.78 |            6.73 |             7.73 |             28.86 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.06 |     12.31 |           2.02 |        8.48 |        5.18 |    0.16 |           10.24 |            11.24 |             21.74 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.08 |     12.31 |           2.28 |        9.82 |        5.18 |    0.64 |           10.23 |            11.23 |             21.60 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.08 |      5.61 |           2.95 | unavailable |        9.66 |    0.14 |            4.54 |             5.54 |              6.61 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.07 |      5.60 |           1.64 | unavailable |        9.12 |    0.32 |            4.54 |             5.54 |              6.59 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.42 |      7.29 |           2.41 | unavailable |       15.92 |    0.61 |            6.15 |             7.15 |             13.89 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.73 |      7.28 |           1.90 | unavailable |       17.85 |    7.80 |            6.15 |             7.15 |             13.65 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.76 |      8.06 |           2.62 |        2.58 |        5.18 |    0.03 |            6.74 |             7.73 |             28.96 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.36 |      8.05 |           2.06 |        7.97 |        5.18 |    6.73 |            6.73 |             7.73 |             28.86 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.76 |      8.06 |           2.62 |       17.45 |        5.18 |    1.07 |            6.74 |             7.73 |             28.96 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.36 |      8.05 |           2.06 |       22.93 |        5.18 |   29.78 |            6.73 |             7.73 |             28.86 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.06 |     12.31 |           2.02 |        8.48 |        5.18 |    0.16 |           10.24 |            11.24 |             21.74 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.08 |     12.31 |           2.28 |        9.82 |        5.18 |    0.64 |           10.23 |            11.23 |             21.60 |

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
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.9 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.9 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=159.6351400766876 g (allowed None … 85.0); apogee_m=6.913639741625834 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.518188596992774 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.699688241761494 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=159.6351400766876 g (allowed None … 85.0); apogee_m=6.883740140052394 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.5112968898173165 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.968696093735788 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=162.18514007668762 g (allowed None … 99.0); apogee_m=24.339630894067973 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.211458155414169 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.594547610898932 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=162.18514007668762 g (allowed None … 99.0); apogee_m=23.54827042607264 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.204101343010205 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=20.116607852237813 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=166.3851400766876 g (allowed None … 113.0); guide_departure_m_s=8.979306495210512 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=166.3851400766876 g (allowed None … 113.0); guide_departure_m_s=8.97226063907037 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=166.3851400766876 g (allowed None … 113.0); guide_departure_m_s=8.979306495210512 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.313065193883704 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=166.3851400766876 g (allowed None … 113.0); guide_departure_m_s=8.97226063907037 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.28077652497983 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=180.2851400766876 g (allowed None … 85.0); apogee_m=5.08419969231567 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.606203222662822 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=9.664294730898146 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=180.2851400766876 g (allowed None … 85.0); apogee_m=5.0744850451022225 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.6005644612869725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.118753838964526 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=182.8351400766876 g (allowed None … 99.0); apogee_m=18.423222703855345 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.289963839726306 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.921199617672954 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=182.8351400766876 g (allowed None … 99.0); apogee_m=17.72948476767651 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.283491289203111 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.85454878009455 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.060683916085129 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.054472256358764 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.060683916085129 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.454683499061687 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.054472256358764 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.929804945277404 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=180.2851400766876 g (allowed None … 85.0); apogee_m=5.08419969231567 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.606203222662822 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.664294730898146 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=180.2851400766876 g (allowed None … 85.0); apogee_m=5.0744850451022225 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.6005644612869725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=9.118753838964526 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=182.8351400766876 g (allowed None … 99.0); apogee_m=18.423222703855345 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.289963839726306 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.921199617672984 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=182.8351400766876 g (allowed None … 99.0); apogee_m=17.72948476767651 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.283491289203111 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.854548780094497 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.060683916085129 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.054472256358764 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.060683916085129 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.454683499061698 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=187.0351400766876 g (allowed None … 113.0); guide_departure_m_s=8.054472256358764 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.92980494527783 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs

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
