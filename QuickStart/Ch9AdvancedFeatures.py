#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Advanced Features
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# In this section, we explore some of the advanced features of Python, 
# focusing on modules and techniques that enhance functionality, efficiency, 
# and code organization.

# Importing standard libraries to leverage advanced features
import itertools  # Provides functions that create iterators for efficient looping
import functools  # Higher-order functions for functional programming
import time  # Provides time-related functions for performance measurement
import asyncio  # Asynchronous programming library for concurrent execution
from typing import List, Dict, Callable, Any, Generator  # Type hinting for better code clarity

# Example 1: Using itertools for efficient looping
# The itertools module provides tools for creating iterators for efficient looping.
# These functions can be memory-efficient and can handle large datasets smoothly.
# Example: Using count() to create an infinite iterator
counter = itertools.count(start=0, step=1)  # Creates an infinite counter starting from 0, incrementing by 1
print(next(counter))  # Output: 0
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2

# Advanced tip: You can use itertools with other functions to create powerful data manipulation tools.
# For example, use itertools.takewhile to create an iterator that takes elements from a 
# given iterable as long as a specified condition is true.
limited_counter = itertools.takewhile(lambda x: x < 5, counter)  # Stops when x is no longer < 5
print(list(limited_counter))  # Output: [0, 1, 2, 3, 4]

# Example 2: Using functools for functional programming
# The functools module provides tools for higher-order functions and operations on callable objects.
# Example: Using lru_cache to memoize a function's results for improved performance.
@functools.lru_cache(maxsize=128)  # Caches up to 128 results to optimize repeated calls
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call to compute Fibonacci number

print(fibonacci(10))  # Output: 55 (computes Fibonacci of 10 efficiently due to caching)

# Best practice: Use memoization for functions that are called frequently with the same arguments, 
# particularly in recursive algorithms, to reduce redundant computations.

# Example 3: Using time for performance measurement
# The time module allows you to measure the performance of your code segments effectively.
start_time = time.time()  # Record the start time
# Simulating a time-consuming operation
sum(range(10**6))  # Example operation (summing numbers from 0 to 999999)
end_time = time.time()  # Record the end time
print(f"Operation took {end_time - start_time} seconds")  # Output: Time taken for the operation

# Example 4: Using asyncio for asynchronous programming
# asyncio is essential for writing concurrent code using the async/await syntax.
# This is particularly useful for I/O-bound tasks, such as web requests or file operations.
async def async_task(task_id: int):
    print(f"Starting task {task_id}")  # Print when a task starts
    await asyncio.sleep(2)  # Simulate a non-blocking I/O operation with sleep
    print(f"Task {task_id} completed")  # Print when a task completes

async def main():
    # Running multiple asynchronous tasks concurrently
    await asyncio.gather(async_task(1), async_task(2), async_task(3))  # Runs tasks 1, 2, and 3 concurrently

# Running the main function in an asyncio event loop
asyncio.run(main())  # Executes the main async function

# Use case: asyncio is especially beneficial for web scraping, API calls, and handling 
# numerous simultaneous connections without blocking the main thread.

# Example 5: Using type hinting for better code clarity
# Type hints improve code readability and maintainability, helping developers understand expected data types.
def process_data(data: List[Dict[str, Any]]) -> None:
    # Accepts a list of dictionaries and processes them
    for item in data:
        print(item)

# Calling the function with a properly typed list of dictionaries
sample_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
process_data(sample_data)  # Output: Each dictionary in sample_data

# Advanced insight: Type hints are not enforced at runtime but can be checked with tools like mypy,
# making them invaluable for large codebases and collaborative projects.

# Example 6: Using generators for efficient memory usage
# Generators allow for lazy evaluation, meaning values are produced on-the-fly rather than stored in memory.
def generate_numbers() -> Generator[int, None, None]:
    for i in range(10):
        yield i  # Yielding values one at a time

# Using the generator
for number in generate_numbers():
    print(number, end=" ")  # Output: 0 1 2 3 4 5 6 7 8 9

# Use case: Generators are excellent for working with large datasets where 
# you don't want to load all data into memory at once, such as reading lines from a large file.

# In summary, utilizing these advanced features effectively can lead to more 
# efficient, readable, and maintainable code, allowing developers to leverage 
# Python's full potential in various domains and applications.


#=================================================================================
# 1. Iterators and Generators
#=================================================================================

# In this section, we explore the concepts of iterators and generators in Python.
# Both provide ways to iterate over sequences, but they have distinct implementations and use cases.

# Iterator example
class CountDown:
    # This class implements an iterator that counts down from a specified start value.
    def __init__(self, start):
        self.start = start  # Initialize the starting point for the countdown

    def __iter__(self):
        # This method is required for the object to be iterable.
        # It returns the iterator object itself (self).
        return self

    def __next__(self):
        # This method returns the next value from the iterator.
        # If the countdown reaches zero, it raises StopIteration to signal that iteration is complete.
        if self.start <= 0:
            raise StopIteration  # StopIteration is raised when the countdown is finished
        self.start -= 1  # Decrement the countdown
        return self.start + 1  # Return the current countdown value

# Using the iterator
print("Countdown:")
for num in CountDown(5):
    print(num, end=" ")  # Output: 5 4 3 2 1, iterates through the countdown
print()

