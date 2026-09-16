"""Fetch pinned public CFD benchmark inputs without overwriting retained data."""

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


SOURCES = {
    'flatplategrids-grids.zip': {
        'url': 'https://www.nasa.gov/wp-content/uploads/2026/02/flatplategrids-grids.zip',
        'bytes': 16445241,
        'sha256': '4b0a64c2c1648f696f92bf9a91e64e972e6c32e76e8daa70ffa65ed8dd641412',
        'role': 'Official TMR five-level exactly nested flat-plate grid family',
    },
    'naca0012-grids.zip': {
        'url': 'https://www.nasa.gov/wp-content/uploads/2026/02/naca0012-grids.zip',
        'bytes': 110097999,
        'sha256': 'b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4',
        'role': 'Official TMR five-level exactly nested NACA 0012 validation grids',
    },
    'n0012_cfl3d_typical_sst.inp': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/n0012_cfl3d_typical_sst.inp',
        'bytes': 6060,
        'sha256': 'e3d1b4e7c9600d03f90e5e6b5cd7a10d01ad041f704e3d60de4cacd57cb375a4',
        'role': 'Official TMR typical CFL3D SST input, including nondimensional freestream turbulence values',
    },
    'n0012clcd_cfl3d_sst.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/n0012clcd_cfl3d_sst.dat',
        'bytes': 417,
        'sha256': '373dc142018816628b7b53ad278327db731162988ba35a166cd9fdc131a7fd7a',
        'role': 'Official TMR CFL3D SST force-coefficient comparison output',
    },
    'n0012cp_cfl3d_sst.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/n0012cp_cfl3d_sst.dat',
        'bytes': 48141,
        'sha256': '378f9dcd058ffbe900081f213ee5c7e24dfaec0d6a9e02f366f96e8d76bf179d',
        'role': 'Official TMR CFL3D SST surface-pressure comparison output',
    },
    'n0012cf_cfl3d_sst.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/n0012cf_cfl3d_sst.dat',
        'bytes': 37962,
        'sha256': 'd8001cd09d0c573de63475f8e0e02a2a989216133af74b84876eba5c328da8be',
        'role': 'Official TMR CFL3D SST surface-skin-friction comparison output',
    },
    'n0012clcd_cfl3d_sa.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/n0012clcd_cfl3d_sa.dat',
        'bytes': 354,
        'sha256': 'b07afec6ce3ae4bf2f2d1a1d53785fde0a5ca68481a0d4186aa92754d811944e',
        'role': 'Official TMR CFL3D Spalart-Allmaras force-coefficient comparison output',
    },
    'n0012cp_cfl3d_sa.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/n0012cp_cfl3d_sa.dat',
        'bytes': 48082,
        'sha256': '2f1231eba6a7da0e988a6954ac34f2f420ff59a5e24fca331110f980cd881dd2',
        'role': 'Official TMR CFL3D Spalart-Allmaras surface-pressure comparison output',
    },
    'n0012cf_cfl3d_sa.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/n0012cf_cfl3d_sa.dat',
        'bytes': 37903,
        'sha256': 'e7372151e535d3f89c2eb8b8260a1e69e6b6681bb33aacdd677967ad5403ba5e',
        'role': 'Official TMR CFL3D Spalart-Allmaras surface-skin-friction comparison output',
    },
    'nasa-tm-4074.pdf': {
        'url': 'https://ntrs.nasa.gov/api/citations/19880019495/downloads/19880019495.pdf',
        'bytes': 11348135,
        'sha256': '8e466706cbdf54b3c778ea2b089c4f52d87686bf7f6b1bd10d224b42c2d06902',
        'role': 'Primary NACA 0012 force and quarter-chord moment tables at matched Mach and Reynolds number',
    },
    'sst-cf_cfl3d.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/FlatPlate_validation/sst-cf_cfl3d.dat',
        'bytes': 6353,
        'sha256': 'd694caf86c8886ad40016f63e76f738e2c8caa982437ba2a1074d5d58efc2109',
        'role': 'Official TMR CFL3D SSTm wall-skin-friction comparison output',
    },
    'sst-upyp_cfl3d.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/FlatPlate_validation/sst-upyp_cfl3d.dat',
        'bytes': 13627,
        'sha256': '2c9715357a45fc792b24ee45c0f2add71ee2e1f54eafd94c38ecdcf53cc34316',
        'role': 'Official TMR CFL3D SSTm law-of-wall comparison output at Re-theta 10000',
    },
    'n0012points_superbig_clust_fix.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_grids/n0012points_superbig_clust_fix.dat',
        'bytes': 824246,
        'sha256': '74e147db4fa052be7ab79465a756c55b39b1786bfd7141a86257e89586728ae1',
        'role': 'Exact corrected TMR altered NACA 0012 surface points',
    },
    'CLCD_Ladson_expdata.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/CLCD_Ladson_expdata.dat',
        'bytes': 1343,
        'sha256': '78cd2f6aa4968e80f44cbf6c96f699bd9c6e45681d958ec528a10cf72ed23357',
        'role': 'Tripped NACA 0012 lift and drag data, Re=6 million, M=0.15',
    },
    'CP_Gregory_expdata.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/CP_Gregory_expdata.dat',
        'bytes': 1608,
        'sha256': '38d8474bc67661c3cef5e4cd9eeddb95d4a436d06abc1f58a8518066f510647c',
        'role': 'NACA 0012 pressure data, Re=2.88 million; match source conditions before comparison',
    },
    'CP_Ladson.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/NACA0012_validation/CP_Ladson.dat',
        'bytes': 6331,
        'sha256': '547e022634a360cd7697813543348cd447ee0038cdbc8f00a5296c7822ec7af8',
        'role': 'NACA 0012 pressure data, Re=6 million, M=0.3, free transition; match source conditions before comparison',
    },
    'retheta_variation_typical.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/FlatPlate_validation/retheta_variation_typical.dat',
        'bytes': 14936,
        'sha256': 'ea563b33fd85a3ab93b1063a74c2f65f10af22189eca2807aa3ce508f83797a7',
        'role': 'TMR flat-plate Re-theta post-processing reference',
    },
    'cf_K-S.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/FlatPlate_validation/cf_K-S.dat',
        'bytes': 4224,
        'sha256': 'bafbaf7fa7969a945a5ad0935ca90c320ab72f14ba5a08474abffa61356bba2d',
        'role': 'TMR Karman-Schoenherr skin-friction reference',
    },
    'u_plus_y_plus.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/FlatPlate_validation/u%2By%2B.dat',
        'bytes': 137104,
        'sha256': '314dc0b5e4aa666ee88ac507eeda8cbeaacc1279057d10430748231264277bcb',
        'role': 'TMR Coles and van-Driest law-of-wall reference at Re-theta=10000',
    },
    'cf_as_function_of_x.dat': {
        'url': 'https://tmbwg.github.io/turbmodels/FlatPlate_validation/cf_as_function_of_x.dat',
        'bytes': 183312,
        'sha256': '97d01033550468819a0f081fee37fc1836ff12a4ad8318f0a80cdc847625a8e2',
        'role': 'TMR flat-plate experimental comparison with plotted 5 percent error bars',
    },
    'openfoam-naca0012-CD-Alpha.png': {
        'url': 'https://gitlab.com/openfoam/documentation/-/raw/4b7889154eb5ed4aaffb4d269055083c364a8286/content/examples/verification-validation/turbulent/naca0012/CD-Alpha.png',
        'bytes': 26050,
        'sha256': '94003df0353e2c2056fcfb1f733ce7ab0aa4848196c4d36770f74804818df512',
        'role': 'Official OpenFOAM documentation drag-versus-angle plot used to recover the plotted alpha-zero OpenFOAM control point',
    },
    'openfoam-naca0012-CP-xc-Alpha-0.png': {
        'url': 'https://gitlab.com/openfoam/documentation/-/raw/4b7889154eb5ed4aaffb4d269055083c364a8286/content/examples/verification-validation/turbulent/naca0012/CP-xc-Alpha-0.png',
        'bytes': 24940,
        'sha256': '85d15763aecf0de7be9eaec843f1080b2c6c7b63ba9146e773027b69467cb985',
        'role': 'Official OpenFOAM alpha-zero surface-pressure comparison plot',
    },
    'openfoam-naca0012-CF-xc-Alpha-0.png': {
        'url': 'https://gitlab.com/openfoam/documentation/-/raw/4b7889154eb5ed4aaffb4d269055083c364a8286/content/examples/verification-validation/turbulent/naca0012/CF-xc-Alpha-0.png',
        'bytes': 21929,
        'sha256': '94614a52b792ff32c95008e3e260fe12ee1c0d7c13a75f51eaf03e735accc3ba',
        'role': 'Official OpenFOAM alpha-zero surface-skin-friction comparison plot',
    },
}


def verified_payload(name: str, payload: bytes) -> dict:
    expected=SOURCES[name]
    digest=hashlib.sha256(payload).hexdigest()
    if len(payload) != expected['bytes'] or digest != expected['sha256']:
        raise ValueError(
            f'Benchmark source mismatch for {name}: got {len(payload)} bytes and {digest}'
        )
    return dict(expected, filename=name)


def fetch(output: Path):
    output.mkdir(parents=True,exist_ok=False)
    records=[]
    for name,source in SOURCES.items():
        with urllib.request.urlopen(source['url'],timeout=30) as response:
            payload=response.read()
        records.append(verified_payload(name,payload))
        (output/name).write_bytes(payload)
    manifest={
        'retrieved_at': datetime.now(timezone.utc).isoformat(),
        'source_index': 'https://tmbwg.github.io/turbmodels/',
        'files': records,
        'accepted_for_design': False,
    }
    (output/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    fetch(args.output)


if __name__ == '__main__':
    main()
