import json
import hashlib
import sys
from pathlib import Path

import numpy as np


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_naca0012_sa_control_case import generate
from cfd_naca0012_sa_control_audit import cfl3d_reference, residual_gate
from cfd_naca0012_sa_control_continue import continue_case
from cfd_naca0012_sa_damping_restart import restart as damping_restart


def synthetic_c_grid() -> tuple[np.ndarray, np.ndarray]:
    x = np.zeros((3, 15))
    y = np.zeros((3, 15))
    angles = np.linspace(0, 2 * np.pi, 9)
    x[0, :4] = [4, 3, 2, 1]
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


def test_sa_control_uses_documented_nasa_conditions(monkeypatch, tmp_path):
    x, y = synthetic_c_grid()
    monkeypatch.setattr(
        "cfd_naca0012_sa_control_case.archive_grid",
        lambda _archive, _ni: (
            x,
            y,
            {"archive_sha256": "pinned", "archive_member": "synthetic"},
        ),
    )
    archive = tmp_path / "grid.zip"
    archive.write_bytes(b"synthetic")
    output = tmp_path / "case"
    spec = generate(archive, output, iterations=500)

    assert spec["model_mapping"]["solver"] == "simpleFoam"
    assert spec["model_mapping"]["ras_model"] == "SpalartAllmaras"
    assert spec["benchmark"] == "TMR 2D NACA 0012"
    assert spec["source"]["archive_sha256"] == "pinned"
    assert abs(spec["conditions"]["reynolds_number"] - 6_000_000) < 200
    assert spec["grid_dimensions"] == [15, 3]
    assert spec["acceptance_limits"]["absolute_cd_vs_cfl3d"] == 0.0002

    velocity = (output / "0" / "U").read_text()
    assert "class volVectorField;" in velocity
    assert "internalField uniform (51.4815 0 0);" in velocity
    assert "type freestreamVelocity;" in velocity
    nu_tilda = (output / "0" / "nuTilda").read_text()
    assert "freestreamValue uniform 3.432e-05;" in nu_tilda
    turbulence = (output / "constant" / "turbulenceProperties").read_text()
    assert "RASModel SpalartAllmaras;" in turbulence
    control = (output / "system" / "controlDict").read_text()
    assert "Aref 0.01;" in control
    assert "magUInf 51.4815;" in control
    assert json.loads((output / "benchmark-spec.json").read_text()) == spec


def test_sa_control_reference_and_residual_gate(monkeypatch, tmp_path):
    reference = tmp_path / "n0012clcd_cfl3d_sa.dat"
    reference.write_text("# synthetic\n0. -6.8553224298E-06 0.81924676041E-02\n")
    monkeypatch.setattr(
        "cfd_naca0012_sa_control_audit.REFERENCE_SHA256",
        hashlib.sha256(reference.read_bytes()).hexdigest(),
    )
    row = cfl3d_reference(reference)
    assert row["cd"] == 0.0081924676041

    lines = []
    for _ in range(100):
        for name in ("p", "Ux", "Uy", "nuTilda"):
            lines.append(f"Solving for {name}, Initial residual = 1e-6")
    final, recent, passed = residual_gate("\n".join(lines))
    assert passed
    assert final == recent == {name: 1e-6 for name in ("p", "Ux", "Uy", "nuTilda")}


def test_sa_continuation_copies_only_reconstructed_state_with_hashes(tmp_path):
    source = tmp_path / "source"
    (source / "constant").mkdir(parents=True)
    (source / "system").mkdir()
    (source / "5000").mkdir()
    (source / "constant" / "transportProperties").write_text("fixed\n")
    (source / "system" / "controlDict").write_text("fixed\n")
    for name in ("U", "p", "nuTilda", "nut"):
        (source / "5000" / name).write_text(f"{name} final\n")
    spec = {
        "benchmark": "TMR 2D NACA 0012",
        "model_mapping": {"ras_model": "SpalartAllmaras"},
        "numerics": {"iterations": 5000},
    }
    spec_path = source / "benchmark-spec.json"
    spec_path.write_text(json.dumps(spec) + "\n")
    (source / "execution.json").write_text(
        json.dumps([{"stage_passed": True}]) + "\n"
    )
    audit = tmp_path / "audit.json"
    audit.write_text(
        json.dumps(
            {
                "case_spec_sha256": hashlib.sha256(spec_path.read_bytes()).hexdigest(),
                "gate_1_passed": False,
                "long_window_trend_gate": False,
                "solver_residual_gate": False,
            }
        )
        + "\n"
    )
    target = tmp_path / "target"
    record = continue_case(source, audit, target)
    assert record["source_time"] == 5000.0
    assert record["physics_or_numerics_changed"] is False
    assert (target / "0" / "U").read_text() == "U final\n"
    target_spec = json.loads((target / "benchmark-spec.json").read_text())
    assert target_spec["continuation"]["cumulative_iterations"] == 10000


def test_sa_damping_restart_applies_one_uniform_half_scale(monkeypatch, tmp_path):
    source = tmp_path / "source"
    (source / "constant").mkdir(parents=True)
    (source / "system").mkdir()
    (source / "5000").mkdir()
    (source / "constant" / "transportProperties").write_text("fixed\n")
    (source / "system" / "controlDict").write_text("fixed\n")
    (source / "system" / "fvSolution").write_text(
        "fields { p 0.3; }\nequations { U 0.7; nuTilda 0.7; }\n"
    )
    for name in ("U", "p", "nuTilda", "nut"):
        (source / "5000" / name).write_text(f"{name} final\n")
    spec_path = source / "benchmark-spec.json"
    spec_path.write_text(
        json.dumps(
            {
                "benchmark": "TMR 2D NACA 0012",
                "model_mapping": {"ras_model": "SpalartAllmaras"},
                "numerics": {"iterations": 5000},
            }
        )
        + "\n"
    )
    (source / "execution.json").write_text(
        json.dumps([{"stage_passed": True}]) + "\n"
    )
    audit = tmp_path / "audit.json"
    audit.write_text(
        json.dumps(
            {
                "case_spec_sha256": hashlib.sha256(spec_path.read_bytes()).hexdigest(),
                "gate_1_passed": False,
                "long_window_trend_gate": False,
                "solver_residual_gate": False,
            }
        )
        + "\n"
    )
    plan = tmp_path / "plan.json"
    plan.write_text("{}\n")
    monkeypatch.setattr(
        "cfd_naca0012_sa_damping_restart.PLAN_SHA256",
        hashlib.sha256(plan.read_bytes()).hexdigest(),
    )
    target = tmp_path / "target"
    record = damping_restart(source, audit, target, plan)
    solution = (target / "system" / "fvSolution").read_text()
    assert "fields { p 0.15; }" in solution
    assert "equations { U 0.35; nuTilda 0.35; }" in solution
    assert record["physics_or_numerics_changed"] is True
    target_spec = json.loads((target / "benchmark-spec.json").read_text())
    assert target_spec["mechanism_test"]["only_numerical_relaxation_changed"]
