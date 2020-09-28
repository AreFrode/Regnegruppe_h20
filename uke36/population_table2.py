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

# Section a)
tN1: List[List] = []
tN1.append(t)
tN1.append(N)

# Section b)
tN2: List[List] = []
for i, j in zip(t, N):
    tN2.append([i, j])

print("table tN1")
for i in range(len(tN1[0])):
    print(
        f"time: {tN1[0][i]} hours, population size: {int(tN1[1][i])} bacteria")

print("\n-------\n")

print("table tN2")
for i in range(len(tN2)):
    print(f"time: {tN2[i][0]} hours, population size: {int(tN2[i][1])} bacteria")
