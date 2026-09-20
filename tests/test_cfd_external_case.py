"""Fail-closed limits for the supplied-exterior visualization adapter."""

import sys
import json
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
pytest.importorskip("cadquery")
from cfd_external_case import prepare
import cfd_external_case
import numpy as np
from cfd_external_audit import normal_diagnostics
import cfd_reconstruct_retained
import cadquery as cq
from rocket_workbench.config import load_config


@pytest.mark.parametrize("kwargs", [
    {"cell_mm": 1}, {"cell_mm": 51}, {"speed": 100}, {"alpha": 11},
    {"iterations": 10}, {"iterations": 3001},
])
def test_exterior_adapter_rejects_unbounded_run_before_creating_files(tmp_path, kwargs):
    output = tmp_path / "case"
    with pytest.raises(ValueError, match="bounds exceeded"):
        prepare(None, tmp_path / "missing.step", output, **kwargs)
    assert not output.exists()


def test_adapter_replaces_template_identity_and_reference(tmp_path, monkeypatch):
    config = load_config(Path(__file__).resolve().parents[1] / "examples/baseline.yaml")
    length = config.geometry.mm("nose_length") + config.geometry.mm("body_length")
    source = tmp_path / "exterior.step"
    cq.exporters.export(cq.Workplane("XY").circle(20).extrude(length), str(source))

    def template(_config, output, *_args):
        output.mkdir()
        (output / "system").mkdir()
        (output / "system/controlDict").write_text("CofR (0.123 0 0);")
        (output / "case-spec.json").write_text(json.dumps({"ring_tail": {"old": True}}))

    monkeypatch.setattr(cfd_external_case, "generate", template)
    monkeypatch.setattr(cfd_external_case, "surface_mesh", lambda *_args: {"triangles": 1})
    output = tmp_path / "case"
    prepare(config, source, output, reference_x_mm=250)
    spec = json.loads((output / "case-spec.json").read_text())
    assert spec["design"] == config.name
    assert spec["geometry_variant"] == "supplied-sealed-exterior"
    assert spec["moment_origin_m"] == [.25, 0, 0]
    assert spec["accepted_for_design"] is False
    assert "ring_tail" not in spec
    assert (output / "external-mm.step").read_bytes() == source.read_bytes()
    assert "CofR (0.25 0 0)" in (output / "system/controlDict").read_text()


def test_exterior_adapter_rejects_wrong_units_or_axis(tmp_path):
    config = load_config(Path(__file__).resolve().parents[1] / "examples/baseline.yaml")
    source = tmp_path / "wrong-units.step"
    cq.exporters.export(cq.Workplane("XY").circle(.02).extrude(.54), str(source))
    output = tmp_path / "case"
    with pytest.raises(ValueError, match="millimetres"):
        prepare(config, source, output)
    assert not output.exists()


def test_serialized_normal_audit_does_not_hide_tiny_reversed_face():
    vertices = np.array([[[0., 0, 0], [1, 0, 0], [0, 1, 0]],
                         [[0., 0, 0], [1e-6, 0, 0], [0, 1e-6, 0]]])
    normals = np.array([[0., 0, 1], [0, 0, -1]])
    result = normal_diagnostics(normals, vertices)
    assert result["stored_normal_winding_mismatches"] == 1
    assert result["negative_normal_winding_count"] == 1
    assert result["mismatch_triangle_area_m2"] == pytest.approx(5e-13)
    assert result["normal_winding_screen_passed"] is False


def test_serialized_normal_audit_rejects_nonfinite_data():
    with pytest.raises(ValueError, match="finite"):
        normal_diagnostics(np.array([[np.nan, 0, 1]]),
                           np.array([[[0., 0, 0], [1, 0, 0], [0, 1, 0]]]))


def test_failed_surface_replacement_withholds_runnable_manifest(tmp_path, monkeypatch):
    config = load_config(Path(__file__).resolve().parents[1] / "examples/baseline.yaml")
    length = config.geometry.mm("nose_length") + config.geometry.mm("body_length")
    source = tmp_path / "exterior.step"
    cq.exporters.export(cq.Workplane("XY").circle(20).extrude(length), str(source))

    def template(_config, output, *_args):
        output.mkdir()
        (output / "case-spec.json").write_text("{}")

    def reject(*_args):
        raise ValueError("surface closure failed")

    monkeypatch.setattr(cfd_external_case, "generate", template)
    monkeypatch.setattr(cfd_external_case, "surface_mesh", reject)
    output = tmp_path / "case"
    with pytest.raises(ValueError, match="closure failed"):
        prepare(config, source, output)
    assert not (output / "case-spec.json").exists()
    assert (output / "template-case-spec.json").exists()


def test_reconstruction_rejects_missing_rank_fields_before_creating_copy(tmp_path, monkeypatch):
    source = tmp_path / "source"
    source.mkdir()
    output = tmp_path / "copy"
    monkeypatch.setattr(sys, "argv", ["cfd_reconstruct_retained", "--case", str(source),
                                      "--output", str(output), "--time", "1000", "--ranks", "8"])
    with pytest.raises(ValueError, match="Missing retained rank 0"):
        cfd_reconstruct_retained.main()
    assert not output.exists()
