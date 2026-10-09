def sum_array(arr):
    return sum(arr)


def max_element(arr):
    if len(arr) != 0:
        return max(arr)
    return None


def min_element(arr):
    if len(arr) != 0:
        return min(arr)
    return None


def average(arr):
    if len(arr) != 0:
        return sum_array(arr) // len(arr)
    return None


def reverse_array(arr):
    return arr[::-1]


def find_index(arr, value):
    for i, x in enumerate(arr):
        if x == value:
            return i
    return -1


def count_positive(arr):
    return sum(1 for x in arr if x > 0)


def count_negative(arr):
    return sum(1 for x in arr if x < 0)


def remove_duplicates(arr):
    return list(arr)


def sort_array(arr):
    return sorted(arr)
