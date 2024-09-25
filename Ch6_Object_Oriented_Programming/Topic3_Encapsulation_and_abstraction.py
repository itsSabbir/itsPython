"""
Object-Oriented Programming - Encapsulation and Abstraction - in the Python Programming Language
================================================================================================

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
Encapsulation and abstraction are fundamental principles of object-oriented programming (OOP) that help in creating modular, maintainable, and scalable code. These concepts are crucial for managing complexity in large software systems.

Encapsulation:
- Definition: The bundling of data and methods that operate on that data within a single unit (class).
- Purpose: To hide the internal state of an object and restrict direct access to it.

Abstraction:
- Definition: The process of hiding complex implementation details and showing only the necessary features of an object.
- Purpose: To reduce complexity and allow focusing on relevant aspects of an object.

Historical context:
- These concepts have been part of OOP since its inception in the 1960s with Simula 67.
- Python, being a multi-paradigm language, has supported OOP features since its creation in 1991.
- Python's approach to encapsulation is more about convention than strict enforcement, aligning with its "we're all consenting adults" philosophy.

Significance:
- Encapsulation promotes data integrity and reduces dependencies between different parts of a program.
- Abstraction allows for the creation of complex systems by hiding unnecessary details and providing a clear, high-level interface.

Common use cases:
- Data validation and access control
- Implementing design patterns (e.g., Adapter, Facade)
- Creating APIs and libraries with stable interfaces

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from abc import ABC, abstractmethod
from typing import List, Any, Dict

class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute
    
    @property
    def account_number(self) -> str:
        """Getter for account_number (read-only)."""
        return self._account_number
    
    @property
    def balance(self) -> float:
        """Getter for balance."""
        return self.__balance
    
    @balance.setter
    def balance(self, value: float) -> None:
        """Setter for balance with validation."""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
    
    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

def demonstrate_encapsulation():
    """Demonstrate encapsulation in Python."""
    account = BankAccount("1234567890", 1000.0)
    
    print(f"Account Number: {account.account_number}")
    print(f"Initial Balance: {account.balance}")
    
    account.deposit(500.0)
    print(f"Balance after deposit: {account.balance}")
    
    account.withdraw(200.0)
    print(f"Balance after withdrawal: {account.balance}")
    
    try:
        account.balance = -100.0  # This will raise an exception
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        # This will raise an AttributeError (cannot access private attribute directly)
        print(account.__balance)
    except AttributeError as e:
        print(f"Error: {e}")

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
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

def demonstrate_abstraction():
    """Demonstrate abstraction in Python."""
    shapes: List[Shape] = [Circle(5), Rectangle(4, 6)]
    
    for shape in shapes:
        print(f"{type(shape).__name__}:")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use clear naming conventions for public, protected, and private attributes.
2. Implement getters and setters using the @property decorator when needed.
3. Use abstract base classes to define interfaces for related classes.
4. Follow the principle of least privilege: only expose what is necessary.

Common Pitfalls:
1. Overusing getters and setters for every attribute.
2. Ignoring Python's convention-based privacy (relying too heavily on name mangling).
3. Creating overly complex abstractions that hinder rather than help understanding.
4. Forgetting to implement abstract methods in concrete classes.

Advanced Tips:
1. Use descriptors for reusable property logic across multiple classes.
2. Leverage metaclasses for advanced control over class creation and behavior.
3. Implement context managers to ensure proper resource management.
4. Use `__slots__` for memory optimization in classes with a fixed set of attributes.
"""

class ValidatedProperty:
    """A descriptor class for implementing validated properties."""
    
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)
    
    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)
    
    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)
    
    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)
    
    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)
    
    def deleter(self, fdel):
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

def demonstrate_advanced_techniques():
    """Demonstrate advanced encapsulation and abstraction techniques."""
    person = Person("Alice", 30)
    print(f"Initial: Name: {person.name}, Age: {person.age}")
    
    person.name = "Bob"
    person.age = 35
    print(f"After update: Name: {person.name}, Age: {person.age}")
    
    try:
        person.name = ""
    except ValueError as e:
        print(f"Error setting name: {e}")
    
    try:
        person.age = 200
    except ValueError as e:
        print(f"Error setting age: {e}")

