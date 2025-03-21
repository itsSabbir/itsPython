"""
Exception Handling - Raising Exceptions - in the Python Programming Language
============================================================================

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
Raising exceptions is a fundamental aspect of Python's exception handling mechanism. It allows developers to signal errors or exceptional conditions in their code, providing a structured way to handle and propagate errors.

Historical context:
- Exception handling has been a part of Python since its early versions.
- The 'raise' statement for raising exceptions was introduced in Python 1.5 (1997).
- Python 2.5 (2006) introduced the 'with' statement, which integrates well with exception handling.
- Python 3.0 (2008) made some changes to exception handling, such as making all exceptions inherit from BaseException.

Significance:
- Allows for clear communication of error conditions.
- Enables separation of error detection and error handling code.
- Facilitates the creation of robust and maintainable software.

Common use cases:
- Signaling invalid input or state.
- Indicating resource unavailability.
- Enforcing invariants or preconditions in functions and methods.
- Implementing custom error handling in libraries and frameworks.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import sys
from typing import Any, List

def basic_raise():
    """Demonstrate basic usage of raise statement."""
    x = -5
    if x < 0:
        raise ValueError("x must be non-negative")

def raise_from():
    """Demonstrate the use of raise...from for exception chaining."""
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid operation") from e

class CustomError(Exception):
    """A custom exception class."""
    def __init__(self, message: str, error_code: int):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

def raise_custom_exception():
    """Demonstrate raising a custom exception."""
    raise CustomError("An error occurred", 500)

def reraise_exception():
    """Demonstrate re-raising an exception."""
    try:
        1 / 0
    except ZeroDivisionError:
        print("Caught exception, re-raising...")
        raise

def raise_from_none():
    """Demonstrate using 'raise...from None' to suppress exception chaining."""
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError("Invalid operation") from None

async def async_raise():
    """Demonstrate raising exceptions in asynchronous code."""
    await asyncio.sleep(1)
    raise ValueError("Async error")

def demonstrate_raising_exceptions():
    """Demonstrate various techniques for raising exceptions."""
    print("1. Basic raise:")
    try:
        basic_raise()
    except ValueError as e:
        print(f"Caught: {e}")

    print("\n2. Raise...from:")
    try:
        raise_from()
    except ValueError as e:
        print(f"Caught: {e}")
        print(f"Original exception: {e.__cause__}")

    print("\n3. Custom exception:")
    try:
        raise_custom_exception()
    except CustomError as e:
        print(f"Caught custom error: {e.message}, code: {e.error_code}")

    print("\n4. Re-raising exception:")
    try:
        reraise_exception()
    except ZeroDivisionError:
        print("Caught re-raised exception")

    print("\n5. Raise...from None:")
    try:
        raise_from_none()
    except ValueError as e:
        print(f"Caught: {e}")
        print(f"Original exception suppressed: {e.__cause__ is None}")

    print("\n6. Async raise:")
    import asyncio
    asyncio.run(async_raise())

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Raise specific exceptions that accurately describe the error condition.
2. Use custom exceptions for domain-specific errors.
3. Include informative error messages when raising exceptions.
4. Use exception chaining (raise...from) to preserve context when re-raising exceptions.

Common Pitfalls:
1. Raising overly generic exceptions (e.g., using Exception instead of more specific types).
2. Catching and re-raising exceptions without preserving the original context.
3. Overusing custom exceptions when built-in exceptions would suffice.
4. Raising exceptions in __del__ methods, which can lead to problems during garbage collection.

Advanced Tips:
1. Use assert statements for debugging and enforcing invariants (they can be disabled in optimized mode).
2. Implement custom exception hierarchies for complex libraries or applications.
3. Use sys.exc_info() for detailed exception information in exception handling code.
4. Leverage the traceback module for advanced stack trace handling when raising exceptions.
"""

import traceback

def validate_age(age: int) -> None:
    """
    Validate age using assert statement.
    
    This function demonstrates the use of assertions for invariant checking.
    """
    assert 0 <= age <= 120, "Invalid age"

