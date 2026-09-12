from collections import Counter
import hashlib
import math
from pathlib import Path
import struct
import xml.etree.ElementTree as ET

import numpy as np
import pytest

from rocket_workbench.config import load_config
from rocket_workbench.cad import build, shapes
from rocket_workbench.flight_model import generate
from rocket_workbench.simulator import Engine
from rocket_workbench.sweep import variant
from rocket_workbench.interfaces import launch_guide

pytestmark = pytest.mark.integration
ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope='module')
def engine():
    with Engine() as engine:
        yield engine


def mesh_volume(path):
    data = path.read_bytes()
    count = struct.unpack_from('<I', data, 80)[0]
    assert len(data) == 84+50*count
    edges = Counter()
    volume = 0
    for i in range(count):
        row = struct.unpack_from('<12fH', data, 84+i*50)
        points = np.array(row[3:12]).reshape(3, 3)
        volume += np.dot(points[0], np.cross(points[1], points[2]))/6
        vertices = [tuple(np.round(p, 5)) for p in points]
        for a, b in [(0, 1), (1, 2), (2, 0)]:
            if vertices[a] != vertices[b]:
                edges[tuple(sorted([vertices[a], vertices[b]]))] += 1
    assert set(edges.values()) == {2}, 'Exported mesh has a hole or nonmanifold edge'
    return abs(volume)


def test_cad_meshes_and_assembly_clearances(tmp_path):
    config = load_config(ROOT/'examples/baseline.yaml')
    parts = shapes(config)
    for name, shape in parts.items():
        assert shape.val().isValid()
        for other, second in parts.items():
            if name < other:
                assert shape.intersect(second).val().Volume() < 1e-5, (name, other)
    records = build(config, tmp_path)
    import cadquery as cq
    guide = launch_guide(config)
    angle = math.radians(guide['angle_deg'])
    center = (guide['center_radius']*math.cos(angle), guide['center_radius']*math.sin(angle), 0)
    rod = cq.Workplane('XY', origin=center).circle(guide['rod_radius']).extrude(600)
    assert guide['collar_rod_gap'] >= .75
    for name, part in parts.items():
        assert rod.intersect(part).val().Volume() < 1e-5, name
    for name, record in records.items():
        assert mesh_volume(tmp_path/f'{name}.stl') == pytest.approx(record['volume_mm3'], rel=.003)
        reloaded = cq.importers.importStep(str(tmp_path/f'{name}.step')).val()
        assert reloaded.Volume() == pytest.approx(record['volume_mm3'], rel=1e-6)
    assert parts['nose-bay'].val().BoundingBox().xlen == pytest.approx(config.geometry.body_od.value)


def test_changed_geometry_mass_and_reload(engine, tmp_path):
    base = load_config(ROOT/'examples/baseline.yaml')
    for config in [base, variant(base, {'body_length':340, 'fin_span':45}, 'test')]:
        out = tmp_path/str(config.geometry.body_length.value)
        out.mkdir()
        parts = build(config, out/'cad')
        for loading in ['empty', 'dummy', 'actual']:
            path = out/f'{loading}.ork'
            expected = generate(config, parts, loading, path)
            doc, warnings = engine.load(path)
            assert not warnings
            sim = engine.new_simulation(doc)
            mass = engine.mass(sim)
            assert mass['dry_mass_g'] == pytest.approx(expected['dry_mass_g'], abs=.05)
            assert mass['dry_cg_x_mm'] == pytest.approx(expected['dry_cg_x_mm'], abs=.05)
            fin = engine.helper.get_component_named(doc.getRocket(), 'Three fins (mass included in collar)')
            assert fin.getHeight()*1000 == pytest.approx(config.geometry.fin_span.value)
            guide = launch_guide(config)
            lug = engine.helper.get_component_named(doc.getRocket(), 'Launch lug and printed sleeve 1')
            assert lug.getOuterRadius()*1000 == pytest.approx(guide['sleeve_outer_radius'])
            assert math.degrees(lug.getAngleOffset()) == pytest.approx(guide['angle_deg'])
            offset = lug.getInstanceOffsets()[0]
            assert math.hypot(offset.y, offset.z)*1000 == pytest.approx(guide['center_radius'])
            engine.save(doc, out/f'{loading}-saved.ork')
            reloaded, warnings = engine.load(out/f'{loading}-saved.ork')
            assert not warnings
            assert engine.mass(reloaded.getSimulation(0))['dry_mass_g'] == pytest.approx(expected['dry_mass_g'], abs=.05)


def test_reference_metrics_repeatability_and_errors(engine):
    reference = ROOT/'examples/upstream-simple.ork'
    assert hashlib.sha256(reference.read_bytes()).hexdigest() == 'f5f4de21acd2279895dfb7376c3353fd4e643b85adbcd034808b1af48f439c21'
    config = load_config(ROOT/'examples/reference.yaml')
    records = []
    for wind in [0, 2, 0]:
        doc, warnings = engine.load(reference)
        assert not warnings
        sim = doc.getSimulation(0)
        engine.configure(sim, config, wind)
        result = engine.run(sim)
        assert result['execution'] == 'completed'
        assert not result['warnings']
        for metric in ['apogee_m', 'guide_departure_m_s', 'deployment_speed_m_s']:
            assert result['metrics'][metric] == pytest.approx(result['engine_summary'][metric], abs=1e-6)
        assert result['metrics']['landing_total_speed_m_s'] == pytest.approx(result['engine_summary']['landing_total_speed_m_s'], abs=1e-6)
        assert result['metrics']['landing_descent_m_s'] <= result['metrics']['landing_total_speed_m_s']+.05
        records.append(result)
    assert records[0]['timeseries'] == records[2]['timeseries']
    bad_motor = config.motors[0].model_copy(update={'digest':'0'*32})
    with pytest.raises(ValueError, match='not uniquely available'):
        engine.motor(sim, bad_motor, config)
    sim.getOptions().setMaxSimulationTime(.15)
    result = engine.run(sim)
    assert result['execution'] == 'simulation failed'
