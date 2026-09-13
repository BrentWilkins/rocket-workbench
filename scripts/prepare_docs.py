"""Stage documentation and its explicitly linked evidence; never rerun physics."""

import argparse
import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\(([^\s)]+)\)")


def home_at_site_root(content):
    """HOME lives in docs/ but is also rendered as the site-root index."""
    def rebase(match):
        url = urlsplit(match[1])
        if url.scheme or url.netloc or not url.path or url.path.startswith('/'):
            return match[0]
        return '](' + url._replace(path=posixpath.normpath('docs/'+url.path)).geturl() + ')'
    return LINK.sub(rebase, content)


def linked_files(path):
    if path.suffix != ".md":
        return
    for match in LINK.finditer(path.read_text()):
        url = urlsplit(match[1])
        if url.scheme or url.netloc or not url.path:
            continue
        target = (path.parent / unquote(url.path)).resolve()
        if not target.is_relative_to(ROOT):
            raise ValueError(f"Link escapes repository: {path}: {match[1]}")
        yield target


def prepare(snapshot=False):
    stage = ROOT / "_site_docs"
    evidence = ROOT / "docs-evidence"
    sources = list((ROOT / "docs").rglob("*.md"))
    sources += list((ROOT / "docs").glob("*.yaml"))
    sources += [path for path in (ROOT / "docs" / "assets").rglob("*") if path.is_file()]
    sources += list((ROOT / "plots").glob("*.svg"))
    sources += [ROOT / "README.md", ROOT / "ROCKET_PROJECT_BRIEF.md"]
    pending = sources[:]
    seen = set()
    while pending:
        logical = pending.pop()
        if logical in seen:
            continue
        seen.add(logical)
        relative = logical.relative_to(ROOT)
        is_run = relative.parts[0] == "runs"
        source = logical if not is_run or snapshot else evidence / relative
        if not source.is_file():
            raise FileNotFoundError(f"Missing documentation input: {source}")
        if is_run and snapshot:
            destination = evidence / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        target = stage / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        # Resolve links using the logical path, not the snapshot's extra prefix.
        if source.suffix == ".md":
            for linked in linked_files(target):
                pending.append(ROOT / linked.relative_to(stage))
    (stage / 'index.md').write_text(home_at_site_root((stage / 'docs' / 'HOME.md').read_text()))
    print(f"Staged {len(seen)} files in {stage}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", action="store_true", help="Refresh linked evidence from local runs")
    prepare(parser.parse_args().snapshot)
