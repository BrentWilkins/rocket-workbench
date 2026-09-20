"""Pinned OpenRocket-owned orhelper adapter; one JVM per command process."""
from __future__ import annotations

import hashlib
import importlib.metadata
import json
import math
import os
import platform
from pathlib import Path

import numpy as np

from .config import Config, MotorCase

JAR_SHA256 = '4959b72f52f5f607941e9722abbb7b7f0c4a38ebbbf84204a329db9f31c4f897'
BRIDGE_REVISION = 'fb132c49e661bb00c5586cce6a4ac0c655425197'
ROOT = Path(__file__).resolve().parents[2]


def runtime():
    jar = Path(os.environ.get('ROCKET_JAR', ROOT / '.tools/OpenRocket-24.12.jar')).resolve()
    if not jar.is_file() or hashlib.sha256(jar.read_bytes()).hexdigest() != JAR_SHA256:
        raise ValueError('Pinned OpenRocket JAR missing or checksum differs; run scripts/bootstrap.py')
    jvm = os.environ.get('ROCKET_JVM')
    if not jvm:
        candidate = Path('/Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home/lib/server/libjvm.dylib')
        if candidate.exists():
            jvm = str(candidate)
        else:
            import jpype
            jvm = jpype.getDefaultJVMPath()
    direct = importlib.metadata.distribution('orhelper').read_text('direct_url.json')
    if direct is None or BRIDGE_REVISION not in json.loads(direct)['url']:
        raise ValueError('Installed orhelper does not match pinned OpenRocket-owned source')
    return jar, Path(jvm)


