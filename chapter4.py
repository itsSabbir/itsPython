# Python Cheat Sheet: Functions

# 1. Defining and Calling Functions

# Basic function definition
def greet(name):
    """This is a docstring. It describes what the function does."""
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!

# Function with multiple parameters and a return value
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")  # Output: 3 + 5 = 8

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 2, 8, 3])
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 8

# 2. Arguments and Parameters

# Default Arguments
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # Output: 9 (uses default exponent 2)
print(power(3, 3))  # Output: 27 (uses provided exponent 3)

# Keyword Arguments
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_person("Bob"))                  # Output: Hello, Bob!
print(greet_person("Charlie", "Good day"))  # Output: Good day, Charlie!
print(greet_person(greeting="Hi", name="David"))  # Output: Hi, David!

# Variable-length Arguments (*args)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(1, 2, 3, 4, 5)) # Output: 15

# Variable-length Keyword Arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# Combining *args and **kwargs
def multi_purpose(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

multi_purpose(1, 2, 3, name="Alice", age=30)
# Output:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}

# 3. Lambda Functions

# Basic lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda functions with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

# Lambda functions with conditional expressions
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))  # Output: Even
print(is_even(5))  # Output: Odd

# Lambda functions with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]

# Lambda functions with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [2, 4]

# 4. Function Annotations

def greet_annotated(name: str) -> str:
    return f"Hello, {name}!"

print(greet_annotated("Eve"))  # Output: Hello, Eve!
print(greet_annotated.__annotations__)  # Output: {'name': <class 'str'>, 'return': <class 'str'>}

# Function with multiple annotations
def process_data(x: int, y: float, z: str) -> dict:
    return {"sum": x + y, "message": z}

result = process_data(5, 3.14, "Processing complete")
print(result)  # Output: {'sum': 8.14, 'message': 'Processing complete'}

# 5. Recursive Functions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")  # Output: 120

# Another example: Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"10th Fibonacci number: {fibonacci(10)}")  # Output: 55

# 6. Higher-Order Functions

def apply_operation(x, y, operation):
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(5, 3, add))      # Output: 8
print(apply_operation(5, 3, multiply)) # Output: 15

# Returning functions
def get_operation(operation_name):
    if operation_name == "add":
        return add
    elif operation_name == "multiply":
        return multiply
    else:
        return lambda x, y: "Invalid operation"

operation = get_operation("add")
print(operation(5, 3))  # Output: 8

# 7. Closures

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_5 = outer_function(5)
print(add_5(3))  # Output: 8
print(add_5(7))  # Output: 12

# 8. Decorators

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

print(greet())  # Output: HELLO, WORLD!

# Decorator with arguments
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_decorator(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# 9. Generators

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up_to(5):
    print(number, end=" ")  # Output: 1 2 3 4 5
print()  # Newline

# Generator expression
squares = (x**2 for x in range(5))
print(list(squares))  # Output: [0, 1, 4, 9, 16]

# 10. Function Attributes

def my_function():
    """This is a docstring."""
    pass

my_function.custom_attribute = "I'm a custom attribute"

print(my_function.__doc__)  # Output: This is a docstring.
print(my_function.custom_attribute)  # Output: I'm a custom attribute

# 11. Partial Functions

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # Output: 16
print(cube(3))    # Output: 27

# 12. Function Caching

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

print(fibonacci_cached(100))  # This will be much faster than the non-cached version

# 13. Asynchronous Functions (Coroutines)

import asyncio

async def async_hello(name):
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    return f"Hello, {name}!"

async def main():
    result = await async_hello("Alice")
    print(result)

asyncio.run(main())  # Output: Hello, Alice!

# 14. Type Hinting for Functions (Python 3.5+)

from typing import List, Dict, Tuple, Optional

def process_data(numbers: List[int], options: Dict[str, str] = {}) -> Tuple[int, Optional[str]]:
    total = sum(numbers)
    message = options.get("message")
    return total, message

result = process_data([1, 2, 3], {"message": "Processed"})
print(result)  # Output: (6, 'Processed')

# This concludes the detailed Python Cheat Sheet for Functions