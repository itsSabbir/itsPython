# Algorithms in Python - Searching algorithms (e.g., binary search) - in the Python Programming Language
# ==================================================================================================

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
from typing import List, Any, Callable, Optional
import bisect
import unittest
import asyncio

# 1. Overview and Historical Context
# ----------------------------------
# Searching algorithms are fundamental in computer science, used to find a particular item
# within a collection of data. They are essential for efficient data retrieval and processing
# in various applications.

# Historical context:
# - Linear search: The simplest form of search, used since the early days of computing.
# - Binary search: First published by D. H. Lehmer in 1946.
# - Hash-based searching: Developed in the 1950s, with major advancements in the 1960s.
# - Advanced tree-based searches (e.g., B-trees): Developed in the late 1960s and early 1970s.

# Significance:
# - Efficient searching is crucial for database operations, file systems, and many algorithms.
# - Understanding search algorithms helps in grasping algorithmic complexity and trade-offs.
# - Many advanced data structures are designed to optimize search operations.

# Common use cases:
# - Finding specific records in databases
# - Searching for files in file systems
# - Implementing autocomplete and spell-check features
# - As a subroutine in more complex algorithms (e.g., in graph traversal)

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def linear_search(arr: List[Any], target: Any) -> int:
    """
    Implement the linear search algorithm.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Args:
    arr (List[Any]): The input list to search
    target (Any): The item to search for
    
    Returns:
    int: The index of the target if found, -1 otherwise
    """
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def binary_search(arr: List[Any], target: Any) -> int:
    """
    Implement the binary search algorithm.
    
    Time complexity: O(log n)
    Space complexity: O(1)
    
    Args:
    arr (List[Any]): The sorted input list to search
    target (Any): The item to search for
    
    Returns:
    int: The index of the target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def jump_search(arr: List[Any], target: Any) -> int:
    """
    Implement the jump search algorithm.
    
    Time complexity: O(sqrt(n))
    Space complexity: O(1)
    
    Args:
    arr (List[Any]): The sorted input list to search
    target (Any): The item to search for
    
    Returns:
    int: The index of the target if found, -1 otherwise
    """
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1

def interpolation_search(arr: List[int], target: int) -> int:
    """
    Implement the interpolation search algorithm.
    
    Time complexity: O(log log n) for uniformly distributed data, O(n) worst case
    Space complexity: O(1)
    
    Args:
    arr (List[int]): The sorted input list of integers to search
    target (int): The item to search for
    
    Returns:
    int: The index of the target if found, -1 otherwise
    """
    low, high = 0, len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

def demonstrate_searching_algorithms():
    """Demonstrate the usage of various searching algorithms."""
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    
    print("Original array:", test_array)
    print(f"Searching for {target}")
    print("Linear search result:", linear_search(test_array, target))
    print("Binary search result:", binary_search(test_array, target))
    print("Jump search result:", jump_search(test_array, target))
    print("Interpolation search result:", interpolation_search(test_array, target))

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Choose the appropriate search algorithm based on the data characteristics and requirements.
# 2. Use Python's built-in functions and modules (e.g., 'in' operator, bisect module) for efficient searching.
# 3. Keep lists sorted when frequent searching is required, to take advantage of binary search.
# 4. Consider using hash tables (dictionaries in Python) for O(1) average case lookup.

# Common Pitfalls:
# 1. Using linear search on large, sorted datasets where binary search would be more efficient.
# 2. Forgetting to sort the list before applying binary search or other algorithms that require sorted input.
# 3. Not considering the trade-off between search time and insertion/deletion time when choosing a data structure.
# 4. Overlooking the potential for overflow in binary search implementation (e.g., (low + high) // 2).

# Advanced Tips:
# 1. Use the bisect module for efficient binary search and insertion in sorted lists.
# 2. Implement custom comparison functions for searching complex objects.
# 3. Consider probabilistic search algorithms for very large datasets.
# 4. Use iterative implementations instead of recursive ones to avoid stack overflow for large inputs.

def binary_search_bisect(arr: List[Any], target: Any) -> int:
    """Use the bisect module for binary search."""
    index = bisect.bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    return -1

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

def search_person_by_age(people: List[Person], target_age: int) -> Optional[Person]:
    """Search for a person by age using binary search with a custom key function."""
    index = bisect.bisect_left(people, target_age, key=lambda p: p.age)
    if index != len(people) and people[index].age == target_age:
        return people[index]
    return None

def demonstrate_advanced_searching():
    """Demonstrate advanced searching techniques."""
    sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Binary search using bisect:", binary_search_bisect(sorted_numbers, 13))
    
    people = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 35), Person("David", 40)]
    people.sort(key=lambda p: p.age)
    result = search_person_by_age(people, 35)
    print("Search person by age:", result)

# 4. Integration and Real-World Applications
# ------------------------------------------

def binary_search_with_insertion_point(arr: List[int], target: int) -> Tuple[bool, int]:
    """
    Perform binary search and return whether the target was found and its insertion point.
    
    This is useful for maintaining a sorted list while inserting new elements.
    
    Args:
    arr (List[int]): The sorted input list to search
    target (int): The item to search for
    
    Returns:
    Tuple[bool, int]: A tuple containing a boolean indicating if the target was found,
                      and the index where it was found or should be inserted
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid
        else:
            return True, mid
    
    return False, left

