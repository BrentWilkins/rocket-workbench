# Rocket Workbench report

Run: `stress-20260913T161708Z-79132db7`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `2043d2299c8da2abac92799e2e1d49c2e2691cfa2ad2d277c2bb868539b96d70`

## Cases

| Case                 | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| -------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-D12-5-wind0  | completed / incomplete inputs         |   215.07 |     13.35 |           1.31 |       1.13 |        5.68 |    0.10 |           15.22 |            16.22 |             68.23 |
| 0-empty-D12-5-wind2  | completed / outside configured limits |   213.45 |     13.35 |           0.73 |       2.56 |        5.68 |   52.65 |           15.21 |            16.21 |             68.09 |
| 0-empty-D12-5-wind4  | completed / outside configured limits |   209.21 |     13.35 |           0.61 |       4.49 |        5.68 |  106.86 |           15.20 |            16.20 |             67.74 |
| 0-dummy-D12-5-wind0  | completed / outside configured limits |   182.76 |     12.92 |           1.70 |       1.89 |        6.15 |    0.09 |           13.04 |            14.04 |             58.75 |
| 0-dummy-D12-5-wind2  | completed / outside configured limits |   180.81 |     12.92 |           1.44 |       3.65 |        6.15 |   32.61 |           13.03 |            14.03 |             58.60 |
| 0-dummy-D12-5-wind4  | completed / outside configured limits |   175.42 |     12.92 |           1.27 |       6.82 |        6.15 |   64.98 |           13.02 |            14.02 |             58.20 |
| 0-actual-D12-5-wind0 | completed / outside configured limits |   182.76 |     12.92 |           1.70 |       1.89 |        6.15 |    0.09 |           13.04 |            14.04 |             58.75 |
| 0-actual-D12-5-wind2 | completed / outside configured limits |   180.81 |     12.92 |           1.44 |       3.65 |        6.15 |   32.61 |           13.03 |            14.03 |             58.60 |
| 0-actual-D12-5-wind4 | completed / outside configured limits |   175.42 |     12.92 |           1.27 |       6.82 |        6.15 |   64.98 |           13.02 |            14.02 |             58.20 |
| 1-empty-D12-5-wind0  | completed / incomplete inputs         |   215.07 |     13.35 |           1.31 |       1.13 |        4.63 |    0.10 |           15.22 |            16.22 |             68.23 |
| 1-empty-D12-5-wind2  | completed / outside configured limits |   213.45 |     13.35 |           0.73 |       2.56 |        4.63 |   70.04 |           15.21 |            16.21 |             68.09 |
| 1-empty-D12-5-wind4  | completed / outside configured limits |   209.21 |     13.35 |           0.61 |       4.49 |        4.63 |  140.68 |           15.20 |            16.20 |             67.74 |
| 1-dummy-D12-5-wind0  | completed / incomplete inputs         |   182.76 |     12.92 |           1.70 |       1.89 |        5.02 |    0.09 |           13.04 |            14.04 |             58.75 |
| 1-dummy-D12-5-wind2  | completed / incomplete inputs         |   180.81 |     12.92 |           1.44 |       3.65 |        5.02 |   46.44 |           13.03 |            14.03 |             58.60 |
| 1-dummy-D12-5-wind4  | completed / incomplete inputs         |   175.42 |     12.92 |           1.27 |       6.82 |        5.02 |   91.52 |           13.02 |            14.02 |             58.20 |
| 1-actual-D12-5-wind0 | completed / incomplete inputs         |   182.76 |     12.92 |           1.70 |       1.89 |        5.02 |    0.09 |           13.04 |            14.04 |             58.75 |
| 1-actual-D12-5-wind2 | completed / incomplete inputs         |   180.81 |     12.92 |           1.44 |       3.65 |        5.02 |   46.44 |           13.03 |            14.03 |             58.60 |
| 1-actual-D12-5-wind4 | completed / incomplete inputs         |   175.42 |     12.92 |           1.27 |       6.82 |        5.02 |   91.52 |           13.02 |            14.02 |             58.20 |
| 2-empty-D12-5-wind0  | completed / incomplete inputs         |   215.07 |     13.35 |           1.31 |       1.13 |        5.68 |    0.10 |           15.22 |            16.22 |             68.23 |
| 2-empty-D12-5-wind2  | completed / outside configured limits |   213.45 |     13.35 |           0.73 |       2.56 |        5.68 |   52.65 |           15.21 |            16.21 |             68.09 |
| 2-empty-D12-5-wind4  | completed / outside configured limits |   209.21 |     13.35 |           0.61 |       4.49 |        5.68 |  106.86 |           15.20 |            16.20 |             67.74 |
| 2-dummy-D12-5-wind0  | completed / outside configured limits |   182.76 |     12.92 |           1.66 |       1.89 |        6.15 |    0.09 |           13.04 |            14.04 |             58.75 |
| 2-dummy-D12-5-wind2  | completed / outside configured limits |   180.81 |     12.92 |           1.40 |       3.66 |        6.15 |   32.60 |           13.03 |            14.03 |             58.60 |
| 2-dummy-D12-5-wind4  | completed / outside configured limits |   175.42 |     12.92 |           1.23 |       6.82 |        6.15 |   65.01 |           13.02 |            14.02 |             58.20 |
| 2-actual-D12-5-wind0 | completed / outside configured limits |   182.76 |     12.92 |           1.66 |       1.89 |        6.15 |    0.09 |           13.04 |            14.04 |             58.75 |
| 2-actual-D12-5-wind2 | completed / outside configured limits |   180.81 |     12.92 |           1.40 |       3.66 |        6.15 |   32.60 |           13.03 |            14.03 |             58.60 |
| 2-actual-D12-5-wind4 | completed / outside configured limits |   175.42 |     12.92 |           1.23 |       6.82 |        6.15 |   65.01 |           13.02 |            14.02 |             58.20 |
| 3-empty-D12-5-wind0  | completed / incomplete inputs         |   215.07 |     13.35 |           1.31 |       1.13 |        4.63 |    0.10 |           15.22 |            16.22 |             68.23 |
| 3-empty-D12-5-wind2  | completed / outside configured limits |   213.45 |     13.35 |           0.73 |       2.56 |        4.63 |   70.04 |           15.21 |            16.21 |             68.09 |
| 3-empty-D12-5-wind4  | completed / outside configured limits |   209.21 |     13.35 |           0.61 |       4.49 |        4.63 |  140.68 |           15.20 |            16.20 |             67.74 |
| 3-dummy-D12-5-wind0  | completed / incomplete inputs         |   182.76 |     12.92 |           1.66 |       1.89 |        5.02 |    0.08 |           13.04 |            14.04 |             58.75 |
| 3-dummy-D12-5-wind2  | completed / incomplete inputs         |   180.81 |     12.92 |           1.40 |       3.66 |        5.02 |   46.42 |           13.03 |            14.03 |             58.60 |
| 3-dummy-D12-5-wind4  | completed / incomplete inputs         |   175.42 |     12.92 |           1.23 |       6.82 |        5.02 |   91.56 |           13.02 |            14.02 |             58.20 |
| 3-actual-D12-5-wind0 | completed / incomplete inputs         |   182.76 |     12.92 |           1.66 |       1.89 |        5.02 |    0.08 |           13.04 |            14.04 |             58.75 |
| 3-actual-D12-5-wind2 | completed / incomplete inputs         |   180.81 |     12.92 |           1.40 |       3.66 |        5.02 |   46.42 |           13.03 |            14.03 |             58.60 |
| 3-actual-D12-5-wind4 | completed / incomplete inputs         |   175.42 |     12.92 |           1.23 |       6.82 |        5.02 |   91.56 |           13.02 |            14.02 |             58.20 |
| 4-empty-D12-5-wind0  | completed / outside configured limits |   197.57 |     13.16 |           0.63 |       0.38 |        5.93 |    0.09 |           13.98 |            14.98 |             62.93 |
| 4-empty-D12-5-wind2  | completed / outside configured limits |   195.84 |     13.16 |           0.73 |       2.67 |        5.93 |   42.21 |           13.97 |            14.97 |             62.78 |
| 4-empty-D12-5-wind4  | completed / outside configured limits |   191.25 |     13.16 |           0.73 |       5.26 |        5.93 |   85.55 |           13.96 |            14.96 |             62.41 |
| 4-dummy-D12-5-wind0  | completed / outside configured limits |   166.56 |     12.60 |           1.51 |       3.78 |        6.38 |    0.07 |           12.10 |            13.10 |             54.40 |
| 4-dummy-D12-5-wind2  | completed / outside configured limits |   164.55 |     12.59 |           1.51 |       5.00 |        6.38 |   24.45 |           12.09 |            13.09 |             54.25 |
| 4-dummy-D12-5-wind4  | completed / outside configured limits |   159.01 |     12.59 |           1.32 |       8.24 |        6.38 |   48.39 |           12.08 |            13.08 |             53.84 |
| 4-actual-D12-5-wind0 | completed / outside configured limits |   166.56 |     12.60 |           1.51 |       3.78 |        6.38 |    0.07 |           12.10 |            13.10 |             54.40 |
| 4-actual-D12-5-wind2 | completed / outside configured limits |   164.55 |     12.59 |           1.51 |       5.00 |        6.38 |   24.45 |           12.09 |            13.09 |             54.25 |
| 4-actual-D12-5-wind4 | completed / outside configured limits |   159.01 |     12.59 |           1.32 |       8.24 |        6.38 |   48.39 |           12.08 |            13.08 |             53.84 |
| 5-empty-D12-5-wind0  | completed / outside configured limits |   197.57 |     13.16 |           0.63 |       0.38 |        4.84 |    0.09 |           13.98 |            14.98 |             62.93 |
| 5-empty-D12-5-wind2  | completed / outside configured limits |   195.84 |     13.16 |           0.73 |       2.67 |        4.84 |   57.60 |           13.97 |            14.97 |             62.78 |
| 5-empty-D12-5-wind4  | completed / outside configured limits |   191.25 |     13.16 |           0.73 |       5.26 |        4.84 |  115.34 |           13.96 |            14.96 |             62.41 |
| 5-dummy-D12-5-wind0  | completed / incomplete inputs         |   166.56 |     12.60 |           1.51 |       3.78 |        5.21 |    0.07 |           12.10 |            13.10 |             54.40 |
| 5-dummy-D12-5-wind2  | completed / incomplete inputs         |   164.55 |     12.59 |           1.51 |       5.00 |        5.21 |   36.64 |           12.09 |            13.09 |             54.25 |
| 5-dummy-D12-5-wind4  | completed / incomplete inputs         |   159.01 |     12.59 |           1.32 |       8.24 |        5.21 |   71.65 |           12.08 |            13.08 |             53.84 |
| 5-actual-D12-5-wind0 | completed / incomplete inputs         |   166.56 |     12.60 |           1.51 |       3.78 |        5.21 |    0.07 |           12.10 |            13.10 |             54.40 |
| 5-actual-D12-5-wind2 | completed / incomplete inputs         |   164.55 |     12.59 |           1.51 |       5.00 |        5.21 |   36.64 |           12.09 |            13.09 |             54.25 |
| 5-actual-D12-5-wind4 | completed / incomplete inputs         |   159.01 |     12.59 |           1.32 |       8.24 |        5.21 |   71.65 |           12.08 |            13.08 |             53.84 |
| 6-empty-D12-5-wind0  | completed / outside configured limits |   197.57 |     13.16 |           0.63 |       0.38 |        5.93 |    0.09 |           13.98 |            14.98 |             62.93 |
| 6-empty-D12-5-wind2  | completed / outside configured limits |   195.84 |     13.16 |           0.73 |       2.67 |        5.93 |   42.21 |           13.97 |            14.97 |             62.78 |
| 6-empty-D12-5-wind4  | completed / outside configured limits |   191.25 |     13.16 |           0.73 |       5.26 |        5.93 |   85.55 |           13.96 |            14.96 |             62.41 |
| 6-dummy-D12-5-wind0  | completed / outside configured limits |   166.56 |     12.60 |           1.47 |       3.78 |        6.38 |    0.07 |           12.10 |            13.10 |             54.40 |
| 6-dummy-D12-5-wind2  | completed / outside configured limits |   164.55 |     12.59 |           1.48 |       5.00 |        6.38 |   24.45 |           12.09 |            13.09 |             54.25 |
| 6-dummy-D12-5-wind4  | completed / outside configured limits |   159.02 |     12.59 |           1.29 |       8.24 |        6.38 |   48.43 |           12.08 |            13.08 |             53.85 |
| 6-actual-D12-5-wind0 | completed / outside configured limits |   166.56 |     12.60 |           1.47 |       3.78 |        6.38 |    0.07 |           12.10 |            13.10 |             54.40 |
| 6-actual-D12-5-wind2 | completed / outside configured limits |   164.55 |     12.59 |           1.48 |       5.00 |        6.38 |   24.45 |           12.09 |            13.09 |             54.25 |
| 6-actual-D12-5-wind4 | completed / outside configured limits |   159.02 |     12.59 |           1.29 |       8.24 |        6.38 |   48.43 |           12.08 |            13.08 |             53.85 |
| 7-empty-D12-5-wind0  | completed / outside configured limits |   197.57 |     13.16 |           0.63 |       0.38 |        4.84 |    0.09 |           13.98 |            14.98 |             62.93 |
| 7-empty-D12-5-wind2  | completed / outside configured limits |   195.84 |     13.16 |           0.73 |       2.67 |        4.84 |   57.60 |           13.97 |            14.97 |             62.78 |
| 7-empty-D12-5-wind4  | completed / outside configured limits |   191.25 |     13.16 |           0.73 |       5.26 |        4.84 |  115.34 |           13.96 |            14.96 |             62.41 |
| 7-dummy-D12-5-wind0  | completed / incomplete inputs         |   166.56 |     12.60 |           1.47 |       3.78 |        5.21 |    0.07 |           12.10 |            13.10 |             54.40 |
| 7-dummy-D12-5-wind2  | completed / incomplete inputs         |   164.55 |     12.59 |           1.48 |       5.00 |        5.21 |   36.64 |           12.09 |            13.09 |             54.25 |
| 7-dummy-D12-5-wind4  | completed / incomplete inputs         |   159.02 |     12.59 |           1.29 |       8.24 |        5.21 |   71.69 |           12.08 |            13.08 |             53.85 |
| 7-actual-D12-5-wind0 | completed / incomplete inputs         |   166.56 |     12.60 |           1.47 |       3.78 |        5.21 |    0.07 |           12.10 |            13.10 |             54.40 |
| 7-actual-D12-5-wind2 | completed / incomplete inputs         |   164.55 |     12.59 |           1.48 |       5.00 |        5.21 |   36.64 |           12.09 |            13.09 |             54.25 |
| 7-actual-D12-5-wind4 | completed / incomplete inputs         |   159.02 |     12.59 |           1.29 |       8.24 |        5.21 |   71.69 |           12.08 |            13.08 |             53.85 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- 0-empty-D12-5-wind0: no engine warnings
- 0-empty-D12-5-wind2: no engine warnings
- 0-empty-D12-5-wind4: no engine warnings
- 0-dummy-D12-5-wind0: no engine warnings
- 0-dummy-D12-5-wind2: no engine warnings
- 0-dummy-D12-5-wind4: no engine warnings
- 0-actual-D12-5-wind0: no engine warnings
- 0-actual-D12-5-wind2: no engine warnings
- 0-actual-D12-5-wind4: no engine warnings
- 1-empty-D12-5-wind0: no engine warnings
- 1-empty-D12-5-wind2: no engine warnings
- 1-empty-D12-5-wind4: no engine warnings
- 1-dummy-D12-5-wind0: no engine warnings
- 1-dummy-D12-5-wind2: no engine warnings
- 1-dummy-D12-5-wind4: no engine warnings
- 1-actual-D12-5-wind0: no engine warnings
- 1-actual-D12-5-wind2: no engine warnings
- 1-actual-D12-5-wind4: no engine warnings
- 2-empty-D12-5-wind0: no engine warnings
- 2-empty-D12-5-wind2: no engine warnings
- 2-empty-D12-5-wind4: no engine warnings
- 2-dummy-D12-5-wind0: no engine warnings
- 2-dummy-D12-5-wind2: no engine warnings
- 2-dummy-D12-5-wind4: no engine warnings
- 2-actual-D12-5-wind0: no engine warnings
- 2-actual-D12-5-wind2: no engine warnings
- 2-actual-D12-5-wind4: no engine warnings
- 3-empty-D12-5-wind0: no engine warnings
- 3-empty-D12-5-wind2: no engine warnings
- 3-empty-D12-5-wind4: no engine warnings
- 3-dummy-D12-5-wind0: no engine warnings
- 3-dummy-D12-5-wind2: no engine warnings
- 3-dummy-D12-5-wind4: no engine warnings
- 3-actual-D12-5-wind0: no engine warnings
- 3-actual-D12-5-wind2: no engine warnings
- 3-actual-D12-5-wind4: no engine warnings
- 4-empty-D12-5-wind0: no engine warnings
- 4-empty-D12-5-wind2: no engine warnings
- 4-empty-D12-5-wind4: no engine warnings
- 4-dummy-D12-5-wind0: no engine warnings
- 4-dummy-D12-5-wind2: no engine warnings
- 4-dummy-D12-5-wind4: no engine warnings
- 4-actual-D12-5-wind0: no engine warnings
- 4-actual-D12-5-wind2: no engine warnings
- 4-actual-D12-5-wind4: no engine warnings
- 5-empty-D12-5-wind0: no engine warnings
- 5-empty-D12-5-wind2: no engine warnings
- 5-empty-D12-5-wind4: no engine warnings
- 5-dummy-D12-5-wind0: no engine warnings
- 5-dummy-D12-5-wind2: no engine warnings
- 5-dummy-D12-5-wind4: no engine warnings
- 5-actual-D12-5-wind0: no engine warnings
- 5-actual-D12-5-wind2: no engine warnings
- 5-actual-D12-5-wind4: no engine warnings
- 6-empty-D12-5-wind0: no engine warnings
- 6-empty-D12-5-wind2: no engine warnings
- 6-empty-D12-5-wind4: no engine warnings
- 6-dummy-D12-5-wind0: no engine warnings
- 6-dummy-D12-5-wind2: no engine warnings
- 6-dummy-D12-5-wind4: no engine warnings
- 6-actual-D12-5-wind0: no engine warnings
- 6-actual-D12-5-wind2: no engine warnings
- 6-actual-D12-5-wind4: no engine warnings
- 7-empty-D12-5-wind0: no engine warnings
- 7-empty-D12-5-wind2: no engine warnings
- 7-empty-D12-5-wind4: no engine warnings
- 7-dummy-D12-5-wind0: no engine warnings
- 7-dummy-D12-5-wind2: no engine warnings
- 7-dummy-D12-5-wind4: no engine warnings
- 7-actual-D12-5-wind0: no engine warnings
- 7-actual-D12-5-wind2: no engine warnings
- 7-actual-D12-5-wind4: no engine warnings

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