# Use case for iterators:
# Iterators are particularly useful when you want to create custom iterable objects,
# especially when the data does not fit in memory or requires complex state management.

# Generator example
# Generators simplify the creation of iterators by allowing you to use the 'yield' statement.
# Here, we define a generator function to generate Fibonacci numbers.
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for _ in range(n):
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update the numbers for the next iteration

# Using the generator
print("Fibonacci sequence:")
for num in fibonacci(10):
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34, generates the first 10 Fibonacci numbers
print()

# Use case for generators:
# Generators are ideal for producing large sequences of data on-the-fly, 
# as they generate items one at a time and do not require all items to be stored in memory.

# Generator expression example
# A generator expression provides a concise way to create a generator without defining a function.
squares = (x**2 for x in range(10))  # Generates the squares of numbers from 0 to 9

print("Squares:", list(squares))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], converts the generator to a list

# Use case for generator expressions:
# They are particularly useful for memory efficiency when processing large datasets or performing transformations,
# as they yield values one at a time instead of creating a full list in memory.

# Tips:
# 1. Use generators for memory-efficient iteration over large sequences, as they consume less memory 
# and can work with infinite sequences without causing memory overflow.
# 2. Generator expressions are more memory-efficient than list comprehensions for large datasets,
# as they only generate values on demand and do not store the entire result set in memory.


#=================================================================================
# 2. Decorators
#=================================================================================

# In Python, decorators are a powerful tool that allows you to modify the behavior of functions or classes.
# They enable code reuse and can enhance the functionality of existing code without changing its structure.

import functools  # Import functools to utilize decorators and preserve metadata

# Example 1: Function decorator
# A function decorator is a callable that takes a function as an argument and returns a new function.
def uppercase_decorator(func: Callable) -> Callable:
    # The wrapper function modifies the behavior of the original function.
    @functools.wraps(func)  # Preserves the metadata of the original function
    def wrapper():
        result = func()  # Call the original function and store its result
        return result.upper()  # Convert the result to uppercase
    return wrapper  # Return the wrapper function

@uppercase_decorator  # Applying the decorator to the greet function
def greet() -> str:
    return "hello, world!"  # Original function that returns a greeting

print(greet())  # Output: HELLO, WORLD!
# The greet function is now wrapped by uppercase_decorator, modifying its return value.

# Use case:
# Function decorators are widely used for logging, access control, caching, and modifying return values.

# Example 2: Class decorator
# A class decorator modifies or enhances the functionality of a class.
def singleton(cls):
    instances = {}  # Dictionary to store instances of the decorated class
    @functools.wraps(cls)  # Preserve the metadata of the original class
    def get_instance(*args, **kwargs):
        # If the class is not already instantiated, create a new instance
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]  # Return the existing instance
    return get_instance  # Return the modified class

@singleton  # Applying the singleton decorator to the DatabaseConnection class
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected"  # Initialize connection attribute

# The DatabaseConnection class now ensures that only one instance exists.
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1.connection)  # Output: Connected
print(db1 is db2)  # Output: True
# Both db1 and db2 refer to the same instance due to the singleton pattern.

# Tip: Use functools.wraps to preserve metadata of the original function/class
# This is crucial for debugging and introspection, as it maintains the original function's name and docstring.

# Example 3: Decorator with arguments
# A decorator with arguments allows for more flexible decoration based on parameters.
def repeat(times: int) -> Callable:
    # The outer function takes the arguments and returns a decorator.
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)  # Preserve the original function's metadata
        def wrapper(*args, **kwargs):
            for _ in range(times):  # Repeat the function call 'times' number of times
                result = func(*args, **kwargs)  # Call the original function
            return result  # Return the result of the last call (if needed)
        return wrapper  # Return the wrapper function
    return decorator  # Return the decorator

@repeat(3)  # Apply the repeat decorator with an argument
def say_hello(name: str) -> None:
    print(f"Hello, {name}!")  # Print a greeting

