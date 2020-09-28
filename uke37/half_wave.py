#!/usr/bin/env python3

from math import sin


def f(x: float) -> float:
    """
    implementation of half wave function

    Args:
        x: value of the signal

    Returns:
        sin of the signal if positive else 0
    """

    return sin(x) if x > 0 else 0.


def test_f():
    x1 = 1
    x2 = -3
    computed1 = f(x1)
    computed2 = f(x2)
    success = computed1 > 0 and computed2 == 0
    assert success, f"Should be: {computed1} > 0 and {computed2} == 0"


test_f()
