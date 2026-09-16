import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_naca0012_stock_sst_audit import cfl3d_reference, residuals
from cfd_naca0012_stock_sst_continue import build as build_stock_sst_continuation
from cfd_naca0012_exact_sstm_incompressible_restart import (
    add_runtime_libraries,
    build as build_exact_sstm,
)
from cfd_naca0012_exact_sstm_compressible_audit import compressible_residuals
from cfd_naca0012_exact_sstm_compressible_restart import (
    build as build_exact_sstm_compressible,
)
from cfd_naca0012_stock_sst_restart import replace_once, reset_field_location
from cfd_naca0012_stock_sst_upwind_restart import (
    _replace_once as replace_upwind_once,
    build as build_stock_sst_upwind,
)
from cfd_naca0012_stock_sst_upwind_from_sa import build as build_stock_sst_upwind_from_sa


def test_stock_sst_plan_is_explicitly_diagnostic_and_fail_closed():
    root = Path(__file__).resolve().parents[1]
    plan = json.loads(
        (root / "cfd" / "naca0012-stock-sst-relative-diagnostic-plan.json").read_text()
    )
    assert plan["validation_status"] == "diagnostic_only_gate_2_remains_blocked_by_failed_gate_1"
    assert plan["source"]["source_gate_1_passed"] is False
    assert plan["declared_changes"]["turbulence_model"].startswith("SpalartAllmaras")
    assert plan["execution"]["gpu"] is False
    assert plan["predeclared_outputs"]["force_agreement"].endswith("<= 0.0002")


def test_restart_text_helpers_are_fail_closed():
    assert reset_field_location('location "5000";\nobject U;') == 'location "0";\nobject U;'
    with pytest.raises(ValueError, match="one FoamFile location"):
        reset_field_location("object U;")
    assert replace_once("a nuTilda b", "nuTilda", "k", "model") == "a k b"
    with pytest.raises(ValueError, match="exactly one model"):
        replace_once("nuTilda nuTilda", "nuTilda", "k", "model")


def test_stock_sst_residual_gate_requires_all_five_equations():
    lines = []
    for _ in range(100):
        for name in ("p", "Ux", "Uy", "k", "omega"):
            lines.append(f"Solving for {name}, Initial residual = 9e-6")
    final, recent, passed = residuals("\n".join(lines))
    assert passed
    assert set(final) == {"p", "Ux", "Uy", "k", "omega"}
    assert all(value == 9e-6 for value in recent.values())
    bad = "\n".join(lines).replace(
        "Solving for omega, Initial residual = 9e-6",
        "Solving for omega, Initial residual = 2e-5",
        1,
    )
    assert residuals(bad)[2] is False


def test_stock_sst_reference_is_checksum_pinned():
    root = Path(__file__).resolve().parents[1]
    reference = cfl3d_reference(
        root / "runs" / "cfd-benchmark-data-v6-sa-20260914" / "n0012clcd_cfl3d_sst.dat"
    )
    assert reference["Cd"] == pytest.approx(0.008093729238)
    assert reference["Cl"] == pytest.approx(-7.6275807991e-06)


def test_exact_production_has_separate_incompressible_registration():
    root = Path(__file__).resolve().parents[1]
    limiter = root / "cfd" / "models" / "TmrSSTmKOnlyLimiterIncompressible"
    exact = root / "cfd" / "models" / "TmrSSTmExactProductionIncompressible"
    assert 'makeRASModel(TmrSSTmKOnlyLimiter);' in (
        limiter / "makeTmrSSTmKOnlyLimiter.C"
    ).read_text()
    assert "libTmrSSTmKOnlyLimiter" in (limiter / "Make" / "files").read_text()
    assert 'makeRASModel(TmrSSTmExactProduction);' in (
        exact / "makeTmrSSTmExactProduction.C"
    ).read_text()
    assert "libTmrSSTmExactProduction" in (exact / "Make" / "files").read_text()
    dockerfile = (root / "cfd" / "Dockerfile.2512-sstm-exact-production-dual").read_text()
    assert "libTmrSSTmExactProduction.so" in dockerfile
    assert "libTmrSSTmExactProductionCompressible.so" not in dockerfile


