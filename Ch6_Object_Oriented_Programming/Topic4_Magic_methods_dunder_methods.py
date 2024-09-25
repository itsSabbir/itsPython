"""
Object-Oriented Programming - Magic Methods (Dunder Methods) - in the Python Programming Language
=================================================================================================

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
Magic methods, also known as dunder (double underscore) methods, are special methods in Python that have double underscores before and after their names. They allow classes to emulate the behavior of built-in types or implement operator overloading, among other things.

Historical context:
- Introduced in early versions of Python to provide a consistent interface for object-oriented programming.
- Evolved over time to include more methods and functionality.
- Inspired by similar concepts in other languages like C++'s operator overloading.

Significance:
- Enable customization of object behavior in response to built-in operations.
- Provide a way to make user-defined classes behave like built-in types.
- Allow for cleaner, more intuitive code by overloading operators.

Common use cases:
- Customizing object creation and initialization
- Implementing container-like behavior
- Operator overloading
- Object representation and formatting
- Context management

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import math
from datetime import datetime
from typing import Any, List, Dict

class ExampleClass:
    """
    This class demonstrates various magic methods in Python.
    """
    
    def __init__(self, value: Any):
        """
        Initialize the ExampleClass instance.
        
        Args:
            value (Any): The initial value for the instance.
        """
        self.value = value
    
    def __str__(self) -> str:
        """
        Return a string representation of the instance.
        
        Returns:
            str: A string representation of the instance.
        """
        return f"ExampleClass(value={self.value})"
    
    def __repr__(self) -> str:
        """
        Return a detailed string representation of the instance.
        
        Returns:
            str: A detailed string representation of the instance.
        """
        return f"<ExampleClass object at {hex(id(self))} with value={self.value}>"
    
    def __len__(self) -> int:
        """
        Return the length of the value if it's a sequence, otherwise return 1.
        
        Returns:
            int: The length of the value or 1.
        """
        return len(self.value) if hasattr(self.value, '__len__') else 1
    
    def __getitem__(self, key):
        """
        Allow indexing or key-based access to the value.
        
        Args:
            key: The index or key to access.
        
        Returns:
            The item at the specified index or key.
        
        Raises:
            TypeError: If the value doesn't support indexing or key-based access.
        """
        if isinstance(self.value, (list, dict, str)):
            return self.value[key]
        raise TypeError(f"'{type(self.value).__name__}' object is not subscriptable")
    
    def __call__(self, *args, **kwargs):
        """
        Make the instance callable.
        
        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        
        Returns:
            str: A string representation of the called instance with arguments.
        """
        return f"Called with args: {args}, kwargs: {kwargs}"
    
    def __eq__(self, other) -> bool:
        """
        Check if this instance is equal to another object.
        
        Args:
            other: The object to compare with.
        
        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, ExampleClass):
            return self.value == other.value
        return False
    
    def __lt__(self, other) -> bool:
        """
        Check if this instance is less than another object.
        
        Args:
            other: The object to compare with.
        
        Returns:
            bool: True if this instance is less than the other object, False otherwise.
        
        Raises:
            TypeError: If the objects can't be compared.
        """
        if isinstance(other, ExampleClass):
            if isinstance(self.value, type(other.value)):
                return self.value < other.value
        raise TypeError(f"'<' not supported between instances of '{type(self).__name__}' and '{type(other).__name__}'")
    
    def __add__(self, other):
        """
        Add this instance to another object.
        
        Args:
            other: The object to add.
        
        Returns:
            ExampleClass: A new instance with the sum of the values.
        
        Raises:
            TypeError: If the objects can't be added.
        """
        if isinstance(other, ExampleClass):
            if isinstance(self.value, (int, float)) and isinstance(other.value, (int, float)):
                return ExampleClass(self.value + other.value)
        raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(other).__name__}'")
    
    def __enter__(self):
        """
        Enter the runtime context for this instance.
        
        Returns:
            ExampleClass: This instance.
        """
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context for this instance.
        
        Args:
            exc_type: The exception type, if an exception occurred.
            exc_value: The exception value, if an exception occurred.
            traceback: The traceback, if an exception occurred.
        
        Returns:
            bool: True if an exception was handled, False otherwise.
        """
        print("Exiting context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_type.__name__}: {exc_value}")
            return True  # Exception handled
        return False

def demonstrate_magic_methods():
    """
    Demonstrate the usage of magic methods in the ExampleClass.
    """
    # Basic usage
    obj = ExampleClass(42)
    print(f"String representation: {obj}")
    print(f"Detailed representation: {repr(obj)}")
    print(f"Length: {len(obj)}")
    
    # Indexing
    list_obj = ExampleClass([1, 2, 3, 4, 5])
    print(f"Third element: {list_obj[2]}")
    
    # Calling the instance
    print(obj(1, 2, 3, keyword="value"))
    
    # Comparison
    obj1 = ExampleClass(10)
    obj2 = ExampleClass(20)
    print(f"obj1 == obj2: {obj1 == obj2}")
    print(f"obj1 < obj2: {obj1 < obj2}")
    
    # Addition
    result = obj1 + obj2
    print(f"obj1 + obj2: {result}")
    
    # Context management
    with ExampleClass("context") as ctx:
        print(f"Inside context: {ctx}")
        # Uncomment the next line to see exception handling
        # raise ValueError("Test exception")

def advanced_magic_methods():
    """
    Demonstrate more advanced uses of magic methods.
    """
    class AdvancedExample:
        def __init__(self, data: Dict[str, Any]):
            self._data = data
        
        def __getattr__(self, name: str) -> Any:
            """
            Dynamically access attributes that don't exist.
            
            Args:
                name (str): The name of the attribute.
            
            Returns:
                Any: The value of the attribute.
            
            Raises:
                AttributeError: If the attribute doesn't exist in the data.
            """
            if name in self._data:
                return self._data[name]
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        
        def __setattr__(self, name: str, value: Any):
            """
            Set attributes dynamically.
            
            Args:
                name (str): The name of the attribute.
                value (Any): The value to set.
            """
            if name == '_data':
                super().__setattr__(name, value)
            else:
                self._data[name] = value
        
        def __iter__(self):
            """
            Make the object iterable.
            
            Yields:
                Tuple[str, Any]: Key-value pairs from the data.
            """
            return iter(self._data.items())
        
        def __reversed__(self):
            """
            Implement reversed iteration.
            
            Yields:
                Tuple[str, Any]: Key-value pairs from the data in reverse order.
            """
            return reversed(list(self._data.items()))
        
        def __contains__(self, item: str) -> bool:
            """
            Check if an item is in the data.
            
            Args:
                item (str): The item to check for.
            
            Returns:
                bool: True if the item is in the data, False otherwise.
            """
            return item in self._data
        
        def __round__(self, n: int = 0):
            """
            Round numeric values in the data.
            
            Args:
                n (int): The number of decimal places to round to.
            
            Returns:
                AdvancedExample: A new instance with rounded values.
            """
            rounded_data = {k: round(v, n) if isinstance(v, (int, float)) else v for k, v in self._data.items()}
            return AdvancedExample(rounded_data)
    
    # Demonstrate advanced magic methods
    adv_obj = AdvancedExample({'a': 1, 'b': 2.5, 'c': 'text'})
    print(f"Accessing dynamic attribute: {adv_obj.a}")
    adv_obj.d = 3.14159
    print(f"Setting dynamic attribute: {adv_obj.d}")
    print("Iterating over object:")
    for key, value in adv_obj:
        print(f"  {key}: {value}")
    print("Reverse iterating over object:")
    for key, value in reversed(adv_obj):
        print(f"  {key}: {value}")
    print(f"Contains 'b': {'b' in adv_obj}")
    rounded_obj = round(adv_obj, 1)
    print(f"Rounded object: {dict(rounded_obj)}")

def main():
    """
    Main function to demonstrate the usage of magic methods.
    """
    print("Demonstrating basic magic methods:")
    demonstrate_magic_methods()
    
    print("\nDemonstrating advanced magic methods:")
    advanced_magic_methods()

if __name__ == "__main__":
    main()

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use magic methods to make your classes behave like built-in types when appropriate.
2. Implement `__repr__` for all classes to aid in debugging.
3. Make sure `__eq__` and `__hash__` are consistent if you implement both.
4. Use `__slots__` for memory optimization when appropriate.
5. Implement comparison methods (`__lt__`, `__gt__`, etc.) consistently.

Common Pitfalls:
1. Forgetting to return a value from methods like `__str__` or `__repr__`.
2. Implementing `__len__` but returning a non-integer value.
3. Not handling type checking in comparison methods, leading to unexpected behavior.
4. Modifying `self` in `__hash__`, which should return a constant value for immutable objects.

Advanced Tips:
1. Use `__slots__` to reduce memory usage for classes with a fixed set of attributes.
2. Implement `__new__` for more control over object creation, especially for singletons or cached instances.
3. Use `__prepare__` in metaclasses to customize class creation.
4. Implement `__missing__` in dict subclasses to handle missing keys.

4. Integration and Real-World Applications
------------------------------------------
- In web frameworks like Django or Flask, magic methods are used to define model fields and customize ORM behavior.
- In scientific computing libraries like NumPy, magic methods enable array operations and broadcasting.
- Game development frameworks use magic methods for sprite collision detection and event handling.
- In testing frameworks, magic methods are used to create mock objects and control attribute access.

Example from a real-world project (simplified version of SQLAlchemy's declarative base):

```python
class Model:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self):
        attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

class User(Model):
    def __init__(self, id, name, email):
        super().__init__(id=id, name=name, email=email)

user = User(1, "John Doe", "john@example.com")
print(user)  # Output: User(id=1, name='John Doe', email='john@example.com')
```

5. Advanced Concepts and Emerging Trends
----------------------------------------
- Asynchronous magic methods (e.g., `__aiter__`, `__anext__`) for use with `async` and `await`.
- Type hinting and magic methods: Using `typing` module to provide better type information.
- Dataclasses in Python 3.7+ use magic methods under the hood to generate boilerplate code.
- The `__post_init__` method in dataclasses for custom initialization logic.

Future developments:
- Proposals for new magic methods to handle more specific use cases.
- Improved performance for frequently used magic methods in the Python interpreter.

6. FAQs and Troubleshooting
---------------------------
Q: Why is my `__eq__` method not being called when I use `==`?
A: Ensure you're not comparing with `None` or a different type. Python short-circuits these comparisons.

Q: How can I make my object behave like a number?
A: Implement numeric magic methods like `__add__`, `__sub__`, `__mul__`, etc.

Q: Why is `len(my_object)` raising a TypeError?
A: Make sure your `__len__` method returns an integer.

Troubleshooting:
1. Use `dir(obj)` to check which magic methods are implemented.
2. Use the `inspect` module to examine method signatures and docstrings.
3. Implement `__getattribute__` carefully to avoid infinite recursion.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- `dataclasses`: Provides a decorator and functions for automatically adding generated special methods to classes.
- `abc` module: For defining abstract base classes with abstract magic methods.
- `functools.total_ordering`: Generates comparison magic methods from a minimal set.

Resources:
- "Python in a Nutshell" by Alex Martelli, Anna Ravenscroft, and Steve Holden
- "Fluent Python" by Luciano Ramalho
- Python Data Model documentation: https://docs.python.org/3/reference/datamodel.html
- Real Python's guide on magic methods: https://realpython.com/python-magic-methods/
- PEP 3119 - Introducing Abstract Base Classes: https://www.python.org/dev/peps/pep-3119/

8. Performance Analysis and Optimization
----------------------------------------
When working with magic methods, it's crucial to consider their performance implications, especially in performance-critical applications. Here are some key points to consider:

1. Profiling Magic Methods:
   Use the `cProfile` module to profile your code and identify which magic methods are called frequently and how much time they consume.

Example of profiling:
"""

