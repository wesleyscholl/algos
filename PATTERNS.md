# Algorithm Patterns - Quick Reference Guide

This guide helps you quickly identify which algorithmic pattern to apply to solve a problem. Master pattern recognition to ace coding interviews!

## 🎯 Pattern Recognition Framework

**How to use this guide:**
1. Read problem statement
2. Identify key characteristics
3. Match to pattern below
4. Apply pattern template
5. Optimize if needed

---

## 📊 Pattern Selection Flowchart

```
Is it a sequence/array problem?
├─ Yes → Need to find pairs/triplets?
│         ├─ Yes → TWO POINTERS or SLIDING WINDOW
│         └─ No → Need to track elements?
│                  ├─ Yes → MONOTONIC STACK
│                  └─ No → KADANE'S or BINARY SEARCH
│
└─ No → Is it a tree/graph?
          ├─ Yes → Need shortest path?
          │         ├─ Yes → BFS or DIJKSTRA
          │         └─ No → DFS or BACKTRACKING
          │
          └─ No → Dynamic optimization?
                    ├─ Yes → DYNAMIC PROGRAMMING
                    └─ No → Special structure? → Consider other patterns
```

---

## 🔍 Pattern Quick Reference

### 1. Two Pointers

**When to use:**
- Array/string with sorted or partially sorted data
- Need to find pairs/triplets with specific sum
- Need to remove duplicates
- Palindrome checking
- Merging sorted arrays

**Key indicators:**
- ✅ "Find pairs that..."
- ✅ "Remove duplicates..."
- ✅ "Reverse..."
- ✅ "Is palindrome..."
- ✅ Sorted array input

**Time:** O(n) | **Space:** O(1)

**Template:**
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Check condition
        if meets_condition(arr[left], arr[right]):
            # Process and move pointers
            left += 1
            right -= 1
        elif arr[left] < target:
            left += 1
        else:
            right -= 1
