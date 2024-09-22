# Functions - Variable-length arguments (*args and **kwargs) - in the Python Programming Language
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
import functools
from typing import Any, Callable, Dict, List, Tuple, Union
import asyncio

# 1. Overview and Historical Context
"""
Variable-length arguments in Python, represented by *args and **kwargs, allow functions
to accept an arbitrary number of positional and keyword arguments, respectively.

Key aspects:
- *args: Collects an arbitrary number of positional arguments into a tuple
- **kwargs: Collects an arbitrary number of keyword arguments into a dictionary

Historical context:
- Introduced in early versions of Python (pre-2.0)
- Inspired by similar concepts in other languages (e.g., C's variadic functions)
- Became increasingly important with the rise of functional programming in Python
- PEP 3102 (2006) introduced keyword-only arguments, enhancing **kwargs usage
- PEP 3132 (2008) introduced extended iterable unpacking, complementing *args

These features are crucial in modern Python development, enabling the creation of
flexible APIs, decorators, and adapters. They align with Python's philosophy of
providing powerful, expressive tools to developers.
"""

# 2. Syntax, Key Concepts, and Code Examples

def sum_all(*args: Union[int, float]) -> Union[int, float]:
    """
    Sums all provided arguments.
    
    Args:
        *args: Variable number of numeric arguments.
    
    Returns:
        Union[int, float]: The sum of all arguments.
    """
    return sum(args)

def print_info(**kwargs: Any) -> None:
    """
    Prints information provided as keyword arguments.
    
    Args:
        **kwargs: Arbitrary keyword arguments.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def combined_example(*args: Any, **kwargs: Any) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
    """
    Demonstrates the use of both *args and **kwargs.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    
    Returns:
        Tuple[Tuple[Any, ...], Dict[str, Any]]: A tuple containing args and kwargs.
    """
    return args, kwargs

# Advanced usage: Function that accepts any callable and its arguments
def call_function(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Calls a function with provided positional and keyword arguments.
    
    Args:
        func (Callable[..., Any]): The function to call.
        *args: Variable positional arguments to pass to the function.
        **kwargs: Variable keyword arguments to pass to the function.
    
    Returns:
        Any: The result of calling the function.
    """
    return func(*args, **kwargs)

# 3. Best Practices, Common Pitfalls, and Advanced Tips

"""
Best Practices:
1. Use clear, descriptive names instead of *args and **kwargs when possible.
2. Document the expected types and meanings of variable-length arguments.
3. Use type annotations to improve code readability and enable static type checking.
4. Be cautious when mixing *args, **kwargs with regular arguments to avoid confusion.

Common Pitfalls:
1. Modifying mutable arguments passed via *args or **kwargs can lead to unexpected side effects.
2. Overuse can make function signatures unclear and harder to understand.
3. Performance overhead for very large numbers of arguments.

Advanced Tips:
1. Use *args and **kwargs in function signatures for creating flexible APIs.
2. Leverage these features for implementing decorators and adapters.
3. Combine with default arguments and keyword-only arguments for powerful function designs.
4. Use functools.partial for partial function application with *args and **kwargs.
"""

# Example of a flexible function using *args and **kwargs
def flexible_function(*args: Any, required_arg: str, **kwargs: Any) -> Dict[str, Any]:
    """
    A flexible function demonstrating the use of *args and **kwargs with a required argument.
    
    Args:
        *args: Variable positional arguments.
        required_arg (str): A required argument.
        **kwargs: Variable keyword arguments.
    
    Returns:
        Dict[str, Any]: A dictionary containing all provided arguments.
    """
    return {
        "args": args,
        "required_arg": required_arg,
        "kwargs": kwargs
    }

# 4. Integration and Real-World Applications

"""
Real-world applications of *args and **kwargs:

1. API Design:
   - Creating flexible interfaces that can adapt to future requirements

2. Decorators:
   - Wrapping functions without knowing their signatures in advance

3. Adapter Patterns:
   - Adapting function calls between incompatible interfaces

4. Event Systems:
   - Handling events with varying numbers of parameters

5. Configuration Management:
   - Accepting arbitrary configuration options

Example: A simple event system using *args and **kwargs
"""

class EventSystem:
    def __init__(self):
        self.listeners = {}

    def add_listener(self, event_type: str, listener: Callable[..., None]) -> None:
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def emit(self, event_type: str, *args: Any, **kwargs: Any) -> None:
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(*args, **kwargs)

# 5. Advanced Concepts and Emerging Trends

"""
Advanced Concepts:
1. Type hinting for *args and **kwargs (PEP 484)
2. Keyword-only arguments (PEP 3102)
3. Positional-only parameters (PEP 570)
4. Extended iterable unpacking (PEP 3132)

Emerging Trends:
1. Enhanced static type checking for variable-length arguments
2. Integration with dataclasses and other metaprogramming tools
3. Use in asynchronous programming with async/await syntax
"""

# Example of type-hinted *args and **kwargs with async function
async def process_data(*args: int, **kwargs: str) -> List[str]:
    """
    Processes data asynchronously with type-hinted variable-length arguments.
    
    Args:
        *args (int): Variable number of integers to process.
        **kwargs (str): Variable keyword arguments with string values.
    
    Returns:
        List[str]: Processed data as a list of strings.
    """
    result = []
    for arg in args:
        await asyncio.sleep(0.1)  # Simulate async processing
        result.append(str(arg * 2))
    for key, value in kwargs.items():
        await asyncio.sleep(0.1)  # Simulate async processing
        result.append(f"{key}: {value.upper()}")
    return result

