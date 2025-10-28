"""
Hash Map / Dictionary Pattern Implementations

Pattern: Fast lookups, counting, and complements
Time: O(1) lookup, O(n) overall
Space: O(n)
"""

from typing import List, Dict
from collections import Counter, defaultdict


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target.
    
    Time: O(n), Space: O(n)
    
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def valid_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams.
    
    Time: O(n), Space: O(1) [limited alphabet]
    
    Example:
        >>> valid_anagram("anagram", "nagaram")
        True
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Count subarrays with sum equal to k using prefix sum.
    
    Time: O(n), Space: O(n)
    
    Example:
        >>> subarray_sum_equals_k([1, 1, 1], 2)
        2
    """
    prefix_sum = {0: 1}
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        # If (current_sum - k) exists, we found a subarray
        count += prefix_sum.get(current_sum - k, 0)
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    
    return count


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other.
    
    Time: O(n * k log k), Space: O(n * k)
    where n = number of strings, k = max string length
    
    Example:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def first_unique_char(s: str) -> int:
    """
    Find index of first non-repeating character.
    
    Time: O(n), Space: O(1) [limited alphabet]
    
    Example:
        >>> first_unique_char("leetcode")
        0
        >>> first_unique_char("loveleetcode")
        2
    """
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains any duplicates.
    
    Time: O(n), Space: O(n)
    
    Example:
        >>> contains_duplicate([1, 2, 3, 1])
        True
    """
    return len(nums) != len(set(nums))


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two arrays.
    
    Time: O(n + m), Space: O(min(n, m))
    
    Example:
        >>> sorted(intersection([1, 2, 2, 1], [2, 2]))
        [2]
    """
    return list(set(nums1) & set(nums2))


def longest_consecutive(nums: List[int]) -> int:
    """
    Find length of longest consecutive sequence.
    
    Time: O(n), Space: O(n)
    
    Example:
        >>> longest_consecutive([100, 4, 200, 1, 3, 2])
        4  # [1, 2, 3, 4]
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            max_length = max(max_length, length)
    
    return max_length
