# this is the first programm
example_list_1 = [1, 2, 2]
example_list_2 = ['b', 'a']


# this is a function to check if a list is ordered or not
def is_list_ordered(unknown_list):

    for i in range(len(unknown_list) - 1):

        if str(unknown_list[i]) > str(unknown_list[i + 1]):
            return False

    return True


print(is_list_ordered(example_list_1))
print(is_list_ordered(example_list_2))
