def newton(f, g, xp, n):
    for _ in range(n):
        z = xp - f(xp)/g(xp)
        xp = z

    return z
