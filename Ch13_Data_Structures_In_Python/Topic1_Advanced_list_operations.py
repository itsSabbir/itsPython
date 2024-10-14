"""
Data Structures in Python - Advanced list operations - in the Python Programming Language
=========================================================================================

Table of Contents:
1. Overview and Historical Context
2. Syntax, Key Concepts, and Code Examples
3. Best Practices, Common Pitfalls, and Advanced Tips
4. Integration and Real-World Applications
5. Advanced Concepts and Emerging Trends
6. FAQs and Troubleshooting
7. Recommended Tools, Libraries, and Resources
8. Performance Analysis and Optimization
9. How to Contribute

Author: Sabbir Hossain

1. Overview and Historical Context
----------------------------------
Lists are one of the most versatile and commonly used data structures in Python. They are mutable, ordered sequences that can contain elements of different types. Advanced list operations go beyond basic indexing and slicing, offering powerful ways to manipulate and process data efficiently.

Historical context:
- Lists have been a core data structure in Python since its inception in 1991.
- Many advanced list operations were introduced or optimized in subsequent Python versions.
- List comprehensions were introduced in Python 2.0 (2000), significantly enhancing list manipulation capabilities.

Significance:
- Advanced list operations allow for concise and efficient data manipulation.
- They play a crucial role in data processing, algorithmic problem-solving, and functional programming in Python.
- Mastering these operations is essential for writing Pythonic and performant code.

Common use cases:
- Data transformation and filtering
- Implementing complex algorithms
- Functional programming patterns
- Efficient memory management in data-intensive applications

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import itertools
import functools
import operator
import random
import time
from typing import List, Any, Callable, Tuple

def list_comprehensions():
    """Demonstrate advanced list comprehension techniques."""
    # Basic list comprehension
    squares = [x**2 for x in range(10)]
    print("1. Squares:", squares)

    # List comprehension with conditional
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print("2. Even squares:", even_squares)

    # Nested list comprehension
    matrix = [[i+j for j in range(3)] for i in range(3)]
    print("3. Matrix:", matrix)

    # Flattening a 2D list
    flattened = [item for sublist in matrix for item in sublist]
    print("4. Flattened matrix:", flattened)

    # List comprehension with multiple conditions
    complex_list = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]
    print("5. Numbers divisible by 2 and 3:", complex_list)

def advanced_slicing():
    """Demonstrate advanced slicing techniques."""
    lst = list(range(10))
    
    # Reversing a list
    reversed_list = lst[::-1]
    print("1. Reversed list:", reversed_list)

    # Selecting every nth item
    every_third = lst[::3]
    print("2. Every third item:", every_third)

    # Negative step slicing
    negative_step = lst[8:3:-1]
    print("3. Negative step slice:", negative_step)

    # Rotating a list
    rotated = lst[3:] + lst[:3]
    print("4. Rotated list:", rotated)

def list_operations():
    """Demonstrate various list operations."""
    # Extending a list
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    lst1.extend(lst2)
    print("1. Extended list:", lst1)

    # Inserting elements
    lst1.insert(2, 10)
    print("2. List after insertion:", lst1)

    # Removing elements
    lst1.remove(10)
    print("3. List after removal:", lst1)

    # Popping elements
    popped = lst1.pop(2)
    print(f"4. Popped element: {popped}, Resulting list: {lst1}")

    # Sorting and reversing
    lst1.sort(reverse=True)
    print("5. Sorted in reverse:", lst1)
    lst1.reverse()
    print("6. Reversed again:", lst1)

def functional_operations():
    """Demonstrate functional programming operations on lists."""
    numbers = list(range(1, 11))

    # Map
    squared = list(map(lambda x: x**2, numbers))
    print("1. Squared numbers:", squared)

    # Filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("2. Even numbers:", evens)

    # Reduce
    sum_all = functools.reduce(operator.add, numbers)
    print("3. Sum of all numbers:", sum_all)

    # Zip
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    combined = list(zip(names, scores))
    print("4. Combined names and scores:", combined)

def advanced_sorting():
    """Demonstrate advanced sorting techniques."""
    # Custom sort key
    words = ["apple", "banana", "cherry", "date"]
    sorted_words = sorted(words, key=len)
    print("1. Words sorted by length:", sorted_words)

    # Sort with multiple criteria
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 25)]
    sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
    print("2. Data sorted by age then name:", sorted_data)

    # Partial sorting with heapq
    import heapq
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    top_3 = heapq.nlargest(3, numbers)
    print("3. Top 3 numbers:", top_3)

def list_as_stack_and_queue():
    """Demonstrate using list as a stack and queue."""
    # Stack operations
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("1. Stack:", stack)
    popped = stack.pop()
    print(f"   Popped: {popped}, Stack now: {stack}")

    # Queue operations (note: using lists as queues is not efficient)
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print("2. Queue:", queue)
    dequeued = queue.pop(0)  # Inefficient for large lists
    print(f"   Dequeued: {dequeued}, Queue now: {queue}")

    # Using deque for efficient queue operations
    from collections import deque
    efficient_queue = deque()
    efficient_queue.append(1)
    efficient_queue.append(2)
    efficient_queue.append(3)
    print("3. Efficient Queue:", efficient_queue)
    dequeued = efficient_queue.popleft()
    print(f"   Dequeued: {dequeued}, Queue now: {efficient_queue}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use list comprehensions for simple transformations and filtering.
2. Prefer built-in functions (map, filter, etc.) for readability and performance.
3. Use appropriate data structures (e.g., deque for queue operations).
4. Leverage the 'key' parameter in sorting functions for complex sorting logic.
5. Use slice assignments for in-place list modifications when possible.

Common Pitfalls:
1. Modifying a list while iterating over it.
2. Inefficient use of '+' operator for repeated list concatenation.
3. Using lists for constant-time lookups (use sets or dictionaries instead).
4. Overusing list comprehensions for complex operations, reducing readability.
5. Ignoring the memory implications of large list operations.

Advanced Tips:
1. Use `itertools` for memory-efficient list operations.
2. Leverage `functools.lru_cache` for memoization in recursive list operations.
3. Use `array.array` for homogeneous numeric lists to save memory.
4. Implement custom `__lt__` methods for complex object sorting.
5. Use `bisect` module for maintaining sorted lists efficiently.
"""

