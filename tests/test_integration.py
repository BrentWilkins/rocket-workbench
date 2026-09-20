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


def test_multilevel_wind_seed_and_vector_conventions(engine):
    from rocket_workbench.robustness import configure_wind, scenarios
    from types import SimpleNamespace

    case = scenarios()[-1]
    def wind(seed):
        options = engine.core.simulation.SimulationOptions()
        sim = SimpleNamespace(getOptions=lambda: options)
        configure_wind(engine, sim, dict(case, seed=seed))
        return options.getMultiLevelWindModel().clone()

    first, repeated, different = wind(123), wind(123), wind(456)
    def velocities(model):
        return np.array([[v.x,v.y] for t,h in [(0,0),(.2,15),(1,87),(2,180)]
                         for v in [model.getWindVelocity(t,1600+h,h)]])
    a, b, c = map(velocities, (first,repeated,different))
    assert a == pytest.approx(b, abs=1e-12)
    assert not np.allclose(a,c,atol=1e-5)
    # Native vector is opposing air velocity, not physical wind-TOWARD.
    assert np.all(a[:,0]<0)
    assert np.all(np.abs(a[:,1])<1e-10)


@pytest.mark.parametrize('platform', ['24-cd', '24-e'])
def test_native_24mm_motor_identity_mass_and_saved_model(engine, tmp_path, platform):
    import sys
    sys.path.insert(0, str(ROOT/'scripts'))
    from study_motor24 import configuration
    config = configuration(platform, 'nominal')
    parts = {name: dict(mass_g=10, cg_x_mm=150) for name in
             ['nose-bay', 'bay-bulkhead', 'payload-sled', 'fin-collar', 'lug-sleeve-1', 'lug-sleeve-2']}
    path = tmp_path/'input.ork'
    expected = generate(config, parts, 'actual', path)
    doc, warnings = engine.load(path)
    assert not warnings
    sim = engine.new_simulation(doc)
    # Select the last motor/delay, not just the first one embedded in the XML.
    selected = config.motors[-1]
    record = engine.motor(sim, selected, config)
    assert record['digest'] == selected.digest
    assert record['diameter_mm'] == 24
    assert record['length_mm'] == selected.dimensions_mm[1]
    mass = engine.mass(sim)
    assert mass['dry_mass_g'] == pytest.approx(expected['dry_mass_g'], abs=.05)
    assert mass['launch_mass_g']-mass['dry_mass_g'] == pytest.approx(record['loaded_mass_g'], abs=.05)
    saved = tmp_path/'saved.ork'
    engine.save(doc, saved)
    reloaded, warnings = engine.load(saved)
    assert not warnings
    mount = list(reloaded.getSimulation(0).getActiveConfiguration().getActiveMotors())[0]
    assert str(mount.getMotor().getDigest()) == selected.digest
    assert mount.getEjectionDelay() == selected.delay_s
    wrong = selected.model_copy(update={'digest': '0'*32})
    with pytest.raises(ValueError, match='not uniquely available'):
        engine.motor(sim, wrong, config)


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


@pytest.mark.parametrize('shape', ['elliptical', 'clipped-delta', 'swept'])
def test_native_freeform_matches_shared_outline(engine, tmp_path, shape):
    import sys
    sys.path.insert(0, str(ROOT/'scripts'))
    from study_fin_shapes import variant
    from rocket_workbench.fins import outline
    config = variant(shape, 45, 410)
    parts = {name: dict(mass_g=10, cg_x_mm=150) for name in
             ['nose-bay', 'bay-bulkhead', 'payload-sled', 'fin-collar', 'lug-sleeve-1', 'lug-sleeve-2']}
    path = tmp_path/'input.ork'
    generate(config, parts, 'actual', path)
    doc, warnings = engine.load(path)
    assert not warnings
    fins = [c for c in doc.getRocket().iterator() if str(c.getClass().getSimpleName())=='FreeformFinSet']
    assert len(fins)==1
    actual = [(float(p.x)*1000,float(p.y)*1000) for p in fins[0].getFinPoints()]
    assert np.asarray(actual) == pytest.approx(np.asarray(outline(config)))
    assert float(fins[0].getPosition().x) == pytest.approx(0)
    assert fins[0].getFinCount()==3


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
        if name in {'fin-collar', 'payload-sled'}:
            from rocket_workbench.orientation import place
            orientation = 'aft-down' if name == 'fin-collar' else 'side-y-plus'
            expected_z = place(parts[name], orientation).val().Center().z
            data = (tmp_path/f'{name}.stl').read_bytes()
            weighted_z = volume = 0.0
            for i in range(struct.unpack_from('<I', data, 80)[0]):
                row = struct.unpack_from('<12fH', data, 84+i*50)
                tri = np.array(row[3:12]).reshape(3, 3)
                v = np.dot(tri[0], np.cross(tri[1], tri[2]))/6
                volume += v
                weighted_z += v*tri[:, 2].sum()/4
            assert weighted_z/volume == pytest.approx(expected_z, abs=.02)
    # STL orientation regression: fin aft end starts with the full collar wall;
    # sled starts with its broad back. Check mesh slice bounds near Z=0.
    from rocket_workbench.orientation import measure, place
    assert measure(place(parts['fin-collar'], 'aft-down'))['first_layer_average_area_mm2'] > 150
    assert measure(place(parts['payload-sled'], 'side-y-plus'))['first_layer_average_area_mm2'] > 1500
    assert parts['nose-bay'].val().BoundingBox().xlen == pytest.approx(config.geometry.body_od.value)


