import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_domain_study import domain_metadata, preserved_inner_grid


def test_preserved_inner_grid_requires_exact_prefix(tmp_path):
    full = tmp_path / "full"
    reduced = tmp_path / "reduced"
    full.mkdir()
    reduced.mkdir()
    x = np.arange(12).reshape(4, 3)
    y = x / 10
    np.savez(full / "tmr-grid.npz", x=x, y=y)
    np.savez(reduced / "tmr-grid.npz", x=x[:3], y=y[:3])
    assert preserved_inner_grid(full, reduced)

    changed = y[:3].copy()
    changed[1, 1] += 1e-12
    np.savez(reduced / "tmr-grid.npz", x=x[:3], y=changed)
    assert not preserved_inner_grid(full, reduced)


def test_domain_metadata_derives_legacy_full_extent(tmp_path):
    case=tmp_path/'legacy'
    case.mkdir()
    y=np.asarray([[0.,0.],[1.,1.]])
    np.savez(case/'tmr-grid.npz',x=y,y=y)
    result=domain_metadata({'case':str(case),'spec':{}})
    assert result['selected_top_y_mean_m'] == 1.0
    assert result['metadata_source'].startswith('derived_')
