# Algorithms in Python - Sorting algorithms (e.g., merge sort, quicksort) - in the Python Programming Language
# =======================================================================================================

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
import random
from typing import List, Callable, Any
import unittest
import asyncio

# 1. Overview and Historical Context
# ----------------------------------
# Sorting algorithms are fundamental in computer science, used to rearrange elements of a list
# in a specific order (usually ascending or descending). They are essential for optimizing search 
# operations and data processing in various applications.

# Historical context:
# - Bubble sort: One of the simplest sorting algorithms, developed in the 1950s.
# - Merge sort: Invented by John von Neumann in 1945.
# - Quicksort: Developed by Tony Hoare in 1959 and published in 1961.
# - Python's built-in sort: Uses Timsort, an algorithm developed by Tim Peters in 2002.

# Significance:
# - Sorting is a fundamental operation in many algorithms and applications.
# - Understanding sorting algorithms helps in grasping algorithmic complexity and trade-offs.
# - Efficient sorting can significantly improve the performance of data processing tasks.

# Common use cases:
# - Organizing data for efficient searching and retrieval
# - Preparing data for presentation or further processing
# - As a sub-routine in more complex algorithms (e.g., in database operations)

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Implement the bubble sort algorithm.
    
    Time complexity: O(n^2)
    Space complexity: O(1)
    
    Args:
    arr (List[int]): The input list to be sorted
    
    Returns:
    List[int]: The sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr: List[int]) -> List[int]:
    """
    Implement the merge sort algorithm.
    
    Time complexity: O(n log n)
    Space complexity: O(n)
    
    Args:
    arr (List[int]): The input list to be sorted
    
    Returns:
    List[int]: The sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function for merge sort to merge two sorted lists."""
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quicksort(arr: List[int]) -> List[int]:
    """
    Implement the quicksort algorithm.
    
    Time complexity: O(n log n) average case, O(n^2) worst case
    Space complexity: O(log n) average case, O(n) worst case
    
    Args:
    arr (List[int]): The input list to be sorted
    
    Returns:
    List[int]: The sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

def timsort(arr: List[int]) -> List[int]:
    """
    Use Python's built-in sorting algorithm (Timsort).
    
    Time complexity: O(n log n)
    Space complexity: O(n)
    
    Args:
    arr (List[int]): The input list to be sorted
    
    Returns:
    List[int]: The sorted list
    """
    return sorted(arr)

def demonstrate_sorting_algorithms():
    """Demonstrate the usage of various sorting algorithms."""
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", test_array)
    print("Bubble sort:", bubble_sort(test_array.copy()))
    print("Merge sort:", merge_sort(test_array.copy()))
    print("Quicksort:", quicksort(test_array.copy()))
    print("Timsort (Python's built-in sort):", timsort(test_array.copy()))

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Choose the appropriate sorting algorithm based on the data characteristics and requirements.
# 2. Use Python's built-in sort() or sorted() for general-purpose sorting tasks.
# 3. Implement custom sorting algorithms only when necessary (e.g., for learning or specific optimizations).
# 4. Consider stability requirements when choosing a sorting algorithm.

# Common Pitfalls:
# 1. Using bubble sort for large datasets (inefficient for n > 1000).
# 2. Ignoring the space complexity of recursive algorithms like quicksort.
# 3. Not considering the stability of sorting algorithms when it matters.
# 4. Overcomplicating implementations of well-known algorithms.

# Advanced Tips:
# 1. Use key functions for custom sorting criteria.
# 2. Implement hybrid algorithms for better performance in specific scenarios.
# 3. Consider parallel sorting algorithms for very large datasets.
# 4. Use sorting networks for small, fixed-size inputs.

def custom_sort_example():
    """Demonstrate custom sorting using key functions."""
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    # Sort by length
    print("Sorted by length:", sorted(words, key=len))
    
    # Sort by last letter
    print("Sorted by last letter:", sorted(words, key=lambda x: x[-1]))
    
    # Sort by number of vowels
    def count_vowels(word):
        return sum(1 for char in word if char in 'aeiou')
    
    print("Sorted by number of vowels:", sorted(words, key=count_vowels))

def hybrid_quicksort(arr: List[int], threshold: int = 10) -> List[int]:
    """
    Implement a hybrid quicksort algorithm that switches to insertion sort for small subarrays.
    
    Args:
    arr (List[int]): The input list to be sorted
    threshold (int): The size threshold for switching to insertion sort
    
    Returns:
    List[int]: The sorted list
    """
    def _quicksort(start, end):
        if end - start + 1 <= threshold:
            # Use insertion sort for small subarrays
            for i in range(start + 1, end + 1):
                key = arr[i]
                j = i - 1
                while j >= start and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
        else:
            # Use quicksort for larger subarrays
            pivot = arr[(start + end) // 2]
            i, j = start, end
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            if start < j:
                _quicksort(start, j)
            if i < end:
                _quicksort(i, end)
    
    _quicksort(0, len(arr) - 1)
    return arr

def demonstrate_advanced_sorting():
    """Demonstrate advanced sorting techniques."""
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    print("Hybrid quicksort:", hybrid_quicksort(test_array.copy()))
    
    custom_sort_example()

# 4. Integration and Real-World Applications
# ------------------------------------------

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

def sort_people_example():
    """Demonstrate sorting of custom objects."""
    people = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35),
        Person("David", 28)
    ]
    
    # Sort by age
    people_sorted_by_age = sorted(people, key=lambda x: x.age)
    print("People sorted by age:", people_sorted_by_age)
    
    # Sort by name
    people_sorted_by_name = sorted(people, key=lambda x: x.name)
    print("People sorted by name:", people_sorted_by_name)

def parallel_merge_sort(arr: List[int]) -> List[int]:
    """
    Implement a parallel merge sort algorithm using asyncio.
    
    This is a simplified example and may not provide performance benefits
    for small arrays due to the overhead of creating tasks.
    
    Args:
    arr (List[int]): The input list to be sorted
    
    Returns:
    List[int]: The sorted list
    """
    async def merge_sort_async(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursively sort the two halves in parallel
        left_task = asyncio.create_task(merge_sort_async(left))
        right_task = asyncio.create_task(merge_sort_async(right))
        
        left_sorted, right_sorted = await asyncio.gather(left_task, right_task)
        
        return merge(left_sorted, right_sorted)
    
    return asyncio.run(merge_sort_async(arr))

def demonstrate_real_world_applications():
    """Demonstrate real-world applications of sorting algorithms."""
    sort_people_example()
    
    large_array = [random.randint(1, 1000) for _ in range(10000)]
    print("Parallel merge sort (first 10 elements):", parallel_merge_sort(large_array)[:10])

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def external_sort(input_file: str, output_file: str, chunk_size: int = 1000) -> None:
    """
    Implement an external sorting algorithm for large files that don't fit in memory.
    
    This is a simplified example that demonstrates the concept.
    
    Args:
    input_file (str): Path to the input file
    output_file (str): Path to the output file
    chunk_size (int): Number of items to process in memory at once
    """
    def read_chunk(file, size):
        return [int(file.readline().strip()) for _ in range(size) if file.readline()]
    
    def write_chunk(file, chunk):
        for item in chunk:
            file.write(f"{item}\n")
    
    # Step 1: Divide the file into sorted chunks
    chunks = []
    with open(input_file, 'r') as f:
        while True:
            chunk = read_chunk(f, chunk_size)
            if not chunk:
                break
            chunk.sort()
            temp_file = f"temp_{len(chunks)}.txt"
            with open(temp_file, 'w') as temp:
                write_chunk(temp, chunk)
            chunks.append(temp_file)
    
    # Step 2: Merge the sorted chunks
    with open(output_file, 'w') as out:
        chunk_iters = [open(chunk, 'r') for chunk in chunks]
        chunk_items = [iter(map(int, f)) for f in chunk_iters]
        current_items = [next(it, None) for it in chunk_items]
        
        while any(item is not None for item in current_items):
            min_item = min((item for item in current_items if item is not None), default=None)
            min_index = current_items.index(min_item)
            
            out.write(f"{min_item}\n")
            
            current_items[min_index] = next(chunk_items[min_index], None)
    
    # Clean up temporary files
    for chunk in chunks:
        os.remove(chunk)

def demonstrate_advanced_concepts():
    """Demonstrate advanced sorting concepts."""
    # Generate a large file for external sorting
    with open("large_file.txt", "w") as f:
        for _ in range(10000):
            f.write(f"{random.randint(1, 1000000)}\n")
    
    external_sort("large_file.txt", "sorted_large_file.txt")
    
    print("External sort completed. Check 'sorted_large_file.txt' for results.")

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    print("Q: When should I use quicksort vs. merge sort?")
    print("A: Quicksort is generally faster in practice and uses less memory, but merge sort is stable and guaranteed O(n log n) time.")
    
    print("\nQ: How can I sort a list of dictionaries by a specific key?")
    print("A: Use the 'key' parameter in sorted() or list.sort():")
    
    data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    sorted_data = sorted(data, key=lambda x: x["age"])
    print(f"Sorted data: {sorted_data}")
    
    print("\nQ: How do I implement a custom comparison for sorting?")
    print("A: Define a custom class with __lt__ method or use functools.cmp_to_key:")
    
    from functools import cmp_to_key
    
    def compare(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
    print(f"Custom sorted numbers: {sorted_numbers}")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    print("Recommended Tools, Libraries, and Resources:")
    print("1. Python's built-in 'sorted()' function and list.sort() method")
    print("2. NumPy library for efficient sorting of numerical arrays: numpy.sort()")
    print("3. Pandas library for sorting DataFrames: DataFrame.sort_values()")
    print("4. 'operator' module for efficient attribute and item getters in custom sort keys")
    print("5. 'heapq' module for heap queue algorithm, useful for partially sorting large datasets")
    print("6. 'Introduction to Algorithms' by Cormen, Leiserson, Rivest, and Stein - Comprehensive coverage of sorting algorithms")
    print("7. 'Python Algorithms: Mastering Basic Algorithms in the Python Language' by Magnus Lie Hetland")
    print("8. Online platforms like LeetCode and HackerRank for practicing sorting problems")
    print("9. Python's official documentation on sorting: https://docs.python.org/3/howto/sorting.html")
    print("10. 'The Algorithm Design Manual' by Steven S. Skiena - Excellent resource for algorithm design, including sorting")

# 8. Performance Analysis and Optimization
# ----------------------------------------

import timeit

def performance_analysis():
    """Analyze and compare the performance of different sorting algorithms."""
    
    def generate_random_list(n):
        return [random.randint(1, 1000) for _ in range(n)]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quicksort", quicksort),
        ("Timsort (Python's built-in)", timsort),
        ("Hybrid Quicksort", hybrid_quicksort)
    ]
    
    sizes = [100, 1000, 10000]
    
    print("Performance Analysis:")
    print("---------------------")
    
    for size in sizes:
        print(f"\nArray size: {size}")
        test_array = generate_random_list(size)
        
        for name, func in algorithms:
            time_taken = timeit.timeit(lambda: func(test_array.copy()), number=10) / 10
            print(f"{name}: {time_taken:.6f} seconds")

def optimize_quicksort():
    """Demonstrate an optimized version of quicksort with various improvements."""
    
    def optimized_quicksort(arr: List[int]) -> List[int]:
        def partition(low: int, high: int) -> int:
            # Choose a better pivot: median of three
            mid = (low + high) // 2
            pivot = sorted([arr[low], arr[mid], arr[high]])[1]
            
            while True:
                while arr[low] < pivot:
                    low += 1
                while arr[high] > pivot:
                    high -= 1
                if low >= high:
                    return high
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        
        def _quicksort(low: int, high: int):
            if high - low < 16:
                # Use insertion sort for small subarrays
                for i in range(low + 1, high + 1):
                    key = arr[i]
                    j = i - 1
                    while j >= low and arr[j] > key:
                        arr[j + 1] = arr[j]
                        j -= 1
                    arr[j + 1] = key
            elif low < high:
                p = partition(low, high)
                _quicksort(low, p)
                _quicksort(p + 1, high)
        
        _quicksort(0, len(arr) - 1)
        return arr
    
    # Compare performance
    test_array = [random.randint(1, 1000) for _ in range(10000)]
    
    original_time = timeit.timeit(lambda: quicksort(test_array.copy()), number=10)
    optimized_time = timeit.timeit(lambda: optimized_quicksort(test_array.copy()), number=10)
    
    print("\nQuicksort Optimization:")
    print(f"Original Quicksort: {original_time:.6f} seconds")
    print(f"Optimized Quicksort: {optimized_time:.6f} seconds")
    print(f"Speedup: {original_time / optimized_time:.2f}x")

# 9. How to Contribute
# --------------------

def how_to_contribute():
    print("How to Contribute to this Note Sheet:")
    print("1. Fork the repository containing this file.")
    print("2. Make your changes or additions.")
    print("3. Ensure all code examples are correct and follow the established style.")
    print("4. Add comments explaining new concepts or functions.")
    print("5. Update the Table of Contents if necessary.")
    print("6. Submit a pull request with a clear description of your changes.")
    print("\nGuidelines for contributions:")
    print("- Maintain the current format and style.")
    print("- Provide working code examples for new concepts.")
    print("- Include performance considerations for new functions.")
    print("- Add relevant references or citations for advanced topics.")

# Unit Tests
class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_arrays = [
            [],
            [1],
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
            list(range(100, 0, -1)),
            [random.randint(1, 1000) for _ in range(1000)]
        ]
    
    def test_bubble_sort(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                self.assertEqual(bubble_sort(arr.copy()), sorted(arr))
    
    def test_merge_sort(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                self.assertEqual(merge_sort(arr.copy()), sorted(arr))
    
    def test_quicksort(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                self.assertEqual(quicksort(arr.copy()), sorted(arr))
    
    def test_hybrid_quicksort(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                self.assertEqual(hybrid_quicksort(arr.copy()), sorted(arr))

# Main function to demonstrate all concepts
def main():
    print("Demonstrating Sorting Algorithms in Python")
    demonstrate_sorting_algorithms()
    demonstrate_advanced_sorting()
    demonstrate_real_world_applications()
    demonstrate_advanced_concepts()
    faqs_and_troubleshooting()
    recommended_resources()
    performance_analysis()
    optimize_quicksort()
    how_to_contribute()
    
    # Run unit tests
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main()