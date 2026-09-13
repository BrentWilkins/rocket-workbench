# Powered-flight acceleration and electronics load

> **Historical geometry; current metric-method reference.** Results below use the generic 18 g payload and short bay,
> not the [component-level avionics design](AVIONICS_DESIGN.md). The timestep check applies to these retained cases.

The earlier 50 mm conical candidate was re-run with all five motor/delay choices, three loadings and winds 0/2 m/s: 30
cases, repeated with half the configured timestep for 60 simulations total. These remain provisional mass/CG models, not
measured electronics or flight approval. The historical flight criteria have not changed.

## C5-3 result

| Loading                  | Peak trajectory acceleration | Peak estimated accelerometer load | Peak powered speed |
| ------------------------ | ---------------------------: | --------------------------------: | -----------------: |
| Empty bay                |                14.34–14.35 g |                     15.34–15.35 g |    33.69–33.86 m/s |
| Provisional 18 g payload |                12.55–12.56 g |                     13.55–13.56 g |    28.64–28.82 m/s |

Dummy and actual load cases currently have identical mass and CG. The unloaded case is included as a lighter-airframe
bound, not as a claim that an absent sensor records anything. The estimated load is below the proposed LSM6DS3TR-C's ±16
g measurement range in these nominal simulations, but does not include vibration or certify freedom from clipping. No
sensor limit has been added as a flight eligibility gate.

- [All motor/loading/wind comparisons](../runs/powered-study-20260913T012040Z/report.md)
- [Nominal CSV](../runs/powered-study-20260913T012040Z/nominal/results.csv)
- [Nominal raw time histories, events and peak times](../runs/powered-study-20260913T012040Z/nominal/results.json)
- [Timestep comparison JSON](../runs/powered-study-20260913T012040Z/comparison.json)

All 60 cases supplied complete powered-flight samples. Halving the configured maximum timestep changed peak estimated
load by less than 0.000002 g and peak powered speed by less than 0.004 m/s across these cases. OpenRocket uses adaptive
steps, so this is a numerical sensitivity check, not proof of continuous-time maxima or accurate motor/hardware inputs.

## Definitions and limits

Powered peaks select positive-thrust samples from liftoff up to, but excluding, first burnout, deployment, abort or
ground contact. They include flight on the guide after liftoff, but exclude coast, deployment and landing. This is a
single-stage metric. Missing events or samples produce unavailable values, not zero. Peaks and their timestamps are
stored in JSON; CSV and Markdown contain the peak values.

Trajectory acceleration is OpenRocket's total acceleration divided by standard gravity, 9.80665 m/s². Estimated
accelerometer load restores the engine's local gravity to the vertical component before taking the magnitude:

```text
estimated load [g] = sqrt(a_lateral² + (a_vertical + local_gravity)²) / 9.80665
```

This is an approximate center-of-mass specific-force magnitude, not a body-axis IMU output. It neglects the engine's
Coriolis contribution and additional rotational acceleration at a sensor displaced from the center of mass. It also
excludes local vibration, board flex, ejection shock and crash deceleration. A simple “total acceleration + 1 g” would
be wrong for general nonvertical motion. The implementation follows the acceleration/gravity semantics in
[OpenRocket 24.12's stepper](https://github.com/openrocket/openrocket/blob/release-24.12/core/src/main/java/info/openrocket/core/simulation/RK4SimulationStepper.java).

The proposed IMU's ±16 g measurement range is not its damage threshold. Its chip datasheet specifies a 10,000 g, 0.2 ms
absolute-maximum shock rating; this does not establish a sustained acceleration allowance or a rating for the assembled
XIAO, soldered stack, GPS antenna or battery. L76K assembly shock tolerance remains unverified.
[ST LSM6DS3TR-C datasheet, section 4.5](https://www.st.com/resource/en/datasheet/lsm6ds3tr-c.pdf).

## Reproduce

With the project's uv-managed Python 3.14 environment and pinned OpenRocket runtime installed:

```sh
uv run python scripts/study_powered_flight.py
uv run pytest --run-integration -q
```

The script creates a new timestamped study with source/artifact hashes, full reports, flight models, motor curves,
resolved inputs and timestep comparisons. Old simulation packages are retained unchanged. The reporting additions also
apply to future ordinary simulations and sweeps.
