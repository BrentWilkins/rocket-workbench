"""Plot the retained exploratory CFD fin Pareto tradeoff without rerunning CFD."""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "rocket-workbench"
import matplotlib.pyplot as plt


COLORS = {
    "elliptical": "#E69F00",
    "trapezoidal": "#0072B2",
    "swept": "#CC79A7",
    "clipped-delta": "#009E73",
}
LABELS = {
    "elliptical": "Elliptical",
    "trapezoidal": "Trapezoidal",
    "swept": "Swept",
    "clipped-delta": "Clipped delta",
}


def interval_point(report: dict, design: str) -> dict:
    """Return paired-grid midpoint and range for one planar design."""
    drag = report["provisional_grid_metrics"][f"{design}:a0"]["metrics"]["Cd"][
        "grid_interval"
    ]
    pitch = report["provisional_grid_metrics"][f"{design}:a5"]["metrics"][
        "CmPitch"
    ]["grid_interval"]
    restoring = sorted(-value for value in pitch)
    return {
        "design": design,
        "drag": sum(drag) / 2,
        "drag_range": drag,
        "restoring": sum(restoring) / 2,
        "restoring_range": restoring,
        "paired_grid": True,
    }


def single_grid_point(report: dict, design: str) -> dict:
    """Return the coarse-only point for a design without paired-grid metrics."""
    rows = {row["case_id"]: row for row in report["rows"]}
    drag = rows[f"{design}-a0-cell20"]["audit"]["coefficient_statistics"]["Cd"][
        "mean"
    ]
    pitch = rows[f"{design}-a5-cell20"]["audit"]["coefficient_statistics"][
        "CmPitch"
    ]["mean"]
    return {
        "design": design,
        "drag": drag,
        "drag_range": None,
        "restoring": -pitch,
        "restoring_range": None,
        "paired_grid": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    report = json.loads(args.audit.read_text())
    points = [
        interval_point(report, "elliptical"),
        interval_point(report, "trapezoidal"),
        interval_point(report, "swept"),
        single_grid_point(report, "clipped-delta"),
    ]

    fig, ax = plt.subplots(figsize=(9, 6), layout="constrained")
    ax.plot(
        [point["drag"] for point in points],
        [point["restoring"] for point in points],
        color="#666666",
        linewidth=1.5,
        linestyle="--",
        zorder=1,
        label="Provisional nondominated tradeoff",
    )

    offsets = {
        "elliptical": (8, 8),
        "trapezoidal": (8, -18),
        "swept": (-68, 8),
        "clipped-delta": (-92, 8),
    }
    for point in points:
        color = COLORS[point["design"]]
        if point["paired_grid"]:
            x_low, x_high = point["drag_range"]
            y_low, y_high = point["restoring_range"]
            ax.errorbar(
                point["drag"],
                point["restoring"],
                xerr=[[point["drag"] - x_low], [x_high - point["drag"]]],
                yerr=[[point["restoring"] - y_low], [y_high - point["restoring"]]],
                fmt="o",
                markersize=8,
                capsize=4,
                color=color,
                ecolor=color,
                zorder=3,
            )
        else:
            ax.scatter(
                point["drag"],
                point["restoring"],
                marker="D",
                s=62,
                facecolors="white",
                edgecolors=color,
                linewidths=2,
                zorder=3,
                label="Single 20 mm grid only",
            )
        ax.annotate(
            LABELS[point["design"]],
            (point["drag"], point["restoring"]),
            xytext=offsets[point["design"]],
            textcoords="offset points",
            fontsize=10,
        )

    ax.annotate(
        "preferred direction",
        xy=(0.515, 5.15),
        xytext=(0.545, 4.95),
        arrowprops={"arrowstyle": "->", "color": "#444444"},
        color="#444444",
        fontsize=9,
    )
    ax.set_xlabel("Zero-angle drag coefficient, Cd (lower is better)")
    ax.set_ylabel(
        "Restoring pitch-moment magnitude at 5 degrees, -CmPitch\n"
        "(higher is stronger)"
    )
    ax.set_title(
        "Provisional CFD drag-restoring tradeoff\n"
        "All points fail at least one campaign gate; bars span 20/15 mm grids"
    )
    ax.grid(alpha=0.25)
    ax.legend(loc="lower right")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=160, metadata={"Date": None})
    plt.close(fig)
    if args.output.suffix.lower() == ".svg":
        svg = args.output.read_text()
        args.output.write_text(
            "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
        )


if __name__ == "__main__":
    main()
