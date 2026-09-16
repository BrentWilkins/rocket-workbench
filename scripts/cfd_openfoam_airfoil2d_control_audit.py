"""Audit the exact upstream OpenFOAM airFoil2D installation control."""

import argparse
import gzip
import hashlib
import json
import math
import re
from pathlib import Path


SOURCE_REPOSITORY = "https://gitlab.com/openfoam/core/openfoam.git"
SOURCE_TAG = "OpenFOAM-v2512"
SOURCE_COMMIT = "87ed40d256d22ea38fcc648dfc82a22162427b18"
SOURCE_PATH = "tutorials/incompressible/simpleFoam/airFoil2D"
DOCUMENTED = {
    "grid_points": [897, 257],
    "airfoil_surface_points": 513,
    "velocity_m_s": [51.4815, 0.0, 0.0],
    "kinematic_viscosity_m2_s": 8.58e-6,
    "angle_deg": 0.0,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_integrity(pristine: Path, case: Path) -> tuple[list[dict], bool]:
    records = []
    for source in sorted(path for path in pristine.rglob("*") if path.is_file()):
        relative = source.relative_to(pristine)
        executed = case / relative
        source_digest = sha256(source)
        executed_digest = sha256(executed) if executed.is_file() else None
        records.append(
            {
                "path": str(relative),
                "source_sha256": source_digest,
                "executed_sha256": executed_digest,
                "matches": source_digest == executed_digest,
            }
        )
    return records, bool(records) and all(record["matches"] for record in records)


def parse_uniform_vector(path: Path, keyword: str) -> list[float]:
    text = path.read_text()
    match = re.search(
        rf"\b{re.escape(keyword)}\s+uniform\s*\(([^)]+)\)\s*;", text
    )
    if not match:
        raise ValueError(f"Could not find uniform vector {keyword!r} in {path}")
    values = [float(value) for value in match.group(1).split()]
    if len(values) != 3:
        raise ValueError(f"Expected three components for {keyword!r} in {path}")
    return values


def parse_scalar(path: Path, keyword: str) -> float:
    match = re.search(
        rf"^\s*{re.escape(keyword)}\s+(?:\[[^]]+\]\s+)?([0-9.eE+-]+)\s*;",
        path.read_text(),
        re.MULTILINE,
    )
    if not match:
        raise ValueError(f"Could not find scalar {keyword!r} in {path}")
    return float(match.group(1))


def parse_foam_list_count(path: Path) -> int:
    with gzip.open(path, "rt") as stream:
        text = stream.read()
    match = re.search(r"\n\s*(\d+)\s*\n\s*\(", text)
    if not match:
        raise ValueError(f"Could not find OpenFOAM list count in {path}")
    return int(match.group(1))


def parse_patch_faces(path: Path, patch: str) -> int:
    with gzip.open(path, "rt") as stream:
        text = stream.read()
    block = re.search(rf"\b{re.escape(patch)}\s*\{{(.*?)\}}", text, re.DOTALL)
    if not block:
        raise ValueError(f"Could not find patch {patch!r} in {path}")
    count = re.search(r"\bnFaces\s+(\d+)\s*;", block.group(1))
    if not count:
        raise ValueError(f"Could not find nFaces for patch {patch!r} in {path}")
    return int(count.group(1))


def solver_completion(log_path: Path, reconstruction_log_path: Path) -> dict:
    log = log_path.read_text()
    reconstruction = reconstruction_log_path.read_text()
    matches = re.findall(r"SIMPLE solution converged in (\d+) iterations", log)
    fatal_markers = (
        "FOAM FATAL",
        "mpirun has detected an attempt to run as root",
        "No times selected",
    )
    clean = not any(marker in log or marker in reconstruction for marker in fatal_markers)
    reconstructed = bool(re.search(r"\nEnd\s*$", reconstruction))
    return {
        "converged_iteration": int(matches[-1]) if matches else None,
        "solver_reported_convergence": bool(matches),
        "fatal_marker_absent": clean,
        "reconstruction_completed": reconstructed,
        "passed": bool(matches) and clean and reconstructed,
    }


def audit(pristine: Path, case: Path, image_id: str) -> dict:
    pristine = pristine.resolve(strict=True)
    case = case.resolve(strict=True)
    files, integrity = input_integrity(pristine, case)
    velocity = parse_uniform_vector(pristine / "0.orig" / "U", "internalField")
    speed = math.hypot(velocity[0], velocity[1])
    angle = math.degrees(math.atan2(velocity[1], velocity[0]))
    viscosity = parse_scalar(
        pristine / "constant" / "transportProperties", "nu"
    )
    cells = parse_foam_list_count(pristine / "constant/polyMesh.orig/cells.gz")
    wall_faces = parse_patch_faces(
        pristine / "constant/polyMesh.orig/boundary.gz", "walls"
    )
    completion = solver_completion(
        case / "log.simpleFoam", case / "log.reconstructPar"
    )
    packaged = {
        "cells": cells,
        "airfoil_wall_faces": wall_faces,
        "velocity_m_s": velocity,
        "speed_m_s": speed,
        "angle_deg": angle,
        "kinematic_viscosity_m2_s": viscosity,
    }
    mismatch = {
        "grid": cells != (DOCUMENTED["grid_points"][0] - 1)
        * (DOCUMENTED["grid_points"][1] - 1),
        "airfoil_resolution": wall_faces
        != DOCUMENTED["airfoil_surface_points"] - 1,
        "velocity": velocity != DOCUMENTED["velocity_m_s"],
        "angle": not math.isclose(angle, DOCUMENTED["angle_deg"], abs_tol=1e-12),
        "viscosity": not math.isclose(
            viscosity,
            DOCUMENTED["kinematic_viscosity_m2_s"],
            rel_tol=0.0,
            abs_tol=1e-15,
        ),
    }
    control_passed = integrity and completion["passed"]
    return {
        "scope": "Exact upstream packaged tutorial installation control only",
        "source": {
            "repository": SOURCE_REPOSITORY,
            "tag": SOURCE_TAG,
            "commit": SOURCE_COMMIT,
            "path": SOURCE_PATH,
        },
        "image_id": image_id,
        "pristine": str(pristine),
        "case": str(case),
        "input_integrity_gate": integrity,
        "input_files": files,
        "solver_completion": completion,
        "packaged_configuration": packaged,
        "documented_validation_configuration": DOCUMENTED,
        "packaged_vs_documented_mismatch": mismatch,
        "packaged_vs_documented_match": not any(mismatch.values()),
        "installation_control_passed": control_passed,
        "nasa_validation_agreement_claimed": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pristine", required=True, type=Path)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--image-id", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.pristine, args.case, args.image_id)
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "openfoam-airfoil2d-control-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
