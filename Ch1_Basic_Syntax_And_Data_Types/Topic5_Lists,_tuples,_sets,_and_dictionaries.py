"""
Expert-Level Cheat Sheet: Basic Syntax and Data Types - Lists, tuples, sets, and dictionaries - in the Python Programming Language

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

This cheat sheet serves as a comprehensive guide to lists, tuples, sets, and dictionaries in Python,
covering basic concepts to advanced techniques. It's designed for developers of all levels,
from beginners to senior/principal developers.

Author: Sabbir
Date: September 18, 2024
Python Version: 3.11+
"""

# Imports
import sys  # Provides access to system-specific parameters and functions
import timeit  # Used to measure execution time of code snippets, useful for performance profiling
import collections  # Contains specialized container datatypes such as namedtuples, defaultdict, deque, etc.
import itertools  # Offers a suite of fast, memory-efficient tools for iterating over data
from typing import List, Tuple, Set, Dict, Any  # Provides type hinting to enhance code readability and maintainability
import unittest  # Supports testing of individual units of source code, essential for ensuring code reliability

# ========================================
# 1. Overview and Historical Context
"""
Lists, tuples, sets, and dictionaries are fundamental data structures in Python, essential for
organizing and manipulating data efficiently.

Historical Context:
- Lists and dictionaries have been part of Python since its inception in 1991.
- Tuples were introduced in Python 1.4 (1996).
- Sets were added as a built-in type in Python 2.4 (2004).
- Dictionaries became ordered by default in Python 3.7 (2018).

In modern software development, these data structures are crucial for:
- Data organization and retrieval
- Algorithm implementation
- Configuration management
- Database operations
- API design and implementation

Compared to other languages:
- Python's list is similar to ArrayList in Java or vector in C++.
- Tuples are similar to structs in C or readonly lists in C#.
- Sets are comparable to HashSet in Java or std::unordered_set in C++.
- Dictionaries are similar to HashMap in Java or std::unordered_map in C++.
"""
# ========================================

# Detailed explanations of each data structure with examples, insights, and advanced tips:

# ========================================
# Lists
# ========================================
# Lists are dynamic arrays that can hold heterogeneous elements and are ordered, mutable, and indexed.
# Common operations include append, remove, pop, sort, and slicing.

my_list: List[Any] = [10, "Hello", 3.14, True]

# Explanation of above initialization:
# - Lists are defined using square brackets [] and can hold elements of mixed data types.
# - `Any` is used from the typing module to indicate that elements can be of any data type.
# - Lists maintain insertion order and allow duplicate elements.

# Advanced Tip: Lists have O(1) complexity for append and pop operations at the end but O(n) complexity for insertions
# and deletions in the middle. Therefore, avoid excessive insertions/deletions in the middle for performance-critical code.

my_list.append(42)  # Adds 42 to the end of the list. Efficient due to O(1) complexity.
my_list.remove("Hello")  # Removes the first occurrence of "Hello". O(n) complexity because it must search through the list.

# Potential Pitfall: Be cautious with `remove()`. If the element doesn't exist, it raises a ValueError. 
# Use try-except or check if the element exists using `if element in my_list` before removing.

# ========================================
# Tuples
# ========================================
# Tuples are immutable sequences typically used for fixed collections of items. They are defined using parentheses ().
my_tuple: Tuple[int, str, float, bool] = (10, "Hello", 3.14, True)

# Explanation:
# - Tuples are immutable, meaning elements cannot be modified, added, or removed after creation.
# - Ideal for fixed data structures, such as coordinates (x, y), database rows, or function return values with multiple items.

# Advanced Tip: Because tuples are immutable, they are hashable and can be used as keys in dictionaries or elements in sets,
# unlike lists. Additionally, tuples generally have a smaller memory footprint and faster access times compared to lists.

# Potential Pitfall: Attempting to modify a tuple, e.g., `my_tuple[0] = 99`, will raise a TypeError. 
# Make sure to choose tuples over lists when immutability is desired or required.

# ========================================
# Sets
# ========================================
# Sets are unordered collections of unique elements. They support operations like union, intersection, and difference.
my_set: Set[int] = {1, 2, 3, 4, 5}

# Explanation:
# - Defined using curly braces {} (similar to dictionaries, but without key-value pairs).
# - Automatically eliminates duplicate values, making them ideal for deduplication tasks.

my_set.add(6)  # Adds element 6. O(1) average time complexity.
my_set.remove(3)  # Removes element 3. Raises KeyError if the element is not found.

# Best Practice: Use `discard()` instead of `remove()` if there's a possibility that the element might not be present. 
# `discard()` doesn't raise an error if the element is absent.

# Advanced Tip: Set operations (union `|`, intersection `&`, difference `-`) are highly efficient in Python and typically 
# outperform equivalent list operations. When dealing with large data collections where uniqueness matters, prefer sets over lists.

# ========================================
# Dictionaries
# ========================================
# Dictionaries are unordered, mutable mappings of key-value pairs and allow for quick retrieval based on keys.
my_dict: Dict[str, Any] = {"name": "Alice", "age": 30, "is_student": False}

# Explanation:
# - Keys are unique, immutable, and typically strings, integers, or tuples.
# - Values can be any data type and are mutable.
# - Access time for retrieving a value by key is O(1) on average, making dictionaries extremely efficient for lookups.

my_dict["email"] = "alice@example.com"  # Adds a new key-value pair to the dictionary.

# Advanced Tip: Since Python 3.7, dictionaries maintain insertion order by default. Although this is not a guarantee by the 
# language specification, it's implemented this way in CPython (Python's reference implementation). Use `collections.OrderedDict` 
# if order preservation is explicitly required in older Python versions.

# Potential Pitfall: Accessing a non-existent key (e.g., `my_dict["address"]`) raises a KeyError. Use `dict.get()` 
# to safely retrieve values without risking an error, e.g., `my_dict.get("address", "N/A")`.

# ========================================
# Collections Module Insights
# ========================================
# The `collections` module provides alternatives to the standard data structures with specialized use cases.
# - `defaultdict`: Like a regular dictionary but provides a default value for non-existent keys, avoiding KeyError.
# - `namedtuple`: Enables creation of tuple-like objects with named fields, improving code readability.
# - `deque`: A double-ended queue that supports O(1) appends and pops from both ends, more efficient than lists for such operations.

# Example usage of defaultdict
from collections import defaultdict
my_defaultdict = defaultdict(int)  # int() returns 0 by default

my_defaultdict['missing_key'] += 1  # Instead of raising a KeyError, the missing key is created with a default value of 0.

# ========================================
# Best Practices Summary:
# - Choose lists for ordered, mutable sequences and tuples for fixed, immutable sequences.
# - Use sets for collections where uniqueness matters and for performing mathematical set operations efficiently.
# - Opt for dictionaries for key-value mappings and leverage `collections.defaultdict` or `OrderedDict` for enhanced functionality.
# ========================================


# ========================================
# 2. Syntax, Key Concepts, and Code Examples
# ---------------------------------

