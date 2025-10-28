"""
Heap / Priority Queue Pattern Implementations

Pattern: Extract min/max efficiently
Time: O(log n) per operation
Space: O(n)
"""

import heapq
from typing import List, Optional
from collections import Counter


def kth_largest_element(nums: List[int], k: int) -> int:
    """
    Find kth largest element using min heap.
    
    Time: O(n log k), Space: O(k)
    
    Example:
        >>> kth_largest_element([3, 2, 1, 5, 6, 4], 2)
        5
    """
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.
    
    Time: O(n log k), Space: O(n)
    
    Example:
        >>> sorted(top_k_frequent([1,1,1,2,2,3], 2))
        [1, 2]
    """
    count = Counter(nums)
    
    # Use min heap with negative frequencies for top k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]


def merge_k_sorted_lists(lists: List[Optional[List[int]]]) -> List[int]:
    """
    Merge k sorted lists using heap.
    
    Time: O(N log k) where N = total elements, Space: O(k)
    
    Example:
        >>> merge_k_sorted_lists([[1,4,5], [1,3,4], [2,6]])
        [1, 1, 2, 3, 4, 4, 5, 6]
    """
    heap = []
    result = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result


def find_median_from_stream():
    """
    Find median from data stream using two heaps.
    
    Time: O(log n) per add, O(1) for median
    Space: O(n)
    """
    class MedianFinder:
        def __init__(self):
            self.small = []  # Max heap (negated values)
            self.large = []  # Min heap
        
        def addNum(self, num: int) -> None:
            # Add to max heap (small)
            heapq.heappush(self.small, -num)
            
            # Balance: move largest from small to large
            if self.small and self.large and (-self.small[0] > self.large[0]):
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            
            # Maintain size property
            if len(self.small) > len(self.large) + 1:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            elif len(self.large) > len(self.small):
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -val)
        
        def findMedian(self) -> float:
            if len(self.small) > len(self.large):
                return -self.small[0]
            return (-self.small[0] + self.large[0]) / 2.0
    
    return MedianFinder()


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin.
    
    Time: O(n log k), Space: O(k)
    
    Example:
        >>> k_closest_points([[1,3], [-2,2], [5,8], [0,1]], 2)
        [[-2, 2], [0, 1]]  # or [[0, 1], [-2, 2]]
    """
    heap = []
    
    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max heap
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [[x, y] for _, x, y in heap]


def task_scheduler(tasks: List[str], n: int) -> int:
    """
    Find minimum time to complete all tasks with cooldown.
    
    Time: O(m log k) where m = total tasks, k = unique tasks
    Space: O(k)
    
    Example:
        >>> task_scheduler(['A','A','A','B','B','B'], 2)
        8  # A -> B -> idle -> A -> B -> idle -> A -> B
    """
    if n == 0:
        return len(tasks)
    
    count = Counter(tasks)
    max_heap = [-freq for freq in count.values()]
    heapq.heapify(max_heap)
    
    time = 0
    
    while max_heap:
        cycle = []
        cycle_time = 0
        
        # Process n+1 tasks (or fewer if heap is smaller)
        for _ in range(n + 1):
            if max_heap:
                freq = heapq.heappop(max_heap)
                cycle.append(freq + 1)  # Decrease frequency (remember it's negative)
                cycle_time += 1
        
        # Add back tasks that still have remaining count
        for freq in cycle:
            if freq < 0:
                heapq.heappush(max_heap, freq)
        
        # If heap is empty, no need for idle time
        time += cycle_time if not max_heap else n + 1
    
    return time


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window of size k.
    Uses heap with lazy deletion.
    
    Time: O(n log n), Space: O(n)
    
    Example:
        >>> sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3)
        [3, 3, 5, 5, 6, 7]
    """
    if not nums or k == 0:
        return []
    
    heap = []
    result = []
    
    for i, num in enumerate(nums):
        heapq.heappush(heap, (-num, i))
        
        if i >= k - 1:
            # Remove elements outside window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            result.append(-heap[0][0])
    
    return result


def last_stone_weight(stones: List[int]) -> int:
    """
    Simulate stone smashing (heavier stones remain).
    
    Time: O(n log n), Space: O(n)
    
    Example:
        >>> last_stone_weight([2, 7, 4, 1, 8, 1])
        1
    """
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        
        if first != second:
            heapq.heappush(heap, -(first - second))
    
    return -heap[0] if heap else 0


def reorganize_string(s: str) -> str:
    """
    Reorganize string so no adjacent chars are same.
    
    Time: O(n log k), Space: O(k) where k = unique chars
    
    Example:
        >>> reorganize_string("aab")
        'aba'
    """
    count = Counter(s)
    max_heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(max_heap)
    
    result = []
    prev_freq, prev_char = 0, ''
    
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)
        
        # Add previous char back if it still has frequency
        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
        
        prev_freq, prev_char = freq + 1, char
    
    result_str = ''.join(result)
    return result_str if len(result_str) == len(s) else ""
