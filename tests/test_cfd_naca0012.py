import json
import hashlib
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_naca0012_case import CONTINUATION_FIELDS, generate, mesh_lists
from cfd_naca0012_force_audit import (
    coefficient_header_vector,
    cfl3d_reference,
    experimental_points,
    long_window_trend,
    mapped_initialization_gate,
    solver_residual_gate,
)
from cfd_naca0012_ladson_reference import matched_rows
from cfd_naca0012_map_fields import (
    mapping_compatibility,
    parse_internal_field,
    prolong_cells,
    replace_internal_field,
)
from cfd_naca0012_numerical_study import independence_limits, within_limits
from cfd_naca0012_acceptance import evaluate as evaluate_acceptance
from cfd_naca0012_drag_component_audit import audit as audit_drag_components
from cfd_naca0012_incompressible_audit import residual_gate as incompressible_residual_gate
from cfd_naca0012_pressure_audit import CFL3D_CP_SHA256
from cfd_naca0012_skin_friction_audit import CFL3D_CF_SHA256
from cfd_naca0012_transport_restart import (
    MOLECULAR_PRANDTL,
    transport_coefficients,
)
from cfd_naca0012_transport_sensitivity import drag_decomposition
from cfd_naca0012_yplus_audit import audit as audit_yplus, parse_yplus_log
from cfd_naca0012_yplus_run import latest_time
from cfd_naca0012_transient_case import replace_once
from cfd_naca0012_transient_audit import courant_history, final_interval_statistics


def synthetic_c_grid() -> tuple[np.ndarray, np.ndarray]:
    x = np.zeros((3, 15))
    y = np.zeros((3, 15))
    x[0, :4] = [4, 3, 2, 1]
    angles = np.linspace(0, 2 * np.pi, 9)
    x[0, 3:12] = 0.5 + 0.5 * np.cos(angles)
    y[0, 3:12] = 0.5 * np.sin(angles)
    x[0, 11:] = [1, 2, 3, 4]
    for row, radius in ((1, 0.7), (2, 1.0)):
        x[row, 3:12] = 0.5 + radius * np.cos(angles)
        y[row, 3:12] = radius * np.sin(angles)
        x[row, :4] = [4, 3, 2, 1]
        y[row, :4] = -radius
        x[row, 11:] = [1, 2, 3, 4]
        y[row, 11:] = radius
    return x, y


def test_neutral_map_split_merges_wake_and_keeps_entire_airfoil():
    x, y = synthetic_c_grid()
    _, internal, patches, wall_distances, cells = mesh_lists(x, y)
    assert cells == 28
    assert len(patches["airfoil"]) == 8
    assert len(patches["farfield"]) == 18
    assert len(internal) > 0
    assert np.all(wall_distances > 0)


def test_generator_serializes_compressible_fields_and_scheme(monkeypatch, tmp_path):
    x, y = synthetic_c_grid()
    monkeypatch.setattr(
        "cfd_naca0012_case.archive_grid",
        lambda _archive, _ni: (
            x,
            y,
            {
                "archive_sha256": "pinned",
                "archive_member": "synthetic",
                "member_crc32": "0",
                "coordinate_payload_sha256": "coordinates",
            },
        ),
    )
    output = tmp_path / "case"
    generate(
        tmp_path / "archive.zip",
        output,
        113,
        10.0,
        25,
        "linear-upwind-velocity",
    )
    assert "uniform uniform" not in (output / "0" / "U").read_text()
    assert "bounded Gauss linearUpwind grad(U)" in (
        output / "system" / "fvSchemes"
    ).read_text()
    thermo = (output / "constant" / "thermophysicalProperties").read_text()
    assert thermo.rstrip().endswith("}")
    spec = json.loads((output / "benchmark-spec.json").read_text())
    assert spec["mesh"]["airfoil_faces"] == 8
    assert spec["conditions"]["angle_of_attack_deg"] == 10.0
    assert spec["convection_scheme"] == "linear-upwind-velocity"
    assert spec["conditions"]["freestream_k_over_acoustic_speed_squared"] == 9e-9
    assert (
        spec["conditions"]["freestream_omega_mu_over_rho_acoustic_speed_squared"]
        == 1e-6
    )
    assert spec["conditions"]["freestream_nut_over_nu"] == pytest.approx(0.009)
    assert spec["conditions"]["turbulence_intensity"] == pytest.approx(
        (6e-9) ** 0.5 / 0.15
    )
    assert "OpenFOAM CmPitch" in spec["force_coefficient_convention"]["nose_up_cm"]
    assert spec["solver_controls"]["relaxation_scale"] == 1.0