# Function to demonstrate fundamental and advanced list operations
def list_basics():
    """Demonstrates basic and advanced concepts related to lists in Python."""

    # ---------------------------
    # List Creation
    # ---------------------------
    # Lists are mutable, ordered collections that allow duplicate elements and can store items of varying data types.
    fruits = ['apple', 'banana', 'cherry']  # Standard list initialization with string elements
    numbers = list(range(1, 6))  # Using `list()` to convert a range object into a list: [1, 2, 3, 4, 5]

    # Note: The `range()` function generates a sequence of numbers but doesn't create a list by default in Python 3.x,
    # hence the use of `list()` for conversion.

    # ---------------------------
    # Accessing Elements
    # ---------------------------
    # Lists are zero-indexed, meaning the first element has an index of 0.
    print(f"First fruit: {fruits[0]}")  # Accessing the first element; O(1) time complexity
    print(f"Last number: {numbers[-1]}")  # Using negative indexing to access the last element; convenient and efficient

    # Advanced Tip: Negative indexing is particularly useful when dealing with dynamically changing lists or unknown sizes.

    # ---------------------------
    # Slicing
    # ---------------------------
    # Slicing allows for accessing a subset of the list by specifying a start, stop, and optional step value.
    print(f"First two fruits: {fruits[:2]}")  # Retrieves elements from index 0 to 1 (stop is exclusive)
    print(f"Every other number: {numbers[::2]}")  # Retrieves every second element; `::2` sets the step size to 2

    # Insight: Slicing creates a shallow copy of the list, meaning it refers to the same elements in memory, 
    # but changes to the slice won't affect the original list's structure.

    # ---------------------------
    # Modifying Lists
    # ---------------------------
    # Lists are mutable, allowing elements to be modified, added, or removed.

    # Adding elements
    fruits.append('date')  # `append` adds an element to the end; efficient with O(1) time complexity on average
    fruits.insert(1, 'blueberry')  # `insert` adds an element at a specific index; can be slower (O(n)) due to shifting
    fruits.extend(['elderberry', 'fig'])  # `extend` adds multiple elements from an iterable; more efficient than repeated `append`

    # Insight: `append` modifies the original list in place, whereas concatenating (e.g., `fruits + ['fig']`) creates a new list.

    # Removing elements
    fruits.remove('banana')  # Removes the first occurrence of 'banana'; O(n) complexity since it may require shifting elements
    popped_fruit = fruits.pop()  # Removes and returns the last element; O(1) time complexity for this operation

    print(f"Modified fruits: {fruits}")
    print(f"Popped fruit: {popped_fruit}")

    # Potential Pitfall: Using `remove()` with an element not present in the list raises a ValueError.
    # It is often safer to check if the element exists using `if 'banana' in fruits:` before attempting removal.

    # ---------------------------
    # List Comprehension
    # ---------------------------
    # A concise way to create lists using an expression followed by a `for` loop, optionally including an `if` condition.
    squared_numbers = [x**2 for x in range(1, 6)]  # Creates a list of squares: [1, 4, 9, 16, 25]

    # Insight: List comprehensions are not only more readable but also faster than traditional loops due to optimizations at the C level.
    print(f"Squared numbers: {squared_numbers}")

# Function to demonstrate fundamental and advanced tuple operations
def tuple_basics():
    """Demonstrates basic and advanced concepts related to tuples in Python."""

    # ---------------------------
    # Tuple Creation
    # ---------------------------
    # Tuples are immutable, ordered collections often used for fixed data structures or when immutability is desired.
    coordinates = (3, 4)  # Tuple with two integers
    person = ('Alice', 30, 'Engineer')  # Tuple with mixed data types (str, int, str)
    single_element_tuple = (42,)  # A single-element tuple requires a trailing comma; otherwise, it's treated as an expression

    # Potential Pitfall: Forgetting the comma when defining a single-element tuple results in a different data type:
    # `single_element_tuple = (42)` would be treated as an integer.

    # ---------------------------
    # Accessing Elements
    # ---------------------------
    # Similar to lists, tuples are zero-indexed.
    print(f"X coordinate: {coordinates[0]}")
    print(f"Person's name: {person[0]}")

    # ---------------------------
    # Tuple Unpacking
    # ---------------------------
    # Tuple unpacking allows multiple variables to be assigned values simultaneously based on tuple elements.
    name, age, occupation = person  # Each variable corresponds to an element in the tuple
    print(f"{name} is {age} years old and works as an {occupation}")

    # Advanced Tip: Unpacking is efficient and can be used to swap variables in Python without a temporary variable:
    # `a, b = b, a` swaps the values of `a` and `b`.

    # ---------------------------
    # Tuples are Immutable
    # ---------------------------
    # Immutability means elements cannot be changed after tuple creation.
    try:
        coordinates[0] = 5  # Attempting to modify a tuple raises a TypeError
    except TypeError as e:
        print(f"Error: {e}")

    # Insight: Immutability makes tuples safer for concurrent applications and as keys in dictionaries (since hashability is required).

    # ---------------------------
    # Named Tuples
    # ---------------------------
    # Named tuples offer a way to create lightweight, immutable objects with named fields, enhancing code readability.
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])  # Defining a named tuple 'Point' with fields 'x' and 'y'
    p = Point(5, 10)  # Creating an instance of 'Point'

    print(f"Point: x={p.x}, y={p.y}")

    # Advanced Tip: Named tuples retain immutability but provide more intuitive access (e.g., `p.x` instead of `p[0]`).
    # They can be converted to dictionaries using `p._asdict()` for interoperability with other data structures.

    # Insight: Named tuples are more memory-efficient than objects created via classes due to their simpler underlying structure.


def set_basics():
    """Demonstrates basic concepts related to sets in Python."""

    # Set creation: Using curly braces `{}` to define a set with unique elements
    # Sets are unordered collections of unique elements, meaning they automatically remove duplicates.
    # They do not support indexing, slicing, or ordered traversal.
    fruits = {'apple', 'banana', 'cherry'}  # Example of a set with string elements
    
    # Alternative set creation using the `set()` function.
    # Demonstrates how duplicates are automatically removed.
    numbers = set([1, 2, 2, 3, 3, 4])  # Duplicate '2' and '3' are eliminated
    # Note: Although you can pass any iterable (list, tuple, etc.) to `set()`, passing non-iterables will cause an error.

    # Adding elements to the set: The `add()` method inserts an element into the set if it's not already present.
    fruits.add('date')  # Adds 'date' to the set
    # Important: Sets being unordered means there's no guarantee on the position of this new element within the set.

    # Removing elements from the set using `remove()`:
    fruits.remove('banana')  # Removes 'banana' from the set
    # If the specified element does not exist in the set, `remove()` raises a `KeyError`.
    # To avoid potential errors, consider using `discard()` instead, as demonstrated below.

    # Using `discard()` to remove elements:
    fruits.discard('elderberry')  # Safely attempts to remove 'elderberry', which isn't present
    # `discard()` does not raise an error if the element is absent, making it safer for uncertain removals.

    # Set Operations: Demonstrating basic set operations using `set1` and `set2`
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    # Union (all unique elements from both sets)
    print(f"Union: {set1 | set2}")  # Equivalent to `set1.union(set2)`
    
    # Intersection (common elements between both sets)
    print(f"Intersection: {set1 & set2}")  # Equivalent to `set1.intersection(set2)`
    
    # Difference (elements in `set1` but not in `set2`)
    print(f"Difference: {set1 - set2}")  # Equivalent to `set1.difference(set2)`
    
    # Symmetric difference (elements in either set, but not both)
    print(f"Symmetric difference: {set1 ^ set2}")  # Equivalent to `set1.symmetric_difference(set2)`

    # Set comprehension: An advanced, concise way to create sets using conditions and expressions
    # `even_squares` contains squares of even numbers from 0 to 9
    even_squares = {x**2 for x in range(10) if x % 2 == 0}
    print(f"Even squares: {even_squares}")
    # Advanced Insight: Set comprehensions are highly efficient for filtering and transforming data while maintaining uniqueness.

