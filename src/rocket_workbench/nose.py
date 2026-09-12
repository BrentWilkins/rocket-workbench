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
