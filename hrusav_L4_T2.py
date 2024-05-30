"""
Да се реализира на python програма

за създаване на хистограма на честотата на срещане насимволите в даден текст.

Програмата да приема като входен параметър текст
и да извежда в конзолата съдържанието на речник,
съдържащ ключове - символите от текста,
а стойностите  - броя срещания на съответния символ.

Примерен изход:
[('a', 5), ('b', 1), ('c', 1), ('i', 1), ('l', 2), ('n', 1)]
"""
import sys


def histogram_creator(text_string):

    frequency_of_occurance = {}
    for char in text_string:
        if char in frequency_of_occurance:
            frequency_of_occurance[char] += 1
        else:
            frequency_of_occurance[char] = 1

    return frequency_of_occurance


if __name__ == "__main__":

    input_text = " ".join(sys.argv[1:])

    histogram = sorted(histogram_creator(input_text).items())

    print(histogram)
