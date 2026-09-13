# Rocket Workbench report

Run: `stress-20260913T041111Z-9744740b`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `d04936a042b1e1189238526a303d19d3b9a20c94e24e35ee9ba01975bacaa08d`

## Cases

| Case                | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-C5-3-wind0  | completed / incomplete inputs         |    75.77 |     13.29 |           1.51 |       3.75 |        5.33 |    0.02 |           12.19 |            13.19 |             27.86 |
| 0-empty-C5-3-wind2  | completed / incomplete inputs         |    74.10 |     13.28 |           1.03 |       4.91 |        5.33 |   10.80 |           12.18 |            13.18 |             27.68 |
| 0-empty-C5-3-wind4  | completed / outside configured limits |    69.82 |     13.28 |           0.95 |       8.14 |        5.33 |   21.26 |           12.17 |            13.17 |             27.22 |
| 0-dummy-C5-3-wind0  | completed / incomplete inputs         |    53.85 |     12.18 |           2.20 |       8.81 |        5.82 |    0.15 |           10.14 |            11.13 |             21.37 |
| 0-dummy-C5-3-wind2  | completed / outside configured limits |    51.89 |     12.17 |           1.87 |      10.10 |        5.82 |    3.34 |           10.13 |            11.13 |             21.23 |
| 0-dummy-C5-3-wind4  | completed / outside configured limits |    47.06 |     12.17 |           1.61 |      13.45 |        5.82 |    7.60 |           10.12 |            11.12 |             20.89 |
| 0-actual-C5-3-wind0 | completed / incomplete inputs         |    53.85 |     12.18 |           2.20 |       8.81 |        5.82 |    0.15 |           10.14 |            11.13 |             21.37 |
| 0-actual-C5-3-wind2 | completed / outside configured limits |    51.89 |     12.17 |           1.87 |      10.10 |        5.82 |    3.34 |           10.13 |            11.13 |             21.23 |
| 0-actual-C5-3-wind4 | completed / outside configured limits |    47.06 |     12.17 |           1.61 |      13.45 |        5.82 |    7.60 |           10.12 |            11.12 |             20.89 |
| 1-empty-C5-3-wind0  | completed / incomplete inputs         |    75.77 |     13.29 |           1.51 |       3.75 |        4.35 |    0.02 |           12.19 |            13.19 |             27.86 |
| 1-empty-C5-3-wind2  | completed / incomplete inputs         |    74.10 |     13.28 |           1.03 |       4.91 |        4.35 |   17.51 |           12.18 |            13.18 |             27.68 |
| 1-empty-C5-3-wind4  | completed / outside configured limits |    69.82 |     13.28 |           0.95 |       8.14 |        4.35 |   33.61 |           12.17 |            13.17 |             27.22 |
| 1-dummy-C5-3-wind0  | completed / incomplete inputs         |    53.85 |     12.18 |           2.20 |       8.81 |        4.76 |    0.12 |           10.14 |            11.13 |             21.37 |
| 1-dummy-C5-3-wind2  | completed / outside configured limits |    51.89 |     12.17 |           1.87 |      10.10 |        4.76 |    0.87 |           10.13 |            11.13 |             21.23 |
| 1-dummy-C5-3-wind4  | completed / outside configured limits |    47.06 |     12.17 |           1.61 |      13.45 |        4.76 |    0.38 |           10.12 |            11.12 |             20.89 |
| 1-actual-C5-3-wind0 | completed / incomplete inputs         |    53.85 |     12.18 |           2.20 |       8.81 |        4.76 |    0.12 |           10.14 |            11.13 |             21.37 |
| 1-actual-C5-3-wind2 | completed / outside configured limits |    51.89 |     12.17 |           1.87 |      10.10 |        4.76 |    0.87 |           10.13 |            11.13 |             21.23 |
| 1-actual-C5-3-wind4 | completed / outside configured limits |    47.06 |     12.17 |           1.61 |      13.45 |        4.76 |    0.38 |           10.12 |            11.12 |             20.89 |
| 2-empty-C5-3-wind0  | completed / incomplete inputs         |    75.77 |     13.29 |           1.51 |       3.75 |        5.33 |    0.02 |           12.19 |            13.19 |             27.86 |
| 2-empty-C5-3-wind2  | completed / incomplete inputs         |    74.10 |     13.28 |           1.03 |       4.91 |        5.33 |   10.80 |           12.18 |            13.18 |             27.68 |
| 2-empty-C5-3-wind4  | completed / outside configured limits |    69.82 |     13.28 |           0.95 |       8.14 |        5.33 |   21.26 |           12.17 |            13.17 |             27.22 |
| 2-dummy-C5-3-wind0  | completed / incomplete inputs         |    53.85 |     12.18 |           2.16 |       8.81 |        5.82 |    0.15 |           10.14 |            11.13 |             21.37 |
| 2-dummy-C5-3-wind2  | completed / outside configured limits |    51.89 |     12.17 |           1.84 |      10.10 |        5.82 |    3.34 |           10.13 |            11.13 |             21.24 |
| 2-dummy-C5-3-wind4  | completed / outside configured limits |    47.07 |     12.17 |           1.57 |      13.44 |        5.82 |    7.55 |           10.12 |            11.12 |             20.90 |
| 2-actual-C5-3-wind0 | completed / incomplete inputs         |    53.85 |     12.18 |           2.16 |       8.81 |        5.82 |    0.15 |           10.14 |            11.13 |             21.37 |
| 2-actual-C5-3-wind2 | completed / outside configured limits |    51.89 |     12.17 |           1.84 |      10.10 |        5.82 |    3.34 |           10.13 |            11.13 |             21.24 |
| 2-actual-C5-3-wind4 | completed / outside configured limits |    47.07 |     12.17 |           1.57 |      13.44 |        5.82 |    7.55 |           10.12 |            11.12 |             20.90 |
| 3-empty-C5-3-wind0  | completed / incomplete inputs         |    75.77 |     13.29 |           1.51 |       3.75 |        4.35 |    0.02 |           12.19 |            13.19 |             27.86 |
| 3-empty-C5-3-wind2  | completed / incomplete inputs         |    74.10 |     13.28 |           1.03 |       4.91 |        4.35 |   17.51 |           12.18 |            13.18 |             27.68 |
| 3-empty-C5-3-wind4  | completed / outside configured limits |    69.82 |     13.28 |           0.95 |       8.14 |        4.35 |   33.61 |           12.17 |            13.17 |             27.22 |
| 3-dummy-C5-3-wind0  | completed / incomplete inputs         |    53.85 |     12.18 |           2.16 |       8.81 |        4.76 |    0.12 |           10.14 |            11.13 |             21.37 |
| 3-dummy-C5-3-wind2  | completed / outside configured limits |    51.89 |     12.17 |           1.84 |      10.10 |        4.76 |    0.88 |           10.13 |            11.13 |             21.24 |
| 3-dummy-C5-3-wind4  | completed / outside configured limits |    47.07 |     12.17 |           1.57 |      13.44 |        4.76 |    0.34 |           10.12 |            11.12 |             20.90 |
| 3-actual-C5-3-wind0 | completed / incomplete inputs         |    53.85 |     12.18 |           2.16 |       8.81 |        4.76 |    0.12 |           10.14 |            11.13 |             21.37 |
| 3-actual-C5-3-wind2 | completed / outside configured limits |    51.89 |     12.17 |           1.84 |      10.10 |        4.76 |    0.88 |           10.13 |            11.13 |             21.24 |
| 3-actual-C5-3-wind4 | completed / outside configured limits |    47.07 |     12.17 |           1.57 |      13.44 |        4.76 |    0.34 |           10.12 |            11.12 |             20.90 |
| 4-empty-C5-3-wind0  | completed / incomplete inputs         |    63.11 |     12.71 |           1.59 |       6.57 |        5.60 |    0.04 |           11.01 |            12.00 |             24.18 |
| 4-empty-C5-3-wind2  | completed / incomplete inputs         |    61.36 |     12.70 |           1.17 |       7.47 |        5.60 |    3.28 |           11.00 |            12.00 |             24.02 |
| 4-empty-C5-3-wind4  | completed / outside configured limits |    56.95 |     12.70 |           1.03 |      10.76 |        5.60 |    6.00 |           10.99 |            11.99 |             23.62 |
| 4-dummy-C5-3-wind0  | completed / outside configured limits |    44.98 |     11.67 |           1.55 |      10.91 |        6.07 |    0.41 |            9.28 |            10.28 |             18.52 |
| 4-dummy-C5-3-wind2  | completed / outside configured limits |    42.89 |     11.66 |           1.89 |      12.71 |        6.07 |    9.07 |            9.27 |            10.27 |             18.41 |
| 4-dummy-C5-3-wind4  | completed / outside configured limits |    38.02 |     11.66 |           1.63 |      16.05 |        6.07 |   18.77 |            9.27 |            10.27 |             18.14 |
| 4-actual-C5-3-wind0 | completed / outside configured limits |    44.98 |     11.67 |           1.55 |      10.91 |        6.07 |    0.41 |            9.28 |            10.28 |             18.52 |
| 4-actual-C5-3-wind2 | completed / outside configured limits |    42.89 |     11.66 |           1.89 |      12.71 |        6.07 |    9.07 |            9.27 |            10.27 |             18.41 |
| 4-actual-C5-3-wind4 | completed / outside configured limits |    38.02 |     11.66 |           1.63 |      16.05 |        6.07 |   18.77 |            9.27 |            10.27 |             18.14 |
| 5-empty-C5-3-wind0  | completed / incomplete inputs         |    63.11 |     12.71 |           1.59 |       6.57 |        4.57 |    0.03 |           11.01 |            12.00 |             24.18 |
| 5-empty-C5-3-wind2  | completed / incomplete inputs         |    61.36 |     12.70 |           1.17 |       7.47 |        4.57 |    8.54 |           11.00 |            12.00 |             24.02 |
| 5-empty-C5-3-wind4  | completed / outside configured limits |    56.95 |     12.70 |           1.03 |      10.76 |        4.57 |   15.44 |           10.99 |            11.99 |             23.62 |
| 5-dummy-C5-3-wind0  | completed / outside configured limits |    44.98 |     11.67 |           1.55 |      10.91 |        4.96 |    0.34 |            9.28 |            10.28 |             18.52 |
| 5-dummy-C5-3-wind2  | completed / outside configured limits |    42.89 |     11.66 |           1.89 |      12.71 |        4.96 |    5.87 |            9.27 |            10.27 |             18.41 |
| 5-dummy-C5-3-wind4  | completed / outside configured limits |    38.02 |     11.66 |           1.63 |      16.05 |        4.96 |   13.66 |            9.27 |            10.27 |             18.14 |
| 5-actual-C5-3-wind0 | completed / outside configured limits |    44.98 |     11.67 |           1.55 |      10.91 |        4.96 |    0.34 |            9.28 |            10.28 |             18.52 |
| 5-actual-C5-3-wind2 | completed / outside configured limits |    42.89 |     11.66 |           1.89 |      12.71 |        4.96 |    5.87 |            9.27 |            10.27 |             18.41 |
| 5-actual-C5-3-wind4 | completed / outside configured limits |    38.02 |     11.66 |           1.63 |      16.05 |        4.96 |   13.66 |            9.27 |            10.27 |             18.14 |
| 6-empty-C5-3-wind0  | completed / incomplete inputs         |    63.11 |     12.71 |           1.59 |       6.57 |        5.60 |    0.04 |           11.01 |            12.00 |             24.18 |
| 6-empty-C5-3-wind2  | completed / incomplete inputs         |    61.36 |     12.70 |           1.17 |       7.47 |        5.60 |    3.28 |           11.00 |            12.00 |             24.02 |
| 6-empty-C5-3-wind4  | completed / outside configured limits |    56.95 |     12.70 |           1.03 |      10.76 |        5.60 |    6.00 |           10.99 |            11.99 |             23.62 |
| 6-dummy-C5-3-wind0  | completed / outside configured limits |    44.98 |     11.67 |           1.51 |      10.91 |        6.07 |    0.41 |            9.28 |            10.28 |             18.52 |
| 6-dummy-C5-3-wind2  | completed / outside configured limits |    42.89 |     11.66 |           1.86 |      12.71 |        6.07 |    9.07 |            9.27 |            10.27 |             18.41 |
| 6-dummy-C5-3-wind4  | completed / outside configured limits |    38.03 |     11.66 |           1.59 |      16.04 |        6.07 |   18.72 |            9.27 |            10.27 |             18.14 |
| 6-actual-C5-3-wind0 | completed / outside configured limits |    44.98 |     11.67 |           1.51 |      10.91 |        6.07 |    0.41 |            9.28 |            10.28 |             18.52 |
| 6-actual-C5-3-wind2 | completed / outside configured limits |    42.89 |     11.66 |           1.86 |      12.71 |        6.07 |    9.07 |            9.27 |            10.27 |             18.41 |
| 6-actual-C5-3-wind4 | completed / outside configured limits |    38.03 |     11.66 |           1.59 |      16.04 |        6.07 |   18.72 |            9.27 |            10.27 |             18.14 |
| 7-empty-C5-3-wind0  | completed / incomplete inputs         |    63.11 |     12.71 |           1.59 |       6.57 |        4.57 |    0.03 |           11.01 |            12.00 |             24.18 |
| 7-empty-C5-3-wind2  | completed / incomplete inputs         |    61.36 |     12.70 |           1.17 |       7.47 |        4.57 |    8.54 |           11.00 |            12.00 |             24.02 |
| 7-empty-C5-3-wind4  | completed / outside configured limits |    56.95 |     12.70 |           1.03 |      10.76 |        4.57 |   15.44 |           10.99 |            11.99 |             23.62 |
| 7-dummy-C5-3-wind0  | completed / outside configured limits |    44.98 |     11.67 |           1.51 |      10.91 |        4.96 |    0.34 |            9.28 |            10.28 |             18.52 |
| 7-dummy-C5-3-wind2  | completed / outside configured limits |    42.89 |     11.66 |           1.86 |      12.71 |        4.96 |    5.87 |            9.27 |            10.27 |             18.41 |
| 7-dummy-C5-3-wind4  | completed / outside configured limits |    38.03 |     11.66 |           1.59 |      16.04 |        4.96 |   13.61 |            9.27 |            10.27 |             18.14 |
| 7-actual-C5-3-wind0 | completed / outside configured limits |    44.98 |     11.67 |           1.51 |      10.91 |        4.96 |    0.34 |            9.28 |            10.28 |             18.52 |
| 7-actual-C5-3-wind2 | completed / outside configured limits |    42.89 |     11.66 |           1.86 |      12.71 |        4.96 |    5.87 |            9.27 |            10.27 |             18.41 |
| 7-actual-C5-3-wind4 | completed / outside configured limits |    38.03 |     11.66 |           1.59 |      16.04 |        4.96 |   13.61 |            9.27 |            10.27 |             18.14 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- 0-empty-C5-3-wind0: no engine warnings
- 0-empty-C5-3-wind2: no engine warnings
- 0-empty-C5-3-wind4: no engine warnings
- 0-dummy-C5-3-wind0: no engine warnings
- 0-dummy-C5-3-wind2: no engine warnings
- 0-dummy-C5-3-wind4: no engine warnings
- 0-actual-C5-3-wind0: no engine warnings
- 0-actual-C5-3-wind2: no engine warnings
- 0-actual-C5-3-wind4: no engine warnings
- 1-empty-C5-3-wind0: no engine warnings
- 1-empty-C5-3-wind2: no engine warnings
- 1-empty-C5-3-wind4: no engine warnings
- 1-dummy-C5-3-wind0: no engine warnings
- 1-dummy-C5-3-wind2: no engine warnings
- 1-dummy-C5-3-wind4: no engine warnings
- 1-actual-C5-3-wind0: no engine warnings
- 1-actual-C5-3-wind2: no engine warnings
- 1-actual-C5-3-wind4: no engine warnings
- 2-empty-C5-3-wind0: no engine warnings
- 2-empty-C5-3-wind2: no engine warnings
- 2-empty-C5-3-wind4: no engine warnings
- 2-dummy-C5-3-wind0: no engine warnings
- 2-dummy-C5-3-wind2: no engine warnings
- 2-dummy-C5-3-wind4: no engine warnings
- 2-actual-C5-3-wind0: no engine warnings
- 2-actual-C5-3-wind2: no engine warnings
- 2-actual-C5-3-wind4: no engine warnings
- 3-empty-C5-3-wind0: no engine warnings
- 3-empty-C5-3-wind2: no engine warnings
- 3-empty-C5-3-wind4: no engine warnings
- 3-dummy-C5-3-wind0: no engine warnings
- 3-dummy-C5-3-wind2: no engine warnings
- 3-dummy-C5-3-wind4: no engine warnings
- 3-actual-C5-3-wind0: no engine warnings
- 3-actual-C5-3-wind2: no engine warnings
- 3-actual-C5-3-wind4: no engine warnings
- 4-empty-C5-3-wind0: no engine warnings
- 4-empty-C5-3-wind2: no engine warnings
- 4-empty-C5-3-wind4: no engine warnings
- 4-dummy-C5-3-wind0: no engine warnings
- 4-dummy-C5-3-wind2: no engine warnings
- 4-dummy-C5-3-wind4: no engine warnings
- 4-actual-C5-3-wind0: no engine warnings
- 4-actual-C5-3-wind2: no engine warnings
- 4-actual-C5-3-wind4: no engine warnings
- 5-empty-C5-3-wind0: no engine warnings
- 5-empty-C5-3-wind2: no engine warnings
- 5-empty-C5-3-wind4: no engine warnings
- 5-dummy-C5-3-wind0: no engine warnings
- 5-dummy-C5-3-wind2: no engine warnings
- 5-dummy-C5-3-wind4: no engine warnings
- 5-actual-C5-3-wind0: no engine warnings
- 5-actual-C5-3-wind2: no engine warnings
- 5-actual-C5-3-wind4: no engine warnings
- 6-empty-C5-3-wind0: no engine warnings
- 6-empty-C5-3-wind2: no engine warnings
- 6-empty-C5-3-wind4: no engine warnings
- 6-dummy-C5-3-wind0: no engine warnings
- 6-dummy-C5-3-wind2: no engine warnings
- 6-dummy-C5-3-wind4: no engine warnings
- 6-actual-C5-3-wind0: no engine warnings
- 6-actual-C5-3-wind2: no engine warnings
- 6-actual-C5-3-wind4: no engine warnings
- 7-empty-C5-3-wind0: no engine warnings
- 7-empty-C5-3-wind2: no engine warnings
- 7-empty-C5-3-wind4: no engine warnings
- 7-dummy-C5-3-wind0: no engine warnings
- 7-dummy-C5-3-wind2: no engine warnings
- 7-dummy-C5-3-wind4: no engine warnings
- 7-actual-C5-3-wind0: no engine warnings
- 7-actual-C5-3-wind2: no engine warnings
- 7-actual-C5-3-wind4: no engine warnings

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

