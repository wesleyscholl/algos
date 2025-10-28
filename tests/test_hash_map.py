"""Tests for hash map pattern implementations."""

import pytest
from implementations.hash_map import (
    two_sum, valid_anagram, subarray_sum_equals_k,
    group_anagrams, first_unique_char, contains_duplicate,
    intersection, longest_consecutive
)


class TestHashMap:
    def test_two_sum(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]
        assert two_sum([3, 2, 4], 6) == [1, 2]
        assert two_sum([3, 3], 6) == [0, 1]
    
    def test_valid_anagram(self):
        assert valid_anagram("anagram", "nagaram") == True
        assert valid_anagram("rat", "car") == False
        assert valid_anagram("a", "a") == True
    
    def test_subarray_sum_equals_k(self):
        assert subarray_sum_equals_k([1, 1, 1], 2) == 2
        assert subarray_sum_equals_k([1, 2, 3], 3) == 2
        assert subarray_sum_equals_k([1], 0) == 0
    
    def test_group_anagrams(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert len(result) == 3
        assert sorted(["eat", "tea", "ate"]) in [sorted(group) for group in result]
    
    def test_first_unique_char(self):
        assert first_unique_char("leetcode") == 0
        assert first_unique_char("loveleetcode") == 2
        assert first_unique_char("aabb") == -1
    
    def test_contains_duplicate(self):
        assert contains_duplicate([1, 2, 3, 1]) == True
        assert contains_duplicate([1, 2, 3, 4]) == False
    
    def test_intersection(self):
        result = sorted(intersection([1, 2, 2, 1], [2, 2]))
        assert result == [2]
    
    def test_longest_consecutive(self):
        assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
        assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
