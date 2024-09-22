# Functions - Parameters and return values - in the Python Programming Language
# Author: Sabbir Hossain
# Last Updated: September 19, 2024

"""
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
"""

import time
import asyncio
from typing import List, Tuple, Callable, Any
from functools import wraps

# 1. Overview and Historical Context
"""
Functions in Python are first-class objects that encapsulate a piece of code which can be reused.
They are fundamental to structured programming and have been a core feature of Python since its inception.

Key aspects of Python functions:
- Defined using the 'def' keyword
- Can accept parameters (arguments) and return values
- Support default arguments, keyword arguments, and variable-length arguments
- Can be assigned to variables, passed as arguments, and returned from other functions

Historical context:
- Introduced in Python 0.9.0 (February 1991)
- Significant enhancements in Python 2.x and 3.x series
- Python 3.0 (2008) introduced function annotations
- Python 3.5 (2015) added support for type hints
- Python 3.8 (2019) introduced the '/' and '*' parameters for positional-only and keyword-only arguments

Functions in Python draw inspiration from functional programming paradigms while maintaining simplicity
and readability, aligning with Python's "batteries included" philosophy.
"""

# 2. Syntax, Key Concepts, and Code Examples

def greet(name: str) -> str:
    """
    A simple function demonstrating basic syntax and return value.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def calculate_area(length: float, width: float = 1.0) -> float:
    """
    Calculates the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float, optional): The width of the rectangle. Defaults to 1.0.
    
    Returns:
        float: The calculated area.
    """
    return length * width

def sum_all(*args: int) -> int:
    """
    Sums all provided arguments.
    
    Args:
        *args: Variable number of integer arguments.
    
    Returns:
        int: The sum of all arguments.
    """
    return sum(args)

def create_person(**kwargs: Any) -> dict:
    """
    Creates a person dictionary from keyword arguments.
    
    Args:
        **kwargs: Arbitrary keyword arguments representing person attributes.
    
    Returns:
        dict: A dictionary containing the person's attributes.
    """
    return kwargs

def factorial(n: int) -> int:
    """
    Calculates the factorial of a number recursively.
    
    Args:
        n (int): The number to calculate factorial for.
    
    Returns:
        int: The factorial of n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)

# Advanced function with multiple return values and type annotations
def analyze_text(text: str) -> Tuple[int, int, List[str]]:
    """
    Analyzes the given text and returns various statistics.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        Tuple[int, int, List[str]]: A tuple containing:
            - The number of words
            - The number of characters
            - A list of unique words
    """
    words = text.split()
    return len(words), len(text), list(set(words))

# Function with default mutable argument (demonstrating potential pitfall)
def append_to_list(item: Any, target_list: List[Any] = None) -> List[Any]:
    """
    Appends an item to a list. If no list is provided, a new one is created.
    
    Args:
        item (Any): The item to append.
        target_list (List[Any], optional): The list to append to. Defaults to None.
    
    Returns:
        List[Any]: The updated list.
    
    Note:
        Using a mutable default argument can lead to unexpected behavior.
        This function demonstrates the correct way to handle this case.
    """
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# Higher-order function example
def apply_operation(func: Callable[[int, int], int], x: int, y: int) -> int:
    """
    Applies a given operation to two integers.
    
    Args:
        func (Callable[[int, int], int]): A function that takes two integers and returns an integer.
        x (int): The first integer.
        y (int): The second integer.
    
    Returns:
        int: The result of applying the function to x and y.
    """
    return func(x, y)

# Decorator example
def timer(func: Callable) -> Callable:
    """
    A decorator that measures the execution time of a function.
    
    Args:
        func (Callable): The function to be timed.
    
    Returns:
        Callable: A wrapper function that times the execution of the original function.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

# Asynchronous function example
async def fetch_data(url: str) -> str:
    """
    Simulates fetching data from a URL asynchronously.
    
    Args:
        url (str): The URL to fetch data from.
    
    Returns:
        str: The fetched data (simulated).
    """
    print(f"Fetching data from {url}")
    await asyncio.sleep(1)  # Simulate network delay
    return f"Data from {url}"

# 3. Best Practices, Common Pitfalls, and Advanced Tips

"""
Best Practices:
1. Follow the PEP 8 style guide for naming conventions and code formatting.
2. Use type hints to improve code readability and catch type-related errors early.
3. Write clear docstrings for all functions, including parameters, return values, and raised exceptions.
4. Keep functions focused on a single task (Single Responsibility Principle).
5. Use default arguments with care, especially with mutable types.
6. Prefer return statements at the end of functions for clarity.

