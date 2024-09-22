# Functions - Default and keyword arguments - in the Python Programming Language
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
from typing import Any, Callable, Dict, List, Optional, Union

# 1. Overview and Historical Context
"""
Default and keyword arguments in Python functions provide flexibility and improve code readability.
They allow developers to create more versatile and user-friendly functions.

Key aspects:
- Default arguments: Provide default values for function parameters
- Keyword arguments: Allow calling functions with named parameters

Historical context:
- Default arguments have been a part of Python since its early versions
- Keyword arguments were introduced in Python 1.0 (1994)
- PEP 3102 (2006) introduced keyword-only arguments in Python 3.0
- PEP 3107 (2006) introduced function annotations, enhancing type hinting for arguments
- PEP 484 (2014) standardized type hints, including for default and keyword arguments
- PEP 570 (2018) introduced positional-only parameters in Python 3.8

These features align with Python's philosophy of providing clear, readable, and flexible code.
They are essential in modern Python development, particularly in creating adaptable APIs and libraries.
"""

# 2. Syntax, Key Concepts, and Code Examples

def greet(name: str, greeting: str = "Hello") -> str:
    """
    A simple function demonstrating default arguments.
    
    Args:
        name (str): The name of the person to greet.
        greeting (str, optional): The greeting to use. Defaults to "Hello".
    
    Returns:
        str: A greeting message.
    """
    return f"{greeting}, {name}!"

def calculate_price(
    base_price: float,
    tax_rate: float = 0.1,
    discount: float = 0.0
) -> float:
    """
    Calculates the final price of an item.
    
    Args:
        base_price (float): The base price of the item.
        tax_rate (float, optional): The tax rate as a decimal. Defaults to 0.1 (10%).
        discount (float, optional): The discount as a decimal. Defaults to 0.0 (0%).
    
    Returns:
        float: The final price after applying tax and discount.
    """
    price_after_discount = base_price * (1 - discount)
    final_price = price_after_discount * (1 + tax_rate)
    return round(final_price, 2)

def create_person(**kwargs: Any) -> Dict[str, Any]:
    """
    Creates a person dictionary using keyword arguments.
    
    Args:
        **kwargs: Arbitrary keyword arguments representing person attributes.
    
    Returns:
        Dict[str, Any]: A dictionary containing the person's attributes.
    """
    return kwargs

def process_data(data: List[int], *, sort: bool = False, reverse: bool = False) -> List[int]:
    """
    Processes a list of integers with keyword-only arguments.
    
    Args:
        data (List[int]): The list of integers to process.
        sort (bool, optional): Whether to sort the list. Defaults to False.
        reverse (bool, optional): Whether to reverse the list. Defaults to False.
    
    Returns:
        List[int]: The processed list of integers.
    """
    result = data.copy()
    if sort:
        result.sort(reverse=reverse)
    elif reverse:
        result.reverse()
    return result

# Advanced function combining various argument types
def advanced_function(
    a: int,
    b: int,
    *args: int,
    c: int = 0,
    d: int = 0,
    **kwargs: Any
) -> Dict[str, Any]:
    """
    An advanced function demonstrating various argument types.
    
    Args:
        a (int): A required positional argument.
        b (int): Another required positional argument.
        *args: Variable-length argument list.
        c (int, optional): A keyword argument. Defaults to 0.
        d (int, optional): Another keyword argument. Defaults to 0.
        **kwargs: Arbitrary keyword arguments.
    
    Returns:
        Dict[str, Any]: A dictionary containing all provided arguments.
    """
    return {
        "a": a,
        "b": b,
        "args": args,
        "c": c,
        "d": d,
        "kwargs": kwargs
    }

# 3. Best Practices, Common Pitfalls, and Advanced Tips

"""
Best Practices:
1. Use default arguments for optional parameters with sensible defaults.
2. Use None as a default for mutable types to avoid unexpected behavior.
3. Place parameters with default values after parameters without defaults.
4. Use keyword arguments to improve code readability, especially for functions with many parameters.
5. Use type hints to clarify expected argument types.

Common Pitfalls:
1. Mutable default arguments (e.g., lists or dictionaries) can lead to unexpected behavior.
2. Overusing default arguments can make function behavior less predictable.
3. Mixing positional and keyword arguments incorrectly can lead to errors.

Advanced Tips:
1. Use functools.partial for partial function application with default arguments.
2. Implement function overloading using singledispatch for type-based dispatch.
3. Use keyword-only arguments to enforce named parameter usage for clarity.
4. Leverage type hints and function annotations for better code documentation and IDE support.
"""

