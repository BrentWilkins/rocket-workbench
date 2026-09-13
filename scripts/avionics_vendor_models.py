"""Fetch checksum-pinned vendor references and export a local XIAO detail assembly.

Vendor files stay in ignored cache/deliverables; do not redistribute without
checking their individual licensing and attribution terms.
"""
import argparse
import hashlib
import json
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = {
    'xiao.zip': ('https://files.seeedstudio.com/wiki/XIAO-BLE/seeed-studio-xiao-nrf52840-3d-model.zip',
                 '0ee799787103e54f382a784abd425e841401934356d4e083308cb0f083bf63a8'),
    'bmp581.brd': ('https://raw.githubusercontent.com/adafruit/Adafruit-BMP5xx-Temperature-and-Pressure-Sensor-PCB/main/Adafruit%20BMP581%20Temperature%20and%20Pressure%20Sensor%20rev%20B.brd',
                   'bdf695b3f2390d46d440a767e2737d656e98016c7cdec45f7db7f6111975e64f'),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='deliverables/avionics-vendor-reference')
    args = parser.parse_args()
    cache = ROOT/'.cache/avionics-vendor'
    cache.mkdir(parents=True, exist_ok=True)
    for name, (url, digest) in ASSETS.items():
        path = cache/name
        data = path.read_bytes() if path.exists() else urllib.request.urlopen(url, timeout=30).read()
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f'Vendor source changed: {name}; review before replacing the expected hash')
        if not path.exists():
            path.write_bytes(data)
    step = cache/'XIAO-nRF52840 v15.step'
    with zipfile.ZipFile(cache/'xiao.zip') as archive:
        data = archive.read(step.name)
    if hashlib.sha256(data).hexdigest() != '7aae140f838ec4ccf624e1902c56fb5ad1161d8dc3b0d759ba379d1a83d75890':
        raise ValueError('XIAO STEP differs')
    if not step.exists():
        step.write_bytes(data)
    elif step.read_bytes() != data:
        raise ValueError('Cached extracted STEP differs from pinned archive; refusing to overwrite it')
    import cadquery as cq
    from study_avionics import avionics_config
    from rocket_workbench.avionics import keepouts, components
    config = avionics_config()
    model = cq.importers.importStep(str(step))
    # Largest solid is the PCB. Align its center to the shared header datum;
    # the USB connector makes the full assembly bounding-box center asymmetric.
    pcb = max(model.solids().vals(), key=lambda s: s.Volume())
    b = pcb.BoundingBox()
    model = model.translate((-(b.xmin+b.xmax)/2, -(b.ymin+b.ymax)/2, -(b.zmin+b.zmax)/2))
    model = model.rotate((0,0,0), (0,1,0), 90).translate((0,-6.625,89))
    keepout = keepouts(config)['xiao-sense']
    # Vendor assembly includes separate component/surface entities; check its
    # complete bounding box, not Boolean subtraction of a non-fused assembly.
    actual, allowed = model.val().BoundingBox(), keepout.val().BoundingBox()
    if any(getattr(actual, axis+'min') < getattr(allowed, axis+'min')-1e-6 or
           getattr(actual, axis+'max') > getattr(allowed, axis+'max')+1e-6 for axis in 'xyz'):
        raise ValueError('Vendor XIAO exceeds packaging envelope')
    out = ROOT/args.output
    out.mkdir(parents=True, exist_ok=False)
    assembly = cq.Assembly(name='vendor-xiao-with-provisional-other-hardware')
    assembly.add(model, name='vendor-xiao', color=cq.Color('green'))
    for name, part in keepouts(config).items():
        if name != 'xiao-sense':
            assembly.add(part, name=name+'-KEEP OUT', color=cq.Color(.9,.6,.1,.4))
    assembly.export(str(out/'avionics-vendor-reference.step'))
    (out/'sources.json').write_text(json.dumps(dict(assets=ASSETS, components=components(),
        note='XIAO vendor visual reference; exact delivered Sense revision unverified. Other solids are provisional keepouts, not vendor models.'), indent=2)+'\n')
    print(out)


if __name__ == '__main__':
    main()
