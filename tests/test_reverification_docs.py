import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_spliced_airframe_is_not_misrepresented_as_the_insert_trial():
    text = (ROOT / "docs/REVERIFICATION.md").read_text()

    assert "two approximately 250 mm tube sections" in text
    assert "not an airframe splice" in text
    assert "does **not** establish a quantified loss" in text


def test_openrocket_primer_marks_model_limits_and_links_reverification():
    text = (ROOT / "docs/OPENROCKET.md").read_text()

    assert "flight-model screen" in text
    assert re.search(r"does not turn (?:a )?detailed STEP solid into\s+a CFD surface", text)
    assert "REVERIFICATION.md" in text