say_hello("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
# The say_hello function is now called three times due to the decorator.

# Tip: Use decorator factories (decorators with arguments) for more flexible decorators
# This approach enhances reusability and configurability of decorators, allowing you to create more dynamic behavior.

#=================================================================================
# 3. Context Managers
#=================================================================================

# Context managers are a powerful feature in Python that enable resource management 
# and ensure proper cleanup of resources such as file handles, network connections, etc.
# They are typically used with the 'with' statement to wrap the execution of a block of code 
# and automatically handle setup and teardown actions.

# Example 1: Custom Context Manager Using a Class
# The following class, FileManager, is designed to manage file operations safely.
class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename  # The name of the file to manage
        self.mode = mode          # The mode in which to open the file (e.g., 'r', 'w', 'a')
        self.file = None         # Placeholder for the file object, initialized to None

    def __enter__(self):
        # This method is called when the execution enters the context of the 'with' statement.
        self.file = open(self.filename, self.mode)  # Open the file and assign it to self.file
        return self.file  # Return the file object for use within the context

    def __exit__(self, exc_type, exc_value, traceback):
        # This method is called when the execution leaves the context of the 'with' statement.
        if self.file:
            self.file.close()  # Ensure the file is closed, even if an exception occurred

# Using the custom context manager
# This block uses the FileManager context manager to write to a file safely.
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')  # Write content to the file. The file will be automatically closed after this block.

# Example 2: Context Manager Using contextlib
# The contextlib module provides utilities for creating context managers more easily.
# Here, we define a context manager function using the @contextmanager decorator.
from contextlib import contextmanager

@contextmanager
def temp_file(filename: str):
    # This function manages a temporary file.
    try:
        f = open(filename, 'w')  # Attempt to open the file in write mode
        yield f  # Yield the file object for use within the context
    finally:
        f.close()  # Ensure the file is closed when the block is exited, even if an error occurred

# Using the contextlib-based context manager
# This block uses the temp_file context manager to write temporary content.
with temp_file('temp.txt') as f:
    f.write('Temporary content')  # Write content to the temporary file

# Tip: Use context managers for resource management and cleanup
# They help in managing resources efficiently, ensuring they are released correctly 
# without requiring manual intervention, which can lead to memory leaks or file corruption 
# if not handled properly. This is especially important in long-running applications.

# Advanced Insight:
# Context managers can also handle exceptions gracefully. 
# In the __exit__ method, the parameters 'exc_type', 'exc_value', and 'traceback' 
# can be used to manage exceptions raised within the 'with' block.
# For example, if you want to log errors or prevent certain exceptions from propagating,
# you can modify the __exit__ method to handle these scenarios.

# Example of handling exceptions in a context manager
class ExceptionHandlingFileManager:
    def __enter__(self):
        self.file = open('error_log.txt', 'w')  # Open a log file
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:  # If an exception occurred
            self.file.write(f"Error: {exc_value}\n")  # Log the error
        self.file.close()  # Close the log file regardless of success or failure

# Using the ExceptionHandlingFileManager
with ExceptionHandlingFileManager() as log_file:
    raise ValueError("An example exception")  # This will be logged

# In this example, the custom context manager logs exceptions while managing file resources.
# By understanding and leveraging context managers, developers can write cleaner, 
# more reliable code that effectively manages resources and handles errors.

#=================================================================================
# 4. Coroutines and Asyncio
#=================================================================================

# In Python, coroutines and the asyncio library facilitate asynchronous programming,
# allowing for concurrent execution of I/O-bound tasks without blocking the main thread.
# This section illustrates the use of async and await keywords with practical examples.

# Example 1: Defining an asynchronous function (coroutine)
# The 'async' keyword defines a coroutine, allowing for non-blocking operations.
# This coroutine simulates fetching data from a given URL.
async def fetch_data(url: str) -> str:
    print(f"Start fetching {url}")  # Indicate the start of the data fetching process
    await asyncio.sleep(2)  # Simulate a time-consuming I/O operation (like network request)
    print(f"Finished fetching {url}")  # Indicate the completion of the fetching process
    return f"Data from {url}"  # Return the simulated data fetched from the URL

# Example 2: Main coroutine that manages multiple fetch operations
# The 'main' coroutine orchestrates fetching data from multiple URLs concurrently.
async def main():
    # List of URLs to fetch data from
    urls = ['http://example.com', 'http://example.org', 'http://example.net']
    
    # Create tasks for fetching data asynchronously using asyncio.create_task()
    # This allows each fetch operation to run concurrently.
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    
    # Gather the results of all tasks and wait for them to complete.
    # This blocks until all tasks are finished and returns their results.
    results = await asyncio.gather(*tasks)
    
    # Output the results of the data fetching
    for result in results:
        print(result)

# Example 3: Running the event loop to execute the main coroutine
# asyncio.run() sets up the event loop, runs the specified coroutine, and handles cleanup.
# This function is the entry point for executing asynchronous code.
# It's essential to use asyncio.run() as it ensures proper management of the event loop.
# Use this only at the top level of the script, as it cannot be called within another coroutine.
asyncio.run(main())

# Output:
# Start fetching http://example.com
# Start fetching http://example.org
# Start fetching http://example.net
# Finished fetching http://example.com
# Finished fetching http://example.org
# Finished fetching http://example.net
# Data from http://example.com
# Data from http://example.org
# Data from http://example.net

# Tip: Use asyncio for I/O-bound concurrent programming
# Asyncio excels in scenarios where tasks involve waiting for external resources,
# such as network requests or file I/O. It is not suitable for CPU-bound tasks, 
# which can block the event loop. In those cases, consider using multiprocessing or concurrent.futures.
# As a best practice, always handle exceptions within coroutines to avoid unhandled promise rejections,
# and keep an eye on the scalability of your coroutines to ensure efficient use of system resources.

#=================================================================================
# 5. Metaclasses
#=================================================================================

# Metaclasses in Python are a powerful feature that allows developers to customize
# class creation. They define the behavior of a class, similar to how classes define 
# the behavior of their instances. A common use case for metaclasses is to enforce 
# certain patterns, like the Singleton pattern, which restricts instantiation of 
# a class to a single instance.

# Example 1: SingletonMetaclass
class SingletonMeta(type):
    # A class-level dictionary to hold instances of classes
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # The __call__ method allows the metaclass to control the instantiation of the class.
        # Here, we check if an instance of the class already exists.
        if cls not in cls._instances:
            # If not, we create a new instance and store it in the _instances dictionary.
            cls._instances[cls] = super().__call__(*args, **kwargs)
        # If an instance already exists, we return the existing instance.
        return cls._instances[cls]

# Example 2: Singleton Class
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        # Initializing an attribute. All instances will share the same value.
        self.value = None

# Usage of the Singleton class
s1 = Singleton()  # First instantiation creates a new instance
s2 = Singleton()  # This will return the same instance as s1

# The following line checks if s1 and s2 are the same instance.
print(s1 is s2)  # Output: True
# This confirms that both variables reference the same object, adhering to the Singleton pattern.

# Advanced Tip: Metaclasses can be used to enforce design patterns, logging, 
# validation, and automatic registration of classes. However, they introduce 
# complexity; hence they should be used judiciously. 

# Uncommon Insight: The __init__ method of the metaclass (SingletonMeta in this case) 
# can also be overridden to perform operations when the class itself is defined, 
# allowing for more complex configurations or validations at class creation time.

# Potential Pitfalls: 
# 1. Overusing metaclasses can lead to code that is difficult to understand and maintain.
# 2. When using metaclasses, ensure that you document their purpose clearly, 
# as their abstract nature can obscure class behavior.
# 3. Be cautious with inheritance; ensure that the behavior of subclasses aligns with 
# the intended metaclass logic to avoid unexpected behaviors.

#=================================================================================
# 6. Descriptor Protocol
#=================================================================================

# Descriptors provide a powerful way to manage attribute access and validation in Python.
# They allow you to customize the behavior of attribute access through method overrides.

# The Validator class is a descriptor that validates the value of an attribute to ensure 
# it falls within a specified range (min_value and max_value).

class Validator:
    def __init__(self, min_value: float, max_value: float):
        # Initialize the validator with minimum and maximum allowable values.
        # This encapsulates validation logic for a range.
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute.
        # It saves the attribute name for later use in validation.
        self.name = name  # Store the attribute name for reference in other methods

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed.
        # It retrieves the value from the instance's __dict__.
        if instance is None:
            return self  # Return the descriptor itself if accessed through the class
        return instance.__dict__.get(self.name)  # Return the stored value or None

    def __set__(self, instance, value):
        # This method is called when a new value is assigned to the attribute.
        # It validates the value against the defined min and max before setting it.
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{self.name} must be between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value  # Store the validated value in the instance's __dict__

# The Person class demonstrates how to use the Validator descriptor to manage an attribute.
class Person:
    age = Validator(0, 150)  # The age attribute is validated to be between 0 and 150

    def __init__(self, name: str, age: int):
        # The constructor initializes the Person object with a name and age.
        self.name = name  # Set the name attribute directly
        self.age = age  # The age attribute is managed by the Validator descriptor

# Usage of the Person class with the Validator descriptor
person = Person("Alice", 30)  # Create a new Person object with name "Alice" and age 30
print(person.age)  # Output: 30, retrieves the age using the __get__ method

# Example of failed validation:
# Uncommenting the next line would raise a ValueError because 200 is outside the valid range
# person.age = 200  # This would raise a ValueError

# Advanced Tip: Descriptors are useful for enforcing constraints on class attributes,
# and they can be reused across multiple classes, enhancing code modularity and reducing duplication.
# When using descriptors, consider their placement and the implications of attribute access,
# especially in inheritance scenarios where the attribute might be overshadowed.

# Potential Pitfalls:
# If a descriptor is not correctly defined (e.g., missing __get__ or __set__ methods), 
# it can lead to unexpected behavior. Always ensure that descriptors are tested thoroughly 
# in the context where they are applied. Additionally, be mindful of performance overheads 
# with descriptors as they add an extra layer of function calls for attribute access.

#=================================================================================
# 7. Function Caching
#=================================================================================

# Function caching is a powerful optimization technique that stores the results of expensive function calls.
# By caching, subsequent calls with the same arguments can return results instantly without recomputation.
# The functools module in Python provides the lru_cache decorator to achieve this easily.

import functools  # Importing functools to access the lru_cache decorator
import time  # Importing time to measure execution time of function calls

# Applying the lru_cache decorator to the fibonacci_cached function.
# The 'maxsize' parameter controls the number of cached results stored; None means unlimited.
# LRU (Least Recently Used) cache will evict the least recently used entries when it reaches the cache size limit.
@functools.lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    # Base case: the Fibonacci sequence defines that the first two numbers are 0 and 1.
    if n < 2:
        return n  # For n = 0, return 0; for n = 1, return 1.

    # Recursive call to calculate Fibonacci numbers using previously cached results.
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Measure execution time to demonstrate the performance gain from caching
start = time.time()  # Record the start time before calling the cached function
print(fibonacci_cached(100))  # Calculate the 100th Fibonacci number
end = time.time()  # Record the end time after the function call

# Calculate and print the time taken to execute the function
print(f"Time taken: {end - start} seconds")  # Output the time elapsed for function execution

# Output: The 100th Fibonacci number and the time taken for the calculation.

# Tip: Use lru_cache for memoization of expensive function calls
# Memoization improves performance by storing results of function calls based on input arguments.
# It is particularly beneficial for recursive functions like Fibonacci where many overlapping calculations occur.

# Use cases:
# - Any recursive algorithm with overlapping subproblems, such as Fibonacci, factorial, or combinatorial problems.
# - API calls or database queries where results can be cached to avoid repeated expensive lookups.
# - Computations that involve heavy calculations but can be optimized by caching.

# Potential pitfalls:
# - Caching consumes memory, so be mindful of the cache size, especially with large input sets.
# - The lru_cache might not be suitable for functions with mutable default arguments, as their state can change unexpectedly.
# - When debugging, cached results may lead to confusion if the function behaves differently than expected due to previously cached values.

# Advanced tip:
# - To clear the cache programmatically, use the fibonacci_cached.cache_clear() method. This can be useful during testing 
#   or when you want to ensure that the function re-evaluates its results after changes to underlying data or logic.

#=================================================================================
# 8. Itertools Module
#=================================================================================

# The itertools module in Python provides a suite of fast, memory-efficient tools
# for working with iterators. It allows for the creation of iterators for efficient looping.
# Here, we will explore different types of iterators provided by this module.

import itertools  # Import the itertools module for advanced iterator functionality

# Infinite iterators
# The itertools.count function creates an infinite iterator that generates numbers
# starting from a specified value (in this case, 10) and increases by 1 each time.
for i in itertools.count(10):  # Starts counting from 10
    if i > 15:  # A condition to stop the loop when the value exceeds 15
        break  # Exits the loop when i exceeds 15 to prevent an infinite loop
    print(i, end=" ")  # Prints each value of i followed by a space, instead of a newline
# Output: 10 11 12 13 14 15
print()  # Prints a newline for clean output separation after the loop

# Use case:
# Infinite iterators can be useful in scenarios where you need to generate a series
# of values until a certain condition is met, like monitoring system metrics.

# Finite iterators
# The itertools.compress function filters elements from one iterable (first argument)
# using a selector iterable (second argument). It yields elements from the first iterable
# only when the corresponding element in the selector is true (non-zero).
print(list(itertools.compress(['A', 'B', 'C', 'D'], [1, 0, 1, 0])))  
# Output: ['A', 'C']
# In this case, 'A' and 'C' are included because their corresponding selector values are 1.

# Use case:
# This function is particularly useful for filtering data based on specific criteria,
# such as extracting relevant features from datasets.

# Combinatoric iterators
# The itertools.combinations function returns all possible combinations of a specified
# length (in this case, 2) from the input iterable (here, the string 'ABC').
print(list(itertools.combinations('ABC', 2)))  
# Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
# Combinations are generated without replacement and the order of elements does not matter.

# Use case:
# Combinatorics is often used in probability calculations, selecting subsets of data,
# or generating test cases where different combinations of inputs are needed.

# Tip: Itertools provides memory-efficient iterators for various operations
# This means that instead of creating large lists that consume memory, itertools generates
# items on-the-fly. This is particularly beneficial when dealing with large datasets or streams,
# as it allows for better performance and lower memory usage.

# Advanced insight:
# Understanding when to use itertools can help optimize code efficiency. For example,
# using `itertools.chain` can help flatten nested lists without creating additional copies,
# leading to significant performance improvements in memory-intensive applications.

# Example of using itertools.chain
print(list(itertools.chain(['A', 'B'], ['C', 'D'])))  # Output: ['A', 'B', 'C', 'D']

# Pitfalls to watch for:
# When using infinite iterators, always ensure there is a condition to break the loop,
# as failing to do so will lead to infinite loops, causing your program to hang.
# Additionally, ensure that your selector iterable in functions like compress
# is the same length as the input iterable to avoid unexpected behavior.

#=================================================================================
# 9. Functools Module
#=================================================================================

# The functools module in Python provides higher-order functions and operations on callable objects.
# This module is essential for functional programming paradigms in Python.
# Below, we explore key features like partial functions and reducing functions.

import functools  # Importing functools to use its features

# Example 1: Partial functions
# Partial functions allow you to fix a certain number of arguments of a function and generate a new function.
# This is particularly useful for creating specialized functions from more general ones.
base_2 = functools.partial(int, base=2)  # Create a partial function for base 2 conversion
# Here, we fix the 'base' argument of the int() function to 2, allowing us to convert binary strings directly to integers.
print(base_2('1010'))  # Converts binary '1010' to decimal
# Output: 10
# This outputs 10 because '1010' in binary equals 10 in decimal.

# Use case:
# Partial functions are useful in scenarios where you repeatedly call a function with certain fixed arguments,
# such as when interacting with APIs or handling specific data formats.

# Example 2: Reducing functions
# The functools.reduce() function applies a rolling computation to sequential pairs of values in an iterable.
# It takes a function and an iterable and applies the function cumulatively to the items of the iterable.
# The first argument is the function, and the second is the iterable.
print(functools.reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))  
# This calculates the product of all numbers in the list [1, 2, 3, 4, 5].
# Output: 120
# Explanation: It computes (((1 * 2) * 3) * 4) * 5 = 120.

