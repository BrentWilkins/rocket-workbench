import json
from pathlib import Path

import pytest

from rocket_workbench.config import load_config
from rocket_workbench.provenance import seal_run, sha256
from rocket_workbench.report import write_report
from rocket_workbench.sweep import variant
from rocket_workbench.uncertainty import StressSpec

ROOT = Path(__file__).resolve().parents[1]


def test_report_build_only_and_manifest(tmp_path):
    (tmp_path/'results.json').write_text(json.dumps(dict(configuration_sha256='test',
        versions={}, missing_inputs=['measure assembly'], criteria=[], cases=[])))
    write_report(tmp_path)
    assert 'no flights were simulated' in (tmp_path/'report.md').read_text()
    assert (tmp_path/'results.csv').read_text().startswith('case,execution,evaluation,')
    seal_run(tmp_path)
    manifest = json.loads((tmp_path/'manifest.json').read_text())
    assert manifest['artifact_sha256']['report.md'] == sha256(tmp_path/'report.md')
    assert manifest['source_sha256']['uv.lock'] == sha256(ROOT/'uv.lock')
    assert 'manifest.json' not in manifest['artifact_sha256']
    manifest['source_sha256'] = {'historical': 'preserve-me'}
    (tmp_path/'manifest.json').write_text(json.dumps(manifest))
    (tmp_path/'report.md').write_text('regenerated report')
    seal_run(tmp_path, record_sources=False)
    refreshed = json.loads((tmp_path/'manifest.json').read_text())
    assert refreshed['source_sha256'] == {'historical': 'preserve-me'}
    assert refreshed['artifact_sha256']['report.md'] == sha256(tmp_path/'report.md')


def test_actual_fixture_and_guide_rejections():
    base = load_config(ROOT/'examples/baseline.yaml')
    with pytest.raises(ValueError, match='launch-lug sleeve overlaps'):
        variant(base, {'body_length':260}, 'test')
    data = base.model_dump()
    data['payload']['width']['value'] = 19
    with pytest.raises(ValueError, match='sled must cover'):
        type(base).model_validate(data)


def test_stress_bounds():
    spec = dict(schema_version=1, print_mass_factors=[1,1.2], payload_cg_offsets_mm=[-5,5],
                chute_cd=[.6,.9], wind_m_s=[0,2,4], max_cases=72, source='test')
    assert StressSpec.model_validate(spec).max_cases == 72
    for key, value in [('print_mass_factors',[2]), ('chute_cd',[float('nan')]), ('wind_m_s',[])]:
        with pytest.raises(ValueError):
            StressSpec.model_validate(dict(spec, **{key:value}))


def test_guideline_catalog_is_explicit():
    import yaml
    catalog = yaml.safe_load((ROOT/'docs/GUIDELINES.yaml').read_text())
    rules = catalog['rules']
    assert len({r['id'] for r in rules}) == len(rules)
    required = {'id', 'rationale', 'source_url', 'source_section', 'applicability',
                'units', 'severity', 'kind', 'manual_inspection'}
    for rule in rules:
        assert required <= rule.keys()
        assert rule['kind'] in {'engineering heuristic', 'enforceable requirement', 'project preference'}
        assert all(rule[k] for k in required-{'manual_inspection'})
