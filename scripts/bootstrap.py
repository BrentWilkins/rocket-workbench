"""Explicit online setup step; generation/simulation themselves remain offline."""
import hashlib
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://github.com/openrocket/openrocket/releases/download/release-24.12/OpenRocket-24.12.jar'
SHA = '4959b72f52f5f607941e9722abbb7b7f0c4a38ebbbf84204a329db9f31c4f897'


def main():
    target = ROOT/'.tools/OpenRocket-24.12.jar'
    target.parent.mkdir(exist_ok=True)
    if target.exists():
        if hashlib.sha256(target.read_bytes()).hexdigest() != SHA:
            raise SystemExit('Existing JAR checksum differs; refusing to overwrite it')
        print('Pinned JAR already present and verified')
        return
    with urllib.request.urlopen(URL, timeout=120) as response:
        data = response.read()
    if hashlib.sha256(data).hexdigest() != SHA:
        raise SystemExit('Download checksum mismatch')
    with target.open('xb') as stream:
        stream.write(data)
    print(target)


if __name__ == '__main__':
    main()
