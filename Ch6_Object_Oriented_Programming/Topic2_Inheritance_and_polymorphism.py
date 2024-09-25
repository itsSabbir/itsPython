"""
Object-Oriented Programming - Inheritance and Polymorphism - in the Python Programming Language
===============================================================================================

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
Inheritance and polymorphism are fundamental concepts in object-oriented programming (OOP) that enable code reuse, extensibility, and flexibility in software design.

Inheritance:
- Definition: A mechanism that allows a new class to be based on an existing class, inheriting its attributes and methods.
- Purpose: To create a hierarchy of classes, promoting code reuse and establishing relationships between classes.

Polymorphism:
- Definition: The ability of different classes to be treated as instances of the same class through a common interface.
- Purpose: To write more flexible and extensible code by allowing objects of different types to be used interchangeably.

Historical context:
- These concepts have been core to OOP since its inception in the 1960s with Simula 67.
- Python has supported inheritance and polymorphism since its creation in 1991.
- Python's implementation of these concepts is influenced by its "duck typing" philosophy.

Significance:
- Inheritance allows for the creation of specialized classes based on more general ones, reducing code duplication.
- Polymorphism enables the creation of more modular and flexible code structures.
- Together, they form the basis for many design patterns and architectural styles in software development.

Common use cases:
- Creating hierarchies of related classes (e.g., shapes, animals, vehicles)
- Implementing plugins or extension systems
- Defining abstract interfaces and their concrete implementations

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from abc import ABC, abstractmethod
from typing import List, Any

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def speak(self) -> str:
        """Abstract method to be implemented by subclasses."""
        pass
    
    def introduce(self) -> str:
        """Concrete method using the abstract speak method."""
        return f"My name is {self.name} and I say {self.speak()}"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

class Duck(Animal):
    def speak(self) -> str:
        return "Quack!"

def demonstrate_basic_inheritance_and_polymorphism():
    """Demonstrate basic concepts of inheritance and polymorphism."""
    animals: List[Animal] = [Dog("Buddy"), Cat("Whiskers"), Duck("Donald")]
    
    for animal in animals:
        print(animal.introduce())

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

def demonstrate_advanced_inheritance():
    """Demonstrate more advanced inheritance concepts."""
    shapes: List[Shape] = [Circle(5), Rectangle(4, 6), Square(3)]
    
    for shape in shapes:
        print(f"{type(shape).__name__}:")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Favor composition over inheritance when possible.
2. Use abstract base classes to define interfaces.
3. Follow the Liskov Substitution Principle: subclasses should be substitutable for their base classes.
4. Keep inheritance hierarchies shallow and focused.
5. Use method overriding judiciously and document when methods are intended to be overridden.

Common Pitfalls:
1. Overusing inheritance, leading to complex and rigid class hierarchies.
2. Violating the Liskov Substitution Principle, causing unexpected behavior in subclasses.
3. Forgetting to call the superclass constructor in subclasses.
4. Using multiple inheritance without understanding the method resolution order (MRO).

Advanced Tips:
1. Use `super()` for proper method resolution in complex inheritance hierarchies.
2. Leverage `__slots__` for memory optimization in large inheritance trees.
3. Implement custom `__init_subclass__` methods for class customization.
4. Use metaclasses for advanced control over class creation and behavior.
"""

class Meta(type):
    def __new__(mcs, name, bases, attrs):
        # Add a new method to the class
        attrs['describe'] = lambda self: f"I am a {name}"
        return super().__new__(mcs, name, bases, attrs)

class BaseWithMeta(metaclass=Meta):
    pass

class Derived(BaseWithMeta):
    pass

