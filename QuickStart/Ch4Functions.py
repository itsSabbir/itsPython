#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Functions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#===============================================================================
# 1. Defining and Calling Functions
#===============================================================================

# In Python, functions are defined using the 'def' keyword.
# Functions are reusable blocks of code that perform a specific task.
# They can accept input parameters, and optionally return a value after execution.
# Below are examples showcasing various types of function definitions and their use cases.

# Example 1: Basic function definition and calling the function
# This function 'greet' takes one parameter, 'name', and returns a greeting message.
# The triple quotes (""" """) just after the function definition form a docstring,
# which provides a description of what the function does. This is optional, but good practice,
# especially for complex functions or when working in teams.
def greet(name):
    """This function returns a greeting message for the provided name."""
    return f"Hello, {name}!"  # Using an f-string to embed the variable 'name' directly into the return string

# Calling the function 'greet' with the argument "Sabbir"
# Functions can be called by their name followed by parentheses enclosing any arguments.
# In this case, the function is called and immediately prints the result.
print(greet("Sabbir"))  # Output: Hello, Sabbir!

# Best practice:
# Always include a docstring for functions that explains their purpose,
# especially when the function's logic becomes complex.
# Keeping function names concise and descriptive improves readability.

# Tip:
# Functions should ideally perform a single, well-defined task.
# Avoid creating functions that do too many things (this aligns with the Single Responsibility Principle in software design).

# Example 2: Function with multiple parameters and a return value
# This 'add' function takes two parameters (a and b) and returns their sum.
def add(a, b):
    return a + b  # Simple addition of the two arguments, 'a' and 'b'

# Calling the function 'add' with the arguments 3 and 5, storing the result in 'result'
result = add(3, 5)  # 'result' now holds the value returned by the function, which is 8
print(f"3 + 5 = {result}")  # Output: 3 + 5 = 8

# Advanced insight:
# Functions in Python can take any number of parameters.
# Python also supports default parameter values, allowing the function to be called without providing every argument.
# Example: def add(a, b=0) could be called with just one argument, and 'b' would default to 0.

# Example 3: Function with multiple return values
# This 'min_max' function accepts a list of numbers and returns two values:
# the minimum and maximum values in the list.
def min_max(numbers):
    return min(numbers), max(numbers)  # The 'min' and 'max' functions return the smallest and largest items from the list

# The function returns two values, which are captured by 'minimum' and 'maximum' through tuple unpacking.
minimum, maximum = min_max([1, 5, 2, 8, 3])  # The function is called with a list, and its two return values are unpacked
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 8

# Unpacking:
# Python allows you to return multiple values from a function as a tuple (i.e., a collection of values).
# By unpacking the returned tuple into separate variables (minimum and maximum), each can be used independently.
# If only one variable were used, it would capture the entire tuple, which may not be desired in all cases.

# Tip:
# Returning multiple values is a powerful feature but should be used judiciously.
# If a function returns too many values, it can make the function harder to understand and use.
# Consider returning a dictionary or a custom object for clarity when handling multiple related outputs.

# Use case:
# This approach of returning multiple values can be useful in cases like statistical functions
# where you need to return several key metrics (e.g., mean, median, and mode), or when performing
# calculations that naturally produce two related results (like min/max, start/end, etc.).

# Advanced tip:
# If returning a tuple, consider using namedtuple or dataclass (from Python's standard library)
# for more readable code. This allows accessing returned values by name rather than position, improving clarity.

#===============================================================================
# 2. Arguments and Parameters
#===============================================================================

# In Python, functions can take various types of arguments and parameters to allow for
# flexibility in how they are called. This includes default arguments, keyword arguments,
# and variable-length arguments (both positional and keyword-based). We'll explore each of these concepts
# with examples and discuss best practices and potential pitfalls.

# Example 1: Default Arguments
# A function with a default argument for 'exponent'. If the user doesn't provide a value for 'exponent',
# the default value (2) is used. This is a great way to provide a fallback behavior while still allowing flexibility.
def power(base, exponent=2):
    # The exponent has a default value of 2, so 'power(3)' will compute 3^2 unless
    # another exponent is explicitly provided.
    return base ** exponent  # '**' is the exponentiation operator in Python

print(power(3))     # Output: 9 (3^2, using the default exponent)
print(power(3, 3))  # Output: 27 (3^3, the provided value overrides the default)

# Best practice: Default arguments are best used when you have a common or standard value for a parameter
# that is likely to be used most of the time. In this case, exponent defaults to 2 (which implies squaring).
# Advanced tip: Be cautious when using mutable types (like lists or dictionaries) as default arguments.
# If modified, they retain the changes across function calls, which can lead to unexpected behavior.

# Example 2: Keyword Arguments
# Keyword arguments allow the caller to specify arguments by name, making the code more readable
# and allowing parameters to be passed in any order.
def greet_person(name, greeting="Hello"):
    # The 'greeting' parameter has a default value, allowing it to be optional
    return f"{greeting}, {name}!"  # This constructs the greeting message using f-string formatting

print(greet_person("Bob"))  # Output: Hello, Bob! (uses default greeting)
print(greet_person("Charlie", "Good day"))  # Output: Good day, Charlie! (custom greeting provided)
print(greet_person(greeting="Hi", name="David"))  # Output: Hi, David! (keyword arguments in reverse order)

# Advanced tip: Keyword arguments are useful in functions with many parameters. By providing
# default values and using keyword arguments, the function call becomes self-explanatory, improving readability.

# Pitfall: Avoid using keyword arguments with overlapping names when combining positional and keyword arguments,
# as it can cause conflicts. Example: `greet_person("David", greeting="Hello")` works, but mixing unnamed
# and named arguments inconsistently can lead to confusion.

# Example 3: Variable-length Arguments (*args)
# The *args syntax allows the function to accept an arbitrary number of positional arguments as a tuple.
def sum_all(*args):
    # *args collects all extra positional arguments into a tuple named 'args'
    return sum(args)  # Sums all elements in the tuple

print(sum_all(1, 2, 3))       # Output: 6 (1 + 2 + 3)
print(sum_all(1, 2, 3, 4, 5)) # Output: 15 (1 + 2 + 3 + 4 + 5)

