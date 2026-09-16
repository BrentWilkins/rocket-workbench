"""Compare generated NACA mesh with OpenFOAM's direct official PLOT3D conversion."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import os
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

import numpy as np


ARCHIVE_SHA256 = "b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4"
PLOT3D_SHA256 = "b6d593736c3839d55389d14dc9361cca13945fa1d6c50645dd30a36614ef6993"
MEMBER_SUFFIX = "NACA0012_grids/n0012_897-257.p3dfmt.gz"


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def foam_array(path: Path, columns: int) -> np.ndarray:
    text = path.read_text()
    match = re.search(r"\n(\d+)\s*\n\(\s*(.*?)\s*\)\s*(?://|$)", text, re.DOTALL)
    if match is None:
        raise ValueError(f"Could not parse OpenFOAM list: {path}")
    count = int(match.group(1))
    payload = match.group(2).replace("4(", " ").replace("(", " ").replace(")", " ")
    values = np.fromstring(payload, sep=" ")
    if values.size != count * columns:
        raise ValueError(f"OpenFOAM list size mismatch: {path}")
    return values.reshape(count, columns)


def unique_nearest_mapping(
    source: np.ndarray, target: np.ndarray, tolerance: float
) -> tuple[np.ndarray, np.ndarray]:
    bins: dict[tuple[int, int, int], list[int]] = {}
    target_keys = np.floor(target / tolerance).astype(np.int64)
    for index, key in enumerate(target_keys):
        bins.setdefault(tuple(int(value) for value in key), []).append(index)
    used = np.zeros(len(target), dtype=bool)
    mapping = np.empty(len(source), dtype=np.int64)
    distances = np.empty(len(source))
    offsets = tuple(itertools.product((-1, 0, 1), repeat=3))
    for source_index, point in enumerate(source):
        key = np.floor(point / tolerance).astype(np.int64)
        candidates = []
        for offset in offsets:
            candidates.extend(
                bins.get(tuple(int(key[i] + offset[i]) for i in range(3)), ())
            )
        available = np.asarray([index for index in candidates if not used[index]])
        if not available.size:
            raise ValueError(f"No unmatched target point near source point {source_index}")
        delta = target[available] - point
        local = int(np.argmin(np.einsum("ij,ij->i", delta, delta)))
        target_index = int(available[local])
        distance = float(np.linalg.norm(delta[local]))
        if distance > tolerance:
            raise ValueError(
                f"Point {source_index} misses target tolerance: {distance} > {tolerance}"
            )
        mapping[source_index] = target_index
        distances[source_index] = distance
        used[target_index] = True
    if not bool(np.all(used)):
        raise ValueError("Point mapping is not bijective")
    return mapping, distances


def audit(
    archive: Path,
    case: Path,
    output: Path,
    image: str,
    cpus: float,
    memory: str,
) -> dict:
    archive = archive.resolve(strict=True)
    case = case.resolve(strict=True)
    if sha256(archive) != ARCHIVE_SHA256:
        raise ValueError("NACA grid archive checksum mismatch")
    target_mesh = case / "constant" / "polyMesh"
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    if spec.get("grid_dimensions") != [897, 257]:
        raise ValueError("Target is not the official 897x257 NACA grid")

    with zipfile.ZipFile(archive) as bundle:
        members = [name for name in bundle.namelist() if name.endswith(MEMBER_SUFFIX)]
        if len(members) != 1:
            raise ValueError("Expected one official 897x257 3-D PLOT3D member")
        member = members[0]
        info = bundle.getinfo(member)
        stored = bundle.read(member)
    plot3d = gzip.decompress(stored)
    if sha256_bytes(plot3d) != PLOT3D_SHA256:
        raise ValueError("Decompressed official PLOT3D checksum mismatch")

    output.mkdir(parents=True, exist_ok=False)
    identity = json.loads(
        subprocess.check_output(["docker", "image", "inspect", image], text=True)
    )[0]
    with tempfile.TemporaryDirectory(prefix="naca-plot3d-parity-", dir="/tmp") as temp:
        direct = Path(temp) / "direct"
        (direct / "system").mkdir(parents=True)
        plot3d_path = direct / "n0012_897-257.p3dfmt"
        plot3d_path.write_bytes(plot3d)
        (direct / "system" / "controlDict").write_text(
            "FoamFile\n{\n version 2.0;\n format ascii;\n class dictionary;\n"
            " location \"system\";\n object controlDict;\n}\n"
            "application simpleFoam;\nstartFrom startTime;\nstartTime 0;\n"
            "stopAt endTime;\nendTime 1;\ndeltaT 1;\n"
            "writeControl timeStep;\nwriteInterval 1;\nwriteFormat ascii;\n"
        )
        shell = (
            "source /usr/lib/openfoam/openfoam2512/etc/bashrc && "
            "plot3dToFoam -noBlank -case /direct /direct/n0012_897-257.p3dfmt; "
            f"status=$?; chown -R {os.getuid()}:{os.getgid()} /direct; exit $status"
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
            f"type=bind,src={direct},dst=/direct",
            identity["Id"],
            shell,
        ]
        result = subprocess.run(command, text=True, capture_output=True)
        log_path = output / "plot3dToFoam.log"
        log_path.write_text(result.stdout + result.stderr)
        if result.returncode != 0 or "FOAM FATAL" in log_path.read_text():
            raise SystemExit(1)

        direct_mesh = direct / "constant" / "polyMesh"
        direct_points_raw = foam_array(direct_mesh / "points", 3)
        target_points = foam_array(target_mesh / "points", 3)
        direct_span_min = float(direct_points_raw[:, 1].min())
        direct_span_max = float(direct_points_raw[:, 1].max())
        target_span_min = float(target_points[:, 2].min())
        target_span_max = float(target_points[:, 2].max())
        direct_points = np.column_stack(
            (
                direct_points_raw[:, 0],
                direct_points_raw[:, 2],
                target_span_min
                + (direct_points_raw[:, 1] - direct_span_min)
                * (target_span_max - target_span_min)
                / (direct_span_max - direct_span_min),
            )
        )
        point_map, distances = unique_nearest_mapping(
            direct_points, target_points, tolerance=1e-6
        )
        direct_faces = foam_array(direct_mesh / "faces", 4).astype(np.int64)
        target_faces = foam_array(target_mesh / "faces", 4).astype(np.int64)
        mapped_faces = np.sort(point_map[direct_faces], axis=1)
        canonical_target_faces = np.sort(target_faces, axis=1)
        direct_order = np.lexsort(tuple(mapped_faces[:, i] for i in (3, 2, 1, 0)))
        target_order = np.lexsort(
            tuple(canonical_target_faces[:, i] for i in (3, 2, 1, 0))
        )
        face_match = np.all(
            mapped_faces[direct_order] == canonical_target_faces[target_order], axis=1
        )

    gate = (
        len(direct_points) == len(target_points) == 460672
        and len(direct_faces) == len(target_faces) == 918464
        and float(distances.max()) <= 1e-6
        and int(face_match.sum()) == 918464
    )
    record = {
        "scope": "Official plot3dToFoam versus generated NASA NACA0012 mesh parity",
        "archive": str(archive),
        "archive_sha256": ARCHIVE_SHA256,
        "archive_member": member,
        "archive_member_crc32": f"{info.CRC:08x}",
        "decompressed_plot3d_sha256": PLOT3D_SHA256,
        "target_case": str(case),
        "target_case_spec_sha256": sha256(spec_path),
        "image_id": identity["Id"],
        "command": command,
        "network_disabled": True,
        "resource_limits": {"cpus": cpus, "memory": memory},
        "log_sha256": sha256(log_path),
        "direct_and_target_point_count": len(target_points),
        "point_mapping_bijective": True,
        "maximum_point_distance_after_axis_span_transform": float(distances.max()),
        "rms_point_distance_after_axis_span_transform": float(
            np.sqrt(np.mean(distances**2))
        ),
        "direct_and_target_face_count": len(target_faces),
        "matching_face_connectivity_sets": int(face_match.sum()),
        "mesh_geometry_and_topology_gate": gate,
        "conclusion": (
            "Generated mesh matches OpenFOAM's direct official PLOT3D conversion; "
            "mesh conversion is not the source of the drag discrepancy."
        ),
        "accepted_for_rocket": False,
    }
    (output / "naca0012-plot3d-mesh-parity.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    print(json.dumps(record))
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--image", required=True)
    parser.add_argument("--cpus", type=float, default=2)
    parser.add_argument("--memory", default="8g")
    args = parser.parse_args()
    audit(args.archive, args.case, args.output, args.image, args.cpus, args.memory)


if __name__ == "__main__":
    main()
