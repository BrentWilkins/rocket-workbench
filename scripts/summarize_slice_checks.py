"""Publish compact native-slicer evidence without local paths or raw G-code."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    rows = []
    for name in ['orientation-fin-forward', 'orientation-fin-aft', 'orientation-sled-old', 'orientation-sled-flat',
                 'x1c-pla-orientation-v3']:
        folder = ROOT/'deliverables'/name
        source = folder/'result.json'
        result = json.loads(source.read_text())
        plate = result['sliced_plates'][0]
        rows.append(dict(name=name, return_code=result['return_code'],
                         total_filament_g=sum(f['total_used_g'] for f in plate['filaments']),
                         predicted_seconds=plate['total_predication'],
                         feature_type_times=plate['feature_type_times'], warning_message=plate['warning_message'],
                         result_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                         project_sha256=hashlib.sha256((folder/'sliced-check.3mf').read_bytes()).hexdigest()))
    output = ROOT/'docs-evidence/orientation-slices.json'
    output.write_text(json.dumps(dict(slicer='Bambu Studio 02.08.02.61',
                                    purpose='Local slice comparison; not physical validation', cases=rows), indent=2)+'\n')
    downloads = ROOT/'docs-evidence/prints'
    downloads.mkdir(exist_ok=True)
    shutil.copy2(ROOT/'deliverables/x1c-pla-orientation-v3/rocket-fit-check-v3.3mf', downloads/'rocket-fit-check-v3.3mf')
    print(output)


if __name__ == '__main__':
    main()
