"""Generate a rhoSimpleFoam case from an official NASA TMR NACA 0012 C-grid."""

import argparse
import gzip
import hashlib
import json
import math
import shutil
import zipfile
from pathlib import Path

import numpy as np

from cfd_flat_plate_case import field, foam_header, parse_plot3d


ARCHIVE_SHA256 = "b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4"
GRID_MEMBERS = {
    113: "n0012_113-33.p2dfmt",
    225: "n0012_225-65.p2dfmt",
    449: "n0012_449-129.p2dfmt.gz",
    897: "n0012_897-257.p2dfmt.gz",
    1793: "n0012_1793-513.p2dfmt.gz",
}

CONTINUATION_FIELDS = ("U", "p", "T", "k", "omega", "nut", "alphat")
TMR_K_OVER_A2 = 9.0e-9
TMR_OMEGA_MU_OVER_RHO_A2 = 1.0e-6


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def continuation_source(
    parent: Path,
    *,
    grid_dimensions: list[int],
    angle_deg: float,
    convection: str,
) -> tuple[Path, dict]:
    """Validate and describe an immutable same-case restart source."""
    parent = parent.resolve(strict=True)
    spec = json.loads((parent / "benchmark-spec.json").read_text())
    execution = json.loads((parent / "execution.json").read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Continuation parent must have a fully passed execution record")
    expected = {
        "benchmark": "TMR 2D NACA 0012",
        "grid_dimensions": grid_dimensions,
        "angle_of_attack_deg": angle_deg,
        "convection_scheme": convection,
        "solver": "rhoSimpleFoam",
        "runtime_library": "libTmrSSTmCompressible.so",
        "transport_model": "sutherland",
        "turbulent_prandtl": 0.9,
    }
    actual = {
        "benchmark": spec.get("benchmark"),
        "grid_dimensions": spec.get("grid_dimensions"),
        "angle_of_attack_deg": spec.get("conditions", {}).get(
            "angle_of_attack_deg"
        ),
        "convection_scheme": spec.get("convection_scheme"),
        "solver": spec.get("model_mapping", {}).get("solver"),
        "runtime_library": spec.get("model_mapping", {}).get("runtime_library"),
        "transport_model": spec.get("conditions", {}).get("transport_model"),
        "turbulent_prandtl": spec.get("conditions", {}).get("turbulent_prandtl"),
    }
    if actual != expected:
        raise ValueError(
            "Continuation parent is not configuration-compatible: "
            f"expected {expected}, got {actual}"
        )
    numeric_times = []
    for candidate in parent.iterdir():
        if not candidate.is_dir():
            continue
        try:
            value = float(candidate.name)
        except ValueError:
            continue
        if value > 0:
            numeric_times.append((value, candidate))
    if not numeric_times:
        raise ValueError("Continuation parent has no positive numeric solution time")
    final_time, final_dir = max(numeric_times, key=lambda item: item[0])
    fields = {}
    for name in CONTINUATION_FIELDS:
        source = final_dir / name
        if not source.is_file() or source.is_symlink():
            raise ValueError(f"Missing regular continuation field {source}")
        fields[name] = {
            "source": str(source),
            "sha256": _file_sha256(source),
        }
    return final_dir, {
        "parent_case": str(parent),
        "parent_final_time": final_time,
        "fields": fields,
    }


def archive_grid(archive: Path, ni: int) -> tuple[np.ndarray, np.ndarray, dict]:
    archive_payload = archive.read_bytes()
    digest = hashlib.sha256(archive_payload).hexdigest()
    if digest != ARCHIVE_SHA256:
        raise ValueError(f"NACA grid archive SHA-256 mismatch: {digest}")
    suffix = GRID_MEMBERS[ni]
    with zipfile.ZipFile(archive) as bundle:
        matches = [name for name in bundle.namelist() if name.endswith(suffix)]
        if len(matches) != 1:
            raise ValueError(f"Expected one archive member ending in {suffix!r}")
        member = matches[0]
        stored = bundle.read(member)
        payload = gzip.decompress(stored) if member.endswith(".gz") else stored
        info = bundle.getinfo(member)
    x, y = parse_plot3d(payload)
    if x.shape[1] != ni:
        raise ValueError(f"Expected grid width {ni}, got {x.shape}")
    return x, y, {
        "archive_sha256": digest,
        "archive_member": member,
        "member_crc32": f"{info.CRC:08x}",
        "coordinate_payload_sha256": hashlib.sha256(payload).hexdigest(),
    }


def _point_segment_distance(point: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    delta = b - a
    fraction = float(np.dot(point - a, delta) / np.dot(delta, delta))
    closest = a + np.clip(fraction, 0.0, 1.0) * delta
    return float(np.linalg.norm(point - closest))


def mesh_lists(x: np.ndarray, y: np.ndarray, span: float = 0.01):
    nj, ni = x.shape
    if ni < 5 or nj < 3:
        raise ValueError("Unexpected NACA C-grid dimensions")
    if (ni - 1) % 14:
        raise ValueError("NACA C-grid width does not have the 3:8:3 neutral-map split")
    wake_edges = 3 * (ni - 1) // 14
    wall_start = wake_edges
    wall_end = ni - 1 - wake_edges

    canonical: dict[tuple[int, int, int], int] = {}
    points: list[tuple[float, float, float]] = []

    def canonical_i(j: int, i: int) -> int:
        if j == 0 and i >= wall_end:
            return ni - 1 - i
        return i

    def point_id(j: int, i: int, side: int) -> int:
        ci = canonical_i(j, i)
        key = (j, ci, side)
        if key not in canonical:
            canonical[key] = len(points)
            points.append((float(x[j, ci]), float(y[j, ci]), (-0.5, 0.5)[side] * span))
        return canonical[key]

    face_map: dict[tuple[int, ...], dict] = {}
    n_cells = (ni - 1) * (nj - 1)

    def add_face(face: tuple[int, ...], owner: int, patch: str | None) -> None:
        key = tuple(sorted(face))
        if key in face_map:
            record = face_map[key]
            if record["neighbour"] is not None:
                raise ValueError("Non-manifold face in merged C-grid")
            record["neighbour"] = owner
            record["patch"] = None
        else:
            face_map[key] = {
                "vertices": face,
                "owner": owner,
                "neighbour": None,
                "patch": patch,
            }

    for j in range(nj - 1):
        for i in range(ni - 1):
            cell = j * (ni - 1) + i
            p00 = point_id(j, i, 0)
            p10 = point_id(j, i + 1, 0)
            p11 = point_id(j + 1, i + 1, 0)
            p01 = point_id(j + 1, i, 0)
            q00 = point_id(j, i, 1)
            q10 = point_id(j, i + 1, 1)
            q11 = point_id(j + 1, i + 1, 1)
            q01 = point_id(j + 1, i, 1)
            add_face((p00, p01, p11, p10), cell, "front")
            add_face((q00, q10, q11, q01), cell, "back")
            add_face((p00, q00, q01, p01), cell, "farfield" if i == 0 else None)
            add_face((p10, p11, q11, q10), cell, "farfield" if i == ni - 2 else None)
            lower_patch = "airfoil" if j == 0 and wall_start <= i < wall_end else "wake"
            add_face((p00, p10, q10, q00), cell, lower_patch if j == 0 else None)
            add_face((p01, q01, q11, p11), cell, "farfield" if j == nj - 2 else None)

    internal = [record for record in face_map.values() if record["neighbour"] is not None]
    boundaries: dict[str, list[dict]] = {"airfoil": [], "farfield": [], "front": [], "back": []}
    for record in face_map.values():
        if record["neighbour"] is None:
            patch = record["patch"]
            if patch not in boundaries:
                raise ValueError(f"Unpaired C-grid boundary face tagged {patch!r}")
            boundaries[patch].append(record)
    if len(boundaries["airfoil"]) != ni - 1 - 2 * wake_edges:
        raise ValueError("Airfoil patch does not match the neutral-map index range")

    wall_distances = []
    for i in range(wall_start, wall_end):
        surface_a = np.array((x[0, i], y[0, i]))
        surface_b = np.array((x[0, i + 1], y[0, i + 1]))
        center = np.array(
            (
                np.mean([x[0, i], x[0, i + 1], x[1, i + 1], x[1, i]]),
                np.mean([y[0, i], y[0, i + 1], y[1, i + 1], y[1, i]]),
            )
        )
        wall_distances.append(_point_segment_distance(center, surface_a, surface_b))

    return points, internal, boundaries, np.asarray(wall_distances), n_cells


def write_mesh(folder: Path, x: np.ndarray, y: np.ndarray) -> dict:
    points, internal, patches, wall_distances, n_cells = mesh_lists(x, y)
    poly = folder / "constant" / "polyMesh"
    poly.mkdir(parents=True, exist_ok=True)
    point_text = "\n".join(f"({px:.15g} {py:.15g} {pz:.15g})" for px, py, pz in points)
    (poly / "points").write_text(
        foam_header("vectorField", "constant/polyMesh", "points")
        + f"{len(points)}\n(\n{point_text}\n)\n"
    )
    ordered = internal + [face for name in patches for face in patches[name]]
    face_text = "\n".join(
        f"4({' '.join(str(value) for value in face['vertices'])})" for face in ordered
    )
    (poly / "faces").write_text(
        foam_header("faceList", "constant/polyMesh", "faces")
        + f"{len(ordered)}\n(\n{face_text}\n)\n"
    )
    owners = "\n".join(str(face["owner"]) for face in ordered)
    neighbours = "\n".join(str(face["neighbour"]) for face in internal)
    (poly / "owner").write_text(
        foam_header("labelList", "constant/polyMesh", "owner")
        + f"{len(ordered)}\n(\n{owners}\n)\n"
    )
    (poly / "neighbour").write_text(
        foam_header("labelList", "constant/polyMesh", "neighbour")
        + f"{len(internal)}\n(\n{neighbours}\n)\n"
    )
    start = len(internal)
    entries = []
    for name, faces in patches.items():
        patch_type = "wall" if name == "airfoil" else ("empty" if name in {"front", "back"} else "patch")
        entries.append(
            f"{name}\n{{\n type {patch_type};\n nFaces {len(faces)};\n startFace {start};\n}}"
        )
        start += len(faces)
    (poly / "boundary").write_text(
        foam_header("polyBoundaryMesh", "constant/polyMesh", "boundary")
        + f"{len(entries)}\n(\n{'\n'.join(entries)}\n)\n"
    )
    return {
        "points": len(points),
        "cells": n_cells,
        "faces": len(ordered),
        "internal_faces": len(internal),
        "airfoil_faces": len(patches["airfoil"]),
        "minimum_wall_distance_m": float(wall_distances.min()),
        "maximum_wall_distance_m": float(wall_distances.max()),
        "wall_distances_m": wall_distances,
    }


def _field_body(boundaries: dict[str, str]) -> str:
    return "boundaryField\n{\n" + "\n".join(
        f"{name}\n{{\n{body}\n}}" for name, body in boundaries.items()
    ) + "\n}\n"


def generate(
    archive: Path,
    output: Path,
    ni: int,
    angle_deg: float,
    iterations: int,
    convection: str = "first-order-upwind",
    initialize_from: Path | None = None,
    relaxation_scale: float = 1.0,
    turbulence_model: str = "tmr-sstm",
    outer_row_index: int | None = None,
) -> None:
    if not 0.0 < relaxation_scale <= 1.0:
        raise ValueError("relaxation_scale must be greater than zero and at most one")
    if output.exists():
        raise FileExistsError(output)
    if turbulence_model == "tmr-sstm":
        ras_model = "TmrSSTm"
        model_coefficients = (
            " gamma1 0.5531666666666668;\n"
            " gamma2 0.4403546666666667;\n"
            " c1 20;\n"
        )
        runtime_library = "libTmrSSTmCompressible.so"
        model_variant = "tmr-sstm-v2512-source-map"
    elif turbulence_model == "komega-sst":
        ras_model = "kOmegaSST"
        model_coefficients = ""
        runtime_library = None
        model_variant = "openfoam-v2512-komegaSST-default-coefficients"
    else:
        raise ValueError(f"Unsupported turbulence model {turbulence_model!r}")
    x, y, source = archive_grid(archive, ni)
    original_grid_dimensions = list(x.shape[::-1])
    if outer_row_index is not None:
        if not 2 <= outer_row_index < x.shape[0] - 1:
            raise ValueError("outer_row_index must retain inner rows and remove outer rows")
        x = x[: outer_row_index + 1].copy()
        y = y[: outer_row_index + 1].copy()
    domain = {
        "source_grid_dimensions": original_grid_dimensions,
        "retained_outer_row_index": (
            outer_row_index if outer_row_index is not None else x.shape[0] - 1
        ),
        "upstream_extent_chords": float(-x[-1].min()),
        "downstream_extent_chords": float(x[-1].max() - 1.0),
        "crossflow_extent_chords": float(abs(y[-1]).max()),
        "uses_official_outer_boundary": outer_row_index is None,
    }
    continuation = None
    continuation_dir = None
    if initialize_from is not None:
        continuation_dir, continuation = continuation_source(
            initialize_from,
            grid_dimensions=list(x.shape[::-1]),
            angle_deg=angle_deg,
            convection=convection,
        )
    output.mkdir(parents=True)
    mesh = write_mesh(output, x, y)

    gamma = 1.4
    mol_weight = 28.97
    gas_constant = 8314.462618 / mol_weight
    temperature = 300.0
    pressure = 101325.0
    cp = 1004.5
    speed_of_sound = math.sqrt(gamma * gas_constant * temperature)
    mach = 0.15
    speed = mach * speed_of_sound
    rho_inf = pressure / (gas_constant * temperature)
    dynamic_viscosity = rho_inf * speed / 6_000_000.0
    sutherland_temperature = 110.4
    sutherland_as = (
        dynamic_viscosity
        * (1.0 + sutherland_temperature / temperature)
        / math.sqrt(temperature)
    )
    cv = cp - gas_constant
    sutherland_effective_prandtl = cp / (
        cv * (1.32 + 1.77 * gas_constant / cv)
    )
    nu_inf = dynamic_viscosity / rho_inf
    angle = math.radians(angle_deg)
    velocity = (speed * math.cos(angle), speed * math.sin(angle), 0.0)
    acoustic_speed = speed / mach
    k_inf = TMR_K_OVER_A2 * acoustic_speed**2
    omega_inf = TMR_OMEGA_MU_OVER_RHO_A2 * acoustic_speed**2 / nu_inf
    intensity = math.sqrt((2.0 / 3.0) * k_inf) / speed
    nut_ratio = k_inf / (omega_inf * nu_inf)
    omega_wall = 10.0 * 6.0 * nu_inf / (0.075 * mesh.pop("wall_distances_m") ** 2)
    wall_omega_values = "\n".join(f"{value:.15g}" for value in omega_wall)

    empty = "type empty;"
    far_u = (
        "type freestreamVelocity;\n"
        f"freestreamValue uniform ({velocity[0]:.15g} {velocity[1]:.15g} 0);\n"
        f"value uniform ({velocity[0]:.15g} {velocity[1]:.15g} 0);"
    )
    scalar_outlet = lambda value: (
        f"type inletOutlet;\ninletValue uniform {value:.15g};\nvalue uniform {value:.15g};"
    )
    field(
        output / "0" / "U",
        "[0 1 -1 0 0 0 0]",
        f"({velocity[0]:.15g} {velocity[1]:.15g} 0)",
        {"airfoil": "type noSlip;", "farfield": far_u, "front": empty, "back": empty},
        "volVectorField",
    )
    field(
        output / "0" / "p",
        "[1 -1 -2 0 0 0 0]",
        f"{pressure:.15g}",
        {
            "airfoil": "type zeroGradient;",
            "farfield": f"type freestreamPressure;\nfreestreamValue uniform {pressure:.15g};",
            "front": empty,
            "back": empty,
        },
    )
    for name, dimensions, value, wall in (
        ("T", "[0 0 0 1 0 0 0]", temperature, "type zeroGradient;"),
        ("k", "[0 2 -2 0 0 0 0]", k_inf, "type fixedValue;\nvalue uniform 0;"),
        (
            "omega",
            "[0 0 -1 0 0 0 0]",
            omega_inf,
            "type fixedValue;\nvalue nonuniform List<scalar>\n"
            f"{len(omega_wall)}\n(\n{wall_omega_values}\n);",
        ),
    ):
        field(
            output / "0" / name,
            dimensions,
            f"{value:.15g}",
            {
                "airfoil": wall,
                "farfield": scalar_outlet(value),
                "front": empty,
                "back": empty,
            },
        )
    field(
        output / "0" / "nut",
        "[0 2 -1 0 0 0 0]",
        f"{nut_ratio * nu_inf:.15g}",
        {
            "airfoil": "type fixedValue;\nvalue uniform 0;",
            "farfield": f"type calculated;\nvalue uniform {nut_ratio * nu_inf:.15g};",
            "front": empty,
            "back": empty,
        },
    )
    field(
        output / "0" / "alphat",
        "[1 -1 -1 0 0 0 0]",
        "0",
        {
            "airfoil": "type compressible::alphatWallFunction;\nvalue uniform 0;",
            "farfield": "type calculated;\nvalue uniform 0;",
            "front": empty,
            "back": empty,
        },
    )
    if continuation_dir is not None:
        for name in CONTINUATION_FIELDS:
            shutil.copyfile(continuation_dir / name, output / "0" / name)

    constant = output / "constant"
    system = output / "system"
    system.mkdir()
    (constant / "thermophysicalProperties").write_text(
        foam_header("dictionary", "constant", "thermophysicalProperties")
        + "thermoType\n{\n type hePsiThermo;\n mixture pureMixture;\n transport sutherland;\n"
        " thermo hConst;\n equationOfState perfectGas;\n specie specie;\n"
        " energy sensibleInternalEnergy;\n}\n"
        "mixture\n{\n specie\n{\n"
        f" molWeight {mol_weight:.15g};\n"
        f"}}\n thermodynamics\n{{\n Cp {cp:.15g};\n Hf 0;\n}}\n transport\n{{\n"
        f" As {sutherland_as:.15g};\n Ts {sutherland_temperature:.15g};\n"
        "}\n}\n"
    )
    (constant / "turbulenceProperties").write_text(
        foam_header("dictionary", "constant", "turbulenceProperties")
        + f"simulationType RAS;\nRAS\n{{\n RASModel {ras_model};\n turbulence on;\n"
        + " printCoeffs on;\n"
        + model_coefficients
        + " Prt 0.90;\n}\n"
    )
    (system / "fvOptions").write_text(
        foam_header("dictionary", "system", "fvOptions")
        + "limitT\n{\n type limitTemperature;\n min 250;\n max 350;\n"
        " selectionMode all;\n}\n"
    )
    (system / "controlDict").write_text(
        foam_header("dictionary", "system", "controlDict")
        + "application rhoSimpleFoam;\n"
        + (f'libs ("{runtime_library}");\n' if runtime_library else "libs ();\n")
        + f"startFrom startTime;\nstartTime 0;\nstopAt endTime;\nendTime {iterations};\n"
        "deltaT 1;\nwriteControl timeStep;\nwriteInterval 100;\npurgeWrite 2;\n"
        "writeFormat ascii;\nwritePrecision 10;\nwriteCompression off;\n"
        "timeFormat general;\ntimePrecision 6;\nrunTimeModifiable false;\n"
        "functions\n{\n coefficients\n{\n type forceCoeffs;\n libs (forces);\n"
        " patches (airfoil);\n rho rho;\n"
        f" rhoInf {rho_inf:.15g};\n pRef {pressure:.15g};\n"
        f" liftDir ({-math.sin(angle):.15g} {math.cos(angle):.15g} 0);\n"
        f" dragDir ({math.cos(angle):.15g} {math.sin(angle):.15g} 0);\n"
        " CofR (0.25 0 0);\n"
        f" magUInf {speed:.15g};\n lRef 1;\n Aref 0.01;\n"
        " writeControl timeStep;\n writeInterval 1;\n}\n}\n"
    )
    if convection == "first-order-upwind":
        velocity_divergence = "bounded Gauss upwind"
        energy_divergence = "bounded Gauss upwind"
    elif convection == "limited-linear":
        velocity_divergence = "bounded Gauss limitedLinearV 1"
        energy_divergence = "bounded Gauss limitedLinear 1"
    elif convection == "lust-blended":
        velocity_divergence = "bounded Gauss LUST grad(U)"
        energy_divergence = "bounded Gauss LUST default"
    elif convection == "linear-upwind-velocity":
        velocity_divergence = "bounded Gauss linearUpwind grad(U)"
        energy_divergence = "bounded Gauss linearUpwind default"
    else:
        raise ValueError(f"Unsupported convection scheme {convection!r}")
    (system / "fvSchemes").write_text(
        foam_header("dictionary", "system", "fvSchemes")
        + "ddtSchemes { default steadyState; }\n"
        "gradSchemes { default Gauss linear; limited cellLimited Gauss linear 1;"
        " grad(U) $limited; grad(k) $limited; grad(omega) $limited; }\n"
        f"divSchemes {{ default none; div(phi,U) {velocity_divergence};"
        f" energy {energy_divergence};"
        " div(phi,e) $energy; div(phi,K) $energy; div(phi,Ekp) $energy;"
        " turbulence bounded Gauss upwind; div(phi,k) $turbulence;"
        " div(phi,omega) $turbulence; div(phid,p) Gauss upwind;"
        " div((phi|interpolate(rho)),p) bounded Gauss upwind;"
        " div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear; }\n"
        "laplacianSchemes { default Gauss linear corrected; }\n"
        "interpolationSchemes { default linear; }\n"
        "snGradSchemes { default corrected; }\nwallDist { method meshWave; }\n"
    )
    (system / "fvSolution").write_text(
        foam_header("dictionary", "system", "fvSolution")
        + 'solvers\n{\n p { solver GAMG; smoother GaussSeidel; tolerance 1e-7; relTol 0.01; }\n'
        ' "(U|k|omega|e)" { solver PBiCGStab; preconditioner DILU; tolerance 1e-7; relTol 0.01; }\n}\n'
        "SIMPLE\n{\n nNonOrthogonalCorrectors 0;\n"
        " pMinFactor 0.1;\n pMaxFactor 2;\n}\n"
        "relaxationFactors\n{\n"
        f" fields {{ p {0.2 * relaxation_scale:.15g};"
        f" rho {0.01 * relaxation_scale:.15g}; }}\n"
        f" equations {{ U {0.1 * relaxation_scale:.15g};"
        f" e {0.1 * relaxation_scale:.15g};"
        f' "(k|omega)" {0.3 * relaxation_scale:.15g}; }}\n}}\n'
    )
    (system / "decomposeParDict").write_text(
        foam_header("dictionary", "system", "decomposeParDict")
        + "numberOfSubdomains 12;\nmethod scotch;\n"
    )

    manifest = {
        "benchmark": "TMR 2D NACA 0012",
        "scope": "external_body_force_pressure_and_moment_workflow",
        "grid_dimensions": list(x.shape[::-1]),
        "mesh": mesh,
        "source": source,
        "domain": domain,
        "geometry": "TMR altered closed NACA 0012 validation grid",
        "conditions": {
            "mach": mach,
            "reynolds_number_chord": 6_000_000,
            "angle_of_attack_deg": angle_deg,
            "chord_m": 1.0,
            "temperature_k": temperature,
            "pressure_pa": pressure,
            "speed_m_s": speed,
            "density_kg_m3": rho_inf,
            "dynamic_viscosity_pa_s": dynamic_viscosity,
            "transport_model": "sutherland",
            "sutherland_as": sutherland_as,
            "sutherland_temperature_k": sutherland_temperature,
            "sutherland_effective_prandtl": sutherland_effective_prandtl,
            "turbulent_prandtl": 0.9,
            "turbulence_intensity": intensity,
            "freestream_nut_over_nu": nut_ratio,
            "freestream_k_over_acoustic_speed_squared": TMR_K_OVER_A2,
            "freestream_omega_mu_over_rho_acoustic_speed_squared": TMR_OMEGA_MU_OVER_RHO_A2,
            "k_m2_s2": k_inf,
            "omega_s-1": omega_inf,
        },
        "model_mapping": {
            "variant": model_variant,
            "solver": "rhoSimpleFoam",
            "runtime_library": runtime_library,
            "image_id": "sha256:143e0e81aa690349714910f096ef1a2dc5fbc723a27355f5078839503a9b7634",
        },
        "wall_treatment": {
            "k": "fixedValue zero",
            "omega": "TMR factor-10 fixedValue per wall face",
            "nut": "fixedValue zero",
        },
        "convection_scheme": convection,
        "force_coefficient_convention": {
            "drag_axis": "freestream direction",
            "lift_axis": "in-plane direction normal to freestream",
            "openfoam_pitch_axis": "liftDir cross dragDir = negative z",
            "nose_up_cm": "OpenFOAM CmPitch; nose is toward negative x from quarter chord",
            "moment_reference": [0.25, 0.0, 0.0],
        },
        "solver_controls": {
            "relaxation_scale": relaxation_scale,
            "purpose": "steady-state convergence control only",
        },
        "initialization": (
            continuation
            if continuation is not None
            else {"method": "uniform_freestream_and_generated_wall_values"}
        ),
        "accepted_for_rocket": False,
    }
    (output / "benchmark-spec.json").write_text(json.dumps(manifest, indent=2) + "\n")
    np.savez(output / "tmr-naca0012-grid.npz", x=x, y=y)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grid-archive", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--grid-ni", type=int, choices=sorted(GRID_MEMBERS), default=113)
    parser.add_argument("--angle-deg", type=float, choices=(0.0, 10.0), required=True)
    parser.add_argument("--iterations", type=int, default=5000)
    parser.add_argument(
        "--convection",
        choices=(
            "first-order-upwind",
            "limited-linear",
            "lust-blended",
            "linear-upwind-velocity",
        ),
        default="first-order-upwind",
    )
    parser.add_argument(
        "--initialize-from",
        type=Path,
        help="Copy latest compatible solution fields from an immutable parent case",
    )
    parser.add_argument(
        "--relaxation-scale",
        type=float,
        default=1.0,
        help="Scale all default under-relaxation factors, in (0, 1]",
    )
    parser.add_argument(
        "--turbulence-model",
        choices=("tmr-sstm", "komega-sst"),
        default="tmr-sstm",
    )
    parser.add_argument(
        "--outer-row-index",
        type=int,
        help="Retain official structured rows 0 through this row for a domain study",
    )
    args = parser.parse_args()
    generate(
        args.grid_archive,
        args.output,
        args.grid_ni,
        args.angle_deg,
        args.iterations,
        args.convection,
        args.initialize_from,
        args.relaxation_scale,
        args.turbulence_model,
        args.outer_row_index,
    )


if __name__ == "__main__":
    main()
