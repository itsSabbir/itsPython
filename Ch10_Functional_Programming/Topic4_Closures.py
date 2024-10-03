"""
Functional Programming - Closures - in the Python Programming Language
======================================================================

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
Closures are a powerful concept in functional programming that allows a function to access variables from its outer (enclosing) lexical scope even after the outer function has returned. This enables the creation of function factories, maintaining state, and implementing data hiding.

Historical context:
- The concept of closures originated in the 1960s with the LISP programming language.
- Python has supported closures since version 2.2 (2001), with improvements in subsequent versions.
- The implementation in Python was influenced by other functional programming languages like Scheme and ML.

Significance:
- Closures provide a way to bind data to a function without using class-based encapsulation.
- They allow for the creation of higher-order functions, a key concept in functional programming.
- Closures enable the implementation of decorators, another powerful Python feature.

Common use cases:
- Creating function factories
- Implementing callbacks and event handlers
- Data hiding and encapsulation without using classes
- Maintaining state in functional programming paradigms

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from typing import Callable, Any, List, Dict
import time

def demonstrate_basic_closure():
    """Demonstrate basic usage of closures."""
    
    def outer_function(x: int) -> Callable[[], int]:
        """
        This is the outer function that defines a local variable 'x'
        and returns an inner function.
        """
        def inner_function() -> int:
            """
            This is the inner function that has access to 'x' from the outer scope.
            It forms a closure by capturing and remembering the value of 'x'.
            """
            return x * 2
        
        return inner_function
    
    # Create two different closures
    closure1 = outer_function(5)
    closure2 = outer_function(10)
    
    print(f"Result of closure1: {closure1()}")  # Output: 10
    print(f"Result of closure2: {closure2()}")  # Output: 20

def demonstrate_closure_with_mutable_data():
    """Demonstrate closures with mutable data."""
    
    def counter() -> Callable[[], int]:
        """
        This function creates a closure that maintains a count.
        """
        count = 0
        def increment() -> int:
            nonlocal count  # Use nonlocal to modify the outer variable
            count += 1
            return count
        return increment
    
    # Create two independent counters
    counter1 = counter()
    counter2 = counter()
    
    print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")  # Output: 1, 2, 3
    print(f"Counter2: {counter2()}, {counter2()}")  # Output: 1, 2

def demonstrate_closure_as_function_factory():
    """Demonstrate using closures as a function factory."""
    
    def power_function(exponent: int) -> Callable[[float], float]:
        """
        This function returns a new function that raises its argument
        to the given exponent.
        """
        def power(base: float) -> float:
            return base ** exponent
        return power
    
    # Create specific power functions
    square = power_function(2)
    cube = power_function(3)
    
    print(f"Square of 4: {square(4)}")  # Output: 16
    print(f"Cube of 3: {cube(3)}")  # Output: 27

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use closures to encapsulate behavior and maintain clean interfaces.
2. Prefer immutable data in closures to avoid unexpected side effects.
3. Use the 'nonlocal' keyword when modifying variables from outer scopes.
4. Document the purpose and behavior of closures, especially in complex scenarios.

Common Pitfalls:
1. Modifying variables from outer scopes without using 'nonlocal' (for non-global variables).
2. Creating closures in loops, which may lead to unexpected behavior due to late binding.
3. Overusing closures when simpler solutions (like classes) might be more appropriate.
4. Memory leaks due to circular references in closures.

Advanced Tips:
1. Use closures to implement simple decorators.
2. Leverage closures for partial function application and currying.
3. Utilize closures for creating generators and coroutines.
4. Combine closures with higher-order functions for powerful functional programming patterns.
"""

from functools import wraps

def demonstrate_advanced_closure_techniques():
    """Demonstrate advanced techniques using closures."""
    
    # Using closure as a decorator
    def timing_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
            return result
        return wrapper
    
    @timing_decorator
    def slow_function(n: int) -> int:
        """A slow function to demonstrate the timing decorator."""
        time.sleep(n)
        return n ** 2
    
    print(f"Result of slow_function(2): {slow_function(2)}")
    
    # Closure for partial application
    def partial(func: Callable, *partial_args) -> Callable:
        """Implement partial function application using closure."""
        def wrapper(*args, **kwargs):
            return func(*partial_args, *args, **kwargs)
        return wrapper
    
    def greet(greeting: str, name: str) -> str:
        return f"{greeting}, {name}!"
    
    say_hello = partial(greet, "Hello")
    print(say_hello("Alice"))  # Output: Hello, Alice!