class DatabaseError(Exception):
    """Base class for database-related exceptions."""
    pass

class ConnectionError(DatabaseError):
    """Raised when a database connection fails."""
    pass

class QueryError(DatabaseError):
    """Raised when a database query fails."""
    pass

def simulate_database_operation():
    """Simulate a database operation with custom exception hierarchy."""
    try:
        # Simulate a failed connection
        raise ConnectionError("Failed to connect to the database")
    except ConnectionError as e:
        # Re-raise with additional context
        raise QueryError("Query execution failed") from e

def advanced_exception_raising():
    """Demonstrate advanced exception raising techniques."""
    try:
        validate_age(150)
    except AssertionError as e:
        print(f"Assertion failed: {e}")

    try:
        simulate_database_operation()
    except DatabaseError as e:
        print(f"Database operation failed: {e}")
        print(f"Original error: {e.__cause__}")

    # Demonstrate traceback handling
    try:
        1 / 0
    except ZeroDivisionError:
        print("Traceback:")
        traceback.print_exc()

"""
4. Integration and Real-World Applications
------------------------------------------
Raising exceptions is crucial in many real-world applications:

1. API development: Signaling errors in REST APIs.
2. Data validation: Raising exceptions for invalid input data.
3. Resource management: Indicating resource unavailability.
4. Plugin systems: Communicating errors in plugin execution.

Real-world example: A function to validate and process user input
"""

import re
from typing import Dict

class ValidationError(Exception):
    """Custom exception for input validation errors."""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

def validate_user_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate and process user input data.

    This function demonstrates exception raising in a real-world scenario.
    """
    processed_data = {}

    # Validate name
    if 'name' not in data:
        raise ValidationError('name', "Name is required")
    if not isinstance(data['name'], str) or len(data['name']) < 2:
        raise ValidationError('name', "Name must be a string with at least 2 characters")
    processed_data['name'] = data['name'].strip()

    # Validate email
    if 'email' not in data:
        raise ValidationError('email', "Email is required")
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, data['email']):
        raise ValidationError('email', "Invalid email format")
    processed_data['email'] = data['email'].lower()

    # Validate age
    if 'age' in data:
        try:
            age = int(data['age'])
            if age < 0 or age > 120:
                raise ValueError
            processed_data['age'] = age
        except ValueError:
            raise ValidationError('age', "Age must be a number between 0 and 120")

    return processed_data

def demonstrate_real_world_application():
    """Demonstrate a real-world application of raising exceptions."""
    test_data = [
        {'name': 'John Doe', 'email': 'john@example.com', 'age': '30'},
        {'name': 'J', 'email': 'invalid-email', 'age': '200'},
        {'email': 'alice@example.com', 'age': '25'},
        {'name': 'Bob Smith', 'email': 'bob@example.com', 'age': 'not-a-number'}
    ]

    for data in test_data:
        try:
            processed = validate_user_input(data)
            print(f"Validated data: {processed}")
        except ValidationError as e:
            print(f"Validation error: {e}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Exception Groups: Python 3.11 introduced Exception Groups for handling multiple exceptions simultaneously.
2. Structural Pattern Matching: Python 3.10 introduced pattern matching, which can be used with exception handling.
3. Typed exceptions: Improved support for type hinting with exceptions.
4. Context variables: Using contextvars module for exception context in asynchronous code.
"""

