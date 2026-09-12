import importlib.util
from pathlib import Path
import xml.etree.ElementTree as ET


def test_plot_styles_are_distinct_and_stable(tmp_path):
    path = Path(__file__).resolve().parents[1]/'scripts/package_review.py'
    spec = importlib.util.spec_from_file_location('package_review', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cases = [dict(loading='actual', wind_m_s=0, motor=dict(designation=m,delay_s=d),
                  timeseries=dict(time_s=[0,1,2],altitude_m=[0,10,0]))
             for m,d in [('A8',3),('B4',4),('C6',3),('C6',5),('C5',3)]]
    observed = []
    for i, order in enumerate([cases, list(reversed(cases))]):
        output = tmp_path/f'{i}.svg'
        module.plot_altitude({'cases':order}, output)
        root = ET.parse(output).getroot()
        ns = {'s':'http://www.w3.org/2000/svg'}
        curves = root.findall('s:polyline', ns)
        mapping = {c.find('s:title',ns).text:(c.attrib['stroke'],c.attrib['stroke-dasharray']) for c in curves}
        assert len(mapping) == 5
        assert len({s[0] for s in mapping.values()}) == 5
        assert len({s[1] for s in mapping.values()}) == 5
        assert root.attrib['role'] == 'img'
        observed.append(mapping)
    assert observed[0] == observed[1]
