# Rocket Workbench report

Run: `bt60-24-cd-heavy-build`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `29396f4490e1f2319d7e3d106ed6c57fc2e66e0d113bdc95f9a7422fa7bc56f6`

## Cases

| Case               | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------ | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-C11-3-wind0  | completed / outside configured limits |    73.83 |     11.97 |           1.33 |       3.57 |        5.33 |    0.02 |           10.35 |            11.35 |             36.89 |
| empty-C11-3-wind2  | completed / outside configured limits |    73.20 |     11.97 |           0.85 |       3.63 |        5.33 |   21.42 |           10.34 |            11.34 |             36.77 |
| empty-C11-3-wind4  | completed / outside configured limits |    71.75 |     11.96 |           0.61 |       3.72 |        5.33 |   44.03 |           10.33 |            11.33 |             36.46 |
| empty-C11-5-wind0  | completed / outside configured limits |    73.98 |     11.97 |           1.16 |      13.42 |        5.33 |    1.32 |           10.35 |            11.35 |             36.89 |
| empty-C11-5-wind2  | completed / outside configured limits |    73.38 |     11.97 |           0.41 |      14.18 |        5.33 |   16.19 |           10.34 |            11.34 |             36.77 |
| empty-C11-5-wind4  | completed / outside configured limits |    71.94 |     11.96 |           0.61 |      14.85 |        5.33 |   29.87 |           10.33 |            11.33 |             36.46 |
| empty-D12-3-wind0  | completed / outside configured limits |   181.23 |     13.17 |           1.21 |      19.61 |        5.30 |    0.05 |           13.98 |            14.98 |             62.80 |
| empty-D12-3-wind2  | completed / outside configured limits |   179.98 |     13.16 |           0.79 |      19.56 |        5.30 |   53.01 |           13.97 |            14.97 |             62.66 |
| empty-D12-3-wind4  | completed / outside configured limits |   176.83 |     13.16 |           0.53 |      19.41 |        5.30 |  106.36 |           13.96 |            14.96 |             62.30 |
| empty-D12-5-wind0  | completed / outside configured limits |   196.26 |     13.17 |           0.79 |       0.64 |        5.30 |    0.09 |           13.98 |            14.98 |             62.80 |
| empty-D12-5-wind2  | completed / outside configured limits |   194.67 |     13.16 |           0.50 |       2.48 |        5.30 |   51.45 |           13.97 |            14.97 |             62.66 |
| empty-D12-5-wind4  | completed / outside configured limits |   190.53 |     13.16 |           0.53 |       4.80 |        5.30 |  104.04 |           13.96 |            14.96 |             62.30 |
| empty-D12-7-wind0  | completed / outside configured limits |   196.26 |     13.17 |           0.79 |      15.86 |        5.30 |    2.77 |           13.98 |            14.98 |             62.80 |
| empty-D12-7-wind2  | completed / outside configured limits |   194.67 |     13.16 |           0.50 |      16.59 |        5.30 |   42.83 |           13.97 |            14.97 |             62.66 |
| empty-D12-7-wind4  | completed / outside configured limits |   190.53 |     13.16 |           0.53 |      20.37 |        5.30 |   78.45 |           13.96 |            14.96 |             62.30 |
| dummy-C11-3-wind0  | completed / outside configured limits |    57.75 |     11.36 |           1.82 |       0.36 |        5.73 |    0.02 |            8.88 |             9.88 |             31.34 |
| dummy-C11-3-wind2  | completed / outside configured limits |    57.17 |     11.35 |           1.01 |       1.35 |        5.73 |   13.35 |            8.87 |             9.87 |             31.21 |
| dummy-C11-3-wind4  | completed / outside configured limits |    55.65 |     11.35 |           1.19 |       2.64 |        5.73 |   27.19 |            8.87 |             9.87 |             30.88 |
| dummy-C11-5-wind0  | completed / outside configured limits |    57.75 |     11.36 |           1.82 |      14.10 |        5.73 |    0.78 |            8.88 |             9.88 |             31.34 |
| dummy-C11-5-wind2  | completed / outside configured limits |    57.17 |     11.35 |           1.01 |      15.91 |        5.73 |    4.04 |            8.87 |             9.87 |             31.21 |
| dummy-C11-5-wind4  | completed / outside configured limits |    55.65 |     11.35 |           1.19 |      19.57 |        5.73 |    7.50 |            8.87 |             9.87 |             30.88 |
| dummy-D12-3-wind0  | completed / outside configured limits |   156.53 |     12.60 |           1.80 |      15.93 |        5.71 |    0.05 |           12.10 |            13.10 |             54.32 |
| dummy-D12-3-wind2  | completed / outside configured limits |   154.91 |     12.59 |           1.38 |      15.99 |        5.71 |   36.92 |           12.09 |            13.09 |             54.17 |
| dummy-D12-3-wind4  | completed / outside configured limits |   150.65 |     12.59 |           1.11 |      16.14 |        5.71 |   73.24 |           12.08 |            13.08 |             53.76 |
| dummy-D12-5-wind0  | completed / incomplete inputs         |   165.70 |     12.60 |           1.35 |       3.97 |        5.71 |    0.07 |           12.10 |            13.10 |             54.32 |
| dummy-D12-5-wind2  | completed / incomplete inputs         |   163.79 |     12.59 |           1.24 |       4.97 |        5.71 |   31.68 |           12.09 |            13.09 |             54.17 |
| dummy-D12-5-wind4  | completed / incomplete inputs         |   158.54 |     12.59 |           1.11 |       8.05 |        5.71 |   62.38 |           12.08 |            13.08 |             53.76 |
| dummy-D12-7-wind0  | completed / outside configured limits |   165.70 |     12.60 |           1.35 |      17.17 |        5.71 |    0.02 |           12.10 |            13.10 |             54.32 |
| dummy-D12-7-wind2  | completed / outside configured limits |   163.79 |     12.59 |           1.24 |      21.88 |        5.71 |   17.39 |           12.09 |            13.09 |             54.17 |
| dummy-D12-7-wind4  | completed / outside configured limits |   158.54 |     12.59 |           1.11 |      24.11 |        5.71 |   29.99 |           12.08 |            13.08 |             53.76 |
| actual-C11-3-wind0 | completed / outside configured limits |    57.75 |     11.36 |           1.82 |       0.36 |        5.73 |    0.02 |            8.88 |             9.88 |             31.34 |
| actual-C11-3-wind2 | completed / outside configured limits |    57.17 |     11.35 |           1.01 |       1.35 |        5.73 |   13.35 |            8.87 |             9.87 |             31.21 |
| actual-C11-3-wind4 | completed / outside configured limits |    55.65 |     11.35 |           1.19 |       2.64 |        5.73 |   27.19 |            8.87 |             9.87 |             30.88 |
| actual-C11-5-wind0 | completed / outside configured limits |    57.75 |     11.36 |           1.82 |      14.10 |        5.73 |    0.78 |            8.88 |             9.88 |             31.34 |
| actual-C11-5-wind2 | completed / outside configured limits |    57.17 |     11.35 |           1.01 |      15.91 |        5.73 |    4.04 |            8.87 |             9.87 |             31.21 |
| actual-C11-5-wind4 | completed / outside configured limits |    55.65 |     11.35 |           1.19 |      19.57 |        5.73 |    7.50 |            8.87 |             9.87 |             30.88 |
| actual-D12-3-wind0 | completed / outside configured limits |   156.53 |     12.60 |           1.80 |      15.93 |        5.71 |    0.05 |           12.10 |            13.10 |             54.32 |
| actual-D12-3-wind2 | completed / outside configured limits |   154.91 |     12.59 |           1.38 |      15.99 |        5.71 |   36.92 |           12.09 |            13.09 |             54.17 |
| actual-D12-3-wind4 | completed / outside configured limits |   150.65 |     12.59 |           1.11 |      16.14 |        5.71 |   73.24 |           12.08 |            13.08 |             53.76 |
| actual-D12-5-wind0 | completed / incomplete inputs         |   165.70 |     12.60 |           1.35 |       3.97 |        5.71 |    0.07 |           12.10 |            13.10 |             54.32 |
| actual-D12-5-wind2 | completed / incomplete inputs         |   163.79 |     12.59 |           1.24 |       4.97 |        5.71 |   31.68 |           12.09 |            13.09 |             54.17 |
| actual-D12-5-wind4 | completed / incomplete inputs         |   158.54 |     12.59 |           1.11 |       8.05 |        5.71 |   62.38 |           12.08 |            13.08 |             53.76 |
| actual-D12-7-wind0 | completed / outside configured limits |   165.70 |     12.60 |           1.35 |      17.17 |        5.71 |    0.02 |           12.10 |            13.10 |             54.32 |
| actual-D12-7-wind2 | completed / outside configured limits |   163.79 |     12.59 |           1.24 |      21.88 |        5.71 |   17.39 |           12.09 |            13.09 |             54.17 |
| actual-D12-7-wind4 | completed / outside configured limits |   158.54 |     12.59 |           1.11 |      24.11 |        5.71 |   29.99 |           12.08 |            13.08 |             53.76 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-C11-3-wind0: no engine warnings
- empty-C11-3-wind2: no engine warnings
- empty-C11-3-wind4: no engine warnings
- empty-C11-5-wind0: no engine warnings
- empty-C11-5-wind2: no engine warnings
- empty-C11-5-wind4: no engine warnings
- empty-D12-3-wind0: no engine warnings
- empty-D12-3-wind2: no engine warnings
- empty-D12-3-wind4: no engine warnings
- empty-D12-5-wind0: no engine warnings
- empty-D12-5-wind2: no engine warnings
- empty-D12-5-wind4: no engine warnings
- empty-D12-7-wind0: no engine warnings
- empty-D12-7-wind2: no engine warnings
- empty-D12-7-wind4: Recovery device deployment at high speed (20.4 m/s): "Nominal 457 mm parachute and lines"
- dummy-C11-3-wind0: no engine warnings
- dummy-C11-3-wind2: no engine warnings
- dummy-C11-3-wind4: no engine warnings
- dummy-C11-5-wind0: no engine warnings
- dummy-C11-5-wind2: no engine warnings
- dummy-C11-5-wind4: no engine warnings
- dummy-D12-3-wind0: no engine warnings
- dummy-D12-3-wind2: no engine warnings
- dummy-D12-3-wind4: no engine warnings
- dummy-D12-5-wind0: no engine warnings
- dummy-D12-5-wind2: no engine warnings
- dummy-D12-5-wind4: no engine warnings
- dummy-D12-7-wind0: no engine warnings
- dummy-D12-7-wind2: Recovery device deployment at high speed (21.9 m/s): "Nominal 457 mm parachute and lines"
- dummy-D12-7-wind4: Recovery device deployment at high speed (24.1 m/s): "Nominal 457 mm parachute and lines"
- actual-C11-3-wind0: no engine warnings
- actual-C11-3-wind2: no engine warnings
- actual-C11-3-wind4: no engine warnings
- actual-C11-5-wind0: no engine warnings
- actual-C11-5-wind2: no engine warnings
- actual-C11-5-wind4: no engine warnings
- actual-D12-3-wind0: no engine warnings
- actual-D12-3-wind2: no engine warnings
- actual-D12-3-wind4: no engine warnings
- actual-D12-5-wind0: no engine warnings
- actual-D12-5-wind2: no engine warnings
- actual-D12-5-wind4: no engine warnings
- actual-D12-7-wind0: no engine warnings
- actual-D12-7-wind2: Recovery device deployment at high speed (21.9 m/s): "Nominal 457 mm parachute and lines"
- actual-D12-7-wind4: Recovery device deployment at high speed (24.1 m/s): "Nominal 457 mm parachute and lines"