def dict_basics():
    """Demonstrates basic concepts related to dictionaries in Python."""
    
    # Dictionary creation: Key-value pairs enclosed in curly braces `{}` or using the `dict()` constructor
    person = {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}  # Using literals
    scores = dict(alice=95, bob=87, charlie=92)  # Using `dict()` with keyword arguments
    
    # Accessing and modifying elements
    print(f"Name: {person['name']}")  # Access value using its key
    person['age'] = 31  # Modifies the existing key-value pair for 'age'
    person['city'] = 'New York'  # Adds a new key-value pair
    
    # Dictionary methods
    # `keys()`, `values()`, and `items()` return views of the dictionary's keys, values, and key-value pairs respectively.
    print(f"Keys: {person.keys()}")  # Outputs: dict_keys(['name', 'age', 'occupation', 'city'])
    print(f"Values: {person.values()}")  # Outputs all values
    print(f"Items: {person.items()}")  # Outputs all key-value pairs
    
    # Using `get()` method with a default value:
    # Prevents `KeyError` if the key doesn't exist; returns 'Not specified' instead.
    salary = person.get('salary', 'Not specified')
    print(f"Salary: {salary}")
    
    # Dictionary comprehension: An advanced way to construct dictionaries dynamically
    squared_numbers = {x: x**2 for x in range(1, 6)}  # Constructs a dictionary with numbers and their squares
    print(f"Squared numbers: {squared_numbers}")

def advanced_operations():
    """Demonstrates advanced operations on lists, tuples, sets, and dictionaries."""
    
    # List sorting and custom sort: Sorting a list using `sort()`
    fruits = ['banana', 'apple', 'cherry', 'date']
    fruits.sort()  # Sorts the list in ascending order by default
    print(f"Sorted fruits: {fruits}")
    
    # Sorting based on a custom criterion: Using the `key` argument
    fruits.sort(key=len, reverse=True)  # Sorts by string length in descending order
    print(f"Fruits sorted by length (descending): {fruits}")
    
    # Using tuples as dictionary keys: Tuples are immutable, making them suitable as dictionary keys
    coordinates = {(0, 0): 'origin', (1, 0): 'unit x', (0, 1): 'unit y'}
    print(f"Value at origin: {coordinates[(0, 0)]}")
    
    # Set operations using set methods
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Is set1 a subset of set2? {set1.issubset(set2)}")  # Checks if all elements of `set1` are in `set2`
    print(f"Do set1 and set2 have any elements in common? {set1.isdisjoint(set2)}")  # Returns True if no common elements
    
    # Merging dictionaries in Python 3.9+: The `|` operator provides a straightforward way to merge dictionaries.
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = dict1 | dict2  # `dict2` values overwrite `dict1` values for duplicate keys ('b' in this case)
    print(f"Merged dictionary: {merged_dict}")

    # Advanced Insight: Before Python 3.9, merging dictionaries required methods like `update()`, 
    # which directly modified the original dictionary, or using dictionary unpacking (`**dict1, **dict2`) 
    # to create a new merged dictionary. The `|` operator offers a more elegant and readable approach.


# ============================================================
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# ============================================================

def best_practices():
    """Demonstrates best practices for working with lists, tuples, sets, and dictionaries."""
    
    # Use list comprehensions for simple transformations
    numbers = [1, 2, 3, 4, 5]
    squared = [x**2 for x in numbers]  # Prefer this over map() for readability in most cases
    # List comprehensions are generally more readable and Pythonic than map() or manual loops.
    # They also have better performance due to their implementation in C.

    # Advanced Tip: Prefer list comprehensions when you don't need lazy evaluation. If working with very large datasets,
    # consider using generator expressions instead to save memory.
    
    # Use generator expressions for large datasets to save memory
    sum_of_squares = sum(x**2 for x in range(1000000))
    # Generator expressions are memory efficient as they yield items one at a time rather than creating the entire list in memory.
    # This is particularly advantageous for operations on large datasets, preventing high memory consumption.
    
    # Use tuple unpacking for multiple assignments
    a, b = 1, 2  # Simultaneously assign values to a and b in one line
    a, b = b, a  # Swapping values without needing a temporary variable
    # This is more concise and Pythonic than using a temporary variable. It also showcases Python's elegant handling of tuples.

    # Use sets for membership testing when you have many items
    large_set = set(range(1000000))
    print(f"Is 500000 in the set? {500000 in large_set}")  # O(1) complexity for membership testing
    # Sets offer average O(1) time complexity for lookups, making them ideal for large datasets where frequent membership testing is required.
    # In contrast, using a list would be O(n), which is inefficient for large collections.

    # Use dict.get() with a default value instead of checking if a key exists
    config = {'debug': True}
    verbose = config.get('verbose', False)  # Avoids KeyError and simplifies the code
    # This is more concise and avoids the need for an explicit if-else check: if 'verbose' in config: verbose = config['verbose'].
    
    # Use collections.defaultdict for handling missing keys
    from collections import defaultdict
    word_counts = defaultdict(int)  # Initializes a new int (defaulting to 0) when a key doesn't exist
    for word in ['apple', 'banana', 'apple', 'cherry']:
        word_counts[word] += 1
    print(f"Word counts: {dict(word_counts)}")
    # defaultdict saves the need for manually initializing keys, reducing boilerplate code.
    # Advanced Tip: You can customize defaultdict with other callable objects, e.g., `defaultdict(list)` or `defaultdict(set)`.

def common_pitfalls():
    """Highlights common pitfalls when working with lists, tuples, sets, and dictionaries."""

    # Mutable default arguments
    def append_to(element, lst=[]):  # Dangerous! The default argument `lst` is mutable.
        lst.append(element)
        return lst
    
    print(append_to(1))  # Output: [1]
    print(append_to(2))  # Output: [1, 2], not [2]
    # Explanation: Default arguments are evaluated once at function definition, not each time the function is called.
    # Thus, the list persists between calls, leading to unintended side effects.

    # Proper way to handle mutable default arguments:
    def append_to_safe(element, lst=None):
        if lst is None:  # Initialize a new list if `lst` is not provided
            lst = []
        lst.append(element)
        return lst
    # Best Practice: Always use `None` as the default value for mutable arguments to avoid shared state between function calls.

    # Modifying a list while iterating over it
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)  # This can skip elements and cause unexpected behavior
    print(f"Attempted to remove even numbers: {numbers}")
    # Pitfall: Modifying a list while iterating over it can lead to skipped elements because the list indices change dynamically.

    # Proper way: Create a new list using list comprehension
    numbers = [1, 2, 3, 4, 5]
    numbers = [num for num in numbers if num % 2 != 0]
    print(f"Correctly removed even numbers: {numbers}")
    # List comprehensions are not only more concise but also avoid the risks of modifying a list in place.

    # Using a list when a set would be more appropriate
    def unique_numbers(numbers):
        unique = []
        for num in numbers:
            if num not in unique:  # O(n) operation for each number, resulting in O(n^2) overall time complexity
                unique.append(num)
        return unique

    # More efficient way using a set:
    def unique_numbers_efficient(numbers):
        return list(set(numbers))  # Converting to a set removes duplicates in O(n) average time complexity
    # Sets automatically handle duplicate entries and offer better performance for this operation.
    # However, note that converting to a set does not preserve the original order of elements.

    # Advanced Tip: If order is important and you want to remove duplicates, use `collections.OrderedDict.fromkeys(numbers)` (Python 3.6+).
    # Since Python 3.7, regular dictionaries maintain insertion order, but using `OrderedDict` explicitly signals your intent.


