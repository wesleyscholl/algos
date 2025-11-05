"""Comprehensive tests for two pointer implementations"""
import pytest
from implementations.two_pointers import (
    two_sum_sorted, is_palindrome, three_sum, container_with_most_water,
    remove_duplicates, move_zeroes, reverse_string, partition
)


class TestTwoSumSorted:
    """Test two sum on sorted array"""
    
    def test_basic_two_sum(self):
        """Test basic two sum"""
        result = two_sum_sorted([2, 7, 11, 15], 9)
        assert result == [1, 2]  # 1-indexed
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = two_sum_sorted([-1, 0, 1, 2], 1)
        assert result == [1, 4]  # 1-indexed (-1 + 2 = 1)
    
    def test_no_solution(self):
        """Test when no solution exists"""
        result = two_sum_sorted([1, 2, 3], 10)
        assert result == []


class TestIsPalindrome:
    """Test palindrome check"""
    
    def test_valid_palindrome(self):
        """Test valid palindrome"""
        assert is_palindrome("racecar") == True
    
    def test_invalid_palindrome(self):
        """Test invalid palindrome"""
        assert is_palindrome("hello") == False
    
    def test_empty_string(self):
        """Test empty string"""
        assert is_palindrome("") == True
    
    def test_single_char(self):
        """Test single character"""
        assert is_palindrome("a") == True


class TestThreeSum:
    """Test three sum"""
    
    def test_basic_three_sum(self):
        """Test basic three sum"""
        result = three_sum([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted(result) == sorted(expected)
    
    def test_no_solution(self):
        """Test no solution"""
        result = three_sum([1, 2, 3])
        assert result == []
    
    def test_all_zeros(self):
        """Test all zeros"""
        result = three_sum([0, 0, 0, 0])
        assert result == [[0, 0, 0]]


class TestContainerWithMostWater:
    """Test container with most water"""
    
    def test_basic_container(self):
        """Test basic container"""
        result = container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
        assert result == 49
    
    def test_two_lines(self):
        """Test two lines"""
        result = container_with_most_water([1, 1])
        assert result == 1


class TestRemoveDuplicates:
    """Test remove duplicates"""
    
    def test_with_duplicates(self):
        """Test with duplicates"""
        nums = [1, 1, 2, 2, 3]
        k = remove_duplicates(nums)
        assert k == 3
        assert nums[:k] == [1, 2, 3]
    
    def test_no_duplicates(self):
        """Test no duplicates"""
        nums = [1, 2, 3]
        k = remove_duplicates(nums)
        assert k == 3


class TestMoveZeroes:
    """Test move zeroes"""
    
    def test_with_zeroes(self):
        """Test with zeroes"""
        nums = [0, 1, 0, 3, 12]
        move_zeroes(nums)
        assert nums == [1, 3, 12, 0, 0]
    
    def test_all_zeroes(self):
        """Test all zeroes"""
        nums = [0, 0, 0]
        move_zeroes(nums)
        assert nums == [0, 0, 0]
    
    def test_no_zeroes(self):
        """Test no zeroes"""
        nums = [1, 2, 3]
        move_zeroes(nums)
        assert nums == [1, 2, 3]


class TestReverseString:
    """Test reverse string"""
    
    def test_basic_reverse(self):
        """Test basic reverse"""
        s = ["h", "e", "l", "l", "o"]
        reverse_string(s)
        assert s == ["o", "l", "l", "e", "h"]
    
    def test_single_char(self):
        """Test single character"""
        s = ["a"]
        reverse_string(s)
        assert s == ["a"]


class TestPartition:
    """Test palindrome partitioning"""
    
    def test_basic_partitioning(self):
        """Test basic palindrome partitioning"""
        result = partition("aab")
        expected = [["a", "a", "b"], ["aa", "b"]]
        assert sorted([sorted(p) for p in result]) == sorted([sorted(p) for p in expected])
    
    def test_single_char(self):
        """Test single character"""
        result = partition("a")
        assert result == [["a"]]
