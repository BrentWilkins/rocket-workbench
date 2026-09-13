# Rocket Workbench report

Run: `stress-20260913T041148Z-eb9f05aa`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `893f9b5720202cfeaca477d1d020bfeb96da3c5a188c10e03710a93f12ca3ed9`

## Cases

| Case                | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        5.45 |    0.01 |           11.61 |            12.61 |             26.25 |
| 0-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        5.45 |    6.45 |           11.61 |            12.61 |             26.08 |
| 0-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        5.45 |   12.47 |           11.60 |            12.60 |             25.67 |
| 0-dummy-C5-3-wind0  | completed / outside configured limits |    49.81 |     11.93 |           2.91 |       9.69 |        5.94 |    0.32 |            9.72 |            10.72 |             20.09 |
| 0-dummy-C5-3-wind2  | completed / outside configured limits |    47.72 |     11.92 |           2.52 |      11.39 |        5.94 |    6.71 |            9.72 |            10.71 |             19.97 |
| 0-dummy-C5-3-wind4  | completed / outside configured limits |    42.67 |     11.92 |           2.19 |      14.82 |        5.94 |   14.18 |            9.71 |            10.71 |             19.68 |
| 0-actual-C5-3-wind0 | completed / outside configured limits |    49.81 |     11.93 |           2.91 |       9.69 |        5.94 |    0.32 |            9.72 |            10.72 |             20.09 |
| 0-actual-C5-3-wind2 | completed / outside configured limits |    47.72 |     11.92 |           2.52 |      11.39 |        5.94 |    6.71 |            9.72 |            10.71 |             19.97 |
| 0-actual-C5-3-wind4 | completed / outside configured limits |    42.67 |     11.92 |           2.19 |      14.82 |        5.94 |   14.18 |            9.71 |            10.71 |             19.68 |
| 1-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        4.45 |    0.00 |           11.61 |            12.61 |             26.25 |
| 1-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        4.45 |   12.53 |           11.61 |            12.61 |             26.08 |
| 1-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        4.45 |   23.49 |           11.60 |            12.60 |             25.67 |
| 1-dummy-C5-3-wind0  | completed / outside configured limits |    49.81 |     11.93 |           2.91 |       9.69 |        4.85 |    0.27 |            9.72 |            10.72 |             20.09 |
| 1-dummy-C5-3-wind2  | completed / outside configured limits |    47.72 |     11.92 |           2.52 |      11.39 |        4.85 |    2.95 |            9.72 |            10.71 |             19.97 |
| 1-dummy-C5-3-wind4  | completed / outside configured limits |    42.67 |     11.92 |           2.19 |      14.82 |        4.85 |    7.94 |            9.71 |            10.71 |             19.68 |
| 1-actual-C5-3-wind0 | completed / outside configured limits |    49.81 |     11.93 |           2.91 |       9.69 |        4.85 |    0.27 |            9.72 |            10.72 |             20.09 |
| 1-actual-C5-3-wind2 | completed / outside configured limits |    47.72 |     11.92 |           2.52 |      11.39 |        4.85 |    2.95 |            9.72 |            10.71 |             19.97 |
| 1-actual-C5-3-wind4 | completed / outside configured limits |    42.67 |     11.92 |           2.19 |      14.82 |        4.85 |    7.94 |            9.71 |            10.71 |             19.68 |
| 2-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        5.45 |    0.01 |           11.61 |            12.61 |             26.25 |
| 2-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        5.45 |    6.45 |           11.61 |            12.61 |             26.08 |
| 2-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        5.45 |   12.47 |           11.60 |            12.60 |             25.67 |
| 2-dummy-C5-3-wind0  | completed / outside configured limits |    49.81 |     11.93 |           2.87 |       9.68 |        5.94 |    0.32 |            9.72 |            10.72 |             20.09 |
| 2-dummy-C5-3-wind2  | completed / outside configured limits |    47.72 |     11.92 |           2.48 |      11.40 |        5.94 |    6.72 |            9.72 |            10.71 |             19.97 |
| 2-dummy-C5-3-wind4  | completed / outside configured limits |    42.67 |     11.92 |           2.16 |      14.82 |        5.94 |   14.18 |            9.71 |            10.71 |             19.68 |
| 2-actual-C5-3-wind0 | completed / outside configured limits |    49.81 |     11.93 |           2.87 |       9.68 |        5.94 |    0.32 |            9.72 |            10.72 |             20.09 |
| 2-actual-C5-3-wind2 | completed / outside configured limits |    47.72 |     11.92 |           2.48 |      11.40 |        5.94 |    6.72 |            9.72 |            10.71 |             19.97 |
| 2-actual-C5-3-wind4 | completed / outside configured limits |    42.67 |     11.92 |           2.16 |      14.82 |        5.94 |   14.18 |            9.71 |            10.71 |             19.68 |
| 3-empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |       4.84 |        4.45 |    0.00 |           11.61 |            12.61 |             26.25 |
| 3-empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |       6.12 |        4.45 |   12.53 |           11.61 |            12.61 |             26.08 |
| 3-empty-C5-3-wind4  | completed / incomplete inputs         |    63.88 |     12.99 |           1.52 |       9.55 |        4.45 |   23.49 |           11.60 |            12.60 |             25.67 |
| 3-dummy-C5-3-wind0  | completed / outside configured limits |    49.81 |     11.93 |           2.87 |       9.68 |        4.85 |    0.27 |            9.72 |            10.72 |             20.09 |
| 3-dummy-C5-3-wind2  | completed / outside configured limits |    47.72 |     11.92 |           2.48 |      11.40 |        4.85 |    2.96 |            9.72 |            10.71 |             19.97 |
| 3-dummy-C5-3-wind4  | completed / outside configured limits |    42.67 |     11.92 |           2.16 |      14.82 |        4.85 |    7.94 |            9.71 |            10.71 |             19.68 |
| 3-actual-C5-3-wind0 | completed / outside configured limits |    49.81 |     11.93 |           2.87 |       9.68 |        4.85 |    0.27 |            9.72 |            10.72 |             20.09 |
| 3-actual-C5-3-wind2 | completed / outside configured limits |    47.72 |     11.92 |           2.48 |      11.40 |        4.85 |    2.96 |            9.72 |            10.71 |             19.97 |
| 3-actual-C5-3-wind4 | completed / outside configured limits |    42.67 |     11.92 |           2.16 |      14.82 |        4.85 |    7.94 |            9.71 |            10.71 |             19.68 |
| 4-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        5.74 |    0.13 |           10.46 |            11.45 |             22.52 |
| 4-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        5.74 |    1.18 |           10.45 |            11.45 |             22.37 |
| 4-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        5.74 |    2.94 |           10.44 |            11.44 |             21.99 |
| 4-dummy-C5-3-wind0  | completed / outside configured limits |    41.06 |     11.28 |           3.01 |      11.30 |        6.20 |    0.63 |            8.87 |             9.87 |             17.20 |
| 4-dummy-C5-3-wind2  | completed / outside configured limits |    38.85 |     11.27 |           2.53 |      14.06 |        6.20 |   12.53 |            8.87 |             9.87 |             17.13 |
| 4-dummy-C5-3-wind4  | completed / outside configured limits |    33.86 |     11.27 |           2.20 |      17.49 |        6.20 |   24.99 |            8.86 |             9.86 |             16.98 |
| 4-actual-C5-3-wind0 | completed / outside configured limits |    41.06 |     11.28 |           3.01 |      11.30 |        6.20 |    0.63 |            8.87 |             9.87 |             17.20 |
| 4-actual-C5-3-wind2 | completed / outside configured limits |    38.85 |     11.27 |           2.53 |      14.06 |        6.20 |   12.53 |            8.87 |             9.87 |             17.13 |
| 4-actual-C5-3-wind4 | completed / outside configured limits |    33.86 |     11.27 |           2.20 |      17.49 |        6.20 |   24.99 |            8.86 |             9.86 |             16.98 |
| 5-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        4.69 |    0.10 |           10.46 |            11.45 |             22.52 |
| 5-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        4.69 |    3.46 |           10.45 |            11.45 |             22.37 |
| 5-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        4.69 |    5.17 |           10.44 |            11.44 |             21.99 |
| 5-dummy-C5-3-wind0  | completed / outside configured limits |    41.06 |     11.28 |           3.01 |      11.30 |        5.06 |    0.54 |            8.87 |             9.87 |             17.20 |
| 5-dummy-C5-3-wind2  | completed / outside configured limits |    38.85 |     11.27 |           2.53 |      14.06 |        5.06 |    9.76 |            8.87 |             9.87 |             17.13 |
| 5-dummy-C5-3-wind4  | completed / outside configured limits |    33.86 |     11.27 |           2.20 |      17.49 |        5.06 |   20.84 |            8.86 |             9.86 |             16.98 |
| 5-actual-C5-3-wind0 | completed / outside configured limits |    41.06 |     11.28 |           3.01 |      11.30 |        5.06 |    0.54 |            8.87 |             9.87 |             17.20 |
| 5-actual-C5-3-wind2 | completed / outside configured limits |    38.85 |     11.27 |           2.53 |      14.06 |        5.06 |    9.76 |            8.87 |             9.87 |             17.13 |
| 5-actual-C5-3-wind4 | completed / outside configured limits |    33.86 |     11.27 |           2.20 |      17.49 |        5.06 |   20.84 |            8.86 |             9.86 |             16.98 |
| 6-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        5.74 |    0.13 |           10.46 |            11.45 |             22.52 |
| 6-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        5.74 |    1.18 |           10.45 |            11.45 |             22.37 |
| 6-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        5.74 |    2.94 |           10.44 |            11.44 |             21.99 |
| 6-dummy-C5-3-wind0  | completed / outside configured limits |    41.06 |     11.28 |           2.98 |      11.30 |        6.20 |    0.63 |            8.87 |             9.87 |             17.20 |
| 6-dummy-C5-3-wind2  | completed / outside configured limits |    38.85 |     11.27 |           2.49 |      14.06 |        6.20 |   12.54 |            8.87 |             9.87 |             17.13 |
| 6-dummy-C5-3-wind4  | completed / outside configured limits |    33.87 |     11.27 |           2.17 |      17.49 |        6.20 |   24.97 |            8.86 |             9.86 |             16.98 |
| 6-actual-C5-3-wind0 | completed / outside configured limits |    41.06 |     11.28 |           2.98 |      11.30 |        6.20 |    0.63 |            8.87 |             9.87 |             17.20 |
| 6-actual-C5-3-wind2 | completed / outside configured limits |    38.85 |     11.27 |           2.49 |      14.06 |        6.20 |   12.54 |            8.87 |             9.87 |             17.13 |
| 6-actual-C5-3-wind4 | completed / outside configured limits |    33.87 |     11.27 |           2.17 |      17.49 |        6.20 |   24.97 |            8.86 |             9.86 |             16.98 |
| 7-empty-C5-3-wind0  | completed / incomplete inputs         |    57.63 |     12.42 |           2.07 |       7.83 |        4.69 |    0.10 |           10.46 |            11.45 |             22.52 |
| 7-empty-C5-3-wind2  | completed / incomplete inputs         |    55.71 |     12.42 |           1.93 |       9.07 |        4.69 |    3.46 |           10.45 |            11.45 |             22.37 |
| 7-empty-C5-3-wind4  | completed / outside configured limits |    50.95 |     12.42 |           1.61 |      12.45 |        4.69 |    5.17 |           10.44 |            11.44 |             21.99 |
| 7-dummy-C5-3-wind0  | completed / outside configured limits |    41.06 |     11.28 |           2.98 |      11.30 |        5.06 |    0.54 |            8.87 |             9.87 |             17.20 |
| 7-dummy-C5-3-wind2  | completed / outside configured limits |    38.85 |     11.27 |           2.49 |      14.06 |        5.06 |    9.76 |            8.87 |             9.87 |             17.13 |
| 7-dummy-C5-3-wind4  | completed / outside configured limits |    33.87 |     11.27 |           2.17 |      17.49 |        5.06 |   20.81 |            8.86 |             9.86 |             16.98 |
| 7-actual-C5-3-wind0 | completed / outside configured limits |    41.06 |     11.28 |           2.98 |      11.30 |        5.06 |    0.54 |            8.87 |             9.87 |             17.20 |
| 7-actual-C5-3-wind2 | completed / outside configured limits |    38.85 |     11.27 |           2.49 |      14.06 |        5.06 |    9.76 |            8.87 |             9.87 |             17.13 |
| 7-actual-C5-3-wind4 | completed / outside configured limits |    33.87 |     11.27 |           2.17 |      17.49 |        5.06 |   20.81 |            8.86 |             9.86 |             16.98 |

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
- 0-dummy-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 0-dummy-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.39343397964299 m/s (allowed None … 10.0)
- 0-dummy-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.821130916031718 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 0-actual-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.39343397964301 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.821130916031734 m/s (allowed None … 10.0)
- 1-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 1-dummy-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.393433979643016 m/s (allowed None … 10.0)
- 1-dummy-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.821130916031679 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 1-actual-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.393433979643016 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.82113091603175 m/s (allowed None … 10.0)
- 2-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 2-dummy-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.39614968792705 m/s (allowed None … 10.0)
- 2-dummy-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.819910935935106 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 2-actual-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.396149687927068 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.81991093593505 m/s (allowed None … 10.0)
- 3-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 3-dummy-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.396149687927055 m/s (allowed None … 10.0)
- 3-dummy-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.819910935935088 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind0: guide_departure_m_s=11.926922368798708 m/s (allowed 12.0 … None)
- 3-actual-C5-3-wind2: guide_departure_m_s=11.921537158109787 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.396149687927037 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind4: guide_departure_m_s=11.919752133384554 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.819910935935141 m/s (allowed None … 10.0)
- 4-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173375 m/s (allowed None … 10.0)
- 4-dummy-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.300950776537427 m/s (allowed None … 10.0); landing_descent_m_s=6.203278676543679 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.061505204906274 m/s (allowed None … 10.0); landing_descent_m_s=6.203208067617343 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.492807763902682 m/s (allowed None … 10.0); landing_descent_m_s=6.203130182054386 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.300950776537427 m/s (allowed None … 10.0); landing_descent_m_s=6.203278676543679 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.061505204906279 m/s (allowed None … 10.0); landing_descent_m_s=6.203208067617343 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.492807763902672 m/s (allowed None … 10.0); landing_descent_m_s=6.203130182054386 m/s (allowed
  None … 6.0)
