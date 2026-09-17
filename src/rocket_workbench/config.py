"""Versioned physical inputs. Lengths are mm; axial origin is the nose tip."""
from __future__ import annotations

import math
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator


class Model(BaseModel):
    model_config = ConfigDict(extra='forbid', allow_inf_nan=False)


class Quantity(Model):
    value: float | None
    unit: Literal['mm', 'g', 'g/cm3', 'm', 'm/s', 'deg', 's', 'cal', '1']
    provenance: Literal['measured', 'manufacturer specification', 'estimate', 'demonstration assumption']
    source: str = Field(min_length=1)

    def require(self, unit: str, positive: bool = False) -> float:
        if self.unit != unit:
            raise ValueError(f'Expected {unit}, received {self.unit}: {self.source}')
        if self.value is None:
            raise ValueError(f'Missing {unit} input: {self.source}')
        if positive and self.value <= 0:
            raise ValueError(f'Expected positive {unit}: {self.source}')
        return self.value


class Geometry(Model):
    body_od: Quantity
    body_id: Quantity
    body_length: Quantity
    nose_length: Quantity
    wall: Quantity
    clearance: Quantity
    bay_length: Quantity
    fin_root: Quantity
    fin_tip: Quantity
    fin_span: Quantity
    fin_sweep: Quantity
    fin_thickness: Quantity
    collar_length: Quantity
    fairing_length: Quantity
    motor_mount_id: Quantity
    motor_mount_length: Quantity
    motor_mount_od: Quantity
    motor_overhang: Quantity
    chute_diameter: Quantity
    chute_packed_length: Quantity
    chute_packed_diameter: Quantity

    def mm(self, name: str) -> float:
        return getattr(self, name).require('mm', positive=True)


class MassItem(Model):
    role: Literal['body', 'mount', 'chute', 'harness', 'wadding', 'lugs', 'bay_hardware', 'collar_adhesive', 'thermal']
    name: str
    mass: Quantity
    x: Quantity


class Payload(Model):
    identity: str | None
    battery_identity: str | None
    length: Quantity
    width: Quantity
    height: Quantity
    mass: Quantity
    cg_x: Quantity
    external_protrusions: bool = False


class Launch(Model):
    elevation: Quantity
    latitude: Quantity
    longitude: Quantity
    guide_length: Quantity
    guide_angle: Quantity
    guide_direction: Quantity
    wind_direction: Quantity
    wind_speeds: list[Quantity] = Field(min_length=1)
    seed: int = Field(ge=0, le=2147483647)
    atmosphere: Literal['ISA']
    time_step: Quantity
    max_time: Quantity


MOTOR_DIMENSIONS_MM = {
    'A8': (18.0, 70.0), 'B4': (18.0, 70.0), 'C6': (18.0, 70.0), 'C5': (18.0, 70.0),
    'C11': (24.0, 70.0), 'D12': (24.0, 70.0), 'E12': (24.0, 95.0),
}


class MotorCase(Model):
    designation: Literal['A8', 'B4', 'C6', 'C5', 'C11', 'D12', 'E12']
    delay_s: float = Field(gt=0)
    digest: str = Field(pattern=r'^[0-9a-f]{32}$')
    max_liftoff_mass: Quantity

    @property
    def dimensions_mm(self):
        return MOTOR_DIMENSIONS_MM[self.designation]

    @model_validator(mode='after')
    def mass_limit(self):
        self.max_liftoff_mass.require('g', True)
        return self


class Criterion(Model):
    metric: str
    minimum: float | None = None
    maximum: float | None = None
    unit: str
    source: str
    kind: Literal['engineering assumption', 'manufacturer requirement']

    @model_validator(mode='after')
    def limits(self):
        units = {'apogee_m': 'm', 'guide_departure_m_s': 'm/s',
                 'minimum_ascent_stability_cal': 'cal', 'deployment_speed_m_s': 'm/s',
                 'landing_descent_m_s': 'm/s', 'landing_displacement_m': 'm'}
        if self.metric not in units or self.unit != units[self.metric]:
            raise ValueError('Unsupported criterion metric or incorrect unit')
        if self.minimum is None and self.maximum is None:
            raise ValueError('A criterion must specify at least one limit')
        if self.minimum is not None and self.maximum is not None and self.minimum > self.maximum:
            raise ValueError('Criterion minimum exceeds maximum')
        if not self.source.strip():
            raise ValueError('Criterion source is required')
        return self


