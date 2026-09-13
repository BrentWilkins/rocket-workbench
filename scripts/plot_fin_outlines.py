"""Show the actual shared fin outlines used by the retained equal-area study."""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

from rocket_workbench.config import load_config
from rocket_workbench.fins import outline, area_mm2


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    styles=[('trapezoidal','#0072B2'),('elliptical','#E69F00'),('clipped-delta','#009E73'),('swept','#CC79A7')]
    fig,axes=plt.subplots(2,2,figsize=(10,9),layout='constrained',sharex=True,sharey=True)
    for ax,(shape,color) in zip(axes.flat,styles):
        config=load_config(args.study/f'{shape}-a45-b410/config.yaml')
        points=outline(config)
        ax.add_patch(Polygon(points,facecolor=color,edgecolor='#222222',alpha=.85))
        ax.set_title(f'{shape}\n{area_mm2(points):.1f} mm²; {config.geometry.mm("fin_span"):.1f} mm span')
        ax.axhline(0,color='#222222',linewidth=2)
        ax.set(xlim=(-3,70),ylim=(-3,70),aspect='equal',xlabel='Axial distance aft (mm)',ylabel='Exposed radial span (mm)')
        ax.grid(alpha=.2)
    fig.suptitle('Same exposed area, different planforms\nShared CAD / flight-model outlines; root attaches at radial zero')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    for ext in ['svg','png']:
        fig.savefig(args.output.with_suffix('.'+ext),dpi=150)
    plt.close(fig)


if __name__=='__main__':
    main()
