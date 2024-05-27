# third task

# create function to check if there is repetition
def repetition_detected(target_list):
    encountered_element = set()

    for item in target_list:
        if item in encountered_element:
            return True
        encountered_element.add(item)
    return False


# check if function is functioning correctly
first_list = [1, 2, 3, 4, 5]
second_list = [1, 2, 3, 4, 1]
third_list = ['a', 'b', 'c', 'd', 'e']
fourth_list = ['a', 'b', 'a', 'c', 'b', 'd', 'c', 'e', 'e']
fifth_list = ['a', '1', 'b', '2', 'c', '3']
sixth_list = ['a', '1', 'b', '2', 'a', '1', 'c', '3', 'b', '2']


print("List1:", "repeats" if repetition_detected(first_list) else "no repeat")
print("List2:", "repeats" if repetition_detected(second_list) else "no repeat")
print("List3:", "repeats" if repetition_detected(third_list) else "no repeat")
print("List4:", "repeats" if repetition_detected(fourth_list) else "no repeat")
print("List5:", "repeats" if repetition_detected(fifth_list) else "no repeat")
print("List6:", "repeats" if repetition_detected(sixth_list) else "no repeat")