# Best practice: *args is ideal when you don't know beforehand how many arguments will be passed to the function.
# It allows the function to be flexible with the number of inputs. *args is commonly used when writing
# functions like sum, min, max, or similar operations where the number of inputs can vary.

# Advanced tip: When using *args, remember that it collects arguments as a tuple. This means you can
# still use all tuple operations on 'args' (e.g., slicing, indexing). Also, *args must appear after
# regular positional arguments in the function definition.

# Example 4: Variable-length Keyword Arguments (**kwargs)
# The **kwargs syntax allows the function to accept an arbitrary number of keyword arguments as a dictionary.
def print_info(**kwargs):
    # **kwargs collects all extra keyword arguments into a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # Iterates over the dictionary and prints each key-value pair

print_info(name="Sabbir", age=30, city="New York")
# Output:
# name: Sabbir
# age: 30
# city: New York

# Best practice: **kwargs is useful when you want to handle named arguments dynamically or pass a dictionary
# of named parameters to a function. It is especially helpful in frameworks or libraries where
# configuration or options might be passed as named parameters.

# Advanced tip: Combining *args and **kwargs in a function signature allows the function to accept any number
# of positional and keyword arguments, making it extremely flexible. This is commonly seen in decorators or
# API wrappers where argument types and numbers are variable.

# Example 5: Combining *args and **kwargs
# A function that accepts both arbitrary positional and keyword arguments.
def multi_purpose(*args, **kwargs):
    # *args collects all positional arguments, while **kwargs collects all keyword arguments
    print("Args:", args)  # Prints the tuple of positional arguments
    print("Kwargs:", kwargs)  # Prints the dictionary of keyword arguments

multi_purpose(1, 2, 3, name="Sabbir", age=30)
# Output:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Sabbir', 'age': 30}

# Best practice: Use this combination when writing highly flexible functions. This pattern is commonly used
# in scenarios where a function needs to be agnostic to the number and type of arguments it will receive.
# However, make sure to document such functions well to prevent confusion regarding which arguments are expected.

# Advanced insight: When combining *args and **kwargs, the order of the parameters matters:
# regular positional arguments -> *args -> default arguments -> **kwargs. This order ensures that the function can
# first handle fixed inputs, then any arbitrary positional arguments, followed by optional defaults, and finally
# arbitrary keyword arguments.


#===============================================================================
# 3. Lambda Functions
#===============================================================================

# Lambda functions are small, anonymous functions in Python, defined using the 'lambda' keyword.
# These functions are typically used when you need a simple, one-time operation and don't want to define a full function using 'def'.
# Lambda functions are syntactically limited to a single expression but can still perform complex operations with multiple arguments or conditions.

# Example 1: Basic lambda function
# This lambda function takes one argument 'x' and returns 'x' squared (x ** 2).
# It's similar to defining a function like 'def square(x): return x ** 2' but in one line.
square = lambda x: x ** 2  # Function that returns the square of a number
print(square(5))  # Output: 25
# Use case: Great for simple operations, like math expressions, where writing a full function would be overkill.

# Advanced tip: Lambda functions can be useful for quick, temporary operations where creating a named function would reduce readability.
# However, excessive use of lambda functions can make code harder to debug and maintain if overused or for complex logic.

# Example 2: Lambda functions with multiple arguments
# This lambda function takes two arguments, 'x' and 'y', and returns their sum.
# Equivalent to 'def add(x, y): return x + y' but condensed.
add = lambda x, y: x + y  # Function that adds two numbers
print(add(3, 4))  # Output: 7
# Use case: Efficient for inline operations like arithmetic, used in callbacks, or simple computations involving multiple arguments.

# Example 3: Lambda functions with conditional expressions
# This lambda function checks whether a number is even or odd.
# The 'if' statement inside the lambda evaluates the condition and returns "Even" if true, or "Odd" if false.
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"  # Check if a number is even or odd
print(is_even(4))  # Output: Even
print(is_even(5))  # Output: Odd
# Use case: When a quick decision-making function is required, such as labeling data or categorizing inputs.
# Conditional expressions are perfect for one-liners that don't require a full function definition.

# Advanced tip: You can use conditional expressions within lambda functions to handle branching logic.
# However, for complex decision trees or nested conditions, it's better to use a standard function definition for clarity.

