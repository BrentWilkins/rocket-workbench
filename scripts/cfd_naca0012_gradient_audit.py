"""Compare limited and unlimited OpenFOAM velocity gradients on a sealed solution."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import numpy as np

from cfd_naca0012_farfield_audit import latest_time, mesh_geometry, sha256
from cfd_naca0012_surface_force_audit import internal_scalar, patch_owners


LIMITED_GRADIENT = "grad(U) $limited;"
UNLIMITED_GRADIENT = "grad(U) Gauss linear;"


def internal_tensor(path: Path) -> np.ndarray:
    match = re.search(
        r"\binternalField\s+nonuniform\s+List<tensor>\s+(\d+)\s*"
        r"\(\s*(.*?)\s*\)\s*;",
        path.read_text(),
        re.DOTALL,
    )
    if not match:
        raise ValueError(f"Missing nonuniform internal tensor field in {path}")
    values = np.asarray(
        [
            [float(value) for value in row.split()]
            for row in re.findall(r"\(([^()]*)\)", match.group(2))
        ],
        dtype=float,
    )
    if values.shape != (int(match.group(1)), 9) or not np.all(np.isfinite(values)):
        raise ValueError(f"Malformed internal tensor field in {path}")
    return values.reshape(-1, 3, 3)


def image_identity(image: str) -> dict:
    return json.loads(
        subprocess.check_output(["docker", "image", "inspect", image], text=True)
    )[0]


def run_variant(
    case: Path,
    time: Path,
    output: Path,
    image_id: str,
    cpus: float,
    memory: str,
    unlimited: bool,
) -> dict:
    name = "unlimited" if unlimited else "limited"
    with tempfile.TemporaryDirectory(prefix=f"naca0012-grad-{name}-", dir="/tmp") as temporary:
        temporary_case = Path(temporary) / "case"
        temporary_case.mkdir()
        for item in ("0", "constant", "system"):
            shutil.copytree(case / item, temporary_case / item, symlinks=True)
        shutil.copytree(time, temporary_case / time.name, symlinks=True)
        schemes = temporary_case / "system" / "fvSchemes"
        scheme_text = schemes.read_text()
        if scheme_text.count(LIMITED_GRADIENT) != 1:
            raise ValueError("Expected exactly one named limited velocity gradient")
        if unlimited:
            schemes.write_text(scheme_text.replace(LIMITED_GRADIENT, UNLIMITED_GRADIENT))

        shell_stage = (
            "source /usr/lib/openfoam/openfoam2512/etc/bashrc && "
            "rhoSimpleFoam -postProcess -func 'grad(U)' -latestTime; "
            f"status=$?; chown -R {os.getuid()}:{os.getgid()} /case; exit $status"
        )
        command = [
            "docker",
            "run",
            "--rm",
            "--network=none",
            "--cpus",
            str(cpus),
            "--memory",
            memory,
            "--mount",
            f"type=bind,src={temporary_case},dst=/case",
            image_id,
            shell_stage,
        ]
        result = subprocess.run(command, text=True, capture_output=True)
        log = output / f"rhoSimpleFoam-gradU-{name}.log"
        log.write_text(result.stdout + result.stderr)
        generated = temporary_case / time.name / "grad(U)"
        passed = (
            result.returncode == 0
            and "FOAM FATAL" not in log.read_text()
            and generated.is_file()
        )
        field = output / f"grad(U)-{name}"
        if passed:
            shutil.copyfile(generated, field)
        record = {
            "variant": name,
            "stage_passed": passed,
            "gradient_scheme": UNLIMITED_GRADIENT if unlimited else LIMITED_GRADIENT,
            "returncode": result.returncode,
            "command": command,
            "log": str(log),
            "log_sha256": sha256(log),
            "field": str(field) if passed else None,
            "field_sha256": sha256(field) if passed else None,
        }
        if not passed:
            raise RuntimeError(json.dumps(record))
        return record


def distribution(values: np.ndarray) -> dict:
    return {
        "minimum": float(values.min()),
        "median": float(np.median(values)),
        "mean": float(values.mean()),
        "maximum": float(values.max()),
        "rms": float(np.sqrt(np.mean(values**2))),
    }


def audit(
    plan_path: Path,
    case: Path,
    force_audit_path: Path,
    output: Path,
    image: str,
    cpus: float,
    memory: str,
) -> dict:
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    if not plan.get("declared_before_new_solver_execution"):
        raise ValueError("Gate 3 remediation plan was not predeclared")
    case = case.resolve(strict=True)
    force_audit_path = force_audit_path.resolve(strict=True)
    force_audit = json.loads(force_audit_path.read_text())
    if Path(force_audit.get("case", "")).resolve() != case or not force_audit.get(
        "coarse_preflight_passed"
    ):
        raise ValueError("Force audit does not establish an admissible source case")
    time = latest_time(case)
    identity = image_identity(image)
    expected_id = plan["fixed_configuration"]["image_id"]
    if identity["Id"] != expected_id:
        raise ValueError("Gradient postprocessor image differs from the predeclared image")

    output.mkdir(parents=True, exist_ok=False)
    records = [
        run_variant(case, time, output, identity["Id"], cpus, memory, False),
        run_variant(case, time, output, identity["Id"], cpus, memory, True),
    ]
    limited = internal_tensor(Path(records[0]["field"]))
    unlimited = internal_tensor(Path(records[1]["field"]))
    if limited.shape != unlimited.shape:
        raise ValueError("Gradient variants have different field sizes")

    owners = patch_owners(case, "airfoil")
    difference = np.linalg.norm(limited - unlimited, axis=(1, 2))
    unlimited_norm = np.linalg.norm(unlimited, axis=(1, 2))
    relative = difference / np.maximum(unlimited_norm, np.finfo(float).tiny)
    symmetric_limited = 0.5 * (limited + np.swapaxes(limited, 1, 2))
    symmetric_unlimited = 0.5 * (unlimited + np.swapaxes(unlimited, 1, 2))
    s2_limited = 2 * np.sum(symmetric_limited**2, axis=(1, 2))
    s2_unlimited = 2 * np.sum(symmetric_unlimited**2, axis=(1, 2))
    s2_relative = np.abs(s2_limited - s2_unlimited) / np.maximum(
        np.abs(s2_unlimited), np.finfo(float).tiny
    )
    nut = internal_scalar(time / "nut")
    production_limited = nut * s2_limited
    production_unlimited = nut * s2_unlimited
    production_relative = np.abs(production_limited - production_unlimited) / np.maximum(
        np.abs(production_unlimited), np.finfo(float).tiny
    )
    face_centers, _ = mesh_geometry(case, "airfoil")
    retained_surface = (face_centers[:, 0] >= 0.01) & (face_centers[:, 0] <= 0.98)

    def comparison(indices: np.ndarray) -> dict:
        return {
            "count": int(len(indices)),
            "changed_fraction": float(np.mean(difference[indices] > 0)),
            "gradient_absolute_frobenius_difference": distribution(difference[indices]),
            "gradient_relative_frobenius_difference": distribution(relative[indices]),
            "S2_relative_difference": distribution(s2_relative[indices]),
            "nut_S2_relative_difference": distribution(production_relative[indices]),
            "sum_nut_S2_limited_over_unlimited": float(
                production_limited[indices].sum()
                / production_unlimited[indices].sum()
            ),
        }

    return {
        "schema_version": 1,
        "scope": "fixed-solution velocity-gradient limiter diagnosis",
        "predeclared_plan": {"path": str(plan_path), "sha256": sha256(plan_path)},
        "case": str(case),
        "case_spec_sha256": sha256(case / "benchmark-spec.json"),
        "nut_field_sha256": sha256(time / "nut"),
        "force_audit": str(force_audit_path),
        "force_audit_sha256": sha256(force_audit_path),
        "solution_time": float(time.name),
        "image_id": identity["Id"],
        "resource_limits": {"cpus": cpus, "memory": memory},
        "network_disabled": True,
        "variants": records,
        "comparison": {
            "all_cells": comparison(np.arange(len(limited))),
            "airfoil_owner_cells": comparison(owners),
            "airfoil_owner_cells_x_over_c_0p01_to_0p98": comparison(
                owners[retained_surface]
            ),
        },
        "method": "Evaluate the same sealed U field once with the production cellLimited Gauss linear 1 scheme and once with Gauss linear; no flow equation is advanced.",
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--force-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--image", default="rocket-workbench-cfd:2512-sstm-exact-production-pr072"
    )
    parser.add_argument("--cpus", type=float, default=2.0)
    parser.add_argument("--memory", default="4g")
    args = parser.parse_args()
    result = audit(
        args.plan,
        args.case,
        args.force_audit,
        args.output,
        args.image,
        args.cpus,
        args.memory,
    )
    output = args.output / "naca0012-gradient-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "comparison": result["comparison"]}))


if __name__ == "__main__":
    main()
