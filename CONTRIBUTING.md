# Contributing to Algos

Thank you for your interest in contributing! This guide will help you add new algorithms and improve existing ones.

## 📂 Project Structure

```
algos/
├── implementations/     # Algorithm implementations by pattern
│   ├── hash_map.py
│   ├── two_pointers.py
│   ├── sliding_window.py
│   ├── binary_search.py
│   ├── dfs_backtracking.py
│   ├── bfs.py
│   ├── dynamic_programming.py
│   ├── graphs.py
│   └── heaps.py
├── tests/              # Test files
│   ├── test_*.py
│   └── conftest.py
├── README.md
└── requirements.txt
```

## 🔧 Adding a New Algorithm

### 1. Choose the Right Pattern File

Place your algorithm in the appropriate pattern file:
- **Hash Map**: Fast lookups, frequency counting
- **Two Pointers**: Sorted arrays, palindromes
- **Sliding Window**: Substrings, subarrays
- **Binary Search**: Sorted data, search spaces
- **DFS/Backtracking**: All possibilities, permutations
- **BFS**: Shortest paths, level-order
- **Dynamic Programming**: Optimal substructure
- **Graphs**: Connected components, paths
- **Heaps**: Top-k, priority queues

### 2. Implementation Template

```python
def algorithm_name(params: Type) -> ReturnType:
    """
    Brief description of what the algorithm does.
    
    Time: O(?), Space: O(?)
    
    Example:
        >>> algorithm_name(input)
        expected_output
    
    Args:
        params: Description of parameters
    
    Returns:
        Description of return value
    """
    # Implementation here
    pass
```

### 3. Key Requirements

✅ **Clear Documentation**
- Docstring with description
- Time and space complexity
- At least one example in docstring
- Explain approach if non-obvious

✅ **Clean Code**
- Descriptive variable names
- Comments for complex logic
- Type hints for parameters and return
- Follow PEP 8 style guide

✅ **Add Tests**
- Create/update test file in `tests/`
- Cover edge cases
- Use pytest format
- Aim for >80% coverage

## 🧪 Testing

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test File
```bash
pytest tests/test_hash_map.py
```

### Run with Coverage
```bash
pytest --cov=implementations tests/
```

### Run Doctests
```bash
python -m doctest implementations/hash_map.py -v
```

## 📝 Code Style

- **Naming**: Use `snake_case` for functions and variables
- **Imports**: Standard library → Third-party → Local
- **Line Length**: Max 88 characters (Black formatter)
- **Type Hints**: Always use for function signatures

## 🎯 What to Contribute

### High Priority
- 🐛 Bug fixes in existing algorithms
- 🧪 More test cases and edge cases
- 📊 Visualization helpers
- 📚 Additional examples in docstrings

### New Algorithms Welcome
- Classic interview problems
- Common LeetCode patterns
- Data structure implementations
- Algorithm optimizations

### Ideas for Enhancement
- Performance benchmarking suite
- Interactive Jupyter notebooks
- Complexity analyzer tool
- Visual algorithm explanations

## 🚀 Pull Request Process

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/algos.git
   cd algos
   ```

2. **Create Branch**
   ```bash
   git checkout -b feature/algorithm-name
   ```

3. **Make Changes**
   - Add implementation
   - Add tests
   - Update documentation

4. **Run Tests**
   ```bash
   pytest tests/
   ```

5. **Commit**
   ```bash
   git add .
   git commit -m "Add [algorithm-name] implementation"
   ```

6. **Push and PR**
   ```bash
   git push origin feature/algorithm-name
   ```
   Then open a Pull Request on GitHub

## 📖 Documentation Standards

### Algorithm Complexity
Always specify both time and space complexity:
```python
Time: O(n log n), Space: O(n)
```

### Examples
Include at least one example showing input → output:
```python
Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
```

## ❓ Questions?

Open an issue with:
- Clear description
- Expected vs actual behavior
- Relevant code snippets

## 🏆 Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes for significant contributions

---

**Happy Coding!** 🎉