# 6. FAQs and Troubleshooting

"""
Q1: When should I use *args vs **kwargs?
A1: Use *args when you want to accept any number of positional arguments,
    and **kwargs when you want to accept any number of keyword arguments.

Q2: Can I use *args and **kwargs together in a function definition?
A2: Yes, you can use both in the same function. The order should be:
    regular arguments, *args, keyword-only arguments, and then **kwargs.

Q3: How do I pass *args and **kwargs to another function?
A3: You can unpack them in the function call: other_func(*args, **kwargs)

Troubleshooting:
1. TypeError: "function() takes x positional arguments but y were given"
   Solution: Ensure you're not passing too many positional arguments.
   Check if you meant to use keyword arguments for some parameters.

2. TypeError: "function() got an unexpected keyword argument"
   Solution: Verify that you're not passing keyword arguments that
   the function doesn't accept. Consider using **kwargs if you need
   to pass arbitrary keyword arguments.

3. Performance issues with large numbers of arguments
   Solution: Consider restructuring your code to pass data more efficiently,
   such as using a single dictionary or object instead of many individual arguments.
"""

# 7. Recommended Tools, Libraries, and Resources

"""
Tools and Libraries:
1. typing module: For type hinting *args and **kwargs
2. functools.wraps: For preserving function metadata in decorators
3. inspect module: For introspecting function signatures with variable-length arguments
4. mypy: Static type checker that supports *args and **kwargs annotations

Resources:
1. "Fluent Python" by Luciano Ramalho
2. "Python Cookbook" by David Beazley and Brian K. Jones
3. Python Documentation: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
4. Real Python tutorial: https://realpython.com/python-kwargs-and-args/
"""

# 8. Performance Analysis and Optimization

def benchmark(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """
    Benchmarks the execution time of a function.
    
    Args:
        func (Callable[..., Any]): The function to benchmark.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    
    Returns:
        float: The execution time in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

# Example of optimizing a function that uses *args
def sum_squares_slow(*args: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of squares (slow version).
    
    Args:
        *args: Variable number of numeric arguments.
    
    Returns:
        Union[int, float]: The sum of squares of all arguments.
    """
    return sum(arg ** 2 for arg in args)

def sum_squares_fast(*args: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of squares (optimized version).
    
    Args:
        *args: Variable number of numeric arguments.
    
    Returns:
        Union[int, float]: The sum of squares of all arguments.
    """
    return sum(map(lambda x: x ** 2, args))

# Main function to demonstrate concepts
async def main() -> None:
    print("1. Basic *args usage:")
    print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

    print("\n2. Basic **kwargs usage:")
    print_info(name="Alice", age=30, city="New York")

    print("\n3. Combined *args and **kwargs:")
    args, kwargs = combined_example(1, 2, 3, name="Bob", age=25)
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

    print("\n4. Calling functions with variable arguments:")
    result = call_function(sum_all, 1, 2, 3, 4, 5)
    print(f"Result of calling sum_all: {result}")

    print("\n5. Flexible function with required argument:")
    result = flexible_function(1, 2, 3, required_arg="important", extra="info")
    print(f"Flexible function result: {result}")

    print("\n6. Event system demonstration:")
    event_system = EventSystem()
    event_system.add_listener("user_login", lambda user, time: print(f"{user} logged in at {time}"))
    event_system.emit("user_login", "Alice", time="14:30")

    print("\n7. Asynchronous function with type-hinted *args and **kwargs:")
    result = await process_data(1, 2, 3, name="Alice", city="New York")
    print(f"Async processing result: {result}")

    print("\n8. Performance comparison:")
    args = tuple(range(1000))
    slow_time = benchmark(sum_squares_slow, *args)
    fast_time = benchmark(sum_squares_fast, *args)
    print(f"Slow version time: {slow_time:.6f} seconds")
    print(f"Fast version time: {fast_time:.6f} seconds")
    print(f"Speedup factor: {slow_time / fast_time:.2f}x")

if __name__ == "__main__":
    asyncio.run(main())

"""
Conclusion:

This comprehensive guide covers the intricacies of variable-length arguments (*args and **kwargs) in Python functions. These powerful features enable developers to create flexible, adaptable, and maintainable code. Key takeaways include:

1. *args and **kwargs provide a way to accept arbitrary numbers of positional and keyword arguments.
2. They are essential for creating flexible APIs, implementing decorators, and designing adaptable software systems.
3. Proper use of these features can lead to more pythonic and reusable code.
4. Understanding potential pitfalls and performance implications is crucial for effective usage.
5. Modern Python development increasingly leverages these features in conjunction with type hinting and asynchronous programming.

As Python continues to evolve, mastering *args and **kwargs becomes increasingly important for developers at all levels. These concepts form a cornerstone of advanced Python programming, enabling the creation of powerful, generic, and reusable code.

Remember to use these features judiciously, always prioritizing code readability and maintainability. When in doubt, refer to the Zen of Python: "Explicit is better than implicit."

By mastering variable-length arguments, you'll be well-equipped to write Python code that is both powerful and flexible, adapting to a wide range of use cases with ease.

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