def advanced_tips():
    """Provides advanced tips for working with lists, tuples, sets, and dictionaries."""

    # Using itertools for efficient iteration
    # The itertools module provides a collection of tools for handling iterators efficiently.
    # These tools allow for memory-efficient looping, especially with large datasets, 
    # without the need to create additional intermediate lists.

    import itertools  # Standard library for advanced iteration tools

    # Cartesian product: Useful for generating all possible combinations of items from multiple lists
    colors = ['red', 'green']  # A list of colors
    sizes = ['S', 'M', 'L']    # A list of sizes

    # itertools.product creates the Cartesian product of input iterables, equivalent to nested for-loops
    combinations = list(itertools.product(colors, sizes))
    
    # Output: [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L')]
    print(f"Product combinations: {combinations}")
    
    # Advanced Insight: 
    # The Cartesian product is often used in scenarios such as generating combinations for testing,
    # exhaustive search problems, or pairing items from different datasets.

    # Grouping data using itertools.groupby
    # itertools.groupby groups adjacent elements with a common key function result.
    # Important: groupby requires the data to be sorted based on the grouping key for accurate results.
    data = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit')]

    # First, sort the data by the category (second element in each tuple)
    grouped = itertools.groupby(sorted(data, key=lambda x: x[1]), key=lambda x: x[1])

    # Iterate through the grouped data
    for key, group in grouped:
        print(f"{key}: {list(group)}")
        
    # Potential Pitfall: Forgetting to sort the data before using groupby may result in incorrect grouping.
    # Advanced Tip: Using groupby is efficient when processing large datasets that are already sorted.

    # Using functools.lru_cache for memoization
    from functools import lru_cache  # lru_cache (Least Recently Used cache) for caching function results
    
    # Fibonacci function with memoization
    @lru_cache(maxsize=None)  # Cache results of the function calls; maxsize=None means an unlimited cache size
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(f"Fibonacci(100): {fibonacci(100)}")
    
    # Explanation:
    # Memoization stores the results of expensive function calls, avoiding redundant calculations.
    # This significantly optimizes recursive functions like Fibonacci, reducing time complexity from O(2^n) to O(n).
    
    # Potential Pitfall: Using lru_cache on functions with mutable arguments can lead to unexpected results. 
    # Always use it with functions that have immutable (hashable) arguments.

    # Using collections.Counter for counting elements in an iterable
    from collections import Counter  # Counter is a dictionary subclass that efficiently counts hashable objects
    
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
    word_counts = Counter(words)  # Creates a dictionary-like object where keys are items and values are their counts
    
    print(f"Word counts: {word_counts}")  # Output: {'apple': 2, 'banana': 2, 'cherry': 1, 'date': 1}
    print(f"Most common word: {word_counts.most_common(1)}")  # Output: [('apple', 2)]
    
    # Advanced Insight: Counter has many useful methods, such as .most_common(n) for finding the n most common elements.
    # It can be used for quick frequency analysis in tasks like natural language processing.

def write_testable_code():
    """Demonstrates how to write testable code for lists, tuples, sets, and dictionaries."""

    # The function `flatten_list` takes a nested list (list of lists) and flattens it into a single list.
    def flatten_list(nested_list):
        """Flatten a nested list."""
        flat_list = []  # Initialize an empty list to hold the flattened elements
        
        for item in nested_list:
            if isinstance(item, list):
                # Recursive case: If the item is a list, extend flat_list with the flattened version of that list
                flat_list.extend(flatten_list(item))
            else:
                # Base case: If the item is not a list, append it to flat_list
                flat_list.append(item)
                
        return flat_list

    # Advanced Explanation:
    # - The use of recursion here simplifies the flattening of arbitrarily nested lists.
    # - The function checks each element’s type with isinstance(), which is more reliable than using type() 
    #   as it accounts for subclassing.
    # Potential Pitfall: For deeply nested lists, recursion depth may become an issue due to Python's default recursion limit.

    # Writing Unit Tests using the unittest module
    # The unittest module provides a framework for constructing and running tests. This makes code more maintainable 
    # and ensures reliability through automatic test execution.
    import unittest  # Import the unittest module for test cases

    class TestFlattenList(unittest.TestCase):
        def test_flatten_list(self):
            # Test cases to validate the correctness of flatten_list
            self.assertEqual(flatten_list([1, [2, 3, [4, 5]], 6]), [1, 2, 3, 4, 5, 6])  # Test with a nested list
            self.assertEqual(flatten_list([]), [])  # Test with an empty list
            self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])  # Test with a flat list

    # Running the tests using unittest.main
    unittest.main(argv=[''], exit=False)  # argv=[''] ensures that unittest doesn't try to interpret any IPython command-line arguments
    
    # Advanced Insight:
    # - Writing testable code encourages separation of concerns (e.g., logic vs. presentation).
    # - unittest.main(argv=[''], exit=False) allows unittest to run within Jupyter Notebooks or interactive Python shells.
    # Potential Pitfall: Forgetting to include exit=False can cause the interpreter to shut down after running tests.

# Key Takeaways:
# - itertools, functools, and collections are powerful modules that extend Python’s capabilities beyond basic loops, 
#   conditionals, and data structures.
# - Writing unit tests ensures that your code is reliable and reduces future bugs, promoting long-term maintainability.
# - Employing advanced techniques such as memoization (lru_cache) can drastically improve performance for specific use cases.


# ========================================
# 4. Integration and Real-World Applications
# ----------------------------------------

def data_processing_example():
    """ 
    Demonstrates the use of fundamental Python data structures: lists, tuples, sets, and dictionaries 
    in the context of a real-world data processing scenario involving employee records. 
    This function performs tasks such as extracting unique values, calculating averages, finding max values, 
    and grouping data based on certain criteria.
    """
    
    # Sample data: A list of dictionaries, each representing an employee record with attributes like id, name,
    # department, and salary. This is a common structure for handling tabular data in Python.
    employees = [
        {'id': 1, 'name': 'Alice', 'department': 'IT', 'salary': 75000},
        {'id': 2, 'name': 'Bob', 'department': 'HR', 'salary': 65000},
        {'id': 3, 'name': 'Charlie', 'department': 'IT', 'salary': 80000},
        {'id': 4, 'name': 'David', 'department': 'Marketing', 'salary': 70000},
        {'id': 5, 'name': 'Eve', 'department': 'IT', 'salary': 78000},
    ]
    
    # --- Extracting Unique Departments ---
    # Using a set comprehension to collect unique departments from the employee data.
    # Sets inherently store unique values, making this the most efficient way to gather distinct items.
    # This step demonstrates the power of comprehensions combined with the uniqueness guarantee of sets.
    departments = set(emp['department'] for emp in employees)
    
    # Using an f-string for formatted output, which is more efficient and readable compared to older string formatting methods.
    print(f"Unique departments: {departments}")
    
    # Advanced Tip: Using set comprehensions is not only concise but also optimally performs deduplication in O(n) time complexity.
    # If using a list and then converting to a set, it would be less efficient.

    # --- Calculating Average Salary by Department ---
    # Using `defaultdict` from the `collections` module, which is a highly efficient way to handle 
    # grouping operations without needing to initialize dictionary keys manually. 
    from collections import defaultdict
    salary_by_dept = defaultdict(list)  # Initializes values as empty lists automatically.
    
    # Populate the dictionary where each department maps to a list of salaries
    for emp in employees:
        salary_by_dept[emp['department']].append(emp['salary'])
    
    # Creating a dictionary comprehension to calculate the average salary for each department.
    # Here, sum(salaries) calculates the total salary for each department, while len(salaries) gives the count.
    avg_salary = {dept: sum(salaries) / len(salaries) for dept, salaries in salary_by_dept.items()}
    
    print(f"Average salary by department: {avg_salary}")
    
    # Insight: This approach is efficient as it processes each employee in O(n) time.
    # Using `defaultdict` avoids the overhead of checking key existence, which improves performance.

    # --- Finding the Highest Paid Employee ---
    # Utilizing the built-in `max()` function with a lambda function as the `key` argument.
    # The lambda function extracts the salary value for comparison.
    highest_paid = max(employees, key=lambda emp: emp['salary'])
    
    # Displaying the highest-paid employee's name.
    print(f"Highest paid employee: {highest_paid['name']}")
    
    # Best Practice: The `max()` function is optimal for finding the maximum value in an iterable
    # in O(n) time complexity, making it suitable for reasonably sized data sets.

    # Potential Pitfall: If the `employees` list were empty, `max()` would raise a `ValueError`.
    # Consider handling this case in production code by using a try-except block or an early return.

    # --- Grouping Employees by Department ---
    # Again, using `defaultdict` to automatically handle missing keys while grouping employee names by department.
    emp_by_dept = defaultdict(list)
    
    # Populate the dictionary where each department maps to a list of employee names
    for emp in employees:
        emp_by_dept[emp['department']].append(emp['name'])
    
    # Converting defaultdict to a regular dictionary for cleaner output
    print(f"Employees by department: {dict(emp_by_dept)}")
    
    # Advanced Tip: Consider using the `groupby` function from the `itertools` module for grouping operations on sorted data.
    # It is more efficient when working with large, pre-sorted datasets but requires the data to be sorted by the key beforehand.