def test_exact_production_dual_image_provenance_pins_build_inputs():
    root = Path(__file__).resolve().parents[1]
    provenance = json.loads(
        (root / "cfd" / "sstm-exact-production-dual-image-provenance.json").read_text()
    )
    assert provenance["architecture"] == "amd64"
    assert provenance["runtime_libraries"] == {
        "incompressible": "libTmrSSTmExactProduction.so",
        "compressible": "libTmrSSTmExactProductionCompressible.so",
    }
    for relative, expected in provenance["source_sha256"].items():
        actual = hashlib.sha256((root / relative).read_bytes()).hexdigest()
        assert actual == expected


def test_exact_sstm_plan_and_builder_block_unconverged_stock_source(tmp_path):
    root = Path(__file__).resolve().parents[1]
    plan_path = root / "cfd" / "naca0012-exact-sstm-incompressible-relative-plan.json"
    plan = json.loads(plan_path.read_text())
    provenance_path = root / "cfd" / "sstm-exact-production-dual-image-provenance.json"
    assert plan["source"]["entry_gate"].startswith("diagnostic_numerics_passed must be true")
    assert hashlib.sha256(provenance_path.read_bytes()).hexdigest() == plan["declared_changes"][
        "runtime_image"
    ]["provenance_sha256"]

    source = root / plan["source"]["case"]
    audit = tmp_path / "failed-stock-audit.json"
    audit.write_text(
        json.dumps(
            {
                "case": str(source.resolve()),
                "case_spec_sha256": plan["source"]["case_spec_sha256"],
                "diagnostic_numerics_passed": False,
                "strict_gate_2_passed": False,
            }
        )
    )
    with pytest.raises(ValueError, match="entry gate did not pass"):
        build_exact_sstm(source, audit, tmp_path / "must-not-exist")
    assert not (tmp_path / "must-not-exist").exists()


def test_stock_sst_continuation_builder_requires_declared_trigger(tmp_path):
    root = Path(__file__).resolve().parents[1]
    plan = json.loads((root / "cfd" / "naca0012-stock-sst-continuation-plan.json").read_text())
    source = root / plan["source"]["case"]
    audit = tmp_path / "incomplete-stock-audit.json"
    audit.write_text(
        json.dumps(
            {
                "case": str(source.resolve()),
                "case_spec_sha256": plan["source"]["case_spec_sha256"],
            }
        )
    )
    with pytest.raises(ValueError, match="Continuation prerequisite provenance_gate"):
        build_stock_sst_continuation(source, audit, tmp_path / "must-not-exist")
    assert not (tmp_path / "must-not-exist").exists()


def test_stock_sst_upwind_plan_changes_only_turbulence_convection():
    root = Path(__file__).resolve().parents[1]
    plan = json.loads(
        (
            root
            / "cfd"
            / "naca0012-stock-sst-turbulence-upwind-remediation-plan-v1.json"
        ).read_text()
    )
    assert set(plan["declared_change"]) == {"div(phi,k)", "div(phi,omega)"}
    assert all(change["to"] == "bounded Gauss upwind" for change in plan["declared_change"].values())
    assert "absolute mean Cl <= 0.004" in plan["predeclared_outputs"]["zero_angle_symmetry"]
    assert "CmPitch <= 0.0002" in plan["predeclared_outputs"]["zero_angle_symmetry"]


def test_stock_sst_upwind_text_replacement_is_fail_closed():
    source = "div(phi,k) bounded Gauss linearUpwind grad(k);"
    assert replace_upwind_once(source, source, "div(phi,k) bounded Gauss upwind;") == (
        "div(phi,k) bounded Gauss upwind;"
    )
    with pytest.raises(ValueError, match="Expected exactly one"):
        replace_upwind_once("", source, "replacement")
    with pytest.raises(ValueError, match="Expected exactly one"):
        replace_upwind_once(f"{source} {source}", source, "replacement")


