# Rocket Workbench report

Run: `stress-20260913T161008Z-c6a25181`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `de7d24e44ea1c5f680109647df53b39abec2911e3d54086de0143bfce67acd64`

## Cases

| Case                 | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| -------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        5.69 |    0.10 |           15.14 |            16.13 |             67.63 |
| 0-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        5.69 |   52.98 |           15.13 |            16.13 |             67.49 |
| 0-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        5.69 |  108.06 |           15.11 |            16.11 |             67.15 |
| 0-dummy-D12-5-wind0  | completed / outside configured limits |   180.07 |     12.86 |           1.76 |       2.35 |        6.16 |    0.08 |           12.98 |            13.97 |             58.30 |
| 0-dummy-D12-5-wind2  | completed / outside configured limits |   178.24 |     12.85 |           1.27 |       3.69 |        6.16 |   32.99 |           12.97 |            13.97 |             58.15 |
| 0-dummy-D12-5-wind4  | completed / outside configured limits |   173.21 |     12.85 |           1.17 |       6.63 |        6.16 |   65.79 |           12.96 |            13.96 |             57.76 |
| 0-actual-D12-5-wind0 | completed / outside configured limits |   180.07 |     12.86 |           1.76 |       2.35 |        6.16 |    0.08 |           12.98 |            13.97 |             58.30 |
| 0-actual-D12-5-wind2 | completed / outside configured limits |   178.24 |     12.85 |           1.27 |       3.69 |        6.16 |   32.99 |           12.97 |            13.97 |             58.15 |
| 0-actual-D12-5-wind4 | completed / outside configured limits |   173.21 |     12.85 |           1.17 |       6.63 |        6.16 |   65.79 |           12.96 |            13.96 |             57.76 |
| 1-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        4.65 |    0.10 |           15.14 |            16.13 |             67.63 |
| 1-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        4.65 |   70.01 |           15.13 |            16.13 |             67.49 |
| 1-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        4.65 |  141.28 |           15.11 |            16.11 |             67.15 |
| 1-dummy-D12-5-wind0  | completed / incomplete inputs         |   180.07 |     12.86 |           1.76 |       2.35 |        5.03 |    0.08 |           12.98 |            13.97 |             58.30 |
| 1-dummy-D12-5-wind2  | completed / incomplete inputs         |   178.24 |     12.85 |           1.27 |       3.69 |        5.03 |   46.56 |           12.97 |            13.97 |             58.15 |
| 1-dummy-D12-5-wind4  | completed / incomplete inputs         |   173.21 |     12.85 |           1.17 |       6.63 |        5.03 |   91.91 |           12.96 |            13.96 |             57.76 |
| 1-actual-D12-5-wind0 | completed / incomplete inputs         |   180.07 |     12.86 |           1.76 |       2.35 |        5.03 |    0.08 |           12.98 |            13.97 |             58.30 |
| 1-actual-D12-5-wind2 | completed / incomplete inputs         |   178.24 |     12.85 |           1.27 |       3.69 |        5.03 |   46.56 |           12.97 |            13.97 |             58.15 |
| 1-actual-D12-5-wind4 | completed / incomplete inputs         |   173.21 |     12.85 |           1.17 |       6.63 |        5.03 |   91.91 |           12.96 |            13.96 |             57.76 |
| 2-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        5.69 |    0.10 |           15.14 |            16.13 |             67.63 |
| 2-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        5.69 |   52.98 |           15.13 |            16.13 |             67.49 |
| 2-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        5.69 |  108.06 |           15.11 |            16.11 |             67.15 |
| 2-dummy-D12-5-wind0  | completed / outside configured limits |   180.07 |     12.86 |           1.73 |       2.35 |        6.16 |    0.08 |           12.98 |            13.97 |             58.30 |
| 2-dummy-D12-5-wind2  | completed / outside configured limits |   178.24 |     12.85 |           1.24 |       3.69 |        6.16 |   33.00 |           12.97 |            13.97 |             58.15 |
| 2-dummy-D12-5-wind4  | completed / outside configured limits |   173.23 |     12.85 |           1.14 |       6.62 |        6.16 |   65.87 |           12.96 |            13.96 |             57.76 |
| 2-actual-D12-5-wind0 | completed / outside configured limits |   180.07 |     12.86 |           1.73 |       2.35 |        6.16 |    0.08 |           12.98 |            13.97 |             58.30 |
| 2-actual-D12-5-wind2 | completed / outside configured limits |   178.24 |     12.85 |           1.24 |       3.69 |        6.16 |   33.00 |           12.97 |            13.97 |             58.15 |
| 2-actual-D12-5-wind4 | completed / outside configured limits |   173.23 |     12.85 |           1.14 |       6.62 |        6.16 |   65.87 |           12.96 |            13.96 |             57.76 |
| 3-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        4.65 |    0.10 |           15.14 |            16.13 |             67.63 |
| 3-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        4.65 |   70.01 |           15.13 |            16.13 |             67.49 |
| 3-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        4.65 |  141.28 |           15.11 |            16.11 |             67.15 |
| 3-dummy-D12-5-wind0  | completed / incomplete inputs         |   180.07 |     12.86 |           1.73 |       2.35 |        5.03 |    0.08 |           12.98 |            13.97 |             58.30 |
| 3-dummy-D12-5-wind2  | completed / incomplete inputs         |   178.24 |     12.85 |           1.24 |       3.69 |        5.03 |   46.57 |           12.97 |            13.97 |             58.15 |
| 3-dummy-D12-5-wind4  | completed / incomplete inputs         |   173.23 |     12.85 |           1.14 |       6.62 |        5.03 |   91.99 |           12.96 |            13.96 |             57.76 |
| 3-actual-D12-5-wind0 | completed / incomplete inputs         |   180.07 |     12.86 |           1.73 |       2.35 |        5.03 |    0.08 |           12.98 |            13.97 |             58.30 |
| 3-actual-D12-5-wind2 | completed / incomplete inputs         |   178.24 |     12.85 |           1.24 |       3.69 |        5.03 |   46.57 |           12.97 |            13.97 |             58.15 |
| 3-actual-D12-5-wind4 | completed / incomplete inputs         |   173.23 |     12.85 |           1.14 |       6.62 |        5.03 |   91.99 |           12.96 |            13.96 |             57.76 |
| 4-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        5.95 |    0.09 |           13.90 |            14.90 |             62.41 |
| 4-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        5.95 |   42.65 |           13.90 |            14.90 |             62.27 |
| 4-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        5.95 |   86.79 |           13.89 |            14.88 |             61.91 |
| 4-dummy-D12-5-wind0  | completed / outside configured limits |   164.26 |     12.54 |           1.18 |       4.19 |        6.40 |    0.06 |           12.04 |            13.04 |             54.01 |
| 4-dummy-D12-5-wind2  | completed / outside configured limits |   162.36 |     12.53 |           1.37 |       5.10 |        6.40 |   24.87 |           12.03 |            13.03 |             53.86 |
| 4-dummy-D12-5-wind4  | completed / outside configured limits |   157.14 |     12.53 |           1.23 |       8.16 |        6.40 |   49.20 |           12.03 |            13.03 |             53.45 |
| 4-actual-D12-5-wind0 | completed / outside configured limits |   164.26 |     12.54 |           1.18 |       4.19 |        6.40 |    0.06 |           12.04 |            13.04 |             54.01 |
| 4-actual-D12-5-wind2 | completed / outside configured limits |   162.36 |     12.53 |           1.37 |       5.10 |        6.40 |   24.87 |           12.03 |            13.03 |             53.86 |
| 4-actual-D12-5-wind4 | completed / outside configured limits |   157.14 |     12.53 |           1.23 |       8.16 |        6.40 |   49.20 |           12.03 |            13.03 |             53.45 |
| 5-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        4.86 |    0.09 |           13.90 |            14.90 |             62.41 |
| 5-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        4.86 |   57.74 |           13.90 |            14.90 |             62.27 |
| 5-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        4.86 |  116.08 |           13.89 |            14.88 |             61.91 |
| 5-dummy-D12-5-wind0  | completed / incomplete inputs         |   164.26 |     12.54 |           1.18 |       4.19 |        5.22 |    0.07 |           12.04 |            13.04 |             54.01 |
| 5-dummy-D12-5-wind2  | completed / incomplete inputs         |   162.36 |     12.53 |           1.37 |       5.10 |        5.22 |   36.82 |           12.03 |            13.03 |             53.86 |
| 5-dummy-D12-5-wind4  | completed / incomplete inputs         |   157.14 |     12.53 |           1.23 |       8.16 |        5.22 |   72.09 |           12.03 |            13.03 |             53.45 |
| 5-actual-D12-5-wind0 | completed / incomplete inputs         |   164.26 |     12.54 |           1.18 |       4.19 |        5.22 |    0.07 |           12.04 |            13.04 |             54.01 |
| 5-actual-D12-5-wind2 | completed / incomplete inputs         |   162.36 |     12.53 |           1.37 |       5.10 |        5.22 |   36.82 |           12.03 |            13.03 |             53.86 |
| 5-actual-D12-5-wind4 | completed / incomplete inputs         |   157.14 |     12.53 |           1.23 |       8.16 |        5.22 |   72.09 |           12.03 |            13.03 |             53.45 |
| 6-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        5.95 |    0.09 |           13.90 |            14.90 |             62.41 |
| 6-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        5.95 |   42.65 |           13.90 |            14.90 |             62.27 |
| 6-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        5.95 |   86.79 |           13.89 |            14.88 |             61.91 |
| 6-dummy-D12-5-wind0  | completed / outside configured limits |   164.26 |     12.54 |           1.15 |       4.19 |        6.40 |    0.06 |           12.04 |            13.04 |             54.01 |
| 6-dummy-D12-5-wind2  | completed / outside configured limits |   162.36 |     12.53 |           1.33 |       5.10 |        6.40 |   24.87 |           12.03 |            13.03 |             53.86 |
| 6-dummy-D12-5-wind4  | completed / outside configured limits |   157.16 |     12.53 |           1.20 |       8.15 |        6.40 |   49.28 |           12.03 |            13.03 |             53.45 |
| 6-actual-D12-5-wind0 | completed / outside configured limits |   164.26 |     12.54 |           1.15 |       4.19 |        6.40 |    0.06 |           12.04 |            13.04 |             54.01 |
| 6-actual-D12-5-wind2 | completed / outside configured limits |   162.36 |     12.53 |           1.33 |       5.10 |        6.40 |   24.87 |           12.03 |            13.03 |             53.86 |
| 6-actual-D12-5-wind4 | completed / outside configured limits |   157.16 |     12.53 |           1.20 |       8.15 |        6.40 |   49.28 |           12.03 |            13.03 |             53.45 |
| 7-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        4.86 |    0.09 |           13.90 |            14.90 |             62.41 |
| 7-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        4.86 |   57.74 |           13.90 |            14.90 |             62.27 |
| 7-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        4.86 |  116.08 |           13.89 |            14.88 |             61.91 |
| 7-dummy-D12-5-wind0  | completed / incomplete inputs         |   164.26 |     12.54 |           1.15 |       4.19 |        5.22 |    0.07 |           12.04 |            13.04 |             54.01 |
| 7-dummy-D12-5-wind2  | completed / incomplete inputs         |   162.36 |     12.53 |           1.33 |       5.10 |        5.22 |   36.83 |           12.03 |            13.03 |             53.86 |
| 7-dummy-D12-5-wind4  | completed / incomplete inputs         |   157.16 |     12.53 |           1.20 |       8.15 |        5.22 |   72.16 |           12.03 |            13.03 |             53.45 |
| 7-actual-D12-5-wind0 | completed / incomplete inputs         |   164.26 |     12.54 |           1.15 |       4.19 |        5.22 |    0.07 |           12.04 |            13.04 |             54.01 |
| 7-actual-D12-5-wind2 | completed / incomplete inputs         |   162.36 |     12.53 |           1.33 |       5.10 |        5.22 |   36.83 |           12.03 |            13.03 |             53.86 |
| 7-actual-D12-5-wind4 | completed / incomplete inputs         |   157.16 |     12.53 |           1.20 |       8.15 |        5.22 |   72.16 |           12.03 |            13.03 |             53.45 |

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
- 0-empty-D12-5-wind2: minimum_ascent_stability_cal=0.49428774713153006 cal (allowed 1.0 … None)
- 0-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111717 cal (allowed 1.0 … None)
- 0-dummy-D12-5-wind0: landing_descent_m_s=6.160264845795353 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind2: landing_descent_m_s=6.160194565084796 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind4: landing_descent_m_s=6.160124361172342 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind0: landing_descent_m_s=6.160264845795353 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind2: landing_descent_m_s=6.160194565084797 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind4: landing_descent_m_s=6.160124361172342 m/s (allowed None … 6.0)
- 1-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-D12-5-wind2: minimum_ascent_stability_cal=0.4942877471317329 cal (allowed 1.0 … None)
- 1-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111584 cal (allowed 1.0 … None)
- 1-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind2: minimum_ascent_stability_cal=0.4942877471315527 cal (allowed 1.0 … None)
- 2-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111584 cal (allowed 1.0 … None)
- 2-dummy-D12-5-wind0: landing_descent_m_s=6.160264845795201 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind2: landing_descent_m_s=6.160194565011932 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind4: landing_descent_m_s=6.160124361045688 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind0: landing_descent_m_s=6.160264845795201 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind2: landing_descent_m_s=6.160194565011932 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind4: landing_descent_m_s=6.160124361045688 m/s (allowed None … 6.0)
- 3-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-D12-5-wind2: minimum_ascent_stability_cal=0.49428774713183565 cal (allowed 1.0 … None)
- 3-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111584 cal (allowed 1.0 … None)
- 3-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460983036 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685161 cal (allowed 1.0 … None)
- 4-dummy-D12-5-wind0: landing_descent_m_s=6.396484651135525 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind2: landing_descent_m_s=6.39641180059153 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind4: landing_descent_m_s=6.396338773330079 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind0: landing_descent_m_s=6.396484651135525 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind2: landing_descent_m_s=6.39641180059153 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind4: landing_descent_m_s=6.396338773330079 m/s (allowed None … 6.0)
- 5-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460982916 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685161 cal (allowed 1.0 … None)
- 5-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460982756 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685161 cal (allowed 1.0 … None)
- 6-dummy-D12-5-wind0: landing_descent_m_s=6.396484651134687 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind2: landing_descent_m_s=6.396411800497534 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind4: landing_descent_m_s=6.3963387730078045 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind0: landing_descent_m_s=6.396484651134687 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind2: landing_descent_m_s=6.396411800497536 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind4: landing_descent_m_s=6.3963387730078045 m/s (allowed None … 6.0)
- 7-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460982902 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685174 cal (allowed 1.0 … None)
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
