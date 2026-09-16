"""Create the predeclared half-relaxation SA convergence mechanism test."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from cfd_naca0012_sa_control_continue import continue_case


METHOD = "same-grid documented-SA half-relaxation mechanism test"
PLAN_SHA256 = "4d7e467b9ffe026155946644321fc6683b297b20705308a6bb46e0dcdf810257"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def restart(
    source: Path, source_audit: Path, target: Path, plan: Path
) -> dict:
    plan = plan.resolve(strict=True)
    if sha256(plan) != PLAN_SHA256:
        raise ValueError("SA damping plan checksum mismatch")
    base_record = continue_case(source, source_audit, target)
    target = target.resolve(strict=True)

    fv_solution_path = target / "system" / "fvSolution"
    fv_solution = fv_solution_path.read_text()
    fv_solution = replace_once(fv_solution, "fields { p 0.3; }", "fields { p 0.15; }")
    fv_solution = replace_once(
        fv_solution,
        "equations { U 0.7; nuTilda 0.7; }",
        "equations { U 0.35; nuTilda 0.35; }",
    )
    fv_solution_path.write_text(fv_solution)

    snapshot = target / "provenance" / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    spec_path = target / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    spec["initialization"]["method"] = METHOD
    spec["initialization"]["physics_or_numerics_changed"] = True
    spec["mechanism_test"] = {
        "name": "uniform_half_scale_SIMPLE_under_relaxation",
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "before": {"p": 0.3, "U": 0.7, "nuTilda": 0.7},
        "after": {"p": 0.15, "U": 0.35, "nuTilda": 0.35},
        "only_numerical_relaxation_changed": True,
    }
    spec["numerics"] = dict(spec["numerics"])
    spec["numerics"]["relaxation"] = spec["mechanism_test"]["after"]
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")

    record = dict(base_record)
    record.update(
        {
            "stage": METHOD,
            "method": METHOD,
            "physics_or_numerics_changed": True,
            "target_case_spec_sha256": sha256(spec_path),
            "plan": str(plan),
            "plan_sha256": PLAN_SHA256,
            "implementation_snapshot": str(snapshot),
            "implementation_sha256": sha256(snapshot),
            "fv_solution_sha256": sha256(fv_solution_path),
        }
    )
    (target / "sa-continuation-execution.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(restart(args.source, args.source_audit, args.target, args.plan)))


if __name__ == "__main__":
    main()
