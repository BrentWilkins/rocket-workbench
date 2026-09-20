"""Paired, assumption-dependent flight experiments; not reliability certification."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

BASES = ((500, 50, "conical"), (500, 40, "ogive"), (530, 40, "ogive"))
SPAN_MM = 53.65384615384615
SEEDS = (20260919, 20260920)


def profile(levels, *, source="synthetic scenario", altitude_reference="AGL", elevation_m=0):
    """Canonical wind = [height AGL m, east m/s, north m/s], linear in vector space."""
    a = np.asarray(levels, dtype=float)
    if a.ndim != 2 or a.shape[1] != 3 or len(a) < 2 or not np.isfinite(a).all():
        raise ValueError("Wind needs at least two finite [height, east, north] levels")
    if altitude_reference not in ("AGL", "MSL"):
        raise ValueError("Wind altitude_reference must be AGL or MSL")
    if altitude_reference == "MSL":
        a[:, 0] -= elevation_m
    if np.any(np.diff(a[:, 0]) <= 0) or a[0, 0] > 0 or a[-1, 0] < 500:
        raise ValueError("Wind heights must increase and cover ground through 500 m AGL")
    return dict(levels=a.tolist(), source=source, altitude_reference="AGL",
                original_altitude_reference=altitude_reference,
                interpolation="linear east/north; endpoint held outside coverage")


def load_profile(path: Path, elevation_m: float):
    data = json.loads(path.read_text())
    for key in ("source", "timestamp", "latitude", "longitude", "altitude_reference", "units"):
        if key not in data:
            raise ValueError(f"Wind profile missing {key}")
    if data["units"] != {"height": "m", "velocity": "m/s"}:
        raise ValueError("Wind profile units must be m and m/s")
    result = profile(data["levels"], source=data["source"],
                     altitude_reference=data["altitude_reference"], elevation_m=elevation_m)
    result.update({k: data[k] for k in ("timestamp", "latitude", "longitude")})
    result["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def constant_wind(speed, heading):
    # Heading is the direction the wind blows TOWARD, clockwise from north.
    east, north = speed * math.sin(math.radians(heading)), speed * math.cos(math.radians(heading))
    return profile([[0, east, north], [1000, east, north]])


def scenarios():
    out = []
    for guide in (.9144, 1.524):
        for speed in (0, 2, 4, 6):
            for heading in ((0,) if speed == 0 else (0, 90)):
                out.append(dict(id=f"rod{guide:g}-wind{speed}-heading{heading}",
                                guide_m=guide, wind=constant_wind(speed, heading),
                                turbulence_m_s=0., tilt_deg=0., tilt_heading_deg=0., seed=SEEDS[0]))
        for name, levels in (("shear", [[0, 0, 2], [100, 0, 4], [500, 0, 6], [1000, 0, 6]]),
                             ("veer", [[0, 0, 2], [100, 2, 3], [500, 6, 0], [1000, 6, 0]])):
            out.append(dict(id=f"rod{guide:g}-{name}", guide_m=guide, wind=profile(levels),
                            turbulence_m_s=0., tilt_deg=0., tilt_heading_deg=0., seed=SEEDS[0]))
    for tilt in (0., 2.):
        out.append(dict(id=f"turbulence-tilt{tilt:g}", guide_m=.9144, wind=constant_wind(4, 90),
                        turbulence_m_s=.5, tilt_deg=tilt, tilt_heading_deg=0., seed=SEEDS[0]))
    return out


def samples(n, seed, roles):
    """Independent per-variable streams: prefix and variable-set stable across run counts.

    Uniform bounds are exploratory engineering assumptions, NOT measured likelihoods.
    Mass coordinates interpolate nominal/upper component records jointly.
    """
    def draws(name, low=0., high=1.):
        salt = int.from_bytes(hashlib.sha256(name.encode()).digest()[:4], "little")
        return np.random.default_rng(np.random.SeedSequence([seed, salt])).uniform(low, high, n)
    columns = {f"mass:{role}": draws(f"mass:{role}") for role in sorted(roles)}
    columns.update(wind_speed_m_s=draws("wind_speed", 0, 6), heading_deg=draws("heading", 0, 360),
                   shear_m_s=draws("shear", -2, 2), veer_deg=draws("veer", -30, 30),
                   tilt_deg=draws("tilt", 0, 2), tilt_heading_deg=draws("tilt_heading", 0, 360),
                   finish_g=draws("finish", 0, 5), turbulence_m_s=draws("turbulence", 0, .5))
    out = []
    for i in range(n):
        d = {k: float(v[i]) for k, v in columns.items()}
        low = constant_wind(d["wind_speed_m_s"], d["heading_deg"])["levels"][0][1:]
        high = constant_wind(max(0, d["wind_speed_m_s"] + d["shear_m_s"]),
                             d["heading_deg"] + d["veer_deg"])["levels"][0][1:]
        d.update(id=f"s{seed}-{i:04d}", seed=int(np.random.SeedSequence([seed, i]).generate_state(1)[0] % (2**31-1)),
                 index=i, master_seed=seed, guide_m=.9144,
                 wind=profile([[0, *low], [500, *high], [1000, *high]], source="exploratory sampled synthetic profile"))
        out.append(d)
    return out


def flight_metrics(result):
    """Additional free-flight metrics. No substitution for missing event/data evidence."""
    a = {k: np.asarray(v, dtype=float) for k, v in result["timeseries"].items()}
    t = a["time_s"]
    events = {}
    for e in result["events"]:
        events.setdefault(e["type"], e["time_s"])
    rod, burnout = events.get("LAUNCHROD"), events.get("BURNOUT")
    dep, apogee = events.get("RECOVERY_DEVICE_DEPLOYMENT"), events.get("APOGEE")
    tilt = np.degrees(np.abs(np.pi / 2 - a["orientation_theta_rad"]))
    aoa = np.degrees(a["angle_of_attack_rad"])
    stability = (a["cp_x_m"] - a["cg_x_m"]) / a["reference_length_m"]
    def at(values, when):
        if when is None or when < t[0] or when > t[-1]:
            return None
        # Keep first sample at an event boundary; no interpolation across deployment discontinuity.
        unique, idx = np.unique(t, return_index=True)
        value = np.interp(when, unique, values[idx])
        return float(value) if np.isfinite(value) else None
    def extreme(values, mask, fn):
        v = values[mask]
        return float(fn(v)) if v.size and np.isfinite(v).all() else None
    free_powered = np.zeros(t.shape, dtype=bool)
    if rod is not None and burnout is not None:
        free_powered = (t >= rod) & (t <= burnout) & (a["thrust_n"] > 0)
    coast = np.zeros(t.shape, dtype=bool)
    if burnout is not None and apogee is not None:
        coast = (t > burnout) & (t < min(apogee, dep if dep is not None else apogee))
    rates = np.degrees(np.hypot(a["pitch_rate_rad_s"], a["yaw_rate_rad_s"]))
    return dict(rod_exit_time_s=rod, burnout_time_s=burnout, guide_exit_aoa_deg=at(aoa, rod),
                powered_min_stability_cal=extreme(stability, free_powered, np.min),
                powered_max_aoa_deg=extreme(aoa, free_powered, np.max),
                powered_max_tilt_deg=extreme(tilt, free_powered, np.max),
                powered_max_pitch_yaw_rate_deg_s=extreme(rates, free_powered, np.max),
                burnout_tilt_deg=at(tilt, burnout), coast_max_aoa_deg=extreme(aoa, coast, np.max),
                burnout_trajectory_tilt_deg=at(np.degrees(np.arccos(np.clip(np.divide(
                    a["velocity_z_m_s"], a["speed_m_s"], out=np.ones_like(t), where=a["speed_m_s"] > 1e-8), -1, 1))), burnout))


def configure_wind(engine, sim, scenario):
    """Dense vector interpolation avoids OR's speed/direction interpolation changing our profile."""
    opts = sim.getOptions()
    opts.setLaunchRodLength(scenario["guide_m"])
    opts.setLaunchRodAngle(math.radians(scenario["tilt_deg"]))
    opts.setLaunchRodDirection(math.radians(scenario["tilt_heading_deg"]))
    opts.setRandomSeed(scenario["seed"])
    opts.setWindModelType(engine.core.models.wind.WindModelType.MULTI_LEVEL)
    wind = opts.getMultiLevelWindModel()
    wind.clearLevels()
    wind.setAltitudeReference(engine.core.models.wind.WindModel.AltitudeReference.AGL)
    a = np.asarray(scenario["wind"]["levels"])
    heights = np.unique(np.r_[a[:, 0], np.arange(0, a[-1, 0]+1, 10)])
    for h in heights:
        east, north = [float(np.interp(h, a[:, 0], a[:, k])) for k in (1, 2)]
        speed = math.hypot(east, north)
        # Native OR convention verified against model velocity in integration tests.
        # OR's vector is the opposing air velocity (added to rocket velocity),
        # unlike our physical wind-TOWARD vector and RocketPy's wind components.
        direction = (math.atan2(east, north) + math.pi) % (2*math.pi)
        wind.addWindLevel(float(h), speed, direction, float(scenario["turbulence_m_s"]))
    # OR 24.12 creates each level with a random constructor seed, independently
    # of SimulationOptions.randomSeed. Its level wrapper exposes no seed/model
    # setter. Replace only that protected model with the public seeded model;
    # fail loudly if the pinned Java API changes. Cloning preserves these seeds.
    for i, level in enumerate(wind.getLevels()):
        seed = int(np.random.SeedSequence([scenario["seed"], i]).generate_state(1)[0] % (2**31-1))
        model = engine.core.models.wind.PinkNoiseWindModel(seed)
        model.setAverage(level.getSpeed())
        model.setDirection(level.getDirection())
        model.setStandardDeviation(level.getStandardDeviation())
        field = level.getClass().getDeclaredField("model")
        field.setAccessible(True)
        field.set(level, model)


def quantiles(values):
    a = np.asarray([v for v in values if v is not None and np.isfinite(v)], dtype=float)
    if not len(a):
        return dict(valid=0, p05=None, median=None, p95=None)
    return dict(valid=len(a), p05=float(np.quantile(a, .05)), median=float(np.median(a)),
                p95=float(np.quantile(a, .95)))
