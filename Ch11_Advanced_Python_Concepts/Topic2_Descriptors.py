"""
Advanced Python Concepts - Descriptors - in the Python Programming Language
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
Descriptors are a powerful feature in Python that provide a way to customize attribute access in objects. They allow you to define how attributes are get, set, or deleted, providing fine-grained control over attribute behavior.

Historical context:
- Descriptors were introduced in Python 2.2 (2001) as part of the unification of types and classes.
- They were designed to provide a clean way to implement computed attributes and to support the property() built-in function.
- Descriptors form the basis for many of Python's core features, including properties, methods, and class methods.

Significance:
- Descriptors enable the creation of reusable attribute access patterns.
- They are fundamental to implementing many of Python's higher-level features and design patterns.
- Descriptors allow for powerful object-oriented programming techniques, such as lazy evaluation and attribute validation.

Common use cases:
- Implementing computed or managed attributes
- Attribute validation and type checking
- Lazy loading of expensive resources
- Implementing caching mechanisms
- Creating decorators that modify attribute behavior

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from typing import Any, TypeVar, Generic

T = TypeVar('T')

class Descriptor:
    """
    A basic descriptor class that demonstrates the descriptor protocol.
    
    The descriptor protocol consists of three methods:
    - __get__: Called when the attribute is accessed
    - __set__: Called when the attribute is assigned a value
    - __delete__: Called when the attribute is deleted
    """
    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        print("Getting the attribute")
        return self._value
    
    def __set__(self, obj: Any, value: Any) -> None:
        print("Setting the attribute")
        self._value = value
    
    def __delete__(self, obj: Any) -> None:
        print("Deleting the attribute")
        del self._value

class ExampleClass:
    descriptor = Descriptor()

def demonstrate_basic_descriptor():
    """Demonstrate basic usage of a descriptor."""
    example = ExampleClass()
    
    example.descriptor = 42
    print(example.descriptor)
    del example.descriptor

class TypedDescriptor(Generic[T]):
    """
    A descriptor that enforces type checking.
    
    This demonstrates how descriptors can be used for attribute validation.
    """
    def __init__(self, name: str, expected_type: type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, obj: Any, objtype: Any = None) -> T:
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj: Any, value: T) -> None:
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be of type {self.expected_type}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj: Any) -> None:
        del obj.__dict__[self.name]

class Person:
    name = TypedDescriptor("name", str)
    age = TypedDescriptor("age", int)

def demonstrate_typed_descriptor():
    """Demonstrate the use of a descriptor for type checking."""
    person = Person()
    person.name = "Alice"
    person.age = 30
    
    print(f"Name: {person.name}, Age: {person.age}")
    
    try:
        person.age = "thirty"  # This should raise a TypeError
    except TypeError as e:
        print(f"Error: {e}")

class LazyProperty:
    """
    A descriptor that implements lazy loading of an attribute.
    
    This demonstrates how descriptors can be used for performance optimization.
    """
    def __init__(self, func: callable):
        self.func = func
    
    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.func.__name__, value)
        return value

class ExpensiveResource:
    @LazyProperty
    def resource(self):
        print("Loading expensive resource...")
        # Simulate expensive computation or I/O operation
        import time
        time.sleep(2)
        return "Expensive Resource Data"

def demonstrate_lazy_property():
    """Demonstrate the use of a descriptor for lazy loading."""
    obj = ExpensiveResource()
    print("Object created, resource not yet loaded.")
    print(f"Accessing resource: {obj.resource}")
    print("Accessing resource again (should be instantaneous):")
    print(f"Resource: {obj.resource}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use descriptors for reusable attribute access patterns across multiple classes.
2. Implement all three methods (__get__, __set__, __delete__) for a complete descriptor.
3. Use descriptors to enforce data validation and maintain invariants.
4. Consider using descriptors for implementing caching mechanisms.

Common Pitfalls:
1. Forgetting that descriptors are shared between instances of a class.
2. Incorrectly implementing __get__ method, leading to infinite recursion.
3. Overusing descriptors for simple cases where properties would suffice.
4. Not considering the performance impact of complex descriptor logic.

Advanced Tips:
1. Use `__set_name__` method for automatic naming of descriptors (Python 3.6+).
2. Combine descriptors with metaclasses for even more powerful class customization.
3. Implement non-data descriptors (only __get__ method) for method-like behaviors.
4. Use descriptors to implement attribute aliases or computed attributes.
"""

class DescriptorWithSetName:
    """
    A descriptor that automatically sets its name.
    
    This demonstrates the use of __set_name__ method introduced in Python 3.6.
    """
    def __set_name__(self, owner: Any, name: str) -> None:
        self.name = name
    
    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)
    
    def __set__(self, obj: Any, value: Any) -> None:
        obj.__dict__[self.name] = value

class AutoNamedAttributes:
    x = DescriptorWithSetName()
    y = DescriptorWithSetName()

