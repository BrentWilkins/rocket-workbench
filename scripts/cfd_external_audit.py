"""Compact read-only diagnostics for a supplied-exterior visualization case.

This deliberately does not run the expensive full CAD/surface symmetry audit or
award aerodynamic acceptance. Serialized STL normals are checked independently
of the mesher's successful surface-closure check.
"""

import argparse
import json
import re
import shlex
from pathlib import Path

import numpy as np

from cfd_audit import audit
from cfd_geometry_audit import read_binary_stl


def normal_diagnostics(normals, vertices):
    if not len(vertices) or not np.isfinite(vertices).all() or not np.isfinite(normals).all():
        raise ValueError("Require a nonempty finite serialized surface")
    cross = np.cross(vertices[:, 1] - vertices[:, 0], vertices[:, 2] - vertices[:, 0])
    double_area = np.linalg.norm(cross, axis=1)
    nondegenerate = double_area > 1e-18
    dot = np.full(len(vertices), np.nan)
    dot[nondegenerate] = np.einsum("ij,ij->i", normals[nondegenerate],
                                  cross[nondegenerate]) / double_area[nondegenerate]
    bad = ~nondegenerate | (dot < .999)
    tetra = np.einsum("ij,ij->i", vertices[:, 0],
                      np.cross(vertices[:, 1], vertices[:, 2])) / 6
    return {
        "triangles": len(vertices),
        "degenerate_triangles": int((~nondegenerate).sum()),
        "stored_normal_winding_mismatches": int(bad.sum()),
        "negative_normal_winding_count": int((dot < 0).sum()),
        "mismatch_triangle_area_m2": float(double_area[bad].sum() / 2),
        "total_triangle_area_m2": float(double_area.sum() / 2),
        "signed_volume_m3": float(tetra.sum()),
        "normal_winding_screen_passed": bool(not bad.any()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Choose a new audit output; preserve previous evidence")
    result = audit(args.case)
    normals, vertices = read_binary_stl(args.case / "constant/triSurface/rocket.stl")
    result["serialized_surface"] = normal_diagnostics(normals, vertices)
    execution = json.loads((args.case / "execution.json").read_text())
    solver_logs = [args.case / f"{index}-{shlex.split(stage['stage'])[0]}.log"
                   for index, stage in enumerate(execution)
                   if "simpleFoam" in shlex.split(stage["stage"])]
    if not solver_logs:
        solver_logs = list(args.case.glob("*-mpirun.log")) + list(args.case.glob("*-simpleFoam.log"))
        result["solver_log_not_in_execution_ledger"] = True
    if len(solver_logs) != 1:
        raise ValueError("Expected exactly one recorded simpleFoam solver stage")
    log = solver_logs[0].read_text()
    residuals = {}
    for field, initial in re.findall(r"Solving for (\w+), Initial residual = ([\deE.+-]+)", log):
        residuals.setdefault(field, []).append(float(initial))
    result["equation_initial_residuals"] = {
        name: {"last_logged": values[-1], "last_100_solve_records_max": max(values[-100:])}
        for name, values in residuals.items()
    }
    yplus_path = args.case / "postProcessing/yplus/0/yPlus.dat"
    if yplus_path.exists():
        rows = [line.split() for line in yplus_path.read_text().splitlines()
                if line.strip() and not line.startswith("#")]
        result["yplus_records"] = [
            {"iteration": float(row[0]), "patch": row[1], "minimum": float(row[2]),
             "maximum": float(row[3]), "average": float(row[4])}
            for row in rows
        ]
    result["scope"] = "Exploratory visualization; no coefficient acceptance or port delta"
    result["not_tested"] = ["Full CAD/STL symmetry", "Mesh/domain independence",
                            "Near-wall adequacy", "Ports/cavities", "Benchmark acceptance"]
    spec = json.loads((args.case / "case-spec.json").read_text())
    result["case_provenance"] = {
        key: spec[key] for key in ["source_step_sha256", "external_adapter_sha256",
                                  "speed_m_s", "alpha_deg", "cell_mm", "moment_origin_m"]
        if key in spec
    }
    result["case_provenance"]["image_id"] = json.loads(
        (args.case / "image.json").read_text())["Id"]
    for index, stage in enumerate(execution):
        if shlex.split(stage["stage"])[0] == "checkMesh":
            mesh_log = (args.case / f"{index}-checkMesh.log").read_text()
            cells = re.search(r"cells:\s+(\d+)", mesh_log)
            result["mesh_cells"] = int(cells[1]) if cells else None
    if "ring_tail" in spec:
        result["manifest_note"] = (
            "Unused zero-ring template metadata block retained; actual supplied STEP and its "
            "SHA-256 define geometry. CofR is the fixed geometric reference, not a CG claim."
        )
    result["source_case"] = str(args.case)
    reconstruction = args.case / "reconstruction.json"
    if reconstruction.exists():
        result["reconstruction"] = json.loads(reconstruction.read_text())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in
                      ["solver_completed", "tail_settled_screen", "serialized_surface"]}))


if __name__ == "__main__":
    main()
