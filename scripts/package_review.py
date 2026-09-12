"""Create a non-overwriting local review bundle, then verify copied evidence.

No publication, installation, purchases or JAR redistribution. Run from the
project venv after the real integration runs listed below have completed.
"""
import argparse
import hashlib
import html
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = [
    '20260912T202256Z-candidate-compact-c137e6e1',
    '20260912T202254Z-candidate-stable-f4dd410f',
    '20260912T192553Z-candidate-recovery-7f53a228',
    'stress-20260912T192230Z-f253babf',
    'stress-20260912T192555Z-b85b3edb',
    'sweep-20260912T192627Z-f956bc56',
    'sweep-20260912T192626Z-59bcc43a',
    'proof-20260912T202227Z-35a8f881',
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plot_altitude(result, target):
    cases = [c for c in result['cases'] if c['loading'] == 'actual' and c['wind_m_s'] == 0]
    # Okabe–Ito Color Universal Design palette, darker subset for white paper.
    # https://jfly.uni-koeln.de/color/#pallet
    # Stable motor mapping plus redundant line patterns, not color-only labels.
    styles = {
        'A8-3': ('#000000', '2 5'),
        'B4-4': ('#CC79A7', '10 5 2 5'),
        'C6-3': ('#0072B2', '10 5'),
        'C6-5': ('#D55E00', '14 4 3 4'),
        'C5-3': ('#009E73', 'none'),
    }
    xmax = max(max(c['timeseries']['time_s']) for c in cases)
    ymax = max(max(c['timeseries']['altitude_m']) for c in cases)*1.1
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 440" role="img" aria-labelledby="plot-title plot-description">',
           '<title id="plot-title">Motor comparison: altitude versus time</title>',
           '<desc id="plot-description">Provisional loaded rocket in zero wind. Motor curves use Okabe–Ito colors and distinct line patterns. Numerical results are in the accompanying report.</desc>',
           '<rect width="760" height="440" fill="white"/>',
           '<style>text{font:13px sans-serif}</style>',
           '<text x="60" y="24">Provisional loaded rocket — wind 0 m/s — altitude versus time</text>']
    for i in range(6):
        x, y = 60+650*i/5, 365-300*i/5
        svg += [f'<path d="M{x} 65 V365 M60 {y} H710" stroke="#ddd"/>',
                f'<text x="{x-10}" y="386">{xmax*i/5:.0f}</text>',
                f'<text x="15" y="{y+4}">{ymax*i/5:.0f}</text>']
    for i, case in enumerate(cases):
        series = case['timeseries']
        points = ' '.join(f'{60+650*t/xmax:.2f},{365-300*a/ymax:.2f}'
                          for t,a in zip(series['time_s'], series['altitude_m']) if a is not None)
        label = f"{case['motor']['designation']}-{case['motor']['delay_s']:g}"
        color, dash = styles[label]
        stroke = f'stroke="{color}" stroke-width="2.4" stroke-dasharray="{dash}"'
        key_x = 60+i*130
        svg += [f'<polyline fill="none" {stroke} points="{points}"><title>{html.escape(label)}</title></polyline>',
                f'<path d="M{key_x} 44 h34" {stroke}/>',
                f'<text x="{key_x+40}" y="48" fill="#222">{html.escape(label)}</text>']
    svg += ['<text x="360" y="410">Time (s)</text><text x="5" y="50">m</text>',
            '<text x="60" y="434">No flight clearance; failures retained. See reports for deployment and warnings.</text></svg>']
    target.write_text('\n'.join(svg))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT/'deliverables'/('review-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    args = parser.parse_args()
    out = args.output.resolve()
    # Fail before copying if required evidence is missing.
    for name in RUNS:
        if not (ROOT/'runs'/name).is_dir():
            raise SystemExit(f'Missing selected run: {name}')
    out.mkdir(parents=True, exist_ok=False)
    for name in ['src', 'scripts', 'tests', 'docs', 'examples']:
        shutil.copytree(ROOT/name, out/name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    for name in ['README.md', 'ROCKET_PROJECT_BRIEF.md', 'pyproject.toml', 'uv.lock', '.python-version', '.gitignore', '.prettierrc.json']:
        shutil.copy2(ROOT/name, out/name)
    for name in RUNS:
        shutil.copytree(ROOT/'runs'/name, out/'runs'/name)
    (out/'plots').mkdir()
    for name in RUNS[:3]:
        result = json.loads((out/'runs'/name/'results.json').read_text())
        plot_altitude(result, out/'plots'/f'{name}.svg')
    test = subprocess.run([sys.executable, '-m', 'pytest', '--run-integration', '-q',
                           f'--junitxml={out / "tests.xml"}'], cwd=ROOT, capture_output=True, text=True)
    (out/'tests.log').write_text(test.stdout+'\n'+test.stderr)
    if test.returncode:
        raise SystemExit(f'Tests failed; evidence retained in {out}')
    # Check each original artifact hash that is present. Historical stress runs
    # without manifests are retained as such, not assigned invented source hashes.
    checked = 0
    for manifest in (out/'runs').rglob('manifest.json'):
        record = json.loads(manifest.read_text())
        for name, expected in record.get('artifact_sha256', {}).items():
            path = manifest.parent/name
            if not path.is_file() or digest(path) != expected:
                raise SystemExit(f'Artifact integrity mismatch: {path}')
            checked += 1
    proof = json.loads((out/'runs'/RUNS[-1]/'evidence.json').read_text())
    if proof['independent_java']['status'] != 'passed':
        raise SystemExit('Independent engine proof did not pass')
    index = ['# Local MVP review package', '',
             'Start with [design findings](docs/REVIEW.md), [build](docs/BUILD.md), [shopping](docs/SHOPPING.md),',
             '[setup/reproduction](README.md), and [physical checks](docs/MEASUREMENTS.md).', '',
             'Generic payload only; no battery selected. No purchases, publication, physical validation or launch clearance.', '',
             '## Flight-profile plots', '']
    index += [f'- [{name}](plots/{name}.svg)' for name in RUNS[:3]]
    index += ['', '## Verification', '', f'- Existing artifact hashes checked: {checked}.',
              '- Real CAD/OpenRocket regression tests: [log](tests.log), [JUnit](tests.xml).',
              '- Independent Java path passed; interactive GUI comparison remains pending.',
              '- `bundle-manifest.json` hashes every included file except itself.',
              '- Dependency binaries are not included; reproduce using the pinned setup instructions.', '']
    (out/'INDEX.md').write_text('\n'.join(index))
    files = {str(p.relative_to(out)): digest(p) for p in sorted(out.rglob('*')) if p.is_file()}
    (out/'bundle-manifest.json').write_text(json.dumps(dict(schema_version=1, files_sha256=files,
        source_root=str(ROOT), selected_runs=RUNS, tests_returncode=test.returncode,
        physical_validation=False, publication=False), indent=2)+'\n')
    print(out)


if __name__ == '__main__':
    main()
