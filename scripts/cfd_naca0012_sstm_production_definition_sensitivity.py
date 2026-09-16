"""Compare deviatoric and NASA SSTm S-squared production definitions."""

import argparse
import json
from pathlib import Path

from cfd_naca0012_sstm_limiter_sensitivity import evaluate


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-case", required=True, type=Path)
    parser.add_argument("--baseline-audit", required=True, type=Path)
    parser.add_argument("--candidate-case", required=True, type=Path)
    parser.add_argument("--candidate-audit", required=True, type=Path)
    parser.add_argument("--cfl3d-reference", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    result = evaluate(
        args.baseline_case,
        args.baseline_audit,
        args.candidate_case,
        args.candidate_audit,
        args.cfl3d_reference,
    )
    result["scope"] = (
        "TMR NACA 0012 zero-angle SSTm production-definition diagnostic"
    )
    result["baseline"]["model"] = (
        "TmrSSTmKOnlyLimiter with deviatoric OpenFOAM production contraction"
    )
    result["candidate"]["model"] = (
        "TmrSSTmExactProduction with NASA TMR P = mu_t S squared"
    )
    result["diagnostic_conclusion"] = (
        "Using the exact NASA SSTm S-squared production definition changes drag "
        "but does not close the remaining same-grid CFL3D discrepancy."
    )

    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-sstm-production-definition-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
