import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_docs import home_at_site_root


def test_home_links_rebased_when_copied_to_site_root():
    assert home_at_site_root('[Current](CURRENT_DESIGN.md#files)') == '[Current](docs/CURRENT_DESIGN.md#files)'
    assert home_at_site_root('[Readme](../README.md)') == '[Readme](README.md)'
    for link in ['[Web](https://example.com/x)', '[Anchor](#local)', '[Absolute](/x)']:
        assert home_at_site_root(link) == link