# Example 4: Lambda functions with 'map()'
# 'map()' is a built-in Python function that applies a function (in this case, a lambda) to every item in an iterable (like a list).
# Here, the lambda squares each element in the 'numbers' list.
numbers = [1, 2, 3, 4, 5]  # List of numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Squaring each number in the list
print(f"Squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]
# Use case: 'map()' with lambda is often used for transforming data in lists or other iterables efficiently.
# It avoids the need for writing explicit loops and keeps the code concise.

# Advanced tip: When using 'map()' with lambda functions, the result is an iterator in Python 3.
# Wrapping it in 'list()' makes it easier to view the result. However, if working with large datasets, leaving it as an iterator
# and consuming it lazily may be more memory-efficient.

# Example 5: Lambda functions with 'filter()'
# 'filter()' applies a function to an iterable and returns only the items that satisfy the condition (where the lambda returns True).
# In this case, it filters out only the even numbers from the 'numbers' list.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filtering out even numbers from the list
print(f"Even numbers: {even_numbers}")  # Output: [2, 4]
# Use case: Filtering elements from a list based on a condition is a common use case.
# 'filter()' combined with lambda is especially useful for quick operations where you need to extract or exclude data based on simple conditions.

# Advanced tip: Both 'map()' and 'filter()' can often be replaced by list comprehensions, which are generally more Pythonic.
# For example, the above filter could be written as: even_numbers = [x for x in numbers if x % 2 == 0].
# This can make the code more readable, but in some cases, 'map()' and 'filter()' with lambdas may still offer a cleaner approach for specific functional programming tasks.

# Pitfalls to avoid:
# 1. Overusing lambda functions for complex logic—this can make code difficult to understand.
# 2. Using lambda for functions that should be reusable—defining a named function with 'def' is preferable for clarity and reuse.


#===============================================================================
# 4. Function Annotations
#===============================================================================

# Function annotations provide a way to attach metadata to function arguments and return types.
# These annotations are optional and do not affect the function's execution; they are mainly for documentation purposes.
# Python does not enforce type checks based on annotations, but they can be useful for readability, static analysis, and tools like IDEs or type checkers (e.g., mypy).
# Here, we explore basic function annotations and their use with different data types.

# Example 1: Function annotation with a single parameter and return type
def greet_annotated(name: str) -> str:
    # The parameter 'name' is annotated with 'str', indicating the expected type is a string.
    # The '-> str' after the function signature specifies that the function is expected to return a string.
    return f"Hello, {name}!"  # Returning a formatted greeting string

# Calling the annotated function with a valid string argument.
print(greet_annotated("Eve"))  # Output: Hello, Eve!

# Accessing the function's annotations using the special __annotations__ attribute
# This returns a dictionary where keys are parameter names and the 'return' key corresponds to the return type.
print(greet_annotated.__annotations__)  
# Output: {'name': <class 'str'>, 'return': <class 'str'>}
# Here, it shows that the 'name' parameter should be a string and the return type is also a string.

# Advanced tip:
# Function annotations are not strictly enforced at runtime, meaning you can pass incorrect types, 
# and the function will still run. However, this can lead to unexpected behavior if not careful.
# It's recommended to use static type checkers (like mypy) to enforce type safety when using annotations in larger codebases.

# Example 2: Function with multiple annotations
def process_data(x: int, y: float, z: str) -> dict:
    # This function takes three parameters with different types:
    # 'x' is expected to be an integer (int)
    # 'y' is expected to be a floating-point number (float)
    # 'z' is expected to be a string (str)
    # The return type is annotated as a dictionary (dict).
    
    # The function returns a dictionary with the sum of x and y, and the string message 'z'.
    return {"sum": x + y, "message": z}

# Calling the function with the correct types for 'x', 'y', and 'z'.
result = process_data(5, 3.14, "Processing complete")
print(result)  
# Output: {'sum': 8.14, 'message': 'Processing complete'}
# The return value is a dictionary containing the sum of x and y, and the provided message.

# Best practice:
# When working in large teams or projects, using annotations can help improve code readability and self-documenting code. 
# They make it clear what types of arguments a function expects and what it will return, reducing potential confusion.

# Uncommon insight:
# Although function annotations are commonly used for type hints, they can also store arbitrary metadata.
# For instance, you can annotate with more complex objects like lists or even custom classes.
# However, since Python doesn't enforce the types, it's important to combine annotations with proper validation where necessary.

# Example of annotations with more complex data types:
from typing import List, Tuple

def handle_complex_data(data: List[int], details: Tuple[str, bool]) -> None:
    # Here, 'data' is expected to be a list of integers, and 'details' is expected to be a tuple containing a string and a boolean.
    # The return type is 'None', indicating the function returns no value.
    print(f"Data: {data}")
    print(f"Details: {details}")

# Calling the function with the correct types.
handle_complex_data([1, 2, 3], ("Important", True))

# Output:
# Data: [1, 2, 3]
# Details: ('Important', True)

# Potential pitfalls:
# As annotations are not enforced, relying solely on them without actual runtime checks or static analysis tools can lead to incorrect assumptions about the data types.
# For example, you might annotate a parameter as 'int' but pass a string instead, and Python will not raise an error unless validation is done separately.

# Conclusion:
# Function annotations are a valuable tool for writing clear, maintainable, and type-aware code.
# While they don't enforce types at runtime, they are essential for documentation, static analysis, and tooling in modern Python development.

#===============================================================================
# 5. Recursive Functions
#===============================================================================

# Recursive functions are functions that call themselves to solve smaller instances of the same problem.
# They are particularly useful for problems that can be broken down into similar subproblems (e.g., factorial, Fibonacci sequence, tree traversal).
# However, recursive functions must have a well-defined base case to avoid infinite recursion and stack overflow.

# Example 1: Factorial Function
# A classic example of recursion is calculating the factorial of a number.
# The factorial of n (denoted as n!) is the product of all positive integers from 1 to n.
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    # Base case: factorial of 0 or 1 is defined as 1.
    # This prevents the recursion from going infinitely and provides a stopping point.
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: multiply n by the factorial of (n-1).
        # This reduces the problem size step by step until it hits the base case.
        return n * factorial(n - 1)

# Test the factorial function
print(f"Factorial of 5: {factorial(5)}")  # Output: 120
# The recursive breakdown for factorial(5):
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1  (Base case reached)

# Recursive functions like factorial are elegant and easy to understand conceptually,
# but recursion can sometimes lead to performance inefficiencies, especially for deep recursions.

# Advanced Tip: 
# Python’s recursion limit is usually set to 1000 by default, and recursing beyond this limit will raise a RecursionError.
# For deep recursion, consider tail recursion or switching to an iterative solution.
# In this factorial example, tail recursion (where the recursive call is the last operation) isn't applied, 
# but it can be optimized in languages that support tail call optimization (TCO).

# Example 2: Fibonacci Sequence
# Another common example of recursion is calculating Fibonacci numbers.
# The Fibonacci sequence is defined as:
# F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
# The nth Fibonacci number is the sum of the two preceding ones.

def fibonacci(n):
    # Base case: F(0) = 0 and F(1) = 1.
    # These stop the recursion when we reach the smallest Fibonacci numbers.
    if n <= 1:
        return n
    else:
        # Recursive case: Fibonacci of n is the sum of Fibonacci of (n-1) and (n-2).
        return fibonacci(n-1) + fibonacci(n-2)

# Test the fibonacci function
print(f"10th Fibonacci number: {fibonacci(10)}")  # Output: 55
# The recursive breakdown for fibonacci(10):
# fibonacci(10) = fibonacci(9) + fibonacci(8)
# fibonacci(9) = fibonacci(8) + fibonacci(7)
# and so on...

# Potential Pitfall: 
# While recursive Fibonacci code is intuitive, it is highly inefficient due to overlapping subproblems.
# The same values (e.g., fibonacci(8), fibonacci(7)) are recalculated multiple times, leading to an exponential time complexity O(2^n).

# Advanced Tip: 
# To avoid the inefficiency of recalculating the same values, use **memoization** (caching previously computed results).
# Python provides an easy way to memoize using the `functools.lru_cache` decorator.
# Alternatively, you can use a dynamic programming approach to reduce time complexity to O(n).

# Example of memoizing the Fibonacci function to optimize performance:
from functools import lru_cache

@lru_cache(maxsize=None)  # Cache the results of function calls to avoid recalculating the same values
def fibonacci_memoized(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

print(f"10th Fibonacci number with memoization: {fibonacci_memoized(10)}")  # Output: 55
# Now, the Fibonacci function runs in linear time, O(n), as each Fibonacci number is computed only once.

# Use case:
# Recursive Fibonacci is elegant for educational purposes but should be optimized using memoization or iterative approaches in real-world applications 
# to avoid unnecessary recomputation and high time complexity.

#===============================================================================
# 6. Higher-Order Functions
#===============================================================================

# Higher-order functions are functions that take other functions as arguments or return functions as their result.
# These are essential for functional programming patterns and allow for more flexible, reusable code.

# Example 1: apply_operation function demonstrates a higher-order function
# This function accepts two values (x, y) and another function (operation) as arguments.
# It then applies the passed 'operation' function to 'x' and 'y'.
def apply_operation(x, y, operation):
    # The operation function is applied to x and y. The 'operation' here could be any function 
    # that takes two arguments. This allows for dynamic behavior based on what function is passed.
    return operation(x, y)

# Defining two basic functions to use with apply_operation
def add(a, b):
    # Adds two values 'a' and 'b' together
    return a + b

def multiply(a, b):
    # Multiplies two values 'a' and 'b' together
    return a * b

# The higher-order function apply_operation is now called with 'add' and 'multiply'
print(apply_operation(5, 3, add))      # Output: 8
# Here, apply_operation(5, 3, add) calls the 'add' function with arguments 5 and 3, returning 8

print(apply_operation(5, 3, multiply)) # Output: 15
# Similarly, apply_operation(5, 3, multiply) calls the 'multiply' function, returning 15

# Use case:
# Higher-order functions like apply_operation allow us to abstract over actions 
# (in this case, different mathematical operations), making the code more flexible and reusable.

# Example 2: Returning functions - another key capability of higher-order functions.
# In this case, get_operation returns a function based on the input string.
def get_operation(operation_name):
    # This function returns a function based on the operation_name argument
    if operation_name == "add":
        return add  # If the operation name is 'add', return the 'add' function
    elif operation_name == "multiply":
        return multiply  # If the operation name is 'multiply', return the 'multiply' function
    else:
        # For an unknown operation, we return a lambda function that outputs an error message
        return lambda x, y: "Invalid operation"

# Calling get_operation with "add", which returns the 'add' function itself
operation = get_operation("add")
# Now, operation holds the reference to the 'add' function, which can be used like a normal function
print(operation(5, 3))  # Output: 8

# Advanced tip:
# Higher-order functions enable flexible design, especially in scenarios involving event handling, callbacks, 
# or algorithms where the behavior needs to be passed dynamically.
# For example, you could have a higher-order function for logging, error-handling wrappers, or function composition.

# Potential pitfalls:
# One common pitfall is misunderstanding function references vs function calls. When passing a function as 
# an argument (as in apply_operation), it's important to pass the function itself (e.g., add), not its result 
# (e.g., add()) unless explicitly needed. 
# Another caution is the use of anonymous (lambda) functions, which are powerful but can reduce readability if overused.

#===============================================================================
# 7. Closures
#===============================================================================

# Closures in Python are a way of retaining access to variables from the enclosing scope even after 
# the outer function has finished execution. This enables delayed or deferred execution of code with context retained.

# Example: outer_function and inner_function demonstrating a closure
def outer_function(x):
    # The 'x' variable from outer_function is enclosed in the scope of inner_function, creating a closure.
    # This means that even after outer_function finishes, the inner function still has access to 'x'.
    def inner_function(y):
        # The inner function has access to 'x' even though it's defined in the outer scope
        return x + y
    return inner_function  # Returns the inner function, which forms a closure around 'x'

# Creating a closure by calling outer_function(5)
# 'add_5' now holds a reference to the inner_function, with 'x' set to 5 in its closure
add_5 = outer_function(5)

# Now, calling add_5(3) is equivalent to inner_function(3) where 'x' is still 5 from the closure
print(add_5(3))  # Output: 8

# Calling the same closure again with a different argument
print(add_5(7))  # Output: 12
# Each time we call add_5, it remembers that 'x' is 5, making it behave like a function that adds 5 to its argument.

# Advanced tip:
# Closures are especially useful for implementing function factories, decorators, and maintaining state in a clean, 
# functional style. They help keep state encapsulated without the need for objects or classes.
# Be mindful of potential memory leaks in long-running programs if closures retain large objects unnecessarily.

# Uncommon insight:
# Closures combined with mutable data can introduce subtle bugs if not handled carefully. Since closures maintain references, 
# changes in the outer scope’s mutable variables (like lists or dictionaries) can affect the closure's behavior in ways that 
# are hard to track. It's often safer to work with immutable data when designing closures for predictable behavior.


#===============================================================================
# 8. Decorators
#===============================================================================

# Decorators are a powerful tool in Python that allow you to modify or enhance the behavior of functions or methods without altering their code.
# They follow the design principle of "wrapping" a function, adding extra functionality before or after the original function runs.
# Decorators make code more modular, reusable, and easier to maintain, especially when dealing with cross-cutting concerns such as logging, authentication, or timing.

# Example 1: Basic decorator without arguments

# A simple decorator that converts the return value of a function to uppercase
def uppercase_decorator(func):
    # Inner function 'wrapper' will wrap around the original function 'func'
    def wrapper():
        result = func()  # Call the original function
        return result.upper()  # Convert the result to uppercase before returning it
    return wrapper  # Return the wrapper function to replace the original one

# The @ syntax is a shorthand for applying the decorator to a function
# Here, @uppercase_decorator is equivalent to greet = uppercase_decorator(greet)
@uppercase_decorator
def greet():
    return "hello, world!"  # Original function returns a simple greeting

# When greet() is called, the uppercase_decorator is applied,
# so the output will be the uppercase version of the greeting
print(greet())  # Output: HELLO, WORLD!

# Explanation:
# 1. The decorator is applied using @uppercase_decorator before the function definition.
# 2. When greet() is called, it is passed to the decorator, which modifies its behavior to return an uppercase string.
# 3. The 'wrapper' function is executed instead of the original greet function, adding the extra functionality (converting to uppercase).

# Use case:
# This pattern is commonly used in web development frameworks like Flask/Django where decorators handle tasks like routing, 
# authentication, or logging. For example, a decorator could log every call made to an API endpoint.

# Example 2: Decorator with arguments

# A more advanced example where the decorator takes arguments, allowing for more flexible functionality.
def repeat_decorator(times):
    # The outer function receives 'times', which specifies how many times to repeat the wrapped function
    def decorator(func):
        # The 'wrapper' function wraps around the original function 'func'
        def wrapper(*args, **kwargs):
            # The 'for' loop repeats the function call the specified number of times
            for _ in range(times):
                result = func(*args, **kwargs)  # Call the original function with its arguments
            return result  # Return the result of the last execution
        return wrapper  # Return the wrapper to replace the original function
    return decorator  # Return the decorator function

# Applying the decorator with an argument (3 times in this case)
@repeat_decorator(3)
def say_hello(name):
    # The original function that prints a greeting
    print(f"Hello, {name}!")

# When say_hello("Sabbir") is called, the repeat_decorator ensures it runs 3 times
say_hello("Sabbir")
# Output:
# Hello, Sabbir!
# Hello, Sabbir!
# Hello, Sabbir!

# Explanation:
# 1. The repeat_decorator takes an argument 'times', which controls how many times the decorated function should be executed.
# 2. The wrapper function calls the original function 'func' in a loop for 'times' iterations, effectively repeating it.
# 3. In this example, the decorated function say_hello prints the greeting three times.

# Advanced tip:
# The ability to pass arguments to decorators allows for greater flexibility, such as controlling execution flow, retry mechanisms, 
# or dynamically setting behavior based on runtime conditions.
# You can also return values or use decorators to memoize functions (i.e., caching the result to avoid repeated calculations).

# Uncommon insights:
# *args and **kwargs in the 'wrapper' function make the decorator flexible enough to handle functions with varying arguments.
# This allows you to apply the same decorator to functions with different parameter structures.
# A common pitfall is forgetting to use *args and **kwargs in the wrapper, leading to errors when applying the decorator to functions with parameters.
# It’s important to return the result of the wrapped function, especially if the decorator modifies or uses the function’s output.

# Use case:
# Decorators with arguments are often used in scenarios like retry mechanisms, where a function should be executed multiple times 
# (e.g., retrying a failed network request), or for dynamic role-based access control in web applications.



#===============================================================================
# 9. Generators
#===============================================================================

# Generators in Python are a special kind of iterable, like lists or tuples, but they do not store their contents in memory.
# Instead, they generate items on the fly, which makes them more memory-efficient when dealing with large datasets.
# The 'yield' keyword is used to produce a value and pause the function execution, allowing the generator to "remember" its state.
# Generators can be iterated one value at a time, making them excellent for handling sequences without the memory overhead of lists.

# Example 1: Generator function using 'yield'
# This generator function counts from 1 up to the specified number 'n'
# Each time 'yield' is called, it returns the current value of 'i' and pauses the function's execution until the next iteration
def count_up_to(n):
    i = 1  # Initialize the counter at 1
    while i <= n:  # Continue as long as 'i' is less than or equal to 'n'
        yield i  # Yield the current value of 'i' and pause execution of the generator
        i += 1  # Increment 'i' after each yield

# Example usage of the generator function
# Using a for-loop to iterate over the generator produced by count_up_to(5)
# Each time the loop asks for the next item, the generator resumes where it left off
for number in count_up_to(5):  # count_up_to(5) generates values from 1 to 5
    print(number, end=" ")  # Output: 1 2 3 4 5, numbers are printed followed by a space
print()  # A new line after printing all the numbers

# Output:
# 1 2 3 4 5

# Advanced tip:
# Generators are useful when working with large datasets or infinite sequences.
# For example, you can create a generator that generates an infinite sequence of numbers, 
# and you can stop consuming when you no longer need more values.
# Generators provide lazy evaluation—meaning values are only computed when requested, unlike lists where all values are computed at once.

# Use case:
# Imagine you're working with a massive log file. Instead of loading the entire log file into memory,
# you could use a generator to read it line by line and process each line in a memory-efficient way.

# Example 2: Generator expression
# A generator expression is similar to a list comprehension but creates a generator instead of a list.
# It uses parentheses instead of square brackets and evaluates lazily, meaning items are generated on demand.
# In this case, it generates the square of each number in the range from 0 to 4.

# Generator expression to create a generator for squares of numbers
squares = (x**2 for x in range(5))  # Creates a generator object that yields squares of 0 to 4

# We can convert the generator to a list by passing it to 'list()', which forces the generator to yield all values.
# This materializes all the results into memory, similar to a list comprehension.
print(list(squares))  # Output: [0, 1, 4, 9, 16], the squares of 0 through 4 are printed as a list

# Advanced tip:
# If you don't need to store all values in memory at once, using a generator expression is far more efficient than a list comprehension.
# For example, this approach shines when working with large or potentially infinite sequences.
# Be careful when you exhaust a generator; after converting it to a list (or iterating through it), the generator is depleted and cannot be reused.
# To generate values again, you must recreate the generator.

# Potential pitfalls:
# Once a generator is exhausted (i.e., fully iterated), it cannot be reset or reused.
# You would need to recreate it if further iterations are required.
# Another common mistake is treating generators like lists or trying to access them via indexing, which is not possible since generators don't support random access.


#===============================================================================
# 10. Function Attributes
#===============================================================================

# In Python, functions are first-class objects, meaning they can have attributes attached to them
# just like any other object (such as instances of classes). 
# These attributes are mutable and can be used to store additional information about the function.

# Example 1: Basic function with a custom attribute
# A function 'my_function' is defined here. 
# Note that the function includes a docstring, which is a string literal typically used to describe 
# the purpose of the function. It can be accessed via the function's '__doc__' attribute.
def my_function():
    """This is a docstring."""  # This string provides documentation for the function
    pass  # The function body contains 'pass' which is a placeholder statement doing nothing for now

# After defining the function, we can add a custom attribute.
# Since functions are objects, attributes can be dynamically added to them.
# Here, we attach an attribute 'custom_attribute' to 'my_function' with the value "I'm a custom attribute".
my_function.custom_attribute = "I'm a custom attribute"  # Assigning a custom attribute to the function

# Accessing the docstring of the function using the '__doc__' attribute.
# This is an internal attribute that contains the docstring of the function.
print(my_function.__doc__)  # Output: This is a docstring.

# Accessing the custom attribute we added.
# 'custom_attribute' is not a built-in attribute; we added this manually to store extra information.
print(my_function.custom_attribute)  # Output: I'm a custom attribute

# Advanced Tip:
# Function attributes can be used for a variety of purposes such as:
# - Attaching metadata to functions (e.g., setting a version number or description).
# - Storing additional information, such as caching results or setting flags related to function behavior.
# - Useful in decorators, where attributes can help track the decorated function’s state.
# Since functions are mutable, attributes can be modified at runtime, offering flexibility.

# Potential Pitfalls:
# - Using function attributes may introduce complexity if overused or mismanaged. 
#   It’s essential to keep track of attributes, especially if multiple parts of the code rely on them.
# - Since function attributes are dynamic, they are not enforced at compile-time. 
#   If removed or altered inadvertently, errors may arise at runtime, especially in larger codebases.

# Example 2: Attaching multiple custom attributes for more complex usage
# Adding a version number and a description to the function using custom attributes.
my_function.version = "1.0"
my_function.description = "This function does nothing but demonstrates function attributes."

print(f"Version: {my_function.version}")  # Output: Version: 1.0
print(f"Description: {my_function.description}")  # Output: Description: This function does nothing but demonstrates function attributes.

# Use Case:
# A practical use case might involve tracking function metadata. 
# For example, in a large codebase, you could use function attributes to mark deprecated functions or 
# store references to related functions, improving code readability and maintainability.

# Example 3: Using function attributes in a decorator
# Here's a decorator that modifies a function and attaches a custom attribute to it.
def my_decorator(func):
    # This decorator adds an 'executed' attribute to the function and modifies its behavior
    func.executed = False  # Initially set to False; this will change once the function is executed

    def wrapper(*args, **kwargs):
        # When the function is called, we set 'executed' to True
        func.executed = True
        return func(*args, **kwargs)

    return wrapper

@my_decorator
def another_function():
    print("Function is running...")

another_function()
print(another_function.executed)  # Output: True

# In this example, the decorator attaches an attribute 'executed' to 'another_function'.
# This attribute tracks whether the function has been called, demonstrating how function attributes 
# can be effectively used in combination with decorators to monitor or modify behavior.

# Best Practice:
# While function attributes are powerful, it's important to use them sparingly.
# Overusing them can clutter the function’s namespace, and their dynamic nature can make debugging more difficult.
# Limit their use to cases where they genuinely enhance the code, such as in decorators or when attaching metadata.

#===============================================================================
# 11. Partial Functions
#===============================================================================

# In Python, the `functools.partial` function allows you to fix a certain number of arguments of a function and generate a new function.
# This is especially useful for creating more specific functions based on general-purpose ones.
# It can help simplify function calls by pre-setting some of the arguments, making the function easier to reuse in different contexts.
# Below is an example of how to use partial functions.

from functools import partial  # Importing 'partial' from the functools module

# Example function:
# This function takes two arguments, 'base' and 'exponent', and returns 'base' raised to the power of 'exponent'.
def power(base, exponent):
    return base ** exponent  # '**' is the exponentiation operator in Python

# Creating a new function 'square' by partially applying 'power' with the exponent fixed at 2
# The base argument is left open for future calls, allowing us to reuse this as a square function
square = partial(power, exponent=2)

# Similarly, creating a new function 'cube' by fixing the exponent at 3
cube = partial(power, exponent=3)

# Now, 'square' behaves like a specialized function that only requires the base as an argument
print(square(4))  # Output: 16, which is equivalent to 4^2 (4 squared)

# The 'cube' function behaves similarly but with the exponent fixed to 3
print(cube(3))    # Output: 27, which is equivalent to 3^3 (3 cubed)

# Use case:
# Partial functions are useful when you have a general-purpose function but need to create multiple variations
# by fixing certain arguments. This can reduce repetitive code and make your functions more readable.
# For example, instead of repeatedly calling `power(base, 2)` for squaring, you can create a more intuitive 'square' function.

# Advanced insights:
# Partial functions are not limited to positional arguments; they can also handle keyword arguments.
# You can fix both positional and keyword arguments in a function, making partial functions highly flexible.
# Additionally, partial functions can be chained together if necessary, though this might reduce clarity in some cases.

# Example with keyword arguments:
def greet(greeting, name):
    return f"{greeting}, {name}!"

# Creating a partial function that fixes the greeting
say_hello = partial(greet, greeting="Hello")

# Now, 'say_hello' only requires the 'name' argument to function
print(say_hello("Sabbir"))  # Output: Hello, Sabbir!

# Tip: Using partial functions can be a powerful technique when working with higher-order functions 
# (functions that accept other functions as arguments), such as in functional programming, callbacks, 
# or when working with libraries that require callback functions (e.g., event-driven programming).

# Potential pitfalls:
# One common issue with partial functions is that the argument names and defaults can sometimes be unclear, 
# especially in large or complex applications. The function signature can become less intuitive because not all 
# arguments are visible in the partial function.
# As a best practice, avoid overusing partial functions if it reduces code readability. Always strive to balance flexibility with clarity.

# Best practices:
# - Use descriptive names for your partial functions to make it clear what specific case they handle (like 'square' or 'cube').
# - While partial functions are useful for fixing certain arguments, be mindful of readability; too many layers of partial applications can obscure the original function.

#===============================================================================
# 12. Function Caching
#===============================================================================

# Function caching is an optimization technique that stores the results of expensive function calls
# and returns the cached result when the same inputs occur again.
# Python provides a built-in decorator for this purpose in the functools module called 'lru_cache'.
# 'LRU' stands for Least Recently Used, which refers to the cache eviction policy it uses.

# Example: Using lru_cache to optimize the Fibonacci sequence calculation

from functools import lru_cache  # Importing the lru_cache decorator from functools module

# Applying the @lru_cache decorator to the Fibonacci function.
# The 'maxsize=None' parameter means that the cache can grow without bound.
# It stores previously computed results of the Fibonacci function.
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    # Base case: If n is less than 2, return n (Fibonacci(0) = 0 and Fibonacci(1) = 1)
    if n < 2:
        return n
    # Recursive case: Fibonacci(n) is the sum of Fibonacci(n-1) and Fibonacci(n-2)
    # Since this is recursive, the function would normally recompute values many times
    # But lru_cache ensures that repeated calls with the same 'n' are cached.
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# The following call will compute Fibonacci(100) efficiently by caching previous results.
# Without caching, the recursive Fibonacci function would perform a large number of redundant calculations.
print(fibonacci_cached(100))  # Output: 354224848179261915075

# Output Explanation:
# The Fibonacci sequence grows exponentially in terms of the number of recursive calls required.
# Without caching, computing Fibonacci(100) would require hundreds of billions of function calls.
# With caching, each Fibonacci number is calculated only once, drastically reducing the time complexity
# from exponential (O(2^n)) to linear (O(n)).

# Use case:
# Caching is most beneficial in scenarios where:
# 1. A function is called repeatedly with the same inputs.
# 2. The function performs expensive calculations or recursive operations.
# In this example, the Fibonacci sequence is an ideal use case since it has overlapping subproblems that are recomputed many times.

# Advanced tip:
# The 'maxsize' parameter allows you to control the maximum number of results the cache can store.
# Once the cache reaches its limit, it will discard the least recently used (LRU) values.
# Setting maxsize=None means that the cache will not discard any results and can grow indefinitely, 
# which is useful when the number of distinct calls is limited, as in the Fibonacci sequence.
# For use cases where memory constraints are important, setting an appropriate maxsize can help 
# balance between performance and memory usage.

# Example of controlling cache size:
# @lru_cache(maxsize=128)  # This limits the cache to the 128 most recent function results
# def some_function(...):
#     ...

# Potential pitfalls:
# 1. Memory usage: Since lru_cache stores function results in memory, using it with large datasets or many different inputs
# can cause excessive memory consumption if not carefully managed.
# 2. Unintended side effects: Be cautious when using lru_cache with functions that have side effects (e.g., printing, modifying global state),
# as the cache will return stored results without re-executing the function, potentially skipping side effects.
# 3. Mutable arguments: lru_cache only works with functions whose arguments are immutable. This is because it uses the function's arguments 
# as keys in the cache, and mutable types like lists or dictionaries cannot be hashed and thus cannot be cached.

# A simple way to clear the cache if needed:
# fibonacci_cached.cache_clear()  # This method clears the cache, forcing the function to recompute the results on subsequent calls.

# Best practice:
# Use function caching for pure functions (functions that always return the same output for the same inputs and have no side effects)
# where repeated calculations occur. Avoid using it in scenarios where the function's results depend on external states or where side effects are expected.

#===============================================================================
# 13. Asynchronous Functions (Coroutines)
#===============================================================================

# Asynchronous functions (also called coroutines) in Python allow for non-blocking code execution.
# This means the program can perform other tasks while waiting for an I/O-bound or time-consuming operation.
# Coroutines are defined using 'async def' and are executed with 'await', 
# which pauses the coroutine's execution until the awaited operation is complete.

# Example 1: Simple async function with asyncio.sleep

import asyncio  # 'asyncio' is the standard Python library for asynchronous operations

# Defining an asynchronous function using 'async def'
# The function accepts a 'name' argument and simulates a delay using 'await asyncio.sleep()'
async def async_hello(name):
    # 'await' pauses the coroutine and allows other tasks to run concurrently
    # Here, 'asyncio.sleep(1)' simulates an asynchronous delay (non-blocking sleep) for 1 second
    await asyncio.sleep(1)  # This would be replaced by actual I/O operations like fetching data from an API
    return f"Hello, {name}!"  # After the sleep, it returns a formatted string greeting the provided name

# Defining another asynchronous function called 'main' to orchestrate the workflow
# The 'main' function calls 'async_hello' and waits for its result using 'await'
async def main():
    # 'await' suspends 'main' until 'async_hello' completes, allowing other asynchronous tasks to run in parallel
    result = await async_hello("Alice")  # Passing "Alice" as an argument to the 'async_hello' function
    print(result)  # Printing the result after receiving the response from 'async_hello'

# Running the event loop using 'asyncio.run()'
# 'asyncio.run()' runs the main asynchronous function and manages the event loop
asyncio.run(main())  # Output: Hello, Alice!

# Explanation:
# 1. The 'async def' syntax declares a function as a coroutine. Coroutines are special functions that 
#    can be paused and resumed, enabling non-blocking I/O or other asynchronous tasks.
# 2. The 'await' keyword is used inside async functions to pause the function until the awaited task completes.
#    In this case, 'asyncio.sleep(1)' pauses execution for 1 second, simulating an async operation (such as a web request or database query).
# 3. The 'asyncio.run(main())' starts the main asynchronous function and handles the event loop.

# Advanced Tip:
# 'asyncio.sleep' is commonly used to simulate I/O-bound tasks like network requests, file reading, etc.
# Using async functions allows Python to handle multiple I/O-bound tasks concurrently, improving performance in cases like:
# - Web scraping with multiple requests
# - Concurrent file or database access
# - Real-time data processing where latency matters (e.g., chat applications or live updates)

# Common use case:
# Async functions are useful in web frameworks like FastAPI or asynchronous web scraping, 
# where you need to handle multiple requests or operations simultaneously without blocking the main thread.

# Example 2: Running multiple coroutines concurrently

# 'asyncio.gather' is used to run multiple async functions concurrently
# This is particularly useful when you need to launch multiple I/O-bound tasks simultaneously

async def async_task(task_name, delay):
    await asyncio.sleep(delay)  # Each task will wait for the specified 'delay' time before completing
    return f"Task {task_name} completed after {delay} seconds"

async def main_concurrent():
    # Running multiple async tasks concurrently using 'asyncio.gather'
    results = await asyncio.gather(
        async_task("A", 1),  # First task with a 1-second delay
        async_task("B", 2),  # Second task with a 2-second delay
        async_task("C", 3)   # Third task with a 3-second delay
    )
    for result in results:
        print(result)  # Print the results of each task once all are completed

asyncio.run(main_concurrent())  
# Output (order may vary):
# Task A completed after 1 seconds
# Task B completed after 2 seconds
# Task C completed after 3 seconds

# Explanation:
# 1. 'asyncio.gather' is used to run multiple async functions concurrently. Each task runs in parallel
#    and completes after its respective delay.
# 2. This allows you to perform multiple I/O-bound tasks simultaneously, which can significantly improve efficiency 
#    when handling asynchronous operations like HTTP requests, file reading, or querying databases.

# Advanced Tip:
# When running multiple coroutines, care should be taken with resource management (e.g., limiting the number of 
# concurrent connections to a database). Use techniques like semaphore control or connection pooling 
# to avoid overwhelming resources.
# For tasks where order of completion is important, 'asyncio.gather' can be replaced with 'asyncio.as_completed' 
# which yields coroutines as soon as they complete, allowing you to process them in real-time.

# Pitfalls:
# 1. 'asyncio.run()' should only be called once and is not re-entrant, meaning that if you're inside an existing event loop 
#    (e.g., in Jupyter or when using certain libraries), calling 'asyncio.run()' will raise a 'RuntimeError'.
#    In such cases, you should use 'await' or 'loop.run_until_complete()' directly.
# 2. 'asyncio' is designed for I/O-bound and high-level structured network code. For CPU-bound tasks (e.g., heavy computation),
#    Python's async framework is less effective. Instead, consider multithreading or multiprocessing.


#===============================================================================
# 14. Type Hinting for Functions (Python 3.5+)
#===============================================================================

# Type hinting allows us to annotate function arguments and return types with expected data types.
# Introduced in Python 3.5+, type hints do not enforce type checking at runtime but serve as a guide
# for developers and tools (like IDEs or linters) to catch potential type-related issues early.

# The 'typing' module provides a range of useful type hinting constructs such as List, Dict, Tuple, and Optional.
# Below, we'll demonstrate type hinting with a function that processes a list of numbers and accepts options in a dictionary.

from typing import List, Dict, Tuple, Optional  # Importing required types for hinting

# Example function using type hints:
# 'numbers' is expected to be a list of integers (List[int]),
# 'options' is a dictionary with string keys and string values (Dict[str, str]), with a default empty dictionary.
# The function returns a tuple: an integer (the sum of numbers) and an optional string (a message).
def process_data(numbers: List[int], options: Dict[str, str] = {}) -> Tuple[int, Optional[str]]:
    # 'total' is the sum of all integers in the 'numbers' list.
    total = sum(numbers)
    
    # 'message' is fetched from the 'options' dictionary using the 'get' method.
    # If the 'message' key is not found, 'message' will be None (default behavior of 'get').
    message = options.get("message")
    
    # Return a tuple: the total sum of the numbers and the optional message.
    return total, message

# Example of calling the function with type-appropriate arguments
result = process_data([1, 2, 3], {"message": "Processed"})

# Print the result, which is expected to be a tuple containing (6, 'Processed').
print(result)  # Output: (6, 'Processed')

# In-depth explanation:

# The 'List[int]' annotation means that the 'numbers' parameter must be a list where all elements are integers.
# If a list contains other types, it would not adhere to this type hint.
# This helps clarify the intention of the function, making it easier for others to use and for tools to catch potential type errors.

# The 'Dict[str, str]' annotation means that the 'options' parameter must be a dictionary where both the keys
# and the values are strings. This ensures that the function processes the dictionary correctly, avoiding unexpected types.

# The 'Tuple[int, Optional[str]]' annotation specifies that the function will return a tuple.
# The first element of the tuple will be an integer (the total of the numbers list).
# The second element is 'Optional[str]', meaning it can be either a string or None.
# 'Optional' is often used when a value can either be of a certain type or absent (None).

# Advanced tip:
# - While Python is dynamically typed, adding type hints greatly improves code readability, maintainability, 
#   and can also catch bugs early during development with static analysis tools.
# - Type hints are particularly useful in large codebases and collaborative projects where the types expected
#   by functions aren't immediately obvious.
# - Type hinting does not affect the runtime performance of Python programs, but combined with tools like 'mypy', 
#   you can perform type checks statically (before running the code), improving code safety without sacrificing performance.

# Example of misuse:
# result = process_data([1, "two", 3], {"message": "Processed"})  # This would not be flagged at runtime
# However, tools like 'mypy' would catch the error: "List item 1 has incompatible type 'str'; expected 'int'".

# Potential pitfalls:
# - Type hinting doesn't enforce the types at runtime, so you can still pass incorrect types and face issues.
#   Static analysis tools like 'mypy' are essential to truly benefit from type hinting by flagging incorrect types before execution.
# - Default values: In this case, 'options' has a default value of an empty dictionary. However, using mutable default arguments
#   (like lists or dictionaries) can lead to unexpected behavior if the default is modified. The best practice is to use 
#   'None' as the default and then initialize the mutable object inside the function.

# Improved approach for 'options' default value:
# def process_data(numbers: List[int], options: Optional[Dict[str, str]] = None) -> Tuple[int, Optional[str]]:
#     if options is None:
#         options = {}
#     total = sum(numbers)
#     message = options.get("message")
#     return total, message