# ========================================
# Explanation and Insights
# ----------------------------------------
# 1. This example covers key data structures: lists (for employee data), dictionaries (for structured records),
#    sets (for unique department extraction), and defaultdicts (for efficient grouping and aggregation).
# 2. Using list comprehensions and set comprehensions keeps the code concise and readable.
# 3. Leveraging `defaultdict` simplifies data processing by eliminating the need to check for key existence.
# 4. The use of `lambda` in `max()` showcases an elegant way to perform custom comparisons on complex data.
# 5. The f-string formatting provides a modern and efficient way to handle output, enhancing readability and performance.
# ========================================


def api_design_example():
    """Demonstrates use of lists, tuples, sets, and dictionaries in API design by managing a book inventory system."""
    
    # Class definition for managing the inventory of books
    class BookInventory:
        # Constructor: Initializes an empty dictionary to store book information
        def __init__(self):
            # `self.books` holds all book records, keyed by ISBN
            # Structure: {ISBN (str): {'title': str, 'author': str, 'quantity': int}}
            self.books = {}
        
        # Method to add a new book to the inventory
        def add_book(self, isbn: str, title: str, author: str, quantity: int) -> None:
            """
            Adds a new book to the inventory.
            
            Parameters:
            - isbn (str): Unique identifier for the book.
            - title (str): Title of the book.
            - author (str): Author of the book.
            - quantity (int): Number of copies available.
            
            Note:
            - This will overwrite existing data if the ISBN already exists, making it important to ensure ISBN uniqueness.
            """
            self.books[isbn] = {'title': title, 'author': author, 'quantity': quantity}
            # Advanced Tip: Consider validating input data (e.g., check if `quantity` is non-negative) to avoid potential issues.
        
        # Method to remove a book from the inventory
        def remove_book(self, isbn: str) -> bool:
            """
            Removes a book from the inventory based on ISBN.
            
            Parameters:
            - isbn (str): Unique identifier of the book to be removed.
            
            Returns:
            - bool: True if the book was removed, False if the book was not found.
            
            Note:
            - Uses `pop()` to both remove and retrieve the item in a single step, which is more efficient than `del` with `get`.
            """
            return self.books.pop(isbn, None) is not None  # Returns True if the book was removed, otherwise False
        
        # Method to retrieve details of a specific book using its ISBN
        def get_book(self, isbn: str) -> dict:
            """
            Fetches book details based on ISBN.
            
            Parameters:
            - isbn (str): Unique identifier of the book.
            
            Returns:
            - dict: Book details, or an empty dictionary if the book is not found.
            
            Note:
            - The `get()` method prevents KeyError if the ISBN doesn't exist in `self.books`.
            """
            return self.books.get(isbn, {})
        
        # Method to update the quantity of a specific book
        def update_quantity(self, isbn: str, quantity: int) -> bool:
            """
            Updates the quantity of a specific book.
            
            Parameters:
            - isbn (str): Unique identifier of the book.
            - quantity (int): New quantity to be updated.
            
            Returns:
            - bool: True if the update was successful, False if the book was not found.
            
            Note:
            - Ensures the book exists before updating, preventing unintended key creation.
            - Important to check that `quantity` is a non-negative integer in real applications.
            """
            if isbn in self.books:
                self.books[isbn]['quantity'] = quantity
                return True
            return False
        
        # Method to retrieve all books in the inventory as a list of dictionaries
        def get_all_books(self) -> list:
            """
            Retrieves a list of all books in the inventory.
            
            Returns:
            - list: List of dictionaries, each containing details of a book, including its ISBN.
            
            Advanced Insight:
            - Uses dictionary unpacking (**book) to combine the ISBN into the book's dictionary, enhancing data clarity.
            """
            return [{'isbn': isbn, **book} for isbn, book in self.books.items()]
        
        # Method to retrieve books by a specific author
        def get_books_by_author(self, author: str) -> list:
            """
            Fetches all books by a specific author.
            
            Parameters:
            - author (str): The author's name to filter books by.
            
            Returns:
            - list: List of dictionaries representing books by the specified author.
            
            Best Practice:
            - Case sensitivity could be an issue. For more robustness, consider normalizing input and stored data using `str.lower()`.
            """
            return [{'isbn': isbn, **book} for isbn, book in self.books.items() if book['author'] == author]
        
        # Method to retrieve a set of ISBNs for books that are currently available (quantity > 0)
        def get_available_books(self) -> set:
            """
            Retrieves ISBNs of all books with a quantity greater than zero.
            
            Returns:
            - set: A set of ISBNs representing available books.
            
            Advanced Tip:
            - Sets are ideal for membership tests and ensuring unique entries, making them efficient for this use case.
            """
            return {isbn for isbn, book in self.books.items() if book['quantity'] > 0}
    
    # Usage example: Demonstrating the BookInventory class functionality
    inventory = BookInventory()
    inventory.add_book("978-1234567890", "Python Mastery", "John Doe", 5)  # Adding a book to the inventory
    inventory.add_book("978-0987654321", "Data Structures", "Jane Smith", 3)
    inventory.add_book("978-1111222233", "Algorithms", "John Doe", 7)
    
    # Retrieving and displaying all books
    print(f"All books: {inventory.get_all_books()}")  # Expecting a list of all books with details
    
    # Fetching and displaying books by author "John Doe"
    print(f"Books by John Doe: {inventory.get_books_by_author('John Doe')}")  # Should show books authored by John Doe
    
    # Displaying the set of available books (ISBNs only)
    print(f"Available books (ISBNs): {inventory.get_available_books()}")  # Should show ISBNs of books with quantity > 0
    
    # Updating the quantity of a book to zero (making it unavailable)
    inventory.update_quantity("978-1234567890", 0)
    
    # Displaying updated available books to reflect changes
    print(f"Updated available books (ISBNs): {inventory.get_available_books()}")  # The previously updated book should no longer appear

# Advanced Insights:
# 1. This code offers a practical example of leveraging Python's core data structures:
#    - Dictionaries provide efficient O(1) average-time complexity for CRUD (Create, Read, Update, Delete) operations.
#    - Lists and sets are used contextually, showcasing the importance of choosing the right data structure for specific tasks.
# 2. Potential scalability concerns: As `self.books` grows, operations like `get_books_by_author` might become slower 
#    due to linear search time (O(n)). Consider using an index (e.g., another dictionary) if dealing with large datasets.

# Pitfall Warning:
# If multiple books have the same title or author, the current implementation doesn't address duplicates by any means 
# other than unique ISBNs. In a real-world scenario, consider enforcing or validating ISBN uniqueness at a broader scope.


# ========================================
# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# This section explores advanced Python concepts such as type hinting, structural pattern matching, 
# collections utilities, and read-only data structures. These concepts are increasingly important for 
# writing modern, robust, and maintainable Python code.
# ========================================