- 0-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 0-empty-C5-3-wind4: minimum_ascent_stability_cal=0.9476279337631374 cal (allowed 1.0 … None)
- 0-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-dummy-C5-3-wind2: deployment_speed_m_s=10.1011926471107 m/s (allowed None … 10.0)
- 0-dummy-C5-3-wind4: deployment_speed_m_s=13.451845741700879 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-actual-C5-3-wind2: deployment_speed_m_s=10.101192647110691 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind4: deployment_speed_m_s=13.45184574170085 m/s (allowed None … 10.0)
- 1-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind4: minimum_ascent_stability_cal=0.9476279337631387 cal (allowed 1.0 … None)
- 1-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind2: deployment_speed_m_s=10.101192647110736 m/s (allowed None … 10.0)
- 1-dummy-C5-3-wind4: deployment_speed_m_s=13.451845741700863 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-C5-3-wind2: deployment_speed_m_s=10.101192647110725 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind4: deployment_speed_m_s=13.451845741700781 m/s (allowed None … 10.0)
- 2-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind4: minimum_ascent_stability_cal=0.9476279337631387 cal (allowed 1.0 … None)
- 2-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind2: deployment_speed_m_s=10.101199850593401 m/s (allowed None … 10.0)
- 2-dummy-C5-3-wind4: deployment_speed_m_s=13.444386258988988 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-actual-C5-3-wind2: deployment_speed_m_s=10.10119985059345 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind4: deployment_speed_m_s=13.444386258988981 m/s (allowed None … 10.0)
- 3-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind4: minimum_ascent_stability_cal=0.9476279337631387 cal (allowed 1.0 … None)
- 3-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind2: deployment_speed_m_s=10.101199850593426 m/s (allowed None … 10.0)
- 3-dummy-C5-3-wind4: deployment_speed_m_s=13.44438625898881 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-C5-3-wind2: deployment_speed_m_s=10.101199850593416 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind4: deployment_speed_m_s=13.444386258988958 m/s (allowed None … 10.0)
- 4-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind4: deployment_speed_m_s=10.757601449676113 m/s (allowed None … 10.0)
- 4-dummy-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.910887581054034 m/s (allowed None … 10.0); landing_descent_m_s=6.073349277471828 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.706922300943944 m/s (allowed None … 10.0); landing_descent_m_s=6.073279996287849 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.045884968160845 m/s (allowed None … 10.0); landing_descent_m_s=6.073210713714415 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.910887581054034 m/s (allowed None … 10.0); landing_descent_m_s=6.073349277471828 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.706922300943909 m/s (allowed None … 10.0); landing_descent_m_s=6.073279996287849 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.045884968160806 m/s (allowed None … 10.0); landing_descent_m_s=6.073210713714415 m/s (allowed
  None … 6.0)