Common Pitfalls:
1. Using mutable default arguments (e.g., lists or dictionaries) incorrectly.
2. Forgetting to return a value when one is expected.
3. Modifying global variables within functions without proper declaration.
4. Overusing nested functions, which can lead to complexity.
5. Not handling exceptions properly, especially in recursive functions.

Advanced Tips:
1. Use functools.lru_cache for memoization of expensive function calls.
2. Leverage closures and function factories for creating specialized functions.
3. Understand the differences between LEGB (Local, Enclosing, Global, Built-in) scopes.
4. Use `*args` and `**kwargs` judiciously for creating flexible function interfaces.
5. Implement context managers using the `contextlib` module for resource management.
"""

# Example of a closure and function factory
def power_function(exponent: int) -> Callable[[float], float]:
    """
    Creates a function that raises a number to the given exponent.
    
    Args:
        exponent (int): The exponent to use.
    
    Returns:
        Callable[[float], float]: A function that takes a number and returns it raised to the exponent.
    """
    def power(base: float) -> float:
        return base ** exponent
    return power

# 4. Integration and Real-World Applications

"""
Functions are fundamental building blocks in Python and are used extensively in various applications:

1. Web Development:
   - Route handlers in web frameworks like Flask or Django
   - Data processing and validation in API endpoints

2. Data Science and Machine Learning:
   - Custom loss functions in neural networks
   - Data preprocessing and feature engineering

3. System Administration:
   - Automating tasks and system operations
   - Parsing and processing log files

4. Game Development:
   - Defining game logic and mechanics
   - Handling user input and events

5. Financial Applications:
   - Implementing complex financial models and calculations
   - Risk assessment and portfolio management functions

Example: A simple web route handler (using Flask-like syntax)
"""

def handle_user_registration(username: str, email: str, password: str) -> dict:
    """
    Simulates handling a user registration request.
    
    Args:
        username (str): The desired username.
        email (str): The user's email address.
        password (str): The user's password.
    
    Returns:
        dict: A response indicating success or failure.
    """
    # In a real application, you would validate inputs and interact with a database
    if len(password) < 8:
        return {"status": "error", "message": "Password too short"}
    
    # Simulate successful registration
    return {"status": "success", "message": f"User {username} registered successfully"}

# 5. Advanced Concepts and Emerging Trends

"""
Advanced Concepts:
1. Function Annotations and Type Hints:
   - Introduced in Python 3.0 and enhanced in subsequent versions
   - Improves code readability and enables static type checking

2. Asynchronous Functions:
   - Introduced in Python 3.5 with async/await syntax
   - Enables efficient handling of I/O-bound and high-latency operations

3. Structural Pattern Matching:
   - Introduced in Python 3.10
   - Enables more expressive ways of working with data structures in functions

Emerging Trends:
1. Increased use of type hints and static type checkers (e.g., mypy)
2. Growing adoption of functional programming paradigms in Python
3. Integration of machine learning models as functions in applications
4. Enhanced support for concurrent and parallel execution of functions
"""

# Example of structural pattern matching (Python 3.10+)
def parse_command(command: str) -> str:
    match command.split():
        case ["quit"]:
            return "Exiting program"
        case ["greet", name]:
            return f"Hello, {name}!"
        case ["add", x, y]:
            return f"Result: {float(x) + float(y)}"
        case _:
            return "Unknown command"

# 6. FAQs and Troubleshooting

"""
Q1: How do I choose between a function and a method?
A1: Use a function for standalone operations. Use a method when the operation is
    closely tied to a specific class or object.

