# Generic avionics provision

**New component-level variant:** [real-part avionics specification and CAD](AVIONICS_DESIGN.md). The generic 18 g
placeholder below is historical; it remains available for comparisons and does not describe the new hardware package.

User decision, 2026-09-12: keep the bay generic. Several XIAO boards are owned, but no variant is selected and no
battery is owned/selected. Reserve configurable capacity for future altitude, IMU and possibly GPS logging. Exact
hardware selection is not a blocker to the provisional software review package.

The historical generic payload target was 45 × 25 × 16 mm and 18 g, including any board, battery, sensors, insulation,
wiring and connectors. This is **not** a claim that all those components fit simultaneously. Configuration validation,
actual envelope measurements and a revised mass/CG model are required when hardware is selected. The generic sled uses
tie slots rather than a particular XIAO hole pattern. Its own mounting holes are fixed v1 interfaces, not XIAO pins.

Empty and secured dummy-load flights remain supported without powered avionics. The case called `actual` in the CLI is
currently a provisional combined payload, not the user's measured electronics. Do not purchase a battery on the
assumption that this envelope or an arbitrary XIAO charging circuit makes it compatible.

## Expansion options, researched 2026-09-12

XIAO add-ons are generally called expansion boards or sensor breakouts, rather than Raspberry Pi HATs. Examples (not an
approved shopping list):

- [XIAO expansion base](https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/) provides a convenient development
  platform. Do not assume the whole base fits this slender flight bay; small wired modules can be more space-efficient.
- [Grove SPA06-003 barometer](https://wiki.seeedstudio.com/grove_barometer_sensor_spa06_003/) is a 3.3 V I2C/SPI
  pressure sensor module. Pressure data can support relative altitude logging. Published board dimensions are 40 × 20 ×
  6.5 mm, before connector/wire routing; a full stack still needs layout and mass verification.
- [Grove BMI088 IMU](https://wiki.seeedstudio.com/Grove-6-Axis_Accelerometer%26Gyroscope_BMI088/) combines accelerometer
  and gyroscope, with selectable acceleration range up to ±24 g. Range, sampling rate, vibration, mounting and clipping
  must be evaluated against the actual flight; it is not a certified rocket flight computer.
- [L76-L GNSS for XIAO](https://wiki.seeedstudio.com/gnss_for_xiao/) is a XIAO-specific satellite-positioning expansion.
  Check exact board revision, pin conflicts, antenna placement and power before choosing it. GPS reception alone does
  not provide a way to find the rocket remotely: telemetry or a postflight readout is a separate system.

Suggested later sequence: barometric altitude logging, then IMU logging, then GPS if location data justifies its extra
packaging and power. No firmware, telemetry, active guidance or deployment electronics are included in this MVP.

## Pressure sensing changes the bay requirements

Required when adding a pressure sensor: include static-pressure breathing holes in the CAD, not just the electronics
model. Size their total area against the actual free chamber volume and required pressure response; choose placement
away from nose/shoulder disturbances and verify the assembled airflow path. Keep the sensing chamber isolated from
ejection gases. Record hole count, diameter, wall thickness and location, and verify the printed holes are clear.
Dimensions remain pending the sensor/chamber layout; the current sealed CAD is not a barometer-ready design.

A forward-facing opening tends to collect ram pressure and bias the inferred altitude low. A flush side opening samples
local surface pressure, which is not inherently below ambient: its bias depends on placement, angle of attack and
surrounding geometry. Use an appropriate straight-body static-port region away from shoulders, lugs and fins; multiple
circumferential ports reduce directional effects but do not cancel all aerodynamic bias. Do not put arbitrary holes
through the cone. See [altimeter installation guidance](https://www.apogeerockets.com/Peak-of-Flight/Newsletter543).

The current protective bay is not a validated barometric sampling chamber. A future pressure sensor needs a deliberately
designed ambient static-pressure vent path, while remaining isolated from the motor ejection-gas volume. A fully sealed
bay cannot simply be assumed to report outside pressure. Vent placement, dynamic-pressure error, pressure lag and
ejection transients need separate design and testing before interpreting its data. No vent holes are silently added to
the current CAD. The first version can carry an unpowered surrogate without claiming that barometric electronics are
ready.
