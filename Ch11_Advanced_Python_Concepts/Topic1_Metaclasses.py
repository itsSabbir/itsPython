"""
Advanced Python Concepts - Metaclasses - in the Python Programming Language
===========================================================================

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
Metaclasses are a powerful and advanced feature in Python that allow for the customization of class creation. They are often described as "the class of a class," providing a way to modify class behavior at definition time.

Historical context:
- The concept of metaclasses has its roots in Smalltalk, one of the earliest object-oriented programming languages.
- Python introduced metaclasses in version 2.2 (2001) as part of the unification of types and classes.
- The syntax and capabilities of metaclasses were significantly enhanced in Python 3.

Significance:
- Metaclasses provide a way to automatically alter classes at creation time, enabling powerful abstractions and code generation.
- They allow for the implementation of various design patterns and architectural styles in a clean and maintainable way.
- Metaclasses are a key component in many advanced Python libraries and frameworks, particularly those dealing with ORMs, serialization, and API generation.

Common use cases:
- Automatic registration of classes (e.g., for plugins or serialization systems)
- Modifying class attributes or methods at creation time
- Implementing singleton patterns or abstract base classes
- Creating domain-specific languages (DSLs) within Python

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from typing import Dict, Any, Type, TypeVar

T = TypeVar('T')

class Meta(type):
    def __new__(cls, name: str, bases: tuple, attrs: Dict[str, Any]) -> Type[T]:
        """
        Metaclass __new__ method, called when a class using this metaclass is created.

        Args:
        cls: The metaclass itself
        name: Name of the class being created
        bases: Tuple of base classes
        attrs: Dictionary of class attributes

        Returns:
        Type[T]: The created class
        """
        # Example: Add a new method to the class
        attrs['added_method'] = lambda self: print(f"This method was added to {name}")
        
        # Example: Modify existing attributes
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                attrs[attr_name] = cls.log_calls(attr_value)
        
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def log_calls(func):
        """Decorator to log method calls."""
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

class MyClass(metaclass=Meta):
    def original_method(self):
        print("This is an original method")

def demonstrate_basic_metaclass():
    """Demonstrate basic usage of metaclasses."""
    obj = MyClass()
    obj.original_method()  # This will be logged
    obj.added_method()     # This method was added by the metaclass

class SingletonMeta(type):
    _instances: Dict[Type[T], T] = {}
    
    def __call__(cls, *args, **kwargs):
        """
        This method is called when creating an instance of a class with this metaclass.
        It ensures only one instance of the class is created.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

def demonstrate_singleton_metaclass():
    """Demonstrate the use of metaclasses to implement a singleton pattern."""
    s1 = Singleton()
    s2 = Singleton()
    print(f"Are s1 and s2 the same object? {s1 is s2}")

class ValidationMeta(type):
    def __new__(cls, name, bases, attrs):
        # Add validation to all setter methods
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, property) and attr_value.fset is not None:
                attrs[attr_name] = property(
                    attr_value.fget,
                    cls.validate(attr_value.fset),
                    attr_value.fdel,
                    attr_value.__doc__
                )
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def validate(func):
        def wrapper(self, value):
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError("Value must be a non-negative number")
            return func(self, value)
        return wrapper

class Product(metaclass=ValidationMeta):
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

