# Python Cheat Sheet: Object-Oriented Programming

# 1. Classes and Objects

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # String representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Representation (for developers)
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())  # Output: Buddy says Woof!
print(dog2)  # Output: Max is 5 years old
print(Dog.species)  # Output: Canis familiaris

# Tip: Use __init__ for initialization, not for complex object setup

# 2. Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

cat = Cat("Whiskers")
dog = Dog("Rex")

print(cat.speak())  # Output: Whiskers says Meow!
print(dog.speak())  # Output: Rex says Woof!

# Tip: Use inheritance to create a hierarchy of related classes

# 3. Multiple Inheritance

class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(duck.speak())  # Output: Donald says Quack!
print(duck.fly())    # Output: I can fly!
print(duck.swim())   # Output: I can swim!

# Tip: Be cautious with multiple inheritance, as it can lead to complex hierarchies

# 4. Method Resolution Order (MRO)

print(Duck.__mro__)
# Output: (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.Flyable'>, 
#          <class '__main__.Swimmable'>, <class 'object'>)

# Tip: Understand MRO to predict method resolution in complex inheritance hierarchies

# 5. Encapsulation

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Tip: Use single underscore for protected attributes and double for private

# 6. Properties

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # Output: 25
print(temp.fahrenheit)  # Output: 77.0
temp.fahrenheit = 86
print(temp.celsius)     # Output: 30.0

# Tip: Use properties for computed attributes and to add behavior to attribute access

# 7. Class and Static Methods

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return cls.add(x, 0) * y  # Using the static method

print(MathOperations.add(5, 3))       # Output: 8
print(MathOperations.multiply(4, 3))  # Output: 12

# Tip: Use static methods for utility functions, and class methods for alternative constructors

# 8. Abstract Base Classes

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # This would raise TypeError
rect = Rectangle(5, 3)
print(rect.area())      # Output: 15
print(rect.perimeter()) # Output: 16

# Tip: Use abstract base classes to define interfaces and ensure derived classes implement required methods

# 9. Method Overriding and Super()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy barks

# Tip: Use super() to call methods from the parent class and avoid duplicate code

# 10. Composition

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return f"Car starting: {self.engine.start()}"

car = Car()
print(car.start())  # Output: Car starting: Engine started

# Tip: Prefer composition over inheritance for more flexible and maintainable code

# 11. Mixins

class SerializeMixin:
    def serialize(self):
        return json.dumps(self.__dict__)

class Person(SerializeMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.serialize())  # Output: {"name": "Alice", "age": 30}

# Tip: Use mixins to add behaviors to classes without full inheritance

# 12. Dataclasses (Python 3.7+)

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(3, 4)
print(p)  # Output: Point(x=3, y=4)
print(p.distance_from_origin())  # Output: 5.0

# Tip: Use dataclasses for creating simple classes with automatic __init__, __repr__, etc.

# 13. Type Hints in Classes (Python 3.5+)

from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add_item(self, item: str) -> None:
        self.items.append(item)

    def get_items(self) -> List[str]:
        return self.items

cart = ShoppingCart()
cart.add_item("Apple")
print(cart.get_items())  # Output: ['Apple']

# Tip: Use type hints to improve code readability and enable better tooling support

# 14. Descriptors

class Positive:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Value must be positive")
        obj.__dict__[self.name] = value

class Product:
    price = Positive()
    quantity = Positive()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product = Product("Apple", 0.5, 10)
# product.price = -1  # This would raise ValueError

# Tip: Use descriptors for reusable property-like behaviors across multiple classes

# 15. Context Managers

class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")

    def query(self, sql):
        print(f"Executing SQL: {sql}")

with DatabaseConnection() as db:
    db.query("SELECT * FROM users")

# Tip: Use context managers for resource management and cleanup

# 16. Metaclasses

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

# Tip: Use metaclasses sparingly, as they can make code harder to understand

# 17. Best Practices and Tips

# 1. Follow the Single Responsibility Principle: Each class should have one, and only one, reason to change.
# 2. Use inheritance sparingly; prefer composition when possible.
# 3. Keep your classes small and focused.
# 4. Use properties instead of getter and setter methods.
# 5. Use abstract base classes to define interfaces.
# 6. Understand and use method resolution order (MRO) in multiple inheritance.
# 7. Use staticmethod and classmethod decorators appropriately.
# 8. Leverage dataclasses for simple data structures.
# 9. Use type hints to improve code readability and maintainability.
# 10. Implement special methods (__str__, __repr__, etc.) for better object representation.
# 11. Use context managers for resource management.
# 12. Be cautious with multiple inheritance and understand its implications.
# 13. Use descriptors for reusable attribute management.
# 14. Understand the difference between class and instance attributes.
# 15. Use metaclasses judiciously, as they can add significant complexity.

# This concludes the enhanced detailed Python Cheat Sheet for Object-Oriented Programming