def test_generator_serializes_lust_blended_scheme(monkeypatch, tmp_path):
    x, y = synthetic_c_grid()
    monkeypatch.setattr(
        "cfd_naca0012_case.archive_grid", lambda _archive, _ni: (x, y, "0")
    )
    output = tmp_path / "case"
    generate(
        tmp_path / "archive.zip",
        output,
        113,
        0.0,
        5,
        "lust-blended",
    )
    schemes = (output / "system" / "fvSchemes").read_text()
    assert "bounded Gauss LUST grad(U)" in schemes
    assert "bounded Gauss LUST default" in schemes
    spec = json.loads((output / "benchmark-spec.json").read_text())
    assert spec["convection_scheme"] == "lust-blended"


def test_yplus_runner_selects_latest_reconstructed_time(tmp_path):
    for name in ("0", "100", "6000"):
        (tmp_path / name).mkdir()
    (tmp_path / "constant").mkdir()
    assert latest_time(tmp_path).name == "6000"


def test_generator_serializes_stock_komega_sst_without_custom_library(
    monkeypatch, tmp_path
):
    x, y = synthetic_c_grid()
    monkeypatch.setattr(
        "cfd_naca0012_case.archive_grid", lambda _archive, _ni: (x, y, "0")
    )
    output = tmp_path / "case"
    generate(
        tmp_path / "archive.zip",
        output,
        113,
        0.0,
        5,
        "linear-upwind-velocity",
        turbulence_model="komega-sst",
    )
    turbulence = (output / "constant" / "turbulenceProperties").read_text()
    control = (output / "system" / "controlDict").read_text()
    assert "RASModel kOmegaSST;" in turbulence
    assert "TmrSSTm" not in turbulence
    assert "libs ();" in control
    spec = json.loads((output / "benchmark-spec.json").read_text())
    assert spec["model_mapping"]["variant"] == (
        "openfoam-v2512-komegaSST-default-coefficients"
    )
    assert spec["model_mapping"]["runtime_library"] is None


def test_generator_retains_exact_structured_rows_for_domain_study(
    monkeypatch, tmp_path
):
    x, y = synthetic_c_grid()
    x = np.vstack((x, x[-1:] * 2.0, x[-1:] * 3.0))
    y = np.vstack((y, y[-1:] * 2.0, y[-1:] * 3.0))
    monkeypatch.setattr(
        "cfd_naca0012_case.archive_grid", lambda _archive, _ni: (x, y, "0")
    )
    output = tmp_path / "case"
    generate(
        tmp_path / "archive.zip",
        output,
        113,
        0.0,
        5,
        "linear-upwind-velocity",
        outer_row_index=3,
    )
    with np.load(output / "tmr-naca0012-grid.npz") as data:
        assert np.array_equal(data["x"], x[:4])
        assert np.array_equal(data["y"], y[:4])
    spec = json.loads((output / "benchmark-spec.json").read_text())
    assert spec["grid_dimensions"] == [15, 4]
    assert spec["domain"]["source_grid_dimensions"] == [15, 5]
    assert spec["domain"]["retained_outer_row_index"] == 3
    assert spec["domain"]["uses_official_outer_boundary"] is False


def test_generator_copies_compatible_latest_state_with_provenance(
    monkeypatch, tmp_path
):
    x, y = synthetic_c_grid()
    monkeypatch.setattr(
        "cfd_naca0012_case.archive_grid",
        lambda _archive, _ni: (
            x,
            y,
            {
                "archive_sha256": "pinned",
                "archive_member": "synthetic",
                "member_crc32": "0",
                "coordinate_payload_sha256": "coordinates",
            },
        ),
    )
    parent = tmp_path / "parent"
    generate(
        tmp_path / "archive.zip",
        parent,
        113,
        10.0,
        25,
        "linear-upwind-velocity",
    )
    (parent / "execution.json").write_text('[{"stage_passed": true}]\n')
    final = parent / "25"
    final.mkdir()
    for name in CONTINUATION_FIELDS:
        (final / name).write_text(f"final field {name}\n")

    child = tmp_path / "child"
    generate(
        tmp_path / "archive.zip",
        child,
        113,
        10.0,
        50,
        "linear-upwind-velocity",
        parent,
    )

    spec = json.loads((child / "benchmark-spec.json").read_text())
    assert spec["initialization"]["parent_case"] == str(parent.resolve())
    assert spec["initialization"]["parent_final_time"] == 25.0
    for name in CONTINUATION_FIELDS:
        assert (child / "0" / name).read_text() == f"final field {name}\n"
        assert len(spec["initialization"]["fields"][name]["sha256"]) == 64


