"""
Exception Handling - Custom Exception Classes - in the Python Programming Language
==================================================================================

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
Custom exception classes in Python allow developers to define their own exception types, enabling more precise and meaningful error handling. This feature is an integral part of Python's exception handling mechanism, which has been a core language feature since its inception.

Historical context:
- Exception handling was introduced in Python 1.5 (1997).
- Custom exceptions became more prevalent with the introduction of new-style classes in Python 2.2 (2001).
- PEP 352 (Python 2.5, 2006) introduced changes to exception handling, including the ability to add attributes to exception instances.

Significance:
- Custom exceptions allow for more granular and descriptive error handling.
- They enable better separation of concerns and improve code readability.
- Custom exceptions facilitate the creation of domain-specific error hierarchies.

Common use cases:
- Representing application-specific error conditions.
- Creating hierarchies of related exceptions for complex systems.
- Enhancing error reporting with additional context or metadata.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import sys
from typing import Any, Dict, List, Optional

class CustomError(Exception):
    """
    Base class for custom exceptions in this module.
    
    Attributes:
        message -- explanation of the error
        code -- optional error code
    """
    def __init__(self, message: str, code: Optional[int] = None):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"[Error {self.code}]: {self.message}" if self.code else self.message

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large."""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small."""
    pass

def check_value(value: int) -> None:
    """
    Check if the given value is within an acceptable range.
    
    Args:
        value (int): The value to check.
    
    Raises:
        ValueTooLargeError: If the value is greater than 100.
        ValueTooSmallError: If the value is less than 10.
    """
    if value > 100:
        raise ValueTooLargeError("Value is too large", code=101)
    elif value < 10:
        raise ValueTooSmallError("Value is too small", code=102)
    print(f"Value {value} is acceptable.")

def demonstrate_basic_usage():
    """Demonstrate basic usage of custom exceptions."""
    test_values = [5, 50, 150]
    
    for value in test_values:
        try:
            check_value(value)
        except ValueTooLargeError as e:
            print(f"Caught an exception: {e}")
        except ValueTooSmallError as e:
            print(f"Caught an exception: {e}")
        except CustomError as e:
            print(f"Caught a generic custom error: {e}")

class DatabaseError(CustomError):
    """Base class for database-related errors."""
    pass

class ConnectionError(DatabaseError):
    """Raised when a database connection fails."""
    pass

class QueryError(DatabaseError):
    """Raised when a database query fails."""
    def __init__(self, message: str, query: str, code: Optional[int] = None):
        super().__init__(message, code)
        self.query = query

    def __str__(self) -> str:
        return f"{super().__str__()}\nFailed query: {self.query}"

class Database:
    """A mock database class to demonstrate exception handling."""
    
    def __init__(self):
        self.connected = False
    
    def connect(self) -> None:
        """Simulate connecting to a database."""
        if not self.connected:
            # Simulate a connection error 50% of the time
            if __import__('random').random() < 0.5:
                raise ConnectionError("Failed to connect to the database", code=201)
            self.connected = True
            print("Connected to the database.")
        else:
            print("Already connected to the database.")
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """
        Simulate executing a database query.
        
        Args:
            query (str): The SQL query to execute.
        
        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing the query results.
        
        Raises:
            ConnectionError: If not connected to the database.
            QueryError: If the query execution fails.
        """
        if not self.connected:
            raise ConnectionError("Not connected to the database", code=202)
        
        # Simulate a query error for DELETE queries
        if query.strip().upper().startswith("DELETE"):
            raise QueryError("Delete operation not permitted", query, code=301)
        
        # Mock successful query execution
        return [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

def demonstrate_advanced_usage():
    """Demonstrate advanced usage of custom exceptions with a mock database."""
    db = Database()
    
    try:
        db.connect()
        result = db.execute_query("SELECT * FROM users")
        print(f"Query result: {result}")
        
        db.execute_query("DELETE FROM users WHERE id = 1")
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except QueryError as e:
        print(f"Query error: {e}")
    except DatabaseError as e:
        print(f"Generic database error: {e}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Create a custom base exception for your module or application.
2. Use descriptive names for your custom exceptions.
3. Include relevant error information in your custom exceptions.
4. Follow the Python style guide (PEP 8) for naming conventions.
5. Document your custom exceptions thoroughly.

Common Pitfalls:
1. Overusing custom exceptions for non-exceptional cases.
2. Creating too many specific exceptions, leading to complex error handling.
3. Not properly chaining exceptions when re-raising.
4. Catching too broad exception types (e.g., bare except clauses).

Advanced Tips:
1. Use exception chaining to preserve the original cause of an error.
2. Implement custom logic in exception classes for advanced error handling.
3. Utilize context managers (with statements) for resource management.
4. Consider using abstract base classes for exception hierarchies.
"""

