# Next platform: more altitude and payload margin

Decision note, 2026-09-13. **Recommendation for the next study, not a simulated new design or purchase approval.**

## Where we are

The current loaded performance cone predicts **57.62–59.50 m** on C5-3 at nominal avionics mass and 0/2 m/s wind. At the
upper avionics allowance it predicts **51.89–53.85 m**; the loaded wind-2 case fails deployment speed. Other motors and
heavier stress cases can be lower. None of the three current candidates clears the full stress grid. See
[retained results](CURRENT_DESIGN.md). Low altitude alone is not proof of a reliable flight.

The retained studies use a **30–120 m demonstration screening gate**. This was an engineering assumption, not a physical
limit, legal/site limit, or user-requested ceiling. The current leader is not reaching that upper gate. The
higher/faster objective should be evaluated in a new study with explicit performance objectives and a real site's
constraints; do not silently change the criteria and relabel old passes. Current evidence stays reproducible.

## Separate motor diameter from body diameter

| Next comparison                    | Reason to consider it                                                            | Principal cost or uncertainty                                             |
| ---------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Existing 18 mm / BT-60             | Retained model and fit parts; possible passive logger test after measured checks | Little demonstrated mass/deployment margin; no full stress pass           |
| 24 mm / BT-60                      | First candidate for more propulsion without enlarging every external part        | New mount/retention, mass/CG, recovery packing and motor/delay evaluation |
| 24 mm / larger body, such as BT-80 | Packaging access and future payload room                                         | New nose, fins, bay and recovery sizing; extra drag and structural mass   |

Estes offers a
[24 mm D/E mount kit for BT-55, BT-60 and BT-80](https://estesrockets.com/products/d-and-e-engine-mount-kit). Thus
buying a wider tube is not a prerequisite for investigating a 24 mm motor. A larger tube is primarily a packaging
choice, not an altitude improvement by itself. No current mount or printed structure is qualified for the larger motor.

**Study the 24 mm / BT-60 option first**, with the current passive logger and explicit added inert-payload allowances.
Compare a wider body only where packaging or servicing justifies it. Recompute CAD mass/CG and evaluate the complete
commercial motor/delay curves, guide departure, stability, deployment, descent and drift at nominal and upper mass. Do
not predict a new altitude from impulse ratios alone. Motor-letter and maximum-liftoff-mass labels are not enough.

## Is the extra cost large?

Manufacturer advertised USD prices checked 2026-09-13, before tax/shipping. These examples are not a full BOM:

| Item                                                                        |   Advertised package price | Interpretation                                                       |
| --------------------------------------------------------------------------- | -------------------------: | -------------------------------------------------------------------- |
| [C5-3](https://estesrockets.com/products/c5-3-engines)                      |                 $14.99 / 3 | About $5.00 per motor                                                |
| [D12-3](https://estesrockets.com/products/d12-3-engines)                    |                 $15.99 / 2 | About $8.00 per motor; listed 24 mm diameter, delay not yet selected |
| [D/E mount kit](https://estesrockets.com/products/d-and-e-engine-mount-kit) |                     $11.99 | Compatible airframe sizes listed above                               |
| [BT-80 tube](https://estesrockets.com/products/bt-80-body-tube-1)           | $5.99 / one 23.5-inch tube | Tube alone, not replacement nose/fin/bay/recovery hardware           |

The motor example adds about **$3 per flight**. That makes a 24 mm comparison worthwhile before committing to the 18 mm
build, but does not establish the total upgrade price. Launch equipment, recovery system, reprints and shipping could
dominate the difference. Keep a compatible single-stage commercial motor and passive recovery as the scope.

**E12 purchase caution:** Estes currently lists a manufacturing-issue bulletin affecting E12-0/-4/-6/-8 lots
`2K1 25336 00` and `2I3 25303 00`. Check the
[manufacturer bulletin](https://estesrockets.com/pages/e12-service-bulletin) and contact Estes about affected stock;
this note does not recommend buying E12 motors.

## Future actuator mass is not just a couple of boards

The present removable avionics allowance is **20.65 g nominal / 29.20 g upper**, with a **14.42 g printed sled**
accounted separately. The whole nominal performance rocket is **157.15 g dry**, excluding its motor.

For scale only, a [FEETECH FS90 micro servo](https://www.pololu.com/product/2818) is specified as 9 g. Two to four such
devices alone total 18–36 g; wiring, mounts, mechanisms and a suitable power system add more. Doubling the
electronics/accessory allowance is therefore plausible, but it is **not** doubling the whole rocket's mass, nor is it a
complete actuator-system budget. The existing logger battery/current allowances do not cover servos. No servo count,
load requirement, mechanism, battery, active controller or new flight performance has been specified.

Active control is a separate development scope, not an automatic next step or a remedy for a marginal passive design.
First establish passive stability, reliable commercial recovery and useful logger data. Extra capacity can initially be
represented as securely retained inert payload in a new study; that does not validate an actively controlled rocket.

## Should we fly the 18 mm version first?

Not merely because its files already exist. If parts are already available, it can still be useful for bench fit,
retention, separation and sensor tests. A passive first flight is conditional on measured mass/CG, updated simulation,
physical checks and an experienced range review; it is not cleared now. If the airframe is still unbuilt and more
payload/altitude is the direction, compare the 24 mm platform before ordering and cutting.

Follow the [NAR Model Rocket Safety Code](https://www.nar.org/ModelRocketSafetyCode), manufacturer instructions and the
actual range's constraints. Larger motors do not bypass those checks.