def advanced_concepts():
    """Explores advanced concepts and emerging trends related to lists, tuples, sets, and dictionaries."""
    
    # --- Import Statements ---
    # Importing type hinting tools and advanced collection types.
    from typing import List, Dict, Tuple, Set, TypeVar  # Provides support for generic programming and type hints
    
    # TypeVar allows us to create generic, reusable components.
    T = TypeVar('T')  # 'T' acts as a placeholder for any data type

    # ========================================
    # Advanced Concept 1: Type Hinting with Generics (Python 3.9+)
    # ----------------------------------------
    # Type hinting increases code readability and helps with static type checkers (e.g., mypy).
    # Generics allow functions to handle various data types flexibly without sacrificing type safety.
    # ========================================

    def process_list(items: List[T]) -> List[Tuple[T, int]]:
        """
        Converts a list of items to a list of tuples, where each tuple contains the item and its length as a string.

        - List[T]: Indicates the function accepts a list of any type 'T'.
        - List[Tuple[T, int]]: The function returns a list of tuples containing the original item and an integer.

        Best Practice: Always use type hints to make code more understandable and to facilitate type checking in larger projects.
        """
        return [(item, len(str(item))) for item in items]

    # Example usage of the `process_list` function with different data types
    numbers: List[int] = [1, 22, 333]  # Explicitly indicating this is a list of integers
    strings: List[str] = ["a", "bb", "ccc"]  # Explicitly indicating this is a list of strings
    print(f"Processed numbers: {process_list(numbers)}")
    print(f"Processed strings: {process_list(strings)}")

    # Advanced Tip: The use of TypeVar ('T') enables this function to be reused for various data types,
    # showcasing how Python's typing system supports flexible yet type-safe code.

    # ========================================
    # Advanced Concept 2: Structural Pattern Matching (Python 3.10+)
    # ----------------------------------------
    # Pattern matching is similar to switch-case statements in other languages but far more powerful.
    # It allows matching complex data structures, making code cleaner and more expressive.
    # ========================================

    def analyze_data_structure(data):
        # The `match` statement inspects the structure and content of `data` and matches specific patterns.
        match data:
            case []:
                return "Empty list"  # Matches an empty list
            case [_]:
                return "Single-element list"  # Matches a list with exactly one element
            case [_, _]:
                return "Two-element list"  # Matches a list with exactly two elements
            case [*_, last]:
                return f"List with {len(data)} elements, last is {last}"  # Matches a list of any length and captures the last element
            case {}:
                return "Empty dict"  # Matches an empty dictionary
            case {'name': str(name), 'age': int(age)}:
                return f"Person dict with name {name} and age {age}"  # Matches a dictionary with 'name' and 'age' keys
            case _:
                return "Unknown data structure"  # Fallback for unmatched cases

    # Demonstrating pattern matching with different data structures
    print(analyze_data_structure([]))  # Should output: "Empty list"
    print(analyze_data_structure([1, 2, 3, 4, 5]))  # Should output: "List with 5 elements, last is 5"
    print(analyze_data_structure({'name': 'Alice', 'age': 30}))  # Should output: "Person dict with name Alice and age 30"

    # Pitfall: Pattern matching is strict in its structure. The dictionary pattern {'name': str(name), 'age': int(age)}
    # will not match if extra keys are present. Always ensure patterns are as specific or as flexible as needed.

    # ========================================
    # Advanced Concept 3: Using collections.ChainMap for Layered Dictionaries
    # ----------------------------------------
    # ChainMap allows combining multiple dictionaries into a single view, enabling multi-layered lookups.
    # This is particularly useful for managing configuration settings where defaults and user overrides coexist.
    # ========================================

    from collections import ChainMap

    defaults = {'color': 'red', 'user': 'guest'}  # Default settings
    user_prefs = {'color': 'blue'}  # User-specific preferences that override defaults
    combined = ChainMap(user_prefs, defaults)  # Combines dictionaries; `user_prefs` takes precedence

    print(f"Combined preferences: {dict(combined)}")  # Outputs: {'color': 'blue', 'user': 'guest'}

    # Advanced Insight: ChainMap doesn't create new dictionaries; it maintains references to the originals.
    # Any modification to `user_prefs` or `defaults` will reflect in `combined`. This is memory efficient but requires caution.

    # ========================================
    # Advanced Concept 4: Using types.MappingProxyType for Read-Only Dictionaries
    # ----------------------------------------
    # MappingProxyType provides a dynamic, read-only view of a dictionary.
    # It’s useful when you want to protect data from being modified but still need access to it.
    # ========================================

    from types import MappingProxyType

    writable = {'one': 1, 'two': 2}  # Original dictionary
    read_only = MappingProxyType(writable)  # Creates a read-only view of 'writable'
    
    # read_only['three'] = 3  # Uncommenting this would raise a TypeError: 'mappingproxy' object does not support item assignment

    # Note: Any changes made to `writable` will be reflected in `read_only`. This can be both a feature and a potential pitfall.

    # ========================================
    # Advanced Concept 5: Immutable Sets with frozenset
    # ----------------------------------------
    # While sets are mutable, frozenset provides an immutable alternative, which can be used as dictionary keys or stored in other sets.
    # This is essential for situations where immutability is required for maintaining data integrity.
    # ========================================

    immutable_set = frozenset([1, 2, 3])  # Creating an immutable set

    # immutable_set.add(4)  # Uncommenting this would raise an AttributeError: 'frozenset' object has no attribute 'add'

    # Advanced Insight: While `frozenset` is immutable, it's still hashable, making it suitable for use in contexts requiring hashable types.
    # This contrasts with regular sets, which are unhashable and therefore cannot be used as dictionary keys.

# Call the function to demonstrate these advanced concepts
# advanced_concepts()


# ========================================
# 6. FAQs and Troubleshooting
# ---------------------------------
def faqs_and_troubleshooting():
    """
    Addresses common questions and issues related to fundamental data structures in Python: 
    lists, tuples, sets, and dictionaries. This section covers frequently encountered problems 
    along with best practices and efficient solutions.
    """
    
    # Q1: How do I remove duplicates from a list while preserving the original order?
    def remove_duplicates(lst):
        # The `dict.fromkeys()` method preserves the insertion order since Python 3.7+. 
        # It utilizes the fact that dictionaries maintain the order of keys, effectively 
        # filtering duplicates while keeping the first occurrence intact.
        return list(dict.fromkeys(lst))
    
    # Example demonstrating duplicate removal while maintaining order
    original = [1, 2, 3, 2, 4, 1, 5]
    print(f"Original: {original}")  # Output: Original list with duplicates
    print(f"Without duplicates: {remove_duplicates(original)}")  # Output: List with duplicates removed

    # Advanced Insight:
    # `dict.fromkeys()` is both time and space efficient compared to other methods like list comprehensions
    # or using `OrderedDict` from `collections`. However, if you're using Python versions older than 3.7,
    # where dictionaries don't maintain order, consider using `OrderedDict.fromkeys(lst)` instead.

    # Q2: How can I sort a list of dictionaries by a specific key?
    people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    
    # The `sorted()` function creates a new sorted list; the `key` parameter specifies the sorting criterion.
    sorted_people = sorted(people, key=lambda x: x['age'])  # Lambda function accesses the 'age' key of each dictionary
    print(f"Sorted by age: {sorted_people}")  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
    
    # Best Practice:
    # Always prefer `sorted()` over `list.sort()` when you need to maintain the original list,
    # as `sorted()` is non-destructive and returns a new list, while `list.sort()` modifies the list in place.
    
    # Potential Pitfall:
    # Sorting with `key=lambda x: x['age']` assumes that all dictionaries have the 'age' key. If not, it raises a KeyError.
    # To handle such cases gracefully, use `key=lambda x: x.get('age', default_value)`.

    # Q3: How do I merge two dictionaries?
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    
    # Merging dictionaries using dictionary unpacking (Python 3.5+ feature)
    merged = {**dict1, **dict2}  # If duplicate keys exist, values from `dict2` will overwrite `dict1`
    print(f"Merged dictionary: {merged}")  # Output: {'a': 1, 'b': 3, 'c': 4}
    
    # Advanced Tip:
    # In Python 3.9+, you can merge dictionaries using the union operator (`|`):
    # merged = dict1 | dict2
    # This is more intuitive and aligns with the mathematical concept of a union.

    # Q4: How can I create a dictionary from two lists?
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    
    # Using `zip()` to combine two lists into pairs and then converting them into a dictionary
    new_dict = dict(zip(keys, values))
    print(f"Dictionary from lists: {new_dict}")  # Output: {'a': 1, 'b': 2, 'c': 3}
    
    # Best Practice:
    # Ensure both lists are of the same length when using `zip()`. If they aren't, the shorter list determines
    # the length of the resulting dictionary, and elements from the longer list are ignored without any error.

    # Alternative Approach:
    # If you need to handle mismatched lengths explicitly, use `itertools.zip_longest`:
    # from itertools import zip_longest
    # new_dict = dict(zip_longest(keys, values, fillvalue=None))

    # Q5: How do I find the intersection of two lists?
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    
    # Converting lists to sets and finding the intersection using the `&` operator
    intersection = list(set(list1) & set(list2))
    print(f"Intersection: {intersection}")  # Output: [4, 5]
    
    # Advanced Insight:
    # The `set` approach is efficient for finding intersections due to O(1) average-time complexity of set lookups.
    # However, this loses the original order. If maintaining order is essential, consider using:
    # intersection = [item for item in list1 if item in list2]

    # Potential Pitfall:
    # Using `&` requires both operands to be sets. Forgetting to convert lists to sets results in a TypeError.
    # Always ensure you explicitly cast to `set()` before applying set operations.