Q2: What's the difference between `*args` and `**kwargs`?
A2: `*args` allows passing a variable number of positional arguments,
    while `**kwargs` allows passing a variable number of keyword arguments.

Q3: How can I optimize recursive functions to avoid stack overflow?
A3: Use tail recursion optimization or consider iterative alternatives for
    very deep recursions. Python doesn't optimize tail recursion automatically.

Troubleshooting:
1. UnboundLocalError: Occurs when trying to modify a global variable without declaring it global.
   Solution: Use the `global` keyword or pass the variable as a parameter.

2. TypeError: Occurs when passing incorrect types to a function.
   Solution: Use type hints and validate input types within the function.

3. RecursionError: Occurs with excessive recursion depth.
   Solution: Implement an iterative solution or increase recursion limit (with caution).
"""

# 7. Recommended Tools, Libraries, and Resources

"""
Tools and Libraries:
1. mypy: Static type checker for Python
2. pylint: Code analysis tool for detecting errors and enforcing coding standards
3. functools: Module for higher-order functions and operations on callable objects
4. itertools: Module for efficient looping and combination generation
5. asyncio: Library for writing asynchronous code using coroutines

Resources:
1. "Fluent Python" by Luciano Ramalho
2. "Python Cookbook" by David Beazley and Brian K. Jones
3. Real Python (https://realpython.com/) - Excellent tutorials on Python functions
4. Python Documentation (https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
"""

# 8. Performance Analysis and Optimization

def benchmark(func: Callable, *args: Any, **kwargs: Any) -> float:
    """
    Benchmarks the execution time of a function.
    
    Args:
        func (Callable): The function to benchmark.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    
    Returns:
        float: The execution time in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

# Example of optimizing a function
def fibonacci_recursive(n: int) -> int:
    """
    Calculates the nth Fibonacci number recursively (inefficient for large n).
    
    Args:
        n (int): The position in the Fibonacci sequence.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_optimized(n: int) -> int:
    """
    Calculates the nth Fibonacci number iteratively (more efficient).
    
    Args:
        n (int): The position in the Fibonacci sequence.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Main function to demonstrate concepts
def main() -> None:
    print("1. Basic function call:")
    print(greet("Alice"))

    print("\n2. Function with default argument:")
    print(f"Area: {calculate_area(5, 3)}")
    print(f"Area (default width): {calculate_area(5)}")

    print("\n3. Variable-length arguments:")
    print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

    print("\n4. Keyword arguments:")
    person = create_person(name="Bob", age=30, city="New York")
    print(f"Person: {person}")

    print("\n5. Recursive function:")
    print(f"Factorial of 5: {factorial(5)}")

    print("\n6. Multiple return values:")
    text = "Python functions are powerful and flexible."
    word_count, char_count, unique_words = analyze_text(text)
    print(f"Word count: {word_count}, Char count: {char_count}")
    print(f"Unique words: {unique_words}")

    print("\n7. Higher-order function:")
    multiply = lambda x, y: x * y
    print(f"Result of operation: {apply_operation(multiply, 4, 5)}")

    print("\n8. Decorator example:")
    @timer
    def slow_function():
        time.sleep(1)
        return "Function completed"
    
    result = slow_function()
    print(result)

    print("\n9. Closure and function factory:")
    square = power_function(2)
    cube = power_function(3)
    print(f"Square of 4: {square(4)}")
    print(f"Cube of 3: {cube(3)}")

    print("\n10. Simulated web route handler:")
    response = handle_user_registration("alice123", "alice@example.com", "securepass123")
    print(f"Registration response: {response}")

    print("\n11. Structural pattern matching (Python 3.10+):")
    commands = ["greet John", "add 5 3", "unknown command"]
    for cmd in commands:
        print(f"Command '{cmd}': {parse_command(cmd)}")

    print("\n12. Asynchronous function example:")
    async def main_async():
        urls = ["http://example.com", "http://example.org", "http://example.net"]
        tasks = [fetch_data(url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)
    
    asyncio.run(main_async())

    print("\n13. Performance comparison:")
    n = 30
    recursive_time = benchmark(fibonacci_recursive, n)
    optimized_time = benchmark(fibonacci_optimized, n)
    print(f"Recursive Fibonacci (n={n}) time: {recursive_time:.6f} seconds")
    print(f"Optimized Fibonacci (n={n}) time: {optimized_time:.6f} seconds")
    print(f"Speedup factor: {recursive_time / optimized_time:.2f}x")

if __name__ == "__main__":
    main()

# Additional advanced examples and concepts

# Example of a generator function
def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """
    A generator function that yields Fibonacci numbers up to a limit.
    
    Args:
        limit (int): The maximum number of Fibonacci numbers to generate.
    
    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Example of function overloading using singledispatch
from functools import singledispatch

@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported type")

@add.register(int)
def _(a: int, b: int) -> int:
    return a + b

@add.register(float)
def _(a: float, b: float) -> float:
    return a + b

@add.register(str)
def _(a: str, b: str) -> str:
    return f"{a} {b}"

# Example of a context manager function
from contextlib import contextmanager

@contextmanager
def managed_file(filename: str, mode: str = 'r'):
    """
    A context manager for file handling.
    
    Args:
        filename (str): The name of the file to open.
        mode (str): The mode in which to open the file.
    
    Yields:
        File: The opened file object.
    """
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

# Example of partial function application
from functools import partial

def greet_with_prefix(prefix: str, name: str) -> str:
    return f"{prefix} {name}!"

greet_mr = partial(greet_with_prefix, "Mr.")
greet_mrs = partial(greet_with_prefix, "Mrs.")

# Example of using type variables for generic functions
from typing import TypeVar, List

T = TypeVar('T')

def first_and_last(sequence: List[T]) -> Tuple[T, T]:
    """
    Returns the first and last elements of a sequence.
    
    Args:
        sequence (List[T]): A list of elements of any type.
    
    Returns:
        Tuple[T, T]: A tuple containing the first and last elements.
    
    Raises:
        IndexError: If the sequence is empty.
    """
    if not sequence:
        raise IndexError("Sequence is empty")
    return sequence[0], sequence[-1]

# Additional main function to demonstrate these advanced concepts
def advanced_examples():
    print("\n--- Advanced Function Examples ---")
    
    print("\nGenerator function:")
    fib_gen = fibonacci_generator(5)
    print("First 5 Fibonacci numbers:", list(fib_gen))
    
    print("\nFunction overloading:")
    print(f"add(1, 2) = {add(1, 2)}")
    print(f"add(1.5, 2.7) = {add(1.5, 2.7)}")
    print(f"add('Hello', 'World') = {add('Hello', 'World')}")
    
    print("\nContext manager:")
    with managed_file('example.txt', 'w') as f:
        f.write("Hello, context manager!")
    print("File written using context manager")
    
    print("\nPartial function application:")
    print(greet_mr("Smith"))
    print(greet_mrs("Johnson"))
    
    print("\nGeneric function with type variables:")
    numbers = [1, 2, 3, 4, 5]
    first, last = first_and_last(numbers)
    print(f"First and last of {numbers}: {first}, {last}")
    
    words = ["apple", "banana", "cherry"]
    first, last = first_and_last(words)
    print(f"First and last of {words}: {first}, {last}")

if __name__ == "__main__":
    main()
    advanced_examples()

"""
Conclusion:

This comprehensive guide covers the fundamental concepts and advanced techniques
related to functions, parameters, and return values in Python. By mastering these
concepts, developers can write more efficient, readable, and maintainable code.

Remember that while Python offers great flexibility, it's important to use these
features judiciously. Always prioritize code readability and maintainability over
clever or overly complex solutions.

As Python continues to evolve, stay updated with the latest language features and
best practices. Regularly refer to the official Python documentation and engage with
the Python community to keep your skills sharp and up-to-date.

Happy coding!
"""

# 9. How to Contribute

"""
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

Your contributions help keep this resource up-to-date and valuable for the Python community. Thank you for your support!
"""