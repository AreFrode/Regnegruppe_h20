#!/usr/bin/env python3

import numpy as np

class NewtonsMethod:
    def __init__(self, x, f, g):
        self.x = x
        self.f = f
        self.g = g

    def step(self):
        self.x -= self.f(self.x) / self.g(self.x)

if __name__ == "__main__":
    my_solver = NewtonsMethod(3.14, np.sin, np.cos)
    for i in range(3):
        print(f"Pi approx: {my_solver.x}, Pi numpy: {np.pi}")
        my_solver.step()
