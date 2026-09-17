# Rocket Workbench report

Run: `stress-20260913T160922Z-8180d281`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `dbea598291f5bd80681de0c1d81081fc3371dbfa40e375a29dbf2413e024d89a`

## Cases

| Case                 | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| -------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        5.69 |    0.10 |           15.14 |            16.13 |             67.63 |
| 0-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        5.69 |   52.98 |           15.13 |            16.13 |             67.49 |
| 0-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        5.69 |  108.06 |           15.11 |            16.11 |             67.15 |
| 0-dummy-D12-5-wind0  | completed / outside configured limits |   189.08 |     12.97 |           1.41 |       1.41 |        6.03 |    0.09 |           13.55 |            14.54 |             60.84 |
| 0-dummy-D12-5-wind2  | completed / outside configured limits |   187.34 |     12.97 |           1.04 |       3.02 |        6.03 |   38.29 |           13.54 |            14.54 |             60.70 |
| 0-dummy-D12-5-wind4  | completed / outside configured limits |   182.60 |     12.96 |           0.98 |       5.76 |        6.03 |   76.84 |           13.53 |            14.53 |             60.32 |
| 0-actual-D12-5-wind0 | completed / outside configured limits |   189.08 |     12.97 |           1.41 |       1.41 |        6.03 |    0.09 |           13.55 |            14.54 |             60.84 |
| 0-actual-D12-5-wind2 | completed / outside configured limits |   187.34 |     12.97 |           1.04 |       3.02 |        6.03 |   38.29 |           13.54 |            14.54 |             60.70 |
| 0-actual-D12-5-wind4 | completed / outside configured limits |   182.60 |     12.96 |           0.98 |       5.76 |        6.03 |   76.84 |           13.53 |            14.53 |             60.32 |
| 1-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        4.65 |    0.10 |           15.14 |            16.13 |             67.63 |
| 1-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        4.65 |   70.01 |           15.13 |            16.13 |             67.49 |
| 1-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        4.65 |  141.28 |           15.11 |            16.11 |             67.15 |
| 1-dummy-D12-5-wind0  | completed / incomplete inputs         |   189.08 |     12.97 |           1.41 |       1.41 |        4.92 |    0.09 |           13.55 |            14.54 |             60.84 |
| 1-dummy-D12-5-wind2  | completed / incomplete inputs         |   187.34 |     12.97 |           1.04 |       3.02 |        4.92 |   52.80 |           13.54 |            14.54 |             60.70 |
| 1-dummy-D12-5-wind4  | completed / outside configured limits |   182.60 |     12.96 |           0.98 |       5.76 |        4.92 |  104.89 |           13.53 |            14.53 |             60.32 |
| 1-actual-D12-5-wind0 | completed / incomplete inputs         |   189.08 |     12.97 |           1.41 |       1.41 |        4.92 |    0.09 |           13.55 |            14.54 |             60.84 |
| 1-actual-D12-5-wind2 | completed / incomplete inputs         |   187.34 |     12.97 |           1.04 |       3.02 |        4.92 |   52.80 |           13.54 |            14.54 |             60.70 |
| 1-actual-D12-5-wind4 | completed / outside configured limits |   182.60 |     12.96 |           0.98 |       5.76 |        4.92 |  104.89 |           13.53 |            14.53 |             60.32 |
| 2-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        5.69 |    0.10 |           15.14 |            16.13 |             67.63 |
| 2-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        5.69 |   52.98 |           15.13 |            16.13 |             67.49 |
| 2-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        5.69 |  108.06 |           15.11 |            16.11 |             67.15 |
| 2-dummy-D12-5-wind0  | completed / outside configured limits |   189.08 |     12.97 |           1.39 |       1.41 |        6.03 |    0.09 |           13.55 |            14.54 |             60.84 |
| 2-dummy-D12-5-wind2  | completed / outside configured limits |   187.34 |     12.97 |           1.01 |       3.02 |        6.03 |   38.30 |           13.54 |            14.54 |             60.70 |
| 2-dummy-D12-5-wind4  | completed / outside configured limits |   182.62 |     12.96 |           0.96 |       5.75 |        6.03 |   76.93 |           13.53 |            14.53 |             60.32 |
| 2-actual-D12-5-wind0 | completed / outside configured limits |   189.08 |     12.97 |           1.39 |       1.41 |        6.03 |    0.09 |           13.55 |            14.54 |             60.84 |
| 2-actual-D12-5-wind2 | completed / outside configured limits |   187.34 |     12.97 |           1.01 |       3.02 |        6.03 |   38.30 |           13.54 |            14.54 |             60.70 |
| 2-actual-D12-5-wind4 | completed / outside configured limits |   182.62 |     12.96 |           0.96 |       5.75 |        6.03 |   76.93 |           13.53 |            14.53 |             60.32 |
| 3-empty-D12-5-wind0  | completed / incomplete inputs         |   211.52 |     13.28 |           1.21 |       0.59 |        4.65 |    0.10 |           15.14 |            16.13 |             67.63 |
| 3-empty-D12-5-wind2  | completed / outside configured limits |   210.05 |     13.27 |           0.49 |       2.15 |        4.65 |   70.01 |           15.13 |            16.13 |             67.49 |
| 3-empty-D12-5-wind4  | completed / outside configured limits |   206.29 |     13.27 |           0.48 |       3.92 |        4.65 |  141.28 |           15.11 |            16.11 |             67.15 |
| 3-dummy-D12-5-wind0  | completed / incomplete inputs         |   189.08 |     12.97 |           1.39 |       1.41 |        4.92 |    0.09 |           13.55 |            14.54 |             60.84 |
| 3-dummy-D12-5-wind2  | completed / incomplete inputs         |   187.34 |     12.97 |           1.01 |       3.02 |        4.92 |   52.81 |           13.54 |            14.54 |             60.70 |
| 3-dummy-D12-5-wind4  | completed / outside configured limits |   182.62 |     12.96 |           0.96 |       5.75 |        4.92 |  104.98 |           13.53 |            14.53 |             60.32 |
| 3-actual-D12-5-wind0 | completed / incomplete inputs         |   189.08 |     12.97 |           1.39 |       1.41 |        4.92 |    0.09 |           13.55 |            14.54 |             60.84 |
| 3-actual-D12-5-wind2 | completed / incomplete inputs         |   187.34 |     12.97 |           1.01 |       3.02 |        4.92 |   52.81 |           13.54 |            14.54 |             60.70 |
| 3-actual-D12-5-wind4 | completed / outside configured limits |   182.62 |     12.96 |           0.96 |       5.75 |        4.92 |  104.98 |           13.53 |            14.53 |             60.32 |
| 4-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        5.95 |    0.09 |           13.90 |            14.90 |             62.41 |
| 4-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        5.95 |   42.65 |           13.90 |            14.90 |             62.27 |
| 4-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        5.95 |   86.79 |           13.89 |            14.88 |             61.91 |
| 4-dummy-D12-5-wind0  | completed / outside configured limits |   172.81 |     12.62 |           1.48 |       3.17 |        6.27 |    0.08 |           12.54 |            13.54 |             56.30 |
| 4-dummy-D12-5-wind2  | completed / outside configured limits |   170.98 |     12.62 |           1.14 |       4.23 |        6.27 |   29.56 |           12.53 |            13.53 |             56.15 |
| 4-dummy-D12-5-wind4  | completed / outside configured limits |   166.00 |     12.61 |           1.06 |       7.16 |        6.27 |   59.03 |           12.52 |            13.52 |             55.75 |
| 4-actual-D12-5-wind0 | completed / outside configured limits |   172.81 |     12.62 |           1.48 |       3.17 |        6.27 |    0.08 |           12.54 |            13.54 |             56.30 |
| 4-actual-D12-5-wind2 | completed / outside configured limits |   170.98 |     12.62 |           1.14 |       4.23 |        6.27 |   29.56 |           12.53 |            13.53 |             56.15 |
| 4-actual-D12-5-wind4 | completed / outside configured limits |   166.00 |     12.61 |           1.06 |       7.16 |        6.27 |   59.03 |           12.52 |            13.52 |             55.75 |
| 5-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        4.86 |    0.09 |           13.90 |            14.90 |             62.41 |
| 5-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        4.86 |   57.74 |           13.90 |            14.90 |             62.27 |
| 5-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        4.86 |  116.08 |           13.89 |            14.88 |             61.91 |
| 5-dummy-D12-5-wind0  | completed / incomplete inputs         |   172.81 |     12.62 |           1.48 |       3.17 |        5.12 |    0.08 |           12.54 |            13.54 |             56.30 |
| 5-dummy-D12-5-wind2  | completed / incomplete inputs         |   170.98 |     12.62 |           1.14 |       4.23 |        5.12 |   42.38 |           12.53 |            13.53 |             56.15 |
| 5-dummy-D12-5-wind4  | completed / incomplete inputs         |   166.00 |     12.61 |           1.06 |       7.16 |        5.12 |   83.66 |           12.52 |            13.52 |             55.75 |
| 5-actual-D12-5-wind0 | completed / incomplete inputs         |   172.81 |     12.62 |           1.48 |       3.17 |        5.12 |    0.08 |           12.54 |            13.54 |             56.30 |
| 5-actual-D12-5-wind2 | completed / incomplete inputs         |   170.98 |     12.62 |           1.14 |       4.23 |        5.12 |   42.38 |           12.53 |            13.53 |             56.15 |
| 5-actual-D12-5-wind4 | completed / incomplete inputs         |   166.00 |     12.61 |           1.06 |       7.16 |        5.12 |   83.66 |           12.52 |            13.52 |             55.75 |
| 6-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        5.95 |    0.09 |           13.90 |            14.90 |             62.41 |
| 6-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        5.95 |   42.65 |           13.90 |            14.90 |             62.27 |
| 6-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        5.95 |   86.79 |           13.89 |            14.88 |             61.91 |
| 6-dummy-D12-5-wind0  | completed / outside configured limits |   172.81 |     12.62 |           1.46 |       3.17 |        6.27 |    0.08 |           12.54 |            13.54 |             56.30 |
| 6-dummy-D12-5-wind2  | completed / outside configured limits |   170.98 |     12.62 |           1.12 |       4.22 |        6.27 |   29.57 |           12.53 |            13.53 |             56.15 |
| 6-dummy-D12-5-wind4  | completed / outside configured limits |   166.01 |     12.61 |           1.03 |       7.15 |        6.27 |   59.11 |           12.52 |            13.52 |             55.76 |
| 6-actual-D12-5-wind0 | completed / outside configured limits |   172.81 |     12.62 |           1.46 |       3.17 |        6.27 |    0.08 |           12.54 |            13.54 |             56.30 |
| 6-actual-D12-5-wind2 | completed / outside configured limits |   170.98 |     12.62 |           1.12 |       4.22 |        6.27 |   29.57 |           12.53 |            13.53 |             56.15 |
| 6-actual-D12-5-wind4 | completed / outside configured limits |   166.01 |     12.61 |           1.03 |       7.15 |        6.27 |   59.11 |           12.52 |            13.52 |             55.76 |
| 7-empty-D12-5-wind0  | completed / incomplete inputs         |   194.49 |     13.09 |           1.19 |       0.88 |        4.86 |    0.09 |           13.90 |            14.90 |             62.41 |
| 7-empty-D12-5-wind2  | completed / outside configured limits |   192.91 |     13.09 |           0.57 |       2.54 |        4.86 |   57.74 |           13.90 |            14.90 |             62.27 |
| 7-empty-D12-5-wind4  | completed / outside configured limits |   188.76 |     13.08 |           0.61 |       4.87 |        4.86 |  116.08 |           13.89 |            14.88 |             61.91 |
| 7-dummy-D12-5-wind0  | completed / incomplete inputs         |   172.81 |     12.62 |           1.46 |       3.17 |        5.12 |    0.08 |           12.54 |            13.54 |             56.30 |
| 7-dummy-D12-5-wind2  | completed / incomplete inputs         |   170.98 |     12.62 |           1.12 |       4.22 |        5.12 |   42.39 |           12.53 |            13.53 |             56.15 |
| 7-dummy-D12-5-wind4  | completed / incomplete inputs         |   166.01 |     12.61 |           1.03 |       7.15 |        5.12 |   83.74 |           12.52 |            13.52 |             55.76 |
| 7-actual-D12-5-wind0 | completed / incomplete inputs         |   172.81 |     12.62 |           1.46 |       3.17 |        5.12 |    0.08 |           12.54 |            13.54 |             56.30 |
| 7-actual-D12-5-wind2 | completed / incomplete inputs         |   170.98 |     12.62 |           1.12 |       4.22 |        5.12 |   42.39 |           12.53 |            13.53 |             56.15 |
| 7-actual-D12-5-wind4 | completed / incomplete inputs         |   166.01 |     12.61 |           1.03 |       7.15 |        5.12 |   83.74 |           12.52 |            13.52 |             55.76 |

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
- 0-empty-D12-5-wind2: minimum_ascent_stability_cal=0.4942877471315874 cal (allowed 1.0 … None)
- 0-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111717 cal (allowed 1.0 … None)
- 0-dummy-D12-5-wind0: landing_descent_m_s=6.026923642929603 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind2: landing_descent_m_s=6.026854772537421 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind4: minimum_ascent_stability_cal=0.9827880492534912 cal (allowed 1.0 … None);
  landing_descent_m_s=6.026786113214636 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind0: landing_descent_m_s=6.026923642929603 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind2: landing_descent_m_s=6.026854772537422 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind4: minimum_ascent_stability_cal=0.9827880492534912 cal (allowed 1.0 … None);
  landing_descent_m_s=6.026786113214636 m/s (allowed None … 6.0)
