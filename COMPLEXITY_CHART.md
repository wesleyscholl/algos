# 📊 Algorithm Complexity Chart

Comprehensive time and space complexity reference for all implemented algorithms.

## 📋 Table of Contents

1. [Hash Map / Dictionary](#hash-map--dictionary)
2. [Two Pointers](#two-pointers)
3. [Sliding Window](#sliding-window)
4. [Binary Search](#binary-search)
5. [DFS & Backtracking](#dfs--backtracking)
6. [BFS (Breadth-First Search)](#bfs-breadth-first-search)
7. [Dynamic Programming](#dynamic-programming)
8. [Graph Algorithms](#graph-algorithms)
9. [Heap / Priority Queue](#heap--priority-queue)
10. [Complexity Comparison Tables](#complexity-comparison-tables)

---

## Hash Map / Dictionary

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Two Sum** | O(n) | O(n) | Single pass with hash map |
| **Valid Anagram** | O(n) | O(1) | Limited alphabet (26 letters) |
| **Subarray Sum Equals K** | O(n) | O(n) | Prefix sum with hash map |
| **Group Anagrams** | O(n × k log k) | O(n × k) | n strings, k = max length |
| **First Unique Character** | O(n) | O(1) | Limited alphabet |
| **Contains Duplicate** | O(n) | O(n) | Set-based detection |
| **Array Intersection** | O(n + m) | O(min(n,m)) | Two sets |
| **Longest Consecutive** | O(n) | O(n) | Set-based sequence detection |

**Pattern Characteristics:**
- **Best for:** Fast lookups, frequency counting, complement finding
- **Average case:** O(1) lookup, O(n) overall
- **Worst case:** O(n) hash collisions (rare with good hash function)

---

## Two Pointers

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Two Sum (Sorted)** | O(n) | O(1) | Left/right pointers |
| **Palindrome Check** | O(n) | O(1) | Skip non-alphanumeric |
| **Remove Duplicates** | O(n) | O(1) | In-place with read/write pointers |
| **Container With Water** | O(n) | O(1) | Greedy pointer movement |
| **Three Sum** | O(n²) | O(1) | O(n log n) sort + O(n²) pairs |
| **Reverse String** | O(n) | O(1) | In-place swap |
| **Move Zeroes** | O(n) | O(1) | In-place with write pointer |
| **Partition (Palindrome)** | O(n × 2ⁿ) | O(n) | All palindrome partitions |

**Pattern Characteristics:**
- **Best for:** Sorted arrays, in-place operations, palindrome checks
- **Space:** Usually O(1) - no extra data structures
- **Optimization:** Reduces O(n²) nested loops to O(n)

---

## Sliding Window

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Max Sum Subarray (Size K)** | O(n) | O(1) | Fixed-size window |
| **Longest Substring (No Repeat)** | O(n) | O(min(n,m)) | m = charset size |
| **Min Window Substring** | O(n + m) | O(m) | Target string length m |
| **Longest Repeating Char Replace** | O(n) | O(1) | 26 letters max |
| **Max Consecutive Ones III** | O(n) | O(1) | Track zero count |
| **Find Anagrams** | O(n) | O(1) | 26 letters max |
| **K Distinct Characters** | O(n) | O(k) | At most k chars in window |

**Pattern Characteristics:**
- **Best for:** Contiguous subarray/substring problems
- **Window types:** Fixed-size O(n), variable-size O(n)
- **Optimization:** Avoids O(n²) brute force checking

---

## Binary Search

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Classic Binary Search** | O(log n) | O(1) | Sorted array |
| **Search Rotated Array** | O(log n) | O(1) | Modified binary search |
| **Find Minimum (Rotated)** | O(log n) | O(1) | One-sided search |
| **Search Insert Position** | O(log n) | O(1) | Find insertion point |
| **Find First and Last** | O(log n) | O(1) | Two binary searches |
| **Integer Square Root** | O(log n) | O(1) | Search space: 1 to n/2 |
| **Find Peak Element** | O(log n) | O(1) | Local maximum |
| **Search 2D Matrix** | O(log(m×n)) | O(1) | Treat as 1D array |
| **Min Eating Speed (Koko)** | O(n log m) | O(1) | n piles, m = max pile |

**Pattern Characteristics:**
- **Best for:** Sorted data, search spaces, optimization problems
- **Search space:** Can be values, indices, or abstract ranges
- **Invariant:** Monotonic function to guide search

---

## DFS & Backtracking

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Subsets** | O(2ⁿ) | O(n) | 2ⁿ subsets, n recursion depth |
| **Permutations** | O(n!) | O(n) | n! permutations |
| **Combination Sum** | O(2^(T/M)) | O(T/M) | T=target, M=min candidate |
| **N-Queens** | O(n!) | O(n²) | n! placements, n² board |
| **Word Search** | O(m×n×4^L) | O(L) | L = word length, 4 directions |
| **Generate Parentheses** | O(4ⁿ/√n) | O(n) | nth Catalan number |
| **Letter Combinations** | O(4ⁿ) | O(n) | Phone keypad, max 4 letters |

**Pattern Characteristics:**
- **Best for:** Generate all possibilities, constraint satisfaction
- **Typical complexity:** Exponential or factorial
- **Optimization:** Pruning, memoization (→ DP)

---

## BFS (Breadth-First Search)

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Level Order Traversal** | O(n) | O(n) | n = number of nodes |
| **Right Side View** | O(n) | O(n) | Visit all nodes |
| **Zigzag Level Order** | O(n) | O(n) | Level-by-level |
| **Shortest Path (Binary Matrix)** | O(n²) | O(n²) | n×n grid, 8 directions |
| **Walls and Gates** | O(m×n) | O(m×n) | Multi-source BFS |
| **Word Ladder** | O(M²×N) | O(M×N) | M=word length, N=word list |
| **Oranges Rotting** | O(m×n) | O(m×n) | Grid simulation |

**Pattern Characteristics:**
- **Best for:** Shortest paths, level-order traversal
- **Queue space:** O(width) where width is max level size
- **Guarantee:** First path found is shortest (unweighted)

---

## Dynamic Programming

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Fibonacci** | O(n) | O(1) | Space-optimized |
| **Climbing Stairs** | O(n) | O(1) | Space-optimized |
| **Coin Change** | O(amount × n) | O(amount) | n = coin types |
| **Longest Increasing Subseq** | O(n²) | O(n) | DP solution (O(n log n) exists) |
| **House Robber** | O(n) | O(1) | Space-optimized |
| **0/1 Knapsack** | O(n × capacity) | O(capacity) | Space-optimized |
| **Longest Common Subseq** | O(m × n) | O(min(m,n)) | Space-optimized |
| **Edit Distance** | O(m × n) | O(n) | Space-optimized |
| **Word Break** | O(n² × m) | O(n) | m = max word length |
| **Unique Paths** | O(m × n) | O(n) | Space-optimized |
| **Max Product Subarray** | O(n) | O(1) | Track max and min |

**Pattern Characteristics:**
- **Best for:** Optimization, counting, decision problems
- **Space optimization:** Often O(n²) → O(n) or O(1)
- **Approaches:** Top-down (memoization) or bottom-up (tabulation)

---

## Graph Algorithms

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **DFS (Adjacency List)** | O(V + E) | O(V) | V vertices, E edges |
| **BFS (Adjacency List)** | O(V + E) | O(V) | Queue + visited set |
| **Has Cycle (Directed)** | O(V + E) | O(V) | DFS with colors |
| **Has Cycle (Undirected)** | O(E × α(V)) | O(V) | Union-Find, α ≈ constant |
| **Connected Components** | O(E × α(V)) | O(V) | Union-Find |
| **Topological Sort** | O(V + E) | O(V) | Kahn's algorithm (BFS) |
| **Course Schedule** | O(V + E) | O(V) | Cycle detection |
| **Dijkstra's Algorithm** | O((V+E) log V) | O(V + E) | Min heap |
| **Bellman-Ford** | O(V × E) | O(V) | Handles negative weights |
| **Clone Graph** | O(V + E) | O(V) | DFS/BFS with hash map |
| **Is Bipartite** | O(V + E) | O(V) | BFS 2-coloring |
| **Network Delay Time** | O((V+E) log V) | O(V + E) | Dijkstra variant |

**Pattern Characteristics:**
- **Representation:** Adjacency list preferred (space efficient)
- **Union-Find:** O(α(n)) per operation, α is inverse Ackermann
- **Shortest path:** Dijkstra for positive, Bellman-Ford for negative

---

## Heap / Priority Queue

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Kth Largest Element** | O(n log k) | O(k) | Min heap of size k |
| **Top K Frequent** | O(n log k) | O(n) | Count + heap |
| **Merge K Sorted Lists** | O(N log k) | O(k) | N total elements, k lists |
| **Median From Stream** | O(log n) add, O(1) find | O(n) | Two heaps |
| **K Closest Points** | O(n log k) | O(k) | Max heap of size k |
| **Task Scheduler** | O(m log k) | O(k) | m tasks, k unique |
| **Sliding Window Maximum** | O(n log n) | O(n) | Heap with lazy deletion |
| **Last Stone Weight** | O(n log n) | O(n) | Max heap simulation |
| **Reorganize String** | O(n log k) | O(k) | k unique chars |

**Pattern Characteristics:**
- **Best for:** Top-K problems, running statistics, scheduling
- **Operations:** Push/pop in O(log n), peek in O(1)
- **Python:** Min heap by default, negate for max heap

---

## Complexity Comparison Tables

### By Time Complexity

| Complexity | Algorithms | Practical Limit (n) |
|------------|-----------|---------------------|
| **O(1)** | Hash lookup, array access | Any |
| **O(log n)** | Binary search, heap operations | 10⁹ |
| **O(n)** | Linear scan, hash map build, two pointers | 10⁸ |
| **O(n log n)** | Sorting, heap sort, merge sort | 10⁶ |
| **O(n√n)** | Optimized LIS (with binary search) | 10⁵ |
| **O(n²)** | Nested loops, naive DP (LCS, Edit Dist) | 10⁴ |
| **O(n³)** | Triple nested loops | 500 |
| **O(2ⁿ)** | Subsets, backtracking | ~20 |
| **O(n!)** | Permutations, traveling salesman | ~10 |

### By Space Complexity

| Space | Pattern/Algorithms | Impact |
|-------|-------------------|--------|
| **O(1)** | Two pointers, space-optimized DP | Minimal memory |
| **O(log n)** | Binary search (recursion), quicksort | Recursion stack |
| **O(n)** | Hash maps, DP arrays, visited sets | Linear memory |
| **O(n²)** | 2D DP, adjacency matrix, grids | Can be expensive |
| **O(V + E)** | Graph adjacency lists | Graph-dependent |
| **O(2ⁿ)** | Backtracking (all solutions) | Exponential memory |

### By Problem Type

| Problem Type | Typical Complexity | Example Algorithms |
|--------------|-------------------|-------------------|
| **Search** | O(log n) to O(n) | Binary search, linear search |
| **Sorting** | O(n log n) | Merge sort, quick sort, heap sort |
| **Graph Traversal** | O(V + E) | DFS, BFS |
| **Shortest Path** | O((V+E) log V) | Dijkstra, A* |
| **MST** | O(E log V) | Kruskal's, Prim's |
| **Dynamic Programming** | O(n) to O(n²) | Depends on states/transitions |
| **Backtracking** | O(2ⁿ) to O(n!) | Generate all possibilities |
| **Greedy** | O(n log n) | Usually sorting + iteration |

---

## 🎯 Quick Selection Guide

### Choose by Input Size

| If n ≤ | Can Use | Examples |
|--------|---------|----------|
| **10** | O(n!), O(2ⁿ) | All permutations, all subsets |
| **20** | O(2ⁿ), O(n³) | Backtracking, triple loops |
| **100** | O(n²), O(n² log n) | Nested loops, O(n²) DP |
| **10³** | O(n² log n) | Sort + nested loop |
| **10⁴** | O(n²) | Naive DP, two nested loops |
| **10⁵** | O(n log n) | Sorting, segment trees |
| **10⁶** | O(n log n) | Efficient sorting, heaps |
| **10⁷** | O(n) | Linear algorithms, hash maps |
| **10⁸** | O(n), O(log n) | Must be very efficient |
| **10⁹+** | O(log n), O(1) | Binary search, math formulas |

### Choose by Problem Constraint

| Constraint | Likely Pattern | Time Complexity |
|------------|---------------|-----------------|
| "Find pair/triplet summing to X" | Hash map or two pointers | O(n) or O(n²) |
| "Maximum/minimum subarray" | Sliding window or DP | O(n) |
| "Search in sorted array" | Binary search | O(log n) |
| "All possible combinations" | Backtracking | O(2ⁿ) |
| "Shortest path" | BFS or Dijkstra | O(V+E) or O((V+E)log V) |
| "Optimal with subproblems" | Dynamic programming | O(n) to O(n²) |
| "Connected components" | DFS/BFS or Union-Find | O(V+E) or O(E×α(V)) |
| "Top K elements" | Heap | O(n log k) |
| "Range queries" | Prefix sum or segment tree | O(n) build, O(1) or O(log n) query |

---

## 🔍 Space-Time Tradeoff Examples

Some algorithms offer space-time tradeoffs:

| Algorithm | Space-Efficient | Time-Efficient | Tradeoff |
|-----------|----------------|----------------|----------|
| **Fibonacci** | O(1) space, O(n) time | O(n) space, O(1) lookup | Memoization vs iteration |
| **LCS** | O(min(m,n)) space | O(m×n) space for path | Track solution vs just length |
| **DFS** | O(h) space (height) | O(V) space for visited | Recursion vs explicit stack |
| **Knapsack** | O(capacity) space | O(n×capacity) for items | Rolling array vs 2D DP |
| **Dijkstra** | O(V) simple array | O(V+E) adjacency list | Dense vs sparse graph |

---

## 📚 Complexity Analysis Tips

### Analyzing Nested Loops
```python
# O(n²) - dependent loops
for i in range(n):
    for j in range(n):
        ...

# O(n×m) - independent loops
for i in range(n):
    for j in range(m):
        ...

# O(n²) - triangle pattern
for i in range(n):
    for j in range(i, n):  # Depends on i
        ...

# O(n) - fixed inner loop
for i in range(n):
    for j in range(10):  # Constant
        ...
```

### Analyzing Recursive Algorithms
```
T(n) = number_of_calls × work_per_call + combine_cost

Examples:
- Binary search: T(n) = T(n/2) + O(1) = O(log n)
- Merge sort: T(n) = 2T(n/2) + O(n) = O(n log n)
- Fibonacci (naive): T(n) = T(n-1) + T(n-2) + O(1) = O(2ⁿ)
- Fibonacci (memo): T(n) = O(n) since each state computed once
```

### Master Theorem
For recurrences of form: T(n) = aT(n/b) + f(n)

- If f(n) = O(n^c) where c < log_b(a): **T(n) = O(n^(log_b(a)))**
- If f(n) = O(n^c) where c = log_b(a): **T(n) = O(n^c log n)**
- If f(n) = O(n^c) where c > log_b(a): **T(n) = O(f(n))**

---

## 🎓 Interview Tips

1. **Always analyze:** State time and space complexity after solving
2. **Optimize iteratively:** Brute force → Better → Optimal
3. **Consider space-time tradeoffs:** Sometimes O(n) space saves time
4. **Know the limits:** Match algorithm complexity to input constraints
5. **Amortized complexity:** Some operations average out (e.g., dynamic array resize)

---

**Use this chart during practice and interviews!** 📊
