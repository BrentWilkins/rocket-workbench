# Re-verification after part substitutions

The selected D12 / BT-60 airframe is **two common 18-inch BT-60 tubes joined by one BT-60 coupler**. This leaves locally replaceable spares, but it is a new physical configuration: earlier 500 mm results used an unjointed body, and the similarly named “insert joint” result concerns avionics-bay retention hardware, not an airframe splice.

## What the splice gives up

- **One uninterrupted tube:** the BMS option has no butt joint, coupler mass, alignment operation, or internal step.
- **Known mass and CG:** the coupler and its adhesive have not been measured or included in the prior ledger.
- **A demonstrated recovery volume:** the coupler must not conflict with the packed chute, wadding, bay insertion, mount, or recovery-line path.
- **A demonstrated structural and alignment result:** flight simulation cannot establish joint bond strength, roundness, straightness, or whether a seam creates an external lip.

It does **not** establish a quantified loss in apogee, stability, or drift. Those quantities need a rerun from the measured assembled configuration. Do not borrow the small performance change from the avionics insert trial.

## Build and measurement gates

1. Use two approximately 250 mm tube sections with the 3-inch BT-60 coupler, giving about 38.1 mm engagement on each side. Keep the joint away from the 145 mm avionics-bay insertion envelope, motor-mount region, and packed recovery bundle; confirm this by dry assembly before cutting or bonding.
2. Measure each cut section, the coupler, and joint adhesive: mass, axial CG from the nose-tip datum, ID/OD, roundness, and straightness. Roll the assembled tube and check collar, nose, and launch-guide fit.
3. With the delivered thin-mil chute, mount, bulkhead, and harness in place, perform repeated unpowered packing and extraction checks. Measure chute mass/CG, packed dimensions, harness/line mass, wadding, hardware, and finished fin assembly.
4. Use a representative spare-tube article to confirm the selected coupler/bond method and inspect for crush, split, or misalignment. This is a fit/assembly check, not a substitute for experienced launch-range review.

## OpenRocket rerun

Create a fresh configuration after measurement and preserve the unjointed runs as historical evidence. Enter measured mass and axial CG for every new item, including coupler and adhesive, then verify its generated ledger against complete empty, dummy, and logger assemblies. Rerun the established D12 motor/delay, loading, wind, and chute-Cd grid without silently narrowing prior uncertainty bounds.

Review guide-departure speed, minimum ascent stability, apogee, deployment warnings, descent rate, and landing displacement. Preserve failed or warning cases. A successful rerun better represents selected hardware; it does not validate the splice, fin bonds, parachute deployment, or flight safety.

Use [MEASUREMENTS.md](MEASUREMENTS.md), [BUILD.md](BUILD.md), and [OPENROCKET.md](OPENROCKET.md) alongside this gate.
