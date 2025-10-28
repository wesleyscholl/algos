"""
BFS (Breadth-First Search) Pattern Implementations

Pattern: Level-by-level traversal using queue
Time: O(V + E)
Space: O(V)
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    """Binary tree node definition."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Binary tree level order traversal.
    
    Time: O(n), Space: O(n)
    
    Example:
        Tree:    3
               /   \\
              9    20
                  /  \\
                15    7
        Result: [[3], [9,20], [15,7]]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    View tree from right side (rightmost node at each level).
    
    Time: O(n), Space: O(n)
    
    Example:
        Tree:    1
               /   \\
              2     3
               \\     \\
                5     4
        Result: [1, 3, 4]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Last node in this level
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Zigzag level order traversal (alternate left-to-right and right-to-left).
    
    Time: O(n), Space: O(n)
    
    Example:
        Tree:    3
               /   \\
              9    20
                  /  \\
                15    7
        Result: [[3], [20,9], [15,7]]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(list(level))
        left_to_right = not left_to_right
    
    return result


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    Find shortest path from top-left to bottom-right in binary matrix.
    Can move in 8 directions. 0 = clear, 1 = blocked.
    
    Time: O(n²), Space: O(n²)
    
    Example:
        >>> shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]])
        4
    """
    if not grid or grid[0][0] == 1:
        return -1
    
    n = len(grid)
    if n == 1:
        return 1
    
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # Mark as visited
    
    while queue:
        row, col, dist = queue.popleft()
        
        if row == n - 1 and col == n - 1:
            return dist
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0):
                queue.append((new_row, new_col, dist + 1))
                grid[new_row][new_col] = 1  # Mark as visited
    
    return -1


def walls_and_gates(rooms: List[List[int]]) -> None:
    """
    Fill rooms with distance to nearest gate.
    -1 = wall, 0 = gate, INF = empty room
    
    Time: O(m*n), Space: O(m*n)
    
    Example:
        Input:  INF  -1   0  INF
                INF  INF INF  -1
                INF  -1  INF  -1
                  0  -1  INF  INF
        
        Output:   3  -1   0   1
                  2   2   1  -1
                  1  -1   2  -1
                  0  -1   3   4
    """
    if not rooms:
        return
    
    m, n = len(rooms), len(rooms[0])
    INF = 2147483647
    queue = deque()
    
    # Find all gates and add to queue
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        row, col = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < m and 0 <= new_col < n and 
                rooms[new_row][new_col] == INF):
                rooms[new_row][new_col] = rooms[row][col] + 1
                queue.append((new_row, new_col))


def word_ladder(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Find shortest transformation sequence from begin_word to end_word.
    
    Time: O(M² * N) where M = word length, N = word list size
    Space: O(M * N)
    
    Example:
        >>> word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        5  # hit -> hot -> dot -> dog -> cog
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        # Try all possible one-letter changes
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    
    return 0


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Find time for all oranges to rot. 0=empty, 1=fresh, 2=rotten.
    Rotten oranges spread to adjacent fresh oranges each minute.
    
    Time: O(m*n), Space: O(m*n)
    
    Example:
        >>> oranges_rotting([[2,1,1],[1,1,0],[0,1,1]])
        4
    """
    if not grid:
        return -1
    
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    # Count fresh oranges and find rotten ones
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0
    
    while queue:
        row, col, time = queue.popleft()
        max_time = max(max_time, time)
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < m and 0 <= new_col < n and 
                grid[new_row][new_col] == 1):
                grid[new_row][new_col] = 2
                fresh -= 1
                queue.append((new_row, new_col, time + 1))
    
    return max_time if fresh == 0 else -1
