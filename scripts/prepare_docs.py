"""Stage documentation and its explicitly linked evidence; never rerun physics."""

import argparse
import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\(([^\s)]+)\)")

# Explicit release inventory: future studies must be promoted deliberately.
CURRENT_RUNS = {
    "recovery-wide-summary-20260913",
    "ring-tail-geometry-step-20260913",
    "sourced-chute-corrected-20260913",
    "cfd-grid-comparison-20260913",
    "fin-shapes-20260913",
    "fin-orientation-20260913",
    "fin-stress-20260913",
    "fin-recovery-20260913",
    "cfd-pilot-audit-20260913",
    "fin-recovery-stress-summary-20260913",
    "motor24-bt60-20260913",
    "avionics-geometry-20260913-corrected",
    "avionics-finalist-stress-20260913",
    "avionics-baseline-stress-20260913",
    "avionics-selected-20260913",
    "avionics-orientation-20260913",
}
ARCHIVE_PAGES = {
    "docs/REVIEW.md", "docs/PLOTS.md", "docs/NOSE_STUDY.md",
    "docs/PRINT_ORIENTATION.md", "docs/POWERED_FLIGHT.md", "docs/LUG_SADDLES.md",
    "docs/AVIONICS.md", "docs/SHOPPING_LEGACY.md", "docs/PROGRESS_LEGACY.md",
    "ROCKET_PROJECT_BRIEF.md",
}


def archive_page(relative):
    return relative.as_posix() in ARCHIVE_PAGES or (
        relative.parts[0] == "runs" and relative.parts[1] not in CURRENT_RUNS
    )


def publication_markdown(relative, content):
    """Label old deep links too, without modifying sealed source evidence."""
    if not archive_page(relative):
        return content
    title = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title:
        content = content[:title.start()] + "# Archived — " + content[title.start() + 2:]
    current = posixpath.relpath("docs/CURRENT_DESIGN.md", relative.parent.as_posix())
    archive = posixpath.relpath("docs/ARCHIVE.md", relative.parent.as_posix())
    notice = (
        "> **ARCHIVED / SUPERSEDED — not current design or purchase guidance.**\n"
        f"> See [current designs]({current}) or the [archive index]({archive}).\n"
        "> Old dimensions, altitude gates, pass counts and downloads below are retained only for provenance.\n\n"
    )
    return "---\nsearch:\n  exclude: true\n---\n\n" + notice + content


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


def prepare(snapshot=False, snapshot_runs=()):
    stage = ROOT / "_site_docs"
    # This fixed generated directory is disposable; stale pages must not leak into releases.
    if stage.is_symlink():
        raise ValueError("Refusing to replace a symlinked documentation staging directory")
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir()
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
        refresh_run = is_run and (snapshot or relative.parts[1] in snapshot_runs)
        source = logical if not is_run or refresh_run else evidence / relative
        if not source.is_file():
            raise FileNotFoundError(f"Missing documentation input: {source}")
        if refresh_run:
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
            target.write_text(publication_markdown(relative, target.read_text()))
    (stage / 'index.md').write_text(home_at_site_root((stage / 'docs' / 'HOME.md').read_text()))
    print(f"Staged {len(seen)} files in {stage}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", action="store_true", help="Refresh linked evidence from local runs")
    parser.add_argument("--snapshot-run", action="append", default=[],
                        help="Refresh only linked evidence in this named run; leave historical snapshots unchanged")
    args = parser.parse_args()
    prepare(args.snapshot, args.snapshot_run)
