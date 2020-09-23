from math import pi

from helpers import compute_volume

import pygmsh


def test():
    geom = pygmsh.opencascade.Geometry()

    geom.add_ellipsoid([1.0, 1.0, 1.0], [1.0, 2.0, 3.0], mesh_size=0.1)

    ref = 8.0 * pi
    mesh = pygmsh.generate_mesh(geom)
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("opencascade_ellipsoid.vtu")
