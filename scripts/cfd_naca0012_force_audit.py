"""Audit NACA 0012 force history, conditions, symmetry, and settling fail-closed."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np

from cfd_naca0012_ladson_reference import OUTPUT_NAME, PDF_SHA256


IMAGE_ID = "sha256:143e0e81aa690349714910f096ef1a2dc5fbc723a27355f5078839503a9b7634"
SUTHERLAND_PR_IMAGE_ID = "sha256:2870176815d77d1b6e252003db8f7598f2bb25e891c7ea97ec459e469b54d020"
SSTM_K_ONLY_LIMITER_IMAGE_ID = "sha256:777e5ff0348eab1026f69bfe7fd2a01685d250a6a186a674a9bdc0e83ff7ef8b"
SSTM_EXACT_PRODUCTION_IMAGE_ID = "sha256:ae3235d75b54311a6dbcdfc2b45f6c9be77a8ff0743c099cf5ca3f3e9db0d23f"
CFL3D_FORCE_SHA256 = "373dc142018816628b7b53ad278327db731162988ba35a166cd9fdc131a7fd7a"


def mapped_initialization_gate(case: Path, spec: dict) -> bool:
    initialization = spec.get("initialization", {})
    method = initialization.get("method")
    if method in {
        "same-grid higher-to-first-order scheme-sensitivity restart",
        "same-grid scheme-sensitivity restart",
        "same-grid tmr-sstm-to-stock-komega-sst sensitivity restart",
        "same-grid polynomial-Sutherland constant-Prandtl sensitivity restart",
            "same-grid exact-Sutherland constant-Prandtl sensitivity restart",
            "same-grid SSTm k-only production-limiter sensitivity restart",
            "same-grid SSTm exact-production sensitivity restart",
            "same-grid SSTm exact-production residual convergence continuation",
            "449x129 exact-transport exact-SSTm numerical-refresh restart",
            "same-grid exact-SSTm LUST numerical-refresh restart",
            "same-grid exact-SSTm exact-wall-distance sensitivity restart",
            "structured retained-row full-to-reduced-domain restart",
    }:
        try:
            if method == "same-grid tmr-sstm-to-stock-komega-sst sensitivity restart":
                record_name = "model-restart-execution.json"
            elif method == "same-grid polynomial-Sutherland constant-Prandtl sensitivity restart":
                record_name = "transport-restart-execution.json"
            elif method == "same-grid exact-Sutherland constant-Prandtl sensitivity restart":
                record_name = "sutherland-pr-restart-execution.json"
            elif method == "same-grid SSTm k-only production-limiter sensitivity restart":
                record_name = "sstm-limiter-restart-execution.json"
            elif method == "same-grid SSTm exact-production sensitivity restart":
                record_name = "sstm-exact-production-restart-execution.json"
            elif method == (
                "same-grid SSTm exact-production residual convergence continuation"
            ):
                record_name = "sstm-exact-production-continuation-execution.json"
            elif method == "449x129 exact-transport exact-SSTm numerical-refresh restart":
                record_name = "exact-sstm-medium-restart-execution.json"
            elif method == "same-grid exact-SSTm LUST numerical-refresh restart":
                record_name = "exact-sstm-lust-restart-execution.json"
            elif method == (
                "same-grid exact-SSTm exact-wall-distance sensitivity restart"
            ):
                record_name = "exact-wall-distance-restart-execution.json"
            elif method == "structured retained-row full-to-reduced-domain restart":
                record_name = "domain-restart-execution.json"
            else:
                record_name = "scheme-restart-execution.json"
            record = json.loads((case / record_name).read_text())
            snapshot = Path(initialization["implementation_snapshot"])
            implementation_digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
            audit_path = Path(initialization["source_audit"])
            audit_digest = hashlib.sha256(audit_path.read_bytes()).hexdigest()
            source_audit = json.loads(audit_path.read_text())
            fields_match = all(
                hashlib.sha256((case / "0" / name).read_bytes()).hexdigest()
                == metadata["restart_sha256"]
                for name, metadata in initialization["fields"].items()
            )
            return (
                record.get("stage_passed") is True
                and record.get("implementation_sha256") == implementation_digest
                and initialization.get("implementation_sha256") == implementation_digest
                and initialization.get("source_audit_sha256") == audit_digest
                and source_audit.get("coarse_preflight_passed") is True
                and fields_match
            )
        except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
            return False
    if method != "structured bilinear logical-coordinate prolongation":
        return True
    try:
        record = json.loads((case / "map-fields-execution.json").read_text())
        implementation = Path(__file__).with_name("cfd_naca0012_map_fields.py")
        implementation_digest = hashlib.sha256(implementation.read_bytes()).hexdigest()
        audit_path = Path(initialization["source_audit"])
        audit_digest = hashlib.sha256(audit_path.read_bytes()).hexdigest()
        source_audit = json.loads(audit_path.read_text())
        fields_match = all(
            hashlib.sha256((case / "0" / name).read_bytes()).hexdigest()
            == metadata["mapped_sha256"]
            for name, metadata in initialization["fields"].items()
        )
        return (
            record.get("stage_passed") is True
            and record.get("implementation_sha256") == implementation_digest
            and initialization.get("implementation_sha256") == implementation_digest
            and initialization.get("source_audit_sha256") == audit_digest
            and source_audit.get("coarse_preflight_passed") is True
            and fields_match
        )
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return False


def coefficient_files(case: Path) -> list[Path]:
    files = sorted((case / "postProcessing" / "coefficients").glob("*/coefficient.dat"))
    if not files:
        files = sorted(
            (case / "postProcessing" / "coefficients").glob("*/forceCoeffs.dat")
        )
    return files


def coefficient_history(case: Path) -> tuple[list[str], np.ndarray]:
    files = coefficient_files(case)
    if len(files) != 1:
        raise ValueError(f"Expected one force coefficient history, got {len(files)}")
    header = next(
        line for line in files[0].read_text().splitlines() if line.startswith("# Time ")
    )
    columns = header.removeprefix("# ").split()
    columns = ["CmPitch" if column == "Cm" else column for column in columns]
    values = np.loadtxt(files[0])
    if values.ndim == 1:
        values = values[None, :]
    if values.shape[1] != len(columns):
        raise ValueError("Force coefficient columns do not match header")
    return columns, values


def coefficient_header_vector(case: Path, label: str) -> list[float]:
    files = coefficient_files(case)
    if len(files) != 1:
        raise ValueError(f"Expected one force coefficient file, found {len(files)}")
    pattern = re.compile(rf"^#\s*{re.escape(label)}\s*:\s*\(([^)]+)\)")
    for line in files[0].read_text().splitlines():
        match = pattern.match(line)
        if match:
            values = [float(value) for value in match.group(1).split()]
            if len(values) == 3:
                return values
            break
    raise ValueError(f"Missing three-component {label} header")


def experimental_points(path: Path, angle: float) -> dict:
    rows = []
    for line in path.read_text().splitlines():
        values = line.split()
        if len(values) != 3:
            continue
        try:
            alpha, cl, cd = map(float, values)
        except ValueError:
            continue
        if abs(alpha - angle) <= 0.2:
            rows.append((alpha, cl, cd))
    if len(rows) < 2:
        raise ValueError(f"Insufficient Ladson repeat points near {angle} degrees")
    data = np.asarray(rows)
    return {
        "points": data.tolist(),
        "angle_window_deg": 0.2,
        "mean_angle_deg": float(data[:, 0].mean()),
        "mean_cl": float(data[:, 1].mean()),
        "mean_cd": float(data[:, 2].mean()),
        "cl_range": float(np.ptp(data[:, 1])),
        "cd_range": float(np.ptp(data[:, 2])),
    }


def cfl3d_reference(path: Path, angle: float) -> dict:
    if hashlib.sha256(path.read_bytes()).hexdigest() != CFL3D_FORCE_SHA256:
        raise ValueError("CFL3D force reference missing or wrong SHA-256")
    rows = []
    for line in path.read_text().splitlines():
        values = line.split()
        if len(values) != 3:
            continue
        try:
            alpha, cl, cd = map(float, values)
        except ValueError:
            continue
        if abs(alpha - angle) <= 0.2:
            rows.append((alpha, cl, cd))
    if len(rows) != 1:
        raise ValueError(f"Expected one CFL3D reference point near {angle} degrees")
    alpha, cl, cd = rows[0]
    return {"angle_deg": alpha, "cl": cl, "cd": cd}


def experimental_moment(path: Path, angle: float) -> dict:
    reference = json.loads(path.read_text())
    source_pdf = path.parent / "nasa-tm-4074.pdf"
    if hashlib.sha256(source_pdf.read_bytes()).hexdigest() != PDF_SHA256:
        raise ValueError("NASA TM-4074 PDF is missing or has the wrong SHA-256")
    rows = [
        row for row in reference["rows"] if abs(row["alpha_deg"] - angle) <= 0.2
    ]
    if len(rows) < 2:
        raise ValueError(f"Insufficient Ladson moment points near {angle} degrees")
    values = np.asarray([row["cm_quarter_chord_nose_up"] for row in rows])
    return {
        "points": rows,
        "angle_window_deg": 0.2,
        "mean_cm_quarter_chord_nose_up": float(values.mean()),
        "cm_range": float(np.ptp(values)),
        "source_pdf_sha256": PDF_SHA256,
    }


def long_window_trend(
    values: np.ndarray,
    indices: dict[str, int],
    angle_deg: float,
    window: int,
) -> tuple[dict[str, float], dict[str, float], bool]:
    """Project force drift over a long window against repeatability limits."""
    if len(values) < window:
        raise ValueError(f"Need at least {window} force samples")
    trend = values[-window:]
    trend_x = trend[:, indices["Time"]]
    projected = {
        name: abs(float(np.polyfit(trend_x, trend[:, indices[name]], 1)[0]) * window)
        for name in ("Cd", "Cl", "CmPitch")
    }
    alpha = np.radians(angle_deg)
    limits = {
        "Cd": 0.0002,
        "Cl": 0.004 * abs(float(np.cos(alpha)))
        + 0.0002 * abs(float(np.sin(alpha))),
        "CmPitch": 0.0002,
    }
    return projected, limits, all(projected[name] <= limits[name] for name in projected)


def solver_residual_gate(
    log: str, window: int = 100
) -> tuple[dict[str, float], dict[str, float], bool]:
    fields = ("p", "Ux", "Uy", "e", "omega", "k")
    histories = {name: [] for name in fields}
    pattern = re.compile(
        r"Solving (?:for )?(p|Ux|Uy|e|omega|k), Initial residual = "
        r"([0-9.eE+-]+)"
    )
    for name, value in pattern.findall(log):
        histories[name].append(float(value))
    missing = [name for name, values in histories.items() if len(values) < window]
    if missing:
        raise ValueError(f"Need at least {window} residual samples for {missing}")
    final = {name: values[-1] for name, values in histories.items()}
    recent_max = {name: max(values[-window:]) for name, values in histories.items()}
    gate = all(value <= 1e-5 for value in final.values()) and all(
        value <= 1e-4 for value in recent_max.values()
    )
    return final, recent_max, gate


def audit(
    case: Path, benchmark_data: Path, window: int = 100, trend_window: int = 500
) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    execution = json.loads((case / "execution.json").read_text())
    image = json.loads((case / "image.json").read_text())
    if spec.get("benchmark") != "TMR 2D NACA 0012":
        raise ValueError("Not a generated TMR NACA 0012 case")
    conditions = spec["conditions"]
    condition_gate = (
        conditions["mach"] == 0.15
        and conditions["reynolds_number_chord"] == 6_000_000
        and conditions["angle_of_attack_deg"] in {0.0, 10.0}
        and conditions.get("transport_model")
        in {"sutherland", "polynomial-sutherland-pr072", "exact-sutherland-pr072"}
        and conditions.get("turbulent_prandtl") == 0.9
        and conditions.get("freestream_k_over_acoustic_speed_squared") == 9e-9
        and conditions.get("freestream_omega_mu_over_rho_acoustic_speed_squared")
        == 1e-6
    )
    model_variant = spec["model_mapping"].get("variant")
    expected_runtime_library = {
        "tmr-sstm-v2512-source-map": "libTmrSSTmCompressible.so",
        "tmr-sstm-k-only-production-limiter": "libTmrSSTmKOnlyLimiterCompressible.so",
        "tmr-sstm-exact-production": "libTmrSSTmExactProductionCompressible.so",
        "tmr-sstm-exact-production-exact-wall-distance": (
            "libTmrSSTmExactProductionCompressible.so"
        ),
        "openfoam-v2512-komegaSST-default-coefficients": None,
    }.get(model_variant, object())
    expected_image_id = spec["model_mapping"].get("image_id", IMAGE_ID)
    runtime_gate = (
        expected_image_id
        in {
            IMAGE_ID,
            SUTHERLAND_PR_IMAGE_ID,
            SSTM_K_ONLY_LIMITER_IMAGE_ID,
            SSTM_EXACT_PRODUCTION_IMAGE_ID,
        }
        and image.get("Id") == expected_image_id
        and spec["model_mapping"]["solver"] == "rhoSimpleFoam"
        and spec["model_mapping"].get("runtime_library")
        == expected_runtime_library
        and all(stage["stage_passed"] for stage in execution)
        and any("rhoSimpleFoam" in stage["stage"] for stage in execution)
    )
    initialization_gate = mapped_initialization_gate(case, spec)
    solver_stages = [
        (index, stage)
        for index, stage in enumerate(execution)
        if "rhoSimpleFoam" in stage["stage"]
    ]
    if len(solver_stages) != 1:
        raise ValueError("Expected one recorded rhoSimpleFoam stage")
    index, solver_stage = solver_stages[0]
    log_path = case / f"{index}-{solver_stage['stage'].split()[0]}.log"
    log = log_path.read_text()
    openfoam_transport = conditions.get(
        "openfoam_transport_model", conditions.get("transport_model")
    )
    if model_variant == "tmr-sstm-v2512-source-map":
        model_patterns = (
            r"Selecting RAS turbulence model TmrSSTm",
            r"gamma1\s+0\.553166",
            r"gamma2\s+0\.44035",
            r"c1\s+20;",
            r"Prt\s+0\.9;",
            rf"transport\s+{re.escape(openfoam_transport)};",
        )
    elif model_variant == "tmr-sstm-k-only-production-limiter":
        model_patterns = (
            r"Selecting RAS turbulence model TmrSSTmKOnlyLimiter",
            r"gamma1\s+0\.553166",
            r"gamma2\s+0\.44035",
            r"c1\s+20;",
            r"Prt\s+0\.9;",
            rf"transport\s+{re.escape(openfoam_transport)};",
        )
    elif model_variant in {
        "tmr-sstm-exact-production",
        "tmr-sstm-exact-production-exact-wall-distance",
    }:
        model_patterns = (
            r"Selecting RAS turbulence model TmrSSTmExactProduction",
            r"gamma1\s+0\.553166",
            r"gamma2\s+0\.44035",
            r"c1\s+20;",
            r"Prt\s+0\.9;",
            rf"transport\s+{re.escape(openfoam_transport)};",
        )
    elif model_variant == "openfoam-v2512-komegaSST-default-coefficients":
        model_patterns = (
            r"Selecting RAS turbulence model kOmegaSST",
            r"Prt\s+0\.9;",
            rf"transport\s+{re.escape(openfoam_transport)};",
        )
    else:
        model_patterns = (r"(?!)",)
    model_gate = all(re.search(pattern, log) for pattern in model_patterns)
    limiter_tail = re.findall(r"LimitedCells=(\d+)", log)
    temperature_limiter_inactive = (
        len(limiter_tail) >= 2 * window
        and all(int(value) == 0 for value in limiter_tail[-2 * window :])
    )

    columns, values = coefficient_history(case)
    pitch_axis = coefficient_header_vector(case, "pitchAxis")
    moment_convention_gate = bool(np.allclose(pitch_axis, [0.0, 0.0, -1.0]))
    indices = {name: columns.index(name) for name in ("Time", "Cd", "Cl", "CmPitch")}
    if len(values) < window:
        raise ValueError(f"Need at least {window} force samples")
    tail = values[-window:]
    means = {
        name: float(tail[:, indices[name]].mean()) for name in ("Cd", "Cl", "CmPitch")
    }
    peak_to_peak = {
        name: float(np.ptp(tail[:, indices[name]])) for name in ("Cd", "Cl", "CmPitch")
    }
    settling_gate = all(value <= 0.01 for value in peak_to_peak.values())
    angle = float(conditions["angle_of_attack_deg"])
    projected_trend, trend_limits, trend_gate = long_window_trend(
        values, indices, angle, trend_window
    )
    final_residuals, recent_max_residuals, residual_gate = solver_residual_gate(log)
    symmetry_gate = (
        abs(means["Cl"]) <= 0.01 and abs(means["CmPitch"]) <= 0.01
        if angle == 0.0
        else None
    )
    experiment = experimental_points(
        benchmark_data / "CLCD_Ladson_expdata.dat", angle
    )
    experiment["cfd_minus_mean_cl"] = means["Cl"] - experiment["mean_cl"]
    experiment["cfd_minus_mean_cd"] = means["Cd"] - experiment["mean_cd"]
    cfl3d_path = benchmark_data / "n0012clcd_cfl3d_sst.dat"
    if cfl3d_path.is_file():
        cfl3d = cfl3d_reference(cfl3d_path, angle)
        cfl3d["openfoam_minus_cfl3d_cl"] = means["Cl"] - cfl3d["cl"]
        cfl3d["openfoam_minus_cfl3d_cd"] = means["Cd"] - cfl3d["cd"]
        cfl3d["comparison_status"] = "diagnostic_pending_numerical_uncertainty"
    else:
        cfl3d = {"comparison_status": "reference_not_present_in_bundle"}
    moment_path = benchmark_data / OUTPUT_NAME
    if moment_path.is_file():
        moment = experimental_moment(moment_path, angle)
        moment["cfd_minus_mean_cm_quarter_chord_nose_up"] = (
            means["CmPitch"] - moment["mean_cm_quarter_chord_nose_up"]
        )
        experiment["quarter_chord_moment"] = moment
    else:
        experiment["quarter_chord_moment"] = {
            "status": "missing_checked_NASA_TM_4074_transcription"
        }
    experiment["comparison_status"] = (
        "diagnostic_pending_grid_scheme_iterative_and_extraction_uncertainty"
    )
    preflight_gate = all(
        (
            condition_gate,
            runtime_gate,
            initialization_gate,
            model_gate,
            temperature_limiter_inactive,
            settling_gate,
            trend_gate,
            residual_gate,
            moment_convention_gate,
            symmetry_gate is not False,
        )
    )
    return {
        "case": str(case),
        "conditions_gate": condition_gate,
        "runtime_and_execution_gate": runtime_gate,
        "mapped_initialization_provenance_gate": initialization_gate,
        "model_configuration_gate": bool(model_gate),
        "sstm_model_configuration_gate": bool(
            model_gate
            and model_variant
            in {
                "tmr-sstm-v2512-source-map",
        "tmr-sstm-k-only-production-limiter",
        "tmr-sstm-exact-production",
        "tmr-sstm-exact-production-exact-wall-distance",
            }
        ),
        "solution_time": float(values[-1, indices["Time"]]),
        "settling_window_samples": window,
        "last_window_mean": means,
        "moment_convention": {
            "openfoam_pitch_axis": pitch_axis,
            "openfoam_cm_pitch_mean": means["CmPitch"],
            "nose_up_cm_mean": means["CmPitch"],
            "conversion": "OpenFOAM CmPitch is already nose-up-positive",
            "gate": moment_convention_gate,
        },
        "last_window_peak_to_peak": peak_to_peak,
        "settling_absolute_limit": 0.01,
        "settling_gate": settling_gate,
        "trend_window_samples": trend_window,
        "projected_change_over_trend_window": projected_trend,
        "trend_absolute_limits_from_experimental_repeatability": trend_limits,
        "long_window_trend_gate": trend_gate,
        "solver_initial_residuals_final": final_residuals,
        "solver_initial_residuals_last_100_max": recent_max_residuals,
        "solver_initial_residual_final_limit": 1e-5,
        "solver_initial_residual_last_100_max_limit": 1e-4,
        "solver_residual_gate": residual_gate,
        "zero_angle_symmetry_gate": symmetry_gate,
        "temperature_limiter_inactive_over_window": temperature_limiter_inactive,
        "ladson_tripped_experiment": experiment,
        "tmr_cfl3d_sst_reference": cfl3d,
        "coarse_preflight_passed": preflight_gate,
        "force_benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--window", type=int, default=100)
    parser.add_argument("--trend-window", type=int, default=500)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.case, args.benchmark_data, args.window, args.trend_window)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-force-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