def test_generator_rejects_invalid_relaxation_before_creating_output(tmp_path):
    output = tmp_path / "invalid"
    with pytest.raises(ValueError, match="relaxation_scale"):
        generate(tmp_path / "missing.zip", output, 113, 0.0, 10, relaxation_scale=0)
    assert not output.exists()


def test_ladson_parser_uses_only_condition_matched_repeat_points(tmp_path):
    data = tmp_path / "ladson.dat"
    data.write_text(
        '# alpha cl cd\n'
        '-0.05 -0.0126 0.00809\n'
        '0.01 -0.0122 0.00804\n'
        '2.0 0.22 0.0082\n'
    )
    result = experimental_points(data, 0.0)
    assert len(result["points"]) == 2
    assert result["mean_cd"] == np.mean([0.00809, 0.00804])


def test_long_window_trend_rejects_slow_drift_hidden_by_short_range():
    values = np.zeros((500, 4))
    values[:, 0] = np.arange(500)
    values[:, 1] = 0.01 + values[:, 0] * 1e-6
    values[:, 2] = 1.0
    projected, limits, passed = long_window_trend(
        values, {"Time": 0, "Cd": 1, "Cl": 2, "CmPitch": 3}, 10.0, 500
    )
    assert projected["Cd"] == pytest.approx(0.0005)
    assert limits["Cd"] == 0.0002
    assert passed is False


def test_coefficient_header_vector_reads_derived_pitch_axis(tmp_path):
    output = tmp_path / "postProcessing" / "coefficients" / "0"
    output.mkdir(parents=True)
    (output / "coefficient.dat").write_text(
        "# pitchAxis : (0.0 0.0 -1.0)\n# Time Cd\n1 0.1\n"
    )
    assert coefficient_header_vector(tmp_path, "pitchAxis") == [0.0, 0.0, -1.0]


def test_ladson_transcription_supplies_matched_quarter_chord_moment():
    zero = matched_rows(0.0)
    ten = matched_rows(10.0)
    assert len(zero) == 3
    assert len(ten) == 2
    assert np.mean([row["cm_quarter_chord_nose_up"] for row in ten]) == pytest.approx(
        0.00505
    )


def test_solver_residual_gate_rejects_force_plateau_with_unsettled_equations():
    fields = ("p", "Ux", "Uy", "e", "omega", "k")
    lines = []
    for _ in range(2):
        lines.extend(
            f"solver: Solving for {name}, Initial residual = 1e-6, Final residual = 1e-9"
            for name in fields
        )
    _, _, passed = solver_residual_gate("\n".join(lines), window=2)
    assert passed is True
    lines[-3] = (
        "solver: Solving for e, Initial residual = 1e-3, Final residual = 1e-7"
    )
    _, _, passed = solver_residual_gate("\n".join(lines), window=2)
    assert passed is False


def test_numerical_independence_uses_experimental_repeatability_scale():
    limits = independence_limits(10.0)
    assert within_limits({"Cd": 0.0001, "Cl": 0.001, "CmPitch": 0.0001}, limits)
    assert not within_limits(
        {"Cd": 0.0003, "Cl": 0.001, "CmPitch": 0.0001}, limits
    )


def test_naca_yplus_parser_rejects_missing_turbulence_model():
    valid = "patch airfoil y+ : min = 0.01, max = 0.19, average = 0.15"
    assert parse_yplus_log(valid)["maximum"] == 0.19
    with pytest.raises(ValueError, match="without a turbulence model"):
        parse_yplus_log("Unable to find turbulence model\n" + valid)


def test_naca_yplus_audit_accepts_pinned_exact_sstm_runtime(tmp_path):
    case = tmp_path / "case"
    case.mkdir()
    (case / "benchmark-spec.json").write_text(
        json.dumps(
            {
                "benchmark": "TMR 2D NACA 0012",
                "grid_dimensions": [897, 257],
                "model_mapping": {
                    "runtime_library": "libTmrSSTmExactProductionCompressible.so"
                },
            }
        )
    )
    log = tmp_path / "postprocess.log"
    log.write_text(
        "Selecting RAS turbulence model TmrSSTmExactProduction\n"
        "patch airfoil y+ : min = 0.01, max = 0.14, average = 0.10\n"
    )

    result = audit_yplus(case, log)

    assert result["wall_resolved_y_plus_gate"] is True
    assert result["airfoil_y_plus"]["maximum"] == pytest.approx(0.14)


