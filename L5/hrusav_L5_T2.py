"""
Създайте рекурсивна функция, 
която при зададено число и степен, 
връща числото, повдигнато на степента
да получава параметри от командния ред със sys.argv
исло и степен и да изпечатва резултатът от повдигането на числото на съответната степен.

Примерен изход при извикване с параметри 2 10:

1024
"""
import sys


def pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / pow(base, -exponent)
    else:
        return base * pow(base, exponent - 1)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError("Proper usage is <filename> <base> <exponent>")

        base = int(sys.argv[1])
        exponent = int(sys.argv[2])

        print(pow(base, exponent))
    
    except ValueError as ve:
        print(ve)