import cProfile
import pstats

def profile_magic_methods():
    def test_function():
        class TestClass:
            def __init__(self, value):
                self.value = value
            
            def __str__(self):
                return str(self.value)
            
            def __add__(self, other):
                return TestClass(self.value + other.value)
        
        # Create and use objects
        obj1 = TestClass(5)
        obj2 = TestClass(10)
        for _ in range(10000):
            result = obj1 + obj2
            str(result)
    
    cProfile.runctx('test_function()', globals(), locals(), 'magic_methods_stats')
    
    # Print the stats
    stats = pstats.Stats('magic_methods_stats')
    stats.strip_dirs().sort_stats('cumulative').print_stats(10)

# Uncomment the next line to run the profiling
# profile_magic_methods()

"""
2. Optimizing Frequently Used Magic Methods:
   - For methods like `__str__` and `__repr__`, consider caching the result if the object is immutable.
   - For `__eq__` and `__hash__`, ensure they are implemented efficiently, especially for large collections.

3. Using `__slots__`:
   For classes with a fixed set of attributes, using `__slots__` can significantly reduce memory usage and slightly improve attribute access speed.

Example of using `__slots__`:
"""

class OptimizedClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# This class will use less memory than a regular class with the same attributes

"""
4. Lazy Evaluation:
   Use magic methods like `__getattr__` for lazy attribute computation, especially for expensive operations.

Example of lazy evaluation:
"""

