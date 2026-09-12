"""Generate explicit demonstration inputs; never substitutes actual measurements."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def q(value, unit, source='Provisional design choice; must be checked against selected parts'):
    return dict(value=value, unit=unit, provenance='demonstration assumption', source=source)


data = dict(
    schema_version=1, name='bt60-demonstration', mode='baseline', material='PLA',
    density=q(1.24, 'g/cm3', 'Full solid volume density assumption; replace with slicer and measured mass'),
    geometry={key: q(value, 'mm') for key, value in dict(
        body_od=41.6, body_id=40.5, body_length=300, nose_length=70,
        wall=1.2, clearance=0.2, bay_length=65, fin_root=65, fin_tip=28,
        fin_span=35, fin_sweep=25, fin_thickness=1.6, collar_length=65, fairing_length=8,
        motor_mount_id=18.2, motor_mount_od=19.8, motor_mount_length=75, motor_overhang=3.2,
        chute_diameter=305, chute_packed_length=65, chute_packed_diameter=30,
    ).items()},
    purchased_masses=[dict(role=role, name=name, mass=q(m, 'g'), x=q(x, 'mm')) for role, name, m, x in [
        ('body', 'BT-60 cardboard airframe', 15, 220),
        ('mount', '18 mm motor mount tube, thrust ring, hook, two centering rings and adhesive', 8, 332.5),
        ('chute', 'Estes 12 inch parachute and lines', 6, 180),
        ('harness', 'Kevlar leader, elastic harness, swivel and knots', 5, 165),
        ('wadding', 'Recovery wadding', 2, 240),
        ('lugs', 'Two paper launch lugs and adhesive', 1, 215),
        ('bay_hardware', 'Bulkhead eye bolt, washers, nuts, sled screws and cable ties', 5, 130),
        ('collar_adhesive', 'Fin collar adhesive and tapered lip fillet', 1.5, 337.5),
        ('thermal', 'Flame-resistant bay shield and perimeter seal allowance', 2, 136),
    ]],
    payload=dict(identity=None, battery_identity=None,
                 length=q(45, 'mm'), width=q(25, 'mm'), height=q(16, 'mm'),
                 mass=q(18, 'g'), cg_x=q(103, 'mm'), external_protrusions=False),
    launch=dict(elevation=q(1600, 'm', 'Demonstration altitude, not an identified launch site'),
                latitude=q(40, 'deg'), longitude=q(-105, 'deg'), guide_length=q(0.9144, 'm'),
                guide_angle=q(0, 'deg'), guide_direction=q(0, 'deg'), wind_direction=q(90, 'deg'),
                wind_speeds=[q(0, 'm/s'), q(2, 'm/s')], seed=42, atmosphere='ISA',
                time_step=q(0.01, 's'), max_time=q(300, 's')),
    motors=[dict(designation=d, delay_s=delay, digest=digest,
                 max_liftoff_mass=dict(value={'A8':85, 'B4':99, 'C6':113}[d], unit='g',
                     provenance='manufacturer specification',
                     source=f'https://estesrockets.com/products/{d.lower()}-{delay}-engines ; Technical Specifications, checked 2026-09-12')) for d, delay, digest in [
        ('A8', 3, '22aec01287ea1e3b8c6f66b26fe5fea6'),
        ('B4', 4, 'c15b9b96bf06e0ab896394787da3c47e'),
        ('C6', 3, 'c8743ef3fa99e14a89885cbe0ead47b2'),
        ('C6', 5, 'c8743ef3fa99e14a89885cbe0ead47b2'),
    ]],
    chute_cd=q(0.75, '1', 'Engineering estimate for flat plastic chute; no measured Cd'),
    criteria=[dict(metric=metric, minimum=lo, maximum=hi, unit=unit,
                   source='Project engineering assumption for demonstration screening; not a launch clearance',
                   kind='engineering assumption') for metric, lo, hi, unit in [
        ('apogee_m', 30, 120, 'm'), ('guide_departure_m_s', 12, None, 'm/s'),
        ('minimum_ascent_stability_cal', 1, None, 'cal'),
        ('deployment_speed_m_s', None, 10, 'm/s'), ('landing_descent_m_s', None, 6, 'm/s'),
    ]],
)

if __name__ == '__main__':
    (ROOT / 'examples/baseline.yaml').write_text(json.dumps(data, indent=2) + '\n')
    data.update(name='upstream-reference', mode='reference', reference_file='upstream-simple.ork')
    (ROOT / 'examples/reference.yaml').write_text(json.dumps(data, indent=2) + '\n')