def test_stock_sst_upwind_builder_rejects_wrong_audit_hash(tmp_path):
    root = Path(__file__).resolve().parents[1]
    plan = json.loads(
        (
            root
            / "cfd"
            / "naca0012-stock-sst-turbulence-upwind-remediation-plan-v1.json"
        ).read_text()
    )
    source = root / plan["source"]["case"]
    audit = tmp_path / "wrong-audit.json"
    audit.write_text("{}\n")
    with pytest.raises(ValueError, match="Source audit does not match the plan"):
        build_stock_sst_upwind(source, audit, tmp_path / "must-not-exist")
    assert not (tmp_path / "must-not-exist").exists()


def test_stock_sst_upwind_from_sa_plan_preserves_gates_and_source():
    root = Path(__file__).resolve().parents[1]
    plan = json.loads(
        (root / "cfd" / "naca0012-stock-sst-upwind-from-sa-plan-v1.json").read_text()
    )
    assert plan["source"]["case_spec_sha256"] == hashlib.sha256(
        (root / plan["source"]["case"] / "benchmark-spec.json").read_bytes()
    ).hexdigest()
    assert plan["source"]["audit_sha256"] == hashlib.sha256(
        (root / plan["source"]["audit"]).read_bytes()
    ).hexdigest()
    assert plan["source"]["required_gates"]["zero_angle_symmetry_gate"] is True
    assert "CmPitch <= 0.0002" in plan["predeclared_outputs"]["zero_angle_symmetry"]


def test_stock_sst_upwind_from_sa_builder_rejects_wrong_audit_hash(tmp_path):
    root = Path(__file__).resolve().parents[1]
    plan = json.loads(
        (root / "cfd" / "naca0012-stock-sst-upwind-from-sa-plan-v1.json").read_text()
    )
    source = root / plan["source"]["case"]
    audit = tmp_path / "wrong-audit.json"
    audit.write_text("{}\n")
    with pytest.raises(ValueError, match="Source audit does not match the plan"):
        build_stock_sst_upwind_from_sa(
            source,
            audit,
            root / "runs" / "cfd-benchmark-data-v6-sa-20260914" / "naca0012-grids.zip",
            tmp_path / "must-not-exist",
        )
    assert not (tmp_path / "must-not-exist").exists()


def test_exact_sstm_builder_enforces_supplied_plan(tmp_path):
    root = Path(__file__).resolve().parents[1]
    default_plan = json.loads(
        (root / "cfd" / "naca0012-exact-sstm-incompressible-relative-plan.json").read_text()
    )
    custom_plan = json.loads(json.dumps(default_plan))
    custom_plan["source"]["case_spec_sha256"] = "0" * 64
    custom_plan_path = tmp_path / "custom-exact-plan.json"
    custom_plan_path.write_text(json.dumps(custom_plan) + "\n")
    source = root / default_plan["source"]["case"]
    source_audit = (
        root
        / "runs"
        / "cfd-openfoam-naca0012-stock-sst-direct-audit-v4-20260915"
        / "naca0012-stock-sst-diagnostic-audit.json"
    )
    with pytest.raises(ValueError, match="predeclared plan"):
        build_exact_sstm(
            source,
            source_audit,
            tmp_path / "must-not-exist",
            plan_path=custom_plan_path,
        )
    assert not (tmp_path / "must-not-exist").exists()


def test_upwind_continuation_plan_pins_failed_residual_source():
    root = Path(__file__).resolve().parents[1]
    plan = json.loads(
        (root / "cfd" / "naca0012-stock-sst-upwind-continuation-plan-v1.json").read_text()
    )
    assert plan["trigger"]["required_false"] == [
        "solver_residual_gate",
        "diagnostic_numerics_passed",
    ]
    assert "scheme_change_only_gate" in plan["trigger"]["required_true"]
    assert len(plan["source"]["audit_sha256"]) == 64
    assert plan["execution"]["additional_iterations"] == 5000