# Function invocation
# faqs_and_troubleshooting()


# ========================================
# 7. Recommended Tools, Libraries, and Resources
# ---------------------------------------------

"""
When working with lists, tuples, sets, and dictionaries in Python, leveraging the right tools and libraries can significantly 
enhance efficiency, performance, and overall productivity. Below is an in-depth guide to some of the most powerful tools and 
resources available for these data structures.

1. Collections Module:
   The `collections` module is part of Python's standard library and offers specialized container data types that extend 
   Python's built-in data structures, providing more powerful alternatives for various scenarios.
   - `namedtuple`: A lightweight object type similar to a tuple but with named fields, improving code readability.
   - `defaultdict`: A subclass of `dict` that returns a default value if a key doesn't exist, avoiding `KeyError`.
   - `Counter`: A convenient way to count occurrences of elements in a collection.
   - `OrderedDict`: Maintains the insertion order of keys (insertion order is now standard in Python 3.7+ dictionaries).
   - `deque`: Provides a double-ended queue with fast appends and pops from either end.

   This module is essential for tasks requiring specialized data handling beyond standard lists or dictionaries.
   Official documentation: https://docs.python.org/3/library/collections.html

2. Itertools Module:
   The `itertools` module provides efficient tools for creating and working with iterators, enabling advanced iteration 
   techniques. It includes functions that work on iterable data structures, such as lists, tuples, and sets, and offers:
   - Infinite iterators (`count`, `cycle`, `repeat`) for generating values indefinitely.
   - Combinatorial generators (`permutations`, `combinations`, `product`) for producing combinations and permutations.
   - Utility functions like `chain` (for chaining multiple iterables), `islice` (for slicing iterables), and `tee` 
     (for creating multiple independent iterators from a single iterable).

   These tools are particularly valuable for handling complex iteration patterns in an optimized and memory-efficient manner.
   Official documentation: https://docs.python.org/3/library/itertools.html

3. Functools Module:
   The `functools` module provides higher-order functions that operate on callable objects, allowing advanced functional 
   programming techniques. Key utilities include:
   - `lru_cache`: Implements caching (memoization) to store the results of expensive function calls and reuse them, 
     significantly improving performance for repetitive computations.
   - `reduce`: Applies a rolling computation to a sequence, reducing it to a single cumulative value.
   - `partial`: Allows the partial application of functions by pre-filling certain arguments, making code more modular 
     and reusable.

   `functools` is especially helpful for improving code efficiency and for writing cleaner, more maintainable code.
   Official documentation: https://docs.python.org/3/library/functools.html

4. Numpy:
   `NumPy` is a powerful, third-party library widely used for numerical computing in Python. It provides support for 
   large, multi-dimensional arrays and matrices, along with a wide range of mathematical functions to operate on them.
   - Arrays in `NumPy` are more efficient and faster than Python lists for numerical operations, thanks to their 
     contiguous memory layout and optimized C-based implementation.
   - Offers comprehensive functionality for array manipulation, linear algebra, statistical analysis, and more.

   `NumPy` is essential for any data-intensive task or scientific computing and serves as the foundation for many 
   other libraries, such as `pandas`.
   Official website: https://numpy.org/

5. Pandas:
   `pandas` is an advanced data manipulation and analysis library built on top of `NumPy`. It introduces two key data 
   structures: `Series` (1D) and `DataFrame` (2D), which offer powerful methods for data wrangling, cleaning, 
   visualization, and analysis.
   - Handles missing data elegantly using NaN (Not a Number) and provides tools for handling missing values.
   - Enables efficient handling of labeled and relational data, making it ideal for data science, finance, and 
     analytics applications.

   `pandas` is invaluable for anyone working with structured data, enabling quick and efficient data manipulation.
   Official website: https://pandas.pydata.org/

# Additional Tools Worth Exploring:
- `array` module: Efficient for storing homogeneous data types with less overhead compared to Python lists.
- `bisect` module: Offers efficient algorithms for maintaining a list in sorted order using binary search.
- `heapq` module: Implements a heap queue algorithm for priority queue implementations.

# Resources for Further Learning and Mastery:
1. Python Official Documentation:
   The official Python documentation is a reliable, comprehensive source for understanding built-in data structures.
   URL: https://docs.python.org/3/tutorial/datastructures.html

2. "Fluent Python" by Luciano Ramalho:
   A highly recommended book for deepening your understanding of Python's data structures, offering insights and 
   techniques for writing more idiomatic, efficient Python code.

3. "Python Cookbook" by David Beazley and Brian K. Jones:
   Contains a collection of practical recipes for solving real-world problems, making it an excellent resource for 
   learning advanced data manipulation techniques and best practices.

4. Real Python Tutorials:
   Real Python offers high-quality tutorials that cover a wide range of topics, including data structures. These 
   tutorials are easy to follow and provide hands-on examples.
   URL: https://realpython.com/tutorials/data-structures/

5. PyData Conference Talks on YouTube:
   PyData conferences feature talks on advanced data structure usage and applications in data science, providing 
   exposure to real-world applications and best practices from industry experts.

# Advanced Insights and Best Practices:
- Always profile your code with `timeit` or `cProfile` when working with large data sets to identify bottlenecks and 
  optimize performance.
- Use `defaultdict` over a standard dictionary when working with collections that need default values, as it 
  eliminates the need for manual checks and initialization.
- Opt for `deque` when you need efficient append and pop operations from both ends of a collection, as it offers 
  O(1) complexity compared to lists' O(n) complexity for these operations.

# Key Takeaway:
Investing time in learning and mastering these tools and resources will greatly enhance your productivity and enable 
you to handle complex data manipulation tasks more efficiently and effectively.
"""
# ========================================
# 8. Performance Analysis and Optimization
# ----------------------------------------
def performance_analysis():
    """Demonstrates performance analysis and optimization techniques using timeit module for benchmarking."""
    import timeit  # Import the timeit module for precise timing of small code snippets

    # ----------------------------------------
    # List vs. Set for Membership Testing
    # ----------------------------------------
    # Explanation: 
    # This section compares the efficiency of membership testing (`in` keyword) between lists and sets.
    # Lists have an average O(n) time complexity for membership testing, while sets have O(1) on average due to their underlying hash table implementation.

    def list_membership(n):
        lst = list(range(n))  # Create a list containing elements from 0 to n-1
        return n-1 in lst  # Check if the last element exists in the list

    def set_membership(n):
        st = set(range(n))  # Create a set containing elements from 0 to n-1
        return n-1 in st  # Check if the last element exists in the set

    n = 10000  # Define the size of the dataset
    # Using timeit to measure execution time for 1000 iterations of each function
    list_time = timeit.timeit(lambda: list_membership(n), number=1000)
    set_time = timeit.timeit(lambda: set_membership(n), number=1000)
    print(f"List membership time: {list_time:.6f} seconds")
    print(f"Set membership time: {set_time:.6f} seconds")

    # Best Practice:
    # - Use sets for membership testing whenever possible, especially with large datasets, as it provides faster lookups.
    
    # Potential Pitfall:
    # - Be cautious about using sets if your data requires maintaining order or if you're working with non-hashable elements (e.g., lists).

    # Advanced Insight:
    # - Although set membership testing is generally O(1), hash collisions can degrade performance to O(n) in the worst case.

    # ----------------------------------------
    # Dictionary vs. List for Counting Elements
    # ----------------------------------------
    # Explanation:
    # This segment demonstrates two different methods of counting elements in a dataset – using a list of lists vs. a dictionary.
    # Counting with lists involves nested loops (O(n^2)), while dictionaries use hash tables, resulting in average O(n) complexity.

    def count_with_list(elements):
        counts = []  # Initialize an empty list to store counts
        for element in elements:
            # Search for the element in the counts list
            for item in counts:
                if item[0] == element:
                    item[1] += 1  # Increment count if found
                    break
            else:
                counts.append([element, 1])  # Add a new entry if not found
        return counts

    def count_with_dict(elements):
        # Use a dictionary comprehension to count elements more efficiently
        return {element: elements.count(element) for element in set(elements)}

    elements = [1, 2, 3, 1, 2, 1, 4, 5, 4] * 1000  # Create a sample dataset with repeated elements
    # Timing the two approaches
    list_count_time = timeit.timeit(lambda: count_with_list(elements), number=10)
    dict_count_time = timeit.timeit(lambda: count_with_dict(elements), number=10)
    print(f"List counting time: {list_count_time:.6f} seconds")
    print(f"Dict counting time: {dict_count_time:.6f} seconds")

    # Best Practice:
    # - Use dictionaries (or `collections.Counter`) for counting occurrences in large datasets as they offer better performance.

    # Potential Pitfall:
    # - Using `elements.count(element)` inside a loop results in O(n^2) time complexity, which is inefficient for large datasets.

    # Advanced Insight:
    # - Consider using `collections.defaultdict(int)` or `collections.Counter` for counting elements efficiently, as they handle the counting logic internally and are optimized for performance.

    # ----------------------------------------
    # List Comprehension vs. map() for Simple Transformations
    # ----------------------------------------
    # Explanation:
    # This comparison showcases the performance difference between list comprehensions and the `map()` function for applying transformations.
    # List comprehensions are often more Pythonic and easier to read, while `map()` can be faster in some cases, especially for large datasets.

    def square_list_comp(n):
        return [x**2 for x in range(n)]  # Using list comprehension to square each element

    def square_map(n):
        return list(map(lambda x: x**2, range(n)))  # Using map() to apply a lambda function to square each element

    n = 10000  # Set the size of the dataset
    # Measure the execution time for each approach
    list_comp_time = timeit.timeit(lambda: square_list_comp(n), number=1000)
    map_time = timeit.timeit(lambda: square_map(n), number=1000)
    print(f"List comprehension time: {list_comp_time:.6f} seconds")
    print(f"Map time: {map_time:.6f} seconds")

    # Best Practice:
    # - Prefer list comprehensions for most cases due to their readability and performance, especially for simple transformations.

    # Potential Pitfall:
    # - `map()` returns an iterator in Python 3, which is lazily evaluated, meaning the transformation is only applied when iterated over.
    # - This can be beneficial for large datasets but might cause confusion if immediate execution is expected.

    # Advanced Insight:
    # - `map()` can outperform list comprehensions when using built-in functions (e.g., `math.sqrt`) due to reduced function call overhead.
    # - If you don't need the transformed list immediately, consider using `map()` to leverage lazy evaluation and save memory.

