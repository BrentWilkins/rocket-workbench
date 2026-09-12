"""Content-addressed run evidence; never imply a missing Git revision exists."""
import hashlib
import json
from pathlib import Path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seal_run(out: Path, record_sources: bool = True):
    root = Path(__file__).resolve().parents[2]
    source_files = [root / n for n in ['pyproject.toml', 'uv.lock', '.python-version']]
    for directory in ['src', 'scripts', 'tests', 'docs']:
        source_files += [p for p in (root/directory).rglob('*')
                         if p.is_file() and p.suffix in {'.py', '.java', '.md', '.yaml'}]
    source = {str(p.relative_to(root)): sha256(p) for p in sorted(source_files) if p.exists()}
    manifest = out/'manifest.json'
    data = json.loads(manifest.read_text()) if manifest.exists() else {'schema_version': 1}
    if record_sources:
        data['source_sha256'] = source
    else:
        # Re-rendering reports must not relabel historical simulation sources.
        data['report_generator_sha256'] = sha256(root/'src/rocket_workbench/report.py')
    data['artifact_sha256'] = {str(p.relative_to(out)): sha256(p)
                for p in sorted(out.rglob('*')) if p.is_file() and p != manifest}
    manifest.write_text(json.dumps(data, indent=2)+'\n')
