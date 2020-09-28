#!/usr/bin/env python3

from typing import List


def quadratic(a: float, b: float, c: float) -> List[float]:
    try:
        sqrt_term: float = (b * b - 4 * a * c)**(0.5)
        if (sqrt_term )
    return (-b + sqrt_term) / (2 * a), (-b - sqrt_term) / (2 * a)


if __name__ == "__main__":
    a: float = float(input("a: "))
    b: float = float(input("b: "))
    c: float = float(input("c: "))

    quad = quadratic(a, b, c)
    print(f"{quad[0]}, {quad[1]}")