def demonstrate_best_practices():
    """Demonstrate best practices and advanced tips."""
    # 1. Efficient list concatenation
    pieces = ['a', 'b', 'c', 'd']
    result = ''.join(pieces)  # More efficient than '+' operator
    print("1. Efficient concatenation:", result)

    # 2. Using itertools for memory efficiency
    large_range = itertools.islice(itertools.count(), 10**6)
    first_10 = list(itertools.islice(large_range, 10))
    print("2. First 10 of a large range:", first_10)

    # 3. Memoization for recursive operations
    @functools.lru_cache(maxsize=None)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("3. 30th Fibonacci number:", fibonacci(30))

    # 4. Using bisect for efficient sorted list insertion
    import bisect
    sorted_list = [1, 3, 5, 7, 9]
    bisect.insort(sorted_list, 4)
    print("4. Efficiently inserted 4:", sorted_list)

def common_pitfalls():
    """Demonstrate common pitfalls and their solutions."""
    # 1. Modifying a list while iterating
    numbers = [1, 2, 3, 4, 5]
    # Incorrect: for num in numbers: if num % 2 == 0: numbers.remove(num)
    # Correct:
    numbers = [num for num in numbers if num % 2 != 0]
    print("1. Odd numbers:", numbers)

    # 2. Inefficient list growth
    def inefficient_growth():
        result = []
        for i in range(10000):
            result = result + [i]  # Inefficient
        return result

    def efficient_growth():
        return list(range(10000))  # Much more efficient

    # 3. Using list for constant-time lookups
    def slow_lookup(lst, item):
        return item in lst  # O(n) time complexity

    def fast_lookup(st, item):
        return item in st  # O(1) average time complexity

    large_list = list(range(10**5))
    large_set = set(large_list)
    
    start = time.time()
    slow_lookup(large_list, 99999)
    print(f"3. Slow lookup time: {time.time() - start:.6f} seconds")

    start = time.time()
    fast_lookup(large_set, 99999)
    print(f"   Fast lookup time: {time.time() - start:.6f} seconds")

