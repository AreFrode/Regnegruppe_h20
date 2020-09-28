#!/usr/bin/env python3
from math import exp


def population(t: float, k: float = 0.2, B: int = 50000, C: int = 9) -> float:
    """
    Computes number of individuals in a population

    Args:
        t: time
        k: growth rate
        B: carrying capacity
        C: initial condition

    Returns:
        Number of individuals after time t
    """

    return B / (1 + C * exp(-k * t))


print(f"Time Population")
for i in range(0, 52, 4):
    print(f"{i:4d} {population(i)}")