def demonstrate_advanced_techniques():
    """Demonstrate advanced inheritance and polymorphism techniques."""
    obj = Derived()
    print(obj.describe())  # Output: I am a Derived

    # Demonstrate method resolution order
    class A:
        def method(self):
            return "A"

    class B(A):
        def method(self):
            return "B" + super().method()

    class C(A):
        def method(self):
            return "C" + super().method()

    class D(B, C):
        pass

    d = D()
    print(f"MRO demonstration: {d.method()}")  # Output: BCA
    print(f"MRO of D: {[cls.__name__ for cls in D.__mro__]}")

"""
4. Integration and Real-World Applications
------------------------------------------
Inheritance and polymorphism are widely used in various Python libraries and frameworks:

1. Django: Uses class-based views with inheritance for code reuse and customization.
2. SQLAlchemy: Employs inheritance in its ORM for different database dialects.
3. Python's built-in libraries: e.g., `collections.abc` provides abstract base classes for containers.

Real-world example: A simple plugin system using inheritance and polymorphism
"""

class Plugin(ABC):
    @abstractmethod
    def activate(self):
        pass
    
    @abstractmethod
    def deactivate(self):
        pass

class LoggingPlugin(Plugin):
    def activate(self):
        print("Logging plugin activated")
    
    def deactivate(self):
        print("Logging plugin deactivated")

class SecurityPlugin(Plugin):
    def activate(self):
        print("Security plugin activated")
    
    def deactivate(self):
        print("Security plugin deactivated")

class PluginManager:
    def __init__(self):
        self.plugins: List[Plugin] = []
    
    def add_plugin(self, plugin: Plugin):
        self.plugins.append(plugin)
    
    def activate_all(self):
        for plugin in self.plugins:
            plugin.activate()
    
    def deactivate_all(self):
        for plugin in self.plugins:
            plugin.deactivate()