def test_transient_transform_replacements_fail_closed():
    solution = replace_once(
        '"(U|k|omega|e)"',
        '"(U|k|omega|e)"',
        '"(rho|U|k|omega|e)"',
        "transient density solver pattern",
    )
    assert solution == '"(rho|U|k|omega|e)"'
    assert replace_once(
        "  p { solver GAMG; }\n",
        "  p { solver GAMG; }\n",
        "  p { solver GAMG; }\n  pFinal { $p; relTol 0; }\n",
        "final pressure solver insertion point",
    ).count("pFinal") == 1

    assert replace_once("one steadyState", "steadyState", "Euler", "scheme") == (
        "one Euler"
    )
    with pytest.raises(ValueError, match="exactly one"):
        replace_once("steadyState steadyState", "steadyState", "Euler", "scheme")


def test_transient_final_interval_statistics():
    times = np.linspace(0.0, 2.0, 201)
    values = np.column_stack((times, 1.0 + times, 2.0 + times, 3.0 + times))
    samples, means, half_ranges = final_interval_statistics(
        ["Time", "Cd", "Cl", "CmPitch"], values, 1.0
    )
    assert samples == 101
    assert means == pytest.approx({"Cd": 2.5, "Cl": 3.5, "CmPitch": 4.5})
    assert half_ranges == pytest.approx({"Cd": 0.5, "Cl": 0.5, "CmPitch": 0.5})


def test_transient_courant_history_pairs_maximum_with_new_time():
    log = (
        "Courant Number mean: 0.1 max: 1.6\n"
        "deltaT = 1e-5\nTime = 1e-4\n"
        "Courant Number mean: 0.01 max: 0.5\nTime = 0.08\n"
    )
    assert courant_history(log) == [(0.0001, 1.6), (0.08, 0.5)]


def test_cross_grid_mapping_requires_adjacent_nested_matching_cases():
    conditions = {
        "mach": 0.15,
        "reynolds_number_chord": 6_000_000,
        "angle_of_attack_deg": 0.0,
        "transport_model": "sutherland",
        "turbulent_prandtl": 0.9,
        "freestream_k_over_acoustic_speed_squared": 9e-9,
        "freestream_omega_mu_over_rho_acoustic_speed_squared": 1e-6,
    }
    model = {"solver": "rhoSimpleFoam", "runtime_library": "libTmrSSTmCompressible.so"}
    source = {
        "benchmark": "TMR 2D NACA 0012",
        "grid_dimensions": [225, 65],
        "conditions": conditions,
        "convection_scheme": "linear-upwind-velocity",
        "model_mapping": model,
    }
    target = {**source, "grid_dimensions": [449, 129]}
    assert mapping_compatibility(source, target)["target_grid_dimensions"] == [449, 129]
    with pytest.raises(ValueError, match="adjacent exactly nested"):
        mapping_compatibility(source, {**target, "grid_dimensions": [897, 257]})
    with pytest.raises(ValueError, match="configurations differ"):
        mapping_compatibility(
            source,
            {**target, "conditions": {**conditions, "angle_of_attack_deg": 10.0}},
        )


def test_structured_prolongation_is_bounded_and_field_round_trips():
    coarse = np.asarray([[0.0], [2.0], [4.0], [6.0]])
    fine = prolong_cells(coarse, (2, 2))
    assert fine.shape == (16, 1)
    assert fine.min() == 0.0
    assert fine.max() == 6.0
    target = "dimensions [0 0 0 0 0 0 0];\ninternalField uniform 0;\nboundaryField {}\n"
    mapped = replace_internal_field(target, "scalar", fine)
    kind, recovered = parse_internal_field(mapped, 16)
    assert kind == "scalar"
    assert recovered == pytest.approx(fine)


def test_structured_prolongation_preserves_constant_vectors():
    coarse = np.tile(np.asarray([[1.0, -2.0, 3.0]]), (6, 1))
    fine = prolong_cells(coarse, (2, 3))
    assert fine == pytest.approx(np.tile(coarse[0], (24, 1)))


