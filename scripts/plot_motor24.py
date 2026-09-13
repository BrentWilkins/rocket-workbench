"""Plot retained motor-comparison results without rerunning physics."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rows = json.loads((args.study/'comparison.json').read_text())
    profiles = ['nominal', 'upper-avionics', 'heavy-build', 'inert-plus20', 'inert-plus40']
    labels = ['Nominal', 'Upper\navionics', 'Heavy\nbuild', '+20 g inert', '+40 g inert']
    motors = [('C5-3', '#0072B2'), ('D12-5', '#E69F00'), ('E12-6', '#009E73')]
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')
    for j, (motor, color) in enumerate(motors):
        group = [next(r for r in rows if r['profile'] == p and r['motor'] == motor) for p in profiles]
        for ax, metric in zip(axes, ['apogee_m', 'guide_departure_m_s']):
            bounds = np.array([r[metric] for r in group], dtype=float)
            mid = bounds.mean(axis=1)
            ax.bar(np.arange(5)+(j-1)*.25, mid, width=.24, color=color, edgecolor='#333333',
                   linewidth=.5, yerr=np.array([mid-bounds[:,0], bounds[:,1]-mid]), capsize=2, label=motor)
    axes[0].set_ylabel('Loaded apogee (m)')
    axes[1].set_ylabel('Loaded guide departure (m/s)')
    axes[1].axhline(12, color='#333333', linestyle='--', linewidth=1, label='12 m/s screening minimum')
    for ax in axes:
        ax.set_xticks(np.arange(5), labels)
        ax.set_axisbelow(True)
        ax.grid(axis='y', alpha=.25)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0].legend(frameon=False)
    axes[1].legend(frameon=False, fontsize=8, loc='lower left')
    fig.suptitle('BT-60 passive logger — retained motor comparison\n'
                 'Bars/ranges: winds 0/2 m/s; other failure gates still apply. E12: affected-lot purchase caution.',
                 fontsize=11)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={'Title': 'Provisional BT-60 motor comparison; not flight clearance'})
    plt.close(fig)
    print(args.output)


if __name__ == '__main__':
    main()
