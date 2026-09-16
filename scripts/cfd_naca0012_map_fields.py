"""Prolong solution fields between adjacent exactly nested TMR NACA grids."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np


FIELDS = ("U", "p", "T", "k", "omega", "nut", "alphat")
IMAGE_ID = "sha256:143e0e81aa690349714910f096ef1a2dc5fbc723a27355f5078839503a9b7634"
NONUNIFORM = re.compile(
    r"internalField\s+nonuniform\s+List<(scalar|vector)>\s+(\d+)\s*\(\s*"
    r"(.*?)\s*\)\s*;",
    re.DOTALL,
)
UNIFORM = re.compile(r"internalField\s+uniform\s+[^;]+;")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def mapping_compatibility(source: dict, target: dict) -> dict:
    source_grid = source.get("grid_dimensions")
    target_grid = target.get("grid_dimensions")
    if not (
        isinstance(source_grid, list)
        and isinstance(target_grid, list)
        and len(source_grid) == len(target_grid) == 2
        and target_grid == [2 * value - 1 for value in source_grid]
    ):
        raise ValueError("Source and target must be adjacent exactly nested TMR grids")
    condition_keys = (
        "mach",
        "reynolds_number_chord",
        "angle_of_attack_deg",
        "transport_model",
        "turbulent_prandtl",
        "freestream_k_over_acoustic_speed_squared",
        "freestream_omega_mu_over_rho_acoustic_speed_squared",
    )
    source_conditions = source.get("conditions", {})
    target_conditions = target.get("conditions", {})
    compared = {
        "benchmark": (source.get("benchmark"), target.get("benchmark")),
        "convection_scheme": (source.get("convection_scheme"), target.get("convection_scheme")),
        "model_mapping": (source.get("model_mapping"), target.get("model_mapping")),
        **{
            key: (source_conditions.get(key), target_conditions.get(key))
            for key in condition_keys
        },
    }
    mismatches = {key: values for key, values in compared.items() if values[0] != values[1]}
    if source.get("benchmark") != "TMR 2D NACA 0012" or mismatches:
        raise ValueError(f"Source and target configurations differ: {mismatches}")
    return {
        "source_grid_dimensions": source_grid,
        "target_grid_dimensions": target_grid,
        "configuration_fields_matched": sorted(compared),
    }


def latest_time(case: Path) -> Path:
    candidates = []
    for item in case.iterdir():
        if item.is_dir():
            try:
                value = float(item.name)
            except ValueError:
                continue
            if value > 0:
                candidates.append((value, item))
    if not candidates:
        raise ValueError("Source case has no positive reconstructed solution time")
    return max(candidates)[1]


def parse_internal_field(text: str, cells: int) -> tuple[str, np.ndarray]:
    match = NONUNIFORM.search(text)
    if match is None or int(match.group(2)) != cells:
        raise ValueError("Source field is not a matching nonuniform reconstructed field")
    kind, _, payload = match.groups()
    if kind == "scalar":
        values = np.fromstring(payload, sep=" ")[:, None]
    else:
        rows = re.findall(r"\(([^()]*)\)", payload)
        values = np.asarray([[float(value) for value in row.split()] for row in rows])
        if values.ndim != 2 or values.shape[1] != 3:
            raise ValueError("Malformed vector internal field")
    if len(values) != cells or not np.all(np.isfinite(values)):
        raise ValueError("Malformed or non-finite internal field values")
    return kind, values


def prolong_cells(values: np.ndarray, source_shape: tuple[int, int]) -> np.ndarray:
    rows, columns = source_shape
    components = values.shape[1]
    coarse = values.reshape(rows, columns, components)

    x = (np.arange(2 * columns) + 0.5) / 2.0 - 0.5
    x0 = np.clip(np.floor(x).astype(int), 0, columns - 1)
    x1 = np.clip(x0 + 1, 0, columns - 1)
    wx = np.clip(x - x0, 0.0, 1.0)[None, :, None]
    across = (1.0 - wx) * coarse[:, x0, :] + wx * coarse[:, x1, :]

    y = (np.arange(2 * rows) + 0.5) / 2.0 - 0.5
    y0 = np.clip(np.floor(y).astype(int), 0, rows - 1)
    y1 = np.clip(y0 + 1, 0, rows - 1)
    wy = np.clip(y - y0, 0.0, 1.0)[:, None, None]
    fine = (1.0 - wy) * across[y0, :, :] + wy * across[y1, :, :]
    if not np.all(np.isfinite(fine)):
        raise ValueError("Prolongation produced non-finite values")
    return fine.reshape(4 * rows * columns, components)


def replace_internal_field(text: str, kind: str, values: np.ndarray) -> str:
    if len(UNIFORM.findall(text)) != 1:
        raise ValueError("Target field must contain exactly one uniform internal field")
    if kind == "scalar":
        body = "\n".join(f"{row[0]:.15g}" for row in values)
    else:
        body = "\n".join("(" + " ".join(f"{value:.15g}" for value in row) + ")" for row in values)
    replacement = f"internalField nonuniform List<{kind}>\n{len(values)}\n(\n{body}\n)\n;"
    return UNIFORM.sub(replacement, text, count=1)


def map_fields(source: Path, target: Path, source_audit: Path) -> dict:
    source = source.resolve(strict=True)
    target = target.resolve(strict=True)
    if (target / "execution.json").exists():
        raise ValueError("Refusing to map into an already executed target case")
    record_path = target / "map-fields-execution.json"
    if record_path.exists():
        raise FileExistsError(record_path)
    source_spec = json.loads((source / "benchmark-spec.json").read_text())
    target_spec_path = target / "benchmark-spec.json"
    target_spec = json.loads(target_spec_path.read_text())
    compatibility = mapping_compatibility(source_spec, target_spec)
    if target_spec["model_mapping"]["image_id"] != IMAGE_ID:
        raise ValueError("Target does not use the pinned CFD image")
    source_execution = json.loads((source / "execution.json").read_text())
    if not source_execution or not all(stage.get("stage_passed") for stage in source_execution):
        raise ValueError("Source case must have a fully passed execution record")
    source_audit = source_audit.resolve(strict=True)
    audit = json.loads(source_audit.read_text())
    if (
        Path(audit.get("case", "")).resolve() != source
        or not audit.get("coarse_preflight_passed")
        or not audit.get("long_window_trend_gate")
        or not audit.get("solver_residual_gate")
    ):
        raise ValueError("Source case must have a matching passed force/residual audit")
    source_time = latest_time(source)
    numeric_target_times = []
    for item in target.iterdir():
        if item.is_dir():
            try:
                numeric_target_times.append(float(item.name))
            except ValueError:
                pass
    if numeric_target_times != [0.0]:
        raise ValueError("Target must contain only its generated zero-time directory")

    source_ni, source_nj = source_spec["grid_dimensions"]
    source_shape = (source_nj - 1, source_ni - 1)
    field_records = {}
    mapped_text = {}
    for name in FIELDS:
        source_field = source_time / name
        target_field = target / "0" / name
        if source_field.is_symlink() or target_field.is_symlink():
            raise ValueError(f"Refusing symlink field {name}")
        kind, values = parse_internal_field(
            source_field.read_text(), source_shape[0] * source_shape[1]
        )
        mapped = prolong_cells(values, source_shape)
        if name in {"T", "k", "omega", "nut", "alphat"} and np.min(mapped) < 0:
            raise ValueError(f"Mapped field {name} violates non-negativity")
        mapped_text[name] = replace_internal_field(target_field.read_text(), kind, mapped)
        field_records[name] = {
            "source_sha256": file_sha256(source_field),
            "mapped_sha256": hashlib.sha256(mapped_text[name].encode()).hexdigest(),
            "source_min": values.min(axis=0).tolist(),
            "source_max": values.max(axis=0).tolist(),
            "mapped_min": mapped.min(axis=0).tolist(),
            "mapped_max": mapped.max(axis=0).tolist(),
        }

    for name, text in mapped_text.items():
        (target / "0" / name).write_text(text)

    implementation = Path(__file__).resolve()
    record = {
        "stage": "structured bilinear prolongation between adjacent nested grids",
        "stage_passed": True,
        "implementation": str(implementation),
        "implementation_sha256": file_sha256(implementation),
        "source_read_only": True,
    }
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    target_spec["initialization"] = {
        "method": "structured bilinear logical-coordinate prolongation",
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_audit": str(source_audit),
        "source_audit_sha256": file_sha256(source_audit),
        "mapping_image_id": None,
        "implementation_sha256": record["implementation_sha256"],
        **compatibility,
        "fields": field_records,
    }
    target_spec_path.write_text(json.dumps(target_spec, indent=2) + "\n")
    return target_spec["initialization"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(map_fields(args.source, args.target, args.source_audit), indent=2))


if __name__ == "__main__":
    main()
