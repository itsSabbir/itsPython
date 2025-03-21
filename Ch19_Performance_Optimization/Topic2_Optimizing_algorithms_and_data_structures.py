# Performance Optimization - Optimizing algorithms and data structures - in the Python Programming Language
# ======================================================================================================

# Table of Contents:
# 1. Overview and Historical Context
# 2. Syntax, Key Concepts, and Code Examples
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# 4. Integration and Real-World Applications
# 5. Advanced Concepts and Emerging Trends
# 6. FAQs and Troubleshooting
# 7. Recommended Tools, Libraries, and Resources
# 8. Performance Analysis and Optimization
# 9. How to Contribute

# Author: Sabbir Hossain

import time
import sys
import cProfile
import random
from typing import List, Dict, Tuple, Any
from collections import defaultdict
from functools import lru_cache

# 1. Overview and Historical Context
# ----------------------------------
# Performance optimization in Python involves improving the efficiency of algorithms and data structures
# to reduce execution time and memory usage. This has been a focus since Python's inception in 1991.

# Key milestones:
# - 2000: Python 2.0 introduced list comprehensions, improving performance for list creation
# - 2008: Python 3.0 brought optimizations in string operations and integer arithmetic
# - 2012: Python 3.3 introduced the 'yield from' syntax, optimizing generator performance
# - 2015: Python 3.5 added type hints, allowing for potential performance improvements through static analysis
# - 2022: Python 3.11 introduced significant performance improvements, including faster startup and better error reporting

