"""
Object-Oriented Programming - Property Decorators - in the Python Programming Language
======================================================================================

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
Property decorators in Python are a powerful feature that allows developers to define methods that behave like attributes. They provide a clean way to implement getters, setters, and deleters for class attributes, enhancing encapsulation and providing a Pythonic approach to access control.

Historical context:
- Introduced in Python 2.2 (2001) as part of the descriptor protocol.
- Simplified in Python 2.4 (2004) with the introduction of the @property decorator.
- Further enhanced in Python 2.6 (2008) with the ability to use @property as a decorator for the getter method.

Significance:
- Allows for computed attributes without breaking the object's interface.
- Provides a way to add validation or transformation logic when getting or setting attribute values.
- Enables lazy evaluation of expensive computations.

Common use cases:
- Data validation
- Computed attributes
- Encapsulation of private variables
- Backward compatibility when refactoring code

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import time
import functools
from typing import Any, Callable

class PropertyExample:
    def __init__(self, value: int):
        self._value = value
    
    @property
    def value(self) -> int:
        """Getter for the value attribute."""
        return self._value
    
    @value.setter
    def value(self, new_value: int):
        """Setter for the value attribute with validation."""
        if not isinstance(new_value, int):
            raise TypeError("Value must be an integer")
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value
    
    @value.deleter
    def value(self):
        """Deleter for the value attribute."""
        print("Deleting value")
        del self._value

def demonstrate_basic_property():
    """Demonstrate basic usage of property decorators."""
    obj = PropertyExample(42)
    print(f"Initial value: {obj.value}")
    
    obj.value = 100
    print(f"After setting: {obj.value}")
    
    try:
        obj.value = -10
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        obj.value = "not an int"
    except TypeError as e:
        print(f"Error: {e}")
    
    del obj.value
    try:
        print(obj.value)
    except AttributeError as e:
        print(f"Error: {e}")

class LazyProperty:
    """A descriptor class for implementing lazy properties."""
    
    def __init__(self, func: Callable):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj: Any, cls: Any = None) -> Any:
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)
        return value

class ExpensiveComputation:
    @LazyProperty
    def expensive_result(self) -> int:
        """A property that performs an expensive computation only when accessed."""
        print("Performing expensive computation...")
        time.sleep(2)  # Simulate expensive computation
        return 42

def demonstrate_lazy_property():
    """Demonstrate the use of a lazy property."""
    obj = ExpensiveComputation()
    print("Object created. Accessing expensive_result for the first time:")
    print(f"Result: {obj.expensive_result}")
    print("Accessing expensive_result again:")
    print(f"Result: {obj.expensive_result}")

class ValidatedProperty:
    """A descriptor class for implementing validated properties."""
    
    def __init__(self, fget: Callable = None, fset: Callable = None, fdel: Callable = None, doc: str = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
    
    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)
    
    def __set__(self, obj: Any, value: Any):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)
    
    def __delete__(self, obj: Any):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)
    
    def getter(self, fget: Callable) -> 'ValidatedProperty':
        return type(self)(fget, self.fset, self.fdel, self.__doc__)
    
    def setter(self, fset: Callable) -> 'ValidatedProperty':
        return type(self)(self.fget, fset, self.fdel, self.__doc__)
    
    def deleter(self, fdel: Callable) -> 'ValidatedProperty':
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    @ValidatedProperty
    def name(self) -> str:
        """Get the person's name."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Set the person's name with validation."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    @ValidatedProperty
    def age(self) -> int:
        """Get the person's age."""
        return self._age
    
    @age.setter
    def age(self, value: int):
        """Set the person's age with validation."""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

