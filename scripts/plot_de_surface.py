"""Render a 3D body/fin/stability surface from the saved D/E geometry sweep."""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.lines import Line2D


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("comparison", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.comparison.read_text())
    selected = [r for r in rows if r["nose_mm"] == 50]
    bodies = sorted({r["body_mm"] for r in selected})
    spans = sorted({r["span_mm"] for r in selected})
    x, y = np.meshgrid(bodies, spans)
    stability = np.zeros_like(x, dtype=float)
    apogee = np.zeros_like(x, dtype=float)
    for i, span in enumerate(spans):
        for j, body in enumerate(bodies):
            cases = [r for r in selected if r["span_mm"] == span and r["body_mm"] == body]
            stability[i, j] = min(r["stability_cal"] for r in cases if r["motor"] == "E12-6")
            apogee[i, j] = next(r["apogee_m"] for r in cases
                                if r["motor"] == "D12-5" and r["wind_m_s"] == 0)

    cmap = plt.colormaps["viridis"]
    norm = colors.Normalize(vmin=apogee.min(), vmax=apogee.max())
    fig = plt.figure(figsize=(15.5, 7.2))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.plot_surface(x, y, stability, facecolors=cmap(norm(apogee)),
                    edgecolor="#303030", linewidth=0.5, shade=False, alpha=0.94)
    passes = stability >= 1.5
    # Raise the markers slightly to prevent the surface from hiding them in a static 3D rendering.
    marker_height = stability + 0.02
    ax.scatter(x[passes], y[passes], marker_height[passes], color="#087e45",
               edgecolor="white", linewidth=1.2, s=68, depthshade=False)
    ax.scatter(x[~passes], y[~passes], marker_height[~passes], color="#c82333",
               edgecolor="white", linewidth=1.2, s=68, depthshade=False)
    ax.plot_surface(x, y, np.full_like(stability, 1.5), color="#b22222", alpha=0.11, shade=False)
    ax.legend(handles=[
        Line2D([0], [0], marker="o", color="none", markerfacecolor="#087e45",
               markeredgecolor="white", markersize=9, label="≥1.5 cal"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor="#c82333",
               markeredgecolor="white", markersize=9, label="<1.5 cal"),
    ], loc="upper left", bbox_to_anchor=(0.03, 0.91), title="E12-6 stability")
    ax.set(xlabel="Body length (mm)", ylabel="Fin span (mm)",
           zlabel="Worst E12-6 stability (cal)")
    ax.set_xticks(bodies)
    ax.set_yticks(spans)
    ax.set_zlim(0.9, max(1.9, stability.max() + 0.1))
    ax.view_init(elev=24, azim=-61)
    ax.set_box_aspect((1.3, 1.0, 0.85))
    ax.set_title("3D geometry view (surface hue = D12-5 apogee)", fontsize=11)
    trade = fig.add_subplot(1, 2, 2)
    body_colors = ["#0868ac", "#d95f02", "#008f75"]
    for j, body in enumerate(bodies):
        hue = body_colors[j % len(body_colors)]
        trade.plot(stability[:, j], apogee[:, j], color=hue, linewidth=2.2,
                   label=f"{body:g} mm body", zorder=2)
        for i, span in enumerate(spans):
            point_color = "#087e45" if passes[i, j] else "#c82333"
            trade.scatter(stability[i, j], apogee[i, j], s=72, color=point_color,
                          edgecolor="white", linewidth=1.2, zorder=3)
            trade.annotate(f"{span:g}", (stability[i, j], apogee[i, j]),
                           xytext=(5, 6), textcoords="offset points", fontsize=8, color=hue)
    trade.axvline(1.5, color="#aa3333", linestyle="--", linewidth=1.2)
    trade.set(xlabel="Worst E12-6 stability (cal)",
              ylabel="D12-5 calm-air apogee (m)",
              title="Joint D/E screen (different motors)")
    trade.grid(alpha=0.3)
    trade.legend(loc="lower left", fontsize=9)
    ax.set_position([0.02, 0.17, 0.47, 0.72])
    trade.set_position([0.62, 0.15, 0.35, 0.72])
    fig.suptitle("BT-60 joint-motor geometry screen: E12 stability and D12 altitude", y=0.96)
    fig.text(0.5, 0.045,
             "Nominal mass · 50 mm nose · 24-inch chute Cd 0.53 · red plane = 1.5 cal planning target",
             ha="center", fontsize=9)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=170)
    fig.savefig(args.output.with_suffix(".svg"))
    print(args.output)


if __name__ == "__main__":
    main()
