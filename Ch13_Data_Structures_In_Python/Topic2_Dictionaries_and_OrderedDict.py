"""
Data Structures in Python - Dictionaries and OrderedDict - in the Python Programming Language
=============================================================================================

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
Dictionaries are one of the most powerful and widely used data structures in Python. They are hash tables that provide efficient key-value pair storage and retrieval. OrderedDict is a dictionary subclass that remembers the order in which keys were inserted.

Historical context:
- Dictionaries have been a core data structure in Python since its inception in 1991.
- The OrderedDict was introduced in Python 2.7 (2010) as part of the collections module.
- In Python 3.7+ (2018), the built-in dict class became ordered by default, maintaining insertion order.

Significance:
- Dictionaries provide O(1) average time complexity for insertions, deletions, and lookups.
- They are fundamental to Python's implementation, used internally for namespaces, function keyword arguments, and more.
- OrderedDict offers additional functionality for order-sensitive operations.

Common use cases:
- Caching and memoization
- Counting and grouping data
- Implementing graphs and trees
- Configuration management
- JSON-like data structures

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from collections import OrderedDict, defaultdict, Counter
import time
from typing import Dict, Any, List, Tuple

def basic_dictionary_operations():
    """Demonstrate basic dictionary operations."""
    # Creating a dictionary
    person = {"name": "Alice", "age": 30, "city": "New York"}
    print("1. Basic dictionary:", person)

    # Accessing values
    print("2. Name:", person["name"])

    # Adding and modifying key-value pairs
    person["job"] = "Engineer"
    person["age"] = 31
    print("3. Updated dictionary:", person)

    # Removing key-value pairs
    del person["city"]
    print("4. After deletion:", person)

    # Dictionary methods
    print("5. Keys:", person.keys())
    print("6. Values:", person.values())
    print("7. Items:", person.items())

    # Dictionary comprehension
    squared = {x: x**2 for x in range(5)}
    print("8. Squared numbers:", squared)

def dictionary_advanced_operations():
    """Demonstrate advanced dictionary operations."""
    # Merging dictionaries
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged = {**dict1, **dict2}
    print("1. Merged dictionary:", merged)

    # Using get() with a default value
    person = {"name": "Bob", "age": 25}
    print("2. Job:", person.get("job", "Unknown"))

    # Nested dictionaries
    nested = {"outer": {"inner": "value"}}
    print("3. Nested value:", nested["outer"]["inner"])

    # Dictionary views
    d = {"a": 1, "b": 2}
    keys = d.keys()
    print("4. Keys before update:", keys)
    d["c"] = 3
    print("5. Keys after update:", keys)

    # Using setdefault()
    d.setdefault("d", 4)
    print("6. After setdefault:", d)

def ordered_dict_operations():
    """Demonstrate OrderedDict operations."""
    # Creating an OrderedDict
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print("1. OrderedDict:", od)

    # Reordering
    od.move_to_end('b')
    print("2. After moving 'b' to end:", od)

    # Popping items
    last = od.popitem()
    first = od.popitem(last=False)
    print(f"3. Popped last: {last}, first: {first}")
    print("   Remaining:", od)

    # Equality comparison
    od1 = OrderedDict([('a', 1), ('b', 2)])
    od2 = OrderedDict([('b', 2), ('a', 1)])
    print("4. od1 == od2:", od1 == od2)

    d1 = dict([('a', 1), ('b', 2)])
    d2 = dict([('b', 2), ('a', 1)])
    print("5. d1 == d2:", d1 == d2)

def dictionary_variants():
    """Demonstrate dictionary variants from the collections module."""
    # defaultdict
    dd = defaultdict(list)
    dd['a'].append(1)
    dd['a'].append(2)
    print("1. defaultdict:", dict(dd))

    # Counter
    c = Counter("abracadabra")
    print("2. Counter:", c)
    print("3. Most common:", c.most_common(2))

    # ChainMap
    from collections import ChainMap
    default_config = {'debug': False, 'port': 8000}
    user_config = {'port': 8080}
    config = ChainMap(user_config, default_config)
    print("4. ChainMap:", dict(config))

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use dictionary comprehensions for simple transformations.
2. Prefer .get() method with a default value to handle missing keys.
3. Use collections.Counter for counting hashable objects.
4. Leverage collections.defaultdict for automatic default value initialization.
5. Use items() method for efficient iteration over key-value pairs.

Common Pitfalls:
1. Modifying a dictionary while iterating over it.
2. Assuming keys are always present (use .get() or try/except).
3. Using mutable objects as dictionary keys.
4. Overusing dictionaries when a simpler data structure would suffice.
5. Neglecting to consider the memory overhead of large dictionaries.

Advanced Tips:
1. Use dict.fromkeys() for initializing dictionaries with default values.
2. Leverage __missing__() method for custom default value handling.
3. Use collections.OrderedDict for maintaining insertion order (pre-Python 3.7).
4. Implement __eq__() and __hash__() methods for custom objects used as dictionary keys.
5. Use weakref.WeakKeyDictionary or weakref.WeakValueDictionary for memory-efficient caching.
"""