## Missing measurements / physical checks

- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: Provisional commercial 24 mm mount assembly plus CD spacer
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

- empty-C11-3-wind0: launch_mass_g=198.9044289977738 g (allowed None … 170.0); guide_departure_m_s=11.97123719603576 m/s
  (allowed 12.0 … None)
- empty-C11-3-wind2: launch_mass_g=198.9044289977738 g (allowed None … 170.0); guide_departure_m_s=11.965534141727854
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8547880165104104 cal (allowed 1.0 … None)
- empty-C11-3-wind4: launch_mass_g=198.9044289977738 g (allowed None … 170.0); guide_departure_m_s=11.963713556668537
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6133994287069712 cal (allowed 1.0 … None)
- empty-C11-5-wind0: launch_mass_g=198.9044289977738 g (allowed None … 142.0); guide_departure_m_s=11.97123719603576 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.42473538753105 m/s (allowed None … 10.0)
- empty-C11-5-wind2: launch_mass_g=198.9044289977738 g (allowed None … 142.0); guide_departure_m_s=11.965534141727854
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.4119270255232507 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.175037335086312 m/s (allowed None … 10.0)
- empty-C11-5-wind4: launch_mass_g=198.9044289977738 g (allowed None … 142.0); guide_departure_m_s=11.963713556668537
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.6133994287069712 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.851650641024996 m/s (allowed None … 10.0)
- empty-D12-3-wind0: deployment_speed_m_s=19.61002666225525 m/s (allowed None … 10.0)
- empty-D12-3-wind2: minimum_ascent_stability_cal=0.7931460755690016 cal (allowed 1.0 … None);
  deployment_speed_m_s=19.561028583936984 m/s (allowed None … 10.0)
