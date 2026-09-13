# Rocket Workbench

Local Python 3.14 / uv / CadQuery / OpenRocket design and simulation workflow. No cloud service, paid simulation license
or LLM is needed inside the workflow. This is a **provisional review package**, not a physically validated rocket.

For the local Zensical site and GitHub Pages setup, see [documentation](docs/DOCUMENTATION.md).

Start with [current designs, simulations and downloads](docs/CURRENT_DESIGN.md), [build instructions](docs/BUILD.md),
[shopping guide](docs/SHOPPING.md), and [component-level avionics](docs/AVIONICS_DESIGN.md). The
[old-news archive](docs/ARCHIVE.md) contains superseded results; all physical fit, strength, pressure and flight checks
remain pending.

## Setup

Tested platform: macOS ARM, Python 3.14.6, Java 21.0.3+7-LTS-152. Install
[uv](https://docs.astral.sh/uv/getting-started/installation/) and a Java 21 JDK. The Java binary is not redistributed or
downloaded by this project. Set `ROCKET_JVM` to your JDK's `lib/server/libjvm.dylib` (macOS), `libjvm.so` (Linux), or
`jvm.dll` (Windows), and `ROCKET_JAVA` to the corresponding Java executable. Only the stated macOS runtime is
integration-tested; another runtime needs the same acceptance checks. On the tested machine the adapter finds the
installed JDK 21 automatically, avoiding its unrelated default Java 8.

From the repository root:

```sh
uv python install 3.14.6
uv sync --locked --extra cad
uv run --frozen python scripts/bootstrap.py
uv run --frozen rocket-workbench doctor
uv run --frozen rocket-workbench integration-proof
uv run --frozen pytest --run-integration -q
```

The first two setup steps may download Python/packages. The bootstrap step downloads the official OpenRocket 24.12 JAR
and verifies its SHA256; it refuses to overwrite a mismatched existing file. Supply `ROCKET_JAR` if the verified JAR is
stored elsewhere. The bridge is pinned to the OpenRocket-owned source revision, not inferred from PyPI. Java may need
permission for macOS preferences outside a restrictive sandbox. No credentials or API keys are required.

After setup, ordinary use is offline:

```sh
uv run --offline --frozen rocket-workbench validate examples/avionics-performance.yaml
uv run --offline --frozen rocket-workbench build examples/avionics-performance.yaml
uv run --offline --frozen rocket-workbench simulate examples/avionics-performance.yaml
uv run --offline --frozen pytest -q
```

Use `report <run-directory>` to regenerate Markdown/CSV from saved results, and `motors C5` to inspect actual installed
curves. Commands create unique run directories; no prior run is overwritten by generation/simulation. `build` exports
CAD and normalized flight models but does **not** simulate flights. `validate` needs no JVM/CAD. Baseline CAD requires
the `cad` extra. The unchanged `examples/upstream-simple.ork` is a separate simulator reference, not our rocket.

Exit codes: 0 means command execution succeeded, **not** that criteria passed; 1 means invalid inputs or execution
failure. `validate`, `build`, and `simulate` accept `--strict`, returning 2 for incomplete inputs or unmet engineering
gates. All current candidates remain incomplete for physical flight approval. Fast tests skip real integration unless
`--run-integration` is supplied.

## Inputs and artifacts

Example YAML files use JSON syntax (valid YAML) for explicit quantities: `value`, `unit`, `provenance`, `source`.
Unknown masses are rejected rather than filled with zero. Edit a copy, keep the measured/assumed distinction, validate,
and generate again. `scripts/create_examples.py`, `create_tradeoff.py`, and `create_review_candidates.py` recreate the
demonstration examples; do not run them over personally edited examples without preserving those edits.

Every full candidate run includes resolved inputs, configuration hash, CAD STEP/STL/preview, normalized `.ork` files for
all loadings and each simulated case, mass ledger, JSON time series/events/motor curves, CSV, Markdown and logs. New run
manifests include dependency/runtime versions through the hashed results, source file hashes and artifact hashes. A
missing Git revision is reported as null when unavailable. The source and documentation are published on GitHub. Sweeps
retain rejected inputs and failed simulations. Stress cases also retain their per-corner inputs. Null outputs mean
unavailable, never zero performance.

Keep results and their input/configuration files together. `runs/` is ignored by Git by default and is not permanent
archival storage by itself. Early development runs may predate schema/interface corrections; use the reviewed runs
linked in the findings, not the earliest files. No automatic deletion or migration of historical evidence is performed.

## Model boundaries

See [MODELING](docs/MODELING.md) for metric definitions, corrected errors, independent engine comparison, geometry
approximations and future CFD/logging boundaries. See [MEASUREMENTS](docs/MEASUREMENTS.md) before updating the payload,
material, guide or recovery system. No powered avionics, active guidance, motor manufacture, custom ignition,
ejection-charge design or legal-site determination is included. Generic capacity does not establish fit for every
XIAO/sensor stack.

Exact dependencies are in `uv.lock`; use `uv add`/`uv lock` for deliberate future updates and rerun acceptance tests. Do
not manually guess transitive versions. Upstream license/source information is in [THIRD_PARTY](docs/THIRD_PARTY.md).
The [guideline catalog](docs/GUIDELINES.yaml) distinguishes rules, heuristics and preferences;
[adapter contracts](docs/ARCHITECTURE.md) document extension boundaries.
