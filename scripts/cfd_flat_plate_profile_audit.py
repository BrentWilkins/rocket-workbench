"""Audit the TMR flat-plate u+ profile at the nominal Re_theta=10000 station."""

import argparse
import json
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import final_time, numeric_pairs, vector_list


TARGET_RETHETA = 10_000.0
MINIMUM_Y_PLUS = 0.9
MAXIMUM_RELATIVE_ERROR = 0.05


def profile_errors(
    y_plus: np.ndarray,
    u_plus: np.ndarray,
    reference_y_plus: np.ndarray,
    reference_u_plus: np.ndarray,
    maximum_y_plus: float,
) -> dict:
    """Compare CFD cell-centre values with a reference in log(y+) space."""
    selected = (
        (y_plus >= MINIMUM_Y_PLUS)
        & (y_plus <= maximum_y_plus)
        & np.isfinite(y_plus)
        & np.isfinite(u_plus)
    )
    if selected.sum() < 3:
        raise ValueError("Fewer than three CFD samples overlap the declared y+ range")
    expected = np.interp(
        np.log10(y_plus[selected]),
        np.log10(reference_y_plus),
        reference_u_plus,
    )
    relative = np.abs(u_plus[selected] - expected) / expected
    return {
        "comparison_points": int(selected.sum()),
        "minimum_y_plus": float(y_plus[selected].min()),
        "maximum_y_plus": float(y_plus[selected].max()),
        "mean_relative_error": float(relative.mean()),
        "maximum_relative_error": float(relative.max()),
        "engineering_5_percent_screen": bool(
            np.all(relative <= MAXIMUM_RELATIVE_ERROR)
        ),
    }


def audit(case: Path, data: Path) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    grid = np.load(case / "tmr-grid.npz")
    x = grid["x"]
    y = grid["y"]
    time = final_time(case)

    velocity = vector_list((time / "U").read_text(), "internalField")[:, 0]
    nj, ni = x.shape
    velocity = velocity.reshape(nj - 1, ni - 1)
    wall_shear = vector_list((time / "wallShearStress").read_text(), "plate")[:, 0]

    leading = int(spec["mesh"]["plate_leading_edge_i"])
    plate_columns = np.arange(leading, ni - 1)
    typical_retheta = numeric_pairs(data / "retheta_variation_typical.dat")
    x_centres = (x[0, :-1] + x[0, 1:]) / 2
    mapped_retheta = np.interp(
        x_centres[plate_columns], typical_retheta[:, 0], typical_retheta[:, 1]
    )
    local_plate_index = int(np.argmin(np.abs(mapped_retheta - TARGET_RETHETA)))
    column = int(plate_columns[local_plate_index])

    speed = float(spec["conditions"]["U_m_s"])
    nu = float(spec["conditions"]["nu_m2_s"])
    u_tau = float(np.sqrt(abs(wall_shear[local_plate_index])))
    if not np.isfinite(u_tau) or u_tau <= 0:
        raise ValueError(f"Invalid friction velocity {u_tau}")

    cell_y = (
        y[:-1, column]
        + y[1:, column]
        + y[:-1, column + 1]
        + y[1:, column + 1]
    ) / 4
    y_plus = cell_y * u_tau / nu
    u_plus = velocity[:, column] / u_tau

    coles = numeric_pairs(data / "u_plus_y_plus.dat")
    cfl3d_raw = numeric_pairs(data / "sst-upyp_cfl3d.dat")
    cfl3d_y_plus = 10**cfl3d_raw[:, 0]
    shared_maximum = float(
        min(y_plus.max(), coles[:, 0].max(), cfl3d_y_plus.max())
    )
    coles_result = profile_errors(
        y_plus, u_plus, coles[:, 0], coles[:, 1], shared_maximum
    )
    cfl3d_result = profile_errors(
        y_plus, u_plus, cfl3d_y_plus, cfl3d_raw[:, 1], shared_maximum
    )

    return {
        "benchmark": spec["benchmark"],
        "solution_time": time.name,
        "target_retheta": TARGET_RETHETA,
        "station": {
            "cell_column": column,
            "x_m": float(x_centres[column]),
            "tmr_typical_mapped_retheta": float(mapped_retheta[local_plate_index]),
            "friction_velocity_m_s": u_tau,
            "cf": float(2 * u_tau**2 / speed**2),
        },
        "declared_comparison_range": {
            "minimum_y_plus": MINIMUM_Y_PLUS,
            "maximum_y_plus": shared_maximum,
            "basis": "shared CFD, TMR Coles/van-Driest, and CFL3D SST support",
        },
        "declared_maximum_pointwise_relative_error": MAXIMUM_RELATIVE_ERROR,
        "coles_van_driest": coles_result,
        "official_cfl3d_sstm": cfl3d_result,
        "profile_gate": bool(
            coles_result["engineering_5_percent_screen"]
            and cfl3d_result["engineering_5_percent_screen"]
        ),
        "limitations": [
            "Cell-centred OpenFOAM velocity is compared at the nearest supplied grid station.",
            "Station selection uses the independent TMR typical x-to-Re_theta mapping.",
            "This wall-subsystem check cannot validate separated rocket flow.",
        ],
        "samples": [
            {"y_plus": float(y_value), "u_plus": float(u_value)}
            for y_value, u_value in zip(y_plus, u_plus, strict=True)
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = audit(args.case, args.benchmark_data)
    (args.output / "flat-plate-profile-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                "station": result["station"],
                "coles_van_driest": result["coles_van_driest"],
                "official_cfl3d_sstm": result["official_cfl3d_sstm"],
                "profile_gate": result["profile_gate"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
