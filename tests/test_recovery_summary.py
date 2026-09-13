import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from summarize_recovery_stress import summarize
from summarize_wide_recovery import drift_bounds


def test_duplicate_mass_profiles_rejected(tmp_path):
    row = dict(design='test', upper=False, mount_factor=1)
    (tmp_path/'comparison.json').write_text(json.dumps([row, row]))
    with pytest.raises(ValueError, match='Overlapping'):
        summarize([tmp_path])


def test_missing_profiles_rejected(tmp_path):
    (tmp_path/'comparison.json').write_text(json.dumps([
        dict(design=name, upper=False, mount_factor=1) for name in ['a','b','c']]))
    with pytest.raises(ValueError, match='Incomplete uncertainty profiles'):
        summarize([tmp_path])


def test_declared_design_inventory_rejected_when_missing(tmp_path):
    (tmp_path/'comparison.json').write_text(json.dumps([
        dict(design='a', upper=False, mount_factor=1)]))
    with pytest.raises(ValueError, match='declared study inventory'):
        summarize([tmp_path], expected_designs=['a', 'b'])


def test_single_declared_design_still_requires_all_profiles(tmp_path):
    (tmp_path/'comparison.json').write_text(json.dumps([
        dict(design='a', upper=False, mount_factor=1)]))
    with pytest.raises(ValueError, match='Incomplete uncertainty profiles'):
        summarize([tmp_path], expected_designs=['a'])


def test_drift_requires_complete_logger_evidence(tmp_path):
    (tmp_path/'results.json').write_text(json.dumps({'cases': []}))
    row = {'profiles': [dict(source_study=str(tmp_path), report='report.md')]}
    with pytest.raises(ValueError, match='24 logger cases'):
        drift_bounds(row)
