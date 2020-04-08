"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    len_array = len(input_array)
    low = 0
    high = len_array
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        current = input_array[mid]
        if current == value:
            return mid
        elif value < current:
            '''Toma izquierda'''
            high = mid - 1
        elif value > current:
            '''Toma derecha'''
            low = mid + 1

    '''
    This works with index of
    try:
        res = input_array.index(value)
        return res
    except:
        return -1
    '''
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, 1))
print(binary_search(test_list, 3))
print(binary_search(test_list, 9))
print(binary_search(test_list, 11))
print(binary_search(test_list, 19))
print(binary_search(test_list, 29))
print(binary_search(test_list, 0))
print(binary_search(test_list, -1))
