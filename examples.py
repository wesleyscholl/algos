"""
Example usage of algorithm implementations.

Run this file to see algorithms in action:
    python examples.py
"""

from implementations.hash_map import two_sum, longest_consecutive
from implementations.two_pointers import three_sum, container_with_most_water
from implementations.sliding_window import length_of_longest_substring
from implementations.binary_search import search_rotated_array
from implementations.dfs_backtracking import subsets, generate_parentheses
from implementations.bfs import level_order_traversal, TreeNode
from implementations.dynamic_programming import coin_change, fibonacci
from implementations.graphs import UnionFind, topological_sort
from implementations.heaps import kth_largest_element, find_median_from_stream


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def main():
    print("\n🧠 Algorithm Examples\n")
    
    # Hash Map Examples
    print_section("Hash Map Pattern")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Two Sum: nums={nums}, target={target}")
    print(f"Result: indices {result} → [{nums[result[0]]}, {nums[result[1]]}]\n")
    
    sequence = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive(sequence)
    print(f"Longest Consecutive: {sequence}")
    print(f"Result: {result} (sequence: 1,2,3,4)\n")
    
    # Two Pointers Examples
    print_section("Two Pointers Pattern")
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print(f"Three Sum: {nums}")
    print(f"Result: {result}\n")
    
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = container_with_most_water(heights)
    print(f"Container With Most Water: {heights}")
    print(f"Result: {result}\n")
    
    # Sliding Window Examples
    print_section("Sliding Window Pattern")
    s = "abcabcbb"
    result = length_of_longest_substring(s)
    print(f"Longest Substring Without Repeating: '{s}'")
    print(f"Result: {result} (substring: 'abc')\n")
    
    # Binary Search Examples
    print_section("Binary Search Pattern")
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search_rotated_array(nums, target)
    print(f"Search Rotated Array: {nums}, target={target}")
    print(f"Result: index {result}\n")
    
    # DFS/Backtracking Examples
    print_section("DFS & Backtracking Pattern")
    nums = [1, 2, 3]
    result = subsets(nums)
    print(f"All Subsets: {nums}")
    print(f"Result: {result}\n")
    
    n = 3
    result = generate_parentheses(n)
    print(f"Generate Parentheses: n={n}")
    print(f"Result: {result}\n")
    
    # BFS Examples
    print_section("BFS Pattern")
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = level_order_traversal(root)
    print(f"Binary Tree Level Order:")
    print(f"       3")
    print(f"      / \\")
    print(f"     9  20")
    print(f"       /  \\")
    print(f"      15   7")
    print(f"Result: {result}\n")
    
    # Dynamic Programming Examples
    print_section("Dynamic Programming Pattern")
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    print(f"Coin Change: coins={coins}, amount={amount}")
    print(f"Result: {result} coins (5+5+1)\n")
    
    n = 10
    result = fibonacci(n)
    print(f"Fibonacci: n={n}")
    print(f"Result: {result}\n")
    
    # Graph Examples
    print_section("Graph Algorithms")
    uf = UnionFind(5)
    edges = [(0, 1), (1, 2), (3, 4)]
    for u, v in edges:
        uf.union(u, v)
    components = len(set(uf.find(i) for i in range(5)))
    print(f"Union-Find: {5} nodes, edges={edges}")
    print(f"Connected Components: {components}\n")
    
    n = 4
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    result = topological_sort(n, edges)
    print(f"Topological Sort: n={n}, edges={edges}")
    print(f"Result: {result}\n")
    
    # Heap Examples
    print_section("Heap / Priority Queue Pattern")
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = kth_largest_element(nums, k)
    print(f"Kth Largest Element: nums={nums}, k={k}")
    print(f"Result: {result}\n")
    
    mf = find_median_from_stream()
    stream = [5, 15, 1, 3]
    print(f"Median From Stream: {stream}")
    for num in stream:
        mf.addNum(num)
        print(f"  Added {num}, median: {mf.findMedian()}")
    
    print("\n" + "="*60)
    print("  ✨ All examples completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
