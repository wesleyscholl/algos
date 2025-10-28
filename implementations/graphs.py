"""
Graph Algorithms Pattern Implementations

Pattern: DFS, BFS, topological sort, union-find, shortest paths
Time: O(V + E)
Space: O(V)
"""

from typing import List, Dict, Set
from collections import deque, defaultdict
import heapq


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns True if union performed."""
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
    def connected(self, x: int, y: int) -> bool:
        """Check if two nodes are connected."""
        return self.find(x) == self.find(y)


def has_cycle_directed(n: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in directed graph using DFS.
    
    Time: O(V + E), Space: O(V)
    
    Example:
        >>> has_cycle_directed(4, [[0,1], [1,2], [2,0], [2,3]])
        True
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(node):
        if color[node] == GRAY:
            return True  # Back edge found
        if color[node] == BLACK:
            return False
        
        color[node] = GRAY
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        color[node] = BLACK
        return False
    
    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    
    return False


def has_cycle_undirected(n: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in undirected graph using Union-Find.
    
    Time: O(E * α(n)), Space: O(V)
    
    Example:
        >>> has_cycle_undirected(4, [[0,1], [1,2], [2,3], [3,0]])
        True
    """
    uf = UnionFind(n)
    
    for u, v in edges:
        if not uf.union(u, v):
            return True  # Already connected, cycle exists
    
    return False


def count_connected_components(n: int, edges: List[List[int]]) -> int:
    """
    Count connected components in undirected graph.
    
    Time: O(E * α(n)), Space: O(V)
    
    Example:
        >>> count_connected_components(5, [[0,1], [1,2], [3,4]])
        2
    """
    uf = UnionFind(n)
    
    for u, v in edges:
        uf.union(u, v)
    
    return len(set(uf.find(i) for i in range(n)))


def topological_sort(n: int, edges: List[List[int]]) -> List[int]:
    """
    Topological sort using Kahn's algorithm (BFS).
    
    Time: O(V + E), Space: O(V)
    
    Example:
        >>> topological_sort(4, [[0,1], [0,2], [1,3], [2,3]])
        [0, 1, 2, 3]  # or [0, 2, 1, 3]
    """
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []


def can_finish_courses(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Check if can finish all courses (detect cycle in dependency graph).
    
    Time: O(V + E), Space: O(V)
    
    Example:
        >>> can_finish_courses(2, [[1,0]])
        True
        >>> can_finish_courses(2, [[1,0], [0,1]])
        False
    """
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == num_courses


def dijkstra(n: int, edges: List[List[int]], start: int) -> List[int]:
    """
    Dijkstra's shortest path algorithm.
    edges = [[u, v, weight], ...]
    
    Time: O((V + E) log V), Space: O(V + E)
    
    Example:
        >>> dijkstra(3, [[0,1,4], [0,2,1], [2,1,2]], 0)
        [0, 3, 1]
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)
    
    while heap:
        d, u = heapq.heappop(heap)
        
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    return dist


def bellman_ford(n: int, edges: List[List[int]], start: int) -> List[int]:
    """
    Bellman-Ford algorithm (handles negative weights).
    edges = [[u, v, weight], ...]
    
    Time: O(V * E), Space: O(V)
    
    Example:
        >>> bellman_ford(3, [[0,1,4], [0,2,1], [2,1,2]], 0)
        [0, 3, 1]
    """
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Relax edges V-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return []  # Negative cycle detected
    
    return dist


def clone_graph(node):
    """
    Clone an undirected graph using DFS.
    
    Time: O(V + E), Space: O(V)
    """
    if not node:
        return None
    
    clones = {}
    
    def dfs(n):
        if n in clones:
            return clones[n]
        
        clone = Node(n.val)
        clones[n] = clone
        
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)


def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if graph is bipartite (2-colorable).
    
    Time: O(V + E), Space: O(V)
    
    Example:
        >>> is_bipartite([[1,3], [0,2], [1,3], [0,2]])
        True
    """
    n = len(graph)
    color = [-1] * n
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                return False
    
    return True


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    Find time for signal to reach all nodes (Dijkstra variant).
    times = [[u, v, time], ...]
    
    Time: O((V + E) log V), Space: O(V + E)
    
    Example:
        >>> network_delay_time([[2,1,1], [2,3,1], [3,4,1]], 4, 2)
        2
    """
    graph = defaultdict(list)
    for u, v, t in times:
        graph[u].append((v, t))
    
    dist = {k: 0}
    heap = [(0, k)]
    
    while heap:
        time, node = heapq.heappop(heap)
        
        if time > dist.get(node, float('inf')):
            continue
        
        for neighbor, t in graph[node]:
            new_time = time + t
            if new_time < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))
    
    return max(dist.values()) if len(dist) == n else -1