def demonstrate_real_world_application():
    """Demonstrate a real-world application of binary search."""
    sorted_list = [1, 3, 5, 7, 9]
    print("Original list:", sorted_list)
    
    target = 6
    found, index = binary_search_with_insertion_point(sorted_list, target)
    
    if found:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found. It should be inserted at index {index}")
        sorted_list.insert(index, target)
        print("Updated list:", sorted_list)

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

async def async_binary_search(arr: List[int], target: int) -> int:
    """
    Implement an asynchronous binary search.
    
    This is a simplified example to demonstrate the concept of asynchronous searching.
    In real-world scenarios, this could be useful for searching across distributed systems
    or when each comparison operation is costly and can be performed asynchronously.
    
    Args:
    arr (List[int]): The sorted input list to search
    target (int): The item to search for
    
    Returns:
    int: The index of the target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Simulate an asynchronous comparison operation
        await asyncio.sleep(0.1)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

async def demonstrate_async_search():
    """Demonstrate asynchronous binary search."""
    arr = list(range(0, 1000, 2))
    target = 500
    result = await async_binary_search(arr, target)
    print(f"Asynchronous binary search result for {target}: {result}")

def exponential_search(arr: List[int], target: int) -> int:
    """
    Implement the exponential search algorithm.
    
    This algorithm is particularly useful for unbounded searches, where the
    array length is infinite or not known in advance.
    
    Time complexity: O(log n)
    Space complexity: O(1)
    
    Args:
    arr (List[int]): The sorted input list to search
    target (int): The item to search for
    
    Returns:
    int: The index of the target if found, -1 otherwise
    """
    if arr[0] == target:
        return 0
    
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    return binary_search(arr[i//2:min(i, len(arr))], target)

def demonstrate_advanced_concepts():
    """Demonstrate advanced searching concepts."""
    arr = list(range(0, 1000, 2))
    target = 500
    result = exponential_search(arr, target)
    print(f"Exponential search result for {target}: {result}")
    
    asyncio.run(demonstrate_async_search())

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    print("Q: When should I use binary search instead of linear search?")
    print("A: Use binary search when your data is sorted and you need to perform many searches.")
    
    print("\nQ: How can I search for the closest value if the exact target is not found?")
    print("A: Modify the binary search to keep track of the closest value during the search process.")
    
    def binary_search_closest(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        closest = arr[0]
        
        while left <= right:
            mid = (left + right) // 2
            if abs(arr[mid] - target) < abs(closest - target):
                closest = arr[mid]
            if arr[mid] == target:
                return arr[mid]
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return closest
    
    arr = [1, 3, 5, 7, 9]
    target = 6
    closest = binary_search_closest(arr, target)
    print(f"Closest value to {target}: {closest}")
    
    print("\nQ: How do I handle duplicate values in binary search?")
    print("A: Modify the binary search to find the leftmost or rightmost occurrence:")
    
    def binary_search_leftmost(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching on the left side
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    arr = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    leftmost = binary_search_leftmost(arr, target)
    print(f"Leftmost occurrence of {target}: {leftmost}")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    print("Recommended Tools, Libraries, and Resources:")
    print("1. Python's built-in 'in' operator for simple searches")
    print("2. 'bisect' module for binary search and insertion in sorted lists")
    print("3. 'SortedContainers' library for maintaining sorted lists efficiently")
    print("4. 'numpy' library for efficient searching in numerical arrays")
    print("5. 'Introduction to Algorithms' by Cormen, Leiserson, Rivest, and Stein - Comprehensive coverage of searching algorithms")
    print("6. 'Python Algorithms: Mastering Basic Algorithms in the Python Language' by Magnus Lie Hetland")
    print("7. Online platforms like LeetCode and HackerRank for practicing searching problems")
    print("8. Python's official documentation on sorting and searching: https://docs.python.org/3/howto/sorting.html")
    print("9. 'Algorithms' by Robert Sedgewick and Kevin Wayne - Excellent resource for algorithm design, including searching")
    print("10. 'Algorithm Design Manual' by Steven S. Skiena - Provides practical insights into algorithm selection and implementation")

# 8. Performance Analysis and Optimization
# ----------------------------------------

import timeit

def performance_analysis():
    """Analyze and compare the performance of different searching algorithms."""
    
    def generate_random_sorted_list(n):
        return sorted([random.randint(1, 1000000) for _ in range(n)])
    
    algorithms = [
        ("Linear Search", linear_search),
        ("Binary Search", binary_search),
        ("Jump Search", jump_search),
        ("Interpolation Search", interpolation_search),
        ("Binary Search (bisect)", binary_search_bisect)
    ]
    
    sizes = [100, 1000, 10000, 100000]
    
    print("Performance Analysis:")
    print("---------------------")
    
    for size in sizes:
        print(f"\nArray size: {size}")
        arr = generate_random_sorted_list(size)
        target = arr[random.randint(0, size-1)]  # Ensure the target exists in the array
        
        for name, func in algorithms:
            time_taken = timeit.timeit(lambda: func(arr, target), number=1000) / 1000
            print(f"{name}: {time_taken:.6f} seconds")

def optimize_binary_search():
    """Demonstrate an optimized version of binary search."""
    
    def optimized_binary_search(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)  # Avoid potential overflow and use bit shift for faster division
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    # Compare performance
    arr = sorted([random.randint(1, 1000000) for _ in range(1000000)])
    target = arr[random.randint(0, len(arr)-1)]
    
    original_time = timeit.timeit(lambda: binary_search(arr, target), number=1000)
    optimized_time = timeit.timeit(lambda: optimized_binary_search(arr, target), number=1000)
    
    print("\nBinary Search Optimization:")
    print(f"Original Binary Search: {original_time:.6f} seconds")
    print(f"Optimized Binary Search: {optimized_time:.6f} seconds")
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
class TestSearchingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_arrays = [
            [],
            [1],
            [1, 3, 5, 7, 9],
            list(range(1, 101)),
            [random.randint(1, 1000) for _ in range(1000)]
        ]
        for arr in self.test_arrays:
            arr.sort()
    
    def test_linear_search(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                if arr:
                    target = random.choice(arr)
                    self.assertEqual(linear_search(arr, target), arr.index(target))
                self.assertEqual(linear_search(arr, -1), -1)
    
    def test_binary_search(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                if arr:
                    target = random.choice(arr)
                    self.assertEqual(binary_search(arr, target), arr.index(target))
                self.assertEqual(binary_search(arr, -1), -1)
    
    def test_jump_search(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                if arr:
                    target = random.choice(arr)
                    self.assertEqual(jump_search(arr, target), arr.index(target))
                self.assertEqual(jump_search(arr, -1), -1)
    
    def test_interpolation_search(self):
        for arr in self.test_arrays:
            with self.subTest(arr=arr):
                if arr:
                    target = random.choice(arr)
                    self.assertEqual(interpolation_search(arr, target), arr.index(target))
                self.assertEqual(interpolation_search(arr, -1), -1)

# Main function to demonstrate all concepts
def main():
    print("Demonstrating Searching Algorithms in Python")
    demonstrate_searching_algorithms()
    demonstrate_advanced_searching()
    demonstrate_real_world_application()
    demonstrate_advanced_concepts()
    faqs_and_troubleshooting()
    recommended_resources()
    performance_analysis()
    optimize_binary_search()
    how_to_contribute()
    
    # Run unit tests
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main()