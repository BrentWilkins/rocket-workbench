# Printable Model Rocket Design Workbench

Product requirements and implementation brief for Codex • 12 September 2026

## 1. Assignment

Build a local, reproducible workflow that connects a complete, simple printable model rocket to OpenRocket flight
simulations. The first product deliverable is a small, conventionally stable rocket Brent can print, assemble, inspect,
and launch with his boys using a commercial motor and passive recovery. Provide the full design and build package, not
only a payload bay. Include an avionics compartment sized for the actual selected electronics in v1. Architect the
software for later autonomous precision recovery and selective OpenFOAM analysis without implementing those advanced
systems in the MVP.

This document authorizes implementation of the software in the provided project workspace. Begin with the integration
proof in milestone 1, then continue through the MVP where inputs permit. Do not stop after proposing an architecture.
Unknown physical dimensions should block a final fitted design, not the software or a clearly labeled demonstration.

This is a development brief, not an approved rocket design. No simulations or physical validation have been completed as
part of this brief.

## 2. User and intended outcome

Brent wants inexpensive model rocketry projects to enjoy with his young boys. He wants minimal glue-dependent assembly,
replaceable printed parts, and room to grow into custom designs and onboard electronics. He owns a Bambu X1 Carbon and
Seeed XIAO ESP32-based boards; at least one board has a camera and antenna. Exact board variant, battery, and base
rocket are not yet confirmed.

Prefer Python and a straightforward command-line workflow. The result should be understandable and editable by a
developer, with CAD exports available for inspection in other tools. Keep recurring costs at zero for the local design
software; Codex usage is separate.

Primary user story: “Give me a simple little 3D printed rocket design, its flight simulation, and everything I need to
print and assemble it for a first launch with my boys.”

The first rocket must physically fit the selected avionics assembly, while remaining flyable with that assembly absent
or replaced by a secured mass surrogate. Working electronics and custom flight-control firmware are not prerequisites
for the first flight. Choose a conservative conventional design with printable nose and fin/body components as
appropriate. Standard lightweight tubes, motor-mount components, harness, recovery material, and thermal protection are
acceptable where they improve practicality; explain the bill of materials. Prefer substantial useful printed parts, but
do not force every component to be printed. Keep assembly and part count modest. Compare feasible A/B/C motor cases
without assuming the lightest motor will lift the finished print.

Long-term user story: “Extend the same project toward autonomous precision recovery near the launch point, ultimately
aspiring to touchdown on the pad, and use CFD where detailed aerodynamic questions justify it.” This is a future
research objective, not a required capability or accuracy promise for the first rocket.

## 3. Scope and priorities

### MVP

- One conventional, single-stage rocket with one commercial 18 mm motor.
- One complete baseline rocket design with printable components, standard purchased parts identified, passive recovery,
  and documented assembly. An avionics bay sized for the selected board, camera, battery, connectors, and mounting
  hardware is required in v1; installed electronics remain optional per flight.
- A complete first-launch shopping list covering the parachute, harness, attachments, ejection protection, commercial
  motor/igniter, and reusable launch equipment. Assume no existing rocket equipment; distinguish purchased parts,
  printed parts, reusable equipment, and per-flight consumables, with quantities and dated price estimates when
  researched.
- Parametric CAD source, STEP and STL exports, and an OpenRocket `.ork` model.
- Batch simulations using actual motor data and explicit launch conditions.
- A readable comparison report and machine-readable results.
- Reproducible environment, meaningful tests, and setup instructions.

### Later

- Autonomous precision recovery toward a designated landing area near the launch point. Touchdown on the pad is
  aspirational. Begin later work with logged passive descent and landing-error prediction; evaluate steerable recovery
  separately. Do not assume stock OpenRocket validates this system.
- Additional interchangeable nose cones, fin assemblies, payload bays, and more extensively printed airframes.
- Optional OpenFOAM studies for specific aerodynamic uncertainties, with benchmark and convergence evidence before using
  results in flight predictions.