"""
4. Integration and Real-World Applications
------------------------------------------
Encapsulation and abstraction are widely used in various Python libraries and frameworks:

1. Django ORM: Uses encapsulation to hide database operations and provide a high-level API.
2. SQLAlchemy: Employs abstraction to provide a uniform interface for different database backends.
3. Requests library: Abstracts away the complexities of HTTP requests behind a simple interface.

Real-world example: A simple content management system (CMS) using encapsulation and abstraction
"""

class Content(ABC):
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def author(self) -> str:
        return self._author
    
    @abstractmethod
    def display(self) -> str:
        pass

class Article(Content):
    def __init__(self, title: str, author: str, body: str):
        super().__init__(title, author)
        self._body = body
    
    def display(self) -> str:
        return f"Article: {self.title} by {self.author}\n\n{self._body}"

class Video(Content):
    def __init__(self, title: str, author: str, url: str, duration: int):
        super().__init__(title, author)
        self._url = url
        self._duration = duration
    
    def display(self) -> str:
        return f"Video: {self.title} by {self.author}\nURL: {self._url}\nDuration: {self._duration} seconds"

class ContentManagementSystem:
    def __init__(self):
        self._content: List[Content] = []
    
    def add_content(self, content: Content) -> None:
        self._content.append(content)
    
    def display_all_content(self) -> None:
        for item in self._content:
            print(item.display())
            print("-" * 40)

