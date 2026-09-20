"""Geometry checks for the D12 printable tip revision."""

import cadquery as cq
import pytest

from rocket_workbench.cad import shapes
from rocket_workbench.config import Config
from rocket_workbench.nose import rounded_cone
from scripts.prepare_tip_refinement import refined_config


def test_rounded_cone_preserves_length_and_base_and_is_smooth():
    cone = rounded_cone(50, 20.8, 1).val()
    assert cone.isValid()
    bounds = cone.BoundingBox()
    assert bounds.zmin == pytest.approx(0, abs=1e-5)
    assert bounds.zmax == pytest.approx(50)
    assert bounds.xmax == pytest.approx(20.8)
    # One spherical and one conical side, joined without a gap.
    assert {face.geomType() for face in cone.Faces()} >= {'SPHERE', 'CONE'}


def test_tip_revision_keeps_root_thick_and_narrows_outer_fin():
    config = refined_config()
    parts = shapes(config)
    for name in ('nose-bay', 'fin-collar'):
        assert parts[name].val().isValid()
        assert len(parts[name].solids().vals()) == 1

    g = config.geometry
    fin = parts['fin-collar'].val()
    outer = g.mm('body_od') / 2 + g.mm('clearance') + g.mm('wall')
    tip = outer + g.mm('fin_span')
    axial = g.mm('nose_length') + g.mm('body_length') - g.mm('collar_length')
    axial += .85 * g.mm('fin_root')

    def thickness(radial):
        probe = cq.Workplane('XY').box(.05, 10, .05).translate((radial, 0, axial)).val()
        return fin.intersect(probe).BoundingBox().ylen

    assert thickness(tip - 12) == pytest.approx(2, abs=.02)
    assert thickness(tip - 4) == pytest.approx(1.4, abs=.03)
    assert thickness(tip - .1) == pytest.approx(.8, abs=.04)


def test_legacy_config_has_no_tip_change():
    data = refined_config().model_dump()
    data['fin_profile'] = 'organic-v2'
    data['geometry'].pop('nose_tip_radius')
    data['geometry'].pop('nose_shoulder_chamfer')
    legacy = Config.model_validate(data)
    assert legacy.geometry.nose_tip_radius is None
    assert legacy.geometry.nose_shoulder_chamfer is None


@pytest.mark.parametrize('field,value', [('fin_thickness', .8), ('fin_span', 8)])
def test_tip_taper_rejects_dimensions_smaller_than_its_land(field, value):
    data = refined_config().model_dump()
    data['geometry'][field]['value'] = value
    with pytest.raises(ValueError, match='Organic fin tip taper'):
        Config.model_validate(data)


def test_leading_edge_review_has_slender_front_and_full_midchord():
    data = refined_config().model_dump()
    data['fin_profile'] = 'organic-v4'
    config = Config.model_validate(data)
    fin = shapes(config)['fin-collar'].val()
    assert fin.isValid()
    assert len(fin.Solids()) == 1
    g = config.geometry
    outer = g.mm('body_od') / 2 + g.mm('clearance') + g.mm('wall')
    radial = outer + g.mm('fin_span') / 2
    leading = g.mm('nose_length') + g.mm('body_length') - g.mm('collar_length')
    leading += .4 * g.mm('fin_root')

    def thickness(chord_offset):
        probe = cq.Workplane('XY').box(.05, 10, .05).translate((radial, 0, leading + chord_offset)).val()
        return fin.intersect(probe).BoundingBox().ylen

    assert thickness(.1) < 1.0
    assert thickness(4.5) == pytest.approx(2, abs=.02)
    root_z = g.mm('nose_length') + g.mm('body_length') - g.mm('collar_length')
    root_x = outer + 1.0
    assert not fin.isInside(cq.Vector(root_x, 0, root_z + .5), 1e-5)
    assert fin.isInside(cq.Vector(root_x, 0, root_z + 5), 1e-5)
    assert not fin.isInside(cq.Vector(root_x, 0, root_z + g.mm('fin_root') - .5), 1e-5)


def test_print_review_has_uniform_root_and_full_thickness_tip():
    data = refined_config().model_dump()
    data['fin_profile'] = 'organic-v5'
    config = Config.model_validate(data)
    fin = shapes(config)['fin-collar'].val()
    assert fin.isValid() and len(fin.Solids()) == 1
    g = config.geometry
    outer = g.mm('body_od') / 2 + g.mm('clearance') + g.mm('wall')
    root_z = g.mm('nose_length') + g.mm('body_length') - g.mm('collar_length')

    # The root begins below the rim without a separate cutout.
    assert not fin.isInside(cq.Vector(outer + .2, 0, root_z + 1), 1e-5)
    assert fin.isInside(cq.Vector(outer + .2, 0, root_z + 3), 1e-5)

    # An exposed cove station stays the same size along its straight run.
    widths = []
    for offset in (12, 25, 40):
        probe = cq.Workplane('XY').box(.03, 8, .03).translate(
            (outer + .5, 2, root_z + offset)).val()
        widths.append(fin.intersect(probe).BoundingBox().ymax)
    assert max(widths) - min(widths) < .02

    tip_x = outer + g.mm('fin_span') - 1
    leading_z = root_z + 2 + (.8 * g.mm('fin_root') - 2) / g.mm('fin_span') * (tip_x - outer)
    probe = cq.Workplane('XY').box(.05, 10, .05).translate((tip_x, 0, leading_z + 5)).val()
    assert fin.intersect(probe).BoundingBox().ylen == pytest.approx(2, abs=.02)
