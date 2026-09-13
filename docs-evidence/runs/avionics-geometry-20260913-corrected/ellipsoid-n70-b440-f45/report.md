# Rocket Workbench report

Run: `ellipsoid-n70-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `cdae7c61216dc5efd185e7cbbbcb9299a05a5d11d17382403909811a79acdb5a`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.76 |      6.45 |           2.17 | unavailable |       10.94 |    0.23 |            5.20 |             6.20 |              8.08 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.74 |      6.44 |           0.87 | unavailable |       10.10 |    0.65 |            5.20 |             6.20 |              8.06 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.97 |      8.14 |           1.59 |       13.90 |        5.68 |    3.06 |            6.99 |             7.98 |             16.60 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.35 |      8.14 |           0.94 |       18.37 |       11.41 |    9.13 |            6.98 |             7.98 |             16.39 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.65 |      8.92 |           2.00 |        1.38 |        4.89 |    0.04 |            7.62 |             8.62 |             34.02 |
| empty-C6-3-wind2  | completed / outside configured limits |    83.18 |      8.92 |           1.28 |        5.90 |        4.89 |    7.21 |            7.62 |             8.62 |             33.87 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.66 |      8.92 |           1.30 |       12.32 |        4.89 |    1.63 |            7.62 |             8.62 |             34.02 |
| empty-C6-5-wind2  | completed / outside configured limits |    83.18 |      8.92 |           1.28 |       18.83 |        4.89 |   10.89 |            7.62 |             8.62 |             33.87 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    69.99 |     13.00 |           1.79 |        4.84 |        4.90 |    0.01 |           11.53 |            12.53 |             26.13 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.31 |     13.00 |           1.23 |        5.82 |        4.90 |   10.33 |           11.52 |            12.52 |             25.97 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.98 |      5.54 |           2.64 | unavailable |        9.70 |    0.10 |            4.49 |             5.49 |              6.50 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.97 |      5.54 |           1.34 | unavailable |        9.10 |    0.46 |            4.49 |             5.49 |              6.49 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.12 |      7.21 |           2.58 | unavailable |       15.34 |    0.58 |            6.09 |             7.09 |             13.72 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.61 |      7.20 |           1.38 | unavailable |       17.45 |    6.33 |            6.09 |             7.09 |             13.53 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.54 |      8.01 |           2.19 |        2.50 |        5.20 |    0.03 |            6.67 |             7.67 |             28.79 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.65 |      8.01 |           1.70 |        7.49 |        5.20 |    4.63 |            6.67 |             7.67 |             28.66 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.54 |      8.01 |           2.19 |       16.58 |        5.20 |    0.72 |            6.67 |             7.67 |             28.79 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.65 |      8.01 |           1.70 |       22.78 |        5.20 |   26.77 |            6.67 |             7.67 |             28.66 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.68 |     12.19 |           2.37 |        8.54 |        5.21 |    0.12 |           10.15 |            11.15 |             21.60 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    52.79 |     12.19 |           1.86 |        9.70 |        5.21 |    0.43 |           10.14 |            11.14 |             21.47 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.98 |      5.54 |           2.64 | unavailable |        9.70 |    0.10 |            4.49 |             5.49 |              6.50 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.97 |      5.54 |           1.34 | unavailable |        9.10 |    0.46 |            4.49 |             5.49 |              6.49 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.12 |      7.21 |           2.58 | unavailable |       15.34 |    0.58 |            6.09 |             7.09 |             13.72 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.61 |      7.20 |           1.38 | unavailable |       17.45 |    6.33 |            6.09 |             7.09 |             13.53 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.54 |      8.01 |           2.19 |        2.50 |        5.20 |    0.03 |            6.67 |             7.67 |             28.79 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.65 |      8.01 |           1.70 |        7.49 |        5.20 |    4.63 |            6.67 |             7.67 |             28.66 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.54 |      8.01 |           2.19 |       16.58 |        5.20 |    0.72 |            6.67 |             7.67 |             28.79 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.65 |      8.01 |           1.70 |       22.78 |        5.20 |   26.77 |            6.67 |             7.67 |             28.66 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.68 |     12.19 |           2.37 |        8.54 |        5.21 |    0.12 |           10.15 |            11.15 |             21.60 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    52.79 |     12.19 |           1.86 |        9.70 |        5.21 |    0.43 |           10.14 |            11.14 |             21.47 |

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
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (23.6°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.8 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (23.6°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.8 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=161.2103314552721 g (allowed None … 85.0); apogee_m=6.76018227314065 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.445296432727772 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=10.943729912098663 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=161.2103314552721 g (allowed None … 85.0); apogee_m=6.744334643788528 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.43923672421882 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8677254158073985 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.102570250642541 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=163.7603314552721 g (allowed None … 99.0); apogee_m=23.966279695937693 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.144552783802464 m/s (allowed 12.0 … None); deployment_speed_m_s=13.897766825789475 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=163.7603314552721 g (allowed None … 99.0); apogee_m=23.352569516987366 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.138031661688546 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9436639095690278 cal (allowed 1.0 … None); deployment_speed_m_s=18.3709647526137 m/s
  (allowed None … 10.0); landing_descent_m_s=11.410708420870767 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=167.96033145527213 g (allowed None … 113.0); guide_departure_m_s=8.923333079662243 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=167.96033145527213 g (allowed None … 113.0); guide_departure_m_s=8.917071240243963 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=167.96033145527213 g (allowed None … 113.0); guide_departure_m_s=8.923333079662243 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.322295464304222 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=167.96033145527213 g (allowed None … 113.0); guide_departure_m_s=8.917071240243963 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.83443580038042 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=181.8603314552721 g (allowed None … 85.0); apogee_m=4.9768954581633125 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.54332908082924 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.700405692599954 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=181.8603314552721 g (allowed None … 85.0); apogee_m=4.969263532990468 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.53837749496282 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.096945328891584 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=184.41033145527211 g (allowed None … 99.0); apogee_m=18.123543862464235 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2089702008718 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.341324071048424 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=184.41033145527211 g (allowed None … 99.0); apogee_m=17.605497258485173 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2033424037132505 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=17.4509663508879 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.012873071215756 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.007353905444704 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.012873071215756 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.578469625338997 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.007353905444704 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.779478863116847 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=181.8603314552721 g (allowed None … 85.0); apogee_m=4.9768954581633125 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.54332908082924 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.700405692599954 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=181.8603314552721 g (allowed None … 85.0); apogee_m=4.969263532990468 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.53837749496282 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.096945328891584 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=184.41033145527211 g (allowed None … 99.0); apogee_m=18.123543862464235 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2089702008718 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.341324071048426 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=184.41033145527211 g (allowed None … 99.0); apogee_m=17.605497258485173 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2033424037132505 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=17.450966350887896 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.012873071215756
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.007353905444704
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.012873071215756
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.57846962533904 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=188.61033145527213 g (allowed None … 113.0); guide_departure_m_s=8.007353905444704
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.779478863116847 m/s (allowed None … 10.0)
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
