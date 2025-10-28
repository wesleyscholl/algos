"""
Two Pointers Pattern Implementations

Pattern: Two indices moving inward/outward or fast/slow
Time: O(n)
Space: O(1)
"""

from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers in sorted array that add to target.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        [1, 2]  # 1-indexed
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome (ignore non-alphanumeric).
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> nums = [1, 1, 2, 2, 3]
        >>> k = remove_duplicates(nums)
        >>> nums[:k]
        [1, 2, 3]
    """
    if not nums:
        return 0
    
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    
    return write


def container_with_most_water(height: List[int]) -> int:
    """
    Find two lines that form container with most water.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        max_area = max(max_area, area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.
    
    Time: O(n²), Space: O(1) excluding output
    
    Example:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result


def reverse_string(s: List[str]) -> None:
    """
    Reverse string in-place.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> s = ["h", "e", "l", "l", "o"]
        >>> reverse_string(s)
        >>> s
        ['o', 'l', 'l', 'e', 'h']
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def move_zeroes(nums: List[int]) -> None:
    """
    Move all zeros to end while maintaining order.
    
    Time: O(n), Space: O(1)
    
    Example:
        >>> nums = [0, 1, 0, 3, 12]
        >>> move_zeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0]
    """
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


def partition(s: str) -> List[List[str]]:
    """
    Partition string into all possible palindrome substrings.
    Uses helper function with two pointers for palindrome check.
    
    Time: O(n * 2^n), Space: O(n)
    
    Example:
        >>> partition("aab")
        [['a', 'a', 'b'], ['aa', 'b']]
    """
    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def backtrack(start: int, path: List[str]):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome_range(start, end):
                path.append(s[start:end + 1])
                backtrack(end + 1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result