- Bounded parameter sweeps for geometry, mass, and recovery choices.
- Import of slicer mass estimates and comparison with measured printed parts.
- Flight-log comparison and refined mass/drag assumptions.
- A small local interface only if the CLI becomes inconvenient.

### Out of scope

- Motor manufacture, propellant work, ignition hardware, staging, or high-power designs. Active flight guidance
  implementation is outside the initial MVP, but is a long-term goal rather than a permanent exclusion.
- Camera firmware, live video, radio tracking infrastructure, or autonomous deployment electronics.
- A hosted service, accounts, cloud database, Kubernetes, or an LLM dependency inside the simulation loop.
- Automatic determination that a launch location is legal or suitable.
- Claiming that a simulated candidate is structurally validated or cleared to fly.

## 4. Architecture and integration decisions

Use a Python package managed with `uv`, a typed configuration model, and a modest CLI. CadQuery is the preferred CAD
engine because it supports Python-driven parametric geometry and CAD/mesh exports. Isolate CAD and simulator
dependencies behind small adapters; avoid a general plugin framework.

Use one canonical configuration to drive CAD and flight-model generation. Do not maintain unrelated sets of geometry
constants. Pick a documented coordinate convention and explicit units at every boundary; user-facing millimeters and
grams are acceptable, with deliberate conversion to the simulator's units.

OpenRocket automation is the first integration check. Its linked API page is incomplete. The original
`SilentSys/orhelper` README targets an older release, but the OpenRocket-owned fork at
https://github.com/openrocket/orhelper explicitly lists OpenRocket 24.12 or above. This is a documented compatibility
claim, not a test performed for this project. Do not assume a current stable CLI or invent Java/Python methods.

Investigate current upstream source and available wrappers, then select the simplest maintained, verifiable route:

1. First test the OpenRocket-owned `orhelper` fork against the latest stable OpenRocket release available at
   implementation time. Verify that the installed package matches the intended source revision rather than assuming the
   PyPI package matches the fork. Investigate patching only for reproduced gaps. Check upstream branches and pull
   requests for existing compatibility work. Reproduce any failure before patching. Inspect Java package/class changes,
   JVM startup and dependency loading, document loading/saving, simulation calls, listeners, and result access as
   possible migration areas; these are investigation targets, not confirmed defects.
2. If needed, maintain a small local patch or fork of the Python bridge, pinned to an exact revision. Preserve licensing
   and prepare a reviewable patch with integration tests; publishing or submitting upstream is not required. Do not
   replace this investigation with an old OpenRocket install merely because the README names one.
3. Use a small Java adapter around OpenRocket's simulation core only if evidence shows that repairing the bridge is
   impractical. Document the specific blocker and tradeoff.

Compatibility acceptance requires more than importing the module: load a reference `.ork`, run a real simulation,
extract time-series data and warnings, modify a component, save and reload the document, and run multiple cases without
state leaking between them. Compare results to the same pinned OpenRocket engine through an independent reference path.
Record the exact tested release rather than claiming compatibility with an unbounded “latest.”

Pin the exact OpenRocket, Java, bridge, Python, and CAD versions actually tested. Document upstream URLs and licenses.
Prefer an external adapter over maintaining an OpenRocket fork. Do not downgrade silently to an old release just to
satisfy a wrapper. If a downgrade is necessary, explain the compatibility tradeoff in a short architecture decision
record.

The CAD mesh is not the flight model. Represent supported exterior geometry using OpenRocket components, and explicitly
map printed structures and electronics to mass and center-of-gravity information. State approximations and unsupported
geometry in the report. In particular, do not silently ignore an externally mounted camera or antenna.

## 5. Required inputs

Every consequential physical input must record its value, unit, and provenance: measured, manufacturer specification,
estimate, or demonstration assumption. Missing values must remain identifiable.

