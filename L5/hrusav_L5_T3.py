"""
Напишете рекурсивна функция за двоично търсене в нареден списък.
да получава параметър от командния ред със sys.argv число за търсене
Резултатът е един от следните два:
    not found - ако стойността не се намира в списъка
    found at X - ако първото срещане на търсената стойност в списъка е на позиция X

Списъкът за търсене да е статично описан в кода и да е следният:
    
[30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988]

Примерен изход при подаване на параметър 88999999

    not found

Примерен изход при подаване на параметър 584

    found at 54
"""
import sys


def binary_search_realization(array, exponent, low, high):
    if high > low:
        middle = low + (high - low) // 2

        if array[middle] == exponent:
            return middle

        elif array[middle] > exponent:
            return binary_search_realization(array, exponent, low, middle - 1)

        else:
            return binary_search_realization(array, exponent, middle + 1, high)
    else:
        return -1


if __name__ == "__main__":
    array = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988]

    if len(sys.argv) != 2:
        print("Proper usage is <filename> <number_to_search>")
    else:
        exponent = int(sys.argv[1])
        result = binary_search_realization(array, exponent, 0, len(array) - 1)
        if result != -1:
            print(f"found at {result}")
        else:
            print("not found")
