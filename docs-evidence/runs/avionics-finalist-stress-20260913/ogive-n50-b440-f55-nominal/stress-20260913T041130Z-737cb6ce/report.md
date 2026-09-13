# Rocket Workbench report

Run: `stress-20260913T041130Z-737cb6ce`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `382a80593874ed5c91e80afec7820f1156507d6ed99e4d768c4b23c544a27f71`

## Cases

| Case                | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        5.45 |    0.01 |           11.61 |            12.61 |             26.25 |
| 0-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        5.45 |    6.45 |           11.61 |            12.61 |             26.08 |
| 0-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        5.45 |   12.47 |           11.60 |            12.60 |             25.67 |
| 0-dummy-C5-3-wind0  | completed / incomplete inputs         |    55.05 |     12.28 |           2.57 |       8.45 |        5.80 |    0.18 |           10.22 |            11.21 |             21.73 |
| 0-dummy-C5-3-wind2  | completed / incomplete inputs         |    53.03 |     12.27 |           2.34 |       9.90 |        5.80 |    3.32 |           10.21 |            11.21 |             21.59 |
| 0-dummy-C5-3-wind4  | completed / outside configured limits |    48.04 |     12.27 |           2.02 |      13.34 |        5.80 |    7.41 |           10.20 |            11.20 |             21.23 |
| 0-actual-C5-3-wind0 | completed / incomplete inputs         |    55.05 |     12.28 |           2.57 |       8.45 |        5.80 |    0.18 |           10.22 |            11.21 |             21.73 |
| 0-actual-C5-3-wind2 | completed / incomplete inputs         |    53.03 |     12.27 |           2.34 |       9.90 |        5.80 |    3.32 |           10.21 |            11.21 |             21.59 |
| 0-actual-C5-3-wind4 | completed / outside configured limits |    48.04 |     12.27 |           2.02 |      13.34 |        5.80 |    7.41 |           10.20 |            11.20 |             21.23 |
| 1-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        4.45 |    0.00 |           11.61 |            12.61 |             26.25 |
| 1-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        4.45 |   12.53 |           11.61 |            12.61 |             26.08 |
| 1-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        4.45 |   23.49 |           11.60 |            12.60 |             25.67 |
| 1-dummy-C5-3-wind0  | completed / incomplete inputs         |    55.05 |     12.28 |           2.57 |       8.45 |        4.74 |    0.15 |           10.22 |            11.21 |             21.73 |
| 1-dummy-C5-3-wind2  | completed / incomplete inputs         |    53.03 |     12.27 |           2.34 |       9.90 |        4.74 |    1.03 |           10.21 |            11.21 |             21.59 |
| 1-dummy-C5-3-wind4  | completed / outside configured limits |    48.04 |     12.27 |           2.02 |      13.34 |        4.74 |    0.06 |           10.20 |            11.20 |             21.23 |
| 1-actual-C5-3-wind0 | completed / incomplete inputs         |    55.05 |     12.28 |           2.57 |       8.45 |        4.74 |    0.15 |           10.22 |            11.21 |             21.73 |
| 1-actual-C5-3-wind2 | completed / incomplete inputs         |    53.03 |     12.27 |           2.34 |       9.90 |        4.74 |    1.03 |           10.21 |            11.21 |             21.59 |
| 1-actual-C5-3-wind4 | completed / outside configured limits |    48.04 |     12.27 |           2.02 |      13.34 |        4.74 |    0.06 |           10.20 |            11.20 |             21.23 |
| 2-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        5.45 |    0.01 |           11.61 |            12.61 |             26.25 |
| 2-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        5.45 |    6.45 |           11.61 |            12.61 |             26.08 |
| 2-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        5.45 |   12.47 |           11.60 |            12.60 |             25.67 |
| 2-dummy-C5-3-wind0  | completed / incomplete inputs         |    55.05 |     12.28 |           2.54 |       8.45 |        5.80 |    0.18 |           10.22 |            11.21 |             21.73 |
| 2-dummy-C5-3-wind2  | completed / incomplete inputs         |    53.03 |     12.27 |           2.31 |       9.90 |        5.80 |    3.33 |           10.21 |            11.21 |             21.59 |
| 2-dummy-C5-3-wind4  | completed / outside configured limits |    48.05 |     12.27 |           1.99 |      13.34 |        5.80 |    7.38 |           10.20 |            11.20 |             21.23 |
| 2-actual-C5-3-wind0 | completed / incomplete inputs         |    55.05 |     12.28 |           2.54 |       8.45 |        5.80 |    0.18 |           10.22 |            11.21 |             21.73 |
| 2-actual-C5-3-wind2 | completed / incomplete inputs         |    53.03 |     12.27 |           2.31 |       9.90 |        5.80 |    3.33 |           10.21 |            11.21 |             21.59 |
| 2-actual-C5-3-wind4 | completed / outside configured limits |    48.05 |     12.27 |           1.99 |      13.34 |        5.80 |    7.38 |           10.20 |            11.20 |             21.23 |
| 3-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        4.45 |    0.00 |           11.61 |            12.61 |             26.25 |
| 3-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        4.45 |   12.53 |           11.61 |            12.61 |             26.08 |
| 3-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        4.45 |   23.49 |           11.60 |            12.60 |             25.67 |
| 3-dummy-C5-3-wind0  | completed / incomplete inputs         |    55.05 |     12.28 |           2.54 |       8.45 |        4.74 |    0.15 |           10.22 |            11.21 |             21.73 |
| 3-dummy-C5-3-wind2  | completed / incomplete inputs         |    53.03 |     12.27 |           2.31 |       9.90 |        4.74 |    1.03 |           10.21 |            11.21 |             21.59 |
| 3-dummy-C5-3-wind4  | completed / outside configured limits |    48.05 |     12.27 |           1.99 |      13.34 |        4.74 |    0.09 |           10.20 |            11.20 |             21.23 |
| 3-actual-C5-3-wind0 | completed / incomplete inputs         |    55.05 |     12.28 |           2.54 |       8.45 |        4.74 |    0.15 |           10.22 |            11.21 |             21.73 |
| 3-actual-C5-3-wind2 | completed / incomplete inputs         |    53.03 |     12.27 |           2.31 |       9.90 |        4.74 |    1.03 |           10.21 |            11.21 |             21.59 |
| 3-actual-C5-3-wind4 | completed / outside configured limits |    48.05 |     12.27 |           1.99 |      13.34 |        4.74 |    0.09 |           10.20 |            11.20 |             21.23 |
| 4-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        5.74 |    0.13 |           10.46 |            11.45 |             22.52 |
| 4-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        5.74 |    1.18 |           10.45 |            11.45 |             22.37 |
| 4-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        5.74 |    2.94 |           10.44 |            11.44 |             21.99 |
| 4-dummy-C5-3-wind0  | completed / outside configured limits |    45.29 |     11.68 |           2.51 |      10.65 |        6.07 |    0.49 |            9.29 |            10.29 |             18.62 |
| 4-dummy-C5-3-wind2  | completed / outside configured limits |    43.18 |     11.67 |           2.37 |      12.66 |        6.07 |    9.37 |            9.28 |            10.28 |             18.53 |
| 4-dummy-C5-3-wind4  | completed / outside configured limits |    38.24 |     11.67 |           2.05 |      16.05 |        6.07 |   19.11 |            9.28 |            10.28 |             18.30 |
| 4-actual-C5-3-wind0 | completed / outside configured limits |    45.29 |     11.68 |           2.51 |      10.65 |        6.07 |    0.49 |            9.29 |            10.29 |             18.62 |
| 4-actual-C5-3-wind2 | completed / outside configured limits |    43.18 |     11.67 |           2.37 |      12.66 |        6.07 |    9.37 |            9.28 |            10.28 |             18.53 |
| 4-actual-C5-3-wind4 | completed / outside configured limits |    38.24 |     11.67 |           2.05 |      16.05 |        6.07 |   19.11 |            9.28 |            10.28 |             18.30 |
| 5-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        4.69 |    0.10 |           10.46 |            11.45 |             22.52 |
| 5-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        4.69 |    3.46 |           10.45 |            11.45 |             22.37 |
| 5-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        4.69 |    5.17 |           10.44 |            11.44 |             21.99 |
| 5-dummy-C5-3-wind0  | completed / outside configured limits |    45.29 |     11.68 |           2.51 |      10.65 |        4.96 |    0.42 |            9.29 |            10.29 |             18.62 |
| 5-dummy-C5-3-wind2  | completed / outside configured limits |    43.18 |     11.67 |           2.37 |      12.66 |        4.96 |    6.12 |            9.28 |            10.28 |             18.53 |
| 5-dummy-C5-3-wind4  | completed / outside configured limits |    38.24 |     11.67 |           2.05 |      16.05 |        4.96 |   13.92 |            9.28 |            10.28 |             18.30 |
| 5-actual-C5-3-wind0 | completed / outside configured limits |    45.29 |     11.68 |           2.51 |      10.65 |        4.96 |    0.42 |            9.29 |            10.29 |             18.62 |
| 5-actual-C5-3-wind2 | completed / outside configured limits |    43.18 |     11.67 |           2.37 |      12.66 |        4.96 |    6.12 |            9.28 |            10.28 |             18.53 |
| 5-actual-C5-3-wind4 | completed / outside configured limits |    38.24 |     11.67 |           2.05 |      16.05 |        4.96 |   13.92 |            9.28 |            10.28 |             18.30 |
| 6-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        5.74 |    0.13 |           10.46 |            11.45 |             22.52 |
| 6-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        5.74 |    1.18 |           10.45 |            11.45 |             22.37 |
| 6-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        5.74 |    2.94 |           10.44 |            11.44 |             21.99 |
| 6-dummy-C5-3-wind0  | completed / outside configured limits |    45.29 |     11.68 |           2.49 |      10.65 |        6.07 |    0.49 |            9.29 |            10.29 |             18.62 |
| 6-dummy-C5-3-wind2  | completed / outside configured limits |    43.18 |     11.67 |           2.35 |      12.66 |        6.07 |    9.37 |            9.28 |            10.28 |             18.53 |
| 6-dummy-C5-3-wind4  | completed / outside configured limits |    38.25 |     11.67 |           2.02 |      16.05 |        6.07 |   19.10 |            9.28 |            10.28 |             18.30 |
| 6-actual-C5-3-wind0 | completed / outside configured limits |    45.29 |     11.68 |           2.49 |      10.65 |        6.07 |    0.49 |            9.29 |            10.29 |             18.62 |
| 6-actual-C5-3-wind2 | completed / outside configured limits |    43.18 |     11.67 |           2.35 |      12.66 |        6.07 |    9.37 |            9.28 |            10.28 |             18.53 |
| 6-actual-C5-3-wind4 | completed / outside configured limits |    38.25 |     11.67 |           2.02 |      16.05 |        6.07 |   19.10 |            9.28 |            10.28 |             18.30 |
| 7-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        4.69 |    0.10 |           10.46 |            11.45 |             22.52 |
| 7-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        4.69 |    3.46 |           10.45 |            11.45 |             22.37 |
| 7-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        4.69 |    5.17 |           10.44 |            11.44 |             21.99 |
| 7-dummy-C5-3-wind0  | completed / outside configured limits |    45.29 |     11.68 |           2.49 |      10.65 |        4.96 |    0.42 |            9.29 |            10.29 |             18.62 |
| 7-dummy-C5-3-wind2  | completed / outside configured limits |    43.18 |     11.67 |           2.35 |      12.66 |        4.96 |    6.12 |            9.28 |            10.28 |             18.53 |
| 7-dummy-C5-3-wind4  | completed / outside configured limits |    38.25 |     11.67 |           2.02 |      16.05 |        4.96 |   13.91 |            9.28 |            10.28 |             18.30 |
| 7-actual-C5-3-wind0 | completed / outside configured limits |    45.29 |     11.68 |           2.49 |      10.65 |        4.96 |    0.42 |            9.29 |            10.29 |             18.62 |
| 7-actual-C5-3-wind2 | completed / outside configured limits |    43.18 |     11.67 |           2.35 |      12.66 |        4.96 |    6.12 |            9.28 |            10.28 |             18.53 |
| 7-actual-C5-3-wind4 | completed / outside configured limits |    38.25 |     11.67 |           2.02 |      16.05 |        4.96 |   13.91 |            9.28 |            10.28 |             18.30 |

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
- 0-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 0-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 0-dummy-C5-3-wind4: deployment_speed_m_s=13.34189916499618 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 0-actual-C5-3-wind4: deployment_speed_m_s=13.341899164996176 m/s (allowed None … 10.0)
- 1-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind4: deployment_speed_m_s=13.341899164996047 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-C5-3-wind4: deployment_speed_m_s=13.341899164996063 m/s (allowed None … 10.0)
- 2-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind4: deployment_speed_m_s=13.33779672504944 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-actual-C5-3-wind4: deployment_speed_m_s=13.337796725049381 m/s (allowed None … 10.0)
- 3-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind4: deployment_speed_m_s=13.337796725049294 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-C5-3-wind4: deployment_speed_m_s=13.337796725049564 m/s (allowed None … 10.0)
- 4-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173327 m/s (allowed None … 10.0)
- 4-dummy-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.6515572779813 m/s (allowed None … 10.0); landing_descent_m_s=6.070881633209207 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.66453741707507 m/s (allowed None … 10.0); landing_descent_m_s=6.070812409512917 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.047650858152128 m/s (allowed None … 10.0); landing_descent_m_s=6.070743187563213 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.6515572779813 m/s (allowed None … 10.0); landing_descent_m_s=6.070881633209207 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.664537417074893 m/s (allowed None … 10.0); landing_descent_m_s=6.070812409512917 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.047650858152263 m/s (allowed None … 10.0); landing_descent_m_s=6.070743187563213 m/s (allowed
  None … 6.0)
- 5-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173323 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.6515572779813 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.664537417074897 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.04765085815221 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.6515572779813 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.664537417074905 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.047650858152068 m/s (allowed None … 10.0)
- 6-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173325 m/s (allowed None … 10.0)
- 6-dummy-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.648524983469752 m/s (allowed None … 10.0); landing_descent_m_s=6.070881633614783 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.663723538353802 m/s (allowed None … 10.0); landing_descent_m_s=6.070812409189482 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.045202084919744 m/s (allowed None … 10.0); landing_descent_m_s=6.070743187365876 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.648524983469752 m/s (allowed None … 10.0); landing_descent_m_s=6.070881633614783 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.663723538353803 m/s (allowed None … 10.0); landing_descent_m_s=6.070812409189482 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.045202084919765 m/s (allowed None … 10.0); landing_descent_m_s=6.070743187365876 m/s (allowed
  None … 6.0)
- 7-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173368 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.648524983469752 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.6637235383538 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.045202084919634 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind0: guide_departure_m_s=11.679112556323913 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.648524983469752 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind2: guide_departure_m_s=11.67384014112369 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.663723538353798 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind4: guide_departure_m_s=11.67213700681044 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.045202084919744 m/s (allowed None … 10.0)

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
