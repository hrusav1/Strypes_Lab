"""
Напишете рекурсивна функция, която връща дали даден символен низ е палиндром 
(дали низът и обърнатият символен низ са същите).
трябва да извежда True или False в завимиост от това дали входът е палиндром.
"""
import sys


def check_if_word_is_palindrome(s):
   
    s = s.lower()

    if len(s) < 2:
        return "True"

    elif s[0] == s[len(s) - 1]:
        return check_if_word_is_palindrome(s[1: len(s) - 1])

    else:
        return "False"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Proper usage is <filename><palindrome>")

    else:
        string = sys.argv[1]

        print(check_if_word_is_palindrome(string))
