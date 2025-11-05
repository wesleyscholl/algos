"""Comprehensive tests for sliding window implementations"""
import pytest
from implementations.sliding_window import (
    max_sum_subarray, length_of_longest_substring, min_window_substring,
    find_anagrams, longest_repeating_character_replacement,
    max_consecutive_ones_iii, length_of_longest_substring_k_distinct
)


class TestMaxSumSubarray:
    """Test maximum sum subarray"""
    
    def test_basic_max_sum(self):
        """Test basic max sum"""
        result = max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
        assert result == 39
    
    def test_all_negative(self):
        """Test all negative numbers"""
        result = max_sum_subarray([-1, -2, -3, -4], 2)
        assert result == -3
    
    def test_window_larger_than_array(self):
        """Test window larger than array"""
        result = max_sum_subarray([1, 2], 5)
        assert result == 0


class TestLengthOfLongestSubstring:
    """Test longest substring without repeating characters"""
    
    def test_basic_string(self):
        """Test basic string"""
        assert length_of_longest_substring("abcabcbb") == 3
    
    def test_all_same(self):
        """Test all same characters"""
        assert length_of_longest_substring("bbbbb") == 1
    
    def test_mixed_string(self):
        """Test mixed string"""
        assert length_of_longest_substring("pwwkew") == 3
    
    def test_empty_string(self):
        """Test empty string"""
        assert length_of_longest_substring("") == 0


class TestMinWindowSubstring:
    """Test minimum window substring"""
    
    def test_basic_window(self):
        """Test basic window"""
        result = min_window_substring("ADOBECODEBANC", "ABC")
        assert result == "BANC"
    
    def test_single_char(self):
        """Test single character"""
        result = min_window_substring("a", "a")
        assert result == "a"
    
    def test_no_window(self):
        """Test no window exists"""
        result = min_window_substring("a", "aa")
        assert result == ""


class TestFindAnagrams:
    """Test find anagrams"""
    
    def test_basic_anagrams(self):
        """Test basic anagrams"""
        result = find_anagrams("cbaebabacd", "abc")
        assert result == [0, 6]
    
    def test_overlapping_anagrams(self):
        """Test overlapping anagrams"""
        result = find_anagrams("abab", "ab")
        assert result == [0, 1, 2]


class TestLongestRepeatingCharacterReplacement:
    """Test longest repeating character replacement"""
    
    def test_basic_replacement(self):
        """Test basic replacement"""
        result = longest_repeating_character_replacement("ABAB", 2)
        assert result == 4
    
    def test_all_same(self):
        """Test all same characters"""
        result = longest_repeating_character_replacement("AAAA", 0)
        assert result == 4


class TestMaxConsecutiveOnesIII:
    """Test max consecutive ones III"""
    
    def test_basic_consecutive(self):
        """Test basic consecutive ones"""
        result = max_consecutive_ones_iii([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
        assert result == 6
    
    def test_all_zeros(self):
        """Test all zeros"""
        result = max_consecutive_ones_iii([0, 0, 0], 2)
        assert result == 2


class TestLongestSubstringKDistinct:
    """Test longest substring with k distinct characters"""
    
    def test_basic_k_distinct(self):
        """Test basic k distinct"""
        result = length_of_longest_substring_k_distinct("eceba", 2)
        assert result == 3
    
    def test_single_char(self):
        """Test single character"""
        result = length_of_longest_substring_k_distinct("a", 1)
        assert result == 1