class Config(Model):
    schema_version: Literal[1]
    name: str = Field(pattern=r'^[a-z0-9-]+$')
    mode: Literal['reference', 'baseline']
    reference_file: str | None = None
    geometry: Geometry
    nose_shape: Literal['conical', 'ogive', 'ellipsoid'] = 'conical'
    fin_shape: Literal['trapezoidal', 'elliptical', 'clipped-delta', 'swept'] = 'trapezoidal'
    fin_profile: Literal['square', 'organic-v2'] = 'square'
    avionics_profile: Literal['xiao-gnss-baro-v1'] | None = None
    bay_retention: Literal['printed-pilots', 'm2-insert-trial-v1'] = 'printed-pilots'
    material: Literal['PLA', 'PETG']
    density: Quantity
    purchased_masses: list[MassItem]
    payload: Payload
    launch: Launch
    motors: list[MotorCase] = Field(min_length=1)
    criteria: list[Criterion]
    chute_cd: Quantity
    printed_measurements: dict[str, tuple[Quantity, Quantity]] = Field(default_factory=dict)

    @model_validator(mode='after')
    def feasible(self):
        if self.bay_retention != 'printed-pilots' and not self.avionics_profile:
            raise ValueError('Insert trial requires the specified avionics layout')
        if self.fin_profile == 'organic-v2' and self.fin_shape != 'clipped-delta':
            raise ValueError('Organic fin profile v2 is defined only for clipped-delta fins')
        g = self.geometry
        for name in Geometry.model_fields:
            g.mm(name)
        od, bore, wall = g.mm('body_od'), g.mm('body_id'), g.mm('wall')
        if bore >= od:
            raise ValueError('Body ID must be smaller than OD')
        if not 38 <= bore <= 43 or not .8 <= wall <= 2:
            raise ValueError('V1 bay fixtures support 38–43 mm body ID and 0.8–2 mm walls only')
        if g.mm('clearance') > .5 or g.mm('nose_length') < 30 or g.mm('bay_length') < 30:
            raise ValueError('Clearance must be <=0.5 mm; nose and bay must be >=30 mm')
        if g.mm('collar_length') + g.mm('fairing_length') >= g.mm('body_length'):
            raise ValueError('Collar and fairing must fit on body')
        if .65*g.mm('body_length') + 25 > g.mm('body_length')-g.mm('collar_length')-g.mm('fairing_length'):
            raise ValueError('Aft launch-lug sleeve overlaps collar fairing; increase body length')
        if g.mm('fin_tip') + g.mm('fin_sweep') > g.mm('fin_root'):
            raise ValueError('Fin tip + sweep must fit inside root chord')
        if g.mm('fin_root') > g.mm('collar_length'):
            raise ValueError('Fin root must fit on collar')
        if g.mm('motor_mount_id') >= g.mm('motor_mount_od') or g.mm('motor_mount_od') >= bore:
            raise ValueError('Motor mount ID < mount OD < body ID required')
        for motor in self.motors:
            diameter, length = motor.dimensions_mm
            if g.mm('motor_mount_id') < diameter or g.mm('motor_mount_length')+g.mm('motor_overhang') < length:
                raise ValueError(f'{motor.designation}: {diameter:g} × {length:g} mm motor does not fit mount')
        available = g.mm('body_length') - g.mm('bay_length') - g.mm('motor_mount_length') - g.mm('motor_overhang') - 15
        if g.mm('chute_packed_length') > available or g.mm('chute_packed_diameter') + 4 > bore:
            raise ValueError('Recovery packing envelope and routing clearance do not fit')
        p = self.payload
        w, h = p.width.require('mm', True), p.height.require('mm', True)
        inner = bore - 2 * g.mm('clearance') - 2 * wall
        # Sled thickness 2 mm and 2 mm installation clearance per side.
        if not self.avionics_profile and math.hypot(w + 4, h + 6) > inner:
            raise ValueError('Avionics cross-section plus sled/service clearance exceeds bay bore')
        if not self.avionics_profile and (w < 20 or math.hypot((w+4)/2, 12) > inner/2):
            raise ValueError('V1 sled must cover its two mounting holes and fit at its actual offset in the bay')
        if self.avionics_profile:
            from .avionics import components
            for part in components(self):
                x, y, z = part['center_mm']
                dx, dy, dz = part['dimensions_mm']
                if math.hypot(abs(x)+dx/2, abs(y)+dy/2) >= inner/2:
                    raise ValueError('Avionics component keepout exceeds actual bay bore')
                if 2*abs(x)+dx > w or 2*abs(y)+dy > h or z+dz/2 > p.length.require('mm', True):
                    raise ValueError('Payload declared envelope omits component/routing space')
        if p.length.require('mm', True) + 15 > g.mm('bay_length'):
            raise ValueError('Avionics axial envelope plus service clearance exceeds bay length')
        p.mass.require('g', True)
        if self.avionics_profile and (g.mm('bay_length') < 145 or g.mm('body_length') < 410):
            raise ValueError('V1 static-port avionics requires bay >=145 mm and body >=410 mm')
        if self.avionics_profile:
            chute_end = self.mass_item('chute').x.value + g.mm('chute_packed_length')/2
            mount_start = g.mm('nose_length')+g.mm('body_length')-g.mm('motor_mount_length')-g.mm('motor_overhang')
            wadding = self.mass_item('wadding').x.value
            if not chute_end+5 <= wadding <= mount_start-5:
                raise ValueError('Avionics recovery wadding 10 mm allowance must lie between packed chute and motor mount')
        if not g.mm('nose_length')+5 <= p.cg_x.require('mm') <= g.mm('nose_length') + g.mm('bay_length')-10:
            raise ValueError('Payload CG must be within the nose/bay region')
        if p.external_protrusions:
            raise ValueError('External camera/antenna geometry is unsupported; cannot silently ignore drag')
        self.density.require('g/cm3', True)
        self.chute_cd.require('1', True)
        roles = [i.role for i in self.purchased_masses]
        required = {'body', 'mount', 'chute', 'harness', 'wadding', 'lugs', 'bay_hardware', 'collar_adhesive', 'thermal'}
        if set(roles) != required or len(roles) != len(required):
            raise ValueError(f'Purchased mass ledger must contain exactly one of each role: {sorted(required)}')
        if len({c.metric for c in self.criteria}) != len(self.criteria):
            raise ValueError('Duplicate evaluation criteria')
        for part, (mass, cg) in self.printed_measurements.items():
            if part not in {'nose-bay', 'bay-bulkhead', 'payload-sled', 'fin-collar', 'lug-sleeve-1', 'lug-sleeve-2'}:
                raise ValueError(f'Unknown printed part: {part}')
            mass.require('g', True)
            if not 0 <= cg.require('mm') <= g.mm('nose_length')+g.mm('body_length'):
                raise ValueError('Printed part CG outside rocket')
        for item in self.purchased_masses:
            item.mass.require('g', True)
            if not 0 <= item.x.require('mm') <= g.mm('nose_length') + g.mm('body_length'):
                raise ValueError(f'{item.name}: CG is outside rocket')
        for key, unit in [('elevation', 'm'), ('latitude', 'deg'), ('longitude', 'deg'),
                          ('guide_length', 'm'), ('guide_angle', 'deg'), ('guide_direction', 'deg'),
                          ('wind_direction', 'deg'), ('time_step', 's'), ('max_time', 's')]:
            getattr(self.launch, key).require(unit)
        if self.launch.guide_length.value <= 0 or not 0 <= self.launch.guide_angle.value <= 30:
            raise ValueError('Guide length must be positive; angle must be 0–30 degrees from vertical')
        if not -90 <= self.launch.latitude.value <= 90 or not -180 <= self.launch.longitude.value <= 180:
            raise ValueError('Invalid launch coordinates')
        if not 0 < self.launch.time_step.value <= 0.05 or self.launch.max_time.value <= 0:
            raise ValueError('Time step must be (0, 0.05] s; maximum time must be positive')
        for wind in self.launch.wind_speeds:
            if wind.require('m/s') < 0:
                raise ValueError('Wind speed cannot be negative')
        if self.mode == 'reference' and not self.reference_file:
            raise ValueError('Reference mode requires reference_file')
        return self

    def mass_item(self, role: str) -> MassItem:
        return next(i for i in self.purchased_masses if i.role == role)

    def missing(self) -> list[str]:
        out = []
        if not self.payload.identity:
            out.append('Exact XIAO board/camera/antenna identity and measured envelope')
        if not self.payload.battery_identity:
            out.append('Battery identity, connector/wire envelopes and retention measurements')
        for item in self.purchased_masses:
            if item.mass.provenance != 'measured':
                out.append(f'Measured mass and balance: {item.name}')
        out.append('Assembled mass/CG, print fit, attachment strength and recovery separation checks')
        if self.mode == 'baseline':
            out.append('V2 saddle bond strength and adhesive mass require physical checks; saddle-specific aerodynamic drag is unresolved')
        if self.avionics_profile:
            out.append('Avionics board/antenna/battery masses, stack clearances, retention, wiring and power must be measured; vendor CAD is not physical validation')
            out.append('Static-port drilling/alignment, bulkhead and screw seals, pressure lag and aerodynamic pressure bias require bench/flight validation')
        return out


def load_config(path: Path) -> Config:
    return Config.model_validate(yaml.safe_load(path.read_text()))


def mass_cg(items: list[tuple[float, float]]) -> tuple[float, float]:
    if not items or any(not math.isfinite(m) or m <= 0 or not math.isfinite(x) for m, x in items):
        raise ValueError('Mass accounting requires known positive masses and finite CG positions')
    mass = sum(m for m, _ in items)
    return mass, sum(m * x for m, x in items) / mass
