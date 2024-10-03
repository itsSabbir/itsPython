"""
Functional Programming - Higher-order functions - in the Python Programming Language
====================================================================================

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
Higher-order functions are a fundamental concept in functional programming, allowing functions to be treated as first-class citizens. They can accept other functions as arguments or return functions as results, enabling powerful abstractions and code reuse.

Historical context:
- The concept of higher-order functions originates from lambda calculus, developed by Alonzo Church in the 1930s.
- Lisp, created by John McCarthy in 1958, was one of the first programming languages to implement higher-order functions.
- Python has supported higher-order functions since its inception in 1991, with enhancements over time.

Significance:
- Higher-order functions promote code reusability and modularity.
- They enable the creation of more abstract and generic code.
- Higher-order functions are essential for implementing many functional programming patterns.

Common use cases:
- Data transformation and filtering (map, filter, reduce)
- Callback functions in asynchronous programming
- Decorators for modifying or enhancing function behavior
- Creating domain-specific languages (DSLs)

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from typing import Callable, List, Any
import time
import functools

def main():
    """
    Main function to demonstrate various aspects of higher-order functions in Python.
    """
    print("1. Basic Higher-Order Function")
    numbers = [1, 2, 3, 4, 5]
    squared = map(lambda x: x**2, numbers)
    print(list(squared))

    print("\n2. Custom Higher-Order Function")
    def apply_operation(func: Callable[[int], int], value: int) -> int:
        return func(value)

    double = lambda x: x * 2
    print(apply_operation(double, 5))

    print("\n3. Returning Functions")
    def create_multiplier(factor: int) -> Callable[[int], int]:
        def multiplier(x: int) -> int:
            return x * factor
        return multiplier

    triple = create_multiplier(3)
    print(triple(4))

    print("\n4. Decorators")
    @timing_decorator
    def slow_function():
        time.sleep(1)
        print("Function executed")

    slow_function()

    print("\n5. Higher-Order Functions with Closures")
    counter = create_counter()
    print(counter())  # 1
    print(counter())  # 2

    print("\n6. Partial Function Application")
    from functools import partial
    base_two_log = partial(log, base=2)
    print(base_two_log(8))  # 3.0

    print("\n7. Function Composition")
    composed = compose(lambda x: x * 2, lambda x: x + 1)
    print(composed(3))  # 8

    print("\n8. Advanced Example: Data Pipeline")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = data_pipeline(data)
    print(result)

def timing_decorator(func: Callable) -> Callable:
    """
    A decorator that measures and prints the execution time of a function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with timing functionality.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

def create_counter() -> Callable[[], int]:
    """
    Creates a counter function using a closure.

    Returns:
        Callable[[], int]: A function that returns the next count when called.
    """
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def log(x: float, base: float = math.e) -> float:
    """
    Calculates the logarithm of x with the given base.

    Args:
        x (float): The value to calculate the logarithm for.
        base (float, optional): The base of the logarithm. Defaults to math.e.

    Returns:
        float: The logarithm of x with the given base.
    """
    return math.log(x, base)

def compose(*funcs: Callable) -> Callable:
    """
    Composes multiple functions into a single function.

    Args:
        *funcs (Callable): Functions to be composed.

    Returns:
        Callable: A new function that applies all the given functions in reverse order.
    """
    def composed_func(x):
        for func in reversed(funcs):
            x = func(x)
        return x
    return composed_func

def data_pipeline(data: List[int]) -> List[int]:
    """
    A data processing pipeline using higher-order functions.

    Args:
        data (List[int]): The input data to process.

    Returns:
        List[int]: The processed data.
    """
    # Filter even numbers
    even_numbers = filter(lambda x: x % 2 == 0, data)
    
    # Square the numbers
    squared = map(lambda x: x**2, even_numbers)
    
    # Sum the squared values
    total = functools.reduce(lambda x, y: x + y, squared)
    
    return total

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------

Best Practices:
1. Keep functions pure (no side effects) when possible.
2. Use type hints to improve code readability and catch potential errors.
3. Prefer built-in functions (map, filter, reduce) for simple operations.
4. Use meaningful names for functions and their parameters.
5. Document higher-order functions clearly, especially their expected inputs and outputs.

Common Pitfalls:
1. Overusing lambda functions, leading to reduced readability.
2. Neglecting to handle edge cases in higher-order functions.
3. Creating overly complex function compositions that are hard to understand and maintain.
4. Misusing closures, leading to unexpected variable bindings.

Advanced Tips:
1. Use functools.partial for partial function application.
2. Implement the @functools.wraps decorator when creating decorators to preserve metadata.
3. Utilize the operator module for common operations in functional programming.
4. Consider using toolz or fn.py libraries for advanced functional programming constructs.

Performance Considerations:
1. Be aware that excessive function calls can impact performance.
2. Use generator expressions instead of list comprehensions for large datasets.
3. Consider using `map()` and `filter()` instead of list comprehensions for simple operations.
4. Profile your code to identify performance bottlenecks in complex function compositions.

