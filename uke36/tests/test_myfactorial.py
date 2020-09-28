#!/usr/bin/env python3

from math import factorial
from factorial import myfactorial


def test_myfactorial() -> None:
    expected = factorial(5)
    computed = myfactorial(5)
    assert computed == expected, f"computed {computed} != expected {expected}"


test_myfactorial()
