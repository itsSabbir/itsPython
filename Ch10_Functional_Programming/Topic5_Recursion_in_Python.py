"""
Functional Programming - Recursion in Python - in the Python Programming Language
=================================================================================

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
Recursion is a fundamental concept in functional programming where a function calls itself to solve a problem by breaking it down into smaller, more manageable subproblems. This approach is based on the principle of mathematical induction and is particularly useful for solving problems with a recursive structure.

Historical context:
- The concept of recursion in computer science dates back to the 1950s, with early work by Stephen Kleene on recursive functions.
- Recursion became a cornerstone of functional programming languages like Lisp (1958) and Haskell (1990).
- Python has supported recursion since its inception in 1991, drawing inspiration from functional programming paradigms.

Significance:
- Recursion provides an elegant and concise way to express solutions to complex problems.
- It is fundamental to many algorithms and data structures, such as tree traversal and divide-and-conquer algorithms.
- Recursion often leads to more readable and maintainable code for problems with a naturally recursive structure.

Common use cases:
- Traversing tree-like data structures (e.g., file systems, XML parsing)
- Implementing divide-and-conquer algorithms (e.g., quicksort, merge sort)
- Solving mathematical problems (e.g., factorial, Fibonacci sequence)
- Backtracking algorithms (e.g., solving Sudoku, generating permutations)

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from typing import List, Any, Optional
import sys

# Increase recursion limit for demonstration purposes
sys.setrecursionlimit(10000)

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    Args:
    n (int): The non-negative integer to calculate the factorial for.
    
    Returns:
    int: The factorial of n.
    
    This function demonstrates a simple recursive implementation.
    It includes a base case (n == 0) and a recursive case (n > 0).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
    n (int): The index of the Fibonacci number to calculate (0-based).
    
    Returns:
    int: The nth Fibonacci number.
    
    This function demonstrates a naive recursive implementation of the Fibonacci sequence.
    It's inefficient for large n due to redundant calculations.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def binary_search(arr: List[int], target: int, low: int = 0, high: Optional[int] = None) -> Optional[int]:
    """
    Perform a binary search on a sorted array using recursion.
    
    Args:
    arr (List[int]): The sorted array to search in.
    target (int): The value to search for.
    low (int): The lower bound of the search range (inclusive).
    high (Optional[int]): The upper bound of the search range (inclusive).
    
    Returns:
    Optional[int]: The index of the target if found, None otherwise.
    
    This function demonstrates a recursive implementation of binary search,
    which is more efficient than linear search for sorted arrays.
    """
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return None
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

def quicksort(arr: List[int]) -> List[int]:
    """
    Sort an array using the quicksort algorithm (recursive implementation).
    
    Args:
    arr (List[int]): The array to be sorted.
    
    Returns:
    List[int]: The sorted array.
    
    This function demonstrates a recursive implementation of the quicksort algorithm,
    which is an efficient, divide-and-conquer sorting method.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def traverse_directory(path: str, depth: int = 0) -> None:
    """
    Recursively traverse and print the contents of a directory.
    
    Args:
    path (str): The path of the directory to traverse.
    depth (int): The current depth in the directory tree (for indentation).
    
    This function demonstrates how recursion can be used to traverse
    tree-like structures such as file systems.
    """
    import os
    
    print('  ' * depth + os.path.basename(path))
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            traverse_directory(item_path, depth + 1)

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Always define a base case to prevent infinite recursion.
2. Ensure that each recursive call moves towards the base case.
3. Use tail recursion when possible for better performance and to avoid stack overflow.
4. Consider using memoization or dynamic programming for recursive problems with overlapping subproblems.
5. Be mindful of the recursion depth limit in Python (default is 1000).

Common Pitfalls:
1. Forgetting to include a base case, leading to infinite recursion.
2. Inefficient implementations that lead to excessive function calls (e.g., naive Fibonacci).
3. Stack overflow errors due to deep recursion.
4. Unnecessary use of recursion for problems better solved iteratively.

Advanced Tips:
1. Use the @functools.lru_cache decorator for automatic memoization of recursive functions.
2. Implement tail recursion optimization manually in Python (as it doesn't support it natively).
3. Use recursion with generators for memory-efficient processing of large data structures.
4. Employ mutual recursion for certain types of problems (e.g., even/odd number checker).
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    
    This function demonstrates the use of the @lru_cache decorator for automatic memoization,
    significantly improving performance for large n compared to the naive recursive approach.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

def tail_recursive_factorial(n: int, accumulator: int = 1) -> int:
    """
    Calculate factorial using tail recursion.
    
    This function demonstrates a tail-recursive implementation of factorial.
    While Python doesn't optimize tail recursion automatically, this pattern
    can be more easily transformed into an iterative solution if needed.
    """
    if n == 0:
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, n * accumulator)