def test_mapped_initialization_gate_is_fail_closed(tmp_path):
    assert mapped_initialization_gate(tmp_path, {}) is True
    spec = {
        "initialization": {
            "method": "structured bilinear logical-coordinate prolongation"
        }
    }
    assert mapped_initialization_gate(tmp_path, spec) is False
    spec["initialization"]["method"] = (
        "same-grid higher-to-first-order scheme-sensitivity restart"
    )
    assert mapped_initialization_gate(tmp_path, spec) is False
    spec["initialization"]["method"] = (
        "same-grid tmr-sstm-to-stock-komega-sst sensitivity restart"
    )
    assert mapped_initialization_gate(tmp_path, spec) is False
    spec["initialization"]["method"] = (
        "structured retained-row full-to-reduced-domain restart"
    )
    assert mapped_initialization_gate(tmp_path, spec) is False


def test_cfl3d_force_reference_is_hash_pinned():
    path = Path("runs/cfd-benchmark-data-v5-20260914/n0012clcd_cfl3d_sst.dat")
    result = cfl3d_reference(path, 0.0)
    assert result == pytest.approx(
        {"angle_deg": 0.0, "cl": -7.6275807991e-6, "cd": 0.008093729238}
    )


def test_cfl3d_surface_references_are_hash_pinned():
    root = Path("runs/cfd-benchmark-data-v5-20260914")
    assert hashlib.sha256((root / "n0012cp_cfl3d_sst.dat").read_bytes()).hexdigest() == (
        CFL3D_CP_SHA256
    )
    assert hashlib.sha256((root / "n0012cf_cfl3d_sst.dat").read_bytes()).hexdigest() == (
        CFL3D_CF_SHA256
    )


def test_zero_angle_acceptance_fails_even_with_full_domain_allowance():
    result = evaluate_acceptance(
        Path(
            "runs/cfd-tmr-naca0012-897x257-a0-sstm-sutherland-prt09-linearupwindU-"
            "tmrfreestream-structured449-force-audit-v5-20260914/naca0012-force-audit.json"
        ),
        Path(
            "runs/cfd-tmr-naca0012-a0-tmrfreestream-structured-grid-lust-"
            "scheme-study-v5-20260914/naca0012-numerical-study.json"
        ),
        Path(
            "runs/cfd-tmr-naca0012-897x257-a0-sstm-sutherland-prt09-linearupwindU-"
            "tmrfreestream-structured449-yplus-audit-v4-20260914/naca0012-yplus-audit.json"
        ),
        Path(
            "runs/cfd-tmr-naca0012-897x257-a0-sstm-vs-komegasst-model-"
            "sensitivity-v1-20260914/naca0012-model-sensitivity.json"
        ),
        Path(
            "runs/cfd-tmr-naca0012-897x233-a0-sstm-linearupwindU-domain100c-"
            "force-audit-failed-v1-20260914/naca0012-force-audit.json"
        ),
        Path(
            "runs/cfd-tmr-naca0012-897x233-a0-sstm-linearupwindU-domain100c-"
            "relax05-force-audit-failed-v1-20260914/naca0012-force-audit.json"
        ),
    )

    drag = result["drag_comparison"]
    assert result["numerical_gates"]["domain_sensitivity"] is False
    assert result["numerical_behavior_passed"] is False
    assert drag["conservative_allowance"] == pytest.approx(0.00043180218307785784)
    assert drag["excess_over_allowance"] == pytest.approx(0.00027689705768114357)
    assert drag["gate_even_granting_full_domain_allowance"] is False
    assert result["accepted_for_rocket"] is False


def test_transport_fit_preserves_sutherland_viscosity_and_constant_prandtl():
    cp = 1004.5
    mu_coefficients, kappa_coefficients, error = transport_coefficients(
        8.067568036899373e-7, 110.4, cp
    )

    temperatures = np.linspace(250.0, 350.0, 101)
    viscosity = np.polynomial.polynomial.polyval(temperatures, mu_coefficients)
    conductivity = np.polynomial.polynomial.polyval(
        temperatures, kappa_coefficients
    )
    assert error < 2e-9
    assert np.max(np.abs(cp * viscosity / conductivity - MOLECULAR_PRANDTL)) < 1e-12


def test_transport_drag_decomposition_uses_final_window(tmp_path):
    log = tmp_path / "solver.log"
    log.write_text(
        "Cd: 9 8 1 0\n"
        "Cd: 0.008 0.001 0.007 0\n"
        "Cd: 0.010 0.003 0.007 0\n"
    )

    result = drag_decomposition(log, window=2)
    assert result == pytest.approx(
        {
            "samples": 2,
            "total_cd": 0.009,
            "pressure_cd": 0.002,
            "viscous_cd": 0.007,
            "internal_cd": 0.0,
        }
    )


