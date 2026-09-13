"""Verify retained artifact hashes without relabeling historical source versions."""
import argparse
import hashlib
import json
from pathlib import Path


def verify(root):
    root=root.resolve(strict=True)
    checked=0
    manifests=sorted(root.rglob('manifest.json'))
    if not manifests:
        raise ValueError('No retained manifests found')
    for manifest in manifests:
        record=json.loads(manifest.read_text())
        artifacts=record.get('artifact_sha256')
        if not artifacts:
            raise ValueError(f'Unsealed or empty manifest: {manifest}')
        for relative,expected in artifacts.items():
            path=(manifest.parent/relative).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                raise ValueError(f'Missing or out-of-scope artifact: {relative}')
            with path.open('rb') as handle:
                actual=hashlib.file_digest(handle,'sha256').hexdigest()
            if actual!=expected:
                raise ValueError(f'Artifact changed: {path}')
            checked+=1
    return dict(study=str(root),manifests=len(manifests),verified_artifact_references=checked,
                scope='Retained artifact integrity only, not model correctness, current source equivalence or physical validation')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('study',type=Path,nargs='+')
    args=parser.parse_args()
    for study in args.study:
        print(json.dumps(verify(study)),flush=True)


if __name__=='__main__':
    main()
