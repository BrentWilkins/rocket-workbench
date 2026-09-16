import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_boundary_audit import audit, patch_type, patch_uniform_scalar
from cfd_flat_plate_case import generate


def generate_case(monkeypatch, tmp_path: Path) -> Path:
    x = np.asarray([[-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]])
    y = np.asarray([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
    monkeypatch.setattr(
        "cfd_flat_plate_case.archive_grid",
        lambda archive, ni: (x, y, {
            "archive_sha256": "test", "archive_member": "test",
            "member_crc32": "0", "coordinate_payload_sha256": "test",
        }),
    )
    case = tmp_path / "case"
    generate(
        tmp_path / "ignored.zip", case, ni=69, iterations=10,
        omega_wall="tmr-fixed-factor10",
    )
    return case


def test_patch_type_is_scoped_to_named_patch():
    text = "inlet { type fixedValue; } top { type zeroGradient; }"
    assert patch_type(text, "top") == "zeroGradient"


def test_uniform_scalar_is_scoped_to_named_patch():
    text = "inlet { type fixedValue; value uniform 1.8e-9; } plate { value uniform 0; }"
    assert patch_uniform_scalar(text, "inlet") == 1.8e-9


def test_generated_case_passes_published_boundary_audit(monkeypatch, tmp_path):
    result = audit(generate_case(monkeypatch, tmp_path))
    assert result["manifest_passed"] is True
    assert result["published_boundary_screen"] is True


def test_legacy_fixed_top_is_rejected(monkeypatch, tmp_path):
    case = generate_case(monkeypatch, tmp_path)
    path = case / "0/U"
    path.write_text(path.read_text().replace(
        "top { type zeroGradient; }",
        "top { type fixedValue; value uniform (1 0 0); }",
    ))
    result = audit(case)
    assert result["checks"]["U"]["top"]["passed"] is False
    assert result["published_boundary_screen"] is False


def test_zero_freestream_nut_is_rejected(monkeypatch, tmp_path):
    case = generate_case(monkeypatch, tmp_path)
    path = case / "0/nut"
    path.write_text(path.read_text().replace(
        "inlet { type fixedValue; value uniform 1.8e-09; }",
        "inlet { type fixedValue; value uniform 0; }",
    ))
    result = audit(case)
    assert result["value_checks"]["nut:inlet"]["passed"] is False
    assert result["published_boundary_screen"] is False