from abc import ABC, abstractmethod
from contextlib import contextmanager

class RetryableError(CustomError, ABC):
    """Abstract base class for errors that can be retried."""
    
    @abstractmethod
    def can_retry(self) -> bool:
        """Determine if the operation can be retried."""
        pass

class TemporaryNetworkError(RetryableError):
    """Raised when a temporary network issue occurs."""
    
    def __init__(self, message: str, attempts: int):
        super().__init__(message)
        self.attempts = attempts
    
    def can_retry(self) -> bool:
        return self.attempts < 3

@contextmanager
def network_operation():
    """A context manager for network operations that may need to be retried."""
    attempts = 0
    while True:
        try:
            yield
            break
        except TemporaryNetworkError as e:
            attempts += 1
            if not e.can_retry():
                raise
            print(f"Retrying operation (attempt {attempts})...")

def demonstrate_advanced_techniques():
    """Demonstrate advanced techniques with custom exceptions."""
    
    def simulate_network_operation():
        if __import__('random').random() < 0.7:
            raise TemporaryNetworkError("Network timeout", attempts=1)
        print("Network operation successful.")
    
    try:
        with network_operation():
            simulate_network_operation()
    except TemporaryNetworkError as e:
        print(f"Operation failed after multiple attempts: {e}")

"""
4. Integration and Real-World Applications
------------------------------------------
Custom exceptions are widely used in various Python libraries and frameworks:

1. Django's exception hierarchy for HTTP errors (e.g., Http404, PermissionDenied).
2. SQLAlchemy's exception classes for database-related errors.
3. Requests library's exceptions for HTTP-related errors.

Real-world example: A simplified version of a RESTful API error handling system.
"""

from enum import Enum
from http import HTTPStatus
from typing import Any, Dict, Optional

class ErrorCode(Enum):
    """Enum representing various error codes in the API."""
    VALIDATION_ERROR = 1001
    AUTHENTICATION_ERROR = 2001
    AUTHORIZATION_ERROR = 2002
    RESOURCE_NOT_FOUND = 3001
    RATE_LIMIT_EXCEEDED = 4001

class APIError(CustomError):
    """Base class for API-related errors."""
    
    def __init__(self, message: str, code: ErrorCode, http_status: HTTPStatus, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code.value)
        self.http_status = http_status
        self.details = details or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the error to a dictionary for JSON serialization."""
        return {
            "error": {
                "code": self.code,
                "message": self.message,
                "details": self.details
            }
        }

class ValidationError(APIError):
    """Raised when request validation fails."""
    
    def __init__(self, message: str, details: Dict[str, Any]):
        super().__init__(message, ErrorCode.VALIDATION_ERROR, HTTPStatus.BAD_REQUEST, details)

class AuthenticationError(APIError):
    """Raised when authentication fails."""
    
    def __init__(self, message: str):
        super().__init__(message, ErrorCode.AUTHENTICATION_ERROR, HTTPStatus.UNAUTHORIZED)

class AuthorizationError(APIError):
    """Raised when the user is not authorized to perform an action."""
    
    def __init__(self, message: str):
        super().__init__(message, ErrorCode.AUTHORIZATION_ERROR, HTTPStatus.FORBIDDEN)

class ResourceNotFoundError(APIError):
    """Raised when a requested resource is not found."""
    
    def __init__(self, resource_type: str, resource_id: Any):
        message = f"{resource_type} with id {resource_id} not found"
        super().__init__(message, ErrorCode.RESOURCE_NOT_FOUND, HTTPStatus.NOT_FOUND)

class RateLimitExceededError(APIError):
    """Raised when the API rate limit is exceeded."""
    
    def __init__(self, limit: int, reset_time: int):
        message = f"Rate limit of {limit} requests exceeded. Try again in {reset_time} seconds."
        super().__init__(message, ErrorCode.RATE_LIMIT_EXCEEDED, HTTPStatus.TOO_MANY_REQUESTS, {"limit": limit, "reset_time": reset_time})

def api_endpoint(user_id: int, resource_id: int):
    """Simulate an API endpoint with various error conditions."""
    if user_id < 0:
        raise ValidationError("Invalid user ID", {"user_id": "Must be a positive integer"})
    if user_id == 0:
        raise AuthenticationError("Invalid authentication token")
    if user_id % 2 == 0:
        raise AuthorizationError("User does not have permission to access this resource")
    if resource_id == 404:
        raise ResourceNotFoundError("User", resource_id)
    if resource_id == 429:
        raise RateLimitExceededError(100, 3600)
    
    return {"user_id": user_id, "resource_id": resource_id, "data": "Some API response data"}

def handle_api_error(error: APIError):
    """Handle API errors and return appropriate responses."""
    error_dict = error.to_dict()
    print(f"HTTP Status: {error.http_status}")
    print(f"Error Response: {error_dict}")
    # In a real API, you would return this response to the client

def demonstrate_real_world_application():
    """Demonstrate a real-world application of custom exceptions in an API setting."""
    test_cases = [
        (-1, 1),    # ValidationError
        (0, 1),     # AuthenticationError
        (2, 1),     # AuthorizationError
        (1, 404),   # ResourceNotFoundError
        (1, 429),   # RateLimitExceededError
        (1, 1),     # Successful case
    ]
    
    for user_id, resource_id in test_cases:
        try:
            result = api_endpoint(user_id, resource_id)
            print(f"API call successful: {result}")
        except APIError as e:
            handle_api_error(e)
        print("---")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Async exception handling: With the rise of asynchronous programming in Python, handling exceptions in async code has become increasingly important.
2. Context-dependent exceptions: Implementing exceptions that behave differently based on the context in which they're raised.
3. Exception logging and monitoring: Integrating custom exceptions with logging and monitoring systems for better error tracking and analysis.
"""

