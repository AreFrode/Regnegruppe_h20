from bisection import bisection
from secant import secant
from newton import newton
from math import sin, cos, pi


f = lambda x : sin(x)
g = lambda x : cos(x)

bisection_approx = bisection(f, 3, 4, 10)
print(f"Approximation of pi = {pi} using the bisection method with ten steps: {bisection_approx}")

secant_approx = secant(f, 4, 3, 4)
print(f"Approximation of pi = {pi} using the secant method with four steps: {secant_approx}")

newton_approx = newton(f, g, 3, 4)
print(f"Approximation of pi = {pi} using newtons method with four steps: {newton_approx}")
