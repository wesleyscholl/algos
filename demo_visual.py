#!/usr/bin/env python3

"""
Algorithm Visualization Demos
Interactive demonstrations of common algorithms
"""

import time

def print_header(title):
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)

def visualize_bfs():
    """Visualize Breadth-First Search"""
    print_header("Breadth-First Search (BFS)")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start = 'A'
    visited = []
    queue = [start]
    
    print(f"\nStarting at node: {start}")
    print(f"Graph: {graph}")
    print("\nTraversal:")
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(f"  Visit: {node}")
            visited.append(node)
            time.sleep(0.3)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    
    print(f"\nVisited nodes: {' → '.join(visited)}")

def visualize_dfs():
    """Visualize Depth-First Search"""
    print_header("Depth-First Search (DFS)")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    visited = []
    
    def dfs(node):
        if node not in visited:
            print(f"  Visit: {node}")
            visited.append(node)
            time.sleep(0.3)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
    
    print(f"\nGraph: {graph}")
    print("\nTraversal:")
    dfs('A')
    print(f"\nVisited nodes: {' → '.join(visited)}")

def visualize_binary_search():
    """Visualize Binary Search"""
    print_header("Binary Search")
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11
    
    print(f"\nArray: {arr}")
    print(f"Target: {target}\n")
    
    left, right = 0, len(arr) - 1
    steps = 0
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        print(f"Step {steps}:")
        print(f"  Range: [{left}, {right}]")
        print(f"  Middle index: {mid}, value: {arr[mid]}")
        
        if arr[mid] == target:
            print(f"  ✅ Found {target} at index {mid}!")
            break
        elif arr[mid] < target:
            print(f"  {arr[mid]} < {target}, search right half")
            left = mid + 1
        else:
            print(f"  {arr[mid]} > {target}, search left half")
            right = mid - 1
        
        time.sleep(0.5)
    
    print(f"\nTotal steps: {steps}")

def visualize_bubble_sort():
    """Visualize Bubble Sort"""
    print_header("Bubble Sort")
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal: {arr}\n")
    
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Swap {arr[j+1]} and {arr[j]}: {arr}")
        if not swapped:
            break
        time.sleep(0.3)
    
    print(f"\nSorted: {arr}")

def main():
    print("\n" + "=" * 50)
    print("  Algorithm Visualization Demos")
    print("=" * 50)
    
    visualize_bfs()
    time.sleep(1)
    
    visualize_dfs()
    time.sleep(1)
    
    visualize_binary_search()
    time.sleep(1)
    
    visualize_bubble_sort()
    
    print("\n" + "=" * 50)
    print("  More Algorithms Available:")
    print("=" * 50)
    print("""
    • Dijkstra's Algorithm (shortest path)
    • Dynamic Programming (fibonacci, knapsack)
    • Merge Sort & Quick Sort
    • Graph algorithms (topological sort, etc)
    • Tree traversals (preorder, inorder, postorder)
    """)
    
    print("=" * 50)
    print("  Repository: github.com/wesleyscholl/algos")
    print("  Coverage: 95% | Tests: Comprehensive suite")
    print("=" * 50)
    print()

if __name__ == "__main__":
    main()
