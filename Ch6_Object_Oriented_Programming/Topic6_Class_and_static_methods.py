"""
Object-Oriented Programming - Class and Static Methods - in the Python Programming Language
===========================================================================================

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
Class and static methods are special types of methods in Python's object-oriented programming model. They provide ways to define methods that are not bound to specific instances of a class, but rather operate on the class itself or function independently of class instances.

Historical context:
- Class methods were introduced in Python 2.2 (2001) along with the new-style classes.
- Static methods have been part of Python since earlier versions but were formalized with the introduction of the @staticmethod decorator in Python 2.4 (2004).
- Both features were inspired by similar concepts in other object-oriented languages like Java and C++.

Significance:
- Class methods provide a way to define methods that operate on the class itself, rather than instances.
- Static methods offer a way to namespace functions within a class without requiring access to the class or instance.
- Both types of methods enhance the organization and readability of code by grouping related functionality within a class.

Common use cases:
- Class methods: Alternative constructors, factory methods, and methods that modify class-level state.
- Static methods: Utility functions related to the class but not dependent on class or instance state.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import time
from typing import List, Any, Type, TypeVar

T = TypeVar('T')

class ExampleClass:
    class_variable = 0
    
    def __init__(self, value: int):
        self.instance_variable = value
    
    @classmethod
    def class_method(cls) -> None:
        """
        A class method that can access and modify class-level state.
        
        Class methods receive the class as an implicit first argument,
        conventionally named 'cls'.
        """
        cls.class_variable += 1
        print(f"Class variable is now: {cls.class_variable}")
    
    @staticmethod
    def static_method(x: int, y: int) -> int:
        """
        A static method that doesn't access class or instance state.
        
        Static methods don't receive any implicit first argument.
        They behave like plain functions but belong to the class's namespace.
        """
        return x + y
    
    @classmethod
    def from_string(cls: Type[T], value: str) -> T:
        """
        An alternative constructor implemented as a class method.
        
        This demonstrates how class methods can be used to create
        factory methods with different creation logic.
        """
        try:
            return cls(int(value))
        except ValueError:
            raise ValueError("Invalid value for ExampleClass")

def demonstrate_basic_usage():
    """Demonstrate basic usage of class and static methods."""
    # Using class method
    ExampleClass.class_method()
    ExampleClass.class_method()
    
    # Using static method
    result = ExampleClass.static_method(3, 4)
    print(f"Static method result: {result}")
    
    # Using alternative constructor
    obj = ExampleClass.from_string("42")
    print(f"Object created with alternative constructor: {obj.instance_variable}")
    
    # Calling methods on an instance (note that this is generally not recommended for class/static methods)
    instance = ExampleClass(10)
    instance.class_method()
    print(f"Static method called on instance: {instance.static_method(5, 6)}")

class ShapeFactory:
    @staticmethod
    def create_square(side_length: float) -> 'Square':
        return Square(side_length)
    
    @staticmethod
    def create_circle(radius: float) -> 'Circle':
        return Circle(radius)

class Shape:
    @staticmethod
    def calculate_area() -> float:
        raise NotImplementedError("Subclasses must implement calculate_area method")

class Square(Shape):
    def __init__(self, side_length: float):
        self.side_length = side_length
    
    @staticmethod
    def calculate_area(side_length: float) -> float:
        return side_length ** 2

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    @staticmethod
    def calculate_area(radius: float) -> float:
        return 3.14159 * radius ** 2

def demonstrate_factory_pattern():
    """Demonstrate the use of static methods in a factory pattern."""
    square = ShapeFactory.create_square(5)
    circle = ShapeFactory.create_circle(3)
    
    print(f"Square area: {Square.calculate_area(square.side_length)}")
    print(f"Circle area: {Circle.calculate_area(circle.radius)}")

class DatabaseConnection:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """
        A class method implementing the singleton pattern.
        
        This ensures only one instance of DatabaseConnection is created.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def query(self, sql: str) -> List[Any]:
        """Simulate a database query."""
        time.sleep(0.1)  # Simulate query execution time
        return [f"Result for: {sql}"]

