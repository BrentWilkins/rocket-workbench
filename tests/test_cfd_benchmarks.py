import hashlib
import sys
from pathlib import Path

import pytest


sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))

from cfd_fetch_benchmarks import SOURCES, verified_payload


def test_benchmark_sources_are_pinned_and_uniquely_named():
    assert len(SOURCES) == 23
    assert SOURCES['naca0012-grids.zip']['sha256'] == (
        'b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4'
    )
    assert SOURCES['flatplategrids-grids.zip']['sha256'] == (
        '4b0a64c2c1648f696f92bf9a91e64e972e6c32e76e8daa70ffa65ed8dd641412'
    )
    assert 'sst-cf_cfl3d.dat' in SOURCES
    assert 'sst-upyp_cfl3d.dat' in SOURCES
    assert SOURCES['n0012clcd_cfl3d_sa.dat']['sha256'] == (
        'b07afec6ce3ae4bf2f2d1a1d53785fde0a5ca68481a0d4186aa92754d811944e'
    )
    assert 'n0012cp_cfl3d_sa.dat' in SOURCES
    assert 'n0012cf_cfl3d_sa.dat' in SOURCES
    assert SOURCES['openfoam-naca0012-CD-Alpha.png']['sha256'] == (
        '94003df0353e2c2056fcfb1f733ce7ab0aa4848196c4d36770f74804818df512'
    )
    assert SOURCES['openfoam-naca0012-CP-xc-Alpha-0.png']['sha256'] == (
        '85d15763aecf0de7be9eaec843f1080b2c6c7b63ba9146e773027b69467cb985'
    )
    assert SOURCES['openfoam-naca0012-CF-xc-Alpha-0.png']['sha256'] == (
        '94614a52b792ff32c95008e3e260fe12ee1c0d7c13a75f51eaf03e735accc3ba'
    )
    assert all(name.endswith(('.dat','.zip','.pdf','.inp','.png')) for name in SOURCES)
    assert all(source['url'].startswith(('https://tmbwg.github.io/','https://www.nasa.gov/','https://ntrs.nasa.gov/','https://gitlab.com/openfoam/'))
               for source in SOURCES.values())
    assert all(len(source['sha256']) == 64 for source in SOURCES.values())


def test_benchmark_payload_fails_closed_on_content_drift():
    name=next(iter(SOURCES))
    with pytest.raises(ValueError,match='source mismatch'):
        verified_payload(name,b'changed upstream data')


def test_benchmark_payload_accepts_declared_content(monkeypatch):
    payload=b'pinned data'
    source={'url':'https://tmbwg.github.io/example.dat','bytes':len(payload),
            'sha256':hashlib.sha256(payload).hexdigest(),'role':'test'}
    monkeypatch.setitem(SOURCES,'example.dat',source)
    assert verified_payload('example.dat',payload)['filename'] == 'example.dat'
