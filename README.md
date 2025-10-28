# 🧠 Algorithm Code Patterns & Complexity Cheat Sheet

A comprehensive quick-reference guide to help you **identify patterns**, **build intuition**, and **ace technical interviews**.  
Includes common approaches, Python snippets, and Big-O complexities.

---

## 📋 Table of Contents

1. [Hash Map / Dictionary](#1-hash-map--dictionary)
2. [Two Pointers](#2-two-pointers)
3. [Sliding Window](#3-sliding-window)
4. [Prefix Sum / Cumulative Count](#4-prefix-sum--cumulative-count)
5. [Binary Search](#5-binary-search)
6. [Depth-First Search (DFS) & Backtracking](#6-depth-first-search-dfs--backtracking)
7. [Breadth-First Search (BFS)](#7-breadth-first-search-bfs)
8. [Dynamic Programming (DP)](#8-dynamic-programming-dp)
9. [Greedy Algorithms](#9-greedy-algorithms)
10. [Sorting & Searching Patterns](#10-sorting--searching-patterns)
11. [Heap / Priority Queue](#11-heap--priority-queue)
12. [Graph Patterns](#12-graph-patterns)
13. [Common Complexities Reference](#13-common-complexities-reference)
14. [Interview Strategy](#14-interview-strategy)

---

## 1. Hash Map / Dictionary

**Pattern:** Fast lookups, counting, and complements.  
**When to Use:** When you need O(1) access to previously seen data.

**Examples:**
- Two Sum
- Valid Anagram
- Subarray Sum Equals K

```python
# Two Sum
d = {}
for i, n in enumerate(nums):
    if target - n in d:
        return [d[target - n], i]
    d[n] = i
````

**Common Variants:**

* Count elements: `Counter(nums)`
* Track frequency or index
* Prefix-sum to detect subarrays

**Complexity:**

| Operation       | Time | Space |
| --------------- | ---- | ----- |
| Insert / Lookup | O(1) | O(n)  |

---

## 2. Two Pointers

**Pattern:** Use two indices moving inward or outward.
**When to Use:** Sorted arrays, linked lists, or string comparisons.

**Examples:**

* Sorted Two Sum
* Container With Most Water
* Palindrome Check
* Remove Duplicates

```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target: return [l, r]
    if s < target: l += 1
    else: r -= 1
```

**Variations:**

* Fast/slow pointers for cycle detection
* Move both pointers conditionally

**Complexity:**

| Operation     | Time | Space |
| ------------- | ---- | ----- |
| Traverse once | O(n) | O(1)  |

---

## 3. Sliding Window

**Pattern:** Dynamic window that expands/contracts.
**When to Use:** Substrings, subarrays, or fixed-size segment problems.

**Examples:**

* Longest substring without repeating chars
* Max sum subarray of size k
* Minimum window substring

```python
window, l, best = {}, 0, 0
for r, c in enumerate(s):
    window[c] = window.get(c, 0) + 1
    while window[c] > 1:
        window[s[l]] -= 1
        l += 1
    best = max(best, r - l + 1)
```

**Types:**

* Fixed-size window
* Variable-size window (expand & shrink)

**Complexity:**

| Operation   | Time | Space |
| ----------- | ---- | ----- |
| Move window | O(n) | O(k)  |

---

## 4. Prefix Sum / Cumulative Count

**Pattern:** Store cumulative results to answer range queries fast.
**When to Use:** Subarray sums, range differences, balance tracking.

**Examples:**

* Subarray sum equals K
* Range sum queries
* Balance parentheses

```python
prefix = {0: 1}
s = res = 0
for n in nums:
    s += n
    res += prefix.get(s - k, 0)
    prefix[s] = prefix.get(s, 0) + 1
```

**Complexity:**

| Operation    | Time | Space |
| ------------ | ---- | ----- |
| Build prefix | O(n) | O(n)  |

---

## 5. Binary Search

**Pattern:** Divide and conquer to find an element or condition boundary.
**When to Use:** Sorted data, search conditions, or monotonic functions.

**Examples:**

* Search in Rotated Array
* Find minimum in rotated array
* Square root, Peak element

```python
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] == target: return m
    if nums[m] < target: l = m + 1
    else: r = m - 1
```

**Binary Search on Answer:**
Used for optimization problems (“minimum X such that…”).

**Complexity:**

| Operation | Time     | Space |
| --------- | -------- | ----- |
| Search    | O(log n) | O(1)  |

---

## 6. Depth-First Search (DFS) & Backtracking

**Pattern:** Explore all possibilities (tree, grid, graph, recursion).
**When to Use:** All subsets, permutations, paths, or decision trees.

**Examples:**

* Subsets / Permutations
* N-Queens
* Word Search

```python
def dfs(i, path):
    if i == len(nums):
        res.append(path[:])
        return
    dfs(i + 1, path + [nums[i]])
    dfs(i + 1, path)
```

**Backtracking Tip:** Undo changes before returning from recursion.

**Complexity:**

| Operation   | Time  | Space |
| ----------- | ----- | ----- |
| Explore all | O(2ⁿ) | O(n)  |

---

## 7. Breadth-First Search (BFS)

**Pattern:** Level-by-level traversal using a queue.
**When to Use:** Shortest path, level order, connected components.

**Examples:**

* Binary Tree Level Order
* Word Ladder
* Shortest Path in Grid

```python
from collections import deque
q = deque([start])
seen = {start}
while q:
    node = q.popleft()
    for nei in graph[node]:
        if nei not in seen:
            seen.add(nei)
            q.append(nei)
```

**Complexity:**

| Operation | Time     | Space |
| --------- | -------- | ----- |
| Visit all | O(V + E) | O(V)  |

---

## 8. Dynamic Programming (DP)

**Pattern:** Break problem into overlapping subproblems.
**When to Use:** Optimal decisions, counting, or sequences.

**Examples:**

* Fibonacci, Climbing Stairs
* Knapsack, Coin Change
* Longest Increasing Subsequence

```python
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
```

**Tips:**

* **Top-down:** Memoization (recursive)
* **Bottom-up:** Tabulation (iterative)

**Complexity:**

| Operation   | Time | Space                   |
| ----------- | ---- | ----------------------- |
| DP solution | O(n) | O(n) (→ O(1) optimized) |

---

## 9. Greedy Algorithms

**Pattern:** Always choose best local decision hoping for global optimum.
**When to Use:** Scheduling, intervals, simple optimization.

**Examples:**

* Activity selection
* Jump Game
* Minimum coins

```python
intervals.sort(key=lambda x: x[1])
end, count = float('-inf'), 0
for s, e in intervals:
    if s >= end:
        count += 1
        end = e
```

**Complexity:**

| Operation      | Time       | Space |
| -------------- | ---------- | ----- |
| Sort + Iterate | O(n log n) | O(1)  |

---

## 10. Sorting & Searching Patterns

**Common Uses:**

* Preprocess data for two-pointer or greedy
* Merge intervals
* Binary search usage

```python
nums.sort()
```

| Algorithm                 | Average    | Worst      | Space    | Stable |
| ------------------------- | ---------- | ---------- | -------- | ------ |
| QuickSort                 | O(n log n) | O(n²)      | O(log n) | ❌      |
| MergeSort                 | O(n log n) | O(n log n) | O(n)     | ✅      |
| HeapSort                  | O(n log n) | O(n log n) | O(1)     | ❌      |
| TimSort (Python `sort()`) | O(n log n) | O(n log n) | O(n)     | ✅      |

---

## 11. Heap / Priority Queue

**Pattern:** Extract min/max efficiently.
**When to Use:** Top-k problems, running median, Dijkstra’s.

**Examples:**

* Kth largest element
* Merge k sorted lists
* Task scheduling

```python
import heapq
heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k: heapq.heappop(heap)
```

**Complexity:**

| Operation | Time     | Space |
| --------- | -------- | ----- |
| Push/Pop  | O(log n) | O(n)  |

---

## 12. Graph Patterns

**Representation:**

```python
graph = {u: [] for u in range(n)}
for u, v in edges:
    graph[u].append(v)
```

**Traversals:**

* DFS (recursive or stack)
* BFS (queue)
* Topological sort (Kahn’s algorithm)
* Union-Find (for connected components)

**Complexity:**

| Operation  | Time           | Space    |
| ---------- | -------------- | -------- |
| DFS/BFS    | O(V + E)       | O(V + E) |
| Union-Find | O(α(n)) per op | O(n)     |

---

## 13. Common Complexities Reference

| Operation / Pattern | Time Complexity | Space |
| ------------------- | --------------- | ----- |
| Single Loop         | O(n)            | O(1)  |
| Nested Loops        | O(n²)           | O(1)  |
| Sorting             | O(n log n)      | O(1)  |
| Binary Search       | O(log n)        | O(1)  |
| DFS / BFS           | O(V + E)        | O(V)  |
| Dynamic Programming | O(n) – O(n²)    | O(n)  |
| Backtracking        | O(2ⁿ)           | O(n)  |
| Matrix Traversal    | O(m × n)        | O(1)  |

---

## 14. Interview Strategy

**Preparation Flow:**

1. Master ~10 patterns (above)
2. Practice 2–3 problems per pattern
3. Focus on:

   * Identifying pattern type
   * Optimizing from brute-force → O(n log n) or O(n)
   * Writing clean, consistent code

**Tips:**

* Always check edge cases
* Use `enumerate()` and `defaultdict()` smartly
* Write helper functions for clarity
* If stuck, verbalize brute-force first

**Mindset:**

> “Every problem is a variation of one of these patterns.”

---

✅ **Recommended Next Step:**
Practice each pattern on LeetCode:

* Easy → Medium of same type
* Focus on *why* a pattern fits, not just memorizing code

---

### ⭐ Author

Created for engineers mastering **problem-solving fundamentals**, **systematic pattern recognition**, and **AI-enhanced learning**.
