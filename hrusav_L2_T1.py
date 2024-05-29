# here we will have to include the sys module
import sys


# this is a function to check if a list is ordered or not
def is_list_ordered(unknown_list):

    for i in range(len(unknown_list) - 1):

        if str(unknown_list[i]) > str(unknown_list[i + 1]):
            return "unsorted"

    return "sorted"


if __name__ == "__main__":
    input_list = sys.argv[1:]

    print(is_list_ordered(input_list))