# Significance:
# - Critical for large-scale applications and data processing tasks
# - Enables Python to compete with lower-level languages in certain domains
# - Allows developers to write more efficient code without sacrificing Python's readability

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def time_execution(func):
    """Decorator to measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Example 1: Optimizing list creation
@time_execution
def create_list_append(n: int) -> List[int]:
    """Create a list using append method."""
    result = []
    for i in range(n):
        result.append(i)
    return result

@time_execution
def create_list_comprehension(n: int) -> List[int]:
    """Create a list using list comprehension."""
    return [i for i in range(n)]

# Example 2: Optimizing dictionary access
@time_execution
def dict_get_default(data: Dict[str, int], keys: List[str]) -> List[int]:
    """Access dictionary elements using get with default."""
    return [data.get(key, 0) for key in keys]

@time_execution
def dict_get_try_except(data: Dict[str, int], keys: List[str]) -> List[int]:
    """Access dictionary elements using try-except."""
    result = []
    for key in keys:
        try:
            result.append(data[key])
        except KeyError:
            result.append(0)
    return result

# Example 3: Memoization for expensive computations
def fibonacci_recursive(n: int) -> int:
    """Recursive Fibonacci implementation (inefficient)."""
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@lru_cache(maxsize=None)
def fibonacci_memoized(n: int) -> int:
    """Memoized Fibonacci implementation using lru_cache."""
    if n < 2:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

# Example 4: Generator for memory-efficient iteration
def generate_large_dataset(n: int) -> List[int]:
    """Generate a large dataset (memory-intensive)."""
    return [i * i for i in range(n)]

def generate_large_dataset_generator(n: int):
    """Generate a large dataset using a generator (memory-efficient)."""
    for i in range(n):
        yield i * i

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use appropriate data structures (e.g., sets for membership testing)
# 2. Leverage built-in functions and standard library modules
# 3. Use generators for large datasets to reduce memory usage
# 4. Profile code to identify bottlenecks before optimizing
# 5. Write clear, maintainable code first, then optimize if necessary

# Common Pitfalls:
# 1. Premature optimization
# 2. Overusing list.append() in loops instead of list comprehensions
# 3. Neglecting to use local variables in tight loops
# 4. Inappropriate use of global variables
# 5. Not considering the overhead of function calls in tight loops

# Advanced Tips:
# 1. Use `__slots__` to reduce memory usage in classes with many instances
# 2. Leverage numpy for numerical computations
# 3. Consider using Cython for performance-critical sections
# 4. Use multiprocessing for CPU-bound tasks, asyncio for I/O-bound tasks
# 5. Optimize string concatenation using join() method or f-strings

# Example: Using __slots__ to reduce memory usage
class PointWithoutSlots:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class PointWithSlots:
    __slots__ = ['x', 'y']
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# 4. Integration and Real-World Applications
# ------------------------------------------

# Real-world example: Optimizing a text processing task
def process_text(text: str) -> Dict[str, int]:
    """Process text and return word frequencies (unoptimized version)."""
    words = text.lower().split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def process_text_optimized(text: str) -> Dict[str, int]:
    """Process text and return word frequencies (optimized version)."""
    return defaultdict(int, ((word, text.lower().split().count(word)) for word in set(text.lower().split())))

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Example: Using numpy for efficient numerical computations
import numpy as np

def matrix_multiply_pure_python(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Matrix multiplication using pure Python (inefficient for large matrices)."""
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_multiply_numpy(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Matrix multiplication using numpy (efficient for large matrices)."""
    return np.dot(a, b)

# 6. FAQs and Troubleshooting
# ---------------------------

def faq_and_troubleshooting():
    """Provide answers to common questions and troubleshooting tips."""
    faqs = {
        "Q: How can I identify performance bottlenecks in my Python code?":
        "A: Use profiling tools like cProfile or line_profiler to identify which parts of your code are taking the most time.",
        
        "Q: When should I use a list vs. a generator?":
        "A: Use a generator when you're dealing with large datasets and don't need to keep all elements in memory at once.",
        
        "Q: How can I optimize database queries in Python?":
        "A: Use appropriate indexing, limit the data fetched, use bulk operations, and consider using ORM caching mechanisms.",
        
        "Q: What's the most efficient way to concatenate strings in Python?":
        "A: For a few strings, use the '+' operator or f-strings. For many strings, use the join() method.",
        
        "Q: How can I make my Python code run faster without rewriting everything in a lower-level language?":
        "A: Profile your code, use appropriate data structures, leverage built-in functions and libraries like numpy, and consider using Cython for critical sections."
    }
    
    for question, answer in faqs.items():
        print(f"{question}\n{answer}\n")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    """Provide recommended tools, libraries, and resources for performance optimization in Python."""
    resources = {
        "Tools": [
            "cProfile - Built-in profiling tool",
            "memory_profiler - For memory usage analysis",
            "line_profiler - For line-by-line profiling",
            "pyflame - For flame graph generation"
        ],
        "Libraries": [
            "numpy - For efficient numerical computations",
            "numba - For JIT compilation",
            "Cython - For C-extensions in Python",
            "multiprocessing - For parallel processing",
            "asyncio - For asynchronous I/O"
        ],
        "Resources": [
            "High Performance Python by Micha Gorelick and Ian Ozsvald",
            "Python Cookbook by David Beazley and Brian K. Jones",
            "Python Performance Tips (https://wiki.python.org/moin/PythonSpeed/PerformanceTips)",
            "Real Python's Performance Optimization Tutorials (https://realpython.com/tutorials/performance/)"
        ]
    }
    
    for category, items in resources.items():
        print(f"{category}:")
        for item in items:
            print(f"- {item}")
        print()

# 8. Performance Analysis and Optimization
# ----------------------------------------

def analyze_performance(func, *args, **kwargs):
    """Analyze the performance of a given function using cProfile."""
    cProfile.runctx('func(*args, **kwargs)', globals(), locals(), sort='cumulative')

# Example of optimizing a frequently called method
class DataProcessor:
    def __init__(self, data: List[int]):
        self.data = data
    
    def process_unoptimized(self) -> int:
        """Unoptimized method for processing data."""
        return sum(x * x for x in self.data if x % 2 == 0)
    
    def process_optimized(self) -> int:
        """Optimized method for processing data."""
        return sum(x * x for x in self.data if not x & 1)

# 9. How to Contribute
# --------------------
# (The contribution guidelines would typically be placed here, but for brevity, they are omitted in this code example.)

def main():
    """Main function to demonstrate various concepts related to performance optimization in Python."""
    
    # Demonstrating list creation optimization
    n = 1000000
    create_list_append(n)
    create_list_comprehension(n)
    
    # Demonstrating dictionary access optimization
    data = {str(i): i for i in range(1000)}
    keys = [str(i) for i in range(1500)]  # Some keys won't be in the dictionary
    dict_get_default(data, keys)
    dict_get_try_except(data, keys)
    
    # Demonstrating memoization
    n = 30
    start = time.time()
    fibonacci_recursive(n)
    print(f"Recursive Fibonacci for n={n} took {time.time() - start:.6f} seconds")
    
    start = time.time()
    fibonacci_memoized(n)
    print(f"Memoized Fibonacci for n={n} took {time.time() - start:.6f} seconds")
    
    # Demonstrating memory usage optimization
    n = 1000000
    sys.getsizeof(generate_large_dataset(n))
    sys.getsizeof(generate_large_dataset_generator(n))
    
    # Demonstrating __slots__ usage
    point_without_slots = PointWithoutSlots(1.0, 2.0)
    point_with_slots = PointWithSlots(1.0, 2.0)
    print(f"Memory usage without __slots__: {sys.getsizeof(point_without_slots)} bytes")
    print(f"Memory usage with __slots__: {sys.getsizeof(point_with_slots)} bytes")
    
    # Demonstrating text processing optimization
    text = "This is a sample text for demonstrating text processing optimization in Python"
    process_text(text)
    process_text_optimized(text)
    
    # Demonstrating numpy optimization
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    matrix_multiply_pure_python(a, b)
    matrix_multiply_numpy(np.array(a), np.array(b))
    
    # Displaying FAQs and troubleshooting tips
    faq_and_troubleshooting()
    
    # Displaying recommended resources
    recommended_resources()
    
    # Demonstrating performance analysis
    data = [random.randint(1, 100) for _ in range(1000000)]
    dp = DataProcessor(data)
    analyze_performance(dp.process_unoptimized)
    analyze_performance(dp.process_optimized)

if __name__ == "__main__":
    main()