"""
4. Integration and Real-World Applications
------------------------------------------
Advanced list operations are widely used in various Python applications:

1. Data Science: Pandas uses advanced list operations for data manipulation.
2. Web Development: Django uses list comprehensions in its ORM queries.
3. Game Development: PyGame uses lists for sprite management and collision detection.

Real-world example: Text Analysis Tool
"""

import re
from collections import Counter

class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.words = re.findall(r'\w+', text.lower())
        self.word_count = len(self.words)
        self.unique_words = set(self.words)
        self.word_frequencies = Counter(self.words)

    def get_most_common_words(self, n: int) -> List[Tuple[str, int]]:
        return self.word_frequencies.most_common(n)

    def get_word_density(self, word: str) -> float:
        return self.word_frequencies[word] / self.word_count

    def get_unique_word_ratio(self) -> float:
        return len(self.unique_words) / self.word_count

    def get_word_length_distribution(self) -> Dict[int, int]:
        return Counter(map(len, self.words))

def demonstrate_text_analysis():
    """Demonstrate the TextAnalyzer application."""
    sample_text = """
    Python is an interpreted, high-level, general-purpose programming language. 
    Created by Guido van Rossum and first released in 1991, Python's design 
    philosophy emphasizes code readability with its notable use of significant 
    whitespace. Its language constructs and object-oriented approach aim to 
    help programmers write clear, logical code for small and large-scale projects.
    """
    
    analyzer = TextAnalyzer(sample_text)
    
    print("1. Most common words:")
    print(analyzer.get_most_common_words(5))
    
    print("\n2. Word density of 'python':")
    print(f"{analyzer.get_word_density('python'):.2%}")
    
    print("\n3. Unique word ratio:")
    print(f"{analyzer.get_unique_word_ratio():.2%}")
    
    print("\n4. Word length distribution:")
    print(analyzer.get_word_length_distribution())

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. List operations in concurrent and parallel programming.
2. Advanced memory management techniques for large lists.
3. Integration of list operations with machine learning pipelines.
"""

import concurrent.futures
import numpy as np

def parallel_list_processing():
    """Demonstrate parallel list processing."""
    def process_chunk(chunk):
        return [x**2 for x in chunk]

    data = list(range(10**6))
    chunk_size = len(data) // 4
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(process_chunk, chunks))

    processed_data = [item for sublist in results for item in sublist]
    print("1. Parallel processing result (first 10 items):", processed_data[:10])

def memory_efficient_large_lists():
    """Demonstrate memory-efficient handling of large lists."""
    # Using numpy for memory-efficient numeric lists
    np_array = np.arange(10**6, dtype=np.int32)
    print(f"2. Numpy array size: {np_array.nbytes / (1024*1024):.2f} MB")

    # Using array module for memory-efficient homogeneous lists
    import array
    arr = array.array('i', range(10**6))
    print(f"3. Array module size: {arr.buffer_info()[1] * arr.itemsize / (1024*1024):.2f} MB")

    # Using itertools for memory-efficient operations
    large_iter = itertools.islice(itertools.count(), 10**6)
    result = sum(itertools.islice(large_iter, 10))
    print("4. Sum of first 10 items from large iterable:", result)

"""
6. FAQs and Troubleshooting
---------------------------
Q1: How can I remove duplicates from a list while preserving order?
A1: Use a dict or OrderedDict to preserve order:
    list(dict.fromkeys(my_list))

Q2: What's the most efficient way to flatten a nested list?
A2: Use a recursive function or itertools.chain:
    list(itertools.chain.from_iterable(nested_list))

Q3: How can I efficiently find the intersection of multiple lists?
A3: Use set intersection:
    set.intersection(*[set(lst) for lst in list_of_lists])

Q4: What's the best way to remove items from a list based on a condition?
A4: Use a list comprehension or the filter function:
    [x for x in lst if condition(x)] or list(filter(condition, lst))

Q5: How can I create a cumulative sum of a list?
A5: Use itertools.accumulate:
    list(itertools.accumulate(my_list))

Troubleshooting guide:
1. Issue: List index out of range error
   Solution: Always check the length of the list before indexing, or use list.get() with a default value.

2. Issue: Unexpected behavior when copying lists
   Solution: Use list.copy() or list[:] for shallow copies, and copy.deepcopy() for deep copies.

