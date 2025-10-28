"""
Binary Search Pattern Implementations

Pattern: Divide and conquer for sorted data or search spaces
Time: O(log n)
Space: O(1)
"""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Classic binary search in sorted array.
    
    Time: O(log n), Space: O(1)
    
    Example:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def search_rotated_array(nums: List[int], target: int) -> int:
    """
    Search in rotated sorted array.
    
    Time: O(log n), Space: O(1)
    
    Example:
        >>> search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0)
        4
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


def find_min_rotated_array(nums: List[int]) -> int:
    """
    Find minimum in rotated sorted array.
    
    Time: O(log n), Space: O(1)
    
    Example:
        >>> find_min_rotated_array([3, 4, 5, 1, 2])
        1
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return nums[left]


def search_insert_position(nums: List[int], target: int) -> int:
    """
    Find position where target should be inserted.
    
    Time: O(log n), Space: O(1)
    
    Example:
        >>> search_insert_position([1, 3, 5, 6], 5)
        2
        >>> search_insert_position([1, 3, 5, 6], 2)
        1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


def find_first_and_last(nums: List[int], target: int) -> List[int]:
    """
    Find first and last position of target in sorted array.
    
    Time: O(log n), Space: O(1)
    
    Example:
        >>> find_first_and_last([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
    """
    def find_bound(is_first: bool) -> int:
        left, right = 0, len(nums) - 1
        bound = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # Look left for first occurrence
                else:
                    left = mid + 1   # Look right for last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return bound
    
    return [find_bound(True), find_bound(False)]


def sqrt(x: int) -> int:
    """
    Compute square root (integer part).
    
    Time: O(log n), Space: O(1)
    
    Example:
        >>> sqrt(8)
        2
        >>> sqrt(16)
        4
    """
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right


def find_peak_element(nums: List[int]) -> int:
    """
    Find a peak element (greater than neighbors).
    
    Time: O(log n), Space: O(1)
    
    Example:
        >>> nums = [1, 2, 3, 1]
        >>> find_peak_element(nums)
        2
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[mid + 1]:
            # Peak is on left side (including mid)
            right = mid
        else:
            # Peak is on right side
            left = mid + 1
    
    return left


def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search in 2D matrix sorted row-wise and column-wise.
    
    Time: O(log(m*n)), Space: O(1)
    
    Example:
        >>> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        >>> search_2d_matrix(matrix, 3)
        True
    """
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        row, col = divmod(mid, n)
        mid_val = matrix[row][col]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


def min_eating_speed(piles: List[int], h: int) -> int:
    """
    Find minimum eating speed to finish bananas within h hours.
    Binary search on answer space.
    
    Time: O(n log m) where m is max pile size, Space: O(1)
    
    Example:
        >>> min_eating_speed([3, 6, 7, 11], 8)
        4
    """
    def can_finish(k: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k  # Ceiling division
        return hours <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
