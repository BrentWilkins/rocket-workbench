"""Compare two measured complete sled assemblies; never issue flight clearance."""
import argparse
import json
from pathlib import Path

from rocket_workbench.progression import compare_assemblies


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dummy', type=Path, required=True)
    p.add_argument('--logger', type=Path, required=True)
    args = p.parse_args()
    result = compare_assemblies(json.loads(args.dummy.read_text()), json.loads(args.logger.read_text()))
    print(json.dumps(result, indent=2))
    return 0 if result['matches_provisional_bench_tolerances'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
