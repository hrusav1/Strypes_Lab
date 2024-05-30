# second task
# need to import sys module again
import sys


# first create a function to take in the strings
def is_anagram(first_string, second_string):

    first_string = first_string.replace(" ", "").lower()
    second_string = second_string.replace(" ", "").lower()

    if len(first_string) != len(second_string):
        return "False"

    # using a list here makes for a linear complexity
    # I do not forsee any need for large string support, so no O log(n)
    # that would meen using a dictionary instead

    # here we create a limited list to hold the ASKII chars
    count_characters = [0] * 128

    for char in first_string:
        # ord() returns ASKII value of char
        count_characters[ord(char)] += 1
    for char in second_string:
        count_characters[ord(char)] -= 1

    for count in count_characters:
        if count != 0:
            return "False"

    return "True"


if __name__ == "__main__":
    # make sure programm is being called properly

    string1 = sys.argv[1]
    string2 = sys.argv[2]

    print(is_anagram(string1, string2))
