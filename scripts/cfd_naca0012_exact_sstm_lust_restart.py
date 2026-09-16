"""Create the predeclared corrected-SSTm fine-grid LUST restart."""

import argparse
import json
from pathlib import Path

from cfd_naca0012_sstm_limiter_restart import restart


METHOD = "same-grid exact-SSTm LUST numerical-refresh restart"
IMAGE_ID = "sha256:ae3235d75b54311a6dbcdfc2b45f6c9be77a8ff0743c099cf5ca3f3e9db0d23f"
LIBS = (
    'libs ("libTmrSSTmCompressible.so" '
    '"libTmrSSTmKOnlyLimiterCompressible.so" '
    '"libTmrSSTmExactProductionCompressible.so" '
    '"libSutherlandPrTransport.so");'
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--iterations", type=int, default=1500)
    args = parser.parse_args()

    result = restart(
        args.source,
        args.source_audit,
        args.target,
        args.iterations,
        method=METHOD,
        image_id=IMAGE_ID,
        source_runtime_model="TmrSSTmExactProduction",
        source_runtime_library="libTmrSSTmExactProductionCompressible.so",
        source_libs=LIBS,
        target_runtime_model="TmrSSTmExactProduction",
        target_runtime_library="libTmrSSTmExactProductionCompressible.so",
        target_libs=LIBS,
        target_variant="tmr-sstm-exact-production",
        record_name="exact-sstm-lust-restart-execution.json",
        source_end_time=1500,
        target_convection_scheme="lust-blended",
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
