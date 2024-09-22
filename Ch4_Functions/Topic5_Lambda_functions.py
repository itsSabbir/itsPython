# Functions - Lambda functions - in the Python Programming Language
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
from typing import Any, Callable, Dict, List, Union
import asyncio

# 1. Overview and Historical Context
"""
Lambda functions in Python are small, anonymous functions defined using the 'lambda' keyword.
They can have any number of arguments but can only contain a single expression.

Key aspects:
- Concise way to create small, one-time-use functions
- Often used with higher-order functions like map(), filter(), and reduce()
- Limited to simple expressions, not full function bodies

Historical context:
- Introduced in Python 1.1 (1994)
- Inspired by lambda calculus and functional programming concepts
- Named after the Greek letter λ used in lambda calculus
- Became increasingly important with the rise of functional programming in Python
- PEP 3113 (2007) considered removing lambda, but it was retained due to its utility
- Python 3.x has maintained lambda functions with minor syntactic changes

Lambda functions align with Python's philosophy of providing concise, expressive tools to developers.
They are particularly useful in functional programming paradigms and for creating callback functions.
"""

# 2. Syntax, Key Concepts, and Code Examples

# Basic lambda function
square = lambda x: x ** 2

# Lambda with multiple arguments
add = lambda x, y: x + y

# Lambda with conditional expression
is_even = lambda x: True if x % 2 == 0 else False

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Lambda with sorting
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])

# Lambda in list comprehension
numbers = [1, 2, 3, 4, 5]
squared_odd_numbers = [num ** 2 for num in numbers if (lambda x: x % 2 != 0)(num)]

# 3. Best Practices, Common Pitfalls, and Advanced Tips

"""
Best Practices:
1. Use lambda functions for simple, one-off operations
2. Prefer regular functions for complex logic or reusable code
3. Use meaningful variable names, even in short lambda functions
4. Combine lambda with built-in functions like map(), filter(), and sorted() for concise operations

Common Pitfalls:
1. Overusing lambda for complex operations, reducing readability
2. Attempting to use statements (e.g., assignment or loops) within lambda functions
3. Neglecting to handle potential exceptions in lambda functions
4. Using lambda when a simple function call would suffice

Advanced Tips:
1. Use lambda to create closure-like behavior
2. Combine lambda with partial function application for powerful function factories
3. Utilize lambda in key functions for custom sorting behavior
4. Leverage lambda in callback functions for event-driven programming
"""

# Example of lambda creating closure-like behavior
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

# Example of lambda with partial function application
from functools import partial

base_power = lambda x, y: x ** y
square = partial(base_power, y=2)
cube = partial(base_power, y=3)

# 4. Integration and Real-World Applications

"""
Real-world applications of lambda functions:

1. Data Processing:
   - Quick transformations in data analysis pipelines

2. GUI Programming:
   - Creating simple callback functions for event handlers

3. Functional Programming:
   - Implementing map-reduce operations in big data processing

4. Web Development:
   - Defining small utility functions in web frameworks

5. Machine Learning:
   - Custom loss functions or simple data transformations in ML pipelines

Example: A simple data processing pipeline using lambda functions
"""

def process_data(data, operations):
    """
    Applies a series of operations to the input data.
    
    Args:
        data (List[int]): Input data to process.
        operations (List[Callable]): List of lambda functions to apply.
    
    Returns:
        List[int]: Processed data.
    """
    result = data
    for op in operations:
        result = list(map(op, result))
    return result

# Usage in main function

# 5. Advanced Concepts and Emerging Trends

"""
Advanced Concepts:
1. Combining lambda with decorators for enhanced functionality
2. Using lambda in asynchronous programming with async/await syntax
3. Leveraging lambda in functional programming constructs like monads

Emerging Trends:
1. Integration with type hinting systems for improved static analysis
2. Potential syntax improvements for multi-line lambda functions (discussed but not implemented)
3. Growing use in data science and machine learning workflows
"""

# Example of lambda in asynchronous context
async def async_process(data, operation):
    """
    Asynchronously processes data using a lambda function.
    
    Args:
        data (List[int]): Input data to process.
        operation (Callable): Lambda function to apply.
    
    Returns:
        List[int]: Processed data.
    """
    return [await asyncio.to_thread(operation, item) for item in data]

# Usage in main function

# 6. FAQs and Troubleshooting

