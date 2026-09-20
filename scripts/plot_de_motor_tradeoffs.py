"""Compare stability and altitude within each motor, with the weighed current collar."""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def flight_speed_stability(run_folder):
    """Ignore near-apogee low-speed CP/AoA excursions for this comparison view."""
    result = json.loads((run_folder / "results.json").read_text())
    margins = []
    for case in result["cases"]:
        if case["loading"] != "actual":
            continue
        rod = next(e["time_s"] for e in case["events"] if e["type"] == "LAUNCHROD")
        apogee = next(e["time_s"] for e in case["events"] if e["type"] == "APOGEE")
        series = case["timeseries"]
        margins.extend((cp - cg) / diameter
                       for t, speed, cp, cg, diameter in zip(
                           series["time_s"], series["speed_m_s"], series["cp_x_m"],
                           series["cg_x_m"], series["reference_length_m"])
                       if rod <= t <= apogee and speed >= 10)
    return min(margins)


def values(rows, motor, body, span, run_root):
    cases = [r for r in rows if r["motor"] == motor and r["body_mm"] == body
             and r["span_mm"] == span and r["nose_mm"] == 50]
    return (flight_speed_stability(run_root / cases[0]["design"]),
            next(r["apogee_m"] for r in cases if r["wind_m_s"] == 0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("comparison", type=Path)
    parser.add_argument("measured_comparison", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--extra-measured", type=Path, action="append", default=[],
                        help="Additional measured-collar body-length comparison files")
    args = parser.parse_args()
    rows = json.loads(args.comparison.read_text())
    measured_sets = [(json.loads(path.read_text()), path.parent)
                     for path in [args.measured_comparison, *args.extra_measured]]
    bodies = sorted({r["body_mm"] for r in rows if r["nose_mm"] == 50})
    spans = sorted({r["span_mm"] for r in rows if r["nose_mm"] == 50})
    body_colors = ["#0868ac", "#d95f02", "#008f75"]

    fig, axes = plt.subplots(1, 2, figsize=(14.5, 6.4))
    for ax, motor in zip(axes, ("D12-5", "E12-6")):
        for j, body in enumerate(bodies):
            hue = body_colors[j % len(body_colors)]
            points = [values(rows, motor, body, span, args.comparison.parent) for span in spans]
            ax.plot([p[0] for p in points], [p[1] for p in points],
                    color=hue, linewidth=2.1, label=f"{body:g} mm body")
            for span, (stability, apogee) in zip(spans, points):
                ax.scatter(stability, apogee, s=64,
                           color="#087e45" if stability >= 1.5 else "#c82333",
                           edgecolor="white", linewidth=1.1, zorder=3)
                ax.annotate(f"{span:g}", (stability, apogee), xytext=(5, 5),
                            textcoords="offset points", fontsize=8, color=hue)

        for measured_rows, run_root in measured_sets:
            for body in sorted({r["body_mm"] for r in measured_rows if r["motor"] == motor}):
                observed = [r for r in measured_rows if r["motor"] == motor and r["body_mm"] == body]
                hue = body_colors[bodies.index(body) % len(body_colors)]
                observed_stability = flight_speed_stability(run_root / observed[0]["design"])
                observed_apogee = next(r["apogee_m"] for r in observed if r["wind_m_s"] == 0)
                ax.scatter(observed_stability, observed_apogee, marker="*", s=300,
                           color=hue, edgecolor="#333333", linewidth=1.0, zorder=5,
                           label="27 g collar, each body" if body == 500 else None)
                if body == 500:
                    ax.annotate("current 500 mm", (observed_stability, observed_apogee),
                                xytext=(-16, -24), textcoords="offset points", fontsize=9,
                                ha="right", color=hue)
        ax.axvline(1.0, color="#777777", linestyle=":", linewidth=1.3)
        ax.axvline(1.5, color="#b22222", linestyle="--", linewidth=1.2)
        ax.set(title=motor, xlabel="Minimum stability above 10 m/s, 0/2/4 m/s wind (cal)",
               ylabel="Calm-air apogee (m)")
        ax.grid(alpha=0.27)
        ax.legend(loc="lower left", fontsize=8)

    fig.suptitle("Same-motor tradeoff at flight speed: more fin/body stability generally costs altitude", y=0.97)
    fig.text(0.5, 0.025,
             "Stars = 27 g collar on each body; only 500 mm is current · nominal mass · dotted = 1.0 cal reference · dashed = 1.5 cal advisory",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.15, top=0.88, wspace=0.22)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=170)
    fig.savefig(args.output.with_suffix(".svg"))
    print(args.output)


if __name__ == "__main__":
    main()