class LazyAttributes:
    def __init__(self):
        self._expensive_attr = None
    
    def __getattr__(self, name):
        if name == 'expensive_attr':
            if self._expensive_attr is None:
                print("Computing expensive attribute...")
                self._expensive_attr = sum(range(1000000))  # Expensive computation
            return self._expensive_attr
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

# Usage
lazy_obj = LazyAttributes()
print(lazy_obj.expensive_attr)  # Computes and returns the value
print(lazy_obj.expensive_attr)  # Returns the cached value without recomputation

"""
5. Avoiding Unnecessary Magic Method Calls:
   Be cautious when implementing magic methods that are called implicitly and frequently, such as `__getattribute__`. Overusing these can lead to performance issues.

6. Benchmarking Different Implementations:
   Use the `timeit` module to compare the performance of different implementations of magic methods.

Example of benchmarking:
"""

import timeit

def benchmark_magic_methods():
    class RegularClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class SlottedClass:
        __slots__ = ['x', 'y']
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    def create_regular():
        return RegularClass(1, 2)
    
    def create_slotted():
        return SlottedClass(1, 2)
    
    regular_time = timeit.timeit(create_regular, number=1000000)
    slotted_time = timeit.timeit(create_slotted, number=1000000)
    
    print(f"Regular class creation time: {regular_time:.6f} seconds")
    print(f"Slotted class creation time: {slotted_time:.6f} seconds")

