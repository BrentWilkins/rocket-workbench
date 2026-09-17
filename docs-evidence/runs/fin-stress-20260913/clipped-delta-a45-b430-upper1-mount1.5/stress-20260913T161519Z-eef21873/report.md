# Rocket Workbench report

Run: `stress-20260913T161519Z-eef21873`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `517639cb48cfade73fce6d94a53c13f586ee11075efe66ce0faa4e77428d805d`

## Cases

| Case                 | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| -------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-D12-5-wind0  | completed / incomplete inputs         |   213.22 |     13.27 |           1.59 |       0.91 |        5.69 |    0.10 |           15.13 |            16.13 |             67.80 |
| 0-empty-D12-5-wind2  | completed / outside configured limits |   211.54 |     13.27 |           0.93 |       2.56 |        5.69 |   51.08 |           15.13 |            16.13 |             67.66 |
| 0-empty-D12-5-wind4  | completed / outside configured limits |   207.07 |     13.26 |           0.81 |       4.70 |        5.69 |  103.32 |           15.11 |            16.11 |             67.30 |
| 0-dummy-D12-5-wind0  | completed / outside configured limits |   181.21 |     12.85 |           1.79 |       2.11 |        6.16 |    0.08 |           12.97 |            13.97 |             58.41 |
| 0-dummy-D12-5-wind2  | completed / outside configured limits |   179.21 |     12.85 |           1.71 |       3.82 |        6.16 |   31.50 |           12.97 |            13.97 |             58.26 |
| 0-dummy-D12-5-wind4  | completed / outside configured limits |   173.69 |     12.85 |           1.50 |       7.05 |        6.16 |   62.65 |           12.96 |            13.96 |             57.85 |
| 0-actual-D12-5-wind0 | completed / outside configured limits |   181.21 |     12.85 |           1.79 |       2.11 |        6.16 |    0.08 |           12.97 |            13.97 |             58.41 |
| 0-actual-D12-5-wind2 | completed / outside configured limits |   179.21 |     12.85 |           1.71 |       3.82 |        6.16 |   31.50 |           12.97 |            13.97 |             58.26 |
| 0-actual-D12-5-wind4 | completed / outside configured limits |   173.69 |     12.85 |           1.50 |       7.05 |        6.16 |   62.65 |           12.96 |            13.96 |             57.85 |
| 1-empty-D12-5-wind0  | completed / incomplete inputs         |   213.22 |     13.27 |           1.59 |       0.91 |        4.65 |    0.10 |           15.13 |            16.13 |             67.80 |
| 1-empty-D12-5-wind2  | completed / outside configured limits |   211.54 |     13.27 |           0.93 |       2.56 |        4.65 |   68.29 |           15.13 |            16.13 |             67.66 |
| 1-empty-D12-5-wind4  | completed / outside configured limits |   207.07 |     13.26 |           0.81 |       4.70 |        4.65 |  136.73 |           15.11 |            16.11 |             67.30 |
| 1-dummy-D12-5-wind0  | completed / incomplete inputs         |   181.21 |     12.85 |           1.79 |       2.11 |        5.03 |    0.08 |           12.97 |            13.97 |             58.41 |
| 1-dummy-D12-5-wind2  | completed / incomplete inputs         |   179.21 |     12.85 |           1.71 |       3.82 |        5.03 |   45.18 |           12.97 |            13.97 |             58.26 |
| 1-dummy-D12-5-wind4  | completed / incomplete inputs         |   173.69 |     12.85 |           1.50 |       7.05 |        5.03 |   88.88 |           12.96 |            13.96 |             57.85 |
| 1-actual-D12-5-wind0 | completed / incomplete inputs         |   181.21 |     12.85 |           1.79 |       2.11 |        5.03 |    0.08 |           12.97 |            13.97 |             58.41 |
| 1-actual-D12-5-wind2 | completed / incomplete inputs         |   179.21 |     12.85 |           1.71 |       3.82 |        5.03 |   45.18 |           12.97 |            13.97 |             58.26 |
| 1-actual-D12-5-wind4 | completed / incomplete inputs         |   173.69 |     12.85 |           1.50 |       7.05 |        5.03 |   88.88 |           12.96 |            13.96 |             57.85 |
| 2-empty-D12-5-wind0  | completed / incomplete inputs         |   213.22 |     13.27 |           1.59 |       0.91 |        5.69 |    0.10 |           15.13 |            16.13 |             67.80 |
| 2-empty-D12-5-wind2  | completed / outside configured limits |   211.54 |     13.27 |           0.93 |       2.56 |        5.69 |   51.08 |           15.13 |            16.13 |             67.66 |
| 2-empty-D12-5-wind4  | completed / outside configured limits |   207.07 |     13.26 |           0.81 |       4.70 |        5.69 |  103.32 |           15.11 |            16.11 |             67.30 |
| 2-dummy-D12-5-wind0  | completed / outside configured limits |   181.21 |     12.85 |           1.76 |       2.11 |        6.16 |    0.08 |           12.97 |            13.97 |             58.41 |
| 2-dummy-D12-5-wind2  | completed / outside configured limits |   179.21 |     12.85 |           1.67 |       3.83 |        6.16 |   31.48 |           12.97 |            13.97 |             58.25 |
| 2-dummy-D12-5-wind4  | completed / outside configured limits |   173.69 |     12.85 |           1.47 |       7.05 |        6.16 |   62.67 |           12.96 |            13.96 |             57.85 |
| 2-actual-D12-5-wind0 | completed / outside configured limits |   181.21 |     12.85 |           1.76 |       2.11 |        6.16 |    0.08 |           12.97 |            13.97 |             58.41 |
| 2-actual-D12-5-wind2 | completed / outside configured limits |   179.21 |     12.85 |           1.67 |       3.83 |        6.16 |   31.48 |           12.97 |            13.97 |             58.25 |
| 2-actual-D12-5-wind4 | completed / outside configured limits |   173.69 |     12.85 |           1.47 |       7.05 |        6.16 |   62.67 |           12.96 |            13.96 |             57.85 |
| 3-empty-D12-5-wind0  | completed / incomplete inputs         |   213.22 |     13.27 |           1.59 |       0.91 |        4.65 |    0.10 |           15.13 |            16.13 |             67.80 |
| 3-empty-D12-5-wind2  | completed / outside configured limits |   211.54 |     13.27 |           0.93 |       2.56 |        4.65 |   68.29 |           15.13 |            16.13 |             67.66 |
| 3-empty-D12-5-wind4  | completed / outside configured limits |   207.07 |     13.26 |           0.81 |       4.70 |        4.65 |  136.73 |           15.11 |            16.11 |             67.30 |
| 3-dummy-D12-5-wind0  | completed / incomplete inputs         |   181.21 |     12.85 |           1.76 |       2.11 |        5.03 |    0.08 |           12.97 |            13.97 |             58.41 |
| 3-dummy-D12-5-wind2  | completed / incomplete inputs         |   179.21 |     12.85 |           1.67 |       3.83 |        5.03 |   45.16 |           12.97 |            13.97 |             58.25 |
| 3-dummy-D12-5-wind4  | completed / incomplete inputs         |   173.69 |     12.85 |           1.47 |       7.05 |        5.03 |   88.89 |           12.96 |            13.96 |             57.85 |
| 3-actual-D12-5-wind0 | completed / incomplete inputs         |   181.21 |     12.85 |           1.76 |       2.11 |        5.03 |    0.08 |           12.97 |            13.97 |             58.41 |
| 3-actual-D12-5-wind2 | completed / incomplete inputs         |   179.21 |     12.85 |           1.67 |       3.83 |        5.03 |   45.16 |           12.97 |            13.97 |             58.25 |
| 3-actual-D12-5-wind4 | completed / incomplete inputs         |   173.69 |     12.85 |           1.47 |       7.05 |        5.03 |   88.89 |           12.96 |            13.96 |             57.85 |
| 4-empty-D12-5-wind0  | completed / incomplete inputs         |   195.87 |     13.09 |           1.46 |       0.60 |        5.95 |    0.09 |           13.90 |            14.90 |             62.55 |
| 4-empty-D12-5-wind2  | completed / outside configured limits |   194.08 |     13.08 |           0.96 |       2.81 |        5.95 |   40.77 |           13.90 |            14.89 |             62.40 |
| 4-empty-D12-5-wind4  | completed / outside configured limits |   189.26 |     13.08 |           0.94 |       5.55 |        5.95 |   82.32 |           13.89 |            14.88 |             62.01 |
| 4-dummy-D12-5-wind0  | completed / outside configured limits |   165.16 |     12.53 |           1.55 |       3.99 |        6.40 |    0.07 |           12.04 |            13.04 |             54.10 |
| 4-dummy-D12-5-wind2  | completed / outside configured limits |   163.12 |     12.53 |           1.79 |       5.19 |        6.40 |   23.50 |           12.03 |            13.03 |             53.95 |
| 4-dummy-D12-5-wind4  | completed / outside configured limits |   157.47 |     12.53 |           1.56 |       8.48 |        6.40 |   46.37 |           12.03 |            13.03 |             53.54 |
| 4-actual-D12-5-wind0 | completed / outside configured limits |   165.16 |     12.53 |           1.55 |       3.99 |        6.40 |    0.07 |           12.04 |            13.04 |             54.10 |
| 4-actual-D12-5-wind2 | completed / outside configured limits |   163.12 |     12.53 |           1.79 |       5.19 |        6.40 |   23.50 |           12.03 |            13.03 |             53.95 |
| 4-actual-D12-5-wind4 | completed / outside configured limits |   157.47 |     12.53 |           1.56 |       8.48 |        6.40 |   46.37 |           12.03 |            13.03 |             53.54 |
| 5-empty-D12-5-wind0  | completed / incomplete inputs         |   195.87 |     13.09 |           1.46 |       0.60 |        4.86 |    0.09 |           13.90 |            14.90 |             62.55 |
| 5-empty-D12-5-wind2  | completed / outside configured limits |   194.08 |     13.08 |           0.96 |       2.81 |        4.86 |   55.99 |           13.90 |            14.89 |             62.40 |
| 5-empty-D12-5-wind4  | completed / outside configured limits |   189.26 |     13.08 |           0.94 |       5.55 |        4.86 |  111.74 |           13.89 |            14.88 |             62.01 |
| 5-dummy-D12-5-wind0  | completed / incomplete inputs         |   165.16 |     12.53 |           1.55 |       3.99 |        5.22 |    0.07 |           12.04 |            13.04 |             54.10 |
| 5-dummy-D12-5-wind2  | completed / incomplete inputs         |   163.12 |     12.53 |           1.79 |       5.19 |        5.22 |   35.56 |           12.03 |            13.03 |             53.95 |
| 5-dummy-D12-5-wind4  | completed / incomplete inputs         |   157.47 |     12.53 |           1.56 |       8.48 |        5.22 |   69.35 |           12.03 |            13.03 |             53.54 |
| 5-actual-D12-5-wind0 | completed / incomplete inputs         |   165.16 |     12.53 |           1.55 |       3.99 |        5.22 |    0.07 |           12.04 |            13.04 |             54.10 |
| 5-actual-D12-5-wind2 | completed / incomplete inputs         |   163.12 |     12.53 |           1.79 |       5.19 |        5.22 |   35.56 |           12.03 |            13.03 |             53.95 |
| 5-actual-D12-5-wind4 | completed / incomplete inputs         |   157.47 |     12.53 |           1.56 |       8.48 |        5.22 |   69.35 |           12.03 |            13.03 |             53.54 |
| 6-empty-D12-5-wind0  | completed / incomplete inputs         |   195.87 |     13.09 |           1.46 |       0.60 |        5.95 |    0.09 |           13.90 |            14.90 |             62.55 |
| 6-empty-D12-5-wind2  | completed / outside configured limits |   194.08 |     13.08 |           0.96 |       2.81 |        5.95 |   40.77 |           13.90 |            14.89 |             62.40 |
| 6-empty-D12-5-wind4  | completed / outside configured limits |   189.26 |     13.08 |           0.94 |       5.55 |        5.95 |   82.32 |           13.89 |            14.88 |             62.01 |
| 6-dummy-D12-5-wind0  | completed / outside configured limits |   165.16 |     12.53 |           1.52 |       3.99 |        6.40 |    0.06 |           12.04 |            13.04 |             54.10 |
| 6-dummy-D12-5-wind2  | completed / outside configured limits |   163.12 |     12.53 |           1.76 |       5.19 |        6.40 |   23.49 |           12.03 |            13.03 |             53.95 |
| 6-dummy-D12-5-wind4  | completed / outside configured limits |   157.47 |     12.53 |           1.53 |       8.48 |        6.40 |   46.38 |           12.03 |            13.03 |             53.54 |
| 6-actual-D12-5-wind0 | completed / outside configured limits |   165.16 |     12.53 |           1.52 |       3.99 |        6.40 |    0.06 |           12.04 |            13.04 |             54.10 |
| 6-actual-D12-5-wind2 | completed / outside configured limits |   163.12 |     12.53 |           1.76 |       5.19 |        6.40 |   23.49 |           12.03 |            13.03 |             53.95 |
| 6-actual-D12-5-wind4 | completed / outside configured limits |   157.47 |     12.53 |           1.53 |       8.48 |        6.40 |   46.38 |           12.03 |            13.03 |             53.54 |
| 7-empty-D12-5-wind0  | completed / incomplete inputs         |   195.87 |     13.09 |           1.46 |       0.60 |        4.86 |    0.09 |           13.90 |            14.90 |             62.55 |
| 7-empty-D12-5-wind2  | completed / outside configured limits |   194.08 |     13.08 |           0.96 |       2.81 |        4.86 |   55.99 |           13.90 |            14.89 |             62.40 |
| 7-empty-D12-5-wind4  | completed / outside configured limits |   189.26 |     13.08 |           0.94 |       5.55 |        4.86 |  111.74 |           13.89 |            14.88 |             62.01 |
| 7-dummy-D12-5-wind0  | completed / incomplete inputs         |   165.16 |     12.53 |           1.52 |       3.99 |        5.22 |    0.07 |           12.04 |            13.04 |             54.10 |
| 7-dummy-D12-5-wind2  | completed / incomplete inputs         |   163.12 |     12.53 |           1.76 |       5.19 |        5.22 |   35.55 |           12.03 |            13.03 |             53.95 |
| 7-dummy-D12-5-wind4  | completed / incomplete inputs         |   157.47 |     12.53 |           1.53 |       8.48 |        5.22 |   69.36 |           12.03 |            13.03 |             53.54 |
| 7-actual-D12-5-wind0 | completed / incomplete inputs         |   165.16 |     12.53 |           1.52 |       3.99 |        5.22 |    0.07 |           12.04 |            13.04 |             54.10 |
| 7-actual-D12-5-wind2 | completed / incomplete inputs         |   163.12 |     12.53 |           1.76 |       5.19 |        5.22 |   35.55 |           12.03 |            13.03 |             53.95 |
| 7-actual-D12-5-wind4 | completed / incomplete inputs         |   157.47 |     12.53 |           1.53 |       8.48 |        5.22 |   69.36 |           12.03 |            13.03 |             53.54 |

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
- 0-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9330982333230047 cal (allowed 1.0 … None)
- 0-empty-D12-5-wind4: minimum_ascent_stability_cal=0.8091174596532038 cal (allowed 1.0 … None)
- 0-dummy-D12-5-wind0: landing_descent_m_s=6.160771173012311 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind2: landing_descent_m_s=6.16070091165991 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind4: landing_descent_m_s=6.160630547046453 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind0: landing_descent_m_s=6.160771173012311 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind2: landing_descent_m_s=6.16070091165991 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind4: landing_descent_m_s=6.160630547046452 m/s (allowed None … 6.0)
- 1-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9330982333232395 cal (allowed 1.0 … None)
- 1-empty-D12-5-wind4: minimum_ascent_stability_cal=0.8091174596532025 cal (allowed 1.0 … None)
- 1-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9330982333233275 cal (allowed 1.0 … None)
- 2-empty-D12-5-wind4: minimum_ascent_stability_cal=0.8091174596532038 cal (allowed 1.0 … None)
- 2-dummy-D12-5-wind0: landing_descent_m_s=6.160771173012369 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind2: landing_descent_m_s=6.160700911639895 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind4: landing_descent_m_s=6.160630546498895 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind0: landing_descent_m_s=6.160771173012369 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind2: landing_descent_m_s=6.160700911639895 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind4: landing_descent_m_s=6.160630546498895 m/s (allowed None … 6.0)
- 3-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9330982333229766 cal (allowed 1.0 … None)
- 3-empty-D12-5-wind4: minimum_ascent_stability_cal=0.8091174596532025 cal (allowed 1.0 … None)
- 3-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9614926060968084 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind4: minimum_ascent_stability_cal=0.936244886878232 cal (allowed 1.0 … None)
- 4-dummy-D12-5-wind0: landing_descent_m_s=6.397069900835324 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind2: landing_descent_m_s=6.396996987845405 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind4: landing_descent_m_s=6.396924011083662 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind0: landing_descent_m_s=6.397069900835324 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind2: landing_descent_m_s=6.396996987845405 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind4: landing_descent_m_s=6.396924011083662 m/s (allowed None … 6.0)
- 5-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9614926060966457 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind4: minimum_ascent_stability_cal=0.936244886878232 cal (allowed 1.0 … None)
- 5-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9614926060969432 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind4: minimum_ascent_stability_cal=0.936244886878232 cal (allowed 1.0 … None)
- 6-dummy-D12-5-wind0: landing_descent_m_s=6.397069900835422 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind2: landing_descent_m_s=6.3969969877781185 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind4: landing_descent_m_s=6.39692401082515 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind0: landing_descent_m_s=6.397069900835422 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind2: landing_descent_m_s=6.396996987778117 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind4: landing_descent_m_s=6.396924010825151 m/s (allowed None … 6.0)
- 7-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-D12-5-wind2: minimum_ascent_stability_cal=0.9614926060967284 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind4: minimum_ascent_stability_cal=0.9362448868782334 cal (allowed 1.0 … None)
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