# Call the function to execute the performance analysis
# performance_analysis()


def main():
    """Main function to demonstrate various concepts. This function acts as an orchestrator, sequentially
    calling individual functions that cover fundamental to advanced Python topics.
    
    The approach of using multiple modular functions here:
    - Demonstrates the modular design, which is a best practice in software engineering.
    - Improves maintainability by allowing isolated testing of each function.
    - Enhances readability and reduces complexity within the `main()` function itself.
    """

    # Basic Operations with Lists
    print("1. List Basics:")
    list_basics()  # Calls the function handling fundamental list operations and concepts.

    # Basic Operations with Tuples
    print("\n2. Tuple Basics:")
    tuple_basics()  # Demonstrates the immutability and uses of tuples in contrast to lists.

    # Basic Operations with Sets
    print("\n3. Set Basics:")
    set_basics()  # Illustrates set operations, unique data handling, and the benefits of hash-based membership tests.

    # Basic Operations with Dictionaries
    print("\n4. Dictionary Basics:")
    dict_basics()  # Explores key-value data structures, lookup efficiency, and dictionary-specific methods.

    # Demonstrates more complex or less commonly known operations in Python
    print("\n5. Advanced Operations:")
    advanced_operations()  # Covers slicing, comprehensions, unpacking, and more advanced Python features.

    # Showcases best practices that enhance code readability, maintainability, and efficiency
    print("\n6. Best Practices:")
    best_practices()  # Discusses topics like PEP 8 compliance, error handling, and modularity.

    # Demonstrates common pitfalls that even experienced developers might encounter
    print("\n7. Common Pitfalls:")
    common_pitfalls()  # Points out issues like mutable default arguments, floating-point inaccuracies, and scope-related problems.

    # Provides advanced tips for writing optimized and efficient code
    print("\n8. Advanced Tips:")
    advanced_tips()  # Offers insights on techniques such as generator expressions, context managers, and efficient looping.

    # Illustrates how to write code that is easy to test
    print("\n9. Testable Code:")
    write_testable_code()  # Discusses strategies for writing unit-testable functions, mocking, and structuring tests effectively.

    # Demonstrates data processing techniques, often used in data science or ETL pipelines
    print("\n10. Data Processing Example:")
    data_processing_example()  # Covers concepts like data cleaning, transformation, aggregation, and using libraries like Pandas if applicable.

    # Showcases principles of API design and how to implement them in Python
    print("\n11. API Design Example:")
    api_design_example()  # Examines RESTful design, parameter handling, error codes, and documentation practices.

    # Introduces advanced concepts like metaprogramming, decorators, or threading/multiprocessing
    print("\n12. Advanced Concepts:")
    advanced_concepts()  # Discusses advanced Python constructs such as decorators, metaclasses, or the Global Interpreter Lock (GIL).

    # Answers common questions and troubleshooting techniques often encountered during Python development
    print("\n13. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()  # Addresses frequent queries and debugging strategies, with emphasis on problem-solving approaches.

    # Discusses how to analyze the performance of your code, a critical skill for optimization
    print("\n14. Performance Analysis:")
    performance_analysis()  # Explores tools like `timeit`, profiling modules (`cProfile`), and tips for identifying bottlenecks.

# Entry point of the program: standard Python convention
if __name__ == "__main__":
    main()  # When this module is run directly, the `main()` function is executed.
    
# Detailed Explanation of Entry Point:
# The `if __name__ == "__main__":` idiom is essential for differentiating between when the script is run directly 
# versus when it's imported as a module in another script. This pattern:
# - Prevents certain code blocks from being executed during import, ensuring modularity and reusability.
# - Is a Python best practice that facilitates clean execution flow in larger projects.
# 
# Common Pitfall: Forgetting this idiom might result in unintended code execution when the script is imported as a module.


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
- Relevance to the main topic of the 're' module and regular expressions in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

"""

# End of cheat sheet