| Group         | Inputs                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Base rocket   | Body outer/inner diameter, tube length, nose shape and shoulder dimensions, fin geometry, motor mount position, component masses and positions; optional existing `.ork`                                                                      |
| V1 avionics   | Required for final bay sizing: exact XIAO variant and camera assembly, battery, connector/wire envelopes, mounting hardware, dimensions, masses and positions, service clearances, antenna placement. Installing them is optional per flight. |
| Printed parts | Material, wall thickness, fit clearance, relevant print assumptions, estimated or measured mass and balance location                                                                                                                          |
| Recovery      | Parachute dimensions and assumptions, attachment locations, separation interface, available packing space                                                                                                                                     |
| Motor         | Manufacturer, exact designation and delay, dimensions, loaded/spent mass where available, thrust-curve source and identity                                                                                                                    |
| Launch        | Site elevation, atmospheric assumptions, wind, launch guide length and angle, and scenario seed where applicable                                                                                                                              |
| Evaluation    | Desired altitude range and explicit review thresholds with rationale/source                                                                                                                                                                   |

Do not infer adequate liftoff performance from the motor letter alone. Treat A/B/C combinations as candidates to
evaluate, not as guaranteed upgrades. Reject incompatible motor dimensions.

Provide a supported reference rocket for simulator comparison and a separate complete printable baseline design. Keep
the simulator reference unchanged. For the printable baseline provide empty-bay, secured dummy-payload, and
actual-avionics configurations using the same exterior geometry. For the generated design, select and document
dimensions and standard interfaces; no existing purchased rocket is required. Distinguish design dimensions from
measurements of the eventual printed assembly.

## 6. Functional requirements

### FR-1: Configuration and validation

Validate units, positive dimensions, geometric feasibility, required clearances, motor fit, and missing physical inputs.
Report actionable errors. Preserve a resolved configuration with every run. Unknown mass must never silently become
zero.

### FR-2: Complete printable baseline rocket

Generate a complete conventional rocket design, including printable nose and fin/body components appropriate to the
selected construction. Define body and motor interfaces, launch-guide attachment, motor retention, recovery separation,
and harness attachment. Specify all purchased components and quantities, printable part files, material/print
assumptions, assembly order, and inspection steps. Provide a print-and-build guide and an assembly preview. Include the
fitted avionics bay in the first design, but do not require operating electronics for launch.

Use configurable dimensions and named assembly interfaces for the required v1 avionics bay and removable sled. Size them
from the actual selected hardware, including cable bends, connectors, camera clearance, battery retention, and
installation/removal access. Separate the avionics from the chute packing and ejection-gas volume, and specify a
protection approach without assuming printed plastic alone is adequate thermal protection. Final fit cannot be
established from a generic XIAO board envelope. Obtain exact board/camera and battery identification and dimensions
before calling the bay ready to fabricate; meanwhile continue software work with clearly flagged provisional inputs.

Account for parachute packing, harness routing, attachment load paths, assembly access, and hardware mass. Prefer simple
mechanical assembly and serviceability. Keep external geometry conventional for the first version. Export separate
printable parts and an assembly view or labeled preview.

The initial baseline includes an actual specified parachute and shock cord/harness, not merely a recovery placeholder in
the simulator. Select a purchasable chute size/material and compatible attachment method after estimating the complete
descending mass. Record the manufacturer's specifications and the drag assumptions used for descent predictions. Include
every required connector, line, fastener, adhesive if unavoidable, and flame-resistant recovery protection in the bill
of materials. Specify motor retention and launch-guide hardware as well. If a streamer is evaluated as an alternative,
retain a parachute-equipped baseline unless Brent chooses otherwise.

Check that the chute and harness physically fit the recovery compartment and identify the nose/body separation
interface. Include packing and assembly instructions sourced from the selected components where available. Simulated
deployment does not demonstrate real ejection reliability; document the necessary physical fit and separation checks.
Model the complete recovery-system mass, and report predicted descent speed and wind drift with assumptions rather than
selecting a chute by appearance alone.

