# Flight-logger firmware high-level design

This is a **design proposal**, not implemented or bench-tested code. It covers the owned Seeed XIAO ESP32-S3 Sense with
the Adafruit ICM-20649 IMU and LPS28 barometer specified in the [avionics design](AVIONICS_DESIGN.md). Every rate, size
and margin below is an arithmetic estimate from published datasheet limits; none is measured on the delivered hardware.

## Are the parts compatible?

Yes, on every interface that matters, and the checks are cheap to restate:

| Check       | ICM-20649 (4464)          | LPS28DFW (6067)            | LIS3MDL (4479), ground use | Result                                  |
| ----------- | ------------------------- | -------------------------- | -------------------------- | --------------------------------------- |
| Bus         | I2C (or SPI)              | I2C / I3C                  | I2C (or SPI)               | All on one I2C bus                      |
| Address     | 0x68 (0x69 via AD0)       | 0x5C (0x5D via SA0)        | 0x1C (0x1E via jumper)     | No collision; leave all jumpers alone   |
| Logic level | 3–5 V tolerant, regulated | 3–5 V tolerant             | 3–5 V tolerant             | All run from the XIAO 3V3 rail          |
| Pull-ups    | 10 kΩ on board            | 10 kΩ on board             | 10 kΩ on board             | 5 kΩ effective, 3.3 kΩ with the mag     |
| Max I2C     | 400 kHz                   | 400 kHz (I3C faster)       | 400 kHz                    | Bus runs at 400 kHz Fast mode           |
| Current     | ~3 mA at full rate        | ~4 µA at 1 Hz, more at ODR | ~270 µA                    | Small against the 80 mA system estimate |

The ICM-20649 is the part actually ordered; it replaces the LIS331HH named in earlier revisions of this document. It is
end-of-life at some distributors, carries a gyro the LIS331 lacked, and reads 16-bit rather than 12-bit.