3. Issue: Memory error when working with very large lists
   Solution: Use generators or itertools for memory-efficient operations, or consider using numpy for large numeric datasets.

4. Issue: Slow performance with large lists
   Solution: Consider using appropriate data structures (e.g., sets for membership testing) or algorithms (e.g., binary search for sorted lists).

5. Issue: Lists changing unexpectedly in functions
   Solution: Be cautious with mutable default arguments in functions. Use None as a default and create the list inside the function if needed.

"""

def demonstrate_troubleshooting():
    """Demonstrate solutions to common issues with list operations."""
    
    # 1. Safely getting an item from a list
    my_list = [1, 2, 3]
    index = 5
    item = my_list[index] if index < len(my_list) else None
    print(f"1. Safe indexing: {item}")
    
    # 2. Proper list copying
    import copy
    original = [1, [2, 3], 4]
    shallow_copy = original.copy()
    deep_copy = copy.deepcopy(original)
    original[1][0] = 'X'
    print(f"2. Original: {original}, Shallow copy: {shallow_copy}, Deep copy: {deep_copy}")
    
    # 3. Memory-efficient operations on large lists
    large_range = range(10**6)
    first_10_squared = list(itertools.islice(map(lambda x: x**2, large_range), 10))
    print(f"3. First 10 squared from large range: {first_10_squared}")
    
    # 4. Efficient membership testing
    large_list = list(range(10**5))
    large_set = set(large_list)
    test_item = 99999
    
    start = time.time()
    list_result = test_item in large_list
    list_time = time.time() - start
    
    start = time.time()
    set_result = test_item in large_set
    set_time = time.time() - start
    
    print(f"4. List membership test: {list_time:.6f} seconds")
    print(f"   Set membership test: {set_time:.6f} seconds")
    
    # 5. Handling mutable default arguments
    def append_to(element, target=None):
        if target is None:
            target = []
        target.append(element)
        return target
    
    result1 = append_to(1)
    result2 = append_to(2)
    print(f"5. Append results: {result1}, {result2}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. NumPy: Efficient array operations and numerical computing
2. Pandas: Data manipulation and analysis built on top of NumPy
3. itertools: Memory-efficient iterators for efficient looping
4. functools: Higher-order functions and operations on callable objects
5. collections: Specialized container datatypes

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (chapters on data structures)
- "Fluent Python" by Luciano Ramalho (chapters on sequences)
- Python's official documentation on lists: https://docs.python.org/3/tutorial/datastructures.html
- Real Python's guide on Python lists and list comprehensions: https://realpython.com/python-lists-tuples/
- Raymond Hettinger's talks on Python's list implementation (available on YouTube)
- PEP 202 - List Comprehensions: https://www.python.org/dev/peps/pep-0202/

8. Performance Analysis and Optimization
----------------------------------------
When working with lists, especially large ones, performance considerations are crucial. Here we'll analyze and compare different list operations and provide optimization strategies.
"""

import sys

def performance_comparison():
    """Compare performance of different list operations."""
    
    # Setup
    lst = list(range(10**5))
    set_version = set(lst)
    
    # 1. List vs Set membership testing
    def list_membership():
        return 99999 in lst
    
    def set_membership():
        return 99999 in set_version
    
    list_time = timeit.timeit(list_membership, number=1000)
    set_time = timeit.timeit(set_membership, number=1000)
    
    print(f"1. Membership test - List: {list_time:.6f}s, Set: {set_time:.6f}s")
    
    # 2. List comprehension vs map
    def list_comp():
        return [x**2 for x in range(1000)]
    
    def map_version():
        return list(map(lambda x: x**2, range(1000)))
    
    list_comp_time = timeit.timeit(list_comp, number=1000)
    map_time = timeit.timeit(map_version, number=1000)
    
    print(f"2. Square numbers - List comp: {list_comp_time:.6f}s, Map: {map_time:.6f}s")
    
    # 3. Concatenation vs extend
    def concat():
        result = []
        for i in range(100):
            result = result + [i]
        return result
    
    def extend():
        result = []
        for i in range(100):
            result.extend([i])
        return result
    
    concat_time = timeit.timeit(concat, number=1000)
    extend_time = timeit.timeit(extend, number=1000)
    
    print(f"3. List growth - Concatenation: {concat_time:.6f}s, Extend: {extend_time:.6f}s")