- empty-D12-3-wind4: minimum_ascent_stability_cal=0.5336438405692148 cal (allowed 1.0 … None);
  deployment_speed_m_s=19.405394583992823 m/s (allowed None … 10.0)
- empty-D12-5-wind0: minimum_ascent_stability_cal=0.7883266035969064 cal (allowed 1.0 … None)
- empty-D12-5-wind2: minimum_ascent_stability_cal=0.49537612518208035 cal (allowed 1.0 … None)
- empty-D12-5-wind4: minimum_ascent_stability_cal=0.5336438405692148 cal (allowed 1.0 … None)
- empty-D12-7-wind0: minimum_ascent_stability_cal=0.7883266035969064 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.862684308878915 m/s (allowed None … 10.0)
- empty-D12-7-wind2: minimum_ascent_stability_cal=0.49537612518208035 cal (allowed 1.0 … None);
  deployment_speed_m_s=16.59352600402451 m/s (allowed None … 10.0)
- empty-D12-7-wind4: minimum_ascent_stability_cal=0.5336438405692148 cal (allowed 1.0 … None);
  deployment_speed_m_s=20.36714748218489 m/s (allowed None … 10.0)
- dummy-C11-3-wind0: launch_mass_g=228.1044289977738 g (allowed None … 170.0); guide_departure_m_s=11.359820924601134
  m/s (allowed 12.0 … None)