# Example of avoiding mutable default argument pitfall
def append_to_list(item: Any, target_list: Optional[List[Any]] = None) -> List[Any]:
    """
    Appends an item to a list, demonstrating safe handling of mutable default arguments.
    
    Args:
        item (Any): The item to append.
        target_list (Optional[List[Any]], optional): The list to append to. Defaults to None.
    
    Returns:
        List[Any]: The updated list.
    """
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# Example of partial function application
def multiply(x: float, y: float) -> float:
    """Multiplies two numbers."""
    return x * y

double = functools.partial(multiply, y=2)

# 4. Integration and Real-World Applications

"""
Real-world applications of default and keyword arguments:

1. Configuration Management:
   - Defining default configuration values that can be overridden

2. API Design:
   - Creating flexible interfaces that can adapt to various use cases

3. Data Processing Pipelines:
   - Configuring processing steps with optional parameters

4. Machine Learning:
   - Setting hyperparameters for models with sensible defaults

5. Web Frameworks:
   - Defining route handlers with optional query parameters

Example: A simple configuration management function
"""

def create_database_config(
    host: str = "localhost",
    port: int = 5432,
    user: str = "admin",
    password: str = "password",
    database: str = "main",
    **additional_options: Any
) -> Dict[str, Any]:
    """
    Creates a database configuration dictionary with default values.
    
    Args:
        host (str, optional): Database host. Defaults to "localhost".
        port (int, optional): Database port. Defaults to 5432.
        user (str, optional): Database user. Defaults to "admin".
        password (str, optional): Database password. Defaults to "password".
        database (str, optional): Database name. Defaults to "main".
        **additional_options: Additional database options.
    
    Returns:
        Dict[str, Any]: A dictionary containing the database configuration.
    """
    config = {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "database": database,
        **additional_options
    }
    return config

# 5. Advanced Concepts and Emerging Trends

"""
Advanced Concepts:
1. Type hinting for default and keyword arguments (PEP 484)
2. Positional-only parameters (PEP 570)
3. Keyword-only arguments (PEP 3102)
4. Variable-length argument lists and dictionaries (*args and **kwargs)
5. Function annotations (PEP 3107)

Emerging Trends:
1. Enhanced static type checking with tools like mypy
2. Increased use of dataclasses for structured default arguments
3. Integration with asynchronous programming (async/await) for default coroutines
"""

# Example of a function with positional-only, keyword-only, and variable-length arguments
def advanced_arg_function(
    a: int,
    b: int,
    /,
    c: int = 0,
    *,
    d: int = 0,
    **kwargs: Any
) -> Dict[str, Any]:
    """
    Demonstrates various argument types including positional-only and keyword-only.
    
    Args:
        a (int): Positional-only argument.
        b (int): Positional-only argument.
        c (int, optional): Regular argument with default. Defaults to 0.
        d (int, optional): Keyword-only argument. Defaults to 0.
        **kwargs: Additional keyword arguments.
    
    Returns:
        Dict[str, Any]: A dictionary containing all provided arguments.
    """
    return {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "kwargs": kwargs
    }

# 6. FAQs and Troubleshooting

"""
Q1: Why use default arguments instead of multiple function definitions?
A1: Default arguments provide a concise way to handle optional parameters,
    reducing code duplication and improving maintainability.

Q2: How do I avoid the mutable default argument pitfall?
A2: Use None as the default value and initialize the mutable object inside the function.

Q3: When should I use *args and **kwargs?
A3: Use them when you need to accept an arbitrary number of arguments or
    when creating wrapper functions that need to pass all arguments to another function.

Troubleshooting:
1. TypeError: "function() got multiple values for argument"
   Solution: Ensure you're not passing the same argument both positionally and as a keyword.

2. SyntaxError: "non-default argument follows default argument"
   Solution: Reorder your function parameters to place default arguments after non-default ones.

3. UnboundLocalError when using mutable default arguments
   Solution: Use None as the default and initialize the mutable object inside the function.
"""

# 7. Recommended Tools, Libraries, and Resources