def memory_usage_analysis():
    """Analyze memory usage of different list representations."""
    
    # Regular list
    regular_list = list(range(10**5))
    regular_size = sys.getsizeof(regular_list) + sum(sys.getsizeof(item) for item in regular_list)
    
    # NumPy array
    np_array = np.arange(10**5)
    np_size = np_array.nbytes
    
    # Range object
    range_obj = range(10**5)
    range_size = sys.getsizeof(range_obj)
    
    print(f"Memory usage:")
    print(f"1. Regular list: {regular_size / 1024:.2f} KB")
    print(f"2. NumPy array: {np_size / 1024:.2f} KB")
    print(f"3. Range object: {range_size / 1024:.2f} KB")

"""
Optimization Strategies:
1. Use appropriate data structures: Sets for unique elements and fast membership testing, dictionaries for key-value pairs.
2. Leverage built-in functions and methods: They are often implemented in C and highly optimized.
3. Use list comprehensions for simple loops: They are generally faster than explicit for loops.
4. Avoid growing lists by concatenation: Use list.append() or list.extend() instead.
5. Use generators for large sequences when you don't need the entire sequence in memory at once.
6. Consider using NumPy for large numerical computations.
7. Use the 'key' parameter in sorting functions instead of creating temporary lists.

Example of optimizing a frequently called method:
"""

def optimize_frequent_operation(numbers: List[int]) -> List[int]:
    """
    Optimize the operation of filtering even numbers and squaring them.
    
    Args:
    numbers (List[int]): Input list of integers
    
    Returns:
    List[int]: List of squared even numbers
    """
    # Unoptimized version
    # return [x**2 for x in numbers if x % 2 == 0]
    
    # Optimized version
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

def demonstrate_optimization():
    """Demonstrate optimization of a frequently called list operation."""
    numbers = list(range(10**5))
    
    def unoptimized():
        return [x**2 for x in numbers if x % 2 == 0]
    
    def optimized():
        return optimize_frequent_operation(numbers)
    
    unopt_time = timeit.timeit(unoptimized, number=100)
    opt_time = timeit.timeit(optimized, number=100)
    
    print("List operation optimization:")
    print(f"1. Unoptimized: {unopt_time:.6f} seconds")
    print(f"2. Optimized: {opt_time:.6f} seconds")
    print(f"Speedup: {unopt_time / opt_time:.2f}x")

"""
9. How to Contribute
--------------------
To contribute to this note sheet:
1. Fork the repository containing this file.
2. Make your changes or additions.
3. Ensure all code examples are correct and follow the established style.
4. Add comments explaining new concepts or functions.
5. Update the Table of Contents if necessary.
6. Submit a pull request with a clear description of your changes.

Guidelines for contributions:
- Maintain the current format and style.
- Provide working code examples for new concepts.
- Include performance considerations for new functions.
- Add relevant references or citations for advanced topics.

When adding new sections or expanding existing ones, consider the following:
- Relevance to the main topic of advanced list operations in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to advanced list operations.
    """
    print("1. List Comprehensions:")
    list_comprehensions()
    
    print("\n2. Advanced Slicing:")
    advanced_slicing()
    
    print("\n3. List Operations:")
    list_operations()
    
    print("\n4. Functional Operations:")
    functional_operations()
    
    print("\n5. Advanced Sorting:")
    advanced_sorting()
    
    print("\n6. List as Stack and Queue:")
    list_as_stack_and_queue()
    
    print("\n7. Best Practices and Advanced Tips:")
    demonstrate_best_practices()
    
    print("\n8. Common Pitfalls:")
    common_pitfalls()
    
    print("\n9. Real-World Application - Text Analysis:")
    demonstrate_text_analysis()
    
    print("\n10. Advanced Concepts:")
    parallel_list_processing()
    memory_efficient_large_lists()
    
    print("\n11. Troubleshooting:")
    demonstrate_troubleshooting()
    
    print("\n12. Performance Comparison:")
    performance_comparison()
    
    print("\n13. Memory Usage Analysis:")
    memory_usage_analysis()
    
    print("\n14. Optimization Demonstration:")
    demonstrate_optimization()

if __name__ == "__main__":
    main()