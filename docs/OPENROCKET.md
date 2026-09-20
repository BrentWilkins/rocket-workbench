# OpenRocket: what this project calculates

OpenRocket is the project's fast, repeatable **flight-model screen**. It answers, “given the rocket and launch
assumptions entered here, what trajectory follows?” It is not a substitute for a packed-recovery test, a fin-bond test,
an ejection test, or a flight.

## What you see in the application

OpenRocket has a design area, **Motors & Configurations**, **Flight Simulations**, and rocket views. Enter conventional
parts—nose, body tube, transition, fin set, launch lug, motor mount, and recovery device—in the design area, then use
the 2D/3D views to check placement.

In **Motors & Configurations**, select the exact motor and ejection delay. In **Flight Simulations**, set the launch
rod, location, atmosphere, and wind. Run the case, then use **Plot / Export** for its time histories and CSV data.
Component analysis is useful for inspecting estimated stability and drag contributions before a trajectory run.

This project normally drives the same OpenRocket 24.12 engine through a pinned local adapter. Each generated run
preserves its normalized `.ork` file, inputs, time histories, motor curve, warnings, and report, so it can be opened in
the GUI later.

## What it calculates for this rocket

For every loading, motor/delay, and wind case, OpenRocket combines the entered mass distribution, motor curve,
atmosphere, guide, and recovery assumptions into a six-degree-of-freedom trajectory. The useful outputs are:

- **Guide-departure speed:** speed built before leaving the 36-inch rod.
- **CG, CP, and stability margin:** the mass balance and extended-Barrowman restoring estimate during ascent.
- **Altitude, velocity, acceleration, and Mach history:** powered-flight performance for the selected motor.
- **Apogee and deployment state:** recovery timing, speed, altitude, and warnings.
- **Descent rate and downrange displacement:** consequences of the entered chute diameter, drag coefficient, mass, and
  wind; these are scenarios, not landing guarantees.

The project evaluates minimum stability over the usable ascent and preserves every engine warning. Its uncertainty runs
vary bounded mass/CG, chute drag coefficient, and wind corners; a pass count is not a probability of success.

## What is entered versus what is assumed

| Input or feature                      | Current treatment                                             | Consequence                                                                  |
| ------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Delivered parts, prints, and hardware | Mass and axial CG must be measured and entered                | The ledger determines how representative the result is.                      |
| D12 motor                             | Exact bundled OpenRocket thrust/mass curve and selected delay | The curve is not a measurement of a purchased specimen.                      |
| Three clipped-delta fins              | Native flat-fin aerodynamic model                             | Collar fillets and small edge refinements are not resolved.                  |
| Thin-mil parachute                    | Measured mass/CG required; drag coefficient remains bounded   | Packing, extraction, heat, and attachment strength are outside the model.    |
| Wind and atmosphere                   | Constant-wind ISA demonstration inputs                        | Gusts, shear, field setup, and weather mismatch remain physical uncertainty. |

OpenRocket supports conventional components well enough for this screen, but it does not turn a detailed STEP solid into
a CFD surface. Do not use it to claim a root-fillet drag benefit, prove a coupler joint, or validate the custom fin
assembly.

## Stability margin: calibers versus diameter

A **caliber** here is one *body-tube outside diameter used as the reference length*, not a motor class or a
fin dimension. With axial positions measured aft from the nose tip, static stability margin is
`(CP position - CG position) / reference body diameter`. Positive margin means the center of gravity (CG) is
ahead of the predicted center of pressure (CP). This BT-60 model uses a provisional **41.6 mm body OD**, so
1.0 caliber is about 41.6 mm of axial CG-to-CP separation and 1.5 calibers about 62.4 mm. The "60" in BT-60
is a tube-size designation, not 60 mm diameter. Recheck the calculation if the delivered tube OD changes.

The configured simulation gate is **at least 1.0 caliber of minimum ascent stability** across the screened
loading/wind cases. [OpenRocket's guidance](https://wiki.openrocket.info/Overrides_and_Surface_Finish)
recommends at least 1.0 caliber for subsonic flight; [NAR's safety-officer guidance](https://nar.org/content.aspx?club_id=114127&module_id=673715&page_id=22)
also uses one body diameter as its check. The **1.5-caliber line is our advisory planning cushion**, not an
OpenRocket requirement, NAR rule, or pass/fail condition. An older NAR beginner booklet has described 1.5
diameters as ideal, but that does not make it a universal threshold. Near-threshold values should not be read
to hundredths of a caliber while part mass, CG, and aerodynamics are still estimates.

More margin is not automatically better: larger fins or a longer body can move the predicted CP aft, while
also adding drag and mass and potentially increasing weathercocking. The tradeoff plot shows those *design
changes* lowering altitude as stability rises; stability itself is not an energy loss. Static margin also
changes during flight as motor propellant burns and aerodynamic conditions change, so the plotted value is
the minimum over the modeled ascent, not a single launch-pad measurement.

## How to interpret a green result

A completed run means the numerical calculation completed with its supplied inputs. The project's stricter status also
checks configured engineering criteria, but neither status grants flight clearance. Reconcile the mass ledger, inspect
warnings, verify recovery packing/separation, inspect airframe and fin roots, and use actual launch-site constraints and
experienced range review.

See [modeling integration decisions](MODELING.md) for the adapter, coordinates, and limitations, and
[re-verification after part substitutions](REVERIFICATION.md) for the selected spliced-airframe workflow.

Sources: [OpenRocket features](https://openrocket.info/features.html),
[Getting Started](https://wiki.openrocket.info/Getting_Started),
[Advanced Flight Simulation](https://wiki.openrocket.info/Advanced_Flight_Simulation), and
[simulation limitations](https://wiki.openrocket.info/Basic_Flight_Simulation).

## Current motor scope

> **2026-09-19 correction:** See the [D12-5/E12-6 geometry and current-collar screen](DE_GEOMETRY_SWEEP.md),
> including the [3D tradeoff plot](../plots/de-geometry-surface.png). The current fin collar has about
> 53.65 mm fin span; the 55 mm selection described below was an earlier parametric screen, not a decision to
> replace the polished collar. The current hardware screen uses its STEP-derived mass and CG. The motor curves
> include loaded mass and propellant mass loss during burn; mount and D-motor spacer are separate mass entries.
> The older C11/18 mm comparisons do not establish a viable fallback at the current launch mass.

The current airframe is designed around 24 mm C11/D12/E12 motors. D12-5 and
E12-6 are the primary validation cases; A8/B4/C5/C6 are low-power fallback
comparisons only. The latest motor-envelope run is preserved in
`runs/motor24-avionics-20260919T2000Z/`, and the fin-span stability screen is
in `runs/stability-fin-span-20260919T/`.

The selected 55 mm fin-span screen improves the loaded worst-wind stability
margin over the earlier 45 mm option, but the result remains provisional until
the installed payload, coupler/adhesive, recovery hardware, and finished fin
assembly have measured mass and CG.
