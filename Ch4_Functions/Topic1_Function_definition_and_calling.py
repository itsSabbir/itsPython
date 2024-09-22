"""
Functions - Function definition and calling - in the Python Programming Language
================================================================================

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
Functions are a fundamental building block in Python, allowing for code reuse,
modularization, and abstraction. They are first-class objects in Python, which
means they can be passed around and used as arguments.

Key aspects:
- Introduced in Python's first release in 1991
- Evolved to include features like keyword arguments, default values, and annotations
- Fundamental to Python's support for functional programming paradigms

Historical context:
- Inspired by languages like C and Lisp
- Developed to promote code reusability and readability
- Continuously improved to support more advanced use cases (e.g., decorators, async functions)

Relevance in modern software development:
- Essential for structuring and organizing code in all Python projects
- Crucial for implementing design patterns and architectural principles
- Fundamental to creating reusable and maintainable code

Comparison with other languages:
- More flexible than C/C++ functions (e.g., multiple return values, keyword arguments)
- Similar to JavaScript functions in their first-class nature
- More straightforward syntax compared to Java methods

Python functions have become increasingly powerful and flexible over time, 
supporting a wide range of programming paradigms and use cases.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import time
import asyncio
from typing import List, Dict, Any, Callable
from functools import wraps


def basic_function_definition():
    """
    Demonstrates basic function definition and calling.
    """
    print("Basic function definition and calling:")

    def greet(name):
        """A simple greeting function."""
        return f"Hello, {name}!"

    # Calling the function
    result = greet("Alice")
    print(result)

    # Function with default parameter
    def greet_with_default(name="World"):
        return f"Hello, {name}!"

    print(greet_with_default())
    print(greet_with_default("Bob"))

    print()


def function_with_multiple_parameters():
    """
    Demonstrates functions with multiple parameters and return values.
    """
    print("Function with multiple parameters and return values:")

    def calculate_statistics(numbers):
        """Calculate mean and standard deviation of a list of numbers."""
        n = len(numbers)
        mean = sum(numbers) / n
        variance = sum((x - mean) ** 2 for x in numbers) / n
        std_dev = variance ** 0.5
        return mean, std_dev

    data = [1, 2, 3, 4, 5]
    mean, std_dev = calculate_statistics(data)
    print(f"Mean: {mean}, Standard Deviation: {std_dev}")

    print()


def function_with_keyword_arguments():
    """
    Demonstrates functions with keyword arguments.
    """
    print("Function with keyword arguments:")

    def create_person(name, age, city="Unknown"):
        return f"{name} is {age} years old and lives in {city}."

    # Calling with positional arguments
    print(create_person("Alice", 30, "New York"))

    # Calling with keyword arguments
    print(create_person(age=25, name="Bob", city="London"))

    # Mixing positional and keyword arguments
    print(create_person("Charlie", age=35))

    print()


def function_with_variable_arguments():
    """
    Demonstrates functions with variable number of arguments.
    """
    print("Function with variable arguments:")

    def sum_all(*args):
        """Sum any number of arguments."""
        return sum(args)

    print(sum_all(1, 2, 3))
    print(sum_all(10, 20, 30, 40, 50))

    def print_info(**kwargs):
        """Print information from keyword arguments."""
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print_info(name="Alice", age=30, city="Paris")

    print()


def higher_order_functions():
    """
    Demonstrates higher-order functions.
    """
    print("Higher-order functions:")

    def apply_operation(func, x, y):
        """Apply a given function to two arguments."""
        return func(x, y)

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    print(apply_operation(add, 5, 3))
    print(apply_operation(multiply, 5, 3))

    # Using lambda functions
    print(apply_operation(lambda a, b: a ** b, 2, 3))

    print()


def function_decorators():
    """
    Demonstrates function decorators.
    """
    print("Function decorators:")

    def timer_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run.")
            return result
        return wrapper

    @timer_decorator
    def slow_function():
        time.sleep(1)
        return "Function completed."

    print(slow_function())

    print()


def function_annotations():
    """
    Demonstrates function annotations.
    """
    print("Function annotations:")

    def greet(name: str) -> str:
        return f"Hello, {name}!"

    print(greet("Alice"))
    print(greet.__annotations__)

    def calculate_area(length: float, width: float) -> float:
        return length * width

    print(calculate_area(5.0, 3.0))
    print(calculate_area.__annotations__)

    print()


async def asynchronous_functions():
    """
    Demonstrates asynchronous functions.
    """
    print("Asynchronous functions:")

    async def fetch_data(delay):
        await asyncio.sleep(delay)
        return f"Data fetched after {delay} seconds"

    async def main_async():
        task1 = asyncio.create_task(fetch_data(1))
        task2 = asyncio.create_task(fetch_data(2))

        print(await task1)
        print(await task2)

    await main_async()

    print()


def recursive_functions():
    """
    Demonstrates recursive functions.
    """
    print("Recursive functions:")

    def factorial(n: int) -> int:
        """Calculate the factorial of a number recursively."""
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(f"Factorial of 5: {factorial(5)}")

    def fibonacci(n: int) -> int:
        """Calculate the nth Fibonacci number recursively."""
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    print(f"10th Fibonacci number: {fibonacci(10)}")

    print()


def main():
    """
    Main function to demonstrate all concepts related to function definition and calling.
    """
    basic_function_definition()
    function_with_multiple_parameters()
    function_with_keyword_arguments()
    function_with_variable_arguments()
    higher_order_functions()
    function_decorators()
    function_annotations()
    asyncio.run(asynchronous_functions())
    recursive_functions()


if __name__ == "__main__":
    main()


"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Follow the DRY (Don't Repeat Yourself) principle by creating functions for reusable code.
2. Use descriptive function names that clearly indicate the function's purpose.
3. Keep functions focused on a single task (Single Responsibility Principle).
4. Use type hints and docstrings to improve code readability and maintainability.
5. Prefer return statements to modify function output rather than modifying global variables.

Common Pitfalls:
1. Overusing global variables within functions, leading to side effects.
2. Creating overly complex functions that are hard to understand and maintain.
3. Forgetting to return a value when one is expected.
4. Modifying mutable default arguments, leading to unexpected behavior.
5. Recursive functions without proper base cases, causing infinite recursion.

Advanced Tips:
1. Use partial functions from the functools module for function currying.
2. Leverage closures to create factory functions and maintain state.
3. Use decorators to add functionality to functions without modifying their code.
4. Implement function caching using the @functools.lru_cache decorator for expensive computations.
5. Utilize the inspect module for introspection and dynamic function creation.

Testing Functions:
1. Use pytest for writing and running tests.
2. Write unit tests for individual functions to ensure they work as expected.
3. Use parameterized tests to test functions with multiple inputs.
4. Mock external dependencies using the unittest.mock module.

Example unit test:
```python
import pytest

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55

@pytest.mark.parametrize("input,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
])
def test_factorial_parametrized(input, expected):
    assert factorial(input) == expected

# Run the tests
pytest.main([__file__])
```

4. Integration and Real-World Applications
------------------------------------------
Functions are fundamental in various domains and applications:

1. Web Development:
   - View functions in web frameworks like Flask or Django
   - API endpoint handlers in RESTful services

2. Data Science and Machine Learning:
   - Data preprocessing and feature engineering functions
   - Custom loss functions in machine learning models

3. System Administration:
   - Automation scripts for system tasks
   - Log parsing and analysis functions

4. Game Development:
   - Event handlers and game logic functions
   - AI behavior functions for game entities

Example from Django (simplified):
```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Function Annotations and Type Checking:
   - Static type checking using tools like mypy
   - Runtime type checking with libraries like typeguard

2. Asynchronous Programming:
   - Increased use of async/await syntax for non-blocking operations
   - Integration with asynchronous frameworks like FastAPI

3. Functional Programming Paradigms:
   - Increased adoption of functional programming concepts in Python
   - Use of libraries like toolz for advanced functional programming

4. Just-In-Time Compilation:
   - Use of Numba for JIT compilation of numerical Python functions
   - Performance improvements for compute-intensive functions

6. FAQs and Troubleshooting
---------------------------
Q: How can I make a function return multiple values?
A: Return a tuple, list, or dictionary containing multiple values.

Q: What's the difference between *args and **kwargs?
A: *args allows passing a variable number of positional arguments, while **kwargs allows passing a variable number of keyword arguments.

Q: How can I optimize a recursive function to avoid stack overflow?
A: Use tail recursion optimization or consider an iterative approach for very deep recursions.

Troubleshooting:
- For unexpected function behavior, use print statements or debuggers to trace the function execution.
- If a function is modifying variables unexpectedly, check for mutable default arguments.
- For performance issues, profile the function using the cProfile module.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools:
- PyCharm: IDE with excellent support for function analysis and refactoring
- pylint: Static code analyzer that can help identify function-related issues

Libraries:
- functools: Provides tools for working with functions and callable objects
- itertools: Offers functions creating iterators for efficient looping

Resources:
- "Fluent Python" by Luciano Ramalho
- "Python Cookbook" by David Beazley and Brian K. Jones
- Python official documentation: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

8. Performance Analysis and Optimization
----------------------------------------
- Use the cProfile module for detailed function performance analysis
- Consider using the line_profiler for line-by-line performance analysis
- For frequently called functions, consider using Cython for performance-critical sections
- Use memoization (@functools.lru_cache) for expensive, pure functions with repeated calls

Optimization strategies:
1. Avoid unnecessary function calls within loops
2. Use built-in functions and standard library functions when possible
3. Consider generator functions for memory-efficient iteration
4. Use appropriate data structures (e.g., sets for membership testing) to optimize function operations

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
"""