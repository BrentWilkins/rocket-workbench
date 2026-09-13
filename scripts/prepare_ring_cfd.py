"""Prepare matched ring-tail flow cases without executing or accepting CFD."""
import argparse
from pathlib import Path

from cfd_case import generate
from rocket_workbench.cli import save_json
from rocket_workbench.config import load_config


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    config = load_config(args.config)
    args.output.mkdir(parents=True,exist_ok=False)
    for chord in (0,5,10):
        generate(config,args.output/f'ring-{chord}mm',cell_mm=20,speed=40,alpha=0,
                 iterations=600,ring_chord_mm=chord)
        print('PREPARED',chord,flush=True)
    save_json(args.output/'comparison-spec.json',dict(chords_mm=[0,5,10],wall_mm=1.2,
        background_cell_mm=20,speed_m_s=40,alpha_deg=0,iterations=600,
        purpose='Matched geometry diagnostics only; not a flight ranking or validated mesh',
        execution='Prepared only. Finish baseline mesh/wall/domain/benchmark checks before accepting results.',
        moment_reference='Common planar baseline dry CG; ring mass not integrated into flight models'))


if __name__ == '__main__':
    main()