def demonstrate_singleton_pattern():
    """Demonstrate the use of class methods in a singleton pattern."""
    conn1 = DatabaseConnection.get_instance()
    conn2 = DatabaseConnection.get_instance()
    
    print(f"Are connections the same object? {conn1 is conn2}")
    
    result = conn1.query("SELECT * FROM users")
    print(f"Query result: {result}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use class methods for alternative constructors or methods that need to access or modify class-level state.
2. Use static methods for utility functions that are related to the class but don't need access to class or instance state.
3. Prefer class methods over static methods when the method needs to be inherited and potentially overridden in subclasses.
4. Use clear and descriptive names for class and static methods to indicate their purpose and behavior.

Common Pitfalls:
1. Mistakenly using an instance method when a class or static method would be more appropriate.
2. Forgetting to use the @classmethod or @staticmethod decorator, leading to unexpected behavior.
3. Attempting to access instance variables (self.x) in a class or static method.
4. Overusing class and static methods when regular instance methods would be more appropriate.

Advanced Tips:
1. Use class methods in abstract base classes to create flexible factory methods.
2. Leverage class methods for implementing alternative constructors with different parameters or creation logic.
3. Use static methods to implement utility functions that are conceptually related to the class but don't require class or instance state.
4. Consider using class methods for implementing the Template Method pattern in Python.
"""

from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @classmethod
    @abstractmethod
    def create_product(cls, *args, **kwargs):
        """Abstract factory method to be implemented by subclasses."""
        pass
    
    @classmethod
    def get_product_info(cls) -> str:
        """
        A concrete class method that can be inherited and used by all subclasses.
        
        This demonstrates how class methods can be used in abstract base classes
        to provide shared functionality.
        """
        return f"Product created by {cls.__name__}"

class ConcreteFactory(AbstractFactory):
    @classmethod
    def create_product(cls, product_type: str, *args, **kwargs):
        """Concrete implementation of the factory method."""
        if product_type == "A":
            return ProductA(*args, **kwargs)
        elif product_type == "B":
            return ProductB(*args, **kwargs)
        else:
            raise ValueError("Invalid product type")

class Product(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass

class ProductA(Product):
    def get_info(self) -> str:
        return "This is Product A"

class ProductB(Product):
    def get_info(self) -> str:
        return "This is Product B"

def demonstrate_advanced_usage():
    """Demonstrate advanced usage of class and static methods."""
    product_a = ConcreteFactory.create_product("A")
    print(product_a.get_info())
    print(ConcreteFactory.get_product_info())
    
    product_b = ConcreteFactory.create_product("B")
    print(product_b.get_info())
    print(ConcreteFactory.get_product_info())

"""
4. Integration and Real-World Applications
------------------------------------------
Class and static methods are widely used in various Python libraries and frameworks:

1. Django: Uses class methods in model classes for custom querysets and managers.
2. SQLAlchemy: Employs class methods for query construction and ORM operations.
3. Python's built-in libraries: e.g., `datetime.fromtimestamp()` is a class method.

Real-world example: A simple logging system using class and static methods
"""

import logging
from typing import Dict, Any

class Logger:
    _loggers: Dict[str, 'Logger'] = {}
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
    
    @classmethod
    def get_logger(cls, name: str) -> 'Logger':
        """
        A class method to implement a singleton-like pattern for loggers.
        
        This ensures that only one logger instance is created for each name.
        """
        if name not in cls._loggers:
            cls._loggers[name] = cls(name)
        return cls._loggers[name]
    
    @staticmethod
    def format_message(message: str, **kwargs: Any) -> str:
        """
        A static method to format log messages with additional context.
        
        This demonstrates how static methods can be used for utility functions
        that don't require access to instance or class state.
        """
        context = ' '.join(f"{k}={v}" for k, v in kwargs.items())
        return f"{message} [{context}]"
    
    def info(self, message: str, **kwargs: Any) -> None:
        """Log an info message."""
        formatted_message = self.format_message(message, **kwargs)
        self.logger.info(formatted_message)
    
    def error(self, message: str, **kwargs: Any) -> None:
        """Log an error message."""
        formatted_message = self.format_message(message, **kwargs)
        self.logger.error(formatted_message)

def demonstrate_real_world_application():
    """Demonstrate a real-world application of class and static methods in a logging system."""
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
    
    # Get loggers
    logger1 = Logger.get_logger("app.module1")
    logger2 = Logger.get_logger("app.module2")
    logger3 = Logger.get_logger("app.module1")  # Same as logger1
    
    # Log some messages
    logger1.info("Starting process", process_id=1234)
    logger2.error("An error occurred", error_code=500)
    logger3.info("Process completed", duration=10.5)
    
    # Demonstrate that logger1 and logger3 are the same object
    print(f"logger1 is logger3: {logger1 is logger3}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Metaclasses: Class methods play a crucial role in metaclass implementation, allowing for powerful class customization.
2. Decorators: Class and static methods can be combined with other decorators for advanced functionality.
3. Type hinting: Recent Python versions have improved support for type hinting with class and static methods.
"""

from typing import Tuple

class Meta(type):
    @classmethod
    def __prepare__(mcs, name: str, bases: Tuple[type, ...], **kwargs: Any) -> Dict[str, Any]:
        """
        Prepare the namespace for the class being created.
        
        This method is called before the class body is executed and can be used to
        customize the namespace in which the class body will be evaluated.
        """
        print(f"Preparing namespace for {name}")
        return {"meta_created": True}
    
    def __new__(mcs, name: str, bases: Tuple[type, ...], namespace: Dict[str, Any], **kwargs: Any) -> type:
        """
        Create a new class with the given name, bases, and namespace.
        
        This method allows for customization of the class creation process.
        """
        print(f"Creating class {name}")
        return super().__new__(mcs, name, bases, namespace)
    
    def __init__(cls, name: str, bases: Tuple[type, ...], namespace: Dict[str, Any], **kwargs: Any) -> None:
        """
        Initialize the newly created class.
        
        This method is called after the class has been created and can be used for
        additional initialization or modification of the class.
        """
        print(f"Initializing class {name}")
        super().__init__(name, bases, namespace)

class AdvancedExample(metaclass=Meta):
    @classmethod
    def class_method(cls) -> None:
        print(f"Class method called on {cls.__name__}")
    
    @staticmethod
    def static_method() -> None:
        print("Static method called")

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts related to class and static methods."""
    obj = AdvancedExample()
    obj.class_method()
    obj.static_method()
    print(f"meta_created attribute: {getattr(AdvancedExample, 'meta_created', False)}")

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use a static method instead of a standalone function?
A: Use a static method when the function is conceptually related to the class but doesn't need access to class or instance state. This helps with organization and namespace management.

Q: Can I call a class method on an instance?
A: Yes, you can call a class method on an instance, but it's generally not recommended as it can lead to confusion. The instance is ignored, and the class is passed as the first argument.

Q: How do I override a static method in a subclass?
A: You can override a static method in a subclass by defining a new method with the same name and using the @staticmethod decorator. However, note that static methods don't have the same polymorphic behavior as instance methods.

Troubleshooting:
1. If a class method is not receiving the class as the first argument, ensure you've used the @classmethod decorator.
2. If a static method is raising a TypeError about missing arguments, make sure you've used the @staticmethod decorator.
3. For unexpected behavior in inherited class methods, check the method resolution order (MRO) using ClassName.__mro__.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
- mypy: A static type checker that can help catch errors related to class and static methods.
- pylint: A linter that can identify potential issues with class and static method usage.
- attrs: A library that can automatically generate special methods, including class methods.


Resources:
- "Fluent Python" by Luciano Ramalho
- "Python Cookbook" by David Beazley and Brian K. Jones
- Python's official documentation on class and static methods: https://docs.python.org/3/library/functions.html#classmethod
- Real Python's guide on class and static methods: https://realpython.com/instance-class-and-static-methods-demystified/
- PEP 3115 - Metaclasses in Python 3: https://www.python.org/dev/peps/pep-3115/

8. Performance Analysis and Optimization
----------------------------------------
When working with class and static methods, it's important to consider their performance implications, especially in performance-critical applications.
"""

import timeit

def benchmark_method_types():
    """Benchmark the performance difference between instance, class, and static methods."""
    class MethodTest:
        def instance_method(self):
            pass
        
        @classmethod
        def class_method(cls):
            pass
        
        @staticmethod
        def static_method():
            pass
    
    obj = MethodTest()
    
    def call_instance_method():
        obj.instance_method()
    
    def call_class_method():
        MethodTest.class_method()
    
    def call_static_method():
        MethodTest.static_method()
    
    instance_time = timeit.timeit(call_instance_method, number=1000000)
    class_time = timeit.timeit(call_class_method, number=1000000)
    static_time = timeit.timeit(call_static_method, number=1000000)
    
    print(f"Instance method time: {instance_time:.6f} seconds")
    print(f"Class method time: {class_time:.6f} seconds")
    print(f"Static method time: {static_time:.6f} seconds")

"""
Performance Considerations:
1. Static methods are generally the fastest, as they don't require any binding to the class or instance.
2. Class methods are slightly slower than static methods due to the implicit passing of the class as the first argument.
3. Instance methods are typically the slowest of the three, as they require binding to the instance.

Optimization Strategies:
1. Use static methods for utility functions that don't need access to class or instance state.
2. Consider using class methods instead of instance methods for operations that only require class-level data.
3. Be mindful of the performance impact when choosing between class and static methods, especially in tight loops or frequently called code.

Example of optimizing a frequently called method:
"""

class OptimizedCounter:
    _count = 0
    
    @classmethod
    def increment(cls):
        cls._count += 1
    
    @staticmethod
    def get_count():
        return OptimizedCounter._count

def demonstrate_optimized_counter():
    """Demonstrate an optimized counter using class and static methods."""
    for _ in range(1000000):
        OptimizedCounter.increment()
    
    print(f"Final count: {OptimizedCounter.get_count()}")

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
- Relevance to the main topic of class and static methods in Python OOP.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to class and static methods.
    """
    print("1. Basic Usage of Class and Static Methods:")
    demonstrate_basic_usage()
    
    print("\n2. Factory Pattern with Static Methods:")
    demonstrate_factory_pattern()
    
    print("\n3. Singleton Pattern with Class Methods:")
    demonstrate_singleton_pattern()
    
    print("\n4. Advanced Usage in Abstract Base Classes:")
    demonstrate_advanced_usage()
    
    print("\n5. Real-World Application (Logging System):")
    demonstrate_real_world_application()
    
    print("\n6. Advanced Concepts (Metaclasses):")
    demonstrate_advanced_concepts()
    
    print("\n7. Performance Benchmarking:")
    benchmark_method_types()
    
    print("\n8. Optimized Counter Example:")
    demonstrate_optimized_counter()

if __name__ == "__main__":
    main()