- 5-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173325 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.300950776537427 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.061505204906261 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.49280776390267 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.300950776537427 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.061505204906279 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.49280776390265 m/s (allowed None … 10.0)
- 6-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173343 m/s (allowed None … 10.0)
- 6-dummy-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.296769929853925 m/s (allowed None … 10.0); landing_descent_m_s=6.203278677895283 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.06172854061378 m/s (allowed None … 10.0); landing_descent_m_s=6.203208067452398 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.48769352086689 m/s (allowed None … 10.0); landing_descent_m_s=6.2031303115122265 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.296769929853925 m/s (allowed None … 10.0); landing_descent_m_s=6.203278677895283 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.061728540613784 m/s (allowed None … 10.0); landing_descent_m_s=6.203208067452398 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.487693520866824 m/s (allowed None … 10.0); landing_descent_m_s=6.2031303115122265 m/s (allowed
  None … 6.0)
- 7-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind4: deployment_speed_m_s=12.454346725173412 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.296769929853927 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.061728540613773 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.487693520866706 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind0: guide_departure_m_s=11.277234405834669 m/s (allowed 12.0 … None);
  deployment_speed_m_s=11.296769929853927 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind2: guide_departure_m_s=11.272185529814067 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.06172854061368 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind4: guide_departure_m_s=11.270688657986847 m/s (allowed 12.0 … None);
  deployment_speed_m_s=17.48769352086674 m/s (allowed None … 10.0)

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
