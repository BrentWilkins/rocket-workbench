import pytest

from rocket_workbench.orientation import measure, place

pytestmark = pytest.mark.integration


def test_box_orientation_contact_and_no_overhang():
    import cadquery as cq
    box = cq.Workplane('XY').box(10, 20, 30)
    upright = measure(place(box, 'forward-down'))
    side = measure(place(box, 'side-x-plus'))
    assert upright['first_layer_average_area_mm2'] == pytest.approx(200)
    assert upright['height_mm'] == pytest.approx(30)
    assert side['first_layer_average_area_mm2'] == pytest.approx(600)
    assert side['height_mm'] == pytest.approx(10)
    assert upright['downward_area_above_first_layer_mm2'] == pytest.approx(0)


def test_overhanging_shelf_is_detected():
    import cadquery as cq
    post = cq.Workplane('XY').box(2, 2, 10)
    shelf = cq.Workplane('XY', origin=(0, 0, 5)).box(10, 10, 2)
    result = measure(place(post.union(shelf), 'forward-down'))
    assert result['first_layer_average_area_mm2'] == pytest.approx(4)
    assert result['downward_area_above_first_layer_mm2'] == pytest.approx(96)
