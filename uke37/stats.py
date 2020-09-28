#!/usr/bin/env python3

import numpy as np
from typing import List


def mean(x_list: List[float]) -> float:
    """
    Function to compute mean value

    Args:
        x_list: list containing all x values

    Returns:
        mean value of elements in x_list
    """

    mean: float = 0.
    for i in x_list:
        mean += i

    return mean / len(x_list)


def standard_deviation(x_list: List[float]) -> float:
    std: float = 0.
    mean_: float = mean(x_list)
    for i in x_list:
        std += (i - mean_)**2

    return np.sqrt((1 / len(x_list)) * std)


def test_mean():
    x_list = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.mean(x_list)
    computed = mean(x_list)
    tol = 1e-14
    success = abs(expected - computed) < tol
    assert success, f"Expected {expected} != {computed} Computed"


def test_standard_deviation():
    x_list = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(x_list)
    computed = standard_deviation(x_list)
    tol = 1e-14
    success = abs(expected - computed) < tol
    assert success, f"Expected {expected} != {computed} Computed"


test_mean()
test_standard_deviation()
