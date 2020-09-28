#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def f2c_shortcut(f: float) -> float:
    return 0.5 * (f - 30)


def f2c(f: float) -> float:
    return (5 * (f - 32)) / 9


if __name__ == "__main__":
    f = np.arange(-20, 130, 10)
    plt.plot(f, f2c_shortcut(f), label="Shortcut plot")
    plt.plot(f, f2c(f), label="Exact curve")
    plt.xlabel("Fahrenheit")
    plt.ylabel("Celsius")
    plt.legend()
    plt.show()
