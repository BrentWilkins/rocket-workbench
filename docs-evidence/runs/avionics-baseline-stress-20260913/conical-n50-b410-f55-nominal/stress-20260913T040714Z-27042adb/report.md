# Rocket Workbench report

Run: `stress-20260913T040714Z-27042adb`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `01c77124cb32511cf9fe60a844ed28b497a2655e9549a9429f030aad8a091e45`

## Cases

| Case                | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        5.38 |    0.00 |           11.96 |            12.96 |             26.99 |
| 0-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        5.38 |    8.48 |           11.95 |            12.95 |             26.82 |
| 0-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        5.38 |   16.37 |           11.94 |            12.94 |             26.39 |
| 0-dummy-C5-3-wind0  | completed / incomplete inputs         |    57.18 |     12.47 |           1.77 |       8.02 |        5.73 |    0.15 |           10.49 |            11.49 |             22.41 |
| 0-dummy-C5-3-wind2  | completed / incomplete inputs         |    55.15 |     12.46 |           2.05 |       9.41 |        5.73 |    1.74 |           10.48 |            11.48 |             22.25 |
| 0-dummy-C5-3-wind4  | completed / outside configured limits |    50.18 |     12.46 |           1.78 |      12.74 |        5.73 |    4.30 |           10.47 |            11.47 |             21.87 |
| 0-actual-C5-3-wind0 | completed / incomplete inputs         |    57.18 |     12.47 |           1.77 |       8.02 |        5.73 |    0.15 |           10.49 |            11.49 |             22.41 |
| 0-actual-C5-3-wind2 | completed / incomplete inputs         |    55.15 |     12.46 |           2.05 |       9.41 |        5.73 |    1.74 |           10.48 |            11.48 |             22.25 |
| 0-actual-C5-3-wind4 | completed / outside configured limits |    50.18 |     12.46 |           1.78 |      12.74 |        5.73 |    4.30 |           10.47 |            11.47 |             21.87 |
| 1-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        4.39 |    0.01 |           11.96 |            12.96 |             26.99 |
| 1-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        4.39 |   14.83 |           11.95 |            12.95 |             26.82 |
| 1-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        4.39 |   27.95 |           11.94 |            12.94 |             26.39 |
| 1-dummy-C5-3-wind0  | completed / incomplete inputs         |    57.18 |     12.47 |           1.77 |       8.02 |        4.68 |    0.12 |           10.49 |            11.49 |             22.41 |
| 1-dummy-C5-3-wind2  | completed / incomplete inputs         |    55.15 |     12.46 |           2.05 |       9.41 |        4.68 |    2.82 |           10.48 |            11.48 |             22.25 |
| 1-dummy-C5-3-wind4  | completed / outside configured limits |    50.18 |     12.46 |           1.78 |      12.74 |        4.68 |    3.63 |           10.47 |            11.47 |             21.87 |
| 1-actual-C5-3-wind0 | completed / incomplete inputs         |    57.18 |     12.47 |           1.77 |       8.02 |        4.68 |    0.12 |           10.49 |            11.49 |             22.41 |
| 1-actual-C5-3-wind2 | completed / incomplete inputs         |    55.15 |     12.46 |           2.05 |       9.41 |        4.68 |    2.82 |           10.48 |            11.48 |             22.25 |
| 1-actual-C5-3-wind4 | completed / outside configured limits |    50.18 |     12.46 |           1.78 |      12.74 |        4.68 |    3.63 |           10.47 |            11.47 |             21.87 |
| 2-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        5.38 |    0.00 |           11.96 |            12.96 |             26.99 |
| 2-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        5.38 |    8.48 |           11.95 |            12.95 |             26.82 |
| 2-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        5.38 |   16.37 |           11.94 |            12.94 |             26.39 |
| 2-dummy-C5-3-wind0  | completed / incomplete inputs         |    57.18 |     12.47 |           1.74 |       8.02 |        5.73 |    0.15 |           10.49 |            11.49 |             22.41 |
| 2-dummy-C5-3-wind2  | completed / incomplete inputs         |    55.15 |     12.46 |           2.02 |       9.41 |        5.73 |    1.74 |           10.48 |            11.48 |             22.25 |
| 2-dummy-C5-3-wind4  | completed / outside configured limits |    50.19 |     12.46 |           1.75 |      12.73 |        5.73 |    4.28 |           10.47 |            11.47 |             21.86 |
| 2-actual-C5-3-wind0 | completed / incomplete inputs         |    57.18 |     12.47 |           1.74 |       8.02 |        5.73 |    0.15 |           10.49 |            11.49 |             22.41 |
| 2-actual-C5-3-wind2 | completed / incomplete inputs         |    55.15 |     12.46 |           2.02 |       9.41 |        5.73 |    1.74 |           10.48 |            11.48 |             22.25 |
| 2-actual-C5-3-wind4 | completed / outside configured limits |    50.19 |     12.46 |           1.75 |      12.73 |        5.73 |    4.28 |           10.47 |            11.47 |             21.86 |
| 3-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        4.39 |    0.01 |           11.96 |            12.96 |             26.99 |
| 3-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        4.39 |   14.83 |           11.95 |            12.95 |             26.82 |
| 3-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        4.39 |   27.95 |           11.94 |            12.94 |             26.39 |
| 3-dummy-C5-3-wind0  | completed / incomplete inputs         |    57.18 |     12.47 |           1.74 |       8.02 |        4.68 |    0.12 |           10.49 |            11.49 |             22.41 |
| 3-dummy-C5-3-wind2  | completed / incomplete inputs         |    55.15 |     12.46 |           2.02 |       9.41 |        4.68 |    2.82 |           10.48 |            11.48 |             22.25 |
| 3-dummy-C5-3-wind4  | completed / outside configured limits |    50.19 |     12.46 |           1.75 |      12.73 |        4.68 |    3.65 |           10.47 |            11.47 |             21.86 |
| 3-actual-C5-3-wind0 | completed / incomplete inputs         |    57.18 |     12.47 |           1.74 |       8.02 |        4.68 |    0.12 |           10.49 |            11.49 |             22.41 |
| 3-actual-C5-3-wind2 | completed / incomplete inputs         |    55.15 |     12.46 |           2.02 |       9.41 |        4.68 |    2.82 |           10.48 |            11.48 |             22.25 |
| 3-actual-C5-3-wind4 | completed / outside configured limits |    50.19 |     12.46 |           1.75 |      12.73 |        4.68 |    3.65 |           10.47 |            11.47 |             21.86 |
| 4-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        5.65 |    0.10 |           10.78 |            11.78 |             23.34 |
| 4-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        5.65 |    0.68 |           10.77 |            11.77 |             23.17 |
| 4-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        5.65 |    0.77 |           10.76 |            11.76 |             22.75 |
| 4-dummy-C5-3-wind0  | completed / outside configured limits |    47.49 |     11.83 |           2.09 |      10.23 |        5.99 |    0.41 |            9.55 |            10.55 |             19.36 |
| 4-dummy-C5-3-wind2  | completed / outside configured limits |    45.38 |     11.82 |           2.08 |      12.03 |        5.99 |    7.75 |            9.54 |            10.54 |             19.24 |
| 4-dummy-C5-3-wind4  | completed / outside configured limits |    40.39 |     11.82 |           1.80 |      15.34 |        5.99 |   16.17 |            9.54 |            10.54 |             18.95 |
| 4-actual-C5-3-wind0 | completed / outside configured limits |    47.49 |     11.83 |           2.09 |      10.23 |        5.99 |    0.41 |            9.55 |            10.55 |             19.36 |
| 4-actual-C5-3-wind2 | completed / outside configured limits |    45.38 |     11.82 |           2.08 |      12.03 |        5.99 |    7.75 |            9.54 |            10.54 |             19.24 |
| 4-actual-C5-3-wind4 | completed / outside configured limits |    40.39 |     11.82 |           1.80 |      15.34 |        5.99 |   16.17 |            9.54 |            10.54 |             18.95 |
| 5-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        4.62 |    0.08 |           10.78 |            11.78 |             23.34 |
| 5-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        4.62 |    5.63 |           10.77 |            11.77 |             23.17 |
| 5-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        4.62 |    9.45 |           10.76 |            11.76 |             22.75 |
| 5-dummy-C5-3-wind0  | completed / outside configured limits |    47.49 |     11.83 |           2.09 |      10.23 |        4.89 |    0.34 |            9.55 |            10.55 |             19.36 |
| 5-dummy-C5-3-wind2  | completed / outside configured limits |    45.38 |     11.82 |           2.08 |      12.03 |        4.89 |    4.27 |            9.54 |            10.54 |             19.24 |
| 5-dummy-C5-3-wind4  | completed / outside configured limits |    40.39 |     11.82 |           1.80 |      15.34 |        4.89 |   10.49 |            9.54 |            10.54 |             18.95 |
| 5-actual-C5-3-wind0 | completed / outside configured limits |    47.49 |     11.83 |           2.09 |      10.23 |        4.89 |    0.34 |            9.55 |            10.55 |             19.36 |
| 5-actual-C5-3-wind2 | completed / outside configured limits |    45.38 |     11.82 |           2.08 |      12.03 |        4.89 |    4.27 |            9.54 |            10.54 |             19.24 |
| 5-actual-C5-3-wind4 | completed / outside configured limits |    40.39 |     11.82 |           1.80 |      15.34 |        4.89 |   10.49 |            9.54 |            10.54 |             18.95 |
| 6-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        5.65 |    0.10 |           10.78 |            11.78 |             23.34 |
| 6-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        5.65 |    0.68 |           10.77 |            11.77 |             23.17 |
| 6-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        5.65 |    0.77 |           10.76 |            11.76 |             22.75 |
| 6-dummy-C5-3-wind0  | completed / outside configured limits |    47.49 |     11.83 |           2.06 |      10.23 |        5.99 |    0.41 |            9.55 |            10.55 |             19.36 |
| 6-dummy-C5-3-wind2  | completed / outside configured limits |    45.38 |     11.82 |           2.05 |      12.03 |        5.99 |    7.76 |            9.54 |            10.54 |             19.24 |
| 6-dummy-C5-3-wind4  | completed / outside configured limits |    40.40 |     11.82 |           1.77 |      15.33 |        5.99 |   16.17 |            9.54 |            10.54 |             18.96 |
| 6-actual-C5-3-wind0 | completed / outside configured limits |    47.49 |     11.83 |           2.06 |      10.23 |        5.99 |    0.41 |            9.55 |            10.55 |             19.36 |
| 6-actual-C5-3-wind2 | completed / outside configured limits |    45.38 |     11.82 |           2.05 |      12.03 |        5.99 |    7.76 |            9.54 |            10.54 |             19.24 |
| 6-actual-C5-3-wind4 | completed / outside configured limits |    40.40 |     11.82 |           1.77 |      15.33 |        5.99 |   16.17 |            9.54 |            10.54 |             18.96 |
| 7-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        4.62 |    0.08 |           10.78 |            11.78 |             23.34 |
| 7-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        4.62 |    5.63 |           10.77 |            11.77 |             23.17 |
| 7-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        4.62 |    9.45 |           10.76 |            11.76 |             22.75 |
| 7-dummy-C5-3-wind0  | completed / outside configured limits |    47.49 |     11.83 |           2.06 |      10.23 |        4.89 |    0.34 |            9.55 |            10.55 |             19.36 |
| 7-dummy-C5-3-wind2  | completed / outside configured limits |    45.38 |     11.82 |           2.05 |      12.03 |        4.89 |    4.28 |            9.54 |            10.54 |             19.24 |
| 7-dummy-C5-3-wind4  | completed / outside configured limits |    40.40 |     11.82 |           1.77 |      15.33 |        4.89 |   10.48 |            9.54 |            10.54 |             18.96 |
| 7-actual-C5-3-wind0 | completed / outside configured limits |    47.49 |     11.83 |           2.06 |      10.23 |        4.89 |    0.34 |            9.55 |            10.55 |             19.36 |
| 7-actual-C5-3-wind2 | completed / outside configured limits |    45.38 |     11.82 |           2.05 |      12.03 |        4.89 |    4.28 |            9.54 |            10.54 |             19.24 |
| 7-actual-C5-3-wind4 | completed / outside configured limits |    40.40 |     11.82 |           1.77 |      15.33 |        4.89 |   10.48 |            9.54 |            10.54 |             18.96 |

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
- 0-dummy-C5-3-wind4: deployment_speed_m_s=12.735036053683087 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 0-actual-C5-3-wind4: deployment_speed_m_s=12.735036053682947 m/s (allowed None … 10.0)
- 1-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind4: deployment_speed_m_s=12.73503605368305 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-C5-3-wind4: deployment_speed_m_s=12.735036053682903 m/s (allowed None … 10.0)
- 2-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind4: deployment_speed_m_s=12.731105888082405 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-actual-C5-3-wind4: deployment_speed_m_s=12.73110588808248 m/s (allowed None … 10.0)
- 3-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind4: deployment_speed_m_s=12.731105888082428 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-C5-3-wind4: deployment_speed_m_s=12.731105888082466 m/s (allowed None … 10.0)
- 4-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638786 m/s (allowed None … 10.0)
- 4-dummy-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22870515816807 m/s (allowed None … 10.0)
- 4-dummy-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.03002694303994 m/s (allowed None … 10.0)
- 4-dummy-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.335052056774604 m/s (allowed None … 10.0)
- 4-actual-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22870515816807 m/s (allowed None … 10.0)
- 4-actual-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.030026943039923 m/s (allowed None … 10.0)
- 4-actual-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.33505205677455 m/s (allowed None … 10.0)
- 5-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638706 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22870515816807 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.030026943039857 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.335052056774696 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22870515816807 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.030026943039951 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.335052056774614 m/s (allowed None … 10.0)
- 6-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638809 m/s (allowed None … 10.0)
- 6-dummy-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22576305710688 m/s (allowed None … 10.0)
- 6-dummy-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.031806579647059 m/s (allowed None … 10.0)
- 6-dummy-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.334105785992366 m/s (allowed None … 10.0)
- 6-actual-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22576305710688 m/s (allowed None … 10.0)
- 6-actual-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.031806579647046 m/s (allowed None … 10.0)
- 6-actual-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.334105785992426 m/s (allowed None … 10.0)
- 7-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638713 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22576305710688 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.031806579647068 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.33410578599237 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind0: guide_departure_m_s=11.829625135906184 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.22576305710688 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind2: guide_departure_m_s=11.823546447479531 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.031806579647068 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind4: guide_departure_m_s=11.821489217052493 m/s (allowed 12.0 … None);
  deployment_speed_m_s=15.334105785992527 m/s (allowed None … 10.0)

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
