# Rocket Workbench report

Run: `ogive-n70-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `7c239009323c88831c00f89085fa418fb8ab03f5f3e62dab990adce4e5b646fd`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.98 |      6.54 |           2.02 | unavailable |       10.86 |    0.29 |            5.28 |             6.28 |              8.26 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.96 |      6.53 |           0.89 | unavailable |       10.08 |    0.45 |            5.28 |             6.28 |              8.24 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.65 |      8.25 |           1.99 |       13.56 |        4.75 |    2.56 |            7.09 |             8.09 |             16.92 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.89 |      8.24 |           0.96 |       19.66 |       14.20 |    9.74 |            7.09 |             8.09 |             16.69 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.43 |      9.02 |           1.89 |        1.70 |        4.86 |    0.04 |            7.73 |             8.73 |             34.57 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.56 |      9.01 |           1.29 |        6.32 |        4.86 |    6.24 |            7.72 |             8.72 |             34.41 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.44 |      9.02 |           1.53 |       12.08 |        4.86 |    1.31 |            7.73 |             8.73 |             34.57 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.56 |      9.01 |           1.29 |       18.84 |        4.86 |   12.61 |            7.72 |             8.72 |             34.41 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.58 |     13.09 |           1.33 |        4.50 |        4.86 |    0.01 |           11.69 |            12.69 |             26.59 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    69.82 |     13.08 |           1.34 |        5.77 |        4.86 |   10.67 |           11.68 |            12.68 |             26.42 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.13 |      5.63 |           2.51 | unavailable |        9.76 |    0.12 |            4.56 |             5.56 |              6.64 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.12 |      5.63 |           1.34 | unavailable |        9.20 |    0.34 |            4.56 |             5.55 |              6.63 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.61 |      7.29 |           2.22 | unavailable |       15.94 |    0.50 |            6.17 |             7.17 |             13.98 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.96 |      7.29 |           1.56 | unavailable |       17.94 |    7.52 |            6.17 |             7.17 |             13.75 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.02 |      8.09 |           2.24 |        2.18 |        5.17 |    0.03 |            6.76 |             7.76 |             29.24 |
| dummy-C6-3-wind2  | completed / outside configured limits |    65.75 |      8.08 |           1.70 |        7.74 |        5.17 |    5.70 |            6.75 |             7.75 |             29.13 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.02 |      8.09 |           2.24 |       16.83 |        5.17 |    0.89 |            6.76 |             7.76 |             29.24 |
| dummy-C6-5-wind2  | completed / outside configured limits |    65.75 |      8.08 |           1.70 |       22.69 |        5.17 |   28.48 |            6.75 |             7.75 |             29.13 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.94 |     12.35 |           1.88 |        8.21 |        5.18 |    0.12 |           10.27 |            11.27 |             21.99 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.99 |     12.35 |           1.89 |        9.57 |        5.18 |    0.13 |           10.27 |            11.27 |             21.86 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.13 |      5.63 |           2.51 | unavailable |        9.76 |    0.12 |            4.56 |             5.56 |              6.64 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.12 |      5.63 |           1.34 | unavailable |        9.20 |    0.34 |            4.56 |             5.55 |              6.63 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.61 |      7.29 |           2.22 | unavailable |       15.94 |    0.50 |            6.17 |             7.17 |             13.98 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.96 |      7.29 |           1.56 | unavailable |       17.94 |    7.52 |            6.17 |             7.17 |             13.75 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.02 |      8.09 |           2.24 |        2.18 |        5.17 |    0.03 |            6.76 |             7.76 |             29.24 |
| actual-C6-3-wind2 | completed / outside configured limits |    65.75 |      8.08 |           1.70 |        7.74 |        5.17 |    5.70 |            6.75 |             7.75 |             29.13 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.02 |      8.09 |           2.24 |       16.83 |        5.17 |    0.89 |            6.76 |             7.76 |             29.24 |
| actual-C6-5-wind2 | completed / outside configured limits |    65.75 |      8.08 |           1.70 |       22.69 |        5.17 |   28.48 |            6.75 |             7.75 |             29.13 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.94 |     12.35 |           1.88 |        8.21 |        5.18 |    0.12 |           10.27 |            11.27 |             21.99 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.99 |     12.35 |           1.89 |        9.57 |        5.18 |    0.13 |           10.27 |            11.27 |             21.86 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (18.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.7 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (18.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.7 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=159.13894494874353 g (allowed None … 85.0); apogee_m=6.978826917691317 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.536009327918718 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.85764087353958 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=159.13894494874353 g (allowed None … 85.0); apogee_m=6.955094873138014 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.529781056559371 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8888235297162048 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.07608220436604 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=161.68894494874354 g (allowed None … 99.0); apogee_m=24.647723352059455 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.245297168954378 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.559473800073205 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=161.68894494874354 g (allowed None … 99.0); apogee_m=23.892925167084137 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.238584578711949 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9618338659441696 cal (allowed 1.0 … None); deployment_speed_m_s=19.660258924006328 m/s
  (allowed None … 10.0); landing_descent_m_s=14.197040161397403 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=165.88894494874353 g (allowed None … 113.0); guide_departure_m_s=9.015071098849711 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=165.88894494874353 g (allowed None … 113.0); guide_departure_m_s=9.00864767339423 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=165.88894494874353 g (allowed None … 113.0); guide_departure_m_s=9.015071098849711 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.077239704934918 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=165.88894494874353 g (allowed None … 113.0); guide_departure_m_s=9.00864767339423 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.835939226556793 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=179.78894494874353 g (allowed None … 85.0); apogee_m=5.126145244283448 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.6310873901772345 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.756020285940165 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=179.78894494874353 g (allowed None … 85.0); apogee_m=5.117769908990926 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.6259238840058785 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.203451775632367 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=182.33894494874352 g (allowed None … 99.0); apogee_m=18.612702071818514 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.292719550258961 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.935719171858196 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=182.33894494874352 g (allowed None … 99.0); apogee_m=17.959648600947396 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.286919875629789 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.940253982908892 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.090255988694642 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.084591690931301 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.090255988694642 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.828796045691313 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.084591690931301 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.691050013308026 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=179.78894494874353 g (allowed None … 85.0); apogee_m=5.126145244283448 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.6310873901772345 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=9.756020285940165 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=179.78894494874353 g (allowed None … 85.0); apogee_m=5.117769908990926 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.6259238840058785 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=9.203451775632365 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=182.33894494874352 g (allowed None … 99.0); apogee_m=18.612702071818514 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.292719550258961 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.935719171858194 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=182.33894494874352 g (allowed None … 99.0); apogee_m=17.959648600947396 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.286919875629789 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.940253982908892 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.090255988694642
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.084591690931301
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.090255988694642
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.828796045691313 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=186.53894494874353 g (allowed None … 113.0); guide_departure_m_s=8.084591690931301
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.691050013308036 m/s (allowed None … 10.0)
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
