# 🎯 Quick Reference Card

Print or save this for quick pattern identification during interviews!

## Pattern Recognition

| **When you see...** | **Think...** | **Implementation** |
|---------------------|-------------|-------------------|
| "Find pair that sums to X" | Hash Map | `two_sum` |
| "Count frequency" | Hash Map | `Counter(arr)` |
| "Sorted array + two elements" | Two Pointers | `left/right pointers` |
| "Longest substring without..." | Sliding Window | `window dict + left/right` |
| "Search in sorted/rotated" | Binary Search | `left/right/mid` |
| "All subsets/permutations" | DFS/Backtracking | `recursive with path` |
| "Shortest path" | BFS | `queue + visited set` |
| "Optimal substructure" | Dynamic Programming | `dp array` |
| "Connected components" | Union-Find | `parent/rank arrays` |
| "Top K elements" | Heap | `heapq` with size k |

---

## Time Complexity Cheat Sheet

| **Complexity** | **Name** | **Examples** | **Max N** |
|---------------|----------|--------------|-----------|
| O(1) | Constant | Hash lookup, array access | Any |
| O(log n) | Logarithmic | Binary search | 10^9 |
| O(n) | Linear | Single loop, hash map build | 10^8 |
| O(n log n) | Linearithmic | Sorting, balanced tree ops | 10^6 |
| O(n²) | Quadratic | Nested loops, naive DP | 10^4 |
| O(2ⁿ) | Exponential | Subsets, backtracking | ~20 |
| O(n!) | Factorial | Permutations | ~10 |

---

## Common Code Patterns

### Hash Map
```python
seen = {}
for i, num in enumerate(arr):
    if target - num in seen:
        return [seen[target - num], i]
    seen[num] = i
```

### Two Pointers
```python
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] + arr[right] == target:
        return [left, right]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1
```

### Sliding Window
```python
left = 0
for right in range(len(s)):
    # Add s[right] to window
    while window_invalid():
        # Remove s[left] from window
        left += 1
```

### Binary Search
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### DFS/Backtracking
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    
    for choice in choices:
        # Make choice
        path.append(choice)
        backtrack(path, remaining_choices)
        # Undo choice
        path.pop()
```

### BFS
```python
from collections import deque
queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

### Dynamic Programming
```python
# Bottom-up approach
dp = [0] * (n + 1)
dp[0] = base_case

for i in range(1, n + 1):
    dp[i] = some_function(dp[i-1], dp[i-2])
```

---

## Python Gotchas

| **Issue** | **Wrong** | **Right** |
|-----------|-----------|-----------|
| Max heap | `heapq.heappush(h, x)` | `heapq.heappush(h, -x)` |
| Integer division | `a / b` (float) | `a // b` (int) |
| Infinity | `999999` | `float('inf')` |
| Copy list | `new = old` | `new = old[:]` or `old.copy()` |
| Sort descending | `arr.sort()` | `arr.sort(reverse=True)` |

---

## Interview Checklist

### Before Coding (5 min)
- [ ] Clarify problem (inputs, outputs, constraints)
- [ ] Ask about edge cases
- [ ] Identify pattern
- [ ] Discuss brute force
- [ ] Optimize approach
- [ ] State time/space complexity

### While Coding (15 min)
- [ ] Write clean, readable code
- [ ] Use meaningful variable names
- [ ] Think out loud
- [ ] Handle edge cases
- [ ] Test with example

### After Coding (5 min)
- [ ] Walk through code
- [ ] Test edge cases
- [ ] Verify complexity
- [ ] Discuss optimizations

---

## Common Mistakes to Avoid

1. ❌ **Not asking clarifying questions**
   - Array sorted? Duplicates allowed? Empty input?

2. ❌ **Jumping to code too quickly**
   - Always discuss approach first

3. ❌ **Not considering edge cases**
   - Empty input, single element, all same values

4. ❌ **Poor variable naming**
   - `x`, `temp`, `data` vs `left_pointer`, `max_sum`, `frequency_map`

5. ❌ **Not explaining thought process**
   - Interviewer can't help if they don't know what you're thinking

6. ❌ **Giving up on optimization**
   - Brute force → Better solution (always try to optimize)

---

## Pro Tips

💡 **If stuck, try these approaches:**
1. Draw examples on paper
2. Start with brute force
3. Look for patterns/repetition
4. Consider sorting first
5. Use a hash map for O(1) lookups
6. Break into smaller subproblems

💡 **Communication matters:**
- Explain what you're doing
- Verbalize your thought process
- Ask for hints if truly stuck
- Stay calm and confident

---

## Essential Python One-Liners

```python
# Reverse string
s[::-1]

# Count occurrences
from collections import Counter; Counter(arr)

# Default dict
from collections import defaultdict; d = defaultdict(list)

# Sort by custom key
arr.sort(key=lambda x: x[1])

# Get min/max
min(arr), max(arr)

# Check if all/any
all(condition for x in arr)
any(condition for x in arr)

# List comprehension with condition
[x for x in arr if condition]

# Enumerate for index + value
for i, val in enumerate(arr):

# Zip multiple iterables
for a, b in zip(arr1, arr2):

# Create 2D array
[[0]*cols for _ in range(rows)]
```

---

**Keep this handy during practice and interviews!** 📌
