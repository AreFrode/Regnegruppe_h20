#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def wavepacket(x: float, t: int = 0) -> float:
    return np.exp(-(x - 3 * t)**2) * np.sin(3 * np.pi * (x - t))


if __name__ == "__main__":
    x = np.arange(-4, 5, 1e-4)
    plt.plot(x, wavepacket(x))
    plt.xlabel("x")
    plt.ylabel(f"f(x, t=0)")
    plt.show()
