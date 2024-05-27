# task four

def exclude_repetition(input_list) -> list:
    
    encountered_element = set()
    exclusive_list = []

    for item in input_list:

        if item not in encountered_element:
            exclusive_list.append(item)
            encountered_element.add(item)

        elif item in exclusive_list:
            exclusive_list.remove(item)

    return exclusive_list


# Test
example_list_one = [1, 2, 3, 1, 4, 5, 2, 6]
example_list_two = ['a', '1', 'b', '2', 'c', '3']
example_list_three = ['a', '1', 'b', '2', 'a', '1', 'c', '3', 'b', '2']
example_list_four = ['a', 'b', 'c', 'd', 'e']

result_one = exclude_repetition(example_list_one)
result_two = exclude_repetition(example_list_two)
result_three = exclude_repetition(example_list_three)
result_four = exclude_repetition(example_list_four)

print("Non-repeating elements:", result_one)
print("Non-repeating elements:", result_two)
print("Non-repeating elements:", result_three)
print("Non-repeating elements:", result_four)