Provide a first-launch equipment list: compatible reusable pad/guide and electrical controller, commercial motors with
the selected delay, compatible igniters/starters, required batteries, and recovery consumables. Include quantities for
an initial three-flight outing as a clearly labeled planning default. Keep reusable setup cost separate from rocket cost
and recurring flight cost. Research affordable compatible products during implementation, record sources/date, and do
not purchase anything automatically. Flag missing specifications instead of inventing product compatibility or
availability.

Support PLA and PETG as configurable material assumptions. Do not promise temperature resistance or strength from a
material name alone; record print orientation and identify attachments requiring physical validation. Treat minimizing
glue and fumes as an assembly preference, not a claim that printing eliminates chemical exposure.

### FR-3: Consistent flight model

Generate or update a `.ork` file that opens successfully in the pinned OpenRocket release. Preserve unrelated components
when modifying an imported design. Map component position, exterior dimensions, mass, and center of gravity
consistently. Avoid double counting masses when applying overrides. Distinguish dry assembly mass from launch mass with
a motor installed.

### FR-4: Simulation and evidence

Run the reference simulation and configurable commercial motor/delay cases. Capture apogee, speed at launch-guide
departure, relevant stability information, deployment time/altitude/speed, descent performance, and landing displacement
where supported. Include units, simulation warnings, failures, and the exact motor data used.

If an output is unavailable, label it unavailable; do not fabricate it or substitute an unrelated metric. Keep failed
cases in the report. Allow configurable wind scenarios; clearly identify predicted displacement as scenario-dependent.

### FR-5: Evaluation and iteration

Separate simulation completion from engineering evaluation. Use statuses such as `simulation failed`,
`incomplete inputs`, `outside configured limits`, and `meets configured simulation criteria`. Never label a case simply
`safe` or `approved`.

Every evaluation threshold must be visible and have a source or be marked as an engineering assumption. When necessary
criteria are absent, report the case as unevaluated. Rank only eligible candidates, with a transparent objective such as
closeness to a user-selected altitude range and low added mass. Do not default to maximum altitude.

The MVP must compare motor/delay cases for the empty bay, secured dummy payload, and actual avionics. Include the bay,
sled, retention hardware, battery, wiring and connectors in their appropriate cases. Place dummy mass to approximate the
actual payload center of gravity, rather than matching only total weight. Use measured assembled mass and balance to
update simulations when available. Evaluate motor/delay selection, stability, launch-guide departure, deployment and
descent for each loading separately; do not assume one motor fits every case. If no 18 mm A/B/C case meets the
configured criteria, report that explicitly and propose a documented design tradeoff instead of escalating motor size
silently. Geometry optimization is optional later; if implemented, use bounded deterministic sweeps before more
elaborate optimizers and retain the evaluated configurations.

### FR-6: Outputs and reproducibility

Each run produces a separate output directory containing resolved inputs, CAD exports, `.ork`, results JSON/CSV, a
Markdown report, and logs. Record configuration hash, dependency versions, motor data identity, and repository revision
when available. Do not overwrite prior runs by default.

The report must show assumptions, missing measurements, geometry approximations, comparison results, and outstanding
physical checks. With dependencies and motor data installed, ordinary generation and simulation must work without
network access.

## 7. Proposed command interface

These are requirements for our own CLI, not existing OpenRocket commands. Adapt names if needed and document actual
implemented behavior.

```sh
uv run rocket-workbench doctor
uv run rocket-workbench validate examples/reference.yaml
uv run rocket-workbench build examples/reference.yaml
uv run rocket-workbench simulate examples/reference.yaml
uv run rocket-workbench report <run-directory>
```

`doctor` checks dependencies and the simulator adapter. Validation must run before build/simulation. Commands should
return nonzero for execution or invalid-input failures; engineering criteria outcomes should also be available as
structured results, with an optional strict exit mode for automation.