def recursive_generator(data: List[Any]) -> Any:
    """
    A recursive generator function for processing nested lists.
    
    This function demonstrates how recursion can be combined with generators
    for memory-efficient processing of nested data structures.
    """
    for item in data:
        if isinstance(item, list):
            yield from recursive_generator(item)
        else:
            yield item

"""
4. Integration and Real-World Applications
------------------------------------------
Recursion is widely used in various domains and applications:

1. Parsing and processing hierarchical data (e.g., XML, JSON)
2. Implementing algorithms in graph theory (e.g., depth-first search)
3. Natural language processing (e.g., parsing context-free grammars)
4. Computer graphics (e.g., fractal generation, ray tracing)

Real-world example: JSON Parser
"""

import json
from typing import Union, Dict, List

JsonValue = Union[Dict[str, 'JsonValue'], List['JsonValue'], str, int, float, bool, None]

def parse_json(data: str) -> JsonValue:
    """
    A simplified recursive JSON parser.
    
    This function demonstrates a real-world application of recursion
    in parsing hierarchical data structures like JSON.
    
    Note: This is a simplified implementation for demonstration purposes.
    In practice, use the built-in json module for robust JSON parsing.
    """
    def parse_value(s: str) -> tuple[JsonValue, str]:
        s = s.strip()
        if s.startswith('{'):
            return parse_object(s)
        elif s.startswith('['):
            return parse_array(s)
        elif s.startswith('"'):
            return parse_string(s)
        elif s.startswith(('true', 'false', 'null')):
            return parse_constant(s)
        else:
            return parse_number(s)
    
    def parse_object(s: str) -> tuple[Dict[str, JsonValue], str]:
        obj: Dict[str, JsonValue] = {}
        s = s[1:].lstrip()  # Remove opening '{'
        while not s.startswith('}'):
            key, s = parse_string(s)
            s = s.lstrip()[1:].lstrip()  # Remove ':'
            value, s = parse_value(s)
            obj[key] = value
            s = s.lstrip()
            if s.startswith(','):
                s = s[1:].lstrip()
        return obj, s[1:]  # Remove closing '}'
    
    def parse_array(s: str) -> tuple[List[JsonValue], str]:
        arr: List[JsonValue] = []
        s = s[1:].lstrip()  # Remove opening '['
        while not s.startswith(']'):
            value, s = parse_value(s)
            arr.append(value)
            s = s.lstrip()
            if s.startswith(','):
                s = s[1:].lstrip()
        return arr, s[1:]  # Remove closing ']'
    
    def parse_string(s: str) -> tuple[str, str]:
        end = s.index('"', 1)
        return s[1:end], s[end+1:]
    
    def parse_number(s: str) -> tuple[Union[int, float], str]:
        end = next(i for i, c in enumerate(s) if c in ',]}')
        num_str = s[:end]
        return int(num_str) if '.' not in num_str else float(num_str), s[end:]
    
    def parse_constant(s: str) -> tuple[Union[bool, None], str]:
        if s.startswith('true'):
            return True, s[4:]
        elif s.startswith('false'):
            return False, s[5:]
        else:  # null
            return None, s[4:]
    
    return parse_value(data)[0]

def demonstrate_json_parser():
    """Demonstrate the recursive JSON parser."""
    json_data = '{"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "swimming"]}'
    parsed_data = parse_json(json_data)
    print("Parsed JSON data:", parsed_data)
    
    # Verify with built-in json module
    assert parsed_data == json.loads(json_data), "Custom parser output doesn't match json.loads()"
    print("Custom parser output matches json.loads() output.")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Trampolining: A technique to implement tail-call optimization in languages that don't support it natively.