def demonstrate_real_world_application():
    """Demonstrate a real-world application of inheritance and polymorphism in a plugin system."""
    manager = PluginManager()
    manager.add_plugin(LoggingPlugin())
    manager.add_plugin(SecurityPlugin())
    
    print("Activating all plugins:")
    manager.activate_all()
    
    print("\nDeactivating all plugins:")
    manager.deactivate_all()

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Protocol classes: A new way to define interfaces in Python 3.8+ using the typing module.
2. Structural subtyping: Using duck typing and protocols for more flexible polymorphism.
3. Generic types: Using type variables for creating classes and functions that work with multiple types.
"""

from typing import Protocol, TypeVar, List

T = TypeVar('T')

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...

def bubble_sort(items: List[T]) -> List[T]:
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts in inheritance and polymorphism."""
    # Using structural subtyping with bubble_sort
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_numbers = bubble_sort(numbers)
    print(f"Sorted numbers: {sorted_numbers}")
    
    # Custom class that implements the Comparable protocol
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
        
        def __lt__(self, other: 'Person') -> bool:
            return self.age < other.age
        
        def __repr__(self) -> str:
            return f"Person(name='{self.name}', age={self.age})"
    
    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
    sorted_people = bubble_sort(people)
    print(f"Sorted people: {sorted_people}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: What's the difference between inheritance and composition?
A: Inheritance creates an "is-a" relationship, while composition creates a "has-a" relationship. Inheritance is about reusing and extending behavior, while composition is about combining objects to create more complex ones.

Q: How does Python handle multiple inheritance?
A: Python uses the C3 linearization algorithm to determine the method resolution order (MRO) in multiple inheritance scenarios. This ensures a consistent and predictable order for method lookup.

Q: What's the purpose of abstract base classes in Python?
A: Abstract base classes define interfaces and common behavior for their subclasses. They can't be instantiated directly and may contain abstract methods that must be implemented by concrete subclasses.

Troubleshooting:
1. If you're getting unexpected method resolution in multiple inheritance, check the MRO using `ClassName.__mro__`.
2. For "TypeError: Can't instantiate abstract class" errors, ensure all abstract methods are implemented in concrete subclasses.
3. If facing issues with `super()` calls, make sure the class hierarchy is properly defined and all `__init__` methods are called correctly.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- mypy: A static type checker that can help catch inheritance and polymorphism-related errors.
- pylint: A linter that can identify potential issues with class hierarchies and method overrides.
- abc module: Built-in module for defining abstract base classes.
- typing module: Provides support for type hints, including Protocol classes for structural subtyping.

Resources:
- "Python in Practice" by Mark Summerfield
- "Fluent Python" by Luciano Ramalho
- Python's official documentation on inheritance: https://docs.python.org/3/tutorial/classes.html#inheritance
- Real Python's guide on inheritance and composition: https://realpython.com/inheritance-composition-python/
- PEP 3119 - Introducing Abstract Base Classes: https://www.python.org/dev/peps/pep-3119/

8. Performance Analysis and Optimization
----------------------------------------
When working with inheritance and polymorphism, it's important to consider their performance implications, especially in large-scale applications.
"""

import timeit

def benchmark_inheritance_vs_composition():
    """Benchmark the performance difference between inheritance and composition."""
    class BaseInheritance:
        def method(self):
            pass
    
    class DerivedInheritance(BaseInheritance):
        def method(self):
            super().method()
    
    class Composition:
        def __init__(self):
            self.base = BaseInheritance()
        
        def method(self):
            self.base.method()
    
    def use_inheritance():
        obj = DerivedInheritance()
        obj.method()
    
    def use_composition():
        obj = Composition()
        obj.method()
    
    inheritance_time = timeit.timeit(use_inheritance, number=1000000)
    composition_time = timeit.timeit(use_composition, number=1000000)
    
    print(f"Inheritance time: {inheritance_time:.6f} seconds")
    print(f"Composition time: {composition_time:.6f} seconds")
    print(f"Composition overhead: {composition_time / inheritance_time:.2f}x")

"""
Performance Considerations:
1. Method lookup in deep inheritance hierarchies can be slower than in shallow ones.
2. Multiple inheritance can lead to complex method resolution paths, potentially impacting performance.
3. Using `__slots__` in classes can significantly reduce memory usage, especially in large inheritance trees.

Optimization Strategies:
1. Keep inheritance hierarchies shallow and focused.
2. Use composition instead of inheritance for complex relationships between objects.
3. Leverage `__slots__` for memory optimization in classes with many instances.
4. Profile your code to identify performance bottlenecks related to inheritance and method calls.

Example of optimizing a class hierarchy with __slots__:
"""

class OptimizedBase:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class OptimizedDerived(OptimizedBase):
    __slots__ = ['z']
    
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

def demonstrate_optimized_inheritance():
    """Demonstrate memory optimization using __slots__ in an inheritance hierarchy."""
    import sys
    
    class RegularBase:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class RegularDerived(RegularBase):
        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z = z
    
    regular_obj = RegularDerived(1, 2, 3)
    optimized_obj = OptimizedDerived(1, 2, 3)
    
    print(f"Memory usage of RegularDerived: {sys.getsizeof(regular_obj)} bytes")
    print(f"Memory usage of OptimizedDerived: {sys.getsizeof(optimized_obj)} bytes")

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
- Relevance to the main topic of inheritance and polymorphism in Python OOP.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to inheritance and polymorphism.
    """
    print("1. Basic Inheritance and Polymorphism:")
    demonstrate_basic_inheritance_and_polymorphism()
    
    print("\n2. Advanced Inheritance:")
    demonstrate_advanced_inheritance()
    
    print("\n3. Advanced Techniques:")
    demonstrate_advanced_techniques()
    
    print("\n4. Real-World Application (Plugin System):")
    demonstrate_real_world_application()
    
    print("\n5. Advanced Concepts:")
    demonstrate_advanced_concepts()
    
    print("\n6. Performance Benchmarking:")
    benchmark_inheritance_vs_composition()
    
    print("\n7. Optimized Inheritance Example:")
    demonstrate_optimized_inheritance()

if __name__ == "__main__":
    main()