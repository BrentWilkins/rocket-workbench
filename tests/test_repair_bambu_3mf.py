import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from repair_bambu_3mf import repair


def test_repairs_malformed_compatible_printers_xml():
    source = '<metadata key="compatible_printers" value=""Bambu X1";"Bambu P1""/>'
    assert repair(source) == ''


def test_repairs_every_malformed_metadata_value():
    source = '<metadata key="print_extruder_variant" value=""A";"B""/>'
    assert repair(source) == ''


def test_requires_compatible_printers_metadata():
    with pytest.raises(ValueError):
        repair('<config/>')