2. Continuation-passing style (CPS): A programming style where control is passed explicitly in the form of a continuation.
3. Recursion schemes: Abstract recursion patterns for processing recursive data structures.
4. Corecursion and stream processing: Generating potentially infinite data structures using recursive definitions.
"""

from typing import Callable, TypeVar

T = TypeVar('T')

def trampoline(f: Callable[..., Union[T, Callable[[], Union[T, Callable]]]]) -> Callable[..., T]:
    """
    A trampoline function for implementing tail-call optimization.
    
    This function demonstrates an advanced technique to avoid stack overflow
    in deeply recursive functions by turning recursion into iteration.
    """
    def wrapped(*args, **kwargs):
        result = f(*args, **kwargs)
        while callable(result):
            result = result()
        return result
    return wrapped

@trampoline
def factorial_trampoline(n: int, acc: int = 1) -> Union[int, Callable[[], Union[int, Callable]]]:
    """
    A tail-recursive factorial function using trampolining.
    
    This function demonstrates how to use the trampoline technique
    to implement a deeply recursive function without stack overflow.
    """
    if n == 0:
        return acc
    else:
        return lambda: factorial_trampoline(n - 1, n * acc)

def demonstrate_advanced_concepts():
    """Demonstrate advanced recursion concepts."""
    # Trampolining example
    print("Factorial of 1000 using trampolining:", factorial_trampoline(1000))
    
    # Corecursion example: generating Fibonacci sequence
    def fibonacci_stream():
        def fib(a, b):
            yield a
            yield from fib(b, a + b)
    
    fib_gen = fibonacci_stream()
    print("First 10 Fibonacci numbers using corecursion:", [next(fib_gen) for _ in range(10)])

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use recursion instead of iteration?
A: Use recursion when the problem has a naturally recursive structure and the solution is clearer and more concise than an iterative approach. Examples include tree traversal and divide-and-conquer algorithms.

Q: How can I avoid stack overflow errors in recursive functions?
A: 1. Use tail recursion when possible.
   2. Implement techniques like trampolining or convert to an iterative solution for very deep recursion.
   3. Use memoization to avoid redundant calculations and reduce call stack depth.
   4. Increase the recursion limit using sys.setrecursionlimit() (use with caution).

Q: How do I debug recursive functions effectively?
A: 1. Use print statements or logging to track the current state and arguments in each recursive call.
   2. Utilize a debugger to step through the recursive calls and inspect the call stack.
   3. Start with small, simple inputs and gradually increase complexity.

Troubleshooting:
1. If you're getting a RecursionError, check for proper base cases and ensure progress towards them.
2. For poor performance in recursive solutions, look for overlapping subproblems and consider memoization or dynamic programming.
3. If facing issues with mutating data structures, consider using immutable data or passing copies to avoid unintended side effects.
"""

def troubleshooting_examples():
    """Demonstrate solutions to common recursion issues."""
    
    # Example 1: Fixing a stack overflow error
    def sum_to_n_bad(n: int) -> int:
        """Incorrect implementation that causes stack overflow for large n."""
        return n + sum_to_n_bad(n - 1)  # Missing base case
    
    def sum_to_n_good(n: int) -> int:
        """Correct implementation with base case."""
        if n == 0:
            return 0
        return n + sum_to_n_good(n - 1)
    
    # Example 2: Improving performance with memoization
    def fib_slow(n: int) -> int:
        """Slow fibonacci implementation without memoization."""
        if n <= 1:
            return n
        return fib_slow(n - 1) + fib_slow(n - 2)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fib_fast(n: int) -> int:
        """Fast fibonacci implementation with memoization."""
        if n <= 1:
            return n
        return fib_fast(n - 1) + fib_fast(n - 2)
    
    # Example 3: Avoiding unintended mutations
    def append_to_list_bad(lst: List[int], n: int) -> List[int]:
        """Incorrect implementation that mutates the input list."""
        lst.append(n)
        return lst
    
    def append_to_list_good(lst: List[int], n: int) -> List[int]:
        """Correct implementation that creates a new list."""
        return lst + [n]
    
    # Demonstrate the examples
    print("Example 1: Fixing stack overflow")
    try:
        sum_to_n_bad(1000)
    except RecursionError:
        print("sum_to_n_bad causes RecursionError")
    print("sum_to_n_good result:", sum_to_n_good(1000))
    
    print("\nExample 2: Improving performance")
    import time
    
    start = time.time()
    fib_slow(30)
    print(f"fib_slow took {time.time() - start:.4f} seconds")
    
    start = time.time()
    fib_fast(30)
    print(f"fib_fast took {time.time() - start:.4f} seconds")
    
    print("\nExample 3: Avoiding unintended mutations")
    original = [1, 2, 3]
    mutated = append_to_list_bad(original, 4)
    print("Original list after append_to_list_bad:", original)
    
    original = [1, 2, 3]
    new_list = append_to_list_good(original, 4)
    print("Original list after append_to_list_good:", original)
    print("New list after append_to_list_good:", new_list)

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. functools: Built-in Python module with tools like lru_cache for memoization.
2. sys: For controlling recursion depth limit with sys.setrecursionlimit().
3. inspect: For introspection of the call stack in recursive functions.
4. graphviz: For visualizing recursive call trees (useful for understanding and debugging).

Resources:
- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein (Chapters on Recursion and Dynamic Programming)
- "Structure and Interpretation of Computer Programs" by Abelson and Sussman (Chapter on Recursion and Tree Recursion)
- Python's official documentation on recursive functions: https://docs.python.org/3/faq/programming.html#how-do-i-write-a-recursive-function
- Real Python's guide on recursion: https://realpython.com/python-thinking-recursively/
- "Recursive Book of Recursion" by Al Sweigart