- dummy-C11-3-wind2: launch_mass_g=228.1044289977738 g (allowed None … 170.0); guide_departure_m_s=11.354806102635473
  m/s (allowed 12.0 … None)
- dummy-C11-3-wind4: launch_mass_g=228.1044289977738 g (allowed None … 170.0); guide_departure_m_s=11.353520643747519
  m/s (allowed 12.0 … None)
- dummy-C11-5-wind0: launch_mass_g=228.1044289977738 g (allowed None … 142.0); guide_departure_m_s=11.359820924601134
  m/s (allowed 12.0 … None); deployment_speed_m_s=14.101981505672606 m/s (allowed None … 10.0)
- dummy-C11-5-wind2: launch_mass_g=228.1044289977738 g (allowed None … 142.0); guide_departure_m_s=11.354806102635473
  m/s (allowed 12.0 … None); deployment_speed_m_s=15.914201993831357 m/s (allowed None … 10.0)
- dummy-C11-5-wind4: launch_mass_g=228.1044289977738 g (allowed None … 142.0); guide_departure_m_s=11.353520643747519
  m/s (allowed 12.0 … None); deployment_speed_m_s=19.567725465855816 m/s (allowed None … 10.0)
- dummy-D12-3-wind0: deployment_speed_m_s=15.929230925585077 m/s (allowed None … 10.0)
- dummy-D12-3-wind2: deployment_speed_m_s=15.989097625102747 m/s (allowed None … 10.0)
- dummy-D12-3-wind4: deployment_speed_m_s=16.144261187575225 m/s (allowed None … 10.0)
- dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- dummy-D12-7-wind0: launch_mass_g=235.4044289977738 g (allowed None … 226.0); deployment_speed_m_s=17.17493447158099
  m/s (allowed None … 10.0)
