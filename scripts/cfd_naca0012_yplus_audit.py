"""Audit solver-context NACA 0012 y-plus output without mutating a CFD case."""

import argparse
import hashlib
import json
import re
from pathlib import Path


YPLUS_LIMIT = 1.0


def parse_yplus_log(text: str) -> dict[str, float]:
    if "Unable to find turbulence model" in text:
        raise ValueError("yPlus ran without a turbulence model")
    matches = re.findall(
        r"patch airfoil y\+ : min = ([0-9.eE+-]+), max = ([0-9.eE+-]+),"
        r" average = ([0-9.eE+-]+)",
        text,
    )
    if len(matches) != 1:
        raise ValueError(f"Expected one airfoil y-plus summary, found {len(matches)}")
    minimum, maximum, average = map(float, matches[0])
    return {"minimum": minimum, "maximum": maximum, "average": average}


def audit(case: Path, postprocess_log: Path) -> dict:
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    if spec.get("benchmark") != "TMR 2D NACA 0012":
        raise ValueError("Not a TMR NACA 0012 case")
    runtime_library = spec.get("model_mapping", {}).get("runtime_library")
    expected_model = {
        "libTmrSSTmCompressible.so": "TmrSSTm",
        "libTmrSSTmExactProductionCompressible.so": "TmrSSTmExactProduction",
    }.get(runtime_library)
    if expected_model is None:
        raise ValueError("Not a mapped compressible SSTm runtime")
    log_text = postprocess_log.read_text()
    if f"Selecting RAS turbulence model {expected_model}" not in log_text:
        raise ValueError(f"Post-processing log did not select {expected_model}")
    values = parse_yplus_log(log_text)
    return {
        "case": str(case),
        "grid_dimensions": spec["grid_dimensions"],
        "case_spec_sha256": hashlib.sha256(spec_path.read_bytes()).hexdigest(),
        "postprocess_log": str(postprocess_log),
        "postprocess_log_sha256": hashlib.sha256(
            postprocess_log.read_bytes()
        ).hexdigest(),
        "method": "rhoSimpleFoam -postProcess -func yPlus -latestTime on temporary copy",
        "wall_resolved_maximum_y_plus_limit": YPLUS_LIMIT,
        "airfoil_y_plus": values,
        "wall_resolved_y_plus_gate": values["maximum"] <= YPLUS_LIMIT,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--postprocess-log", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.case, args.postprocess_log)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-yplus-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
