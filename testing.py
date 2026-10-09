import pytest
import work_with_array as ar


def test_sum_array():
    assert ar.sum_array([1, 2, 3]) == 6
    assert ar.sum_array([-1, -2, -3]) == -6
    assert ar.sum_array([]) == 0


def test_max_element():
    assert ar.max_element([1, 2, 3]) == 3
    assert ar.max_element([-1, -2, -3]) == -1
    assert ar.max_element([]) == None


def test_min_element():
    assert ar.min_element([1, 2, 3]) == 1
    assert ar.min_element([-1, -2, -3]) == -3
    assert ar.min_element([]) == None


def test_average():
    assert ar.average([1, 2, 3]) == 2
    assert ar.average([-1, -2, -3]) == -2
    assert ar.average([1.1, 2.1, 3.1]) == 2.1
    assert ar.average([-1.1, -2.1, -3.1]) == -2.1
    assert ar.average([]) == None


def test_reverse_array():
    assert ar.reverse_array([1, 2, 3]) == [3, 2, 1]
    assert ar.reverse_array([-1, -2, -3]) == [-3, -2, -1]
    assert ar.reverse_array([]) == []


def test_find_index():
    assert ar.find_index([1, 2, 3], 2) == 1
    assert ar.find_index([-1, -2, -3], -3) == 2
    assert ar.find_index([1.1, 2.1, 3.1], 3.1) == 2
    assert ar.find_index([], -1) == -1


def test_count_positive():
    assert ar.count_positive([1, 2, 3, 0, -1]) == 3
    assert ar.count_positive([-1, -2, -3]) == 0
    assert ar.count_positive([]) == 0


def test_count_negative():
    assert ar.count_negative([1, 2, 3, 0, -1]) == 1
    assert ar.count_negative([-1, -2, -3]) == 3
    assert ar.count_negative([]) == 0


def test_remove_duplicates():
    assert ar.remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert ar.remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert ar.remove_duplicates([]) == []


def test_sort_array():
    assert ar.sort_array([1, 2, 3]) == [1, 2, 3]
    assert ar.sort_array([-1, -2, -3]) == [-3, -2, -1]
    assert ar.sort_array([]) == []
