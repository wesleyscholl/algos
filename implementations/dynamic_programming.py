"""
Dynamic Programming Pattern Implementations

Pattern: Break problems into overlapping subproblems
Time: Typically O(n) to O(n²)
Space: O(n) (can often be optimized to O(1))
"""

from typing import List


def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> fibonacci(6)
        8  # 0,1,1,2,3,5,8
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def climbing_stairs(n: int) -> int:
    """
    Count ways to climb n stairs (1 or 2 steps at a time).
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> climbing_stairs(3)
        3  # 1+1+1, 1+2, 2+1
    """
    if n <= 2:
        return n
    
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def coin_change(coins: List[int], amount: int) -> int:
    """
    Find minimum coins needed to make amount.
    
    Time: O(amount * n), Space: O(amount)
    
    Example:
        >>> coin_change([1, 2, 5], 11)
        3  # 5+5+1
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Find length of longest increasing subsequence.
    
    Time: O(n²), Space: O(n)
    
    Example:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4  # [2, 3, 7, 101]
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def house_robber(nums: List[int]) -> int:
    """
    Rob houses (can't rob adjacent ones) for maximum money.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> house_robber([2, 7, 9, 3, 1])
        12  # rob houses 0,2,4
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev, curr = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, prev + nums[i])
    
    return curr


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack: maximize value within weight capacity.
    
    Time: O(n * capacity), Space: O(capacity)
    
    Example:
        >>> knapsack_01([1, 2, 3], [10, 15, 40], 6)
        65  # items 1 and 2
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse backwards to avoid using same item multiple times
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find length of longest common subsequence.
    
    Time: O(m * n), Space: O(min(m, n))
    
    Example:
        >>> longest_common_subsequence("abcde", "ace")
        3  # "ace"
    """
    m, n = len(text1), len(text2)
    
    # Use space-optimized version
    prev = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr
    
    return prev[n]


def edit_distance(word1: str, word2: str) -> int:
    """
    Minimum edit distance (insert, delete, replace).
    
    Time: O(m * n), Space: O(n)
    
    Example:
        >>> edit_distance("horse", "ros")
        3  # horse -> rorse -> rose -> ros
    """
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
        prev = curr
    
    return prev[n]


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Check if string can be segmented into dictionary words.
    
    Time: O(n² * m), Space: O(n)
    where n = len(s), m = max word length
    
    Example:
        >>> word_break("leetcode", ["leet", "code"])
        True
    """
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]


def unique_paths(m: int, n: int) -> int:
    """
    Count unique paths in m x n grid from top-left to bottom-right.
    
    Time: O(m * n), Space: O(n)
    
    Example:
        >>> unique_paths(3, 7)
        28
    """
    dp = [1] * n
    
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[n-1]


def max_product_subarray(nums: List[int]) -> int:
    """
    Find maximum product of contiguous subarray.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> max_product_subarray([2, 3, -2, 4])
        6  # [2, 3]
    """
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for num in nums[1:]:
        # When multiplied by negative, max becomes min and vice versa
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)
    
    return result