- 0-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-empty-D12-5-wind2: minimum_ascent_stability_cal=0.7277673257790508 cal (allowed 1.0 … None)
- 0-empty-D12-5-wind4: minimum_ascent_stability_cal=0.607101487700022 cal (allowed 1.0 … None)
- 0-dummy-D12-5-wind0: landing_descent_m_s=6.145326204066306 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind2: landing_descent_m_s=6.14525613920065 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind4: landing_descent_m_s=6.1451861294931 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind0: landing_descent_m_s=6.145326204066306 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind2: landing_descent_m_s=6.145256139200649 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind4: landing_descent_m_s=6.1451861294931 m/s (allowed None … 6.0)
- 1-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-D12-5-wind2: minimum_ascent_stability_cal=0.727767325779219 cal (allowed 1.0 … None)
- 1-empty-D12-5-wind4: minimum_ascent_stability_cal=0.607101487700022 cal (allowed 1.0 … None)
- 1-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind2: minimum_ascent_stability_cal=0.7277673257791242 cal (allowed 1.0 … None)
- 2-empty-D12-5-wind4: minimum_ascent_stability_cal=0.607101487700022 cal (allowed 1.0 … None)
- 2-dummy-D12-5-wind0: landing_descent_m_s=6.145326204064433 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind2: landing_descent_m_s=6.1452561390043945 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind4: landing_descent_m_s=6.145186129215024 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind0: landing_descent_m_s=6.145326204064433 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind2: landing_descent_m_s=6.1452561390043945 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind4: landing_descent_m_s=6.145186129215024 m/s (allowed None … 6.0)
- 3-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-D12-5-wind2: minimum_ascent_stability_cal=0.7277673257783757 cal (allowed 1.0 … None)
- 3-empty-D12-5-wind4: minimum_ascent_stability_cal=0.607101487700022 cal (allowed 1.0 … None)
- 3-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind0: minimum_ascent_stability_cal=0.6328679403535403 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind2: minimum_ascent_stability_cal=0.7308122352680839 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7293057604199525 cal (allowed 1.0 … None)
- 4-dummy-D12-5-wind0: landing_descent_m_s=6.382196412337185 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind2: landing_descent_m_s=6.3821236919416044 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind4: landing_descent_m_s=6.382050884102744 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind0: landing_descent_m_s=6.3821964123371835 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind2: landing_descent_m_s=6.382123691941604 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind4: landing_descent_m_s=6.382050884102744 m/s (allowed None … 6.0)
- 5-empty-D12-5-wind0: minimum_ascent_stability_cal=0.6328679403535403 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind2: minimum_ascent_stability_cal=0.7308122352679585 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7293057604199525 cal (allowed 1.0 … None)
- 5-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind0: minimum_ascent_stability_cal=0.6328679403535403 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind2: minimum_ascent_stability_cal=0.7308122352678491 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7293057604199525 cal (allowed 1.0 … None)
- 6-dummy-D12-5-wind0: landing_descent_m_s=6.382196412337268 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind2: landing_descent_m_s=6.382123691872002 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind4: landing_descent_m_s=6.382050883734466 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind0: landing_descent_m_s=6.382196412337268 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind2: landing_descent_m_s=6.382123691872002 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind4: landing_descent_m_s=6.382050883734466 m/s (allowed None … 6.0)
- 7-empty-D12-5-wind0: minimum_ascent_stability_cal=0.6328679403535403 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind2: minimum_ascent_stability_cal=0.730812235267781 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7293057604199525 cal (allowed 1.0 … None)
- 7-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 7-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs

## Deterministic stress envelope

These are bounded scenario corners, not probabilities or reliability estimates.

```json
{
  "schema_version": 1,
  "print_mass_factors": [1.0, 1.2],
  "payload_cg_offsets_mm": [-5.0, 5.0],
  "chute_cd": [0.6, 0.9],
  "wind_m_s": [0.0, 2.0, 4.0],
  "max_cases": 72,
  "source": "Engineering stress envelope, not measured distributions: print mass +0/+20%, payload CG +/-5 mm, chute Cd 0.6/0.9, uniform wind 0/2/4 m/s"
}
```

Each case records its applied factors in results.json and has a resolved corner input file.

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
    "pydantic": "2.13.5"
  }
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
