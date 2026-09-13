# Modeling and integration decisions

Status: software demonstration; no measured assembly, ejection test, or flight.

## Runtime decision (2026-09-12)

Use OpenRocket 24.12 with the OpenRocket-owned orhelper fork at `fb132c49e661bb00c5586cce6a4ac0c655425197`. The fork,
not the similarly named PyPI release, is installed from its exact archive URL in `uv.lock`. No bridge patch or
OpenRocket fork was required. The adapter checks the installed archive identity and JAR checksum before starting the
engine.

Tested on macOS ARM with Python 3.14.6, Oracle JDK 21.0.3+7-LTS-152 and CadQuery 2.8.0. Python package versions are
resolved by uv, not handwritten; `uv.lock` is the reproducible dependency pin. Other operating systems are not claimed
tested. Java 21 is selected explicitly because this machine's default Java is 8. Java startup uses macOS preferences
outside the project sandbox; grant that access when requested. No network is required for ordinary runs.

The maintained wrapper loads/saves documents and exposes the real engine and time series. Its convenience simulation
method chooses a fresh random seed; the production adapter instead invokes the public engine simulation method with an
empty listener array after setting the configured seed. The integration proof separately exercises the upstream
convenience method and listener callbacks, saves/reloads a changed body, and checks A–B–A repeatability.

`scripts/ReferenceCheck.java` is an independent acceptance check, not a second production adapter: it loads the
unchanged reference through the same pinned engine without Python/orhelper. It compares altitude/time arrays (1e-9
absolute) and apogee, guide, deployment and total landing speed (1e-6 absolute). This checks the bridge/extraction path,
not the physical correctness of OpenRocket. An interactive GUI cross-check remains explicitly pending.

Sources: [OpenRocket release](https://github.com/openrocket/openrocket/releases/tag/release-24.12),
[maintained bridge](https://github.com/openrocket/orhelper/tree/fb132c49e661bb00c5586cce6a4ac0c655425197),
[engine source](https://github.com/openrocket/openrocket/tree/release-24.12).

## Coordinates, mass and geometry

Canonical dimensions are mm/g with explicit provenance. Nose tip is axial zero, positive aft. CAD uses +Z for that axis;
OpenRocket uses +x, metres and kilograms. The assembly STEP preserves assembly coordinates; STLs are rotated/translated
for printing. STL coordinates therefore must not be used as assembled CGs.

The full purchased tube mass appears once even where the collar covers it. Nose shell, internal sleeve, bulkhead and
sled are lumped into the nose mass/CG override; the fin collar includes all three fins, whose separate aerodynamic
component has explicit zero mass because its mass is already included. Each launch-lug sleeve has its own CAD-derived
override; paper lugs/adhesive remain in the purchased ledger. Motor mass comes from the selected thrust curve and is not
part of dry mass. Every generated loading is checked against an independent mass/CG sum before simulation, tolerance
0.05 g / 0.05 mm.

Native components model the conical nose, tube, tapered collar, three flat fins and cylindrical lug sleeves. V2 lug
saddles add a curved bonding pad to the CAD: their mass/CG is included, but their noncylindrical drag is not resolved by
the native cylindrical lug component. See [archived saddle revision](LUG_SADDLES.md). `cad/interfaces.json` records the
shared guide dimensions. Paper lugs sit inside printed sleeves at 60 degrees between fins; the sleeve raises the rod
clear of the collar. OpenRocket sees the combined outer sleeve and inner lug bore; the small internal adhesive gap is
not an aerodynamic feature. Sleeve-to-body adhesive fillets and the thin collar-fairing lip are not resolved aerodynamic
surfaces. Attachment strength is unverified.

The payload is an internal mass with provisional combined electronics/battery/ wiring dimensions and CG. Dummy and
actual cases deliberately match mass and CG; they are not independent measurements. Empty retains the bay and hardware.
External antennas/cameras are rejected rather than silently omitting their drag. No camera field of view or radio
performance is promised.

## Metrics and error corrections

- Event metrics use the first event occurrence and interpolate neighboring samples. Deployment at/after ground impact is
  unavailable, not a valid low deployment speed.
- Landing descent is the magnitude of **vertical** speed at ground impact. OpenRocket's native ground-hit summary is
  **total** speed; these differ in wind. Both are retained and total speed is compared against the native result.
- Minimum ascent stability includes all samples from guide departure strictly before apogee/deployment/ground. No
  low-speed or high-angle samples are hidden. The speed, time and angle of attack at the minimum expose the limitations
  of interpreting a static CP near apogee.
- Aborted runs can have missing channels. They remain failed cases with null unavailable outputs, never zero-filled
  successes.
- Constant wind, zero turbulence and ISA atmosphere are explicit demonstration assumptions. Landing displacement is
  scenario-specific, not a recovery radius guarantee. Chute Cd is assumed, not measured; native recovery does not test
  packing, ejection force, heat or attachment strength.

## Selection and uncertainty

Start with bounded deterministic grids, retain rejected geometry and every failed flight, and compare A/B/C cases across
empty/dummy/actual loads. A motor letter alone does not establish suitability. Manufacturer maximum liftoff mass is
checked separately from guide speed and other criteria. C5-3 was added within the original 18 mm A/B/C scope after
conventional A8/B4/C6 cases failed; its specific newer curve identity must not be substituted with an older C5 curve.

Nominal passes remain `incomplete inputs`; no flight-eligible ranking is produced. The shortlist is a comparison for
review, not a clearance to fly. The stress command evaluates bounded mass, CG, chute-Cd and wind corners. Those corners
have no assigned probabilities: a pass fraction is not reliability. Geometry/material assumptions and manufacturing
tolerances still need physical validation even if every simulated corner passes.

## Future boundaries

Keep configuration, CAD, native flight generation, simulation and evaluation as small separate modules. Future flight
logs can compare measured mass, descent and drift with retained time series. Use passive data before fitting a surrogate
or launching a probabilistic Monte Carlo study; specify distributions and validate coverage first. Latin-hypercube
sampling can reduce sampling cost once enough parameters justify it. Bayesian optimization is premature for this small
grid. Optional CFD should answer a named aerodynamic uncertainty with mesh/time-step convergence and a benchmark before
importing coefficients. Precision recovery, active guidance, deployment electronics and firmware are not implemented or
validated by this MVP.
