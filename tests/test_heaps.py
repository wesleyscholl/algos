"""Comprehensive tests for heap implementations"""
import pytest
from implementations.heaps import (
    kth_largest_element, top_k_frequent, merge_k_sorted_lists,
    find_median_from_stream, k_closest_points, task_scheduler,
    sliding_window_maximum, last_stone_weight, reorganize_string
)


class TestKthLargestElement:
    """Test kth largest element"""
    
    def test_basic_kth_largest(self):
        """Test basic kth largest"""
        result = kth_largest_element([3, 2, 1, 5, 6, 4], 2)
        assert result == 5
    
    def test_all_same(self):
        """Test all same elements"""
        result = kth_largest_element([1, 1, 1, 1], 2)
        assert result == 1
    
    def test_single_element(self):
        """Test single element"""
        result = kth_largest_element([5], 1)
        assert result == 5


class TestTopKFrequent:
    """Test top k frequent elements"""
    
    def test_basic_frequency(self):
        """Test basic frequency"""
        result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert sorted(result) == [1, 2]
    
    def test_all_unique(self):
        """Test all unique elements"""
        result = top_k_frequent([1, 2, 3, 4], 2)
        assert len(result) == 2
    
    def test_single_element(self):
        """Test single element"""
        result = top_k_frequent([1], 1)
        assert result == [1]


class TestMergeKSortedLists:
    """Test merge k sorted lists"""
    
    def test_basic_merge(self):
        """Test basic merge"""
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        result = merge_k_sorted_lists(lists)
        assert result == [1, 1, 2, 3, 4, 4, 5, 6]
    
    def test_empty_lists(self):
        """Test empty lists"""
        result = merge_k_sorted_lists([[], [], []])
        assert result == []
    
    def test_single_list(self):
        """Test single list"""
        result = merge_k_sorted_lists([[1, 2, 3]])
        assert result == [1, 2, 3]


class TestMedianFinder:
    """Test median finder"""
    
    def test_basic_median(self):
        """Test basic median finding"""
        MedianFinder = find_median_from_stream()
        mf = MedianFinder  # It returns the class itself
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2.0
    
    def test_single_element(self):
        """Test single element"""
        MedianFinder = find_median_from_stream()
        mf = MedianFinder  # It returns the class itself
        mf.addNum(5)
        assert mf.findMedian() == 5.0


class TestKClosestPoints:
    """Test k closest points to origin"""
    
    def test_basic_closest(self):
        """Test basic closest points"""
        points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
        result = k_closest_points(points, 2)
        assert len(result) == 2
        # Check that distances are smallest (should be [0,1] and [-2,2] or [1,3])
        distances = [p[0]**2 + p[1]**2 for p in result]
        assert all(d <= 10 for d in distances)
    
    def test_single_point(self):
        """Test single point"""
        result = k_closest_points([[1, 1]], 1)
        assert result == [[1, 1]]


class TestTaskScheduler:
    """Test task scheduler"""
    
    def test_basic_schedule(self):
        """Test basic task scheduling"""
        result = task_scheduler(["A", "A", "A", "B", "B", "B"], 2)
        assert result == 8


class TestSlidingWindowMaximum:
    """Test sliding window maximum"""
    
    def test_basic_sliding(self):
        """Test basic sliding window"""
        result = sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
        assert result == [3, 3, 5, 5, 6, 7]


class TestLastStoneWeight:
    """Test last stone weight"""
    
    def test_basic_stones(self):
        """Test basic stone weight"""
        result = last_stone_weight([2, 7, 4, 1, 8, 1])
        assert result == 1


class TestReorganizeString:
    """Test reorganize string"""
    
    def test_basic_reorganize(self):
        """Test basic reorganization"""
        result = reorganize_string("aab")
        # Check no adjacent characters are same
        for i in range(len(result) - 1):
            assert result[i] != result[i + 1]