```

**Classic Problems:**
- Two Sum II (sorted array)
- 3Sum
- Container With Most Water
- Valid Palindrome

---

### 2. Sliding Window

**When to use:**
- Contiguous subarray/substring problems
- Maximum/minimum sum of subarray size K
- Longest substring with K distinct characters
- Pattern matching in strings

**Key indicators:**
- ✅ "Subarray/substring of size..."
- ✅ "Longest/shortest subarray with..."
- ✅ "Maximum sum of K consecutive..."
- ✅ Contiguous elements

**Time:** O(n) | **Space:** O(k)

**Template:**
```python
def sliding_window(arr, k):
    window_start = 0
    window_sum = 0
    result = 0
    
    for window_end in range(len(arr)):
        # Add to window
        window_sum += arr[window_end]
        
        # Shrink if needed
        if window_end >= k - 1:
            result = max(result, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    return result
```

**Classic Problems:**
- Maximum Sum Subarray of Size K
- Longest Substring with K Distinct Characters
- Fruits Into Baskets
- Minimum Window Substring

---

### 3. Fast & Slow Pointers

**When to use:**
- Linked list cycle detection
- Finding middle of linked list
- Cycle start point
- Happy number problems

**Key indicators:**
- ✅ "Detect cycle..."
- ✅ "Find middle..."
- ✅ Linked list problems
- ✅ "Happy number" type problems

**Time:** O(n) | **Space:** O(1)

**Template:**
```python
def fast_slow(head):
    slow = fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle detected
    
    return False  # No cycle
```

**Classic Problems:**
- Linked List Cycle
- Find Middle of Linked List
- Happy Number
- Palindrome Linked List

---

### 4. Merge Intervals

**When to use:**
- Overlapping intervals
- Meeting room problems
- Insert/merge intervals
- Interval scheduling

**Key indicators:**
- ✅ "Merge overlapping..."
- ✅ "Schedule meetings..."
- ✅ "Insert interval..."
- ✅ Given list of intervals

**Time:** O(n log n) | **Space:** O(n)

**Template:**
```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Overlap?
        if current[0] <= last[1]:
            # Merge
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # No overlap
            merged.append(current)
    
    return merged
```

**Classic Problems:**
- Merge Intervals
- Insert Interval
- Meeting Rooms II
- Employee Free Time

---

### 5. Cyclic Sort

**When to use:**
- Array contains numbers in range [1, n]
- Find missing/duplicate numbers
- Rearrange in place

**Key indicators:**
- ✅ "Find missing number..."
- ✅ "Array contains 1 to n..."
- ✅ "Find duplicate..."
- ✅ Numbers in specific range

**Time:** O(n) | **Space:** O(1)

**Template:**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        
        if nums[i] != nums[correct_index]:
            # Swap to correct position
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
```

**Classic Problems:**
- Missing Number
- Find All Duplicates
- Find the Duplicate Number
- First Missing Positive

---

### 6. In-place Linked List Reversal

**When to use:**
- Reverse part of linked list
- Reverse in groups
- Reverse between positions

**Key indicators:**
- ✅ "Reverse linked list..."
- ✅ "Reverse nodes in K-group..."
- ✅ "Reverse between positions..."

**Time:** O(n) | **Space:** O(1)

**Template:**
```python
def reverse_linkedlist(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev  # New head
```

**Classic Problems:**
- Reverse Linked List
- Reverse Linked List II
- Reverse Nodes in k-Group
- Rotate List

---

### 7. Tree BFS

**When to use:**
- Level-order traversal
- Shortest path in tree
- Left/rightmost nodes per level
- Connect nodes at same level

**Key indicators:**
- ✅ "Level by level..."
- ✅ "Zigzag traversal..."
- ✅ "Connect nodes..."
- ✅ "Minimum depth..."

**Time:** O(n) | **Space:** O(n)

**Template:**
```python
from collections import deque

def tree_bfs(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

**Classic Problems:**
- Binary Tree Level Order Traversal
- Zigzag Level Order Traversal
- Minimum Depth of Binary Tree
- Connect Level Order Siblings

---

### 8. Tree DFS

**When to use:**
- Root-to-leaf path problems
- Sum of paths
- Validate tree properties
- Serialize/deserialize

**Key indicators:**
- ✅ "Root to leaf..."
- ✅ "Path sum..."
- ✅ "Maximum depth..."
- ✅ "Validate BST..."

**Time:** O(n) | **Space:** O(h) where h = height

**Template:**
```python
def tree_dfs(root, target_sum):
    if not root:
        return False
    
    # Leaf node
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Recurse on children
    target_sum -= root.val
    return (tree_dfs(root.left, target_sum) or 
            tree_dfs(root.right, target_sum))
```

**Classic Problems:**
- Path Sum
- Sum of Path Numbers
- Maximum Path Sum
- Diameter of Binary Tree

---

### 9. Two Heaps

**When to use:**
- Find median of stream
- Sliding window median
- Balance two data sets

**Key indicators:**
- ✅ "Find median..."
- ✅ "Balance..."
- ✅ "Middle element..."

**Time:** O(log n) per insertion | **Space:** O(n)

**Template:**
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Lower half (negated for max)
        self.min_heap = []  # Upper half
    
    def add_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]
```

**Classic Problems:**
- Find Median from Data Stream
- Sliding Window Median
- IPO

---

### 10. Subsets

**When to use:**
- Generate all combinations
- Power set problems
- Permutations
- Letter combinations

**Key indicators:**
- ✅ "All subsets..."
- ✅ "All combinations..."
- ✅ "All permutations..."
- ✅ "Generate..."

**Time:** O(2^n) or O(n!) | **Space:** O(n)

**Template:**
```python
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

**Classic Problems:**
- Subsets
- Permutations
- Combinations
- Letter Combinations of Phone Number

---

### 11. Modified Binary Search

**When to use:**
- Search in rotated sorted array
- Find peak element
- Search in infinite array
- Find range of target

**Key indicators:**
- ✅ "Sorted" or "rotated sorted"
- ✅ "Find peak..."
- ✅ O(log n) time required
- ✅ "Search in..."

**Time:** O(log n) | **Space:** O(1)

**Template:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

**Classic Problems:**
- Search in Rotated Sorted Array
- Find Peak Element
- Search in Infinite Sorted Array
- Find Smallest Letter Greater Than Target

---

### 12. Top K Elements

**When to use:**
- K largest/smallest elements
- Kth largest element
- K closest points
- Frequency-based problems

**Key indicators:**
- ✅ "Top K..."
- ✅ "K largest/smallest..."
- ✅ "K most frequent..."
- ✅ "K closest..."

**Time:** O(n log k) | **Space:** O(k)

**Template:**
```python
import heapq

def top_k_elements(nums, k):
    # Min heap of size k
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return list(heap)
```

**Classic Problems:**
- Kth Largest Element
- K Closest Points to Origin
- Top K Frequent Elements
- K Closest Numbers

---

### 13. K-way Merge

**When to use:**
- Merge K sorted arrays/lists
- Smallest range covering elements
- Kth smallest in sorted matrix

**Key indicators:**
- ✅ "K sorted arrays/lists..."
- ✅ "Merge K..."
- ✅ "Kth smallest..."
- ✅ Multiple sorted inputs

**Time:** O(n log k) | **Space:** O(k)

**Template:**
```python
import heapq

def merge_k_sorted(lists):
    heap = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result
```

**Classic Problems:**
- Merge K Sorted Lists
- Kth Smallest Element in Sorted Matrix
- Smallest Range Covering K Lists
- Smallest Number Range

---

### 14. Bitwise XOR

**When to use:**
- Find missing/duplicate with XOR properties
- Single number problems
- Bit manipulation tricks

**Key indicators:**
- ✅ "Find missing..."
- ✅ "Single number..."
- ✅ "Appears once..."
- ✅ O(1) space required

**Time:** O(n) | **Space:** O(1)

**Template:**
```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**XOR Properties:**
- `a ^ a = 0` (same numbers cancel)
- `a ^ 0 = a` (identity)
- `a ^ b ^ a = b` (commutative)

**Classic Problems:**
- Single Number
- Single Number II
- Missing Number
- Find the Difference

---

## 🎓 Pattern Recognition Cheat Sheet

| Problem Type | Pattern | Time | Space |
|--------------|---------|------|-------|
| Find pairs in sorted array | Two Pointers | O(n) | O(1) |
| Subarray of size K | Sliding Window | O(n) | O(k) |
| Detect cycle in linked list | Fast & Slow | O(n) | O(1) |
| Merge overlapping ranges | Merge Intervals | O(n log n) | O(n) |
| Find missing in [1...n] | Cyclic Sort | O(n) | O(1) |
| Reverse linked list | In-place Reversal | O(n) | O(1) |
| Level-order tree traversal | Tree BFS | O(n) | O(n) |
| Root-to-leaf paths | Tree DFS | O(n) | O(h) |
| Find median of stream | Two Heaps | O(log n) | O(n) |
| All combinations | Subsets/Backtracking | O(2^n) | O(n) |
| Search in rotated array | Modified Binary Search | O(log n) | O(1) |
| K largest elements | Top K | O(n log k) | O(k) |
| Merge K sorted lists | K-way Merge | O(n log k) | O(k) |
| Find single number | Bitwise XOR | O(n) | O(1) |

---

## 💡 Pro Tips

### How to Master Patterns

1. **Learn one pattern at a time** - Don't rush
2. **Solve 5-10 problems per pattern** - Build muscle memory
3. **Identify patterns in problem statements** - Key skill
4. **Time yourself** - Simulate interview pressure
5. **Explain your approach out loud** - Communication matters

### Common Mistakes

❌ **Jumping to code too quickly** - Think first, code second  
❌ **Not considering edge cases** - Empty input, single element, etc.  
❌ **Ignoring time/space complexity** - Always analyze  
❌ **Not testing with examples** - Walk through manually  
❌ **Memorizing solutions** - Understand the pattern instead

### Interview Strategy

1. **Clarify the problem** - Ask questions
2. **Identify the pattern** - Use this guide
3. **Discuss approach** - Before coding
4. **Write clean code** - Use template
5. **Test with examples** - Walk through
6. **Analyze complexity** - State time/space
7. **Optimize if possible** - Better approach?

---

## 📚 Study Path

### Week 1-2: Foundation
- Two Pointers
- Sliding Window
- Fast & Slow Pointers

### Week 3-4: Trees & Graphs
- Tree BFS
- Tree DFS
- Graph BFS/DFS

### Week 5-6: Advanced
- Dynamic Programming
- Backtracking
- Greedy Algorithms

### Week 7-8: Optimization
- Top K Elements
- K-way Merge
- Bitwise Operations

---

**Remember: Pattern recognition is a skill. Practice makes perfect! 🚀**
