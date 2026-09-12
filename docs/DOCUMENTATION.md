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
`python scripts/prepare_docs.py --snapshot`, then review the `docs-evidence/` changes before committing. Staging does
not delete stale files; use a fresh checkout for release builds, as the Pages workflow does.

## GitHub Pages

The public repository is `brentwilkins/rocket-workbench`, with its Pages source configured as **GitHub Actions**. The
documentation workflow checks pull requests and deploys pushes to `main` or manual runs on `main`. No personal access
token is required. The site uses relative links so a repository-name URL prefix works. The site URL is
https://brentwilkins.github.io/rocket-workbench/; updates appear after a successful deployment. CI pins uv 0.12.13 so
its Python download catalog includes the pinned Python 3.14.6.

## Diagrams

Use fenced `mermaid` blocks for flowcharts and component relationships; native support is configured in `zensical.toml`.
Keep scientific charts as SVGs. Mermaid requires JavaScript in the reader's browser.
