# task 5

# in this case we will need some imports
import sys
import math


def quadratic_eqution_solver(a, b, c):
    # Discriminant / Solve for D
    D = b**2 - 4*a*c

    # in case there are two real roots so there is an x1 and x2
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"{x1:.2f}|{x2:.2f}"

    # in case there is only one real root so only x1 is real
    elif D == 0:
        x = -b / (2*a)
        return f"{x:.2f}"

    # in case there are no real roots
    else:
        return "special case"


# here we will have to interract with humans, so command line explanations
if len(sys.argv) != 4:
    print("Write aguments for a, b and c, please")
    print("The way to do it is python3 hrusav_L1_T5.py <a> <b> <c>")
    print("a b and c are the exponents and are to be written without the <>")
    sys.exit(1)

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except ValueError:
    print("Coefficients must be numbers and may be floats.")
    sys.exit(1)

# test the function
result = quadratic_eqution_solver(a, b, c)
print(result)