import sys

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts in raising exceptions."""
    # Exception Groups (Python 3.11+)
    if sys.version_info >= (3, 11):
        def raise_group():
            raise ExceptionGroup(
                "multiple_errors",
                [ValueError("error 1"),
                 TypeError("error 2"),
                 OSError("error 3")]
            )

        try:
            raise_group()
        except* ValueError as e:
            print(f"Caught ValueError: {e}")
        except* TypeError as e:
            print(f"Caught TypeError: {e}")
        except* OSError as e:
            print(f"Caught OSError: {e}")

    # Structural Pattern Matching (Python 3.10+)
    if sys.version_info >= (3, 10):
        def match_exception(exc):
            match exc:
                case ValueError():
                    print("Matched ValueError")
                case TypeError():
                    print("Matched TypeError")
                case Exception():
                    print("Matched generic Exception")

        try:
            1 / 0
        except Exception as e:
            match_exception(e)

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I create custom exceptions versus using built-in exceptions?
A: Create custom exceptions for domain-specific errors or when you need to include additional context. Use built-in exceptions for general error conditions.

Q: How can I include more context when raising an exception?
A: Use exception chaining with 'raise...from' or create custom exceptions with additional attributes.

Q: Is it okay to use assertions in production code?
A: Assertions are typically used for debugging and can be disabled in optimized mode. For production error checking, use explicit if statements and raise exceptions.

Troubleshooting:
1. If exception context is lost, ensure you're using 'raise...from' when re-raising exceptions.
2. For hard-to-debug exceptions, use logging and consider using a debugger to step through the code.
3. If exceptions are not propagating as expected, check for broad except clauses that might be catching and silencing them.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- traceback: Built-in module for working with stack traces.
- logging: Built-in module for flexible event logging, useful for recording exception information.
- pytest: Testing framework with good support for testing exception raising.
- better_exceptions: Library for pretty-printing exception information.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones
- "Effective Python" by Brett Slatkin
- Python's official documentation on Exceptions: https://docs.python.org/3/tutorial/errors.html
- Real Python's guide on Raising and Handling Exceptions: https://realpython.com/python-exceptions/
- PEP 3134 - Exception Chaining and Embedded Tracebacks: https://www.python.org/dev/peps/pep-3134/

8. Performance Analysis and Optimization
----------------------------------------
Raising exceptions can have performance implications, especially when used in tight loops or performance-critical code paths.
"""

import time
import cProfile
import pstats
from io import StringIO

def benchmark_exception_raising(num_iterations: int = 100000):
    """
    Benchmark different approaches to error handling.
    """
    def with_exception():
        try:
            raise ValueError("Error")
        except ValueError:
            pass

    def with_conditional():
        error_condition = True
        if error_condition:
            return "Error"

    # Benchmark exception raising
    start_time = time.time()
    for _ in range(num_iterations):
        with_exception()
    exception_time = time.time() - start_time

    # Benchmark conditional check
    start_time = time.time()
    for _ in range(num_iterations):
        with_conditional()
    conditional_time = time.time() - start_time

    print(f"Exception raising time: {exception_time:.4f} seconds")
    print(f"Conditional check time: {conditional_time:.4f} seconds")

def profile_exception_raising():
    """
    Profile exception raising to identify performance bottlenecks.
    """
    def function_with_exceptions():
        for i in range(1000):
            try:
                if i % 2 == 0:
                    raise ValueError("Even number")
                else:
                    raise TypeError("Odd number")
            except (ValueError, TypeError):
                pass

    profiler = cProfile.Profile()
    profiler.enable()
    function_with_exceptions()
    profiler.disable()
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

"""
Performance Considerations:
1. Raising exceptions is generally slower than conditional checks for error handling.
2. Exception handling can have a significant performance impact in tight loops.
3. The performance cost of raising an exception is higher than that of a simple function call.

Optimization Strategies:
1. Use exceptions for exceptional cases, not for regular flow control.
2. Consider using return codes or sentinel values for expected error conditions in performance-critical sections.
3. When possible, move exception handling outside of tight loops.
4. Use more specific exception types to avoid unnecessary exception handling overhead.

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
- Relevance to the main topic of raising exceptions in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to raising exceptions.
    """
    print("1. Basic Exception Raising Techniques:")
    demonstrate_raising_exceptions()

    print("\n2. Advanced Exception Raising Techniques:")
    advanced_exception_raising()

    print("\n3. Real-World Application:")
    demonstrate_real_world_application()

    print("\n4. Advanced Concepts:")
    demonstrate_advanced_concepts()

    print("\n5. Performance Benchmarking:")
    benchmark_exception_raising()

    print("\n6. Profiling Exception Raising:")
    profile_exception_raising()

if __name__ == "__main__":
    main()