def test_saddles_have_broad_concave_bonds_and_clear_bores():
    import cadquery as cq
    for filename in ['baseline.yaml', 'candidate-recovery.yaml']:
        config = load_config(ROOT/'examples'/filename)
        guide = launch_guide(config)
        parts = shapes(config)
        angle = math.radians(guide['angle_deg'])
        for index, z in enumerate(guide['starts']):
            part = parts[f'lug-sleeve-{index+1}']
            assert len(part.solids().vals()) == 1
            assert part.val().isValid()
            inner = guide['saddle_inner_radius']
            clearance = cq.Workplane('XY', origin=(0, 0, z)).circle(inner-1e-5).extrude(guide['length'])
            assert part.intersect(clearance).val().Volume() < 1e-5
            contact_shell = (cq.Workplane('XY', origin=(0, 0, z)).circle(inner+.01)
                             .circle(inner).extrude(guide['length']))
            # Thin-shell volume / thickness approximates the concave contact area.
            area = part.intersect(contact_shell).val().Volume()/.01
            assert area == pytest.approx(guide['saddle_bond_area_mm2'], rel=.005)
            assert area > 300
            center = (guide['center_radius']*math.cos(angle), guide['center_radius']*math.sin(angle), z)
            bore = cq.Workplane('XY', origin=center).circle(guide['sleeve_inner_radius']-1e-5).extrude(guide['length'])
            assert part.intersect(bore).val().Volume() < 1e-5


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
            fin = engine.helper.get_component_named(doc.getRocket(), f'{config.fin_count} fins (mass included in collar)')
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


@pytest.mark.parametrize('shape', ['conical', 'ogive', 'ellipsoid'])
def test_nose_profile_survives_engine_reload(engine, tmp_path, shape):
    from rocket_workbench.nose import radius_at
    from rocket_workbench.config import Config
    data = load_config(ROOT/'examples/candidate-recovery.yaml').model_dump()
    data['nose_shape'] = shape
    config = Config.model_validate(data)
    parts = build(config, tmp_path/'cad')
    path = tmp_path/'nose.ork'
    ledger = generate(config, parts, 'actual', path)
    doc, warnings = engine.load(path)
    assert not warnings
    sim = engine.new_simulation(doc)
    engine.save(doc, tmp_path/'saved.ork')
    doc, warnings = engine.load(tmp_path/'saved.ork')
    assert not warnings
    nose = engine.helper.get_component_named(doc.getRocket(), 'Printed nose and bay assembly')
    assert str(nose.getShapeType().name()).lower() == shape
    for x in [0, .01, 1, 10, 35, 69, 70]:
        assert nose.getRadius(x/1000)*1000 == pytest.approx(radius_at(shape, x, 70, 20.8), abs=1e-6)
    assert engine.mass(doc.getSimulation(0))['dry_mass_g'] == pytest.approx(ledger['dry_mass_g'], abs=.05)


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
        metrics = result['metrics']
        assert metrics['powered_data_complete']
        assert metrics['powered_samples'] > 5
        ts = result['timeseries']
        lift = next(e['time_s'] for e in result['events'] if e['type'] == 'LIFTOFF')
        burnout = next(e['time_s'] for e in result['events'] if e['type'] == 'BURNOUT')
        samples = [i for i, t in enumerate(ts['time_s']) if lift <= t < burnout and ts['thrust_n'][i] > 0]
        assert metrics['peak_powered_acceleration_g'] == pytest.approx(max(ts['acceleration_m_s2'][i] for i in samples)/9.80665)
        assert metrics['peak_powered_specific_force_estimate_g'] == pytest.approx(max(
            (ts['acceleration_xy_m_s2'][i]**2 + (ts['acceleration_z_m_s2'][i]+ts['gravity_m_s2'][i])**2)**.5
            for i in samples)/9.80665)
        assert lift <= metrics['peak_powered_specific_force_estimate_g_time_s'] < burnout
        records.append(result)
    assert records[0]['timeseries'] == records[2]['timeseries']
    bad_motor = config.motors[0].model_copy(update={'digest':'0'*32})
    with pytest.raises(ValueError, match='not uniquely available'):
        engine.motor(sim, bad_motor, config)
    sim.getOptions().setMaxSimulationTime(.15)
    result = engine.run(sim)
    assert result['execution'] == 'simulation failed'
