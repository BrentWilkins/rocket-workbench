"""Fit and print orientation checks for the manual-fin collar option."""

import pytest

from rocket_workbench.separable_fins import parts, printable_parts
from scripts.prepare_tip_refinement import refined_config


def test_collar_and_fin_are_independent_valid_print_solids():
    config = refined_config()
    collar, fin = parts(config)
    for part in (collar, fin):
        assert part.val().isValid()
        assert len(part.val().Solids()) == 1
    assert collar.val().intersect(fin.val()).Volume() == pytest.approx(0, abs=1e-5)

    printable_collar, printable_fin = printable_parts(config)
    assert printable_collar.val().BoundingBox().zmin == pytest.approx(0, abs=1e-5)
    assert printable_fin.val().BoundingBox().zmin == pytest.approx(0, abs=1e-5)
    assert printable_fin.val().BoundingBox().zlen == pytest.approx(
        config.geometry.mm('fin_thickness'), abs=1e-5)
