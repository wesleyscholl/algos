# Changelog

All notable changes to the algos project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added - 2025-01-XX

#### Test Coverage Improvements (95% Coverage Achieved)
- **test_bfs.py**: Added comprehensive tests for BFS implementations
  - 15 tests covering level order traversal, zigzag order, right side view
  - Tests for shortest path in binary matrix, walls and gates, word ladder
  - Tests for oranges rotting problem
  - Coverage: 95% (141/148 lines)

- **test_dfs_backtracking.py**: Added comprehensive tests for DFS/backtracking
  - 16 tests covering subsets, permutations, combination sum
  - Tests for parentheses generation, letter combinations, word search
  - Tests for N-Queens problem
  - Coverage: 99% (110/111 lines)

- **test_two_pointers.py**: Added comprehensive tests for two-pointer pattern
  - 21 tests covering two sum, palindrome checks, three sum
  - Tests for container with most water, remove duplicates, move zeroes
  - Tests for string reversal and palindrome partitioning
  - Coverage: 96% (93/97 lines)

- **test_sliding_window.py**: Added comprehensive tests for sliding window pattern
  - 18 tests covering max sum subarray, longest substring without repeating chars
  - Tests for minimum window substring, find anagrams
  - Tests for longest repeating character replacement, max consecutive ones
  - Tests for longest substring with k distinct characters
  - Coverage: 95% (97/102 lines)

- **test_heaps.py**: Added comprehensive tests for heap/priority queue
  - 17 tests covering kth largest element, top k frequent elements
  - Tests for merging k sorted lists, median finder, k closest points
  - Tests for task scheduler, sliding window maximum, last stone weight
  - Tests for string reorganization
  - Coverage: 97% (112/115 lines)

- **test_graphs.py**: Added comprehensive tests for graph algorithms
  - 19 tests covering union-find, cycle detection (directed/undirected)
  - Tests for topological sort, connected components, graph cloning
  - Tests for Dijkstra's algorithm, Bellman-Ford, course scheduling
  - Tests for bipartite detection, network delay time
  - Coverage: 90% (149/165 lines)

#### Test Statistics
- **Total Tests**: 134 tests (106 new tests added)
- **Overall Coverage**: 95% (941/990 lines covered)
- **Test Files Added**: 6 new comprehensive test files
- **Algorithms Covered**: 50+ algorithm implementations now tested

#### Quality Improvements
- All tests passing with pytest 8.4.2
- Comprehensive edge case coverage (empty inputs, single elements, large inputs)
- Proper handling of special cases (negative numbers, duplicates, cycles)
- Clear test naming and documentation
- Organized test classes by algorithm pattern

## Previous Coverage (Before This Update)
- Only 3 test files existed (binary_search, dynamic_programming, hash_map)
- Coverage: ~30% (only 28 existing tests)
- 6 algorithm files completely untested (bfs, dfs_backtracking, two_pointers, sliding_window, heaps, graphs)

## Testing Approach
- Unit tests using pytest framework
- Mocking not required (pure algorithm implementations)
- Focus on correctness, edge cases, and boundary conditions
- Each test class organized by function/algorithm type
- Test data carefully chosen to cover common patterns and edge cases