def demonstrate_validation_metaclass():
    """Demonstrate using metaclasses for automatic attribute validation."""
    product = Product(10)
    print(f"Initial price: {product.price}")
    
    try:
        product.price = 20
        print(f"Updated price: {product.price}")
        
        product.price = -5  # This should raise a ValueError
    except ValueError as e:
        print(f"Validation error: {e}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use metaclasses sparingly and only when simpler solutions (like decorators or base classes) are insufficient.
2. Document the behavior of metaclasses thoroughly, as they can make code harder to understand.
3. Follow the principle of least astonishment: metaclasses should modify classes in predictable ways.
4. Use metaclasses to enforce coding standards or patterns across multiple classes.

Common Pitfalls:
1. Overusing metaclasses, leading to unnecessarily complex and hard-to-maintain code.
2. Metaclass conflicts when using multiple inheritance with classes that have different metaclasses.
3. Performance overhead for class creation, especially for frequently instantiated classes.
4. Difficulty in debugging issues related to metaclass behavior.

Advanced Tips:
1. Use `__init_subclass__` for simpler class customization when full metaclass power is not needed.
2. Combine metaclasses with abstract base classes for powerful interface enforcement.
3. Utilize metaclasses for aspect-oriented programming in Python.
4. Leverage metaclasses for creating domain-specific languages (DSLs) within Python.
"""

from abc import ABCMeta, abstractmethod

class InterfaceMeta(ABCMeta):
    def __new__(cls, name, bases, attrs):
        # Ensure all abstract methods are implemented
        for base in bases:
            if isinstance(base, ABCMeta):
                for attr_name in base.__abstractmethods__:
                    if attr_name not in attrs:
                        raise TypeError(f"Can't create abstract class {name}! "
                                        f"{attr_name} must be implemented.")
        return super().__new__(cls, name, bases, attrs)

class MyInterface(metaclass=InterfaceMeta):
    @abstractmethod
    def my_method(self):
        pass

class MyImplementation(MyInterface):
    def my_method(self):
        print("Method implemented")

def demonstrate_interface_metaclass():
    """Demonstrate using metaclasses with abstract base classes for interface enforcement."""
    try:
        class IncompleteImplementation(MyInterface):
            pass
    except TypeError as e:
        print(f"Error creating incomplete class: {e}")
    
    obj = MyImplementation()
    obj.my_method()

"""
4. Integration and Real-World Applications
------------------------------------------
Metaclasses are used in various Python libraries and frameworks:

1. Django ORM: Uses metaclasses for model definition and validation.
2. SQLAlchemy: Employs metaclasses for declarative ORM functionality.
3. Python-Telegram-Bot: Uses metaclasses for command handling.

Real-world example: Automatic API Endpoint Registration
"""

class APIEndpointMeta(type):
    endpoints = {}
    
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if name != 'APIEndpoint':
            path = attrs.get('path', f"/{name.lower()}")
            cls.endpoints[path] = new_cls
        return new_cls

class APIEndpoint(metaclass=APIEndpointMeta):
    def handle_request(self):
        raise NotImplementedError

class UserEndpoint(APIEndpoint):
    path = "/users"
    
    def handle_request(self):
        return "Handling user request"

class ProductEndpoint(APIEndpoint):
    def handle_request(self):
        return "Handling product request"

def simulate_api_request(path):
    """Simulate an API request to demonstrate automatic endpoint registration."""
    endpoint_cls = APIEndpointMeta.endpoints.get(path)
    if endpoint_cls:
        endpoint = endpoint_cls()
        return endpoint.handle_request()
    else:
        return "404 Not Found"

def demonstrate_api_metaclass():
    """Demonstrate a real-world application of metaclasses in API endpoint registration."""
    print("Registered endpoints:", list(APIEndpointMeta.endpoints.keys()))
    print("User request:", simulate_api_request("/users"))
    print("Product request:", simulate_api_request("/product"))
    print("Invalid request:", simulate_api_request("/invalid"))

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Metaclasses in type annotations: PEP 484 introduced support for metaclasses in type hints.
2. Runtime class creation: Using `type()` for dynamic class creation based on runtime conditions.
3. Metaclasses in asynchronous programming: Customizing class creation for coroutines and async generators.
4. Metaclasses in static analysis tools: Enhancing type checking and code analysis capabilities.
"""

import asyncio

class AsyncMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                attrs[attr_name] = asyncio.coroutine(attr_value)
        return super().__new__(cls, name, bases, attrs)

class AsyncClass(metaclass=AsyncMeta):
    def method(self):
        return "This method is now a coroutine"

async def demonstrate_async_metaclass():
    """Demonstrate advanced usage of metaclasses with asynchronous programming."""
    obj = AsyncClass()
    result = await obj.method()
    print(f"Async method result: {result}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use metaclasses instead of class decorators?
A: Use metaclasses when you need to modify the class creation process itself, rather than just modifying the created class. Metaclasses are more powerful but also more complex.

Q: How do I resolve metaclass conflicts in multiple inheritance?
A: Use a common base metaclass that combines the functionality of conflicting metaclasses, or consider redesigning your class hierarchy to avoid the conflict.

Q: Can metaclasses affect class instantiation performance?
A: Yes, especially if the metaclass performs complex operations. Profile your code and consider caching or lazy evaluation techniques if performance is a concern.

Troubleshooting:
1. Use the `__prepare__` method in metaclasses to control the creation of the class namespace.
2. For debugging, implement `__repr__` in your metaclass to provide informative output.
3. Use the `inspect` module to introspect classes and metaclasses during development and debugging.
"""

import inspect

def troubleshooting_examples():
    """Demonstrate troubleshooting techniques for metaclasses."""
    
    class DebugMeta(type):
        @classmethod
        def __prepare__(mcs, name, bases):
            print(f"Preparing namespace for {name}")
            return {}
        
        def __new__(cls, name, bases, attrs):
            print(f"Creating class {name}")
            return super().__new__(cls, name, bases, attrs)
        
        def __init__(cls, name, bases, attrs):
            print(f"Initializing class {name}")
            super().__init__(name, bases, attrs)
        
        def __repr__(cls):
            return f"<{cls.__name__} metaclass for {cls.__name__}>"
    
    class DebuggedClass(metaclass=DebugMeta):
        def method(self):
            pass
    
    print("Metaclass:", DebuggedClass.__class__)
    print("Class attributes:", inspect.getmembers(DebuggedClass))

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. attrs: Provides class creation utilities that can be combined with metaclasses.
2. typing: For type hinting support with metaclasses.
3. abc: The Abstract Base Classes module, often used in conjunction with metaclasses.
4. wrapt: A powerful decorating library that can be used with metaclasses.

Resources:
- "Python in a Nutshell" by Alex Martelli, Anna Ravenscroft, and Steve Holden (Chapter on Metaclasses)
- "Expert Python Programming" by Michal Jaworski and Tarek Ziade (Advanced sections on metaclasses)
- Python's official documentation on metaclasses: https://docs.python.org/3/reference/datamodel.html#metaclasses
- Real Python's guide on metaclasses: https://realpython.com/python-metaclasses/
- PEP 3115 - Metaclasses in Python 3: https://www.python.org/dev/peps/pep-3115/

8. Performance Analysis and Optimization
----------------------------------------
When working with metaclasses, it's crucial to understand their performance implications, especially in large-scale applications or frequently instantiated classes.
"""

import timeit

def performance_comparison():
    """Compare performance of class creation and instantiation with and without metaclasses."""
    
    # Standard class definition
    standard_class_def = """
class StandardClass:
    def method(self):
        pass
    """
    
    # Class with a simple metaclass
    metaclass_def = """
class SimpleMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['added_attr'] = 42
        return super().__new__(cls, name, bases, attrs)

class MetaClass(metaclass=SimpleMeta):
    def method(self):
        pass
    """
    
    # Measure class creation time
    standard_creation_time = timeit.timeit(stmt=standard_class_def, number=10000)
    meta_creation_time = timeit.timeit(stmt=metaclass_def, number=10000)
    
    print(f"Standard class creation time: {standard_creation_time:.6f} seconds")
    print(f"Metaclass creation time: {meta_creation_time:.6f} seconds")
    print(f"Overhead: {(meta_creation_time - standard_creation_time) / standard_creation_time:.2%}")
    
    # Measure instantiation time
    standard_instantiation_time = timeit.timeit(stmt="StandardClass()", setup=standard_class_def, number=100000)
    meta_instantiation_time = timeit.timeit(stmt="MetaClass()", setup=metaclass_def, number=100000)
    
    print(f"\nStandard class instantiation time: {standard_instantiation_time:.6f} seconds")
    print(f"Metaclass instantiation time: {meta_instantiation_time:.6f} seconds")
    print(f"Overhead: {(meta_instantiation_time - standard_instantiation_time) / standard_instantiation_time:.2%}")

"""
Performance Considerations:
1. Metaclasses add overhead to class creation, which can be significant if many classes are defined dynamically.
2. The impact on instantiation time is usually minimal unless the metaclass performs complex operations in __call__.
3. Metaclasses that modify many attributes or methods can increase memory usage.

Optimization Strategies:
1. Cache results of expensive computations in the metaclass.
2. Use __slots__ in classes created by metaclasses to reduce memory footprint.
3. Minimize the use of __new__ in metaclasses, preferring __init__ when possible.
4. Profile your code to identify bottlenecks and optimize only where necessary.
"""

def optimize_metaclass_usage():
    """Demonstrate optimization techniques for metaclasses."""
    
    class OptimizedMeta(type):
        _cache = {}
        
        def __new__(cls, name, bases, attrs):
            # Cache expensive computations
            if name not in cls._cache:
                cls._cache[name] = compute_expensive_attribute()
            attrs['expensive_attr'] = cls._cache[name]
            
            # Use __slots__ to reduce memory usage
            attrs['__slots__'] = tuple(attrs.get('__slots__', ())) + ('optimized_attr',)
            
            return super().__new__(cls, name, bases, attrs)
    
    def compute_expensive_attribute():
        """Simulate an expensive computation."""
        return sum(range(1000000))
    
    class OptimizedClass(metaclass=OptimizedMeta):
        pass
    
    # Measure instantiation time of optimized class
    optimized_time = timeit.timeit(stmt="OptimizedClass()", setup="from __main__ import OptimizedClass", number=100000)
    print(f"Optimized metaclass instantiation time: {optimized_time:.6f} seconds")

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
- Relevance to the main topic of metaclasses in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to metaclasses in Python.
    """
    print("Basic Metaclass Usage:")
    demonstrate_basic_metaclass()
    
    print("\nSingleton Metaclass:")
    demonstrate_singleton_metaclass()
    
    print("\nValidation Metaclass:")
    demonstrate_validation_metaclass()
    
    print("\nInterface Metaclass:")
    demonstrate_interface_metaclass()
    
    print("\nAPI Endpoint Metaclass:")
    demonstrate_api_metaclass()
    
    print("\nAsync Metaclass:")
    asyncio.run(demonstrate_async_metaclass())
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Comparison:")
    performance_comparison()
    
    print("\nOptimizing Metaclass Usage:")
    optimize_metaclass_usage()

if __name__ == "__main__":
    main()