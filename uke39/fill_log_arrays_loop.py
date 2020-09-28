#!/usr/bin/env python3

import numpy as np


def f(x: float) -> float:
    return np.log(x)


if __name__ == "__main__":
    n = 101
    start = 1
    stop = 10
    h = (stop - start) / (n - 1)
    x = np.zeros(101)
    y = np.zeros(101)
    for i in range(n):
        x[i] = start + h * i
        y[i] = f(x[i])

    print(y[-1])
