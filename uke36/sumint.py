#!/usr/bin/env python3


def sumint(n: int) -> int:
    """
    Summing all positive integers up to n

    Args:
        n: highest int for sum

    Returns:
        the sum of ints up to n
    """

    sum_: int = 0
    for i in range(n + 1):
        sum_ += i

    return sum_


def sumint_analytical(n: int) -> int:
    """
    Analytical expression for sum of natural numbers

    Args:
        n: highest number to be included

    Returns:
        the sum up to and including n
    """

    return int(0.5 * (n * (n + 1)))
