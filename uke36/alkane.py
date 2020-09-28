#!/usr/bin/env python3

Mc: float = 12.011    # [g/mol]
Mh: float = 1.0079    # [g/mol]

for i in range(2, 10):
    n: float = i
    m: float = 2 * i + 2
    print(f"M(C{n}H{m}) = {n*Mc + m*Mh:.3f}")
