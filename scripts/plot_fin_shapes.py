"""Render retained fin-screen results; never rerun simulations to make a plot."""
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
    rows = json.loads((args.study/'comparison.json').read_text())
    colors = {'trapezoidal':'#0072B2','elliptical':'#E69F00','clipped-delta':'#009E73','swept':'#CC79A7'}
    fig, axes = plt.subplots(1,2,figsize=(13,8),sharey=True,layout='constrained')
    for i,r in enumerate(rows):
        color = colors[r['shape']]
        for ax,key in zip(axes,['apogee_m','minimum_ascent_stability_cal']):
            lo,hi = r[key]
            ax.plot([lo,hi],[i,i],color=color,linewidth=3)
            ax.plot(lo,i,marker='o' if r['summary']['planned']['passed']==6 else 'x',color=color)
    axes[0].set_yticks(range(len(rows)),[r['design'] for r in rows])
    axes[0].invert_yaxis()
    axes[0].set_xlabel('Loaded apogee across 0/2/4 m/s wind (m)')
    axes[1].set_xlabel('Minimum ascent stability across those flights (cal)')
    axes[1].axvline(1,color='#444444',linestyle='--',label='Configured 1 cal minimum')
    axes[1].legend()
    for ax in axes:
        ax.grid(axis='x',alpha=.25)
    fig.suptitle('D12-5 / BT-60: equal-area fin comparison\nNominal estimates; × = at least one planned case fails; not flight clearance')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    for ext in ['svg','png']:
        fig.savefig(args.output.with_suffix('.'+ext),dpi=160)
    plt.close(fig)


if __name__=='__main__':
    main()
