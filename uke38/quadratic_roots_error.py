#!/usr/bin/env python3

import sys
from quadratic_roots_input import quadratic


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