def demonstrate_real_world_application():
    """Demonstrate a real-world application of encapsulation and abstraction in a CMS."""
    cms = ContentManagementSystem()
    
    article = Article("Python Basics", "John Doe", "Python is a versatile programming language...")
    video = Video("OOP in Python", "Jane Smith", "https://example.com/oop-video", 600)
    
    cms.add_content(article)
    cms.add_content(video)
    
    cms.display_all_content()

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Protocol classes: A new way to define interfaces in Python 3.8+ using the typing module.
2. Data classes: Simplifying the creation of classes that are primarily used to store data.
3. Type hinting and static type checking: Enhancing code clarity and catching errors early.
"""

from typing import Protocol, runtime_checkable
from dataclasses import dataclass

@runtime_checkable
class Printable(Protocol):
    def print_info(self) -> str:
        ...

@dataclass
class Book:
    title: str
    author: str
    year: int
    
    def print_info(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

def print_item(item: Printable) -> None:
    print(item.print_info())

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts in encapsulation and abstraction."""
    book = Book("1984", "George Orwell", 1949)
    print_item(book)
    
    print(f"Is Book Printable? {isinstance(book, Printable)}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: How can I achieve true private attributes in Python?
A: While Python doesn't have true private attributes, you can use name mangling (double underscore prefix) to make attributes harder to access from outside the class.

Q: What's the difference between an abstract class and an interface?
A: In Python, abstract classes can have method implementations, while interfaces (implemented using abstract base classes with only abstract methods) cannot.

Q: How do I choose between inheritance and composition for code reuse?
A: Use inheritance for "is-a" relationships and composition for "has-a" relationships. Prefer composition over inheritance when possible to reduce coupling.

Troubleshooting:
1. If you're getting AttributeError when accessing a "private" attribute, check if it's name-mangled (e.g., `self.__attribute` becomes `self._ClassName__attribute`).
2. For unexpected behavior in inherited abstract methods, ensure all abstract methods are implemented in concrete classes.
3. If type hinting doesn't seem to work, make sure you're using a compatible version of Python and have proper tooling set up (e.g., mypy).

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- mypy: A static type checker that can help enforce encapsulation and abstraction principles.
- pylint: A linter that can identify potential issues with class design and attribute usage.
- abc module: Built-in module for defining abstract base classes.
- dataclasses: Built-in module for automatically adding generated special methods to classes.

Resources:
- "Python in a Nutshell" by Alex Martelli, Anna Ravenscroft, and Steve Holden
- "Fluent Python" by Luciano Ramalho
- Python's official documentation on data model: https://docs.python.org/3/reference/datamodel.html
- Real Python's guide on OOP: https://realpython.com/python3-object-oriented-programming/
- PEP 3119 - Introducing Abstract Base Classes: https://www.python.org/dev/peps/pep-3119/

8. Performance Analysis and Optimization
----------------------------------------
When working with encapsulation and abstraction, it's important to consider their performance implications, especially in large-scale applications.
"""

import timeit

def benchmark_attribute_access():
    """Benchmark the performance difference between direct and property-based attribute access."""
    class DirectAccess:
        def __init__(self):
            self.attr = 42
    
    class PropertyAccess:
        def __init__(self):
            self._attr = 42
        
        @property
        def attr(self):
            return self._attr
        
        @attr.setter
        def attr(self, value):
            self._attr = value
    
    direct_obj = DirectAccess()
    property_obj = PropertyAccess()
    
    def direct_access():
        return direct_obj.attr
    
    def property_access():
        return property_obj.attr
    
    direct_time = timeit.timeit(direct_access, number=1000000)
    property_time = timeit.timeit(property_access, number=1000000)
    
    print(f"Direct attribute access time: {direct_time:.6f} seconds")
    print(f"Property-based access time: {property_time:.6f} seconds")
    print(f"Property overhead: {property_time / direct_time:.2f}x")

def optimize_attribute_access():
    """Demonstrate techniques to optimize attribute access."""
    class OptimizedAccess:
        __slots__ = ['_value']
        
        def __init__(self, value):
            self._value = value
        
        def get_value(self):
            return self._value
        
        def set_value(self, new_value):
            self._value = new_value
    
    obj = OptimizedAccess(42)
    
    def access_with_methods():
        obj.get_value()
        obj.set_value(43)
    
    optimized_time = timeit.timeit(access_with_methods, number=1000000)
    print(f"Optimized access time: {optimized_time:.6f} seconds")

"""
Performance Considerations:
1. Direct attribute access is generally faster than property-based access due to the function call overhead of properties.
2. The `__slots__` declaration can significantly reduce memory usage and slightly improve attribute access speed for classes with a fixed set of attributes.
3. Method calls for getters and setters are slightly slower than direct attribute access but faster than property access.

Optimization Strategies:
1. Use direct attribute access for simple, internal attributes that don't require validation or complex logic.
2. Consider using `__slots__` for classes with a large number of instances or a fixed set of attributes.
3. For frequently accessed attributes that require some logic, consider using methods instead of properties.
4. Use caching techniques for expensive computations in property getters.

Example of optimizing a class with many instances:
"""

class OptimizedPoint:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

def demonstrate_optimized_class():
    """Demonstrate the memory efficiency of a class using __slots__."""
    import sys
    
    class RegularPoint:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    regular_point = RegularPoint(1, 2)
    optimized_point = OptimizedPoint(1, 2)
    
    print(f"Memory usage of RegularPoint: {sys.getsizeof(regular_point)} bytes")
    print(f"Memory usage of OptimizedPoint: {sys.getsizeof(optimized_point)} bytes")

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
- Relevance to the main topic of encapsulation and abstraction in Python OOP.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to encapsulation and abstraction.
    """
    print("1. Demonstrating Encapsulation:")
    demonstrate_encapsulation()
    
    print("\n2. Demonstrating Abstraction:")
    demonstrate_abstraction()
    
    print("\n3. Advanced Techniques:")
    demonstrate_advanced_techniques()
    
    print("\n4. Real-World Application (CMS):")
    demonstrate_real_world_application()
    
    print("\n5. Advanced Concepts:")
    demonstrate_advanced_concepts()
    
    print("\n6. Performance Benchmarking:")
    benchmark_attribute_access()
    
    print("\n7. Optimized Attribute Access:")
    optimize_attribute_access()
    
    print("\n8. Memory Optimization with __slots__:")
    demonstrate_optimized_class()

if __name__ == "__main__":
    main()