import asyncio
import logging
from contextvars import ContextVar

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Context variable to store the current operation context
current_context = ContextVar("current_context", default="default")

class ContextAwareError(CustomError):
    """An error class that's aware of the current execution context."""
    
    def __init__(self, message: str, context: Optional[str] = None):
        super().__init__(message)
        self.context = context or current_context.get()
    
    def __str__(self):
        return f"[{self.context}] {self.message}"

async def async_operation(value: int):
    """An asynchronous operation that may raise an exception."""
    await asyncio.sleep(0.1)  # Simulate some async work
    if value % 2 == 0:
        raise ContextAwareError("Even values are not allowed")
    return value * 2

async def process_values(values: List[int]):
    """Process a list of values asynchronously with error handling."""
    tasks = [async_operation(value) for value in values]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for value, result in zip(values, results):
        if isinstance(result, Exception):
            logger.error(f"Error processing value {value}: {result}")
        else:
            logger.info(f"Processed value {value}: {result}")

class ExceptionCounter:
    """A context manager that counts the number of exceptions raised."""
    
    def __init__(self):
        self.count = 0
        self.exceptions = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.count += 1
            self.exceptions.append((exc_type, exc_value))
        return False  # Re-raise the exception

async def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts and emerging trends in exception handling."""
    
    # Async exception handling
    values = [1, 2, 3, 4, 5]
    current_context.set("async_processing")
    await process_values(values)
    
    # Context-dependent exceptions
    def risky_operation(value):
        current_context.set(f"operation_{value}")
        if value < 0:
            raise ContextAwareError("Negative values are not allowed")
        return value * 2
    
    for val in [-1, 2, -3, 4]:
        try:
            result = risky_operation(val)
            logger.info(f"Operation result: {result}")
        except ContextAwareError as e:
            logger.error(str(e))
    
    # Exception logging and monitoring
    with ExceptionCounter() as counter:
        try:
            raise ValueError("First error")
        except ValueError:
            logger.exception("Caught ValueError")
        
        try:
            raise TypeError("Second error")
        except TypeError:
            logger.exception("Caught TypeError")
    
    logger.info(f"Total exceptions caught: {counter.count}")
    for exc_type, exc_value in counter.exceptions:
        logger.info(f"Exception type: {exc_type.__name__}, message: {str(exc_value)}")

"""
6. FAQs and Troubleshooting
---------------------------
Q1: When should I create a custom exception?
A1: Create a custom exception when you need to represent an error condition specific to your application or library that isn't adequately covered by built-in exceptions. This allows for more precise error handling and can provide better context to users of your code.