## 8. Milestones and acceptance checks

| Milestone                   | Deliverable                                                                                                | Acceptance evidence                                                                                                                                                                                                                                                                                                         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Prove integration        | Pinned environment, adapter, reference rocket, short decision record                                       | Automated simulation completes with real motor data. Compare the same configuration against an independently run OpenRocket GUI case or an authoritative fixture. Record tolerances and explain discrepancies. If GUI comparison cannot be performed, mark that check pending explicitly.                                   |
| 2. Connect models           | Canonical configuration and generated flight/CAD representations                                           | A known dimension change reaches both models. Independently check representative dimensions and mass/CG calculations. Generated `.ork` loads successfully.                                                                                                                                                                  |
| 3. Generate baseline rocket | Complete design, assembly preview, STEP/STL exports, bill of materials and print/build guide               | Every structural part is either generated or identified as a purchased component; solids/meshes and interfaces are checked; motor retention and passive recovery are documented. Fitted avionics compartment and service access checked against identified hardware; operating electronics not required.                    |
| 4. Compare flights          | Motor/delay batch, JSON/CSV, report                                                                        | Successful and failing cases appear correctly; actual curves/delays are identified; no failed or incomplete case is ranked as eligible.                                                                                                                                                                                     |
| 5. Handoff                  | README, example, tests, limitations, measurement checklist, complete build and first-launch shopping lists | A fresh supported environment can reproduce the demonstration through documented commands. No undisclosed manual editing between CAD and simulation. The parachute, harness, protection, retention, launch equipment, and consumables are accounted for; estimated total cost and outstanding physical checks are explicit. |

Use tests where they catch consequential mistakes: units and coordinate conversion, component mass aggregation and CG,
override double counting, adapter integration, unsupported geometry, invalid fit, and warning/failure propagation.
Validate representative CAD outputs rather than testing every getter. Separate slower real-simulator integration tests
from fast tests; mocked results cannot establish milestone 1.

Software completion does not require Brent to have purchased a rocket. Deliver a concrete baseline fabrication candidate
and its complete build package. As-built mass, balance, interfaces, motor fit, and recovery fit remain physical checks
before a first launch. Feed measured values back into the simulation before selecting the final motor/delay. Physical
assembly and flight validation must not be reported as completed by software.

The first user milestone is a successful simple print, assembly, launch, and recovery. The software handoff is an
intermediate step toward that outcome. Advanced architecture work must not delay the baseline design merely to complete
unused infrastructure.

## 9. Suggested repository layout

| Path                        | Purpose                                                            |
| --------------------------- | ------------------------------------------------------------------ |
| `pyproject.toml`, `uv.lock` | Reproducible Python environment                                    |
| `src/rocket_workbench/`     | Configuration, CAD, simulator adapter, evaluation, reporting, CLI  |
| `java/`                     | Only if a Java adapter is needed                                   |
| `examples/`                 | Simulator reference and complete printable baseline configurations |
| `tests/`                    | Focused correctness and integration checks                         |
| `docs/`                     | Decisions, measurement guide, modeling limitations                 |
| `runs/`                     | Generated output, normally ignored by Git                          |

Respect any existing repository layout and instructions. Keep the implementation small enough for one person to
maintain.

## 10. Instructions for the first Codex session

1. Read this brief and applicable repository instructions. Inspect the environment and existing files before making
   changes.
2. Establish a short implementation plan and start milestone 1 immediately. Verify current upstream integration options
   rather than coding against guessed APIs.
3. Create a working reference simulation, retain real output, and document the selected integration. If one route fails,
   investigate the next reasonable route before declaring a blocker.
4. Continue through the MVP using clearly labeled sample inputs. Ask for physical measurements only when needed for a
   personalized fit or a decision that cannot reasonably be deferred.