"""
4. Integration and Real-World Applications
------------------------------------------
Closures are widely used in various Python libraries and frameworks:

1. Django: For creating custom middleware and context processors.
2. Flask: In route decorators and application factories.
3. Pytest: For fixture implementation and test parameterization.

Real-world example: Configurable Logger
"""

import logging
from typing import Callable

def create_logger(name: str, level: int = logging.INFO) -> Callable[[str], None]:
    """
    Create a configurable logger using closures.
    
    This function returns a logging function that is preconfigured
    with a specific name and level.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create a handler and set its level
    handler = logging.StreamHandler()
    handler.setLevel(level)
    
    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    
    def log(message: str) -> None:
        """The closure that uses the configured logger."""
        logger.info(message)
    
    return log

def demonstrate_real_world_application():
    """Demonstrate a real-world application of closures in a logging system."""
    
    # Create loggers for different modules
    log_main = create_logger("main")
    log_utils = create_logger("utils", level=logging.DEBUG)
    
    # Use the loggers
    log_main("Starting the application")
    log_utils("Initializing utility functions")
    
    # Simulate some application logic
    result = 42
    log_main(f"Computation result: {result}")
    log_utils("Cleaning up resources")
    
    log_main("Application finished")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous closures: Using closures with async/await for managing asynchronous state.
2. Type hinting for closures: Improved static type checking for functions returning closures.
3. Functional reactive programming: Using closures to implement reactive patterns in Python.
4. Memory-efficient closures: Techniques for optimizing closure memory usage in large-scale applications.
"""

import asyncio
from typing import Callable, Awaitable

async def demonstrate_async_closure():
    """Demonstrate the use of closures in asynchronous programming."""
    
    async def create_async_counter() -> Callable[[], Awaitable[int]]:
        count = 0
        async def increment():
            nonlocal count
            await asyncio.sleep(0.1)  # Simulate some async operation
            count += 1
            return count
        return increment
    
    async_counter = await create_async_counter()
    
    print("Async counter results:")
    for _ in range(3):
        result = await async_counter()
        print(result)

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts related to closures."""
    
    # Run the async demonstration
    asyncio.run(demonstrate_async_closure())
    
    # Demonstrate closure with type hints
    from typing import TypeVar, Callable
    
    T = TypeVar('T')
    U = TypeVar('U')
    
    def create_multiplier(factor: T) -> Callable[[U], U]:
        def multiplier(x: U) -> U:
            return x * factor  # type: ignore
        return multiplier
    
    double = create_multiplier(2)
    print(f"Double of 5: {double(5)}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: How do closures differ from classes for maintaining state?
A: Closures provide a lightweight alternative to classes for simple state management. They're often more concise but less powerful for complex scenarios.

Q: Can closures access and modify global variables?
A: Yes, closures can access global variables, but it's generally considered bad practice. Use the 'global' keyword if modification is necessary.

Q: How do I debug issues with closures?
A: Use print statements or logging within the closure to track variable values. Python's debugger (pdb) can also step through closure execution.

Troubleshooting:
1. If a closure isn't capturing the expected value, check for late binding issues, especially in loops.
2. For unexpected behavior with mutable data, ensure you're using 'nonlocal' when modifying variables from outer scopes.
3. If facing memory issues, look for circular references or consider using weak references.
"""

