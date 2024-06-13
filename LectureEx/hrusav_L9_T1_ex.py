import math

class BisectionError(Exception):
    pass

def f1(x):
    return x**3 + 3*x - 5

def f2(x):
    return math.exp(x) - 2*x - 2

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Моля, въведете числова стойност.")

def print_function_table():
    print("\nФункции, които могат да бъдат използвани:")
    print("╔════════════════════════════╗")
    print("║ Функция      ║ Описание    ║")
    print("╠══════════════╬═════════════╣")
    print("║ f1           ║ x^3 + 3x - 5║")
    print("║ f2           ║ e^x - 2x - 2║")
    print("╚══════════════╩═════════════╝")

def bisection(a, b, func, tol=1e-6, max_iter=100):
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

if __name__ == "__main__":
    print("Контроли:")
    print("- За изход от програмата въведете 'q'.")
    print_function_table()
    print("\nМоля, въведете граници на интервала (a и b).")
    while True:
        try:
            a = get_numeric_input("Въведете стойност за a: ")
            b = get_numeric_input("Въведете стойност за b: ")
            root = bisection(a, b, f1)  # You can replace f1 with f2 if needed
            print("Коренът на уравнението е: ", root)
        except BisectionError as e:
            print("Грешка:", e)
        except KeyboardInterrupt:
            print("\nПрограмата беше прекратена.")
            exit()
        except EOFError:
            print("\nПрограмата беше прекратена.")
            exit()
        except ValueError:
            print("\nМоля, въведете валидна числова стойност.")
        except Exception as e:
            print("\nНеочаквана грешка:", e)
        choice = input("Желаете ли да продължите? (Натиснете 'q' за изход): ")
        if choice.lower() == 'q':
            break

