"""Plot the current D12/E12 geometry tradeoff from saved simulation results."""

import argparse
import json
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("comparison", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.comparison.read_text())
    grouped = defaultdict(list)
    for row in rows:
        if row["nose_mm"] == 50:
            grouped[(row["body_mm"], row["span_mm"])].append(row)

    colors = {500: "#0072B2", 530: "#D55E00", 560: "#009E73"}
    fig, ax = plt.subplots(figsize=(8.2, 5.4))
    fig.subplots_adjust(left=0.12, right=0.97, top=0.90, bottom=0.23)
    for body in sorted({key[0] for key in grouped}):
        points = []
        for (current_body, span), cases in grouped.items():
            if current_body != body:
                continue
            e12 = [c for c in cases if c["motor"] == "E12-6"]
            d12 = next(c for c in cases if c["motor"] == "D12-5" and c["wind_m_s"] == 0)
            points.append((span, min(c["stability_cal"] for c in e12), d12["apogee_m"]))
        points.sort()
        ax.plot([p[1] for p in points], [p[2] for p in points], color=colors[int(body)],
                lw=1.8, marker="o", ms=5, label=f"{body:g} mm body")
        for span, stability, apogee in points:
            ax.annotate(f"{span:g} mm", (stability, apogee), xytext=(4, 4),
                        textcoords="offset points", fontsize=8, color=colors[int(body)])
    ax.axvline(1.0, color="#666666", linestyle=":", lw=1.3, label="configured stability minimum")
    ax.axvline(1.5, color="#333333", linestyle="--", lw=1.1, label="1.5 cal design target")
    ax.set(xlabel="Worst E12-6 loaded stability, 0/2/4 m/s wind (calibers)",
           ylabel="D12-5 loaded apogee, calm air (m)",
           title="BT-60 D/E geometry tradeoff — corrected avionics layout")
    ax.grid(True, color="#dddddd", linewidth=0.7)
    ax.legend(loc="lower left", fontsize=8)
    fig.text(0.5, 0.055,
             "Nominal mass, 24-inch chute Cd 0.53, 50 mm nose. Parametric fin aerodynamics; no flight clearance.",
             fontsize=8, ha="center")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output)
    fig.savefig(args.output.with_suffix(".png"), dpi=160)
    print(args.output)


if __name__ == "__main__":
    main()