def test_sutherland_pr_image_provenance_pins_all_build_inputs():
    provenance = json.loads(
        Path("cfd/sstm-compressible-pr072-image-provenance.json").read_text()
    )
    assert provenance["image"]["id"] == (
        "sha256:2870176815d77d1b6e252003db8f7598f2bb25e891c7ea97ec459e469b54d020"
    )
    for relative_path, expected_sha256 in provenance["build_inputs"].items():
        assert hashlib.sha256(Path(relative_path).read_bytes()).hexdigest() == (
            expected_sha256
        )


def test_zero_angle_drag_component_audit_closes_total_difference():
    result = audit_drag_components(
        Path(
            "runs/cfd-tmr-naca0012-897x257-a0-sstm-sutherland-prt09-linearupwindU-"
            "tmrfreestream-structured449-fixed6000-12r-20260914"
        ),
        Path(
            "runs/cfd-tmr-naca0012-897x257-a0-sstm-sutherland-prt09-linearupwindU-"
            "tmrfreestream-structured449-force-audit-v5-20260914/"
            "naca0012-force-audit.json"
        ),
        Path("runs/cfd-benchmark-data-v5-20260914"),
    )

    difference = result["openfoam_minus_cfl3d"]
    assert difference["pressure_cd"] + difference["viscous_cd"] == pytest.approx(
        difference["total_cd"]
    )
    assert difference["viscous_fraction_of_total_discrepancy"] == pytest.approx(
        0.6649421915806742
    )
    assert result["accepted_for_rocket"] is False


def test_incompressible_residual_gate_checks_every_solved_field():
    lines = []
    for _ in range(100):
        for name in ("p", "Ux", "Uy", "omega", "k"):
            lines.append(f"Solving for {name}, Initial residual = 9e-6")
    final, recent_max, passed = incompressible_residual_gate("\n".join(lines))
    assert passed is True
    assert final == pytest.approx({name: 9e-6 for name in final})
    assert recent_max == pytest.approx({name: 9e-6 for name in recent_max})

    lines[-1] = "Solving for k, Initial residual = 1.01e-5"
    assert incompressible_residual_gate("\n".join(lines))[2] is False


def test_tmr_sstm_k_only_limiter_keeps_omega_production_unlimited():
    source = Path(
        "cfd/models/TmrSSTmKOnlyLimiter/TmrSSTmKOnlyLimiter.C"
    ).read_text()
    omega_block, k_block = source.split("tmp<fvScalarMatrix> kEqn", maxsplit=1)

    assert "gamma*GbyNu0" in omega_block
    assert "GbyNu(GbyNu0" not in omega_block
    assert "this->Pk(G)" in k_block
    assert "c1=20" in k_block


def test_tmr_sstm_k_only_limiter_image_provenance_pins_build_inputs():
    provenance = json.loads(
        Path("cfd/sstm-k-only-limiter-pr072-image-provenance.json").read_text()
    )
    assert provenance["image_id"] == (
        "sha256:777e5ff0348eab1026f69bfe7fd2a01685d250a6a186a674a9bdc0e83ff7ef8b"
    )
    for relative_path, expected_sha256 in provenance["source_sha256"].items():
        assert hashlib.sha256(Path(relative_path).read_bytes()).hexdigest() == (
            expected_sha256
        )


def test_tmr_sstm_exact_production_returns_s_squared():
    source = Path(
        "cfd/models/TmrSSTmExactProduction/TmrSSTmExactProduction.C"
    ).read_text()

    assert "const volScalarField& S2" in source
    assert "S2()" in source
    assert "devTwoSymm" not in source


def test_tmr_sstm_exact_production_image_provenance_pins_build_inputs():
    provenance = json.loads(
        Path("cfd/sstm-exact-production-pr072-image-provenance.json").read_text()
    )
    assert provenance["image_id"] == (
        "sha256:ae3235d75b54311a6dbcdfc2b45f6c9be77a8ff0743c099cf5ca3f3e9db0d23f"
    )
    for relative_path, expected_sha256 in provenance["source_sha256"].items():
        assert hashlib.sha256(Path(relative_path).read_bytes()).hexdigest() == (
            expected_sha256
        )
