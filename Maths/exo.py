import math


def Seuil():
    n = 0
    u = 0.1
    while math.log(2) - u > 0.0001:
        n += 1
        u = 2 * u * math.exp(-u)
    return (u, n)


def Valeur(a):
    n = 0
    while n - math.log(n**2 + 1) < a:
        n += 1
    return n


def ExtendedGCD(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = ExtendedGCD(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def Solver(a, b, n):
    g, x0, y0 = ExtendedGCD(a, b)

    if n % g != 0:
        return None  

    x = x0 * (n // g)
    y = y0 * (n // g)

    return x, y