- dummy-D12-7-wind2: launch_mass_g=235.4044289977738 g (allowed None … 226.0); deployment_speed_m_s=21.882448178298862
  m/s (allowed None … 10.0)
- dummy-D12-7-wind4: launch_mass_g=235.4044289977738 g (allowed None … 226.0); deployment_speed_m_s=24.108251430714922
  m/s (allowed None … 10.0)
- actual-C11-3-wind0: launch_mass_g=228.1044289977738 g (allowed None … 170.0); guide_departure_m_s=11.359820924601134
  m/s (allowed 12.0 … None)
- actual-C11-3-wind2: launch_mass_g=228.1044289977738 g (allowed None … 170.0); guide_departure_m_s=11.354806102635473
  m/s (allowed 12.0 … None)
- actual-C11-3-wind4: launch_mass_g=228.1044289977738 g (allowed None … 170.0); guide_departure_m_s=11.353520643747519
  m/s (allowed 12.0 … None)
- actual-C11-5-wind0: launch_mass_g=228.1044289977738 g (allowed None … 142.0); guide_departure_m_s=11.359820924601134
  m/s (allowed 12.0 … None); deployment_speed_m_s=14.101981505672606 m/s (allowed None … 10.0)
- actual-C11-5-wind2: launch_mass_g=228.1044289977738 g (allowed None … 142.0); guide_departure_m_s=11.354806102635473
  m/s (allowed 12.0 … None); deployment_speed_m_s=15.91420199383129 m/s (allowed None … 10.0)
- actual-C11-5-wind4: launch_mass_g=228.1044289977738 g (allowed None … 142.0); guide_departure_m_s=11.353520643747519
  m/s (allowed 12.0 … None); deployment_speed_m_s=19.567725465855855 m/s (allowed None … 10.0)
- actual-D12-3-wind0: deployment_speed_m_s=15.929230925585077 m/s (allowed None … 10.0)
- actual-D12-3-wind2: deployment_speed_m_s=15.989097625102817 m/s (allowed None … 10.0)
- actual-D12-3-wind4: deployment_speed_m_s=16.144261187575278 m/s (allowed None … 10.0)
- actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- actual-D12-7-wind0: launch_mass_g=235.4044289977738 g (allowed None … 226.0); deployment_speed_m_s=17.17493447158099
  m/s (allowed None … 10.0)
- actual-D12-7-wind2: launch_mass_g=235.4044289977738 g (allowed None … 226.0); deployment_speed_m_s=21.882448178296116
  m/s (allowed None … 10.0)
- actual-D12-7-wind4: launch_mass_g=235.4044289977738 g (allowed None … 226.0); deployment_speed_m_s=24.108251430714944
  m/s (allowed None … 10.0)

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

- apogee_m: 30.0 … None m; engineering assumption; New motor comparison: report altitude without inherited 120 m
  ceiling; retain 30 m minimum. Site altitude clearance is unassessed.
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
  "repository_revision": "2ca06e7f9c7adcd40d8e6847452df77f6a5b9717"
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