def demonstrate_set_name():
    """Demonstrate the use of __set_name__ in descriptors."""
    obj = AutoNamedAttributes()
    obj.x = 10
    obj.y = 20
    print(f"x: {obj.x}, y: {obj.y}")
    print(f"Descriptor names: x.name = {obj.__class__.x.name}, y.name = {obj.__class__.y.name}")

"""
4. Integration and Real-World Applications
------------------------------------------
Descriptors are used extensively in Python's standard library and many third-party libraries:

1. Django ORM: Uses descriptors for field definitions in models.
2. SQLAlchemy: Employs descriptors for declarative ORM functionality.
3. attrs library: Utilizes descriptors for its attribute management.

Real-world example: Implementing a Unit Conversion System
"""

class Unit:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

class Distance:
    """A class representing distance with automatic unit conversion."""
    
    def __init__(self, value: float, unit: str = 'm'):
        self._distance = Unit(value, unit)
    
    class DistanceDescriptor:
        def __init__(self, unit: str, conversion_factor: float):
            self.unit = unit
            self.conversion_factor = conversion_factor
        
        def __get__(self, obj: Any, objtype: Any = None) -> float:
            if obj is None:
                return self
            return obj._distance.value * self.conversion_factor
        
        def __set__(self, obj: Any, value: float) -> None:
            obj._distance = Unit(value / self.conversion_factor, 'm')
    
    meters = DistanceDescriptor('m', 1)
    kilometers = DistanceDescriptor('km', 0.001)
    miles = DistanceDescriptor('mi', 0.000621371)

def demonstrate_unit_conversion():
    """Demonstrate a real-world application of descriptors in a unit conversion system."""
    distance = Distance(5000)  # 5000 meters
    print(f"Distance in meters: {distance.meters}m")
    print(f"Distance in kilometers: {distance.kilometers}km")
    print(f"Distance in miles: {distance.miles}mi")
    
    distance.kilometers = 10  # Set to 10 km
    print(f"\nUpdated distance in meters: {distance.meters}m")
    print(f"Updated distance in miles: {distance.miles}mi")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Descriptor Protocol Updates: PEP 487 introduced __set_name__ for easier descriptor implementation.
2. Data Classes: While not directly related, data classes (introduced in Python 3.7) provide an alternative to some use cases of descriptors.
3. Type Hinting for Descriptors: Ongoing improvements in static type checking support for descriptors.
4. Asynchronous Descriptors: Exploration of descriptor-like behavior in asynchronous contexts.
"""

import asyncio

class AsyncDescriptor:
    """
    A descriptor that supports asynchronous get and set operations.
    
    This demonstrates an emerging concept of descriptors in asynchronous programming.
    """
    def __init__(self):
        self._value = None
    
    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        return self._value
    
    async def async_get(self, obj: Any) -> Any:
        await asyncio.sleep(1)  # Simulate async operation
        return self._value
    
    async def async_set(self, obj: Any, value: Any) -> None:
        await asyncio.sleep(1)  # Simulate async operation
        self._value = value

class AsyncExample:
    descriptor = AsyncDescriptor()

async def demonstrate_async_descriptor():
    """Demonstrate the use of an asynchronous descriptor."""
    obj = AsyncExample()
    await obj.descriptor.async_set(obj, "Async Value")
    value = await obj.descriptor.async_get(obj)
    print(f"Async Descriptor Value: {value}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use descriptors instead of properties?
A: Use descriptors when you need to reuse the same attribute access logic across multiple classes or when you need more control over the attribute access process.

Q: How can I debug descriptor behavior?
A: Implement logging in descriptor methods, use the `vars()` function to inspect object dictionaries, and consider using the `inspect` module for introspection.

Q: Can descriptors be used with slots?
A: Yes, but with some limitations. Descriptors work with slots, but you cannot use the instance dictionary for storage as it doesn't exist with slots.

Troubleshooting:
1. If a descriptor seems to be ignored, check if it's being overwritten in the instance dictionary.
2. For performance issues, profile your code and consider caching descriptor results.
3. If facing unexpected behavior with inheritance, remember that descriptors are resolved using the same MRO as methods.
"""

import inspect

def troubleshooting_examples():
    """Demonstrate troubleshooting techniques for descriptors."""
    
    class DebugDescriptor:
        def __get__(self, obj: Any, objtype: Any = None) -> Any:
            print(f"Getting attribute from {obj}")
            return 42
        
        def __set__(self, obj: Any, value: Any) -> None:
            print(f"Setting attribute on {obj} to {value}")
    
    class DebuggedClass:
        attr = DebugDescriptor()
    
    obj = DebuggedClass()
    print("Accessing attribute:")
    obj.attr
    print("\nSetting attribute:")
    obj.attr = 10
    
    print("\nInspecting class:")
    print(inspect.getmembers(DebuggedClass, lambda x: isinstance(x, DebugDescriptor)))

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. attrs: Provides class creation utilities that can work alongside descriptors.
2. descriptor_tools: A library with utilities for working with descriptors.
3. typeguard: Can be used in conjunction with descriptors for runtime type checking.
4. PyDantic: While not directly related to descriptors, it offers an alternative for data validation.