The XIAO ESP32-S3 has no STEMMA QT connector, so exactly one wired transition is needed: cut the Dupont end off a single
[4209 QT-to-header cable](https://www.adafruit.com/product/4209) and solder the tails to the XIAO. Red is 3V3, black
GND, blue SDA, yellow SCL. From there the sensors chain on their second QT jacks with
[4210 QT-to-QT cables](https://www.adafruit.com/product/4210): XIAO to ICM-20649 to LPS28, leaving a free jack for the
magnetometer during ground use.

This keeps **four** wires on the XIAO pads rather than twelve, leaves a keyed serviceable connector at every sensor, and
makes the single vibration-critical joint a solder joint. The cost is chain dependency: unplugging a mid-chain board
disconnects everything behind it, so bench-test with the chain in its flight order.

## Are the rates achievable?

**Bus loading is not the constraint.** A 12-byte burst read of the ICM-20649 (accel and gyro together) costs roughly 144
bit-times including address, register pointer, restart and ACKs; a 5-byte LPS28 read costs roughly 80. At 375 Hz and 50
Hz respectively:

```text
ICM-20649:  375 Hz x 144 bits = 54.0 kbit/s
LPS28:       50 Hz x  80 bits =  4.0 kbit/s
Total                         = 58.0 kbit/s
```

That is **15% of a 400 kHz Fast-mode bus**. Adding the magnetometer at 100 Hz would bring it to about 17%. There is
ample headroom; the bus was never going to be the limit.

**Two sensor-side limits do bite, and one of them invalidates the previously documented rate:**

1. **Neither 200 Hz nor 400 Hz is selectable.** The ICM-20649 derives both ODRs from a 1125 Hz internal rate divided by
   an 8-bit divider: `ODR = 1125 / (1 + SMPLRT_DIV)`. That yields 1125, 562.5, **375**, 281.25, 225 Hz and so on. The
   old "200 samples/s" figure was inherited from the retired nRF52840 onboard IMU, and the "400 Hz" figure came from the
   LIS331HH that this part replaces. **Use 375 Hz** (divider 2) and decimate in post if you want less. Confirm the
   divider base against the datasheet register map before writing the driver.
2. **Anti-aliasing must be set deliberately.** At 375 Hz ODR the Nyquist limit is 187.5 Hz, and motor/airframe vibration
   has real content above that. The part offers selectable digital low-pass cutoffs on both accel and gyro; pick a
   cutoff below 187 Hz so out-of-band vibration folds into the record as bias rather than as convincing-looking signal.

The LPS28 supports 1–200 Hz, so the specified 50 Hz is comfortable and could go higher if pressure lag testing asks for
it.

## Resolution, and why the range trick is no longer needed

The ICM-20649 is **16-bit on both accel and gyro**, with no left-justification to undo. Accelerometer sensitivity is
8192 LSB/g at ±4 g, 4096 at ±8 g, 2048 at ±16 g and **1024 LSB/g at ±30 g** — about **0.98 mg/LSB at the flight range**.

That single number removes a whole firmware behaviour. The LIS331HH resolved only 12 mg/LSB at ±24 g, roughly 0.7° of
rail tilt, which is why earlier revisions of this document specified switching to a narrow range on the pad and back on
launch detect. At 0.98 mg/LSB the ±30 g range alone resolves tilt to about **0.06°**, twelve times better than the part
it replaces and better than the LIS331's own best-case narrow range. **Select ±30 g once at init and leave it there.**
Quantization is no longer the limit; sensor noise over a 187 Hz bandwidth is, so average on the pad rather than
switching ranges. Measure that noise floor on the bench before quoting a tilt figure.

The gyro is new capability the LIS331 never had. At ±4000 dps it reads 8.2 LSB/dps, about 0.12 dps resolution, and ±4000
dps is far beyond any roll rate this airframe will see — a fast finned spin is a few hundred dps. Its value is
post-flight attitude reconstruction over a 20 s flight; integrated heading drift is not a concern at that duration. Log
raw gyro counts alongside accel rather than fusing on board.

## Logging architecture

The ESP32-S3's **8 MB PSRAM changes the design** relative to the retired nRF52840 plan, which had to ration internal
flash. Sensor records are small:

```
accel record:  4 B timestamp + 6 B xyz            = 10 B @ 400 Hz = 4.0 kB/s
baro record:   4 B timestamp + 4 B press + 2 B T  = 10 B @  50 Hz = 0.5 kB/s
Total                                                             = 4.5 kB/s
```

A 60-second flight is **270 kB**; five minutes is 1.35 MB. The entire flight fits in PSRAM with room left for camera
framebuffers. So:

- **Never write sensor data to SD during boost.** Buffer to PSRAM, flush to SD after landing is detected, and flush
  again on a timer as a power-loss hedge.
- The prelaunch ring buffer still exists, but to bound PSRAM use and keep SD writes off the boost timeline — not because
  storage is scarce.
- **SD contention is the real risk.** The camera writing JPEG frames to the same microSD can block for tens of
  milliseconds. Decoupling sensors into PSRAM removes that coupling from the flight-critical path entirely.

Verify actual free PSRAM after the camera allocates its framebuffers before trusting these numbers.

## Timestamps and video correlation

Use `esp_timer_get_time()` (64-bit µs, monotonic) as the single time base for every record. Log a record per camera
frame containing the frame index and the same timestamp, so video and sensor traces can be aligned in post without
assuming a constant frame interval. Frame intervals under SD load will not be constant.

## Task structure

Two cores, with the boost-critical path isolated from I/O:

| Task         | Core | Priority | Period           | Job                                      |
| ------------ | ---: | -------: | ---------------- | ---------------------------------------- |
| `sensor`     |    1 |     high | 2.67 ms (375 Hz) | Burst-read both sensors, append to PSRAM |
| `flight_fsm` |    1 |      med | 10 ms            | State machine, event marks               |
| `camera`     |    0 |      med | frame-driven     | Capture, write JPEG to SD                |
| `telemetry`  |    0 |      low | 1 Hz             | BLE/WiFi status while on pad only        |
| `flush`      |    0 |      low | on event         | PSRAM to SD after landing / on timer     |

Drive the `sensor` task from the ICM-20649's INT1 data-ready output rather than a software timer if a GPIO is free; it
removes sampling jitter from the record. The board also breaks out INT2 and a 512-byte FIFO, either of which can absorb
a late task wake-up.

## Flight state machine

```
IDLE -> ARMED -> BOOST -> COAST -> APOGEE -> DESCENT -> LANDED
```

- **IDLE → ARMED:** commanded over BLE/WiFi. Radios off from ARMED onward.
- **ARMED → BOOST:** accel magnitude above ~3 g sustained ~100 ms. Retain the prelaunch ring buffer so the record
  includes the pre-ignition seconds.
- **BOOST → COAST:** accel magnitude drops below ~1.5 g. No range change; ±30 g resolves coast adequately.
- **COAST → APOGEE:** pressure minimum, confirmed over several samples, cross-checked against integrated accel.
- **DESCENT → LANDED:** pressure and accel both quiet for several seconds. Triggers the SD flush.

Flag saturation, resets, battery state and dropped samples in the record rather than interpolating. The state machine is
for **logging and post-flight segmentation only** — it commands nothing. Ejection remains the motor's job.

## Radio policy

The ESP32-S3 does WiFi and BLE, which makes pad-side status and configuration easy. **Keep both radios off from ARMED
through LANDED.** They add current draw and interrupt load during the only phase where the sampling deadline matters,
and they buy nothing in flight. Re-enable after the LANDED flush if a "find me" beacon is wanted — though at these
altitudes a visual track is more reliable.

## Open items before implementation

- Measure free PSRAM with the camera initialized at the chosen resolution.
- Bench-measure real I2C transaction time; the estimates above ignore clock stretching.
- Confirm a free GPIO for the ICM-20649 INT1 data-ready line against the Sense expansion board's pin usage.
- Confirm the 1125 Hz ODR base and divider formula against the ICM-20649 register map; 375 Hz depends on it.
- Measure the ICM-20649 accelerometer noise floor at the chosen bandwidth before quoting any tilt resolution.
- Characterize pressure lag and leakage against the static-port design before trusting the altitude trace.
- Measure actual current draw; the 80 mA average is an allowance, not a measurement.
