"""Render a performance comparison from retained search results, never rerun physics."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not (args.study/'manifest.json').is_file():
        raise ValueError('Only render a completed, sealed geometry study')
    rows = json.loads((args.study/'comparison.json').read_text())
    front = json.loads((args.study/'pareto.json').read_text())
    fig, ax = plt.subplots(figsize=(9, 6), layout='constrained')
    styles = [('conical', '#0072b2', 'o'), ('ogive', '#d55e00', 's'), ('ellipsoid', '#009e73', '^')]
    for shape, color, marker in styles:
        selected = [r for r in rows if r['nominal_feasible'] and r['design'].startswith(shape+'-')]
        ax.scatter([r['speed_m_s'] for r in selected], [r['apogee_m'] for r in selected],
                   c=color, marker=marker, s=50, label=shape, edgecolors='#202830', linewidths=.5)
    ax.scatter([r['speed_m_s'] for r in front], [r['apogee_m'] for r in front],
               facecolors='none', edgecolors='#202830', s=160, linewidths=1.5, label='nominal Pareto front')
    ax.set(xlabel='Worst-wind loaded peak powered speed (m/s)', ylabel='Worst-wind loaded apogee (m)',
           title='Current avionics: performance among nominally feasible designs')
    ax.grid(alpha=.2)
    ax.legend(loc='best')
    fig.supxlabel('20.65 g avionics; winds 0/2 m/s. Failed designs excluded, retained in reports.\n'
                  'Bounded search, not flight approval. Ogive drag caveat applies.', fontsize=9)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output)
    fig.savefig(args.output.with_suffix('.png'), dpi=150)
    plt.close(fig)
    print(args.output)


if __name__ == '__main__':
    main()
