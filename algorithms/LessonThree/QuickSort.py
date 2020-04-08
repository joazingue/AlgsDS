"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array, start, pivot_index):
    next = start
    while next < pivot_index:
        # print("%s vs %s" % (array[pivot_index], array[next]))
        if array[next] > array[pivot_index]:
            array[next], array[pivot_index - 1], array[pivot_index] = array[pivot_index - 1], array[pivot_index], array[next]
            pivot_index -= 1
        else:
            next += 1
    return pivot_index

def recursionQS(array, start, end):
    new_pivot = partition(array, start, end)
    if start < new_pivot:
        new_pivot = recursionQS(array, start, new_pivot - 1)
        new_pivot = recursionQS(array, new_pivot + 1, end)

    return new_pivot


def recursionQuickSort(array):
    start = 0
    end = len(array) - 1
    recursionQS(array, start, end)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
#      [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
print(recursionQuickSort(test))