# Uncomment the next line to run the benchmark
# benchmark_magic_methods()

"""
7. Memory Usage Optimization:
   Use the `sys.getsizeof()` function to compare memory usage of objects with different implementations of magic methods.

Example of comparing memory usage:
"""

import sys

def compare_memory_usage():
    class RegularClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class SlottedClass:
        __slots__ = ['x', 'y']
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    regular_obj = RegularClass(1, 2)
    slotted_obj = SlottedClass(1, 2)
    
    print(f"Memory usage of RegularClass: {sys.getsizeof(regular_obj)} bytes")
    print(f"Memory usage of SlottedClass: {sys.getsizeof(slotted_obj)} bytes")

# Uncomment the next line to compare memory usage
# compare_memory_usage()

"""
These optimization techniques can significantly improve the performance of your Python code, especially when dealing with large numbers of objects or in performance-critical applications.

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
- Relevance to the main topic of magic methods in Python OOP.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate the usage of magic methods and performance considerations.
    """
    print("Demonstrating magic methods and performance considerations:")
    
    # Uncomment the following lines to run the demonstrations
    # profile_magic_methods()
    # benchmark_magic_methods()
    # compare_memory_usage()
    
    print("For detailed output, uncomment the function calls in the main() function.")

if __name__ == "__main__":
    main()