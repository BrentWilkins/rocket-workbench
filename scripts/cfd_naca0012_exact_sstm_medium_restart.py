"""Restart the converged 449x129 case with exact transport and SSTm equations."""

import argparse
import json
from pathlib import Path

from cfd_naca0012_sstm_limiter_restart import restart


METHOD = "449x129 exact-transport exact-SSTm numerical-refresh restart"
IMAGE_ID = "sha256:ae3235d75b54311a6dbcdfc2b45f6c9be77a8ff0743c099cf5ca3f3e9db0d23f"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--iterations", type=int, default=2000)
    args = parser.parse_args()

    result = restart(
        args.source,
        args.source_audit,
        args.target,
        args.iterations,
        method=METHOD,
        image_id=IMAGE_ID,
        source_runtime_model="TmrSSTm",
        source_runtime_library="libTmrSSTmCompressible.so",
        source_libs='libs ("libTmrSSTmCompressible.so");',
        target_runtime_model="TmrSSTmExactProduction",
        target_runtime_library="libTmrSSTmExactProductionCompressible.so",
        target_libs=(
            'libs ("libTmrSSTmCompressible.so" '
            '"libTmrSSTmKOnlyLimiterCompressible.so" '
            '"libTmrSSTmExactProductionCompressible.so" '
            '"libSutherlandPrTransport.so");'
        ),
        target_variant="tmr-sstm-exact-production",
        record_name="exact-sstm-medium-restart-execution.json",
        source_transport_model="sutherland",
        convert_to_exact_sutherland_pr072=True,
        source_end_time=4000,
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