"""
Q1: Can lambda functions contain multiple expressions?
A1: No, lambda functions are restricted to a single expression in Python.
    For multiple expressions, use a regular function.

Q2: How do I handle exceptions in lambda functions?
A2: You can use a try-except block within the lambda, but it's often clearer
    to use a regular function for operations that might raise exceptions.

Q3: Can I use type hints with lambda functions?
A3: Direct type hinting for lambda functions is not supported, but you can
    assign a lambda to a variable and type-hint that variable.

Troubleshooting:
1. SyntaxError: "lambda cannot contain assignment"
   Solution: Lambda functions cannot contain statements. Use a regular function instead.

2. UnboundLocalError in lambda
   Solution: Be cautious with variable scoping. Lambda functions can access
   variables in their containing scope but cannot modify them.

3. Performance issues with complex lambda functions
   Solution: For complex operations, use regular functions which are often
   more readable and can be optimized more effectively by the Python interpreter.
"""

# 7. Recommended Tools, Libraries, and Resources

"""
Tools and Libraries:
1. functools: Provides higher-order functions and operations on callable objects
2. operator: Provides efficient alternatives to simple lambda functions
3. toolz: Functional programming tools extending Python's capabilities
4. pylint: Can help identify potential issues with lambda usage

Resources:
1. "Python Cookbook" by David Beazley and Brian K. Jones
2. "Functional Programming in Python" by David Mertz
3. Python Documentation: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
4. Real Python tutorial: https://realpython.com/python-lambda/
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

# Example of optimizing lambda vs regular function
def square_regular(x):
    return x ** 2

square_lambda = lambda x: x ** 2

# Usage in main function for performance comparison

# Main function to demonstrate concepts
async def main():
    print("1. Basic lambda usage:")
    print(f"Square of 5: {square(5)}")
    print(f"Sum of 3 and 4: {add(3, 4)}")
    print(f"Is 6 even? {is_even(6)}")

    print("\n2. Lambda with built-in functions:")
    print(f"Squared numbers: {squared_numbers}")
    print(f"Sorted pairs: {sorted_pairs}")

    print("\n3. Lambda in list comprehension:")
    print(f"Squared odd numbers: {squared_odd_numbers}")

    print("\n4. Lambda creating closure-like behavior:")
    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")

    print("\n5. Lambda with partial function application:")
    print(f"Square of 4: {square(4)}")
    print(f"Cube of 3: {cube(3)}")

    print("\n6. Data processing pipeline:")
    data = [1, 2, 3, 4, 5]
    operations = [
        lambda x: x * 2,
        lambda x: x + 1,
        lambda x: x ** 2
    ]
    processed_data = process_data(data, operations)
    print(f"Processed data: {processed_data}")

    print("\n7. Asynchronous lambda usage:")
    async_data = [1, 2, 3, 4, 5]
    async_result = await async_process(async_data, lambda x: x ** 2)
    print(f"Async processed data: {async_result}")

    print("\n8. Performance comparison:")
    test_value = 1000000
    regular_time = benchmark(square_regular, test_value)
    lambda_time = benchmark(square_lambda, test_value)
    print(f"Regular function time: {regular_time:.6f} seconds")
    print(f"Lambda function time: {lambda_time:.6f} seconds")
    print(f"Performance ratio: {regular_time / lambda_time:.2f}")

if __name__ == "__main__":
    asyncio.run(main())

"""
Conclusion:

This comprehensive guide covers the intricacies of lambda functions in Python. These concise,
anonymous functions provide a powerful tool for functional programming and quick, one-off operations.
Key takeaways include:

1. Lambda functions offer a compact syntax for simple, single-expression functions.
2. They are particularly useful with higher-order functions and in functional programming paradigms.
3. While powerful, lambda functions should be used judiciously to maintain code readability.
4. Understanding the limitations and best practices of lambda functions is crucial for effective usage.
5. Lambda functions integrate well with modern Python features, including asynchronous programming.

As Python continues to evolve, lambda functions remain a fundamental feature, enabling concise
and expressive code. Mastering lambda functions is essential for writing pythonic code and
leveraging functional programming techniques in Python.

Remember to use lambda functions where they enhance readability and conciseness, but don't
hesitate to use regular functions for more complex operations. As always, clarity and maintainability
should be prioritized in your code.

By mastering lambda functions, you'll have a powerful tool in your Python programming toolkit,
enabling you to write more expressive and functional code.

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

Your contributions help keep this resource up-to-date and valuable for the Python community.
Thank you for your support!
"""