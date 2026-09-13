"""Check native 3MF transforms, bed placement and settings without printing."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

import numpy as np

NS = {'c': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
PATH = '{http://schemas.microsoft.com/3dmanufacturing/production/2015/06}path'


def matrix(value):
    result = np.eye(4)
    if value:
        result[:, :3] = np.array([float(v) for v in value.split()]).reshape(4,3)
    if not np.isfinite(result).all():
        raise ValueError('Nonfinite 3MF transform')
    return result


def inspect(path):
    with ZipFile(path) as archive:
        if archive.testzip():
            raise ValueError('Corrupt archive')
        settings = json.loads(archive.read('Metadata/project_settings.config'))
        for key, expected in [('printer_model','Bambu Lab X1 Carbon'), ('nozzle_diameter',['0.4']),
                              ('curr_bed_type','Textured PEI Plate'), ('filament_type',['PLA'])]:
            if settings[key] != expected:
                raise ValueError(f'Unexpected setting: {key}')
        def vertices(document, object_id, transform, active=()):
            key = (document,object_id)
            if key in active:
                raise ValueError('Cyclic 3MF components')
            root = ET.fromstring(archive.read(document))
            if root.get('unit','millimeter') != 'millimeter':
                raise ValueError('Require millimetre geometry')
            obj = root.find(f"c:resources/c:object[@id='{object_id}']",NS)
            if obj is None:
                raise ValueError('Missing component object')
            points = obj.findall('c:mesh/c:vertices/c:vertex',NS)
            if points:
                raw = np.array([[float(p.get(k)) for k in ('x','y','z')]+[1.] for p in points])
                return raw @ transform
            children = obj.findall('c:components/c:component',NS)
            if not children:
                raise ValueError('Empty object')
            return np.vstack([vertices(child.get(PATH,document).lstrip('/'), child.get('objectid'),
                               matrix(child.get('transform')) @ transform, (*active,key)) for child in children])
        root = ET.fromstring(archive.read('3D/3dmodel.model'))
        items = root.findall('c:build/c:item',NS)
        if len(items) != 6:
            raise ValueError('Expected six separately placed printable objects')
        rows = []
        for item in items:
            points = vertices('3D/3dmodel.model',item.get('objectid'),matrix(item.get('transform')))[:,:3]
            lo,hi = points.min(axis=0),points.max(axis=0)
            if not np.isfinite(points).all() or abs(lo[2]) > .05:
                raise ValueError('Object is not on the bed')
            if np.any(lo[:2] < -.05) or np.any(hi[:2] > 256.05) or hi[2] > 256.05:
                raise ValueError('Object exceeds X1C build volume')
            rows.append(dict(object_id=item.get('objectid'),minimum_mm=lo.tolist(),maximum_mm=hi.tolist()))
        return dict(objects=rows,settings_pass=True,placement_pass=True,
                    limitations='Bounding-volume check only; no collision, brim, support or toolpath validation')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project',type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.project),indent=2))