- 1-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-D12-5-wind2: minimum_ascent_stability_cal=0.49428774713173423 cal (allowed 1.0 … None)
- 1-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111717 cal (allowed 1.0 … None)
- 1-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind4: minimum_ascent_stability_cal=0.9827880492534898 cal (allowed 1.0 … None)
- 1-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind4: minimum_ascent_stability_cal=0.9827880492534898 cal (allowed 1.0 … None)
- 2-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind2: minimum_ascent_stability_cal=0.4942877471316061 cal (allowed 1.0 … None)
- 2-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111717 cal (allowed 1.0 … None)
- 2-dummy-D12-5-wind0: landing_descent_m_s=6.0269236429280095 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind2: landing_descent_m_s=6.026854772555168 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind4: minimum_ascent_stability_cal=0.9589409117814232 cal (allowed 1.0 … None);
  landing_descent_m_s=6.026786112990884 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind0: landing_descent_m_s=6.0269236429280095 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind2: landing_descent_m_s=6.026854772555168 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind4: minimum_ascent_stability_cal=0.9589409117814218 cal (allowed 1.0 … None);
  landing_descent_m_s=6.026786112990885 m/s (allowed None … 6.0)
- 3-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-D12-5-wind2: minimum_ascent_stability_cal=0.4942877471314927 cal (allowed 1.0 … None)
- 3-empty-D12-5-wind4: minimum_ascent_stability_cal=0.47829475823111717 cal (allowed 1.0 … None)
- 3-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind4: minimum_ascent_stability_cal=0.9589409117814232 cal (allowed 1.0 … None)
- 3-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind4: minimum_ascent_stability_cal=0.9589409117814232 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460983876 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685161 cal (allowed 1.0 … None)
- 4-dummy-D12-5-wind0: landing_descent_m_s=6.268166797059213 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind2: landing_descent_m_s=6.268095286223148 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind4: landing_descent_m_s=6.268023807804828 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind0: landing_descent_m_s=6.268166797059213 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind2: landing_descent_m_s=6.268095286223148 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind4: landing_descent_m_s=6.268023807804828 m/s (allowed None … 6.0)
- 5-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460982262 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685161 cal (allowed 1.0 … None)
- 5-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460983663 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685161 cal (allowed 1.0 … None)
- 6-dummy-D12-5-wind0: landing_descent_m_s=6.26816679705913 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind2: landing_descent_m_s=6.268095286247016 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind4: landing_descent_m_s=6.2680238077624075 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind0: landing_descent_m_s=6.26816679705913 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind2: landing_descent_m_s=6.268095286247016 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind4: landing_descent_m_s=6.2680238077624075 m/s (allowed None … 6.0)
- 7-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5698127460983876 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6074676093685161 cal (allowed 1.0 … None)
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