Q2: How do I choose between raising an exception and returning an error code?
A2: In Python, it's generally preferred to raise exceptions for error conditions rather than returning error codes. Exceptions provide more context, are harder to ignore, and allow for centralized error handling. Use exceptions for exceptional conditions and return values for expected outcomes.

Q3: How can I add custom attributes to my exceptions?
A3: You can add custom attributes by defining them in your exception class's __init__ method. For example:

class CustomError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

Q4: How do I properly chain exceptions?
A4: Use the `raise ... from ...` syntax to chain exceptions. This preserves the original exception as the __cause__ of the new exception:

try:
    # Some operation that may raise an exception
    raise ValueError("Invalid value")
except ValueError as e:
    raise CustomError("A custom error occurred") from e

Troubleshooting Guide:
1. Exception not being caught:
   - Ensure you're catching the correct exception type.
   - Check if the exception is being raised in a different thread or async context.

2. Too many exceptions being raised:
   - Review your code for proper error checking and handling.
   - Consider using context managers (with statements) for resource management.

3. Exception handling affecting performance:
   - Avoid using exceptions for flow control in performance-critical code.
   - Use profiling tools to identify bottlenecks in exception handling.

4. Difficulty in debugging complex exception chains:
   - Use logging to track exception propagation.
   - Utilize debugger features like exception breakpoints.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. traceback module: For extracting, formatting, and printing exceptions and stack traces.
2. logging module: For integrating exception handling with application logging.
3. pytest: Testing framework with excellent support for testing exception handling.
4. sentry-sdk: For error tracking and performance monitoring in production environments.
5. better_exceptions: Library for pretty-printing exception information during development.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (Chapter 14: Testing, Debugging, and Exceptions)
- "Effective Python" by Brett Slatkin (Item 51: Compose Multiple Contexts in Context Managers)
- Python's official documentation on Exceptions: https://docs.python.org/3/tutorial/errors.html
- Real Python's guide on Python exceptions: https://realpython.com/python-exceptions/
- PEP 3134 – Exception Chaining and Embedded Tracebacks: https://www.python.org/dev/peps/pep-3134/

8. Performance Analysis and Optimization
----------------------------------------
When working with custom exceptions, it's important to consider their performance implications, especially in performance-critical applications.

Performance Considerations:
1. Exception handling can be slower than regular code execution.
2. Creating and raising exceptions has a performance cost.
3. Deeply nested try-except blocks can impact performance.

Optimization Strategies:
1. Use exceptions for exceptional cases, not for regular control flow.
2. Prefer more specific exception types over general ones to avoid unnecessary exception handling.
3. Consider using a "look before you leap" (LBYL) approach instead of "easier to ask forgiveness than permission" (EAFP) in performance-critical sections.
4. Profile your code to identify any performance bottlenecks related to exception handling.

Example of optimizing exception handling:
"""

import time

def demonstrate_performance_optimization():
    """Demonstrate performance optimization techniques for exception handling."""
    
    # Suboptimal approach: Using exceptions for control flow
    def divide_with_exception(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')
    
    # Optimized approach: Check before division
    def divide_with_check(a, b):
        return a / b if b != 0 else float('inf')
    
    # Performance comparison
    def measure_performance(func, iterations=1000000):
        start_time = time.time()
        for _ in range(iterations):
            func(10, 2)
            func(10, 0)
        end_time = time.time()
        return end_time - start_time
    
    exception_time = measure_performance(divide_with_exception)
    check_time = measure_performance(divide_with_check)
    
    print(f"Time taken with exception handling: {exception_time:.4f} seconds")
    print(f"Time taken with pre-check: {check_time:.4f} seconds")
    print(f"Performance improvement: {(exception_time - check_time) / exception_time * 100:.2f}%")

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
- Relevance to the main topic of custom exception classes in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to custom exception classes.
    """
    print("Demonstrating basic usage of custom exceptions:")
    demonstrate_basic_usage()
    print("\nDemonstrating advanced usage of custom exceptions:")
    demonstrate_advanced_usage()
    print("\nDemonstrating advanced techniques with custom exceptions:")
    demonstrate_advanced_techniques()
    print("\nDemonstrating real-world application of custom exceptions:")
    demonstrate_real_world_application()
    print("\nDemonstrating advanced concepts and emerging trends:")
    asyncio.run(demonstrate_advanced_concepts())
    print("\nDemonstrating performance optimization:")
    demonstrate_performance_optimization()

if __name__ == "__main__":
    main()