Edge Cases:
1. Handle potential exceptions in higher-order functions, especially when working with user-defined functions.
2. Be cautious with recursion in higher-order functions to avoid stack overflow.
3. Consider the implications of mutable default arguments in higher-order functions.

Testing:
Here's an example of how to write unit tests for higher-order functions:
"""

import unittest

class TestHigherOrderFunctions(unittest.TestCase):
    def test_apply_operation(self):
        self.assertEqual(apply_operation(lambda x: x * 2, 5), 10)
        self.assertEqual(apply_operation(lambda x: x + 1, 5), 6)

    def test_create_multiplier(self):
        double = create_multiplier(2)
        triple = create_multiplier(3)
        self.assertEqual(double(5), 10)
        self.assertEqual(triple(5), 15)

    def test_compose(self):
        add_one = lambda x: x + 1
        double = lambda x: x * 2
        composed = compose(double, add_one)
        self.assertEqual(composed(3), 8)

# Uncomment the following lines to run the tests
# if __name__ == '__main__':
#     unittest.main()

"""
4. Integration and Real-World Applications
------------------------------------------

1. Web Frameworks:
   Higher-order functions are used extensively in web frameworks like Django and Flask for defining routes, middleware, and request handlers.

2. Data Processing:
   Libraries like Pandas use higher-order functions for data transformation and analysis operations.

3. Asynchronous Programming:
   Callback functions in asyncio and other asynchronous libraries are often implemented using higher-order functions.

4. Machine Learning:
   Scikit-learn uses higher-order functions for implementing custom estimators and transformers.

5. GUI Programming:
   Event handlers in GUI frameworks often utilize higher-order functions for callback mechanisms.

Example: Using higher-order functions in a data processing scenario
"""

import pandas as pd

def process_dataframe(df: pd.DataFrame, operations: List[Callable[[pd.DataFrame], pd.DataFrame]]) -> pd.DataFrame:
    """
    Applies a series of operations to a DataFrame using higher-order functions.

    Args:
        df (pd.DataFrame): The input DataFrame.
        operations (List[Callable[[pd.DataFrame], pd.DataFrame]]): A list of functions to apply to the DataFrame.

    Returns:
        pd.DataFrame: The processed DataFrame.
    """
    return functools.reduce(lambda acc, func: func(acc), operations, df)

# Example usage
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# operations = [
#     lambda df: df.assign(C=df['A'] + df['B']),
#     lambda df: df[df['C'] > 5],
#     lambda df: df.sort_values('C', ascending=False)
# ]
# result = process_dataframe(df, operations)
# print(result)

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------

1. Functional Reactive Programming (FRP):
   Combining higher-order functions with reactive programming paradigms for handling asynchronous data streams.

2. Effect Systems:
   Exploring ways to track and manage side effects in functional programming using higher-order functions and type systems.

3. Dependent Types:
   Investigating the use of dependent types in conjunction with higher-order functions for more expressive and safer code.

4. Algebraic Effects:
   Studying the application of algebraic effects and handlers as an alternative to monads for managing computational effects.

5. Quantum Computing:
   Exploring the use of higher-order functions in quantum computing algorithms and simulations.

Example: Implementing a simple effect system using higher-order functions
"""

from typing import TypeVar, Callable

T = TypeVar('T')
Effect = Callable[[], T]

def pure(value: T) -> Effect[T]:
    return lambda: value

def bind(effect: Effect[T], func: Callable[[T], Effect[Any]]) -> Effect[Any]:
    return lambda: func(effect())()

def run_effect(effect: Effect[T]) -> T:
    return effect()

# Example usage
# def get_user_input() -> Effect[str]:
#     return lambda: input("Enter your name: ")

# def greet(name: str) -> Effect[None]:
#     return lambda: print(f"Hello, {name}!")

# effect = bind(get_user_input(), greet)
# run_effect(effect)

"""
6. FAQs and Troubleshooting
---------------------------

Q: What's the difference between map() and list comprehension?
A: map() returns an iterator and is generally more memory-efficient for large datasets,
   while list comprehensions are often more readable for simple operations.

Q: How can I debug higher-order functions effectively?
A: Use logging, add print statements inside the functions, and utilize debugging tools
   that support stepping through function calls.

Q: Are there any performance concerns when using higher-order functions?
A: While higher-order functions can introduce some overhead due to function calls,
   the impact is usually negligible. Profile your code for performance-critical sections.

Q: How do I handle exceptions in higher-order functions?
A: Wrap the function call in a try-except block within the higher-order function,
   or consider using the `functools.wraps` decorator to preserve the original function's metadata.

Troubleshooting Guide:
1. Unexpected results from higher-order functions:
   - Check the input and output types of the functions being passed.
   - Verify that the functions are pure and don't have unintended side effects.

2. Performance issues with large datasets:
   - Consider using generator expressions or itertools for lazy evaluation.
   - Profile the code to identify bottlenecks and optimize accordingly.

3. Difficulty in understanding complex function compositions:
   - Break down the composition into smaller, named functions for clarity.
   - Add type hints and docstrings to improve readability and maintainability.

4. Issues with variable scope in closures:
   - Be mindful of the closure's scope and use the `nonlocal` keyword when necessary.
   - Consider using classes or partial function application as alternatives.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------

Tools and Libraries:
1. functools: Built-in module for higher-order functions and tools for functional programming
2. itertools: Module for efficient looping and iteration
3. operator: Module providing efficient alternatives to simple lambda functions
4. toolz: Library for functional programming
5. fn.py: Library for functional programming in Python

Resources:
1. "Functional Programming in Python" by David Mertz
2. "Python Functional Programming Cookbook" by Steven F. Lott
3. "Functional Python Programming" by Steven F. Lott
4. PEP 3107 - Function Annotations: https://www.python.org/dev/peps/pep-3107/
5. "Functional Programming HOWTO" in Python documentation: https://docs.python.org/3/howto/functional.html

8. Performance Analysis and Optimization
----------------------------------------

Profiling higher-order functions:
Use the `cProfile` module or the `line_profiler` package to identify performance bottlenecks.

Example of profiling a higher-order function:
"""