# Use case:
# Reducing functions are particularly useful for aggregating data, such as computing sums, products,
# or other cumulative operations over collections.

# Tip: Use functools for higher-order functions and operations on callable objects.
# This module enhances code modularity and clarity, particularly in functional programming contexts.
# Advanced tip: Be mindful of using lambda functions with functools.reduce as they can sometimes lead to less readable code.
# Named functions or partial functions can improve clarity in more complex reductions.

# Potential pitfalls:
# Overusing partial functions may lead to less readable code if used excessively, especially when the partial functions are deeply nested.
# Always aim for code that balances clarity and efficiency.

#=================================================================================
# 10. Type Hinting and Generics
#=================================================================================

# Type hinting in Python enhances code readability and maintainability by explicitly indicating the expected types of variables, 
# function parameters, and return values. It is particularly useful for static type checkers and IDEs that provide type checking 
# and autocompletion features.

from typing import TypeVar, Generic, List  # Importing necessary components for type hinting and generics

# TypeVar allows you to create a generic type that can be used for type hints.
# T can be any type, allowing the Stack class to be flexible for different data types.
T = TypeVar('T')

# Definition of a generic Stack class using Generic[T]
class Stack(Generic[T]):
    def __init__(self) -> None:
        # Initializing the stack with an empty list to hold items of type T.
        self.items: List[T] = []  # Using List from typing for better type hints

    def push(self, item: T) -> None:
        # Method to add an item of type T to the stack.
        # Type hinting indicates that 'item' must match the type specified for the stack.
        self.items.append(item)  # Adding the item to the end of the list, representing the top of the stack

    def pop(self) -> T:
        # Method to remove and return the last item added to the stack (LIFO order).
        # Type hinting specifies that this method returns an item of type T.
        return self.items.pop()  # Removes the last item from the list and returns it