- 5-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind4: deployment_speed_m_s=10.757601449675862 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.910887581054034 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.70692230094391 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.0458849681608 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.910887581054034 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.706922300943914 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.045884968160806 m/s (allowed None … 10.0)
- 6-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind4: deployment_speed_m_s=10.757601449675894 m/s (allowed None … 10.0)
- 6-dummy-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.90708006706059 m/s (allowed None … 10.0); landing_descent_m_s=6.073349277638242 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.706890374755433 m/s (allowed None … 10.0); landing_descent_m_s=6.073279995818526 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.035406142357655 m/s (allowed None … 10.0); landing_descent_m_s=6.073210713979047 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.90708006706059 m/s (allowed None … 10.0); landing_descent_m_s=6.073349277638242 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.706890374755769 m/s (allowed None … 10.0); landing_descent_m_s=6.073279995818526 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.03540614235765 m/s (allowed None … 10.0); landing_descent_m_s=6.073210713979047 m/s (allowed
  None … 6.0)
- 7-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind4: deployment_speed_m_s=10.757601449675878 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.90708006706059 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.706890374755766 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.035406142357672 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind0: guide_departure_m_s=11.667177953546787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.90708006706059 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind2: guide_departure_m_s=11.661560376564227 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.706890374755764 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind4: guide_departure_m_s=11.659697544194932 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.03540614235765 m/s (allowed None … 10.0)

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
    "pydantic": "2.13.5"
  }
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
