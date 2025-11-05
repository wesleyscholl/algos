"""Comprehensive tests for DFS and backtracking implementations"""
import pytest
from implementations.dfs_backtracking import (
    subsets, permutations, combination_sum, generate_parentheses,
    letter_combinations, word_search, solve_n_queens
)


class TestSubsets:
    """Test subset generation"""
    
    def test_basic_subsets(self):
        """Test basic subset generation"""
        result = subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        assert sorted(result) == sorted(expected)
    
    def test_empty_set(self):
        """Test empty set"""
        result = subsets([])
        assert result == [[]]
    
    def test_single_element(self):
        """Test single element"""
        result = subsets([1])
        assert sorted(result) == sorted([[], [1]])


class TestPermutations:
    """Test permutation generation"""
    
    def test_basic_permutations(self):
        """Test basic permutations"""
        result = permutations([1, 2, 3])
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        assert sorted(result) == sorted(expected)
    
    def test_single_element(self):
        """Test single element"""
        result = permutations([1])
        assert result == [[1]]
    
    def test_two_elements(self):
        """Test two elements"""
        result = permutations([1, 2])
        assert sorted(result) == sorted([[1, 2], [2, 1]])


class TestCombinationSum:
    """Test combination sum"""
    
    def test_basic_combination(self):
        """Test basic combination sum"""
        result = combination_sum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        assert sorted(result) == sorted(expected)
    
    def test_no_solution(self):
        """Test no solution exists"""
        result = combination_sum([2], 1)
        assert result == []


class TestGenerateParentheses:
    """Test parentheses generation"""
    
    def test_three_pairs(self):
        """Test three pairs of parentheses"""
        result = generate_parentheses(3)
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        assert sorted(result) == sorted(expected)
    
    def test_one_pair(self):
        """Test one pair"""
        result = generate_parentheses(1)
        assert result == ["()"]


class TestLetterCombinations:
    """Test letter combinations from phone number"""
    
    def test_two_digits(self):
        """Test two digits"""
        result = letter_combinations("23")
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        assert sorted(result) == sorted(expected)
    
    def test_empty_input(self):
        """Test empty input"""
        result = letter_combinations("")
        assert result == []


class TestWordSearch:
    """Test word search in grid"""
    
    def test_word_exists(self):
        """Test when word exists"""
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        assert word_search(board, "ABCCED") == True
    
    def test_word_not_exists(self):
        """Test when word doesn't exist"""
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        assert word_search(board, "ABCB") == False


class TestNQueens:
    """Test N-Queens problem"""
    
    def test_four_queens(self):
        """Test 4 queens"""
        result = solve_n_queens(4)
        assert len(result) == 2  # 2 solutions for n=4
    
    def test_one_queen(self):
        """Test single queen"""
        result = solve_n_queens(1)
        assert result == [["Q"]]
