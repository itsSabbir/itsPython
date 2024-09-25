"""
Object-Oriented Programming - Classes and Objects - in the Python Programming Language
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
Classes and objects are fundamental concepts in object-oriented programming (OOP). They provide a way to structure code, encapsulate data and behavior, and create reusable, modular software components.

Historical context:
- The concept of classes and objects originated with Simula 67 in the 1960s.
- Python has supported OOP since its inception in 1991.
- Python's implementation of classes evolved significantly with the introduction of "new-style" classes in Python 2.2 (2001) and their becoming the default in Python 3.

Significance:
- Classes provide a blueprint for creating objects, encapsulating data and behavior.
- Objects are instances of classes, representing specific entities with their own state and behavior.
- OOP facilitates code organization, reusability, and maintenance.

Common use cases:
- Modeling real-world entities and concepts in software
- Implementing data structures and abstract data types
- Organizing and structuring large codebases

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

class Person:
    """
    A class representing a person.
    
    This class demonstrates basic class structure, instance variables,
    methods, and the use of docstrings for documentation.
    """
    
    def __init__(self, name: str, age: int):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        """
        Generate an introduction string for the person.
        
        Returns:
            str: An introduction message
        """
        return f"Hello, my name is {self.name} and I'm {self.age} years old."
    
    def have_birthday(self) -> None:
        """Increment the person's age by one year."""
        self.age += 1

def demonstrate_basic_class_usage():
    """Demonstrate basic usage of classes and objects."""
    # Creating an instance of the Person class
    alice = Person("Alice", 30)
    
    # Accessing instance variables
    print(f"Name: {alice.name}")
    print(f"Age: {alice.age}")
    
    # Calling instance methods
    print(alice.introduce())
    
    # Modifying object state
    alice.have_birthday()
    print(f"After birthday: {alice.introduce()}")

class BankAccount:
    """
    A class representing a bank account.
    
    This class demonstrates the use of class variables, property decorators,
    and encapsulation principles.
    """
    
    interest_rate = 0.02  # Class variable
    
    def __init__(self, account_number: str, balance: float = 0):
        self._account_number = account_number
        self._balance = balance
    
    @property
    def account_number(self) -> str:
        """Get the account number."""
        return self._account_number
    
    @property
    def balance(self) -> float:
        """Get the current balance."""
        return self._balance
    
    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit
        
        Raises:
            ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.
        
        Args:
            amount (float): The amount to withdraw
        
        Raises:
            ValueError: If the amount is negative or exceeds the current balance
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
    
    @classmethod
    def set_interest_rate(cls, rate: float) -> None:
        """
        Set the interest rate for all bank accounts.
        
        Args:
            rate (float): The new interest rate
        """
        cls.interest_rate = rate
    
    def apply_interest(self) -> None:
        """Apply the current interest rate to the account balance."""
        self._balance += self._balance * self.interest_rate

