"""Refresh presentation-only previews and reseal artifacts without changing flight data."""
import argparse
from pathlib import Path

from rocket_workbench.cad import preview
from rocket_workbench.config import load_config
from rocket_workbench.provenance import seal_run

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('study', type=Path)
args = parser.parse_args()
for config in args.study.glob('nose-*/config.yaml'):
    preview(load_config(config), config.parent/'cad/assembly.svg')
    seal_run(config.parent, record_sources=False)
