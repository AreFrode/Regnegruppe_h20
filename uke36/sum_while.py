#!/usr/bin/env python3

s: float = 0
M: int = 3

counter: int = 1
while counter < M + 1:
    s += 1 / ((2 * counter)**2)
    counter += 1

print(s)
