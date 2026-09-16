"""Audit conserved transport and state distortion on a NACA farfield patch."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np


FIELDS = ("phi", "U", "p", "T", "rho")
SEGMENTS = ("upstream", "upper", "lower", "downstream")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def latest_time(case: Path) -> Path:
    candidates: list[tuple[float, Path]] = []
    for child in case.iterdir():
        if not child.is_dir() or child.is_symlink():
            continue
        try:
            value = float(child.name)
        except ValueError:
            continue
        if value > 0 and all((child / name).is_file() for name in FIELDS):
            candidates.append((value, child))
    if not candidates:
        raise ValueError(f"No reconstructed positive solution time in {case}")
    return max(candidates, key=lambda item: item[0])[1]


def braced_block(text: str, name: str) -> str:
    match = re.search(rf"(?m)^\s*{re.escape(name)}\s*$\s*\{{", text)
    if not match:
        raise ValueError(f"Missing dictionary block {name!r}")
    opening = text.find("{", match.start())
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return text[opening + 1 : index]
    raise ValueError(f"Unclosed dictionary block {name!r}")


def counted_list(text: str) -> tuple[int, str]:
    match = re.search(r"(?m)^\s*(\d+)\s*$\s*\(", text)
    if not match:
        raise ValueError("Missing counted OpenFOAM list")
    count = int(match.group(1))
    opening = text.find("(", match.start())
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "(":
            depth += 1
        elif text[index] == ")":
            depth -= 1
            if depth == 0:
                return count, text[opening + 1 : index]
    raise ValueError("Unclosed counted OpenFOAM list")


def mesh_geometry(case: Path, patch: str = "farfield") -> tuple[np.ndarray, np.ndarray]:
    poly = case / "constant" / "polyMesh"
    point_count, point_body = counted_list((poly / "points").read_text())
    points = np.asarray(
        [[float(value) for value in row.split()] for row in re.findall(r"\(([^()]*)\)", point_body)],
        dtype=float,
    )
    if points.shape != (point_count, 3) or not np.all(np.isfinite(points)):
        raise ValueError("Malformed mesh points")

    face_count, face_body = counted_list((poly / "faces").read_text())
    face_rows = re.findall(r"\b(\d+)\s*\(([^()]*)\)", face_body)
    if len(face_rows) != face_count:
        raise ValueError("Malformed mesh faces")
    faces: list[np.ndarray] = []
    for declared, payload in face_rows:
        labels = np.fromstring(payload, sep=" ", dtype=int)
        if len(labels) != int(declared):
            raise ValueError("Face vertex count mismatch")
        faces.append(labels)

    patch_dict = braced_block((poly / "boundary").read_text(), patch)
    n_faces_match = re.search(r"\bnFaces\s+(\d+)\s*;", patch_dict)
    start_match = re.search(r"\bstartFace\s+(\d+)\s*;", patch_dict)
    if not n_faces_match or not start_match:
        raise ValueError(f"Patch {patch!r} lacks nFaces/startFace")
    n_faces = int(n_faces_match.group(1))
    start = int(start_match.group(1))
    selected = faces[start : start + n_faces]
    if len(selected) != n_faces:
        raise ValueError("Patch face range exceeds mesh")

    centers = np.empty((n_faces, 3), dtype=float)
    area_vectors = np.empty((n_faces, 3), dtype=float)
    for index, labels in enumerate(selected):
        vertices = points[labels]
        centers[index] = vertices.mean(axis=0)
        area_vectors[index] = 0.5 * sum(
            np.cross(vertices[i], vertices[(i + 1) % len(vertices)])
            for i in range(len(vertices))
        )
    if np.any(np.linalg.norm(area_vectors, axis=1) <= 0):
        raise ValueError("Farfield contains zero-area faces")
    return centers, area_vectors


def patch_values(path: Path, patch: str, expected_count: int) -> np.ndarray:
    block = braced_block(path.read_text(), patch)
    nonuniform = re.search(
        r"\bvalue\s+nonuniform\s+List<(scalar|vector)>\s+(\d+)\s*\(\s*(.*?)\s*\)\s*;",
        block,
        re.DOTALL,
    )
    if nonuniform:
        kind, declared, payload = nonuniform.groups()
        if int(declared) != expected_count:
            raise ValueError(f"Patch value count mismatch in {path}")
        if kind == "vector":
            values = np.asarray(
                [
                    [float(value) for value in row.split()]
                    for row in re.findall(r"\(([^()]*)\)", payload)
                ],
                dtype=float,
            )
            expected_shape = (expected_count, 3)
        else:
            values = np.fromstring(payload, sep=" ", dtype=float)
            expected_shape = (expected_count,)
        if values.shape != expected_shape:
            raise ValueError(f"Malformed nonuniform patch values in {path}")
        return values

    uniform = re.search(r"\bvalue\s+uniform\s+(\([^;]+\)|[^;\s]+)\s*;", block)
    if not uniform:
        raise ValueError(f"Patch {patch!r} has no serialized value in {path}")
    payload = uniform.group(1).strip()
    if payload.startswith("("):
        row = np.fromstring(payload[1:-1], sep=" ", dtype=float)
        if row.shape != (3,):
            raise ValueError(f"Malformed uniform vector in {path}")
        return np.repeat(row[None, :], expected_count, axis=0)
    return np.full(expected_count, float(payload), dtype=float)


def segment_labels(area_vectors: np.ndarray) -> np.ndarray:
    planar = area_vectors[:, :2]
    dominant_x = np.abs(planar[:, 0]) >= np.abs(planar[:, 1])
    labels = np.empty(len(planar), dtype=object)
    labels[dominant_x & (planar[:, 0] < 0)] = "upstream"
    labels[dominant_x & (planar[:, 0] >= 0)] = "downstream"
    labels[~dominant_x & (planar[:, 1] >= 0)] = "upper"
    labels[~dominant_x & (planar[:, 1] < 0)] = "lower"
    if set(labels) != set(SEGMENTS):
        raise ValueError(f"Farfield segmentation incomplete: {sorted(set(labels))}")
    return labels


def state_statistics(values: np.ndarray, areas: np.ndarray, reference: np.ndarray) -> dict:
    weights = areas / areas.sum()
    delta = values - reference
    if values.ndim == 1:
        return {
            "area_weighted_mean": float(np.sum(weights * values)),
            "minimum": float(values.min()),
            "maximum": float(values.max()),
            "area_weighted_rms_delta_from_freestream": float(
                np.sqrt(np.sum(weights * delta**2))
            ),
            "maximum_absolute_delta_from_freestream": float(np.max(np.abs(delta))),
        }
    return {
        "area_weighted_mean": np.sum(weights[:, None] * values, axis=0).tolist(),
        "minimum": values.min(axis=0).tolist(),
        "maximum": values.max(axis=0).tolist(),
        "area_weighted_rms_delta_from_freestream": np.sqrt(
            np.sum(weights[:, None] * delta**2, axis=0)
        ).tolist(),
        "maximum_absolute_delta_from_freestream": np.max(np.abs(delta), axis=0).tolist(),
    }


def transport_statistics(
    mask: np.ndarray,
    phi: np.ndarray,
    velocity: np.ndarray,
    pressure: np.ndarray,
    temperature: np.ndarray,
    area_vectors: np.ndarray,
    pressure_reference: float,
    cp: float,
) -> dict:
    selected_phi = phi[mask]
    selected_u = velocity[mask]
    selected_p = pressure[mask]
    selected_t = temperature[mask]
    selected_sf = area_vectors[mask]
    inflow = -float(selected_phi[selected_phi < 0].sum())
    outflow = float(selected_phi[selected_phi > 0].sum())
    throughflow = inflow + outflow
    net_mass = float(selected_phi.sum())
    total_enthalpy = cp * selected_t + 0.5 * np.sum(selected_u**2, axis=1)
    enthalpy_flux = selected_phi * total_enthalpy
    convective_momentum = np.sum(selected_phi[:, None] * selected_u, axis=0)
    pressure_traction = np.sum(
        (selected_p - pressure_reference)[:, None] * selected_sf, axis=0
    )
    return {
        "face_count": int(mask.sum()),
        "mass_flux": {
            "inflow_positive_magnitude": inflow,
            "outflow_positive_magnitude": outflow,
            "net_outward": net_mass,
            "absolute_closure_over_total_throughflow": (
                abs(net_mass) / throughflow if throughflow else None
            ),
        },
        "convective_momentum_flux_outward": convective_momentum.tolist(),
        "gauge_pressure_traction_outward": pressure_traction.tolist(),
        "convective_plus_pressure_momentum_flux_outward": (
            convective_momentum + pressure_traction
        ).tolist(),
        "convective_total_enthalpy_flux_outward": float(
            np.sum(enthalpy_flux)
        ),
        "absolute_energy_closure_over_total_transport": (
            float(abs(np.sum(enthalpy_flux)) / np.sum(np.abs(enthalpy_flux)))
            if np.any(enthalpy_flux)
            else None
        ),
    }


def audit_case(case: Path) -> dict:
    case = case.resolve(strict=True)
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    conditions = spec["conditions"]
    time = latest_time(case)
    centers, area_vectors = mesh_geometry(case)
    n_faces = len(centers)
    fields = {name: patch_values(time / name, "farfield", n_faces) for name in FIELDS}
    phi = fields["phi"]
    velocity = fields["U"]
    pressure = fields["p"]
    temperature = fields["T"]
    density = fields["rho"]
    if any(not np.all(np.isfinite(value)) for value in fields.values()):
        raise ValueError("Farfield values contain non-finite entries")

    areas = np.linalg.norm(area_vectors, axis=1)
    labels = segment_labels(area_vectors)
    p_ref = float(conditions["pressure_pa"])
    t_ref = float(conditions["temperature_k"])
    rho_ref = float(conditions["density_kg_m3"])
    u_ref = np.asarray([conditions["speed_m_s"], 0.0, 0.0], dtype=float)
    cp = 1004.5
    whole_mask = np.ones(n_faces, dtype=bool)

    return {
        "case": str(case),
        "solution_time": float(time.name),
        "grid_dimensions": spec["grid_dimensions"],
        "domain": spec.get("domain"),
        "source_hashes": {
            "benchmark_spec": sha256(spec_path),
            "points": sha256(case / "constant" / "polyMesh" / "points"),
            "faces": sha256(case / "constant" / "polyMesh" / "faces"),
            "boundary": sha256(case / "constant" / "polyMesh" / "boundary"),
            **{name: sha256(time / name) for name in FIELDS},
        },
        "farfield": {
            "face_count": n_faces,
            "area": float(areas.sum()),
            "state": {
                "U": state_statistics(velocity, areas, u_ref),
                "p": state_statistics(pressure, areas, np.asarray(p_ref)),
                "T": state_statistics(temperature, areas, np.asarray(t_ref)),
                "rho": state_statistics(density, areas, np.asarray(rho_ref)),
            },
            "transport": transport_statistics(
                whole_mask,
                phi,
                velocity,
                pressure,
                temperature,
                area_vectors,
                p_ref,
                cp,
            ),
            "segments": {
                segment: {
                    "area": float(areas[labels == segment].sum()),
                    "state": {
                        "U": state_statistics(velocity[labels == segment], areas[labels == segment], u_ref),
                        "p": state_statistics(pressure[labels == segment], areas[labels == segment], np.asarray(p_ref)),
                        "T": state_statistics(temperature[labels == segment], areas[labels == segment], np.asarray(t_ref)),
                        "rho": state_statistics(density[labels == segment], areas[labels == segment], np.asarray(rho_ref)),
                    },
                    "transport": transport_statistics(
                        labels == segment,
                        phi,
                        velocity,
                        pressure,
                        temperature,
                        area_vectors,
                        p_ref,
                        cp,
                    ),
                }
                for segment in SEGMENTS
            },
        },
    }


def audit(plan_path: Path, cases: list[Path]) -> dict:
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    if not plan.get("declared_before_new_solver_execution"):
        raise ValueError("Remediation plan was not predeclared")
    results = [audit_case(case) for case in cases]
    if len({tuple(item["grid_dimensions"]) for item in results}) != len(results):
        raise ValueError("Cases must have distinct grid/domain dimensions")
    return {
        "schema_version": 1,
        "scope": "read-only NACA 0012 farfield state and transport diagnosis",
        "predeclared_plan": {"path": str(plan_path), "sha256": sha256(plan_path)},
        "method": {
            "mass": "Sum reconstructed outward face mass flux phi; report inflow and outflow separately.",
            "momentum": "Sum phi times boundary velocity plus gauge-pressure traction over oriented patch faces.",
            "energy": "Sum phi times Cp*T plus one-half velocity squared, with Cp=1004.5 J/(kg K).",
            "segments": "Classify each face by the dominant component and sign of its oriented area vector.",
            "limitations": "Diagnostic balance omits viscous work and heat conduction on the remote farfield; it is not an acceptance gate.",
        },
        "implementation": {
            "path": str(Path(__file__).resolve()),
            "sha256": sha256(Path(__file__).resolve()),
        },
        "cases": results,
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--case", required=True, type=Path, action="append", dest="cases")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.plan, args.cases)
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "naca0012-farfield-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "cases": len(result["cases"])}))


if __name__ == "__main__":
    main()
