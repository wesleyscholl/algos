"""
DFS and Backtracking Pattern Implementations

Pattern: Explore all possibilities through recursion
Time: Typically O(2^n) or O(n!)
Space: O(n) for recursion depth
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets (power set).
    
    Time: O(2^n), Space: O(n)
    
    Example:
        >>> subsets([1, 2, 3])
        [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    """
    result = []
    
    def backtrack(start: int, path: List[int]):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations.
    
    Time: O(n!), Space: O(n)
    
    Example:
        >>> permutations([1, 2, 3])
        [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    """
    result = []
    
    def backtrack(path: List[int], remaining: List[int]):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    backtrack([], nums)
    return result


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all combinations that sum to target (numbers can be reused).
    
    Time: O(2^target), Space: O(target)
    
    Example:
        >>> combination_sum([2, 3, 6, 7], 7)
        [[2,2,3], [7]]
    """
    result = []
    
    def backtrack(start: int, path: List[int], remaining: int):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result


def solve_n_queens(n: int) -> List[List[str]]:
    """
    Solve N-Queens problem.
    
    Time: O(n!), Space: O(n²)
    
    Example:
        >>> solve_n_queens(4)
        [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
    """
    def create_board():
        return [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal top-left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check diagonal top-right
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'
    
    result = []
    backtrack(create_board(), 0)
    return result


def word_search(board: List[List[str]], word: str) -> bool:
    """
    Find if word exists in 2D board.
    
    Time: O(m * n * 4^L) where L is word length, Space: O(L)
    
    Example:
        >>> board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
        >>> word_search(board, "ABCCED")
        True
    """
    if not board or not board[0]:
        return False
    
    m, n = len(board), len(board[0])
    
    def backtrack(row, col, index):
        if index == len(word):
            return True
        
        if (row < 0 or row >= m or col < 0 or col >= n or
            board[row][col] != word[index]):
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Explore all 4 directions
        found = (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1))
        
        # Restore
        board[row][col] = temp
        
        return found
    
    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True
    
    return False


def generate_parentheses(n: int) -> List[str]:
    """
    Generate all valid combinations of n pairs of parentheses.
    
    Time: O(4^n / √n), Space: O(n)
    
    Example:
        >>> generate_parentheses(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    """
    result = []
    
    def backtrack(path: str, open_count: int, close_count: int):
        if len(path) == 2 * n:
            result.append(path)
            return
        
        if open_count < n:
            backtrack(path + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(path + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result


def letter_combinations(digits: str) -> List[str]:
    """
    Letter combinations of phone number.
    
    Time: O(4^n), Space: O(n)
    
    Example:
        >>> letter_combinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    """
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            result.append(path)
            return
        
        for letter in phone[digits[index]]:
            backtrack(index + 1, path + letter)
    
    backtrack(0, '')
    return result
