def bisection(f, a, b, n):
    for _ in range(n):
        m = 0.5*(a + b)
        
        if f(m) == 0.:
            a = m
            b = m

        elif f(a)*f(m) < 0.:
            b = m

        else:
            a = m
    
    return 0.5*(a + b)

if __name__ == "__main__":
    print(bisection(lambda x : (x*x) - 2, 1, 2, 33))