def test_continuation_builder_enforces_supplied_audit_digest(tmp_path):
    root = Path(__file__).resolve().parents[1]
    plan_path = root / "cfd" / "naca0012-stock-sst-upwind-continuation-plan-v1.json"
    plan = json.loads(plan_path.read_text())
    source = root / plan["source"]["case"]
    wrong_audit = tmp_path / "wrong-audit.json"
    wrong_audit.write_text("{}\n")

    with pytest.raises(ValueError, match="source audit does not match"):
        build_stock_sst_continuation(
            source,
            wrong_audit,
            tmp_path / "must-not-exist",
            plan_path,
        )
    assert not (tmp_path / "must-not-exist").exists()


def test_exact_sstm_runtime_libraries_are_inserted_fail_closed():
    libraries = (
        'libs ("libTmrSSTm.so" "libTmrSSTmKOnlyLimiter.so" '
        '"libTmrSSTmExactProduction.so");'
    )
    assert add_runtime_libraries("libs ();\nfunctions\n{\n}\n").startswith(libraries)
    assert add_runtime_libraries("functions\n{\n    libs (forces);\n}\n").startswith(
        libraries
    )
    with pytest.raises(ValueError, match="top-level runtime libraries"):
        add_runtime_libraries('libs ("existing.so");\nfunctions\n{\n}\n')
    with pytest.raises(ValueError, match="top-level functions"):
        add_runtime_libraries("application simpleFoam;\n")


def test_compressible_plan_preserves_mach_reynolds_and_velocity():
    root = Path(__file__).resolve().parents[1]
    plan = json.loads(
        (
            root
            / "cfd"
            / "naca0012-exact-sstm-compressible-from-incompressible-plan-v1.json"
        ).read_text()
    )
    thermo = plan["declared_changes"]["thermodynamics"]
    gas_constant = 8314.46261815324 / thermo["molecular_weight_kg_kmol"]
    acoustic_speed = (thermo["gamma"] * gas_constant * thermo["temperature_k"]) ** 0.5
    assert thermo["velocity_m_s"] / acoustic_speed == pytest.approx(0.15)
    assert (
        thermo["density_kg_m3"]
        * thermo["velocity_m_s"]
        / thermo["dynamic_viscosity_pa_s"]
    ) == pytest.approx(6000174.825174825)
    assert plan["execution"]["gpu"] is False


def test_compressible_residual_gate_uses_all_six_equations():
    rows = []
    for _ in range(100):
        for name in ("Ux", "Uy", "e", "p", "omega", "k"):
            value = 2e-5 if name == "e" else 1e-6
            prefix = "for " if name in {"e", "p"} else ""
            rows.append(
                f"Solving {prefix}{name}, Initial residual = {value}, "
                "Final residual = 1e-9, No Iterations 1"
            )
    _, recent, passed = compressible_residuals("\n".join(rows), 100)
    assert recent["e"] == 2e-5
    assert passed is False


def test_compressible_builder_rejects_unpinned_audit(tmp_path):
    root = Path(__file__).resolve().parents[1]
    plan_path = (
        root
        / "cfd"
        / "naca0012-exact-sstm-compressible-from-incompressible-plan-v1.json"
    )
    plan = json.loads(plan_path.read_text())
    wrong_audit = tmp_path / "wrong-audit.json"
    wrong_audit.write_text("{}\n")
    with pytest.raises(ValueError, match="Source audit .*does not match"):
        build_exact_sstm_compressible(
            root / plan["source"]["case"],
            wrong_audit,
            tmp_path / "must-not-exist",
            plan_path,
        )
    assert not (tmp_path / "must-not-exist").exists()