def demonstrate_best_practices():
    """Demonstrate best practices and advanced tips."""
    # 1. Dictionary comprehension
    squared = {x: x**2 for x in range(5)}
    print("1. Squared dict:", squared)

    # 2. Using .get() with default
    config = {"debug": True}
    port = config.get("port", 8000)
    print("2. Port:", port)

    # 3. Using Counter
    from collections import Counter
    words = "the quick brown fox jumps over the lazy dog".split()
    word_counts = Counter(words)
    print("3. Word counts:", word_counts)

    # 4. Using defaultdict
    from collections import defaultdict
    grouped = defaultdict(list)
    for name in ["Alice", "Bob", "Charlie", "Anna"]:
        grouped[name[0]].append(name)
    print("4. Grouped names:", dict(grouped))

    # 5. Efficient key-value iteration
    data = {"a": 1, "b": 2, "c": 3}
    for key, value in data.items():
        print(f"5. {key}: {value}")

def demonstrate_advanced_techniques():
    """Demonstrate advanced dictionary techniques."""
    # Custom default value handling
    class DefaultHandlingDict(dict):
        def __missing__(self, key):
            return f"No value for '{key}'"

    d = DefaultHandlingDict({"a": 1, "b": 2})
    print("1. Custom default handling:", d["c"])

    # Using WeakKeyDictionary for caching
    import weakref
    class HeavyObject:
        def __init__(self, value):
            self.value = value

    cache = weakref.WeakKeyDictionary()
    obj1 = HeavyObject(1)
    obj2 = HeavyObject(2)
    cache[obj1] = "Result 1"
    cache[obj2] = "Result 2"
    print("2. WeakKeyDictionary:", list(cache.items()))
    del obj1
    print("   After deleting obj1:", list(cache.items()))

    # Subclassing dict for custom behavior
    class CaseInsensitiveDict(dict):
        def __setitem__(self, key, value):
            super().__setitem__(key.lower(), value)

        def __getitem__(self, key):
            return super().__getitem__(key.lower())

    cid = CaseInsensitiveDict()
    cid["Name"] = "Alice"
    print("3. Case-insensitive dict:", cid["name"])

"""
4. Integration and Real-World Applications
------------------------------------------
Dictionaries and OrderedDict are widely used in various Python applications:

1. Configuration Management: Storing application settings
2. Caching: Implementing memoization and caching strategies
3. Data Processing: Grouping and aggregating data efficiently
4. Web Development: Handling JSON data in APIs

Real-world example: Simple Cache Implementation
"""

import time

class SimpleCache:
    def __init__(self, max_size=100):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)
        self.cache[key] = value

