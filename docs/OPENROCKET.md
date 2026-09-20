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

- **Guide-departure speed:** speed built during usable travel along the launch guide.
- **CG, CP, and stability margin:** the mass balance and extended-Barrowman restoring estimate during ascent.
- **Altitude, velocity, acceleration, and Mach history:** powered-flight performance for the selected motor.
- **Apogee and deployment state:** recovery timing, speed, altitude, and warnings.
- **Descent rate and downrange displacement:** consequences of the entered chute diameter, drag coefficient, mass, and
  wind; these are scenarios, not landing guarantees.

The earlier screens evaluate minimum stability over the usable ascent and preserve every engine warning. The
[paired robustness study](FLIGHT_ROBUSTNESS.md) additionally isolates free powered flight, measures nose tilt, angle of
attack and angular motion, and samples bounded mass/CG, finish, launcher and weather assumptions. Its recovery
coefficient and motor curve are fixed; the older bounded-recovery screens are separate experiments. A pass count under
assumed bounds is not a measured probability of success.

## What is entered versus what is assumed

| Input or feature                      | Current treatment                                                          | Consequence                                                               |
| ------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Delivered parts, prints, and hardware | Mass and axial CG must be measured and entered                             | The ledger determines how representative the result is.                   |
| D12 motor                             | Exact bundled OpenRocket thrust/mass curve and selected delay              | The curve is not a measurement of a purchased specimen.                   |
| Three clipped-delta fins              | Native flat-fin aerodynamic model                                          | Collar fillets and small edge refinements are not resolved.               |
| Thin-mil parachute                    | Measured mass/CG required; drag coefficient remains bounded                | Packing, extraction, heat, and attachment strength are outside the model. |
| Wind and atmosphere                   | ISA baseline; robustness study adds altitude-dependent wind and turbulence | Synthetic profiles are not launch-day forecasts or resolved local gusts.  |

OpenRocket supports conventional components well enough for this screen, but it does not turn a detailed STEP solid into
a CFD surface. Do not use it to claim a root-fillet drag benefit, prove a coupler joint, or validate the custom fin
assembly.

### Guide travel and flight-phase comparisons

The robustness runner explicitly supplies **physical rod length minus the tail-to-aft-lug-bottom distance** as the
departure threshold. OpenRocket 24.12 calculates this effective length internally, but the event path used here
otherwise compares travel against the configured full rod length. In this model the native clearance approximation gives
0.7644 m on a 0.9144 m rod. It does not measure actual two-lug guidance, friction or rod flex. Earlier geometry-sweep
guide speeds used the full length and should not be used for current launch clearance.

Angle of attack is relative to airflow; nose tilt and trajectory tilt are relative to vertical and are distinct. The new
powered minimum stability is evaluated **after guide exit, before burnout, with positive thrust**; it excludes
constrained guide motion and low-speed behavior near apogee. Compare like metrics and flight phases, not that number
against the earlier whole-ascent minimum. The [robustness report](FLIGHT_ROBUSTNESS.md) includes an interactive viewer,
matched-wind comparisons and paired uncertainty distributions.

## Stability margin: calibers versus diameter

A **caliber** here is one _body-tube outside diameter used as the reference length_, not a motor class or a fin
dimension. With axial positions measured aft from the nose tip, static stability margin is
`(CP position - CG position) / reference body diameter`. Positive margin means the center of gravity (CG) is ahead of
the predicted center of pressure (CP). This BT-60 model uses a provisional **41.6 mm body OD**, so 1.0 caliber is about
41.6 mm of axial CG-to-CP separation and 1.5 calibers about 62.4 mm. The "60" in BT-60 is a tube-size designation, not
60 mm diameter. Recheck the calculation if the delivered tube OD changes.

The configured simulation gate is **at least 1.0 caliber of minimum ascent stability** across the screened loading/wind
cases. [OpenRocket's guidance](https://wiki.openrocket.info/Overrides_and_Surface_Finish) recommends at least 1.0
caliber for subsonic flight;
[NAR's safety-officer guidance](https://nar.org/content.aspx?club_id=114127&module_id=673715&page_id=22) also uses one
body diameter as its check. The **1.5-caliber line is our advisory planning cushion**, not an OpenRocket requirement,
NAR rule, or pass/fail condition. An older NAR beginner booklet has described 1.5 diameters as ideal, but that does not
make it a universal threshold. Near-threshold values should not be read to hundredths of a caliber while part mass, CG,
and aerodynamics are still estimates.

The **CG is the balance point**; the **CP is the effective location of the combined aerodynamic side force**. When the
rocket tilts relative to the airflow, a CP behind the CG gives that force leverage to turn the nose back toward the
airflow, like the feathers on a dart. A CP ahead of the CG instead tends to amplify the disturbance. More separation
gives more restoring leverage for the same aerodynamic side force; it does not directly specify how quickly oscillations
settle.

Extra margin provides a cushion against uncertain component placement and changes in CP with angle of attack. It is
**not a percentage safety rating or a wind rating**. In wind, the restoring tendency points the nose into the relative
airflow, not necessarily vertically: stronger weathercocking can reduce altitude. See
[NASA's explanation of weathercocking](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/rocket-weather-cocking/).
Comparing wind tolerance also requires guide-exit speed, angle of attack, stability throughout powered flight, and
departure from vertical under matched wind conditions; a minimum-margin/apogee plot alone does not establish an
allowable wind speed.

More margin is not automatically better: larger fins or a longer body can move the predicted CP aft, while also adding
drag and mass and potentially increasing weathercocking. The tradeoff plot shows those _design changes_ lowering
altitude as stability rises; stability itself is not an energy loss. Static margin also changes during flight as motor
propellant burns and aerodynamic conditions change, so the plotted value is the minimum over the modeled ascent, not a
single launch-pad measurement.

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

The current validation cases are **D12-5 and E12-6** in the 24 mm mount, with the printed 53.65 mm-span collar weighed
at 27 g before finish. Motor curves include loaded mass and propellant loss; mount hardware and the D-motor spacer are
separate mass entries. Installed payload, coupler/adhesive, recovery and finished mass/CG remain estimates requiring
physical checks.

The [payload sweep](PAYLOAD_SWEEP.md) excludes C11-3 at this launch mass. Earlier 18 mm motor comparisons do not
establish a fallback for this build. Use the [flight-robustness report](FLIGHT_ROBUSTNESS.md) for current guide-travel,
powered-flight and uncertain-condition comparisons.
