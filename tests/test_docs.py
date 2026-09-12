"""Documentation must build from curated evidence without local simulation runs."""

import importlib.util
from pathlib import Path


def test_prepare_uses_snapshot_and_preserves_relative_links(tmp_path):
    script = Path(__file__).resolve().parents[1] / "scripts/prepare_docs.py"
    spec = importlib.util.spec_from_file_location("prepare_docs", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = tmp_path
    (tmp_path / "docs").mkdir()
    (tmp_path / "plots").mkdir()
    (tmp_path / "README.md").write_text("# Readme")
    (tmp_path / "ROCKET_PROJECT_BRIEF.md").write_text("# Brief")
    (tmp_path / "docs/HOME.md").write_text("# Home")
    (tmp_path / "docs/REVIEW.md").write_text("[Report](../runs/example/report.md)")
    evidence = tmp_path / "docs-evidence/runs/example"
    evidence.mkdir(parents=True)
    (evidence / "report.md").write_text("[Data](results.csv)")
    (evidence / "results.csv").write_text("apogee_m\n123\n")
    module.prepare()
    assert not (tmp_path / "runs").exists()
    assert (tmp_path / "_site_docs/runs/example/results.csv").read_text() == "apogee_m\n123\n"
    assert (tmp_path / "_site_docs/index.md").read_text() == "# Home"