5. Keep a brief progress record distinguishing implemented, verified, and pending work. On handoff, provide exact
   commands, generated example outputs, test results, and remaining limitations.

Do not install system-wide tools, delete unrelated files, purchase hardware, or publish the project merely to complete
this brief. Follow the host's permissions and use a local environment where practical. Do not stop for approval on
ordinary reversible implementation choices already within this scope.

## 11. Starting references

These are research entry points, not a tested compatibility matrix. Check current upstream documentation and source
before implementation.

- [OpenRocket source](https://github.com/openrocket/openrocket)
- [OpenRocket downloads](https://openrocket.info/downloads)
- [Incomplete API documentation](https://openrocket.readthedocs.io/en/latest/dev_guide/api_documentation.html)
- [OpenRocket codebase walkthrough](https://openrocket.readthedocs.io/en/latest/dev_guide/codebase_walkthrough.html)
- [OpenRocket-owned orhelper bridge](https://github.com/openrocket/orhelper) — README lists OpenRocket 24.12 or above;
  test and pin this first.
- [Original orhelper Python bridge](https://github.com/SilentSys/orhelper) — historical repository; README targets
  OpenRocket 15.03.
- [CadQuery introduction](https://cadquery.readthedocs.io/en/latest/intro.html)
- [Codex CLI documentation](https://learn.chatgpt.com/docs/codex/cli)

## 12. Design guidelines and rule provenance

OpenRocket supplies flight-model calculations and analysis tools; it is not a complete rulebook for fabrication,
assembly, or active controls. Build a small, explicit guideline catalog alongside the workbench. Each entry must contain
an identifier, rationale, source URL and section where available, applicability, units, severity, and whether it is an
enforceable requirement, an engineering heuristic, or a project preference. Store thresholds separately from code, and
identify rules that require manual inspection. Do not infer that absence of simulator warnings establishes design
validity.

Use these sources for distinct purposes:

| Source                                                                                                                                                                       | Use                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [OpenRocket features](https://openrocket.info/features.html) and [advanced design guide](https://openrocket.readthedocs.io/en/latest/user_guide/advanced_rocket_design.html) | Supported geometry, CG/CP analysis, simulation, component modeling, and optimization capabilities                                       |
| [NASA Glenn rocket stability](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/rocket-stability/)                                                                    | Physical explanation of conventional passive stability; distinguish principles from quantitative project thresholds                     |
| [NAR Model Rocket Safety Code](https://www.nar.org/ModelRocketSafetyCode)                                                                                                    | Materials, commercial motors, recovery, and launch practices; keep these distinct from jurisdiction-specific law                        |
| Actual kit/motor/component manufacturer documentation                                                                                                                        | Fit, recommended motors/delays, assembly constraints, and hardware specifications                                                       |
| Measured print specimens and assembled components                                                                                                                            | Fit, mass, balance, attachment strength, recovery separation, and thermal protection evidence that flight simulation does not establish |

Cover at least conventional stability across relevant flight conditions, launch-guide departure performance, recovery
deployment speed, descent performance, motor fit, mass accounting, and recovery packing/attachment review. Derive
criteria from sources applicable to the chosen rocket, and document exceptions. A single static stability number or
universal thrust-to-weight rule must not substitute for relevant simulation and inspection.

For future active-control research, separately assess whether a simulator represents the necessary actuation, sensing,
delays, and failure behavior. Do not treat a successful passive OpenRocket simulation as validation of a controlled
vehicle. This brief does not select or implement a flight controller.

## 13. Extension architecture: required now, implemented incrementally

Keep domain data independent of OpenRocket, CadQuery, and OpenFOAM classes. Use small Python interfaces or functions
with typed inputs/outputs and versioned serialized artifacts. No service framework, plugin marketplace, or empty
advanced subsystem is needed. Implement only the baseline backend; document the following boundaries with concrete data
examples.

| Boundary                 | MVP implementation                                                                           | Future extension enabled                                                 |
| ------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Vehicle definition       | Components, geometry, material assumptions, mass/CG, named interfaces                        | Optional payloads and new printable assemblies                           |
| CAD generation           | CadQuery exports from the vehicle definition                                                 | Alternative geometry generators and analysis mesh export                 |
| Aerodynamic data         | Identify OpenRocket's native model and assumptions                                           | Externally generated coefficient datasets, including CFD or measurements |
| Flight simulation        | OpenRocket adapter using the preferred patched Python bridge                                 | Alternative flight/recovery models without changing CAD or reports       |
| Recovery definition      | Passive recovery type and parameters, deployment assumptions                                 | Separately scoped steerable recovery model                               |
| Environment              | Explicit atmosphere and wind scenario with provenance                                        | Wind profiles, measured conditions, and uncertainty scenarios            |
| Results and observations | Time-series and event records, units, coordinate conventions, predicted landing displacement | Measured flight logs and prediction-versus-observation comparisons       |
| Evaluation               | Sourced baseline criteria and transparent results                                            | Landing-error distributions and future experiment-specific criteria      |

Requirements for extension compatibility:

- Configuration schemas must have versions. V1 bay geometry requires an identified avionics envelope; the
  installed-payload selection can be empty, dummy, or actual. Future-analysis dependencies must not be required for
  baseline operation. Unknown capabilities produce explicit errors, never silent fallback to a simpler model.
- Document reference frames, units, reference area/length, moment reference point, and provenance for aerodynamic
  datasets. Record their applicable operating range; flag out-of-range use. Preserve native-model results when comparing
  external data.
- Advanced tools must be optional dependencies. A user can build and simulate the first rocket without installing
  OpenFOAM or any control-system tooling.
- Do not couple CFD execution into every geometry change or simulation. A later CFD adapter would export a case, run an
  explicitly selected analysis, and produce a traceable dataset. Verify the chosen OpenRocket release's import/override
  support and limitations before using it.
- A future OpenFOAM milestone must identify a specific question, a benchmark, mesh/convergence checks, and limitations.
  Agreement between simulations is a cross-check; physical measurements provide validation evidence. Flexible-canopy CFD
  is a separate advanced investigation, not the initial precision-recovery model.
- Precision recovery needs a separately scoped descent model and measured behavior. Begin with passive landing
  predictions and recorded landing error. Do not equate a specified surface wind with the actual wind throughout the
  descent, or promise pad-level accuracy.
- Preserve stable artifact identifiers so a printed revision, simulation, and later flight log can be compared. Keep
  results usable without Java-specific objects.

Acceptance now: baseline generation and simulation run with advanced dependencies absent; the fitted bay supports empty,
dummy, and actual loading cases without geometry changes; schema and adapter boundaries are documented; changing the
concrete simulator integration does not require rewriting the canonical vehicle definition or CAD generator. Do not
implement dummy physics to claim future capabilities are working.

Reference for later integration research:
[OpenRocket aerodynamic lookup tables](https://openrocket.readthedocs.io/en/latest/user_guide/advanced_flight_simulation.html#aerodynamic-lookup-tables).
Verify release-specific behavior before implementation.

## 14. Python port decision

Keep Python as the public interface while initially calling OpenRocket's Java engine through the tested bridge. Do not
make rewriting the engine a prerequisite for the first rocket. The repository separates its core and Swing UI, which
makes a core-only investigation more plausible than porting the complete application, but numerical correctness and
behavioral parity still require substantial verification.

If a native Python backend is explored later, scope a bounded subset and compare it against a pinned OpenRocket release
across meaningful regression cases. Account for component mass/inertia, aerodynamics, motor interpolation,
atmosphere/wind, integration, flight events, recovery, warnings, and file compatibility. Keep unsupported cases
explicit. Preserve applicable upstream license and attribution requirements for translated source. A port is a separate
milestone and must not replace the functioning bridge on the basis of a few matching trajectories.