def demonstrate_advanced_class_features():
    """Demonstrate advanced features of classes and objects."""
    account1 = BankAccount("1234567890", 1000)
    account2 = BankAccount("0987654321", 2000)
    
    print(f"Account 1 balance: ${account1.balance:.2f}")
    print(f"Account 2 balance: ${account2.balance:.2f}")
    
    account1.deposit(500)
    account2.withdraw(300)
    
    print(f"After transactions:")
    print(f"Account 1 balance: ${account1.balance:.2f}")
    print(f"Account 2 balance: ${account2.balance:.2f}")
    
    print(f"Current interest rate: {BankAccount.interest_rate:.2%}")
    account1.apply_interest()
    account2.apply_interest()
    
    print(f"After applying interest:")
    print(f"Account 1 balance: ${account1.balance:.2f}")
    print(f"Account 2 balance: ${account2.balance:.2f}")
    
    BankAccount.set_interest_rate(0.03)
    print(f"New interest rate: {BankAccount.interest_rate:.2%}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use clear and descriptive names for classes, methods, and attributes.
2. Follow the Single Responsibility Principle: each class should have one primary responsibility.
3. Use property decorators for getter and setter methods to control attribute access.
4. Implement proper encapsulation by using private attributes (prefixed with double underscore).
5. Write comprehensive docstrings for classes and methods.

Common Pitfalls:
1. Overusing inheritance instead of composition.
2. Forgetting to call the superclass constructor in subclasses.
3. Modifying mutable default arguments in method definitions.
4. Ignoring the Liskov Substitution Principle in inheritance hierarchies.

Advanced Tips:
1. Use `__slots__` to optimize memory usage for classes with a fixed set of attributes.
2. Implement custom `__new__` methods for advanced instance creation control.
3. Utilize metaclasses for class creation customization.
4. Use abstract base classes to define interfaces and common behavior.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Shape(ABC):
    """
    An abstract base class for shapes.
    
    This class demonstrates the use of abstract methods and properties.
    """
    
    @property
    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate and return the perimeter of the shape."""
        pass

class Circle(Shape):
    """A class representing a circle."""
    
    __slots__ = ['_radius']
    
    def __init__(self, radius: float):
        self._radius = radius
    
    @property
    def radius(self) -> float:
        """Get the radius of the circle."""
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        """Set the radius of the circle."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self) -> float:
        """Calculate and return the area of the circle."""
        return 3.14159 * self._radius ** 2
    
    def perimeter(self) -> float:
        """Calculate and return the perimeter of the circle."""
        return 2 * 3.14159 * self._radius

class Rectangle(Shape):
    """A class representing a rectangle."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    @property
    def area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def demonstrate_advanced_concepts():
    """Demonstrate advanced OOP concepts in Python."""
    shapes: List[Shape] = [Circle(5), Rectangle(4, 6)]
    
    for shape in shapes:
        print(f"{type(shape).__name__}:")
        print(f"  Area: {shape.area:.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
    
    # Demonstrate the use of __slots__
    circle = Circle(3)
    print(f"\nCircle attributes: {dir(circle)}")
    
    try:
        circle.new_attribute = 42
    except AttributeError as e:
        print(f"Error adding new attribute: {e}")

"""
4. Integration and Real-World Applications
------------------------------------------
Classes and objects are fundamental to many Python libraries and frameworks:

1. Django: Uses class-based views and models to represent database tables.
2. SQLAlchemy: Employs classes to represent database tables and relationships.
3. Pygame: Uses classes to represent game objects and manage game state.

Real-world example: A simple task management system
"""

from datetime import datetime, timedelta

class Task:
    """A class representing a task in a task management system."""
    
    def __init__(self, title: str, description: str, due_date: datetime):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
    
    def complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True
    
    def is_overdue(self) -> bool:
        """Check if the task is overdue."""
        return not self.completed and datetime.now() > self.due_date
    
    def __str__(self) -> str:
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} ({status}) - Due: {self.due_date.strftime('%Y-%m-%d')}"

class Project:
    """A class representing a project containing multiple tasks."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        self.tasks.append(task)
    
    def get_pending_tasks(self) -> List[Task]:
        """Get all pending tasks in the project."""
        return [task for task in self.tasks if not task.completed]
    
    def get_overdue_tasks(self) -> List[Task]:
        """Get all overdue tasks in the project."""
        return [task for task in self.tasks if task.is_overdue()]

def demonstrate_real_world_application():
    """Demonstrate a real-world application of classes and objects."""
    project = Project("Website Redesign")
    
    task1 = Task("Design mockups", "Create initial design mockups", datetime.now() + timedelta(days=7))
    task2 = Task("Implement frontend", "Develop HTML/CSS for new design", datetime.now() + timedelta(days=14))
    task3 = Task("Backend integration", "Integrate new design with backend", datetime.now() + timedelta(days=21))
    
    project.add_task(task1)
    project.add_task(task2)
    project.add_task(task3)
    
    print(f"Project: {project.name}")
    print("Tasks:")
    for task in project.tasks:
        print(f"- {task}")
    
    task1.complete()
    
    print("\nPending tasks:")
    for task in project.get_pending_tasks():
        print(f"- {task}")
    
    # Simulate an overdue task
    task2.due_date = datetime.now() - timedelta(days=1)
    
    print("\nOverdue tasks:")
    for task in project.get_overdue_tasks():
        print(f"- {task}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Data classes: Simplifying the creation of classes primarily used to store data.
2. Type hinting and static type checking: Enhancing code clarity and catching errors early.
3. Structural pattern matching: New feature in Python 3.10+ for advanced object matching and decomposition.
"""

from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grades: List[float] = field(default_factory=list)
    
    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts in Python OOP."""
    student = Student("Alice", 20, [85.5, 92.0, 88.5])
    print(f"Student: {student}")
    print(f"Average grade: {student.average_grade():.2f}")
    
    # Structural pattern matching (Python 3.10+)
    def describe_person(person):
        match person:
            case Student(name=name, age=age) if age < 18:
                return f"{name} is a minor student"
            case Student(name=name, age=age):
                return f"{name} is an adult student"
            case _:
                return "Not a student"
    
    print(describe_person(student))

"""
6. FAQs and Troubleshooting
---------------------------
Q: What's the difference between a class and an instance?
A: A class is a blueprint for creating objects, while an instance is a specific object created from a class.

Q: How do I create a singleton class in Python?
A: You can create a singleton by controlling the instance creation in the `__new__` method or using a module-level object.

Q: What are the benefits of using properties instead of direct attribute access?
A: Properties allow for controlled access to attributes, enabling validation, computed values, and maintaining backwards compatibility.

Troubleshooting:
1. If you're getting AttributeError when accessing an attribute, check for typos and ensure the attribute is defined in the `__init__` method.
2. For unexpected behavior in inherited methods, verify that you're calling the superclass methods when necessary.
3. If facing issues with circular imports, consider restructuring your code or using lazy imports.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- mypy: A static type checker that can help catch errors related to class and object usage.
- pylint: A linter that can identify potential issues with class design and object-oriented principles.
- dataclasses: A built-in module for automatically adding generated special methods to classes.

Resources:
- "Python in Practice" by Mark Summerfield
- "Fluent Python" by Luciano Ramalho
- Python's official documentation on classes: https://docs.python.org/3/tutorial/classes.html
- Real Python's guide on OOP in Python: https://realpython.com/python3-object-oriented-programming/
- PEP 3115 - Metaclasses in Python 3: https://www.python.org/dev/peps/pep-3115/
- PEP 557 - Data Classes: https://www.python.org/dev/peps/pep-0557/

8. Performance Analysis and Optimization
----------------------------------------
When working with classes and objects in Python, it's important to consider their performance implications, especially in large-scale applications or performance-critical code.
"""

import timeit
from sys import getsizeof

def benchmark_class_vs_dict():
    """Benchmark the performance difference between class instances and dictionaries."""
    class SimpleClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    def create_class_instance():
        return SimpleClass(1, 2)
    
    def create_dict():
        return {"x": 1, "y": 2}
    
    class_time = timeit.timeit(create_class_instance, number=1000000)
    dict_time = timeit.timeit(create_dict, number=1000000)
    
    print(f"Class instance creation time: {class_time:.6f} seconds")
    print(f"Dictionary creation time: {dict_time:.6f} seconds")
    
    class_instance = SimpleClass(1, 2)
    dict_instance = {"x": 1, "y": 2}
    
    print(f"Class instance size: {getsizeof(class_instance)} bytes")
    print(f"Dictionary size: {getsizeof(dict_instance)} bytes")

class OptimizedClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

def demonstrate_slots_optimization():
    """Demonstrate memory optimization using __slots__."""
    regular_class = SimpleClass(1, 2)
    optimized_class = OptimizedClass(1, 2)
    
    print(f"Regular class size: {getsizeof(regular_class)} bytes")
    print(f"Optimized class size: {getsizeof(optimized_class)} bytes")

"""
Performance Considerations:
1. Class instances generally have more overhead than simple data structures like dictionaries.
2. Using `__slots__` can significantly reduce memory usage for classes with a fixed set of attributes.
3. Method lookup in deep inheritance hierarchies can be slower than in shallow ones.
4. Dynamic attribute creation and deletion can impact performance.

Optimization Strategies:
1. Use `__slots__` for classes with many instances or a fixed set of attributes.
2. Consider using `namedtuple` or `dataclasses` for simple data container classes.
3. Profile your code to identify performance bottlenecks related to class and object usage.
4. Be mindful of the depth of inheritance hierarchies and method resolution complexity.

Example of optimizing a frequently instantiated class:
"""

from dataclasses import dataclass

@dataclass
class OptimizedDataClass:
    x: int
    y: int

def demonstrate_dataclass_optimization():
    """Demonstrate optimization using dataclasses."""
    regular_class = SimpleClass(1, 2)
    data_class = OptimizedDataClass(1, 2)
    
    print(f"Regular class size: {getsizeof(regular_class)} bytes")
    print(f"Dataclass size: {getsizeof(data_class)} bytes")
    
    def create_regular_class():
        return SimpleClass(1, 2)
    
    def create_data_class():
        return OptimizedDataClass(1, 2)
    
    regular_time = timeit.timeit(create_regular_class, number=1000000)
    data_time = timeit.timeit(create_data_class, number=1000000)
    
    print(f"Regular class creation time: {regular_time:.6f} seconds")
    print(f"Dataclass creation time: {data_time:.6f} seconds")

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
- Relevance to the main topic of classes and objects in Python OOP.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to classes and objects.
    """
    print("1. Basic Class Usage:")
    demonstrate_basic_class_usage()
    
    print("\n2. Advanced Class Features:")
    demonstrate_advanced_class_features()
    
    print("\n3. Advanced OOP Concepts:")
    demonstrate_advanced_concepts()
    
    print("\n4. Real-World Application (Task Management System):")
    demonstrate_real_world_application()
    
    print("\n5. Advanced Concepts (Data Classes and Pattern Matching):")
    demonstrate_advanced_concepts()
    
    print("\n6. Performance Benchmarking:")
    benchmark_class_vs_dict()
    
    print("\n7. Memory Optimization with __slots__:")
    demonstrate_slots_optimization()
    
    print("\n8. Optimization with Data Classes:")
    demonstrate_dataclass_optimization()

if __name__ == "__main__":
    main()