8. Performance Analysis and Optimization
----------------------------------------
When working with recursive functions, it's crucial to understand their performance characteristics and how to optimize them for efficiency.
"""

import timeit
from typing import Callable

def performance_comparison(func: Callable, *args, number: int = 1000):
    """
    Compare the performance of different implementations of the same function.
    
    Args:
    func (Callable): The function to test.
    *args: Arguments to pass to the function.
    number (int): Number of times to run the test.
    
    Returns:
    float: The average execution time per call in seconds.
    """
    total_time = timeit.timeit(lambda: func(*args), number=number)
    return total_time / number

def analyze_recursion_performance():
    """Analyze and compare performance of recursive vs. iterative implementations."""
    
    def factorial_recursive(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial_recursive(n - 1)
    
    def factorial_iterative(n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    n = 500  # Be cautious with larger values due to recursion depth limit
    
    recursive_time = performance_comparison(factorial_recursive, n)
    iterative_time = performance_comparison(factorial_iterative, n)
    
    print(f"Factorial of {n}:")
    print(f"Recursive implementation: {recursive_time:.6f} seconds per call")
    print(f"Iterative implementation: {iterative_time:.6f} seconds per call")
    print(f"Recursive is {recursive_time / iterative_time:.2f}x slower than iterative")

    # Memoized recursive implementation
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def factorial_memoized(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial_memoized(n - 1)
    
    memoized_time = performance_comparison(factorial_memoized, n)
    print(f"Memoized recursive implementation: {memoized_time:.6f} seconds per call")
    print(f"Memoized is {memoized_time / iterative_time:.2f}x slower than iterative")

"""
Performance Considerations:
1. Recursive functions often have higher memory usage due to the call stack.
2. Simple recursive implementations can be slower than their iterative counterparts.
3. The depth of recursion is limited by Python's maximum recursion depth.
4. Recursive solutions with overlapping subproblems can be extremely inefficient without optimization.

Optimization Strategies:
1. Use memoization or dynamic programming to avoid redundant calculations.
2. Convert tail-recursive functions to iterative implementations for better performance.
3. Use generator functions for memory-efficient processing of recursive structures.
4. Implement trampolining for deeply recursive functions to avoid stack overflow.
"""

def optimize_recursion_example():
    """Demonstrate optimization techniques for recursive functions."""
    
    def fibonacci_naive(n: int) -> int:
        if n <= 1:
            return n
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
    
    @lru_cache(maxsize=None)
    def fibonacci_memoized(n: int) -> int:
        if n <= 1:
            return n
        return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    
    def fibonacci_iterative(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    n = 30
    
    print(f"Computing Fibonacci({n}):")
    
    naive_time = performance_comparison(fibonacci_naive, n, number=10)
    print(f"Naive recursive: {naive_time:.6f} seconds per call")
    
    memoized_time = performance_comparison(fibonacci_memoized, n)
    print(f"Memoized recursive: {memoized_time:.6f} seconds per call")
    
    iterative_time = performance_comparison(fibonacci_iterative, n)
    print(f"Iterative: {iterative_time:.6f} seconds per call")
    
    print(f"Memoized is {naive_time / memoized_time:.2f}x faster than naive")
    print(f"Iterative is {naive_time / iterative_time:.2f}x faster than naive")

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
- Relevance to the main topic of recursion in Python's functional programming paradigm.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to recursion in Python.
    """
    print("Basic Recursion Examples:")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Fibonacci of 7: {fibonacci(7)}")
    print(f"Binary search for 5 in [1, 3, 5, 7, 9]: {binary_search([1, 3, 5, 7, 9], 5)}")
    print(f"Quicksort [3, 6, 8, 10, 1, 2, 1]: {quicksort([3, 6, 8, 10, 1, 2, 1])}")
    
    print("\nAdvanced Recursion Techniques:")
    print(f"Fibonacci of 100 (memoized): {fibonacci_memoized(100)}")
    print(f"Factorial of 5 (tail recursive): {tail_recursive_factorial(5)}")
    print("Recursive generator example:", list(recursive_generator([1, [2, 3], [4, [5, 6]]])))
    
    print("\nReal-World Application: JSON Parsing")
    demonstrate_json_parser()
    
    print("\nAdvanced Concepts:")
    demonstrate_advanced_concepts()
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Analysis:")
    analyze_recursion_performance()
    
    print("\nOptimization Example:")
    optimize_recursion_example()

if __name__ == "__main__":
    main()