# Usage Example
# Creating an instance of Stack that can hold integers
stack = Stack[int]()  # The stack is defined to hold integers
stack.push(1)  # Pushing the integer 1 onto the stack
stack.push(2)  # Pushing the integer 2 onto the stack
print(stack.pop())  # Output: 2 - Pops the last item added (2) from the stack

# Advanced tip:
# Generics are extremely powerful for building reusable and type-safe data structures.
# They ensure that the data types are consistent across operations, preventing type-related errors at runtime.
# Using generic classes can significantly enhance the flexibility and reusability of your code.

# Potential pitfalls:
# While type hints improve code clarity, they are optional and do not enforce type checks at runtime.
# Developers should still validate types where necessary, especially when dealing with dynamic data sources.
# Furthermore, overusing complex generics can lead to code that is difficult to read and maintain; 
# it's crucial to strike a balance between flexibility and simplicity.

# Use case:
# Generics are particularly useful in data structures and algorithms where you want to handle different types of data 
# without duplicating code. For example, a generic Stack can be used for integers, strings, or any custom objects.
# By specifying the type when creating the stack, you ensure that only items of that type can be pushed onto it.

#=================================================================================
# 11. Advanced Comprehensions
#=================================================================================

# In this section, we explore advanced comprehensions in Python,
# which provide a concise way to create lists, dictionaries, and sets.
# Comprehensions can improve readability and performance but should be used judiciously.