class Engine:
    def __enter__(self):
        import orhelper
        jar, jvm = runtime()
        self.instance = orhelper.OpenRocketInstance(jar=str(jar), jvm=str(jvm), loglevel='ERROR')
        self.instance.__enter__()
        self.helper = orhelper.Helper(self.instance)
        self.core = self.instance.openrocket_core
        if str(self.core.util.BuildProperties.getVersion()) != '24.12':
            raise ValueError('Wrong OpenRocket engine version')
        return self

    def __exit__(self, *args):
        return self.instance.__exit__(*args)

    def versions(self):
        import jpype
        return dict(openrocket=str(self.core.util.BuildProperties.getVersion()),
                    java=str(jpype.java.lang.System.getProperty('java.runtime.version')),
                    python=platform.python_version(), bridge_revision=BRIDGE_REVISION,
                    jar_sha256=JAR_SHA256,
                    packages={p: importlib.metadata.version(p) for p in ['orhelper', 'jpype1', 'numpy', 'pydantic']})

    def load(self, path: Path):
        import jpype
        loader = self.core.file.GeneralRocketLoader(jpype.java.io.File(str(path.resolve())))
        doc = loader.load()
        warnings = [str(w) for w in loader.getWarnings()]
        return doc, warnings

    def save(self, doc, path: Path):
        self.helper.save_doc(str(path.resolve()), doc)

    def new_simulation(self, doc):
        from .flight_model import CONFIG_ID
        sim = self.core.document.Simulation(doc, doc.getRocket())
        sim.setFlightConfigurationId(self.core.rocketcomponent.FlightConfigurationId(CONFIG_ID))
        doc.addSimulation(sim)
        return sim

    def configure(self, sim, config: Config, wind: float):
        opts = sim.getOptions()
        launch = config.launch
        opts.setLaunchAltitude(launch.elevation.value)
        opts.setLaunchLatitude(launch.latitude.value)
        opts.setLaunchLongitude(launch.longitude.value)
        opts.setISAAtmosphere(True)
        opts.setLaunchIntoWind(False)
        opts.setLaunchRodLength(launch.guide_length.value)
        opts.setLaunchRodAngle(math.radians(launch.guide_angle.value))
        opts.setLaunchRodDirection(math.radians(launch.guide_direction.value))
        opts.setWindModelType(self.core.models.wind.WindModelType.AVERAGE)
        opts.getAverageWindModel().setAverage(wind)
        # V1 scenarios deliberately use constant wind. Do not imply a vertical
        # wind profile or stochastic ensemble from these two scalar cases.
        opts.getAverageWindModel().setStandardDeviation(0)
        opts.getAverageWindModel().setDirection(math.radians(launch.wind_direction.value))
        opts.setRandomSeed(launch.seed)
        opts.setTimeStep(launch.time_step.value)
        opts.setMaxSimulationTime(launch.max_time.value)

    def motor(self, sim, case: MotorCase, config: Config):
        diameter, length = case.dimensions_mm
        motors = list(self.core.startup.Application.getMotorSetDatabase().findMotors(
            case.digest, self.core.motor.Motor.Type.SINGLE, 'Estes', case.designation, diameter/1000, length/1000))
        matches = [m for m in motors if str(m.getDigest()) == case.digest
                   and str(m.getDesignation()) == case.designation
                   and abs(m.getDiameter()*1000-diameter) < .01
                   and abs(m.getLength()*1000-length) < .01]
        if len(matches) != 1:
            raise ValueError(f'Exact motor curve {case.digest} not uniquely available')
        motor = matches[0]
        if motor.getDiameter()*1000 > config.geometry.motor_mount_id.value or motor.getLength()*1000 > config.geometry.motor_mount_length.value+config.geometry.motor_overhang.value:
            raise ValueError('Selected motor does not fit configured mount')
        if case.delay_s not in list(motor.getStandardDelays()):
            raise ValueError(f'Delay {case.delay_s} not in motor data standard delays')
        mounts = list(sim.getActiveConfiguration().getActiveMotors())
        if len(mounts) != 1:
            raise ValueError(f'Expected one motor mount, got {len(mounts)}')
        mounts[0].setMotor(motor)
        mounts[0].setEjectionDelay(case.delay_s)
        sim.getActiveConfiguration().update()
        return self.motor_record(motor, case.delay_s)

    @staticmethod
    def motor_record(motor, delay):
        return dict(manufacturer=str(motor.getManufacturer()), designation=str(motor.getDesignation()),
                    delay_s=delay, digest=str(motor.getDigest()), diameter_mm=motor.getDiameter()*1000,
                    length_mm=motor.getLength()*1000, loaded_mass_g=motor.getLaunchMass()*1000,
                    spent_mass_g=motor.getBurnoutMass()*1000,
                    source='OpenRocket 24.12 bundled motor database; identified by engine JAR SHA256 and curve digest',
                    description=str(motor.getDescription()), time_s=list(motor.getTimePoints()),
                    thrust_n=list(motor.getThrustPoints()),
                    mass_g=[p.weight*1000 for p in motor.getCGPoints()],
                    cg_from_front_mm=[p.x*1000 for p in motor.getCGPoints()])

    def mass(self, sim):
        calc = self.core.masscalc.MassCalculator
        config = sim.getActiveConfiguration()
        dry, launch = calc.calculateStructure(config), calc.calculateLaunch(config)
        return dict(dry_mass_g=dry.getMass()*1000, dry_cg_x_mm=dry.getCM().x*1000,
                    launch_mass_g=launch.getMass()*1000, launch_cg_x_mm=launch.getCM().x*1000,
                    dry_pitch_inertia_kg_m2=dry.getLongitudinalInertia(),
                    dry_roll_inertia_kg_m2=dry.getRotationalInertia(),
                    launch_pitch_inertia_kg_m2=launch.getLongitudinalInertia(),
                    launch_roll_inertia_kg_m2=launch.getRotationalInertia())

    def run(self, sim):
        import jpype
        # orhelper.Helper.run_simulation randomizes seed unconditionally. No
        # fork is needed: use its underlying public engine API with an empty
        # listener array, retaining the bridge's startup/load/save/extraction.
        listeners = jpype.JArray(self.core.simulation.listeners.SimulationListener)(0)
        error = None
        try:
            sim.simulate(listeners)
        except Exception as exc:
            error = f'{type(exc).__name__}: {exc}'
        result = dict(execution='simulation failed' if error else 'completed', error=error,
                      warnings=[], events=[], timeseries={}, metrics={})
        data = sim.getSimulatedData()
        if data is None or data.getBranchCount() == 0:
            result.update(execution='simulation failed', error=error or 'No flight data')
            return result
        result['warnings'] = [str(w) for w in data.getWarningSet()]
        branch = data.getBranch(0)
        result['events'] = [dict(type=str(e.getType().name()), time_s=float(e.getTime()),
                                 detail=str(e.getData()) if e.getData() is not None else None)
                            for e in branch.getEvents()]
        names = dict(time_s='TYPE_TIME', altitude_m='TYPE_ALTITUDE', velocity_z_m_s='TYPE_VELOCITY_Z',
                     speed_m_s='TYPE_VELOCITY_TOTAL', east_m='TYPE_POSITION_X', north_m='TYPE_POSITION_Y',
                     cg_x_m='TYPE_CG_LOCATION', cp_x_m='TYPE_CP_LOCATION', reference_length_m='TYPE_REFERENCE_LENGTH',
                     mass_kg='TYPE_MASS', mach='TYPE_MACH_NUMBER', sound_speed_m_s='TYPE_SPEED_OF_SOUND',
                     angle_of_attack_rad='TYPE_AOA', acceleration_m_s2='TYPE_ACCELERATION_TOTAL',
                     acceleration_z_m_s2='TYPE_ACCELERATION_Z', acceleration_xy_m_s2='TYPE_ACCELERATION_XY',
                     gravity_m_s2='TYPE_GRAVITY', thrust_n='TYPE_THRUST_FORCE',
                     orientation_theta_rad='TYPE_ORIENTATION_THETA',
                     orientation_phi_rad='TYPE_ORIENTATION_PHI',
                     pitch_rate_rad_s='TYPE_PITCH_RATE', yaw_rate_rad_s='TYPE_YAW_RATE',
                     roll_rate_rad_s='TYPE_ROLL_RATE', drag_coefficient='TYPE_DRAG_COEFF',
                     wind_speed_m_s='TYPE_WIND_VELOCITY', wind_direction_rad='TYPE_WIND_DIRECTION')
        raw = self.helper.get_timeseries(sim, names.values())
        time = np.asarray(raw['TYPE_TIME'], dtype=float)
        if time.ndim != 1 or not len(time):
            result.update(execution='simulation failed', error=error or 'No time samples')
            return result
        arrays = {}
        for key, name in names.items():
            value = np.asarray(raw[name], dtype=float)
            arrays[key] = value if value.ndim == 1 and len(value) == len(time) else np.full(len(time), np.nan)
        result['timeseries'] = {key: [float(v) if np.isfinite(v) else None for v in a] for key, a in arrays.items()}
        result['metrics'] = summarize(arrays, result['events'])
        result['engine_summary'] = {key: finite(value) for key, value in dict(
            apogee_m=data.getMaxAltitude(), guide_departure_m_s=data.getLaunchRodVelocity(),
            deployment_speed_m_s=data.getDeploymentVelocity(), landing_total_speed_m_s=data.getGroundHitVelocity()).items()}
        events = {e['type'] for e in result['events']}
        if 'SIM_ABORT' in events or 'GROUND_HIT' not in events:
            result.update(execution='simulation failed', error=error or 'Aborted or did not reach ground within maximum time')
        return result


