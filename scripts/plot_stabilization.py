"""Publish the stabilization study results and geometry-comparison figures."""

import argparse
import csv
import hashlib
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "rocket-workbench-stabilization"
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


BASES = ((500, 50, "conical"), (500, 40, "ogive"), (530, 40, "ogive"))


def save_figure(fig, path):
    fig.savefig(path, metadata={"Date": None})
    fig.savefig(path.with_suffix(".png"), dpi=160)
    plt.close(fig)


def aft_fins(rows, path):
    fig, axes = plt.subplots(1, 3, figsize=(12.8, 5), sharex=True, sharey=True)
    for ax, (body, nose, shape) in zip(axes, BASES, strict=True):
        for count, color in ((3, "#177a9f"), (4, "#c05a26")):
            subset = sorted((r for r in rows if r["variant"] == "baseline"
                             and r["body_mm"] == body and r["nose_mm"] == nose
                             and r["nose_shape"] == shape and r["motor"] == "E12-6"
                             and r["wind_m_s"] == 4 and r["fin_count"] == count),
                            key=lambda r: r["span_mm"])
            if len(subset) != 4:
                raise ValueError("Missing fin-count comparison points")
            ax.plot([r["stability_cal"] for r in subset], [r["apogee_m"] for r in subset],
                    "o-", color=color, label=f"{count} aft fins")
            for row in subset:
                ax.annotate(f'{row["span_mm"]:.2f}'.rstrip("0").rstrip("."),
                            (row["stability_cal"], row["apogee_m"]), xytext=(3, 6),
                            textcoords="offset points", fontsize=8, color=color)
        ax.axvline(1.5, ls="--", color="#777777", lw=1)
        ax.margins(x=0.13, y=0.10)
        ax.grid(alpha=0.25)
        ax.set(title=f"{body} mm body, {nose} mm {shape}",
               xlabel="Minimum ascent stability (calibers)")
        ax.legend(fontsize=8, loc="lower left")
    axes[0].set_ylabel("E12-6 apogee at 4 m/s wind (m)")
    fig.suptitle("Three versus four aft fins, including their estimated printed mass")
    fig.text(0.5, 0.015, "Point labels are fin span in mm. Dashed line: 1.5-caliber design target. Root chord remains 65 mm.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.06, 1, 0.93))
    save_figure(fig, path)


def forward_effects(rows, path):
    subset = [r for r in rows if r["body_mm"] == 500 and r["nose_shape"] == "ogive"
              and r["nose_mm"] == 40 and r["motor"] == "E12-6"
              and r["wind_m_s"] == 4 and r["wind_heading_deg"] == 0]
    reference = next(r for r in subset if r["variant"] == "reference")
    options = [("guard", n) for n in (1, 2, 5, 10)]
    options += [("canard", n) for n in (10, 20)]
    options += [("ballast", n) for n in (2, 5, 10)]
    fig, axes = plt.subplots(1, 2, figsize=(11, 6.2), sharey=True)
    colors = {"guard": "#177a9f", "canard": "#c05a26", "ballast": "#79509e"}
    labels = []
    for y, (kind, size) in enumerate(options):
        row = next(r for r in subset if r["variant"] == kind and r["variant_size"] == size)
        control = next((r for r in subset if r["variant"] == f"{kind}-mass-only"
                        and r["variant_size"] == size), row)
        labels.append(f"{size:g} g nose ballast" if kind == "ballast"
                      else f"{kind}: {size:g} mm projection")
        for ax, field in zip(axes, ("stability_cal", "apogee_m"), strict=True):
            actual, mass_only = row[field] - reference[field], control[field] - reference[field]
            ax.plot([mass_only, actual], [y, y], color=colors[kind], lw=1.5)
            if kind != "ballast":
                ax.scatter(mass_only, y, s=52, facecolors="white", edgecolors=colors[kind], zorder=3)
            ax.scatter(actual, y, s=40, color=colors[kind], zorder=4)
    for ax in axes:
        ax.axvline(0, color="#777777", lw=1)
        ax.grid(axis="x", alpha=0.25)
    axes[0].set(yticks=range(len(labels)), yticklabels=labels,
                xlabel="Change in stability (calibers)")
    axes[0].invert_yaxis()
    axes[1].set_xlabel("Change in E12-6 apogee (m)")
    fig.legend(handles=[
        Line2D([0], [0], marker="o", color="none", markerfacecolor="#555555", label="surface and mass"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor="white", markeredgecolor="#555555",
               label="same mass and axial CG, no surface")], loc="lower center", ncol=2,
               bbox_to_anchor=(0.58, 0.045), fontsize=8)
    fig.suptitle("Forward additions: 500 mm body, 40 mm ogive, existing three-fin span")
    fig.text(0.5, 0.015, "4 m/s wind, heading 0°. Guard projection is radial height, not the 5 mm camera-hole diameter. Flat-fin proxies only.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.11, 1, 0.94))
    save_figure(fig, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, nargs=4, required=True,
                        help="fins, forward, references, small-guard comparison JSONs")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows, inputs = [], []
    for path, expected in zip(args.inputs, (144, 198, 18, 72), strict=True):
        data = json.loads(path.read_text())
        if len(data) != expected or any(r["status"] != "completed" for r in data):
            raise ValueError(f"Incomplete study: {path}")
        rows.extend(data)
        inputs.append(dict(path=str(path), rows=len(data), sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    keys = [(r["design"], r["wind_m_s"], r["wind_heading_deg"]) for r in rows]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate stabilization case")
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "stabilization.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (args.output / "stabilization-provenance.json").write_text(json.dumps(dict(
        inputs=inputs, cases=len(rows),
        assumptions="Nominal logger mass; calibrated CAD mass for 3/4 fins; fixed zero-cant forward surface proxies; no controller"),
        indent=2) + "\n")
    aft_fins(rows, args.output / "three-vs-four-fins.svg")
    forward_effects(rows, args.output / "forward-additions.svg")
    print(f"Published {len(rows)} stabilization cases")


if __name__ == "__main__":
    main()
