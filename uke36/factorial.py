#!/usr/bin/env python3

def myfactorial(n: int) -> int:
    if n > 1:
        return n * myfactorial(n - 1)
    else:
        return n