def finite(value):
    return float(value) if math.isfinite(value) else None


def summarize(arrays, event_records):
    """Pure extraction boundary, tested with event transitions and missing data.

    Stability remains the full pre-deployment ascent minimum. No low-speed or
    high-angle samples are silently discarded to make a candidate pass.
    """
    t = arrays['time_s']
    events = {}
    for event in event_records:
        events.setdefault(event['type'], event['time_s'])
    ground = events.get('GROUND_HIT')

    def at(event, key):
        when = events.get(event)
        if when is None or not len(t) or when < t[0] or when > t[-1]:
            return None
        if event == 'RECOVERY_DEVICE_DEPLOYMENT' and ground is not None and when >= ground:
            return None
        # First sample at duplicate event timestamps: do not select a later,
        # post-transition zero velocity at the same timestamp.
        unique_t, first = np.unique(t, return_index=True)
        return finite(np.interp(when, unique_t, arrays[key][first]))

    departure, recovery, apogee = (events.get(k) for k in ['LAUNCHROD', 'RECOVERY_DEVICE_DEPLOYMENT', 'APOGEE'])
    end = min(x for x in [recovery, apogee, ground, float(t[-1])] if x is not None)
    ascent = (t >= departure) & (t < end) if departure is not None else np.zeros(len(t), dtype=bool)
    with np.errstate(invalid='ignore', divide='ignore'):
        stability = (arrays['cp_x_m']-arrays['cg_x_m'])/arrays['reference_length_m']
    valid = stability[ascent & np.isfinite(stability)]
    vz = at('GROUND_HIT', 'velocity_z_m_s')
    east, north = at('GROUND_HIT', 'east_m'), at('GROUND_HIT', 'north_m')
    result = dict(apogee_m=finite(np.nanmax(arrays['altitude_m'])),
        guide_departure_m_s=at('LAUNCHROD', 'speed_m_s'),
        minimum_ascent_stability_cal=float(valid.min()) if valid.size else None,
        deployment_time_s=recovery, deployment_altitude_m=at('RECOVERY_DEVICE_DEPLOYMENT', 'altitude_m'),
        deployment_speed_m_s=at('RECOVERY_DEVICE_DEPLOYMENT', 'speed_m_s'),
        deployment_before_ground=recovery is not None and ground is not None and recovery < ground,
        landing_descent_m_s=abs(vz) if vz is not None else None,
        landing_total_speed_m_s=at('GROUND_HIT', 'speed_m_s'),
        landing_east_m=east, landing_north_m=north,
        landing_displacement_m=math.hypot(east, north) if east is not None and north is not None else None)
    if valid.size:
        indices = np.flatnonzero(ascent & np.isfinite(stability))
        worst = indices[int(np.argmin(valid))]
        result['stability_minimum_time_s'] = float(t[worst])
        result['stability_minimum_speed_m_s'] = finite(arrays['speed_m_s'][worst])
        if 'angle_of_attack_rad' in arrays:
            result['stability_minimum_aoa_deg'] = finite(np.degrees(arrays['angle_of_attack_rad'][worst]))
    result.update(powered_metrics(arrays, event_records))
    return result


