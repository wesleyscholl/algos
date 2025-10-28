"""
Sliding Window Pattern Implementations

Pattern: Dynamic window that expands/contracts
Time: O(n)
Space: O(k) where k is window size or character set
"""

from typing import List, Dict
from collections import defaultdict, Counter


def max_sum_subarray(nums: List[int], k: int) -> int:
    """
    Find maximum sum of subarray of size k.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
        39  # [4, 2, 10, 23]
    """
    if len(nums) < k:
        return 0
    
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def length_of_longest_substring(s: str) -> int:
    """
    Find length of longest substring without repeating characters.
    
    Time: O(n), Space: O(min(n, m)) where m is charset size
    
    Example:
        >>> length_of_longest_substring("abcabcbb")
        3  # "abc"
        >>> length_of_longest_substring("pwwkew")
        3  # "wke"
    """
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If char seen and in current window, move left
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


def min_window_substring(s: str, t: str) -> str:
    """
    Find minimum window substring containing all chars of t.
    
    Time: O(n + m), Space: O(m)
    
    Example:
        >>> min_window_substring("ADOBECODEBANC", "ABC")
        'BANC'
    """
    if not s or not t:
        return ""
    
    target_count = Counter(t)
    required = len(target_count)
    formed = 0
    
    window_counts = defaultdict(int)
    left = 0
    min_len = float('inf')
    min_left = 0
    
    for right, char in enumerate(s):
        window_counts[char] += 1
        
        if char in target_count and window_counts[char] == target_count[char]:
            formed += 1
        
        # Try to contract window
        while formed == required and left <= right:
            # Update result if smaller window found
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            
            # Remove leftmost char
            window_counts[s[left]] -= 1
            if s[left] in target_count and window_counts[s[left]] < target_count[s[left]]:
                formed -= 1
            
            left += 1
    
    return "" if min_len == float('inf') else s[min_left:min_left + min_len]


def longest_repeating_character_replacement(s: str, k: int) -> int:
    """
    Find longest substring with same letter after k replacements.
    
    Time: O(n), Space: O(1) [26 letters]
    
    Example:
        >>> longest_repeating_character_replacement("AABABBA", 1)
        4  # "AABA"
    """
    count = defaultdict(int)
    left = 0
    max_count = 0
    max_length = 0
    
    for right, char in enumerate(s):
        count[char] += 1
        max_count = max(max_count, count[char])
        
        # If we need more than k replacements, shrink window
        window_size = right - left + 1
        if window_size - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


def max_consecutive_ones_iii(nums: List[int], k: int) -> int:
    """
    Find max consecutive 1s after flipping at most k zeros.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> max_consecutive_ones_iii([1,1,1,0,0,0,1,1,1,1,0], 2)
        6
    """
    left = 0
    zeros = 0
    max_length = 0
    
    for right, num in enumerate(nums):
        if num == 0:
            zeros += 1
        
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of p's anagrams in s.
    
    Time: O(n), Space: O(1) [26 letters]
    
    Example:
        >>> find_anagrams("cbaebabacd", "abc")
        [0, 6]
    """
    if len(p) > len(s):
        return []
    
    p_count = Counter(p)
    window_count = Counter(s[:len(p) - 1])
    result = []
    
    for i in range(len(p) - 1, len(s)):
        # Add new character
        window_count[s[i]] += 1
        
        # Check if anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
        
        # Remove leftmost character
        left_char = s[i - len(p) + 1]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
    
    return result


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find longest substring with at most k distinct characters.
    
    Time: O(n), Space: O(k)
    
    Example:
        >>> length_of_longest_substring_k_distinct("eceba", 2)
        3  # "ece"
    """
    if k == 0:
        return 0
    
    char_count = defaultdict(int)
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        char_count[char] += 1
        
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
