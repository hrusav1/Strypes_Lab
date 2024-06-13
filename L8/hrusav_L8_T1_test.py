import math

class BisectionError(Exception):
    pass

def f1(x):
    return x**3 + 3*x - 5

def f2(x):
    return math.exp(x) - 2*x - 2

def bisection(a, b, func, tol=0.001, max_iter=100):
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

    print(f"{'i':<3} {'a':<10} {'x':<10} {'b':<10} {'f(a)':<12} {'f(x)':<12} {'f(b)':<12}")
    iteration = 0
    while iteration < max_iter:
        midpoint = (a + b) / 2
        fa = func(a)
        fx = func(midpoint)
        fb = func(b)
        print(f"{iteration + 1:<3} {a:<10.6f} {midpoint:<10.6f} {b:<10.6f} {fa:<12.6f} {fx:<12.6f} {fb:<12.6f}")
        if abs(fx) < tol:
            return midpoint
        if fa * fx < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1

    raise BisectionError("Достигнат е максималният брой итерации. Възможно е решението да не е намерено с желаната точност.")

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Невалиден вход. Моля, въведете числова стойност.")

def main():
    print("Въведете граничните стойности за метода на дихотомията:")
    a = get_input("a: ")
    b = get_input("b: ")

    print("Изберете функцията, която искате да използвате:")
    print("1: f1(x) = x^3 + 3x - 5")
    print("2: f2(x) = exp(x) - 2x - 2")
    
    func_choice = input("Въведете номера на функцията, която искате да използвате: ")

    if func_choice == '1':
        func = f1
    elif func_choice == '2':
        func = f2
    else:
        print("Невалиден избор. Изход.")
        return

    try:
        root = bisection(a, b, func)
        print(f"Коренът на функцията в интервала [{a}, {b}] е приблизително {root}")
    except BisectionError as e:
        print(e)

if __name__ == "__main__":
    main()