import cProfile

def profile_higher_order_function():
    data = list(range(1000000))
    result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))

cProfile.run('profile_higher_order_function()')

"""
Optimization strategies:
1. Use built-in functions and operators instead of lambda functions when possible
2. Leverage itertools for efficient iteration and combination of iterables
3. Consider using NumPy for numerical operations on large datasets
4. Use `functools.lru_cache` for memoization of expensive function calls

Example of optimizing a higher-order function:
"""

from functools import lru_cache
import operator

@lru_cache(maxsize=None)
def expensive_calculation(x: int) -> int:
    # Simulate an expensive calculation
    return x**3

def optimized_higher_order_function(data: List[int]) -> List[int]:
    return list(map(expensive_calculation, filter(lambda x: x % 2 == 0, data)))

# Usage
# result = optimized_higher_order_function(list(range(1000000)))

"""
9. How to Contribute (continued)
--------------------

Remember, the goal is to keep this note sheet as an authoritative and up-to-date resource for Python developers of all skill levels.

- When adding new examples, ensure they demonstrate practical applications of higher-order functions.
- If discussing advanced topics, provide sufficient context and explanations for less experienced developers.
- When referencing external resources, prefer well-established and maintained sources.
- Consider adding exercises or challenges to help readers practice the concepts.

Conclusion
----------
Higher-order functions are a powerful tool in Python's functional programming arsenal. They enable developers to write more abstract, reusable, and expressive code. By mastering higher-order functions, you can create more elegant solutions to complex problems and improve the overall design of your software.

As Python continues to evolve, the importance of functional programming concepts like higher-order functions is likely to grow. Stay informed about new developments in the Python community, and don't hesitate to experiment with innovative uses of higher-order functions in your projects.

Thank you for using this expert-level note sheet on higher-order functions in Python. Happy coding!
"""

# Additional examples and advanced concepts

from typing import List, Callable, TypeVar, Generic

T = TypeVar('T')
R = TypeVar('R')

class Functor(Generic[T]):
    """
    A simple implementation of a Functor, demonstrating advanced use of higher-order functions.
    """
    def __init__(self, value: T):
        self.value = value

    def map(self, func: Callable[[T], R]) -> 'Functor[R]':
        return Functor(func(self.value))

def compose(*funcs: Callable) -> Callable:
    """
    A more advanced function composition utility.
    """
    def composition(x):
        for func in reversed(funcs):
            x = func(x)
        return x
    return composition

def curry(func: Callable) -> Callable:
    """
    A simple currying implementation using higher-order functions.
    """
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*(args + more_args))
    return curried

def memoize(func: Callable) -> Callable:
    """
    A memoization decorator using higher-order functions.
    """
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized

def pipeline(*funcs: Callable) -> Callable:
    """
    Creates a pipeline of functions using higher-order functions.
    """
    def pipe(data):
        result = data
        for func in funcs:
            result = func(result)
        return result
    return pipe

def main():
    print("1. Functor Example")
    functor = Functor(5)
    result = functor.map(lambda x: x * 2).map(lambda x: x + 1).value
    print(f"Functor result: {result}")

    print("\n2. Advanced Function Composition")
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    composed = compose(double, add_one, double)
    print(f"Composed function result: {composed(5)}")

    print("\n3. Currying")
    @curry
    def add(x, y, z):
        return x + y + z
    add_5 = add(5)
    add_5_10 = add_5(10)
    print(f"Curried function result: {add_5_10(15)}")

    print("\n4. Memoization")
    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    print(f"Fibonacci(30): {fibonacci(30)}")

    print("\n5. Function Pipeline")
    data = [1, 2, 3, 4, 5]
    process = pipeline(
        lambda x: map(lambda n: n * 2, x),
        lambda x: filter(lambda n: n > 5, x),
        lambda x: reduce(lambda a, b: a + b, x)
    )
    result = process(data)
    print(f"Pipeline result: {result}")

if __name__ == "__main__":
    main()

# Uncomment the following lines to run the unit tests
# import unittest
# unittest.main(argv=[''], exit=False)