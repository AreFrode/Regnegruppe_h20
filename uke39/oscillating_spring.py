#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def y(t: float, k: float = 4., gamma: float = 0.15, m: float = 9., A: float = 0.3) -> float:
    return A * np.exp(-gamma * t) * np.cos(t * np.sqrt(k / m))


if __name__ == "__main__":
    n = 101
    start = 0
    stop = 25
    t = (stop - start) / (n - 1)
    t_array = np.zeros(n)
    y_array = np.zeros(n)
    for i in range(n):
        t_array[i] = start + i * t
        y_array[i] = y(t_array[i])

    plt.plot(t_array, y_array, label="a)")

    t_array = np.linspace(0, 25, 101, endpoint=True)
    y_array = y(t_array)

    plt.plot(t_array, y_array, "--", label="b)")
    plt.xlabel("time [t]")
    plt.ylabel("y(t)")
    plt.legend()
    plt.show()