def demonstrate_validated_property():
    """Demonstrate the use of a validated property."""
    person = Person("Alice", 30)
    print(f"Initial name: {person.name}, age: {person.age}")
    
    person.name = "Bob"
    person.age = 35
    print(f"After update: name: {person.name}, age: {person.age}")
    
    try:
        person.name = ""
    except ValueError as e:
        print(f"Error setting name: {e}")
    
    try:
        person.age = 200
    except ValueError as e:
        print(f"Error setting age: {e}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use properties for computed attributes that don't require expensive calculations.
2. Implement proper validation in setters to maintain data integrity.
3. Use properties to maintain backward compatibility when refactoring.
4. Keep property methods simple and focused on a single responsibility.

Common Pitfalls:
1. Overusing properties where simple public attributes would suffice.
2. Implementing expensive computations in property getters without caching.
3. Forgetting to implement all three methods (getter, setter, deleter) when needed.
4. Modifying the object's state in getter methods, which should be side-effect free.

Advanced Tips:
1. Use functools.cached_property for caching expensive computations (Python 3.8+).
2. Implement custom property-like decorators for complex scenarios.
3. Utilize descriptors for reusable property logic across multiple classes.
4. Consider using __slots__ with properties for memory optimization.
"""

class PropertyBestPractices:
    def __init__(self, value: int):
        self._value = value
        self._expensive_result = None
    
    @property
    def value(self) -> int:
        return self._value
    
    @value.setter
    def value(self, new_value: int):
        if not isinstance(new_value, int):
            raise TypeError("Value must be an integer")
        self._value = new_value
        # Invalidate cached result when value changes
        self._expensive_result = None
    
    @functools.cached_property
    def expensive_computation(self) -> int:
        print("Performing expensive computation...")
        time.sleep(2)  # Simulate expensive computation
        return self._value * 1000

def demonstrate_best_practices():
    """Demonstrate best practices and advanced tips for properties."""
    obj = PropertyBestPractices(10)
    print(f"Initial value: {obj.value}")
    print(f"Expensive computation result: {obj.expensive_computation}")
    print("Accessing expensive computation again (should be cached):")
    print(f"Expensive computation result: {obj.expensive_computation}")
    
    obj.value = 20
    print(f"Value after update: {obj.value}")
    print("Expensive computation after value change (should recompute):")
    print(f"Expensive computation result: {obj.expensive_computation}")

"""
4. Integration and Real-World Applications
------------------------------------------
Properties are widely used in various Python libraries and frameworks:

1. Django ORM: Uses properties to define computed fields on model classes.
2. SQLAlchemy: Employs properties for lazy-loading of related objects.
3. Python's built-in libraries: e.g., pathlib uses properties for path manipulation.

Real-world example: A simple caching system using properties
"""

import hashlib
from typing import Dict

class CachingSystem:
    def __init__(self):
        self._cache: Dict[str, Any] = {}
    
    def _get_cache_key(self, func: Callable, *args, **kwargs) -> str:
        """Generate a unique cache key for a function call."""
        key = f"{func.__name__}:{args}:{kwargs}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def cached_property(self, func: Callable) -> property:
        """A property decorator that caches the result of expensive computations."""
        @functools.wraps(func)
        def wrapper(obj):
            cache_key = self._get_cache_key(func, obj)
            if cache_key not in self._cache:
                self._cache[cache_key] = func(obj)
            return self._cache[cache_key]
        return property(wrapper)

class DataAnalyzer:
    def __init__(self, data: list):
        self.data = data
        self.caching_system = CachingSystem()
    
    @CachingSystem.cached_property
    def average(self) -> float:
        """Calculate the average of the data (expensive operation)."""
        print("Calculating average...")
        time.sleep(2)  # Simulate expensive computation
        return sum(self.data) / len(self.data)
    
    @CachingSystem.cached_property
    def standard_deviation(self) -> float:
        """Calculate the standard deviation of the data (expensive operation)."""
        print("Calculating standard deviation...")
        time.sleep(2)  # Simulate expensive computation
        avg = self.average
        return (sum((x - avg) ** 2 for x in self.data) / len(self.data)) ** 0.5

def demonstrate_real_world_application():
    """Demonstrate a real-world application of properties in a caching system."""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    analyzer = DataAnalyzer(data)
    
    print("Calculating average for the first time:")
    print(f"Average: {analyzer.average}")
    
    print("Calculating average again (should be cached):")
    print(f"Average: {analyzer.average}")
    
    print("Calculating standard deviation:")
    print(f"Standard Deviation: {analyzer.standard_deviation}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Asynchronous Properties: With the rise of asynchronous programming in Python, there's a growing need for asynchronous properties.
2. Type Hints for Properties: Improving static type checking for properties.
3. Property Factories: Creating reusable property patterns.
"""

import asyncio

class AsyncProperty:
    """A descriptor class for implementing asynchronous properties."""
    
    def __init__(self, func):
        self.func = func
    
    def __get__(self, obj, cls):
        if obj is None:
            return self
        return asyncio.create_task(self.func(obj))

class AsyncExample:
    def __init__(self, value: int):
        self._value = value
    
    @AsyncProperty
    async def async_value(self) -> int:
        await asyncio.sleep(1)  # Simulate async operation
        return self._value * 2

async def demonstrate_async_property():
    """Demonstrate the use of an asynchronous property."""
    obj = AsyncExample(21)
    result = await obj.async_value
    print(f"Async property result: {result}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use properties instead of simple attributes?
A: Use properties when you need to add logic for getting, setting, or deleting an attribute, or when you want to compute a value on-the-fly.

Q: How can I make a read-only property?
A: Implement only the getter method and omit the setter and deleter.

Q: Can I use properties with inheritance?
A: Yes, properties can be inherited and overridden in subclasses.

Troubleshooting:
1. If a property setter is not being called, ensure you're assigning to the property and not the underlying attribute.
2. For performance issues with properties, consider caching expensive computations or using lazy evaluation.
3. If a property is not showing up in dir(obj), make sure it's defined at the class level, not in __init__.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- attrs: Provides class decorators that auto-generate properties.
- dataclasses: Offers a way to create classes with automatically added properties.
- PyPy: A JIT-compiled implementation of Python that can optimize property access.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones
- "Fluent Python" by Luciano Ramalho
- Python's official documentation on properties: https://docs.python.org/3/library/functions.html#property
- Real Python's guide on Python properties: https://realpython.com/python-property/

8. Performance Analysis and Optimization
----------------------------------------
When working with properties, it's important to consider their performance implications, especially in performance-critical applications.
"""

import timeit

def benchmark_property_vs_attribute():
    """Benchmark the performance difference between properties and simple attributes."""
    class WithAttribute:
        def __init__(self, value):
            self.value = value
    
    class WithProperty:
        def __init__(self, value):
            self._value = value
        
        @property
        def value(self):
            return self._value
        
        @value.setter
        def value(self, new_value):
            self._value = new_value
    
    def attribute_access():
        obj = WithAttribute(42)
        for _ in range(1000):
            obj.value
            obj.value = 43
    
    def property_access():
        obj = WithProperty(42)
        for _ in range(1000):
            obj.value
            obj.value = 43
    
    attribute_time = timeit.timeit(attribute_access, number=1000)
    property_time = timeit.timeit(property_access, number=1000)
    
    print(f"Attribute access time: {attribute_time:.6f} seconds")
    print(f"Property access time: {property_time:.6f} seconds")
    print(f"Property overhead: {property_time / attribute_time:.2f}x")

def optimize_property_access():
    """Demonstrate techniques to optimize property access."""
    class OptimizedProperty:
        def __init__(self, value):
            self._value = value
            self._cached_expensive_result = None
        
        @property
        def value(self):
            return self._value
        
        @value.setter
        def value(self, new_value):
            self._value = new_value
            self._cached_expensive_result = None
        
        @property
        def expensive_result(self):
            if self._cached_expensive_result is None:
                print("Computing expensive result...")
                time.sleep(0.1)  # Simulate expensive computation
                self._cached_expensive_result = self._value * 1000
            return self._cached_expensive_result
    
    obj = OptimizedProperty(42)
    print(f"Initial expensive result: {obj.expensive_result}")
    print(f"Cached expensive result: {obj.expensive_result}")
    
    obj.value = 43
    print(f"Expensive result after value change: {obj.expensive_result}")

"""
Performance Considerations:
1. Simple property access is generally slower than direct attribute access due to the function call overhead.
2. For frequently accessed properties, consider using simple attributes if no additional logic is required.
3. Use caching techniques for expensive computations in property getters.
4. Profile your code to identify performance bottlenecks related to property access.

Optimization Strategies:
1. Lazy Evaluation: Compute and cache values only when needed.
2. Attribute Promotion: Convert properties to attributes after initial setup if they won't change.
3. Use `__slots__` to reduce memory usage and slightly speed up attribute access.
4. Consider using the `@functools.cached_property` decorator for automatic caching (Python 3.8+).

Example of attribute promotion:
"""

class AttributePromotion:
    def __init__(self, value):
        self._value = value
    
    @property
    def promoted_value(self):
        # Compute the value and promote it to an attribute
        result = self._value * 2
        object.__setattr__(self, 'promoted_value', result)
        return result

def demonstrate_attribute_promotion():
    """Demonstrate the attribute promotion technique."""
    obj = AttributePromotion(21)
    print("Accessing promoted_value for the first time (computed):")
    print(obj.promoted_value)
    print("Accessing promoted_value again (now an attribute):")
    print(obj.promoted_value)

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
- Relevance to the main topic of property decorators in Python OOP.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to property decorators.
    """
    print("1. Basic Property Usage:")
    demonstrate_basic_property()
    
    print("\n2. Lazy Property:")
    demonstrate_lazy_property()
    
    print("\n3. Validated Property:")
    demonstrate_validated_property()
    
    print("\n4. Best Practices and Advanced Tips:")
    demonstrate_best_practices()
    
    print("\n5. Real-World Application (Caching System):")
    demonstrate_real_world_application()
    
    print("\n6. Asynchronous Property:")
    asyncio.run(demonstrate_async_property())
    
    print("\n7. Performance Benchmarking:")
    benchmark_property_vs_attribute()
    
    print("\n8. Optimized Property Access:")
    optimize_property_access()
    
    print("\n9. Attribute Promotion:")
    demonstrate_attribute_promotion()

if __name__ == "__main__":
    main()