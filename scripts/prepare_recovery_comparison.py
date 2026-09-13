"""Prepare consistent nominal recovery candidates for the expanded uncertainty grid."""
import argparse
from pathlib import Path

from rocket_workbench.cli import save_json
from rocket_workbench.provenance import seal_run
from study_fin_recovery import configuration as generic
from study_sourced_chute import configuration as sourced


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    candidates = [generic(20, 430), generic(22, 460), sourced(False, .53)]
    for config in candidates:
        folder = args.output/config.name
        folder.mkdir()
        save_json(folder/'config.yaml', config.model_dump())
    save_json(args.output/'search-spec.json', dict(designs=[c.name for c in candidates],
        rationale='Compare current performance leader, intermediate generic recovery, and literature-characterized chute',
        bounds='Nominal/upper avionics and chute +20%, mount 1/1.5, expanded 72-case inner grid',
        limitations='Pairs upper chute and avionics allowances; not independent full-factorial component masses. '
                    'Packing remains provisional. No cap insert revision or physical validation.'))
    seal_run(args.output)


if __name__ == '__main__':
    main()
