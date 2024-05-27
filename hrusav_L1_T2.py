# second task

# first create a function to take in the strings
def is_anagram(first_string, second_string):

    first_string = first_string.replace(" ", "").lower()
    second_string = second_string.replace(" ", "").lower()

    if len(first_string) != len(second_string):
        return False

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
            return False

    return True


# test code to check function

# Test strings
test_string_1 = "Vladimir Nabokov"
test_string_2 = "Vivian Darkbloom"
test_string_3 = "rocket boys"
test_string_4 = "october sky"
test_string_5 = "Pesho e doktor"
test_string_6 = "Gosho e traktorist"

pairs = [
    (test_string_1, test_string_2),
    (test_string_3, test_string_4),
    (test_string_5, test_string_6)
]


for str1, str2 in pairs:
    if is_anagram(str1, str2):
        print(f'"{str1}" and "{str2}" are anagrams.')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams.')
