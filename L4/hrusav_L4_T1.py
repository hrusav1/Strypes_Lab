# first task L4

""" Напишете програма, която извежда списък от всички ключове, 
които сочат към дадена стойност, 
а ако няма нито една такава стойност, то да се връща празен списък.
Програмата да приема като входен параметър стойността за търсене. 
Речникът да е статично описан в кода на програмата и да е следния:
d={1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}

Примерен изход:
[1, 4, 7]"""

import sys


def all_keys_pointing_to_value(value):

    staticly_coded_dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}

    keys = []
    for key, val in staticly_coded_dictionary.items():
        if val == value:
            keys.append(key)
    return keys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <value>")
        sys.exit(1)

    sought_value = sys.argv[1]

    print(all_keys_pointing_to_value(sought_value))