"""
Tools and Libraries:
1. mypy: Static type checker for Python
2. pylint: Code analysis tool for detecting errors and enforcing coding standards
3. Black: Code formatter that adheres to PEP 8 style guide
4. functools: Module for higher-order functions and operations on callable objects

Resources:
1. "Fluent Python" by Luciano Ramalho
2. "Effective Python" by Brett Slatkin
3. Python Documentation: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
4. Real Python tutorials: https://realpython.com/python-kwargs-and-args/
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

# Example of optimizing a function with default arguments
def fibonacci_with_cache(n: int, cache: Dict[int, int] = {}) -> int:
    """
    Calculates the nth Fibonacci number using memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        cache (Dict[int, int], optional): A cache of previously computed values. Defaults to {}.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci_with_cache(n-1, cache) + fibonacci_with_cache(n-2, cache)
    cache[n] = result
    return result

# Main function to demonstrate concepts
def main() -> None:
    print("1. Basic default argument usage:")
    print(greet("Alice"))
    print(greet("Bob", greeting="Hi"))

    print("\n2. Calculating prices with default tax rate and discount:")
    print(f"Price: ${calculate_price(100)}")
    print(f"Price with 20% discount: ${calculate_price(100, discount=0.2)}")

    print("\n3. Creating a person with keyword arguments:")
    person = create_person(name="Charlie", age=30, city="New York")
    print(f"Person: {person}")

    print("\n4. Processing data with keyword-only arguments:")
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Sorted data: {process_data(data, sort=True)}")
    print(f"Reversed data: {process_data(data, reverse=True)}")

    print("\n5. Advanced function with various argument types:")
    result = advanced_function(1, 2, 3, 4, c=5, d=6, x=7, y=8)
    print(f"Advanced function result: {result}")

    print("\n6. Avoiding mutable default argument pitfall:")
    list1 = append_to_list(1)
    list2 = append_to_list(2)
    print(f"List 1: {list1}, List 2: {list2}")

    print("\n7. Partial function application:")
    print(f"Double of 5: {double(5)}")

    print("\n8. Database configuration with default values:")
    default_config = create_database_config()
    custom_config = create_database_config(host="db.example.com", port=5433, ssl=True)
    print(f"Default config: {default_config}")
    print(f"Custom config: {custom_config}")

    print("\n9. Advanced argument function:")
    adv_result = advanced_arg_function(1, 2, c=3, d=4, e=5, f=6)
    print(f"Advanced argument function result: {adv_result}")

    print("\n10. Performance comparison of Fibonacci implementations:")
    n = 30
    regular_time = benchmark(fibonacci_with_cache, n, {})
    cached_time = benchmark(fibonacci_with_cache, n)
    print(f"Regular time: {regular_time:.6f} seconds")
    print(f"Cached time: {cached_time:.6f} seconds")
    print(f"Speedup factor: {regular_time / cached_time:.2f}x")

if __name__ == "__main__":
    main()

"""
Conclusion:

This comprehensive guide covers the intricacies of default and keyword arguments in Python functions. These features are fundamental to creating flexible, readable, and maintainable code in Python. By mastering these concepts, developers can:

1. Design more versatile and user-friendly APIs
2. Improve code readability and reduce redundancy
3. Implement efficient function overloading and partial application
4. Create robust and adaptable software systems

Key takeaways:
- Default arguments provide sensible fallback values for optional parameters
- Keyword arguments enhance code clarity, especially for functions with many parameters
- Careful use of these features can lead to more pythonic and maintainable codebases
- Understanding potential pitfalls, like mutable default arguments, is crucial for writing bug-free code
- Advanced usage, including keyword-only arguments and positional-only parameters, offers fine-grained control over function interfaces

As Python continues to evolve, staying updated with best practices and emerging trends in function design is essential. The concepts covered in this guide form a solid foundation for writing efficient, clear, and flexible Python code across various domains and applications.

Remember that while these features offer great flexibility, they should be used judiciously. Always prioritize code readability and maintainability. When in doubt, refer to the Zen of Python: "Explicit is better than implicit."

For further exploration:
1. Experiment with different combinations of argument types in your own projects
2. Study how popular Python libraries and frameworks utilize these concepts
3. Keep an eye on Python Enhancement Proposals (PEPs) for future developments in function design

By mastering default and keyword arguments, you'll be well-equipped to write Python code that is both powerful and elegant, adapting to a wide range of use cases with ease.

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

if __name__ == "__main__":
    main()