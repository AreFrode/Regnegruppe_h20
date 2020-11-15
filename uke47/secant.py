def secant(f, xp, xpp, n):
    for _ in range(n):
        z = xp - ((xp-xpp)/(f(xp)-f(xpp)))*f(xp)
        xpp = xp
        xp = z

    return z