def troubleshooting_examples():
    """Demonstrate solutions to common issues with closures."""
    
    # Late binding issue
    def create_multipliers_incorrect():
        return [lambda x: i * x for i in range(4)]
    
    # Correct solution using default argument
    def create_multipliers_correct():
        return [lambda x, i=i: i * x for i in range(4)]
    
    print("Incorrect multipliers:")
    for mult in create_multipliers_incorrect():
        print(mult(2))  # Will print 6 four times
    
    print("Correct multipliers:")
    for mult in create_multipliers_correct():
        print(mult(2))  # Will print 0, 2, 4, 6
    
    # Demonstrating nonlocal for mutable data
    def counter_with_nonlocal():
        count = 0
        def increment():
            nonlocal count
            count += 1
            return count
        return increment
    
    c = counter_with_nonlocal()
    print(f"Counter: {c()}, {c()}, {c()}")  # Will print 1, 2, 3

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. functools: Built-in Python module with tools for working with higher-order functions and operations on callable objects.
2. typing: For type hinting in closures and functions returning closures.
3. inspect: For introspection of closures and their enclosing scopes.
4. pylint: Can help identify issues with variable scoping in closures.

Resources:
- "Fluent Python" by Luciano Ramalho (Chapter on closures and decorators)
- "Python Cookbook" by David Beazley and Brian K. Jones (Recipes involving closures)
- Python's official documentation on nested functions and closures: https://docs.python.org/3/reference/executionmodel.html#resolution-of-names
- Real Python's guide on closures: https://realpython.com/python-closures/
- PEP 3104 - Access to Names in Outer Scopes: https://www.python.org/dev/peps/pep-3104/

8. Performance Analysis and Optimization
----------------------------------------
When working with closures, it's important to consider their performance implications, especially in performance-critical applications.
"""

import timeit

def performance_comparison():
    """Compare performance of closures vs. class-based implementations."""
    
    # Closure-based implementation
    def create_counter_closure():
        count = 0
        def increment():
            nonlocal count
            count += 1
            return count
        return increment
    
    # Class-based implementation
    class CounterClass:
        def __init__(self):
            self.count = 0
        
        def increment(self):
            self.count += 1
            return self.count
    
    # Performance test
    closure_counter = create_counter_closure()
    class_counter = CounterClass()
    
    closure_time = timeit.timeit(closure_counter, number=1000000)
    class_time = timeit.timeit(class_counter.increment, number=1000000)
    
    print(f"Closure-based counter time: {closure_time:.6f} seconds")
    print(f"Class-based counter time: {class_time:.6f} seconds")
    print(f"Relative performance: {class_time / closure_time:.2f}x")

"""
Performance Considerations:
1. Closures can be slightly slower than regular function calls due to the additional scope lookup.
2. Creating many closures can increase memory usage, as each closure retains its own copy of the enclosing scope.
3. Closures can be more efficient than classes for simple state management scenarios.

Optimization Strategies:
1. Use closures judiciously, especially in performance-critical sections of code.
2. Consider using `__slots__` in classes as an alternative to closures for better memory efficiency in some cases.
3. Minimize the size of the captured scope to reduce memory overhead.
4. Use the `dis` module to inspect the bytecode of closures for low-level optimization opportunities.
"""

def optimize_closure_usage():
    """Demonstrate optimization techniques for closures."""
    
    import dis
    
    def create_optimized_counter():
        count = 0
        def increment():
            nonlocal count
            count += 1
            return count
        return increment
    
    optimized_counter = create_optimized_counter()
    
    print("Bytecode of the optimized counter:")
    dis.dis(optimized_counter)
    
    # Measure performance
    optimized_time = timeit.timeit(optimized_counter, number=1000000)
    print(f"Optimized counter time: {optimized_time:.6f} seconds")

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
- Relevance to the main topic of closures in Python's functional programming paradigm.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to closures.
    """
    print("Basic Closure Usage:")
    demonstrate_basic_closure()
    
    print("\nClosure with Mutable Data:")
    demonstrate_closure_with_mutable_data()
    
    print("\nClosure as Function Factory:")
    demonstrate_closure_as_function_factory()
    
    print("\nAdvanced Closure Techniques:")
    demonstrate_advanced_closure_techniques()
    
    print("\nReal-World Application of Closures:")
    demonstrate_real_world_application()
    
    print("\nAdvanced Concepts:")
    demonstrate_advanced_concepts()
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Comparison:")
    performance_comparison()
    
    print("\nOptimizing Closure Usage:")
    optimize_closure_usage()

if __name__ == "__main__":
    main()