def powered_metrics(arrays, event_records):
    """Sampled single-stage powered-flight peaks, never deployment/impact peaks.

    Load estimate restores local gravity to the world-coordinate acceleration.
    It neglects Coriolis and sensor-offset rotational terms; it is not an IMU
    axis prediction or a board shock-survival assessment.
    """
    keys = ['acceleration_m_s2', 'acceleration_z_m_s2', 'acceleration_xy_m_s2',
            'gravity_m_s2', 'thrust_n']
    result = dict(powered_samples=0, powered_data_complete=False)
    for name in ['acceleration_g', 'specific_force_estimate_g', 'speed_m_s']:
        result[f'peak_powered_{name}'] = None
        result[f'peak_powered_{name}_time_s'] = None
    if any(k not in arrays for k in keys):
        return result
    events = {}
    for event in event_records:
        events.setdefault(event['type'], event['time_s'])
    start, stop = events.get('LIFTOFF'), events.get('BURNOUT')
    if start is None or stop is None or stop <= start:
        return result
    t = arrays['time_s']
    stop = min([stop] + [events[k] for k in ['GROUND_HIT', 'RECOVERY_DEVICE_DEPLOYMENT', 'SIM_ABORT'] if k in events])
    window = (t >= start) & (t < stop)
    powered = window & (arrays['thrust_n'] > 0)
    result['powered_samples'] = int(powered.sum())
    result['powered_data_complete'] = bool(powered.any() and
        np.isfinite(arrays['thrust_n'][window]).all() and
        all(np.isfinite(arrays[k][powered]).all() for k in keys + ['speed_m_s']))
    values = dict(acceleration_g=arrays['acceleration_m_s2']/9.80665,
                  specific_force_estimate_g=np.hypot(arrays['acceleration_xy_m_s2'],
                      arrays['acceleration_z_m_s2'] + arrays['gravity_m_s2'])/9.80665,
                  speed_m_s=arrays['speed_m_s'])
    for name, value in values.items():
        # Do not label a partial finite subset as a complete peak.
        if not powered.any() or not np.isfinite(arrays['thrust_n'][window]).all() or not np.isfinite(value[powered]).all():
            continue
        indices = np.flatnonzero(powered)
        index = indices[np.argmax(value[powered])]
        result[f'peak_powered_{name}'] = float(value[index])
        result[f'peak_powered_{name}_time_s'] = float(t[index])
    return result
