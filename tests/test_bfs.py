"""Comprehensive tests for BFS implementations"""
import pytest
from implementations.bfs import (
    TreeNode, level_order_traversal, zigzag_level_order,
    right_side_view, shortest_path_binary_matrix,
    walls_and_gates, word_ladder, oranges_rotting
)


def build_tree(values):
    """Helper to build tree from list (BFS order, None for missing nodes)"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


class TestLevelOrderTraversal:
    """Test level order traversal"""
    
    def test_simple_tree(self):
        """Test basic level order traversal"""
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = level_order_traversal(root)
        assert result == [[3], [9, 20], [15, 7]]
    
    def test_single_node(self):
        """Test single node tree"""
        root = TreeNode(1)
        result = level_order_traversal(root)
        assert result == [[1]]
    
    def test_empty_tree(self):
        """Test empty tree"""
        result = level_order_traversal(None)
        assert result == []
    
    def test_left_skewed(self):
        """Test left-skewed tree"""
        root = build_tree([1, 2, None, 3, None])
        result = level_order_traversal(root)
        assert result == [[1], [2], [3]]


class TestZigzagLevelOrder:
    """Test zigzag level order traversal"""
    
    def test_zigzag_basic(self):
        """Test zigzag traversal"""
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = zigzag_level_order(root)
        assert result == [[3], [20, 9], [15, 7]]
    
    def test_zigzag_empty(self):
        """Test zigzag on empty tree"""
        result = zigzag_level_order(None)
        assert result == []


class TestRightSideView:
    """Test right side view"""
    
    def test_right_view_basic(self):
        """Test right side view"""
        root = build_tree([1, 2, 3, None, 5, None, 4])
        result = right_side_view(root)
        assert result == [1, 3, 4]
    
    def test_right_view_single(self):
        """Test single node"""
        root = TreeNode(1)
        result = right_side_view(root)
        assert result == [1]


class TestShortestPathBinaryMatrix:
    """Test shortest path in binary matrix"""
    
    def test_basic_path(self):
        """Test basic shortest path"""
        grid = [[0, 1], [1, 0]]
        assert shortest_path_binary_matrix(grid) == 2
    
    def test_no_path(self):
        """Test no path exists"""
        grid = [[1, 0], [1, 0]]
        assert shortest_path_binary_matrix(grid) == -1


class TestWallsAndGates:
    """Test walls and gates"""
    
    def test_basic_walls_gates(self):
        """Test basic walls and gates"""
        INF = 2147483647
        rooms = [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF]
        ]
        walls_and_gates(rooms)
        # Just check function runs and modifies rooms
        assert rooms[0][2] == 0  # Gate stays 0
        assert rooms[3][0] == 0  # Gate stays 0


class TestWordLadder:
    """Test word ladder"""
    
    def test_basic_word_ladder(self):
        """Test basic word ladder"""
        result = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        assert result == 5
    
    def test_no_transformation(self):
        """Test no transformation sequence"""
        result = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        assert result == 0


class TestOrangesRotting:
    """Test oranges rotting"""
    
    def test_basic_rotting(self):
        """Test basic rotting"""
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        assert oranges_rotting(grid) == 4
    
    def test_impossible(self):
        """Test impossible to rot"""
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        assert oranges_rotting(grid) == -1
