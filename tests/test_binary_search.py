"""Tests for binary search implementations."""

import pytest
from implementations.binary_search import (
    binary_search, search_rotated_array, find_min_rotated_array,
    search_insert_position, find_first_and_last, sqrt,
    find_peak_element, search_2d_matrix, min_eating_speed
)


class TestBinarySearch:
    def test_binary_search(self):
        assert binary_search([1, 2, 3, 4, 5], 3) == 2
        assert binary_search([1, 2, 3, 4, 5], 6) == -1
        assert binary_search([], 1) == -1
    
    def test_search_rotated_array(self):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
        assert search_rotated_array([1], 0) == -1
    
    def test_find_min_rotated_array(self):
        assert find_min_rotated_array([3, 4, 5, 1, 2]) == 1
        assert find_min_rotated_array([4, 5, 6, 7, 0, 1, 2]) == 0
        assert find_min_rotated_array([11, 13, 15, 17]) == 11
    
    def test_search_insert_position(self):
        assert search_insert_position([1, 3, 5, 6], 5) == 2
        assert search_insert_position([1, 3, 5, 6], 2) == 1
        assert search_insert_position([1, 3, 5, 6], 7) == 4
    
    def test_find_first_and_last(self):
        assert find_first_and_last([5, 7, 7, 8, 8, 10], 8) == [3, 4]
        assert find_first_and_last([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
        assert find_first_and_last([], 0) == [-1, -1]
    
    def test_sqrt(self):
        assert sqrt(4) == 2
        assert sqrt(8) == 2
        assert sqrt(16) == 4
    
    def test_find_peak_element(self):
        result = find_peak_element([1, 2, 3, 1])
        assert result == 2
    
    def test_search_2d_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        assert search_2d_matrix(matrix, 3) == True
        assert search_2d_matrix(matrix, 13) == False
    
    def test_min_eating_speed(self):
        assert min_eating_speed([3, 6, 7, 11], 8) == 4
        assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
