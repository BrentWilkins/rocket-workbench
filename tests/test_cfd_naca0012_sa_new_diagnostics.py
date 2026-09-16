import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_naca0012_plot3d_mesh_parity import unique_nearest_mapping
from cfd_naca0012_force_audit import coefficient_history
from cfd_naca0012_sa_nonorthogonal_comparison import classify
from cfd_naca0012_sa_nonorthogonal_restart import restart
from cfd_naca0012_sa_openfoam4_restart import restart as openfoam4_restart
from cfd_openfoam_naca0012_plot_audit import components


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_nonorthogonal_restart_changes_only_declared_system_values(tmp_path):
    source = tmp_path / "source"
    for directory in ("constant", "system", "5000"):
        (source / directory).mkdir(parents=True, exist_ok=True)
    for field in ("U", "p", "nuTilda", "nut"):
        (source / "5000" / field).write_text(f"field-{field}\n")
    (source / "constant" / "transportProperties").write_text("nu 8.58e-06;\n")
    (source / "system" / "fvSolution").write_text(
        "SIMPLE { nNonOrthogonalCorrectors 0; }\n"
    )
    (source / "system" / "controlDict").write_text(
        "application simpleFoam; endTime 5000; deltaT 1;\n"
    )
    spec = {
        "conditions": {"nu_tilda_m2_s": 3.432e-05},
        "numerics": {"iterations": 5000},
        "mechanism_test": {"name": "uniform_half_scale_SIMPLE_under_relaxation"},
    }
    spec_path = source / "benchmark-spec.json"
    spec_path.write_text(json.dumps(spec) + "\n")
    (source / "execution.json").write_text(
        json.dumps([{"stage_passed": True}]) + "\n"
    )
    source_audit = tmp_path / "source-audit.json"
    source_audit.write_text(json.dumps({"case_spec_sha256": digest(spec_path)}) + "\n")

    target = tmp_path / "target"
    plan = Path(
        "cfd/naca0012-sa-nonorthogonal-corrector-screen-plan.json"
    ).resolve(strict=True)
    record = restart(source, source_audit, target, plan)

    assert "nNonOrthogonalCorrectors 4;" in (
        target / "system" / "fvSolution"
    ).read_text()
    assert "endTime 1000;" in (target / "system" / "controlDict").read_text()
    assert (target / "constant" / "transportProperties").read_text() == (
        source / "constant" / "transportProperties"
    ).read_text()
    assert all(
        (target / "0" / field).read_bytes() == (source / "5000" / field).read_bytes()
        for field in ("U", "p", "nuTilda", "nut")
    )
    target_spec = json.loads((target / "benchmark-spec.json").read_text())
    assert target_spec["numerics"]["iterations"] == 1000
    assert target_spec["mechanism_test"]["only_nNonOrthogonalCorrectors_changed"]
    assert record["fv_solution_sha256"] == digest(target / "system" / "fvSolution")


def test_nonorthogonal_screen_classifier_honors_declared_boundaries():
    assert classify(-0.000019) == "null_effect"
    assert classify(0.00002) == "null_effect"
    assert classify(-0.00003) == "ambiguous_effect"
    assert classify(0.00003) == "ambiguous_effect"
    assert classify(-0.00005) == "material_toward_official_plot"


def test_plot_components_finds_diagonal_and_separate_regions():
    mask = np.zeros((5, 6), dtype=bool)
    mask[0, 0] = True
    mask[0, 1] = True
    mask[3, 4:6] = True
    groups = sorted((sorted(group) for group in components(mask)), key=len)
    assert groups == [[(0, 0), (1, 0)], [(4, 3), (5, 3)]]


def test_unique_nearest_mapping_is_bijective_and_checks_tolerance():
    source = np.array([[0.0, 0.0, 0.0], [1.0, 2.0, 3.0], [-1.0, 0.5, 2.0]])
    target = source[[2, 0, 1]] + np.array([1e-9, -1e-9, 0.0])
    mapping, distances = unique_nearest_mapping(source, target, tolerance=1e-7)
    assert mapping.tolist() == [1, 2, 0]
    assert np.max(distances) < 2e-9

    with np.testing.assert_raises(ValueError):
        unique_nearest_mapping(source, target, tolerance=1e-12)


def test_legacy_force_coefficient_history_normalizes_pitch_name(tmp_path):
    folder = tmp_path / "postProcessing" / "coefficients" / "0"
    folder.mkdir(parents=True)
    (folder / "forceCoeffs.dat").write_text(
        "# Time Cm Cd Cl Cl(f) Cl(r)\n"
        "1 -1e-4 8.5e-3 2e-3 1e-3 1e-3\n"
    )
    columns, values = coefficient_history(tmp_path)
    assert columns == ["Time", "CmPitch", "Cd", "Cl", "Cl(f)", "Cl(r)"]
    assert values.shape == (1, 6)


def test_openfoam4_restart_records_only_compatibility_adapters(tmp_path):
    source = tmp_path / "source-v2512"
    for directory in ("constant", "system", "5000"):
        (source / directory).mkdir(parents=True, exist_ok=True)
    (source / "5000" / "U").write_text(
        "boundaryField { farfield { type            freestreamVelocity; } }\n"
    )
    for field in ("p", "nuTilda", "nut"):
        (source / "5000" / field).write_text(f"field-{field}\n")
    (source / "constant" / "transportProperties").write_text("nu 8.58e-06;\n")
    (source / "constant" / "turbulenceProperties").write_text(
        "simulationType RAS;\n"
    )
    (source / "system" / "fvSchemes").write_text("default none;\n")
    (source / "system" / "fvSolution").write_text(
        "SIMPLE\n{\n    nNonOrthogonalCorrectors 0;\n}\n"
    )
    (source / "system" / "controlDict").write_text(
        "application simpleFoam; endTime 5000; libs (forces);\n"
    )
    spec = {
        "conditions": {"nu_tilda_m2_s": 3.432e-05},
        "numerics": {"iterations": 5000},
        "model_mapping": {"solver": "simpleFoam", "ras_model": "SpalartAllmaras"},
    }
    spec_path = source / "benchmark-spec.json"
    spec_path.write_text(json.dumps(spec) + "\n")
    (source / "execution.json").write_text(
        json.dumps([{"stage_passed": True}]) + "\n"
    )
    source_audit = tmp_path / "source-audit.json"
    source_audit.write_text(json.dumps({"case_spec_sha256": digest(spec_path)}) + "\n")

    target = tmp_path / "target-v4"
    plan = Path("cfd/naca0012-sa-openfoam4-lineage-screen-plan.json").resolve(
        strict=True
    )
    record = openfoam4_restart(source, source_audit, target, plan)

    assert "type            freestream;" in (target / "0" / "U").read_text()
    assert 'libs ("libforces.so");' in (
        target / "system" / "controlDict"
    ).read_text()
    assert "pRefCell 0;" in (target / "system" / "fvSolution").read_text()
    target_spec = json.loads((target / "benchmark-spec.json").read_text())
    assert len(target_spec["mechanism_test"]["compatibility_adapters"]) == 3
    assert target_spec["model_mapping"]["version"] == "4.1"
    assert record["fv_schemes_sha256"] == digest(target / "system" / "fvSchemes")