Resources:
- "Python Cookbook" by David Beazley and Brian K. Jones (Chapter on Metaprogramming)
- "Fluent Python" by Luciano Ramalho (Chapters on Descriptors and Metaclasses)
- Python's official documentation on descriptors: https://docs.python.org/3/howto/descriptor.html
- Raymond Hettinger's "Descriptor HowTo Guide": https://github.com/rhettinger/descriptor_tools
- PEP 487 - Simpler customization of class creation: https://www.python.org/dev/peps/pep-0487/

8. Performance Analysis and Optimization
----------------------------------------
When working with descriptors, it's important to consider their performance implications, especially in frequently accessed attributes or large-scale applications.
"""

import timeit

def performance_comparison():
    """Compare performance of different attribute access methods."""
    
    class PlainClass:
        def __init__(self):
            self._attr = 0
        
        def get_attr(self):
            return self._attr
        
        def set_attr(self, value):
            self._attr = value
    
    class PropertyClass:
        def __init__(self):
            self._attr = 0
        
        @property
        def attr(self):
            return self._attr
        
        @attr.setter
        def attr(self, value):
            self._attr = value
    
    class DescriptorClass:
        class Descriptor:
            def __get__(self, obj: Any, objtype: Any = None) -> Any:
                return obj._attr
            
            def __set__(self, obj: Any, value: Any) -> None:
                obj._attr = value
        
        attr = Descriptor()
        
        def __init__(self):
            self._attr = 0
    
    def test_plain():
        obj = PlainClass()
        obj.set_attr(1)
        obj.get_attr()
    
    def test_property():
        obj = PropertyClass()
        obj.attr = 1
        obj.attr
    
    def test_descriptor():
        obj = DescriptorClass()
        obj.attr = 1
        obj.attr
    
    plain_time = timeit.timeit(test_plain, number=1000000)
    property_time = timeit.timeit(test_property, number=1000000)
    descriptor_time = timeit.timeit(test_descriptor, number=1000000)
    
    print(f"Plain attribute access time: {plain_time:.6f} seconds")
    print(f"Property access time: {property_time:.6f} seconds")
    print(f"Descriptor access time: {descriptor_time:.6f} seconds")
    
    print(f"\nProperty overhead: {(property_time - plain_time) / plain_time:.2%}")
    print(f"Descriptor overhead: {(descriptor_time - plain_time) / plain_time:.2%}")

"""
Performance Considerations:
1. Descriptors add a small overhead compared to plain attribute access.
2. For simple cases, properties might be slightly faster than custom descriptors.
3. The performance impact of descriptors is usually negligible unless used in tight loops or performance-critical code.
4. Complex logic in descriptor methods can significantly impact performance.

Optimization Strategies:
1. Use caching or memoization techniques for expensive computations in descriptors.
2. Consider using __slots__ to reduce memory usage when using many descriptors.
3. For performance-critical code, benchmark different implementations (plain attributes, properties, descriptors) to choose the best approach.
4. Use profiling tools to identify bottlenecks in descriptor usage.
"""

class CachedDescriptor:
    """A descriptor that caches its value after first access."""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)
        return value

class OptimizedExample:
    @CachedDescriptor
    def expensive_calculation(self):
        print("Performing expensive calculation...")
        import time
        time.sleep(1)  # Simulate expensive operation
        return 42

def demonstrate_optimized_descriptor():
    """Demonstrate an optimized descriptor with caching."""
    obj = OptimizedExample()
    
    start = time.time()
    result1 = obj.expensive_calculation
    time1 = time.time() - start
    
    start = time.time()
    result2 = obj.expensive_calculation
    time2 = time.time() - start
    
    print(f"First call result: {result1}, time: {time1:.4f} seconds")
    print(f"Second call result: {result2}, time: {time2:.4f} seconds")

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
- Relevance to the main topic of descriptors in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to descriptors in Python.
    """
    print("Basic Descriptor Usage:")
    demonstrate_basic_descriptor()
    
    print("\nTyped Descriptor:")
    demonstrate_typed_descriptor()
    
    print("\nLazy Property:")
    demonstrate_lazy_property()
    
    print("\nDescriptor with __set_name__:")
    demonstrate_set_name()
    
    print("\nUnit Conversion System:")
    demonstrate_unit_conversion()
    
    print("\nAsynchronous Descriptor:")
    asyncio.run(demonstrate_async_descriptor())
    
    print("\nTroubleshooting Examples:")
    troubleshooting_examples()
    
    print("\nPerformance Comparison:")
    performance_comparison()
    
    print("\nOptimized Descriptor:")
    demonstrate_optimized_descriptor()

if __name__ == "__main__":
    main()