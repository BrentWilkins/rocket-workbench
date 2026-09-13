import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from package_d12_review import PARTS, PROJECT, digest, verify_print_sources


@pytest.fixture
def export(tmp_path):
    cad = tmp_path/'cad'
    cad.mkdir()
    for name in PARTS:
        (cad/(name+'.stl')).write_bytes(name.encode())
    (tmp_path/PROJECT).write_bytes(b'project fixture, not a real 3MF')
    record = dict(source_run='fixture', project_sha256=digest(tmp_path/PROJECT),
                  parts={p.name:digest(p) for p in cad.iterdir()})
    (tmp_path/'manifest.json').write_text(json.dumps(record))
    return tmp_path, cad, record


def test_matching_source_hashes(export):
    folder, cad, record = export
    assert verify_print_sources(folder, cad, 'fixture') == record


def test_missing_mesh_manifest_rejected(export):
    folder, cad, record = export
    record['parts'] = {}
    (folder/'manifest.json').write_text(json.dumps(record))
    with pytest.raises(ValueError, match='six expected'):
        verify_print_sources(folder, cad, 'fixture')


def test_changed_mesh_rejected(export):
    folder, cad, _ = export
    (cad/'nose-bay.stl').write_bytes(b'changed')
    with pytest.raises(ValueError, match='Print mesh differs'):
        verify_print_sources(folder, cad, 'fixture')


def test_wrong_simulation_source_rejected(export):
    folder, cad, _ = export
    with pytest.raises(ValueError, match='different simulation'):
        verify_print_sources(folder, cad, 'other')


def test_changed_project_rejected(export):
    folder, cad, _ = export
    (folder/PROJECT).write_bytes(b'changed')
    with pytest.raises(ValueError, match='changed after export'):
        verify_print_sources(folder, cad, 'fixture')
