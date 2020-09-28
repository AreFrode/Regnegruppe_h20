#!/usr/bin/env python3
from typing import List


def triangle_area(vertices: List[List[float]]) -> float:
    """
    computes the area of a triangle

    Args:
        vertices: nested list on form ((xi,yi),(xi+1,yi+1)) containing the vertices

    Returns:
        The computed area
    """

    return 0.5 * abs(vertices[1][0] * vertices[2][1]
                     - vertices[2][0] * vertices[1][1]
                     - vertices[0][0] * vertices[2][1]
                     + vertices[2][0] * vertices[0][1]
                     + vertices[0][0] * vertices[1][1]
                     - vertices[1][0] * vertices[0][1])


def test_triangle_area():
    """
    Verify the area of a triangle with vertices(0,0), (1,0), and (0,2).
    """
    v1 = [0, 0]
    v2 = [1, 0]
    v3 = [0, 2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg


test_triangle_area()