def fibonacci(n, cache):
    if n < 2:
        return n
    result = cache.get(n)
    if result is not None:
        return result
    result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    cache.put(n, result)
    return result

def demonstrate_cache_usage():
    """Demonstrate the usage of SimpleCache with Fibonacci calculation."""
    cache = SimpleCache()
    
    start = time.time()
    result = fibonacci(100, cache)
    end = time.time()
    
    print(f"1. 100th Fibonacci number: {result}")
    print(f"2. Calculation time: {end - start:.6f} seconds")
    print(f"3. Cache size: {len(cache.cache)}")
    print(f"4. Cache keys: {list(cache.cache.keys())}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Type hinting for dictionaries in Python 3.9+
2. Using dictionaries in concurrent and parallel programming
3. Memory-efficient dictionaries for large-scale applications
"""

from typing import Dict, List, TypedDict

class Person(TypedDict):
    name: str
    age: int

def demonstrate_type_hinting():
    """Demonstrate type hinting with dictionaries."""
    def process_people(people: Dict[str, Person]) -> List[str]:
        return [f"{id}: {person['name']}" for id, person in people.items()]

    people: Dict[str, Person] = {
        "001": {"name": "Alice", "age": 30},
        "002": {"name": "Bob", "age": 25}
    }

    result = process_people(people)
    print("1. Processed people:", result)

import asyncio

async def concurrent_dict_operations():
    """Demonstrate concurrent dictionary operations."""
    async def update_dict(d: Dict[str, int], key: str, value: int):
        await asyncio.sleep(0.1)  # Simulate some async operation
        d[key] = value

    data: Dict[str, int] = {}
    tasks = [update_dict(data, f"key{i}", i) for i in range(5)]
    await asyncio.gather(*tasks)
    print("2. Concurrent dictionary:", data)

"""
6. FAQs and Troubleshooting
---------------------------
Q1: How can I sort a dictionary by value?
A1: Use the sorted() function with a custom key:
    sorted(d.items(), key=lambda x: x[1])

Q2: What's the difference between dict.get() and dict[]?
A2: dict.get() returns a default value (or None) for missing keys, while dict[] raises a KeyError.

Q3: How can I merge two dictionaries?
A3: In Python 3.5+, use {**dict1, **dict2}. In older versions, use dict1.update(dict2).

Q4: When should I use OrderedDict instead of a regular dict?
A4: Use OrderedDict when you need guaranteed order preservation and order-based operations, especially in Python versions earlier than 3.7.

Q5: How can I implement a bi-directional dictionary?
A5: Create a custom class that maintains two internal dictionaries, updating both when adding or removing items.

Troubleshooting guide:
1. Issue: KeyError when accessing dictionary
   Solution: Use dict.get() with a default value or handle the exception with try/except.

2. Issue: Unexpected behavior with mutable dictionary keys
   Solution: Use immutable types (e.g., tuples instead of lists) for dictionary keys.

3. Issue: Memory usage problems with large dictionaries
   Solution: Consider using generators for large datasets or use specialized libraries like pandas for very large data structures.

4. Issue: Difficulty in serializing dictionaries with complex objects
   Solution: Implement custom serialization methods or use libraries like pickle or json with custom encoders/decoders.

5. Issue: Thread-safety issues with shared dictionaries
   Solution: Use threading.Lock for synchronization or consider using concurrent.futures.ThreadPoolExecutor for parallel dictionary operations.
"""

def demonstrate_troubleshooting():
    """Demonstrate solutions to common dictionary-related issues."""
    # 1. Safely getting a value
    d = {"a": 1, "b": 2}
    value = d.get("c", "Not found")
    print(f"1. Safe get: {value}")

    # 2. Using immutable keys
    d = {(1, 2): "value"}  # Tuple as a key
    print(f"2. Dictionary with tuple key: {d}")

    # 3. Memory-efficient large dictionary operations
    def process_large_dict():
        large_dict = {i: i**2 for i in range(10**6)}
        # Instead of storing all values, we use a generator
        result = (value for key, value in large_dict.items() if key % 10000 == 0)
        return list(result)

    print(f"3. Efficient large dict processing: {process_large_dict()[:5]}...")

    # 4. Custom serialization
    import json
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def point_encoder(obj):
        if isinstance(obj, Point):
            return {"x": obj.x, "y": obj.y}
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    point_dict = {"origin": Point(0, 0), "end": Point(5, 5)}
    json_str = json.dumps(point_dict, default=point_encoder)
    print(f"4. Custom serialization: {json_str}")

    # 5. Thread-safe dictionary operations
    import threading

    class ThreadSafeDict:
        def __init__(self):
            self._dict = {}
            self._lock = threading.Lock()

        def set(self, key, value):
            with self._lock:
                self._dict[key] = value

        def get(self, key, default=None):
            with self._lock:
                return self._dict.get(key, default)

    safe_dict = ThreadSafeDict()
    safe_dict.set("key", "value")
    print(f"5. Thread-safe get: {safe_dict.get('key')}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. collections: Provides specialized container datatypes including OrderedDict, defaultdict, and Counter.
2. typing: Offers support for type hints, including Dict and TypedDict.
3. json: Built-in module for JSON encoding and decoding, often used with dictionaries.
4. pickle: Module for serializing and deserializing Python object structures, including dictionaries.
5. pandas: Data manipulation library with DataFrame, which can be thought of as a more powerful dictionary-like structure.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (chapters on data structures)
- "Fluent Python" by Luciano Ramalho (chapters on dictionaries and sets)
- Python's official documentation on dictionaries: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Real Python's guide on Python dictionaries: https://realpython.com/python-dicts/
- Raymond Hettinger's talks on Python's dictionary implementation (available on YouTube)
- PEP 468 - Preserving the order of **kwargs in a function: https://www.python.org/dev/peps/pep-0468/

8. Performance Analysis and Optimization
----------------------------------------
When working with dictionaries, especially large ones, performance considerations are crucial. Here we'll analyze and compare different dictionary operations and provide optimization strategies.
"""

import timeit
import sys

def performance_comparison():
    """Compare performance of different dictionary operations."""
    
    # Setup
    small_dict = {i: i for i in range(100)}
    large_dict = {i: i for i in range(100000)}
    
    # 1. Dictionary lookup vs list search
    def dict_lookup():
        return 99 in small_dict
    
    def list_search():
        return 99 in list(small_dict.keys())
    
    dict_time = timeit.timeit(dict_lookup, number=100000)
    list_time = timeit.timeit(list_search, number=100000)
    
    print(f"1. Lookup - Dict: {dict_time:.6f}s, List: {list_time:.6f}s")
    
    # 2. Dict comprehension vs loop
    def dict_comp():
        return {i: i**2 for i in range(1000)}
    
    def dict_loop():
        d = {}
        for i in range(1000):
            d[i] = i**2
        return d
    
    comp_time = timeit.timeit(dict_comp, number=1000)
    loop_time = timeit.timeit(dict_loop, number=1000)
    
    print(f"2. Creation - Comprehension: {comp_time:.6f}s, Loop: {loop_time:.6f}s")
    
    # 3. OrderedDict vs dict (Python 3.7+)
    def ordered_dict_ops():
        od = OrderedDict()
        for i in range(1000):
            od[i] = i
        od.popitem()
        od.popitem(last=False)
    
    def regular_dict_ops():
        d = {}
        for i in range(1000):
            d[i] = i
        d.popitem()
        d.pop(next(iter(d)))
    
    ordered_time = timeit.timeit(ordered_dict_ops, number=1000)
    regular_time = timeit.timeit(regular_dict_ops, number=1000)
    
    print(f"3. OrderedDict vs dict - OrderedDict: {ordered_time:.6f}s, dict: {regular_time:.6f}s")

def memory_usage_analysis():
    """Analyze memory usage of different dictionary implementations."""
    
    # Regular dict
    regular_dict = {i: i for i in range(10000)}
    regular_size = sys.getsizeof(regular_dict)
    
    # OrderedDict
    ordered_dict = OrderedDict((i, i) for i in range(10000))
    ordered_size = sys.getsizeof(ordered_dict)
    
    # defaultdict
    default_dict = defaultdict(int)
    for i in range(10000):
        default_dict[i] = i
    default_size = sys.getsizeof(default_dict)
    
    print(f"Memory usage:")
    print(f"1. Regular dict: {regular_size / 1024:.2f} KB")
    print(f"2. OrderedDict: {ordered_size / 1024:.2f} KB")
    print(f"3. defaultdict: {default_size / 1024:.2f} KB")

"""
Optimization Strategies:
1. Use dictionary comprehensions for creating dictionaries when possible.
2. Prefer 'key in dict' over 'key in dict.keys()' for membership testing.
3. Use dict.setdefault() or defaultdict for setting default values.
4. For frequent removals and insertions with order preservation, consider using an OrderedDict.
5. Use collections.Counter for counting hashable objects efficiently.
6. For large dictionaries, consider using generators or itertools for memory-efficient operations.
7. Use the 'key' parameter in sorting functions instead of creating temporary lists.

Example of optimizing a frequently called method:
"""

def optimize_frequent_operation(data: Dict[str, List[int]]) -> Dict[str, int]:
    """
    Optimize the operation of summing values for each key in a dictionary.
    
    Args:
    data (Dict[str, List[int]]): Input dictionary with string keys and list of integers as values
    
    Returns:
    Dict[str, int]: Dictionary with the sum of values for each key
    """
    # Unoptimized version
    # return {key: sum(values) for key, values in data.items()}
    
    # Optimized version
    return {key: sum(values) for key, values in data.items()}

def demonstrate_optimization():
    """Demonstrate optimization of a frequently called dictionary operation."""
    data = {
        "A": [1, 2, 3, 4, 5],
        "B": [10, 20, 30, 40, 50],
        "C": [100, 200, 300, 400, 500]
    }
    
    def unoptimized():
        return {key: sum(values) for key, values in data.items()}
    
    def optimized():
        return optimize_frequent_operation(data)
    
    unopt_time = timeit.timeit(unoptimized, number=100000)
    opt_time = timeit.timeit(optimized, number=100000)
    
    print("Dictionary operation optimization:")
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
- Relevance to the main topic of dictionaries and OrderedDict in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to dictionaries and OrderedDict.
    """
    print("1. Basic Dictionary Operations:")
    basic_dictionary_operations()
    
    print("\n2. Advanced Dictionary Operations:")
    dictionary_advanced_operations()
    
    print("\n3. OrderedDict Operations:")
    ordered_dict_operations()
    
    print("\n4. Dictionary Variants:")
    dictionary_variants()
    
    print("\n5. Best Practices and Advanced Tips:")
    demonstrate_best_practices()
    
    print("\n6. Advanced Techniques:")
    demonstrate_advanced_techniques()
    
    print("\n7. Real-World Application - Simple Cache:")
    demonstrate_cache_usage()
    
    print("\n8. Type Hinting with Dictionaries:")
    demonstrate_type_hinting()
    
    print("\n9. Concurrent Dictionary Operations:")
    asyncio.run(concurrent_dict_operations())
    
    print("\n10. Troubleshooting:")
    demonstrate_troubleshooting()
    
    print("\n11. Performance Comparison:")
    performance_comparison()
    
    print("\n12. Memory Usage Analysis:")
    memory_usage_analysis()
    
    print("\n13. Optimization Demonstration:")
    demonstrate_optimization()

if __name__ == "__main__":
    main()