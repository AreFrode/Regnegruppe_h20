#!/usr/bin/env python3

from typing import List
import numpy as np


def pop(t: int) -> float:
    return (50000) / (1 + 9 * np.exp(-0.2 * t))


n: int = 12
t: List[int] = np.linspace(0, 48, n + 1, dtype=np.int16)
N: List[float] = np.zeros(n + 1)

for i in range(len(t)):
    N[i] = pop(t[i])

for i, j in zip(t, N):
    print(f"time: {i:2.0f} hours, population size: {j} bacteria")
