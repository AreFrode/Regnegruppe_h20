#!/usr/bin/env python3

s: float = 0
M: int = 3

for i in range(1, M + 1):
    s += 1 / ((2 * i)**2)

print(s)
