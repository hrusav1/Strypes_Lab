"""
Създайте рекурсивна функция за изчисляване на първите n числа на Фибоначи
, и тяхното съхранение в списък. 
Реализацията трябва да съхранява вече изчислените стойности, 
така че когато рекурсивно извикване е с аргумент, който вече е изчислен
, стойността да се взима директно, а да не се изчислява.
 да получава параметри от командния ред със sys.argv
 начално и крайно число
 позиция в редицата
 и да разпечатва списък с числата от редицата на Фибоначи,
 от началният до крайният индекс включително.

 Примерен изход при параметри 4 20:

 [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
"""
import sys


def fibonacci_calsulator(n, memory={}):
    if n in memory:
        return memory[n]
    if n <= 2:
        return 1
    memory[n] = fibonacci_calsulator(n-1, memory) + fibonacci_calsulator(n-2, memory)

    return memory[n]


def fibonacci_sequence_calculation(start, end):
    fib_seq = []

    for i in range(start - 1, end + 1):
        fib_seq.append(fibonacci_calsulator(i))

    return fib_seq


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fibonacci.py <start> <end>")
    else:
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        if start < 1 or end < start:
            print("given range is invalid")
        else:
            print(fibonacci_sequence_calculation(start, end))
