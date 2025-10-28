"""Tests for dynamic programming implementations."""

import pytest
from implementations.dynamic_programming import (
    fibonacci, climbing_stairs, coin_change, longest_increasing_subsequence,
    house_robber, knapsack_01, longest_common_subsequence, edit_distance,
    word_break, unique_paths, max_product_subarray
)


class TestDynamicProgramming:
    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(6) == 8
        assert fibonacci(10) == 55
    
    def test_climbing_stairs(self):
        assert climbing_stairs(2) == 2
        assert climbing_stairs(3) == 3
        assert climbing_stairs(5) == 8
    
    def test_coin_change(self):
        assert coin_change([1, 2, 5], 11) == 3
        assert coin_change([2], 3) == -1
        assert coin_change([1], 0) == 0
    
    def test_longest_increasing_subsequence(self):
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
        assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1
    
    def test_house_robber(self):
        assert house_robber([1, 2, 3, 1]) == 4
        assert house_robber([2, 7, 9, 3, 1]) == 12
    
    def test_knapsack_01(self):
        assert knapsack_01([1, 2, 3], [10, 15, 40], 6) == 65
        assert knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
    
    def test_longest_common_subsequence(self):
        assert longest_common_subsequence("abcde", "ace") == 3
        assert longest_common_subsequence("abc", "abc") == 3
        assert longest_common_subsequence("abc", "def") == 0
    
    def test_edit_distance(self):
        assert edit_distance("horse", "ros") == 3
        assert edit_distance("intention", "execution") == 5
    
    def test_word_break(self):
        assert word_break("leetcode", ["leet", "code"]) == True
        assert word_break("applepenapple", ["apple", "pen"]) == True
        assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    
    def test_unique_paths(self):
        assert unique_paths(3, 7) == 28
        assert unique_paths(3, 2) == 3
    
    def test_max_product_subarray(self):
        assert max_product_subarray([2, 3, -2, 4]) == 6
        assert max_product_subarray([-2, 0, -1]) == 0
