#!/usr/bin/env python3

import sys


def quadratic(a: float, b: float, c: float) -> float:
    try:
        sqrt_term: float = (b * b) - 4 * a * c
        if sqrt_term < 0:
            raise ValueError
        sqrt_term = sqrt_term**(0.5)
        return (-b + sqrt_term) / (2 * a), (-b - sqrt_term) / (2 * a)
    except ValueError as e:
        sys.exit("IKKE LOV MED KOMPLEKSE TALL >:(")


def main(a: float, b: float, c: float) -> None:
    quad = quadratic(a, b, c)
    print(f"{quad[0]}, {quad[1]}")


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 4
        main(float(sys.argv[1]), float(
            sys.argv[2]), float(sys.argv[3]))
    except IndexError as e:
        main(float(input("a: ")), float(input("b: ")), float(input("c: ")))
    except AssertionError as e:
        main(float(input("a: ")), float(input("b: ")), float(input("c: ")))
