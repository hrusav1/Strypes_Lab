import math


class BisectionError(Exception):
    pass

def f1(x):
    return x**3 + 3*x - 5

def f2(x):
    return math.exp(x) - 2*x - 2

def bisection(a, b, func, tol=1e-6, max_iter=100):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise BisectionError("Граничните стойности на интервала трябва да са числа.")

    if func(a) * func(b) >= 0:
        raise BisectionError("Функцията трябва да сменя знаци на краищата на интервала.")

    if math.isinf(a) or math.isinf(b):
        raise BisectionError("Границите на интервала трябва да са крайни.")

    if func(a) == 0:
        return a

    if func(b) == 0:
        return b

    iteration = 0
    while iteration < max_iter:
        midpoint = (a + b) / 2
        if abs(func(midpoint)) < tol:
            return midpoint
        if func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1

    raise BisectionError("Достигнат максимален брой итерации. Възможно е решението да не е намерено с желаната точност.")
