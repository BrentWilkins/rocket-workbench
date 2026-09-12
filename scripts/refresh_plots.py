"""Render current plot styling from saved results without rerunning physics.

Historical review bundles stay unchanged; current presentation assets go in plots/.
"""
import json
from pathlib import Path

from package_review import ROOT, RUNS, plot_altitude


def main():
    out = ROOT/'plots'
    out.mkdir(exist_ok=True)
    for run in RUNS[:3]:
        source = ROOT/'runs'/run/'results.json'
        target = out/f'{run}.svg'
        plot_altitude(json.loads(source.read_text()), target)
        print(target)


if __name__ == '__main__':
    main()
