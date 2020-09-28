#!/usr/bin/env python3

from sumint import sumint, sumint_analytical


def test_sumint() -> None:
    val: int = 10
    expected: int = 55
    computed: int = sumint(10)
    success: bool = computed == expected
    assert success, f"computed {computed} != expected {expected}"


def test_sumint_analytical() -> None:
    val: int = 10
    expected: int = 55
    computed: int = sumint_analytical(val)
    success: bool = computed == expected
    assert success, f"computed {computed} != expected {expected}"


test_sumint()
test_sumint_analytical()
