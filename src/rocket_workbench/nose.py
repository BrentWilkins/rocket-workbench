"""Analytic nose profiles matching OpenRocket release-24.12 Transition.Shape."""

import math


def radius_at(shape: str, x: float, length: float, radius: float) -> float:
    if length <= 0 or radius <= 0 or not 0 <= x <= length:
        raise ValueError('Invalid nose dimensions or station')
    if shape == 'conical':
        return radius*x/length
    if shape == 'ellipsoid':
        return radius*math.sqrt(max(0, 1-(1-x/length)**2))
    if shape == 'ogive':
        if length < radius:
            raise ValueError('Tangent ogive requires length >= radius')
        rho = (length*length+radius*radius)/(2*radius)
        return math.sqrt(max(0, rho*rho-(length-x)**2)) + radius-rho
    raise ValueError(f'Unsupported nose shape: {shape}')


def solid(shape, length, radius):
    """Smooth revolved CAD with cosine-spaced interpolation stations."""
    import cadquery as cq
    stations = [length*(1-math.cos(math.pi*i/200))/2 for i in range(201)]
    points = [(radius_at(shape, x, length, radius), x) for x in stations]
    return (cq.Workplane('XZ').moveTo(*points[0]).spline(points[1:], includeCurrent=True)
            .lineTo(0, length).close().revolve(360, (0, 0), (0, 1)))


def rounded_cone(length: float, radius: float, tip_radius: float):
    """Cone with a tangent spherical tip, retaining its length and base radius."""
    import cadquery as cq

    if not 0 < tip_radius < length / 10 or radius <= 0:
        raise ValueError('Invalid rounded cone dimensions')
    # Tangent from the base point (length, radius) to the circle centered
    # tip_radius behind the axial tip. The upper-left tangent is the nose.
    vx, vy = length - tip_radius, radius
    distance_sq = vx * vx + vy * vy
    if distance_sq <= tip_radius * tip_radius:
        raise ValueError('Nose base must lie outside the tip sphere')
    tangent_scale = tip_radius * math.sqrt(distance_sq - tip_radius * tip_radius) / distance_sq
    tangent_z = tip_radius + tip_radius**2 * vx / distance_sq - tangent_scale * vy
    tangent_r = tip_radius**2 * vy / distance_sq + tangent_scale * vx
    tangent_angle = math.atan2(tangent_z - tip_radius, tangent_r)
    mid_angle = (-math.pi / 2 + tangent_angle) / 2
    arc_mid = (tip_radius * math.cos(mid_angle), tip_radius * (1 + math.sin(mid_angle)))
    return (cq.Workplane('XZ').moveTo(0, 0)
            .threePointArc(arc_mid, (tangent_r, tangent_z))
            .lineTo(radius, length).lineTo(0, length).close()
            .revolve(360, (0, 0), (0, 1)))
