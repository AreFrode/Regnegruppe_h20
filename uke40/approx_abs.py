#!/usr/bin/env python3

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

#matplotlib.use('TkAgg')

def abs_approx(x: float, N: int) -> float:
    sum_ = 0.
    for i in range(1, N+1):
        sum_ += (np.cos((2.*i - 1.)*x))/((2.*i - 1.)**2.)

    sum_ *= (4.)/(np.pi)
    return 0.5*np.pi - sum_

if __name__ == "__main__":
    x = np.linspace(-np.pi, np.pi, 100, endpoint=True)
    for i in range(1, 5):
        plt.plot(x, abs_approx(x,i), label=f"N={i}")
    
    plt.plot(x,np.abs(x),label="Analytical")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
