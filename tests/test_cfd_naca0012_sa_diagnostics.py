import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_naca0012_sa_execution_sensitivity import compare
from cfd_naca0012_sa_freestream_restart import restart
from cfd_naca0012_sa_ft2_restart import restart as ft2_restart
from cfd_naca0012_sa_profile_audit import numeric_pairs_before_next_zone, profile_error


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_sa_reference_parser_stops_at_second_zone(tmp_path):
    reference = tmp_path / "reference.dat"
    reference.write_text(
        'variables="x","cp"\nzone, t="alpha=0"\n0 1\n1 2\n'
        'zone, t="alpha=10"\n0 99\n'
    )
    np.testing.assert_allclose(
        numeric_pairs_before_next_zone(reference), [[0.0, 1.0], [1.0, 2.0]]
    )


def test_profile_error_interpolates_only_retained_chord():
    result = profile_error(
        np.array([0.0, 0.25, 0.75, 1.0]),
        np.array([99.0, 1.5, 2.5, 99.0]),
        np.array([[0.0, 1.0], [1.0, 3.0]]),
    )
    assert result["comparison_points"] == 2
    assert result["rms_difference"] == 0.0


def test_serial_comparison_closes_decomposition_mechanism(tmp_path):
    plan = Path("cfd/naca0012-sa-control-serial-plan.json").resolve(strict=True)
    source_case = tmp_path / "source"
    serial_case = tmp_path / "serial"
    source_case.mkdir()
    serial_case.mkdir()
    source_audit = tmp_path / "source.json"
    source_audit.write_text(
        json.dumps(
            {
                "case": str(source_case),
                "last_window_mean": {"Cd": 0.00849, "Cl": 0.0034, "CmPitch": 0.0001},
                "solver_initial_residuals_final": {"Uy": 4.1e-5},
                "solver_residual_gate": False,
            }
        )
    )
    serial_audit = tmp_path / "serial.json"
    serial_audit.write_text(
        json.dumps(
            {
                "case": str(serial_case),
                "last_window_mean": {"Cd": 0.008488, "Cl": 0.0027, "CmPitch": 0.00028},
                "solver_initial_residuals_final": {"Uy": 3.5e-5},
                "solver_residual_gate": False,
                "restart_provenance_gate": True,
                "runtime_and_execution_gate": True,
            }
        )
    )
    (serial_case / "benchmark-spec.json").write_text(
        json.dumps(
            {
                "initialization": {
                    "source_case": str(source_case),
                    "source_audit_sha256": digest(source_audit),
                },
                "mechanism_test": {
                    "plan_sha256": digest(plan),
                    "only_execution_decomposition_changed": True,
                    "before": {"mpi_ranks": 12, "decomposition": "Scotch"},
                    "after": {"mpi_ranks": 1, "decomposition": "none"},
                },
            }
        )
    )
    result = compare(source_audit, serial_audit, plan)
    assert result["gate"] is True
    assert result["decomposition_is_dominant_mechanism"] is False


def test_freestream_restart_changes_only_nutilda_boundary_input(tmp_path):
    source = tmp_path / "source"
    for directory in ("constant", "system", "5000"):
        (source / directory).mkdir(parents=True, exist_ok=True)
    for name in ("U", "p", "nut"):
        (source / "5000" / name).write_text(f"{name}\n")
    (source / "5000" / "nuTilda").write_text(
        "internal state\nfreestreamValue uniform 3.432e-05;\n"
    )
    spec_path = source / "benchmark-spec.json"
    spec_path.write_text(
        json.dumps(
            {
                "benchmark": "TMR 2D NACA 0012",
                "model_mapping": {"ras_model": "SpalartAllmaras"},
                "conditions": {"nu_tilda_m2_s": 3.432e-05},
            }
        )
    )
    (source / "execution.json").write_text(
        json.dumps([{"stage_passed": True}])
    )
    source_audit = tmp_path / "source-audit.json"
    source_audit.write_text(json.dumps({"case_spec_sha256": digest(spec_path)}))
    target = tmp_path / "target"
    plan = Path(
        "cfd/naca0012-sa-freestream-ratio-sensitivity-plan.json"
    ).resolve(strict=True)

    result = restart(source, source_audit, target, plan)

    assert "freestreamValue uniform 2.574e-05;" in (
        target / "0" / "nuTilda"
    ).read_text()
    assert (target / "0" / "U").read_text() == "U\n"
    target_spec = json.loads((target / "benchmark-spec.json").read_text())
    assert target_spec["conditions"]["nu_tilda_m2_s"] == 2.574e-05
    assert target_spec["mechanism_test"]["only_farfield_nuTilda_changed"] is True
    assert result["stage_passed"] is True


def test_ft2_restart_changes_only_turbulence_dictionary(tmp_path):
    source = tmp_path / "source"
    for directory in ("constant", "system", "5000"):
        (source / directory).mkdir(parents=True, exist_ok=True)
    turbulence = "RAS\n{\n    printCoeffs on;\n}\n"
    (source / "constant" / "turbulenceProperties").write_text(turbulence)
    for name in ("U", "p", "nuTilda", "nut"):
        (source / "5000" / name).write_text(f"{name}\n")
    spec_path = source / "benchmark-spec.json"
    spec_path.write_text(
        json.dumps(
            {
                "model_mapping": {"ras_model": "SpalartAllmaras"},
                "mechanism_test": {
                    "after": {"nuTilda_to_nu_ratio": 3.0},
                    "model_ft2": False,
                },
            }
        )
    )
    (source / "execution.json").write_text(json.dumps([{"stage_passed": True}]))
    source_audit = tmp_path / "source-audit.json"
    source_audit.write_text(json.dumps({"case_spec_sha256": digest(spec_path)}))
    target = tmp_path / "target"
    plan = Path("cfd/naca0012-sa-standard-ft2-sensitivity-plan.json").resolve(
        strict=True
    )

    result = ft2_restart(source, source_audit, target, plan)

    assert "ft2 true;" in (target / "constant" / "turbulenceProperties").read_text()
    assert (target / "system").is_dir()
    assert (target / "0" / "nuTilda").read_text() == "nuTilda\n"
    target_spec = json.loads((target / "benchmark-spec.json").read_text())
    assert target_spec["mechanism_test"]["only_ft2_switch_changed"] is True
    assert result["stage_passed"] is True
