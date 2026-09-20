"""Build the current D12 fin-tip and nose-tip print review as new artifacts."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import cadquery as cq

from rocket_workbench.cad import build
from rocket_workbench.config import Config

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.prepare_organic_fin import organic_config, render


def refined_config() -> Config:
    data = organic_config().model_dump()
    data['name'] = 'd12-conical-n50-b500-tip-refinement-v3'
    data['fin_profile'] = 'organic-v3'
    for name, value, reason in (
        ('nose_tip_radius', 1.0, 'Tangent spherical nose cap for primer and sanding'),
        ('nose_shoulder_chamfer', 0.3, 'Outer shoulder lead-in for tube insertion'),
    ):
        data['geometry'][name] = dict(
            value=value, unit='mm', provenance='estimate', source=reason)
    return Config.model_validate(data)


def bending_screen(config: Config) -> dict:
    """Relative elastic tip-load compliance; modulus and load cancel."""
    g = config.geometry
    span, root = g.mm('fin_span'), g.mm('fin_root')
    station = np.linspace(0, span, 10001)
    chord = root * (1 - .8 * station / span)
    full = np.full_like(station, g.mm('fin_thickness'))
    tapered = np.where(station <= span - 8, full,
                       full - (full - .8) * (station - (span - 8)) / 8)

    def compliance(thickness):
        return float(np.trapezoid((span - station)**2 / (chord * thickness**3), station))

    return {
        'model': 'Euler-Bernoulli cantilever, unit lateral tip load, rectangular local section',
        'tip_load_compliance_ratio_v3_to_full_thickness': compliance(tapered) / compliance(full),
        'root_thickness_mm': float(tapered[0]),
        'limits': 'Geometry-only comparison; excludes printed layer bonds, root cove, impact and flutter. Not a strength rating.',
    }


def section_diagram(destination: Path) -> None:
    """Schematic end view of the symmetric outer-span taper."""
    destination.write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" role="img" aria-label="Fin section: full 2 mm thickness, symmetric 8 mm taper to 0.8 mm at the outer tip">
<rect width="800" height="350" fill="#f5f8fc"/>
<text x="42" y="48" font-family="sans-serif" font-size="25" fill="#17324d">Outboard fin section (schematic)</text>
<path d="M 90 120 L 310 120 L 710 156 L 710 194 L 310 230 L 90 230 Z" fill="#1467a7" stroke="#0b3556" stroke-width="3"/>
<line x1="310" y1="98" x2="710" y2="98" stroke="#17324d" stroke-width="2" marker-start="url(#a)" marker-end="url(#a)"/>
<text x="447" y="88" font-family="sans-serif" font-size="19" fill="#17324d">8 mm taper</text>
<line x1="65" y1="120" x2="65" y2="230" stroke="#17324d" stroke-width="2"/>
<text x="30" y="277" font-family="sans-serif" font-size="18" fill="#17324d">2.0 mm</text>
<line x1="735" y1="156" x2="735" y2="194" stroke="#17324d" stroke-width="2"/>
<text x="686" y="278" font-family="sans-serif" font-size="18" fill="#17324d">0.8 mm</text>
<text x="90" y="318" font-family="sans-serif" font-size="17" fill="#435b6e">Fin root and most of span stay full thickness</text>
<defs><marker id="a" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M 0 4 L 8 0 L 8 8 Z" fill="#17324d"/></marker></defs>
</svg>\n''')


def record_flight(run: Path, destination: Path, config: Config) -> None:
    result_path = run / 'results.json'
    raw = result_path.read_bytes()
    result = json.loads(raw)
    digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
    if result['configuration_sha256'] != digest:
        raise ValueError('Flight run does not match tip-refinement configuration')
    rows = []
    for case in result['cases']:
        metrics = case['metrics']
        rows.append({
            'id': case['id'],
            'execution': case['execution'],
            'status': case['evaluation']['status'],
            'criteria_passed': all(check['passed'] for check in case['evaluation']['checks']),
            **{key: metrics[key] for key in (
                'guide_departure_m_s', 'minimum_ascent_stability_cal',
                'apogee_m', 'landing_descent_m_s')},
        })
    summary = {
        'source_run': run.name,
        'results_sha256': hashlib.sha256(raw).hexdigest(),
        'configuration_sha256': digest,
        'completed_cases': sum(row['execution'] == 'completed' for row in rows),
        'configured_criteria_passed': sum(row['criteria_passed'] for row in rows),
        'missing_inputs': result['missing_inputs'],
        'cases': rows,
    }
    destination.write_text(json.dumps(summary, indent=2) + '\n')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--flight-run', type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    config = refined_config()
    (args.output / 'config.json').write_text(json.dumps(config.model_dump(), indent=2) + '\n')
    records = build(config, args.output / 'cad')
    # Capture the small roundover accurately in the two revised print meshes.
    for name in ('nose-bay', 'fin-collar'):
        part = cq.importers.importStep(str(args.output / 'cad' / f'{name}.step'))
        printable = part.rotate((0, 0, 0), (1, 0, 0), 180)
        bottom = printable.val().BoundingBox().zmin
        cq.exporters.export(printable.translate((0, 0, -bottom)),
                            str(args.output / 'cad' / f'{name}.stl'),
                            tolerance=.01, angularTolerance=.05)
    keep = {'assembly.step', 'fin-collar.step', 'nose-bay.step',
            'mass-properties.json', *(f'{name}.stl' for name in
              ('nose-bay', 'bay-bulkhead', 'payload-sled', 'fin-collar',
               'lug-sleeve-1', 'lug-sleeve-2'))}
    for path in (args.output / 'cad').iterdir():
        if path.name not in keep:
            path.unlink()
    render(config, args.output / 'fin-collar-review.png')
    section_diagram(args.output / 'fin-tip-section.svg')
    summary = {
        'configuration': config.name,
        'nose_tip_radius_mm': config.geometry.mm('nose_tip_radius'),
        'nose_shoulder_chamfer_mm': config.geometry.mm('nose_shoulder_chamfer'),
        'fin_tip_taper_length_mm': 8.0,
        'fin_tip_land_mm': 0.8,
        'mass_g_solid_density_estimate': {
            name: records[name]['mass_g'] for name in ('nose-bay', 'fin-collar')},
        'structural_screen': bending_screen(config),
        'print_status': 'CAD review; inspect actual slice and bend-test a printed collar',
    }
    (args.output / 'design-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    if args.flight_run is not None:
        record_flight(args.flight_run, args.output / 'flight-screen.json', config)
    files = sorted(path for path in args.output.rglob('*') if path.is_file())
    (args.output / 'SHA256SUMS').write_text(''.join(
        f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(args.output)}\n'
        for path in files))
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
