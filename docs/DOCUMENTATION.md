# Documentation site

Zensical is a uv-managed, locked documentation dependency. Python 3.14 is required. The documentation build needs
neither Java nor CAD dependencies.

```sh
uv run --locked --only-group docs python scripts/prepare_docs.py
uv run --locked --only-group docs zensical serve
```

Open the localhost URL printed by Zensical. After changing source documents or plots, rerun the staging command; the
preview watches the staged files, not the originals. For a static build:

```sh
uv run --locked --only-group docs zensical build --clean --strict
```

The generated site is in `site/`. Neither `site/` nor `_site_docs/` belongs in Git. Staging copies source Markdown and
the explicitly linked evidence in `docs-evidence/runs/`. It does not publish the full local `runs/`, tools,
environments, or historical deliverable bundles. To refresh evidence intentionally from local runs, use
`python scripts/prepare_docs.py --snapshot`, then review the `docs-evidence/` changes before committing. Staging
recreates the generated `_site_docs/` directory so unlinked old pages cannot leak into search or a local preview. Do not
edit that generated directory; edit repository source documents. Pages also builds from a fresh checkout.

## Current versus archived material

Navigation keeps superseded pages together under **Archive — old news, not current designs**. Staging adds an
unambiguous archive heading and notice to every old page and linked old run report, including bookmarked deep links.
These pages are excluded from site search using
[Zensical's documented search exclusion](https://zensical.org/docs/setup/search/). Original report snapshots, hashes and
downloads are unchanged; the notices apply only to the rendered documentation.

`CURRENT_RUNS` and `ARCHIVE_PAGES` in `scripts/prepare_docs.py` are the explicit publication inventory. Promote new
studies deliberately when updating the current comparison. Do not silently rewrite historical criteria or pass counts.
Use `--snapshot-run RUN_NAME` to refresh only one study's linked artifacts without replacing historical snapshots.

## GitHub Pages

The public repository is `brentwilkins/rocket-workbench`, with its Pages source configured as **GitHub Actions**. The
documentation workflow checks pull requests and deploys pushes to `main` or manual runs on `main`. No personal access
token is required. The site uses relative links so a repository-name URL prefix works. The site URL is
https://brentwilkins.github.io/rocket-workbench/; updates appear after a successful deployment. CI pins uv 0.12.13 so
its Python download catalog includes the pinned Python 3.14.6.

## Diagrams

Use fenced `mermaid` blocks for flowcharts and component relationships; native support is configured in `zensical.toml`.
Keep scientific charts as SVGs. Mermaid requires JavaScript in the reader's browser.
