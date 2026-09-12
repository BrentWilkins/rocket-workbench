import pytest


def pytest_addoption(parser):
    parser.addoption('--run-integration', action='store_true', default=False)


def pytest_collection_modifyitems(config, items):
    if not config.getoption('--run-integration'):
        for item in items:
            if 'integration' in item.keywords:
                item.add_marker(pytest.mark.skip(reason='Use --run-integration for real CAD/Java checks'))
