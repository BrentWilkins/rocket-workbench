# D12-5 / E12-6 design screen

This OpenRocket 24.12 screen uses the **500 mm BT-60 body**, 50 mm nose, current integrated fin-collar geometry, 24 mm motor mount, and provisional 24-inch recovery model. The printed collar's **27 g raw mass** and XIAO ESP32-S3 Sense's **6 g raw mass** are weighed inputs; their installed CG, finish and remaining hardware are still estimates. The two-tube coupler and bond are allowances, not measured assembled parts. The actual Estes EST2271 plastic parachute in the [shopping list](SHOPPING.md) has **not** inherited the modeled nylon canopy's drag or packing evidence.

| Mass case | D12-5 / E12-6 launch mass | Lowest loaded stability | Fastest deployment | Calm-air apogee |
| --- | ---: | ---: | ---: | ---: |
| Raw weighed parts, nominal remaining estimates | 218.4 / 234.7 g | 1.66 / 1.49 cal | 6.67 / 7.56 m/s | 181.8 / 323.0 m |
| Upper remaining estimates, +3 g finish | 245.5 / 261.8 g | 1.99 / 1.74 cal | 9.47 / 9.86 m/s | 155.0 / 291.5 m |
| Upper remaining estimates, +5 g finish sensitivity | — | — | 9.66 / 9.96 m/s | — |

These modeled cases pass the configured **1.0-cal minimum stability** and **10 m/s maximum deployment-speed** screens over 0, 2 and 4 m/s winds. The nominal E12-6 value of 1.49 cal is just below a separate *advisory* 1.5-cal planning target, not a failure of the configured 1.0-cal test. The upper E12-6 deployment margin is small enough that the displayed hundredths of a metre per second should not be treated as physical precision. See [caliber and stability context](OPENROCKET.md#stability-margin-calibers-versus-diameter).

The [same-motor stability/altitude plot](../plots/de-geometry-same-motor.png) places the weighed current collar on the mass-calibrated fin-span curves for each body length. Longer bodies and larger fins can improve stability but generally cost altitude in the plotted set. The [3D geometry plot](../plots/de-geometry-surface.png) combines **E12-6 stability** with **D12-5 altitude**; it is a cross-motor design view, not a same-motor tradeoff or an interpolated flight test. OpenRocket models the collar with parametric fins; it does not credit the blended root's possible aerodynamic improvement.

Evidence: [nominal run](../runs/de-weighed-nominal-20260919T2100Z/comparison.json), [upper +3 g run](../runs/de-weighed-upper-20260919T2100Z/comparison.json), [upper +5 g run](../runs/de-weighed-finish5-upper-20260919T2105Z/comparison.json), and [calibrated geometry sweep](../runs/de-calibrated-geometry-20260919T2120Z/comparison.json). Earlier search files remain in `runs/` for provenance; they are not current build recommendations.

## Before relying on the screen

Weigh the finished collar, assembled coupler/bond, motor mount, chute, harness, battery and wiring; measure their axial CGs and the complete loaded rocket CG. Confirm the camera window, pressure vent, launch guides, chute extraction and recovery attachment physically. Rerun D12-5 and E12-6 with the delivered canopy and measured hardware without silently narrowing the wind or chute-drag bounds. The [re-verification checklist](REVERIFICATION.md) tracks these gates. This screen is **not flight clearance**.
