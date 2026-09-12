# Adapter and artifact contracts

The implemented domain is `Config` (Pydantic, schema version 1), not an OpenRocket or CadQuery object.
`cad.build(Config, output)` returns plain part mass/CG records; `flight_model.generate(Config, parts, loading, path)`
exports native XML and an independent dry ledger. `Engine` owns Java objects internally and returns plain
JSON-compatible simulation records. `report.evaluate(result, Config)` separates execution, numeric criteria and missing
physical checks. No OpenFOAM/control packages or placeholder physics are required.

Concrete existing boundary examples:

```json
{ "mass_g": 12.5, "cg_x_mm": 133.5, "provenance": "estimate", "source": "example only" }
```

```json
{
  "schema_version": 1,
  "cases": [
    {
      "id": "actual-C5-3-wind2",
      "loading": "actual",
      "wind_m_s": 2,
      "execution": "completed",
      "metrics": { "apogee_m": null },
      "warnings": []
    }
  ]
}
```

These fragments illustrate types, not measured or simulated values. Actual full schemas/records are in the example
configurations and retained results. A case ID is unique within its timestamp/UUID run; configuration/content hashes
connect a printed revision to its assumptions. Future observations should reference run ID, configuration SHA256, part
hashes, as-built measurements and case ID, with their own timestamps/sensor calibration and coordinate conventions.
Missing outputs remain null. Do not serialize Java instances into domain artifacts.

Current recovery contract is a parachute with diameter, packing envelope, Cd and motor-ejection delay. Environment
carries explicit ISA/site/guide/wind/seed. Neither is silently upgraded into a canopy/control or wind-profile
simulation. Unsupported external protrusions and unknown configuration fields are errors. Schema migration must be
explicit; old development runs remain preserved.

## Future aerodynamic dataset contract (not implemented)

An external dataset must define at least:

```yaml
schema_version: 1
backend: external-example-not-supported
configuration_sha256: required
coordinates: body +x nose-to-aft; define +y/+z and force/moment signs explicitly
reference_length: { value: 0.0416, unit: m }
reference_area: { value: 0.001359179, unit: m2 }
moment_reference: { value: [0, 0, 0], unit: m, description: nose tip example }
independent_axes: [Mach, Reynolds, angle_of_attack_rad]
valid_ranges: required-from-validated-study
coefficients: required-with-force-and-moment-definitions
provenance: required solver/version/mesh/boundaries/convergence/benchmark
out_of_range: error
```

The area is an illustrative circular body reference; a future importer must verify conventions and units, not accept
this fragment as usable data. Specify whether moments are about the nose, CG or another point and transform them
explicitly. Preserve native results alongside any externally supplied data. Lookup/override support in the pinned engine
must be investigated before an importer is implemented; no coefficient importer exists in this MVP.

A future CFD adapter would export a selected case and return a traceable dataset, not run on every CAD change. Require a
named question, benchmark and mesh/time- step convergence. Flexible parachutes and precision recovery need separately
scoped models and measured behavior, including sensing, actuation, delay and failure modes. A native Python engine port
is also a separate parity project, not a replacement justified by a few matching trajectories. Preserve upstream
licenses for any translated code.
