# Python Cheat Sheet: Advanced Features (Enhanced Detailed Version)

import itertools
import functools
import time
import asyncio
from typing import List, Dict, Callable, Any, Generator

# 1. Iterators and Generators

# Iterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Using the iterator
print("Countdown:")
for num in CountDown(5):
    print(num, end=" ")  # Output: 5 4 3 2 1
print()

# Generator
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
print("Fibonacci sequence:")
for num in fibonacci(10):
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
print()

# Tip: Use generators for memory-efficient iteration over large sequences

# Generator expression
squares = (x**2 for x in range(10))
print("Squares:", list(squares))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Tip: Generator expressions are more memory-efficient than list comprehensions for large datasets

# 2. Decorators

# Function decorator
def uppercase_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet() -> str:
    return "hello, world!"

print(greet())  # Output: HELLO, WORLD!

# Class decorator
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected"

# Tip: Use functools.wraps to preserve metadata of the original function/class

# Decorator with arguments
def repeat(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name: str) -> None:
    print(f"Hello, {name}!")

say_hello("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# Tip: Use decorator factories (decorators with arguments) for more flexible decorators

# 3. Context Managers

class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Using the context manager
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')

# Context manager using contextlib
from contextlib import contextmanager

@contextmanager
def temp_file(filename: str):
    try:
        f = open(filename, 'w')
        yield f
    finally:
        f.close()

# Using the contextlib-based context manager
with temp_file('temp.txt') as f:
    f.write('Temporary content')

# Tip: Use context managers for resource management and cleanup

# 4. Coroutines and Asyncio

async def fetch_data(url: str) -> str:
    print(f"Start fetching {url}")
    await asyncio.sleep(2)  # Simulating I/O operation
    print(f"Finished fetching {url}")
    return f"Data from {url}"

async def main():
    urls = ['http://example.com', 'http://example.org', 'http://example.net']
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Run the event loop
asyncio.run(main())

# Tip: Use asyncio for I/O-bound concurrent programming

# 5. Metaclasses

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

# Tip: Use metaclasses to customize class creation behavior

# 6. Descriptor Protocol

class Validator:
    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{self.name} must be between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value

class Person:
    age = Validator(0, 150)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
print(person.age)  # Output: 30
# person.age = 200  # This would raise a ValueError

# Tip: Use descriptors for reusable attribute management across multiple classes

# 7. Function Caching

@functools.lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Measure execution time
start = time.time()
print(fibonacci_cached(100))
end = time.time()
print(f"Time taken: {end - start} seconds")

# Tip: Use lru_cache for memoization of expensive function calls

# 8. Itertools Module

# Infinite iterators
for i in itertools.count(10):
    if i > 15:
        break
    print(i, end=" ")  # Output: 10 11 12 13 14 15
print()

# Finite iterators
print(list(itertools.compress(['A', 'B', 'C', 'D'], [1, 0, 1, 0])))  # Output: ['A', 'C']

# Combinatoric iterators
print(list(itertools.combinations('ABC', 2)))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Tip: Itertools provides memory-efficient iterators for various operations

# 9. Functools Module

# Partial functions
base_2 = functools.partial(int, base=2)
print(base_2('1010'))  # Output: 10

# Reducing functions
print(functools.reduce(lambda x, y: x*y, [1, 2, 3, 4, 5]))  # Output: 120

# Tip: Use functools for higher-order functions and operations on callable objects

# 10. Type Hinting and Generics

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Usage
stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

# Tip: Use type hinting and generics for better code documentation and IDE support

# 11. Advanced Comprehensions

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension with conditions
squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Squares of even numbers:", squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Tip: Use comprehensions for concise and readable code, but don't sacrifice clarity for brevity

# 12. Context Variables (Python 3.7+)

import contextvars

request_id = contextvars.ContextVar('request_id', default=None)

def process_request(id: str) -> None:
    token = request_id.set(id)
    print(f"Processing request {request_id.get()}")
    request_id.reset(token)

process_request('12345')
print(f"After processing: {request_id.get()}")  # Output: After processing: None

# Tip: Use context variables for managing state in asynchronous code

# 13. Structural Pattern Matching (Python 3.10+)

def parse_command(command: str) -> str:
    match command.split():
        case ["quit"]:
            return "Exiting"
        case ["hello", name]:
            return f"Hello, {name}!"
        case ["add", x, y]:
            return f"Result: {float(x) + float(y)}"
        case _:
            return "Invalid command"

print(parse_command("hello Alice"))  # Output: Hello, Alice!
print(parse_command("add 5 3"))      # Output: Result: 8.0

# Tip: Use structural pattern matching for complex branching logic based on data structures

# 14. Advanced Sorting

# Sorting with key function
words = ['banana', 'apple', 'cherry', 'date']
sorted_words = sorted(words, key=len)
print("Words sorted by length:", sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

# Sorting with multiple criteria
data = [('Alice', 25), ('Bob', 30), ('Charlie', 25)]
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
print("Data sorted by age then name:", sorted_data)
# Output: [('Alice', 25), ('Charlie', 25), ('Bob', 30)]

# Tip: Use the key parameter in sorting functions for complex sorting logic

# 15. Advanced Unpacking

# Extended iterable unpacking
first, *middle, last = range(10)
print(f"First: {first}, Middle: {middle}, Last: {last}")
# Output: First: 0, Middle: [1, 2, 3, 4, 5, 6, 7, 8], Last: 9

# Unpacking in function calls
def power(base, exponent):
    return base ** exponent

powers = [2, 3]
result = power(*powers)
print(f"2^3 = {result}")  # Output: 2^3 = 8

# Tip: Use extended unpacking for more flexible assignment and function calls

# Best Practices and Tips:

# 1. Use generators for memory-efficient iteration over large sequences.
# 2. Leverage decorators for adding functionality to functions and classes without modifying their code.
# 3. Utilize context managers for proper resource management and cleanup.
# 4. Employ asyncio for I/O-bound concurrent programming.
# 5. Use metaclasses judiciously, as they can add significant complexity.
# 6. Implement descriptors for reusable attribute management across classes.
# 7. Apply function caching (memoization) for expensive computations.
# 8. Utilize the itertools and functools modules for efficient operations on iterables and functions.
# 9. Use type hinting and generics for better code documentation and IDE support.
# 10. Employ advanced comprehensions for concise and readable code, but prioritize clarity.
# 11. Use context variables for managing state in asynchronous code.
# 12. Leverage structural pattern matching for complex branching logic (Python 3.10+).
# 13. Utilize advanced sorting techniques with key functions for complex sorting logic.
# 14. Apply advanced unpacking for more flexible assignment and function calls.
# 15. Always consider the readability and maintainability of your code when using advanced features.

# This concludes the enhanced detailed Python Cheat Sheet for Advanced Features