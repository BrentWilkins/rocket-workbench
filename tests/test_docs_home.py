import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_docs import ARCHIVE_PAGES, CURRENT_RUNS, archive_page, home_at_site_root, publication_markdown


def test_home_links_rebased_when_copied_to_site_root():
    assert home_at_site_root('[Current](CURRENT_DESIGN.md#files)') == '[Current](docs/CURRENT_DESIGN.md#files)'
    assert home_at_site_root('[Readme](../README.md)') == '[Readme](README.md)'
    for link in ['[Web](https://example.com/x)', '[Anchor](#local)', '[Absolute](/x)']:
        assert home_at_site_root(link) == link


def test_archived_pages_and_deep_reports_have_notice_and_no_search():
    for path in [*ARCHIVE_PAGES, 'runs/old-study/candidate/report.md']:
        relative = Path(path)
        original = '# Old results\n\n30–120 m; 72/72 passes\n'
        rendered = publication_markdown(relative, original)
        assert rendered.startswith('---\nsearch:\n  exclude: true\n---')
        assert '# Archived — Old results' in rendered
        assert 'ARCHIVED / SUPERSEDED' in rendered
        assert '30–120 m; 72/72 passes' in rendered
        assert 'CURRENT_DESIGN.md' in rendered
        assert archive_page(relative)


def test_current_reports_are_not_rewritten_or_hidden():
    for run in CURRENT_RUNS:
        path = Path('runs') / run / 'candidate' / 'report.md'
        original = '# Current report\n\nPreserve evidence\n'
        assert not archive_page(path)
        assert publication_markdown(path, original) == original
    assert not archive_page(Path('docs/CURRENT_DESIGN.md'))


def test_old_pages_are_only_in_archive_navigation():
    import tomllib

    root = Path(__file__).resolve().parents[1]
    nav = tomllib.loads((root / 'zensical.toml').read_text())['project']['nav']
    def paths(items):
        for item in items:
            if isinstance(item, str):
                yield item
            else:
                for value in item.values():
                    yield from paths(value if isinstance(value, list) else [value])
    assert not ARCHIVE_PAGES.intersection(paths(nav[:-1]))
    assert ARCHIVE_PAGES.issubset(set(paths(nav[-1:])))


def test_current_build_uses_current_body_lengths():
    root = Path(__file__).resolve().parents[1]
    text = (root / 'docs/BUILD.md').read_text()
    assert '340 mm' not in text
    assert '380 mm' not in text
    assert '410 mm' not in text and '440 mm' not in text
    assert '500 mm' in text and '24 mm' in text and 'insert' in text
    assert 'BUILD_18MM.md' in text
    archived = (root / 'docs/BUILD_18MM.md').read_text()
    assert '410 mm' in archived and '440 mm' in archived


def test_staging_removes_unlinked_stale_pages(tmp_path, monkeypatch):
    import prepare_docs

    monkeypatch.setattr(prepare_docs, 'ROOT', tmp_path)
    (tmp_path / 'docs').mkdir()
    (tmp_path / 'docs/HOME.md').write_text('# Current home\n')
    (tmp_path / 'README.md').write_text('# Readme\n')
    (tmp_path / 'ROCKET_PROJECT_BRIEF.md').write_text('# Brief\n')
    (tmp_path / '_site_docs').mkdir()
    (tmp_path / '_site_docs/stale.md').write_text('# Obsolete\n')
    prepare_docs.prepare()
    assert not (tmp_path / '_site_docs/stale.md').exists()
    assert (tmp_path / '_site_docs/index.md').read_text() == '# Current home\n'


def test_selective_snapshot_preserves_historical_evidence(tmp_path, monkeypatch):
    import prepare_docs
    monkeypatch.setattr(prepare_docs, 'ROOT', tmp_path)
    (tmp_path/'docs').mkdir()
    (tmp_path/'docs/HOME.md').write_text('[Old](../runs/old/data.json) [New](../runs/new/data.json)')
    (tmp_path/'README.md').write_text('# Readme')
    (tmp_path/'ROCKET_PROJECT_BRIEF.md').write_text('# Brief')
    for run in ['old', 'new']:
        (tmp_path/'runs'/run).mkdir(parents=True)
        (tmp_path/'runs'/run/'data.json').write_text('local')
    (tmp_path/'docs-evidence/runs/old').mkdir(parents=True)
    (tmp_path/'docs-evidence/runs/old/data.json').write_text('sealed historical')
    prepare_docs.prepare(snapshot_runs=['new'])
    assert (tmp_path/'docs-evidence/runs/old/data.json').read_text() == 'sealed historical'
    assert (tmp_path/'docs-evidence/runs/new/data.json').read_text() == 'local'