# Example 1: Nested list comprehension
# A nested list comprehension allows for flattening a 2D list (matrix) into a 1D list.
# Here, we have a matrix represented as a list of lists.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# The comprehension iterates through each row in the matrix,
# and then through each number in the row to create a single flat list.
flattened = [num for row in matrix for num in row]  
print("Flattened matrix:", flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use case:
# Flattening nested structures is common in data manipulation tasks, especially in data science.
# For instance, converting a matrix of pixel values into a single list for image processing.

# Example 2: Dictionary comprehension with conditions
# Dictionary comprehensions allow for creating dictionaries in a more concise way.
# Here, we create a dictionary that maps even numbers from 0 to 9 to their squares.
squares = {x: x**2 for x in range(10) if x % 2 == 0}
# The comprehension iterates through numbers in the specified range,
# applying a condition to include only even numbers in the resulting dictionary.
print("Squares of even numbers:", squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Use case:
# This pattern is useful in scenarios where you need to create mappings based on specific criteria,
# such as generating lookup tables or aggregating data.

# Advanced tips:
# 1. Readability vs. Conciseness: While comprehensions can make your code shorter,
#    prioritize readability, especially for complex expressions. Overly nested comprehensions
#    can make the code difficult to understand at a glance.
# 2. Performance: Comprehensions are often faster than using traditional loops,
#    but for very large datasets, consider using generator expressions (using parentheses) 
#    to save memory when only iterating through values.

# Potential pitfalls:
# 1. Debugging: If a comprehension becomes too complex, consider refactoring it into a standard loop
#    for easier debugging and understanding.
# 2. Excessive nesting: Avoid deeply nested comprehensions; they can lead to confusion.
#    If you find yourself nesting comprehensions beyond two levels, it's usually a sign to rethink
#    your approach or break the logic into separate steps.

#=================================================================================
# 12. Context Variables (Python 3.7+)
#=================================================================================

# Context variables are a powerful feature introduced in Python 3.7,
# providing a way to manage state in a thread-safe manner, particularly useful in asynchronous programming.

import contextvars  # Import the contextvars module for managing context variables

# Creating a ContextVar instance for storing a request ID.
# This variable can hold state specific to a context, such as a request or a user session.
request_id = contextvars.ContextVar('request_id', default=None)

# Example function to process a request identified by a unique ID.
def process_request(id: str) -> None:
    # The set method assigns a new value to the context variable and returns a token.
    # This token can be used to reset the variable to its previous state.
    token = request_id.set(id)
    # Print the current request ID from the context variable.
    # Using request_id.get() retrieves the value associated with the current context.
    print(f"Processing request {request_id.get()}")
    # Reset the context variable to its previous state using the token.
    request_id.reset(token)

# Calling the function with a sample request ID.
process_request('12345')
# After processing, print the value of the context variable.
# Since we reset the variable, it will return to its default state (None).
print(f"After processing: {request_id.get()}")  # Output: After processing: None

# Tip: Use context variables for managing state in asynchronous code.
# In async applications, context variables allow you to maintain request-specific data
# across asynchronous calls without interference from other requests.
# Unlike thread-local storage, context variables ensure that the state remains consistent
# across async tasks, which is crucial in frameworks like asyncio or FastAPI.

# Use cases:
# 1. Logging: Attach a unique request ID to log entries to trace execution across different parts of an application.
# 2. User sessions: Store user-specific data that should persist across multiple async operations.
# 3. Middleware: Manage state information in web applications where multiple layers might access the same request context.

# Advanced tips:
# - Context variables provide a clean way to avoid global state issues in async environments,
#   reducing the complexity and potential bugs associated with traditional state management.
# - Be cautious about using context variables extensively; while they help maintain state,
#   over-reliance can lead to confusion if many variables are used. It's essential to document their usage clearly.
# - When using context variables in a multi-threaded environment, remember that each thread has its context,
#   which can lead to unexpected behaviors if context is not managed properly.

# Potential pitfalls:
# - Forgetting to reset a context variable can lead to state leaks, where old values persist beyond their intended scope.
# - Context variables are not meant for sharing data across different threads. For inter-thread communication,
#   consider using thread-local storage or other synchronization mechanisms.

# In summary, context variables are a powerful tool for managing state in Python applications, especially in async contexts.
# Proper use can lead to cleaner, more maintainable code that handles state effectively without side effects.

#=================================================================================
# 13. Structural Pattern Matching (Python 3.10+)
#=================================================================================

# Structural pattern matching, introduced in Python 3.10, allows for more expressive and readable 
# conditional branching based on the structure of data, particularly useful for handling complex conditions.
# The 'match' statement provides a way to compare a variable against a series of patterns.

# Example: Function to parse commands
# The function 'parse_command' processes a command string and responds based on its contents.
# It demonstrates the use of pattern matching to simplify branching logic.

def parse_command(command: str) -> str:
    # The command is split into parts for analysis; splitting a string creates a list of words.
    match command.split():
        # Case 1: Matches exactly one element in the list, "quit".
        case ["quit"]:  # If the command is 'quit', exit the application.
            return "Exiting"  # Provides clear feedback for user action.
        
        # Case 2: Matches a command "hello" followed by a name.
        case ["hello", name]:  # If the command is 'hello' followed by a name, extract the name.
            return f"Hello, {name}!"  # Returns a personalized greeting.
        
        # Case 3: Matches an "add" command followed by two numbers.
        case ["add", x, y]:  # If the command is 'add', extract the two numbers.
            # Converts strings x and y to floats for addition and returns the result.
            return f"Result: {float(x) + float(y)}"  # Performs addition and formats the output.
        
        # Default case: Catches all other patterns not previously matched.
        case _:  # The underscore (_) acts as a wildcard, matching any other case.
            return "Invalid command"  # Returns an error message for unrecognized commands.

# Testing the parse_command function with different inputs
print(parse_command("hello Alice"))  # Output: Hello, Alice!
# This output confirms that the function correctly recognizes and processes a greeting command.

print(parse_command("add 5 3"))      # Output: Result: 8.0
# This output demonstrates that the function can perform arithmetic operations based on user commands.

# Tip: Use structural pattern matching for complex branching logic based on data structures.
# It enhances code readability and maintainability, especially when dealing with nested data or complex conditions.
# Patterns can also be extended to match tuples, lists, dictionaries, and more, providing a powerful tool for 
# handling varied data structures in a clean, concise manner.

# Advanced insight:
# Pattern matching allows for deconstructing data structures directly in the match cases, 
# which can lead to cleaner code by avoiding multiple lines for checking conditions.
# For example, matching on dictionaries can be done as follows:
data = {"action": "add", "values": [5, 3]}
match data:
    case {"action": "add", "values": [x, y]}:
        print(f"Result: {x + y}")
    case _:
        print("Invalid data structure")

# Potential pitfalls:
# While powerful, pattern matching can lead to complex logic that may be difficult to debug if overused.
# It is important to balance readability with the complexity of patterns; avoid nesting too many patterns deep, 
# which can obscure the code's intention. Aim for clarity in both your matching patterns and overall structure.

#=================================================================================
# 14. Advanced Sorting
#=================================================================================

# In this section, we explore advanced sorting techniques in Python.
# Sorting is a fundamental operation that can be customized using key functions and multiple criteria.

# Example 1: Sorting with key function
# The 'sorted()' function returns a new sorted list from the elements of any iterable.
# By default, it sorts elements based on their natural order.
# However, we can customize the sorting behavior using the 'key' parameter.
words = ['banana', 'apple', 'cherry', 'date']
# Here, we sort 'words' based on their length using the 'len' function as the key.
# The key function takes each element as input and returns a value that is used for sorting.
sorted_words = sorted(words, key=len)
# This results in words being ordered by their length, shortest to longest.
print("Words sorted by length:", sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

# Use case:
# Sorting by length is useful in scenarios like arranging filenames, 
# prioritizing short messages, or organizing data entries by their size.

# Example 2: Sorting with multiple criteria
# Python's sorting functions can handle complex sorting logic using tuples in the key.
# Here, we sort a list of tuples based on multiple criteria.
data = [('Alice', 25), ('Bob', 30), ('Charlie', 25)]
# We use a lambda function that returns a tuple (age, name) for each element.
# This allows us to first sort by age (the second element of the tuple),
# and if ages are the same, sort by name (the first element) in alphabetical order.
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
# This results in tuples being ordered by age first, then by name.
print("Data sorted by age then name:", sorted_data) 
# Output: [('Alice', 25), ('Charlie', 25), ('Bob', 30)]

# Tip:
# When using the key parameter, consider that the function you provide should be efficient,
# especially when sorting large datasets, as it is called for every item in the iterable.
# Additionally, using a tuple for the key allows for chaining multiple sorting criteria 
# seamlessly, which enhances code readability and maintainability.

# Advanced tip:
# The 'key' parameter can accept any callable, including built-in functions, custom functions,
# or lambda functions, which offers flexibility in defining sorting logic. 
# For example, you can use a custom function to sort by a more complex rule, such as 
# sorting by the last character of a string or by a calculated score based on multiple fields.

# Potential pitfalls:
# Be aware of the performance implications of sorting. The time complexity of the sort operation 
# is O(n log n). If you frequently sort large datasets, consider the data structure used (like 
# using a balanced tree or a heap) to optimize access and sorting operations.
# Also, ensure the key function returns consistent types; mixed types can lead to unexpected results 
# or errors during sorting.

#=================================================================================
# 15. Advanced Unpacking
#=================================================================================

# In Python, advanced unpacking provides powerful ways to assign values from iterables
# to multiple variables, enhancing code clarity and flexibility.

# Example 1: Extended iterable unpacking
# Extended unpacking allows for capturing multiple items from an iterable in one step.
# Here, we unpack a range of numbers into three variables: 'first', 'middle', and 'last'.
first, *middle, last = range(10)  # range(10) generates numbers 0 through 9
print(f"First: {first}, Middle: {middle}, Last: {last}")
# Output: First: 0, Middle: [1, 2, 3, 4, 5, 6, 7, 8], Last: 9
# 'first' captures the first element (0), 'last' captures the last element (9),
# and 'middle' captures all elements in between, stored as a list.

# Use case:
# This feature is particularly useful when the structure of the data is known but varies in size,
# such as when processing lines of text or entries from a database.

# Example 2: Unpacking in function calls
# Unpacking can also simplify function calls by passing lists or tuples as arguments.
def power(base, exponent):
    return base ** exponent  # Computes base raised to the power of exponent

powers = [2, 3]  # A list containing base and exponent values
result = power(*powers)  # Unpacking the list 'powers' into the function arguments
print(f"2^3 = {result}")  # Output: 2^3 = 8
# Here, the elements of 'powers' are unpacked so that 'base' receives 2 and 'exponent' receives 3.

# Advanced tip:
# When using unpacking in function calls, ensure the number of elements matches the function's parameters
# to avoid runtime errors. You can also use **kwargs for keyword arguments to further enhance flexibility.

# Best Practices and Tips:

# 1. Use generators for memory-efficient iteration over large sequences.
# Generators yield items one at a time, saving memory compared to lists that load all items at once.

# 2. Leverage decorators for adding functionality to functions and classes without modifying their code.
# Decorators provide a clean way to extend behavior, such as logging or access control.

# 3. Utilize context managers for proper resource management and cleanup.
# Context managers automatically handle resource allocation and deallocation, reducing the risk of leaks.

# 4. Employ asyncio for I/O-bound concurrent programming.
# Asyncio allows for non-blocking operations, which is ideal for tasks like web scraping or handling multiple requests.

# 5. Use metaclasses judiciously, as they can add significant complexity.
# While powerful, metaclasses can make code harder to understand. Use them when necessary for custom class behavior.

# 6. Implement descriptors for reusable attribute management across classes.
# Descriptors define how attributes are accessed and modified, promoting reusable logic.

# 7. Apply function caching (memoization) for expensive computations.
# Memoization stores results of expensive function calls, improving performance on repeated calls.

# 8. Utilize the itertools and functools modules for efficient operations on iterables and functions.
# These modules provide a wealth of tools for common tasks, enhancing code efficiency and readability.

# 9. Use type hinting and generics for better code documentation and IDE support.
# Type hints improve code clarity and help catch errors early by specifying expected types.

# 10. Employ advanced comprehensions for concise and readable code, but prioritize clarity.
# List comprehensions and generator expressions can simplify code, but complex comprehensions may reduce readability.

# 11. Use context variables for managing state in asynchronous code.
# Context variables allow for thread-local storage, which is crucial in asynchronous programming.

# 12. Leverage structural pattern matching for complex branching logic (Python 3.10+).
# Pattern matching simplifies the handling of complex conditions, improving code clarity.

# 13. Utilize advanced sorting techniques with key functions for complex sorting logic.
# Custom sorting can be achieved using the key parameter in sorting functions, allowing for greater flexibility.

# 14. Apply advanced unpacking for more flexible assignment and function calls.
# Advanced unpacking helps to streamline the assignment of multiple variables from complex data structures.

# 15. Always consider the readability and maintainability of your code when using advanced features.
# While advanced techniques can enhance functionality, code should remain clear and easy to maintain.

# This concludes the enhanced detailed Python Cheat Sheet for Advanced Features