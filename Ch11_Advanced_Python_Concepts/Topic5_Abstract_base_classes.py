"""
Advanced Python Concepts - Abstract Base Classes - in the Python Programming Language
=====================================================================================

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
Abstract Base Classes (ABCs) in Python provide a way to define interfaces or abstract types that other classes can implement. They allow for the creation of hierarchies of classes with shared behavior without implementing that behavior in the base class.

Historical context:
- ABCs were introduced in Python 2.6 and 3.0 (2008) as part of PEP 3119.
- The abc module was added to provide infrastructure for defining ABCs.
- This feature was inspired by similar concepts in languages like Java and C++.

Significance:
- ABCs enable the creation of well-defined interfaces in Python.
- They provide a way to ensure that derived classes implement particular methods.
- ABCs support duck typing while still allowing for compile-time type checking.

Common use cases:
- Defining interfaces for plugins or frameworks.
- Ensuring a set of classes adhere to a common interface.
- Creating base classes for collections or other abstract data types.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from abc import ABC, abstractmethod
import collections.abc
from typing import List, Any, Dict

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        """
        An abstract method that must be implemented by all subclasses.
        
        Returns:
            str: The sound the animal makes.
        """
        pass
    
    @abstractmethod
    def move(self) -> None:
        """
        An abstract method representing the animal's movement.
        """
        pass
    
    def breathe(self) -> None:
        """
        A concrete method that can be inherited by subclasses.
        """
        print("Inhale... Exhale...")

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"
    
    def move(self) -> None:
        print("Running on four legs")

class Fish(Animal):
    def speak(self) -> str:
        return "Blub!"
    
    def move(self) -> None:
        print("Swimming")

def demonstrate_basic_usage():
    """Demonstrate basic usage of Abstract Base Classes."""
    # Uncommenting the following line would raise a TypeError
    # animal = Animal()
    
    dog = Dog()
    fish = Fish()
    
    print(f"Dog says: {dog.speak()}")
    dog.move()
    dog.breathe()
    
    print(f"Fish says: {fish.speak()}")
    fish.move()
    fish.breathe()

class CustomList(collections.abc.MutableSequence):
    def __init__(self, data: List[Any] = None):
        """Initialize the custom list."""
        self._data = data or []
    
    def __getitem__(self, index: int) -> Any:
        """Get an item at a specific index."""
        return self._data[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        """Set an item at a specific index."""
        self._data[index] = value
    
    def __delitem__(self, index: int) -> None:
        """Delete an item at a specific index."""
        del self._data[index]
    
    def __len__(self) -> int:
        """Return the length of the list."""
        return len(self._data)
    
    def insert(self, index: int, value: Any) -> None:
        """Insert a value at a specific index."""
        self._data.insert(index, value)

def demonstrate_abc_collections():
    """Demonstrate the use of ABCs from the collections module."""
    custom_list = CustomList([1, 2, 3, 4, 5])
    print(f"Original list: {custom_list}")
    custom_list.append(6)
    print(f"After append: {custom_list}")
    custom_list.reverse()
    print(f"After reverse: {custom_list}")
    
    # Demonstrate that CustomList is recognized as a MutableSequence
    print(f"Is CustomList a MutableSequence? {isinstance(custom_list, collections.abc.MutableSequence)}")

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        Process the given data.
        
        Args:
            data (Any): The data to process.
        
        Returns:
            Any: The processed data.
        """
        pass
    
    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        Get the name of the processor.
        
        Returns:
            str: The name of the processor.
        """
        pass

class NumberSquarer(DataProcessor):
    @classmethod
    def get_name(cls) -> str:
        return "NumberSquarer"
    
    def process(self, data: int) -> int:
        return data ** 2

class StringReverser(DataProcessor):
    @classmethod
    def get_name(cls) -> str:
        return "StringReverser"
    
    def process(self, data: str) -> str:
        return data[::-1]

def demonstrate_abstract_class_methods():
    """Demonstrate the use of abstract class methods."""
    processors: Dict[str, DataProcessor] = {
        NumberSquarer.get_name(): NumberSquarer(),
        StringReverser.get_name(): StringReverser()
    }
    
    print(f"Square of 5: {processors['NumberSquarer'].process(5)}")
    print(f"Reverse of 'hello': {processors['StringReverser'].process('hello')}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use ABCs to define interfaces when you want to ensure certain methods are implemented.
2. Combine ABCs with isinstance() checks for runtime type checking.
3. Use abstract properties to define required attributes in subclasses.
4. Implement ABCs for your own abstract types to make them compatible with isinstance() and issubclass().

Common Pitfalls:
1. Forgetting to inherit from ABC when creating an abstract base class.
2. Not implementing all abstract methods in a concrete subclass.
3. Overusing ABCs when simple inheritance or duck typing would suffice.
4. Attempting to instantiate an abstract base class directly.

Advanced Tips:
1. Use @abstractmethod in combination with other method decorators.
2. Leverage ABC metaclasses for more complex abstract base class behavior.
3. Use abstract base classes to define both synchronous and asynchronous interfaces.
4. Implement __subclasshook__() for custom subclass checks.
"""

from abc import ABC, abstractmethod, ABCMeta

class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    @property
    def area(self) -> float:
        return 3.14159 * self.radius ** 2

class AbstractContextManager(ABC):
    @abstractmethod
    def __enter__(self):
        """Enter the runtime context."""
        pass
    
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the runtime context."""
        pass

class MyContextManager(AbstractContextManager):
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        return False  # Propagate exceptions

class VirtualSubclassMeta(ABCMeta):
    def __subclasscheck__(cls, subclass):
        return hasattr(subclass, 'my_abstract_method')

class VirtualBaseClass(metaclass=VirtualSubclassMeta):
    @abstractmethod
    def my_abstract_method(self):
        pass

class VirtualSubclass:
    def my_abstract_method(self):
        print("Virtual subclass method")

def demonstrate_advanced_concepts():
    """Demonstrate advanced concepts with ABCs."""
    # Abstract properties
    circle = Circle(5)
    print(f"Circle area: {circle.area}")
    
    # Abstract context manager
    with MyContextManager() as cm:
        print("Inside context")
    
    # Virtual subclasses
    print(f"Is VirtualSubclass a subclass of VirtualBaseClass? {issubclass(VirtualSubclass, VirtualBaseClass)}")
    print(f"Is VirtualSubclass instance a VirtualBaseClass? {isinstance(VirtualSubclass(), VirtualBaseClass)}")

"""
4. Integration and Real-World Applications
------------------------------------------
ABCs are widely used in various Python libraries and frameworks:

1. collections.abc: Provides ABCs for containers and iterators.
2. asyncio: Uses ABCs to define protocols for asynchronous programming.
3. typing: Leverages ABCs for runtime type checking and static type hinting.

Real-world example: A plugin system using ABCs
"""

import pkgutil
import importlib
from typing import List, Type

class Plugin(ABC):
    @abstractmethod
    def activate(self):
        """Activate the plugin."""
        pass
    
    @abstractmethod
    def deactivate(self):
        """Deactivate the plugin."""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Get the name of the plugin."""
        pass

class PluginManager:
    def __init__(self):
        self.plugins: List[Plugin] = []
    
    def load_plugins(self, package_name: str):
        """Load all plugins from a given package."""
        package = importlib.import_module(package_name)
        for _, name, is_pkg in pkgutil.iter_modules(package.__path__):
            if not is_pkg:
                module = importlib.import_module(f'{package_name}.{name}')
                for item_name in dir(module):
                    item = getattr(module, item_name)
                    if isinstance(item, type) and issubclass(item, Plugin) and item is not Plugin:
                        self.plugins.append(item())
    
    def activate_all(self):
        """Activate all loaded plugins."""
        for plugin in self.plugins:
            plugin.activate()
    
    def deactivate_all(self):
        """Deactivate all loaded plugins."""
        for plugin in self.plugins:
            plugin.deactivate()

# Example plugins (in real-world scenarios, these would be in separate files)
class LoggingPlugin(Plugin):
    @property
    def name(self) -> str:
        return "LoggingPlugin"
    
    def activate(self):
        print(f"Activating {self.name}")
    
    def deactivate(self):
        print(f"Deactivating {self.name}")

class SecurityPlugin(Plugin):
    @property
    def name(self) -> str:
        return "SecurityPlugin"
    
    def activate(self):
        print(f"Activating {self.name}")
    
    def deactivate(self):
        print(f"Deactivating {self.name}")

def demonstrate_plugin_system():
    """Demonstrate a real-world application of ABCs in a plugin system."""
    # In a real scenario, we would load plugins from a directory
    # For this example, we'll manually add our example plugins
    manager = PluginManager()
    manager.plugins = [LoggingPlugin(), SecurityPlugin()]
    
    manager.activate_all()
    print("Plugins are active...")
    manager.deactivate_all()

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Protocol classes: Introduced in Python 3.8, these provide a way to define structural subtyping (similar to Go interfaces).
2. Generics with ABCs: Combining ABCs with generics for more precise type hinting.
3. Runtime checkable protocols: Allowing isinstance() checks for protocol classes.
"""

from typing import Protocol, runtime_checkable, TypeVar, Generic

T = TypeVar('T')

@runtime_checkable
class Printable(Protocol):
    def __str__(self) -> str:
        ...

class Pair(Generic[T]):
    def __init__(self, first: T, second: T):
        self.first = first
        self.second = second

class Point(Pair[float]):
    def __str__(self) -> str:
        return f"Point({self.first}, {self.second})"

def print_if_printable(obj: Any) -> None:
    if isinstance(obj, Printable):
        print(str(obj))
    else:
        print("Object is not printable")

def demonstrate_advanced_typing():
    """Demonstrate advanced typing concepts with ABCs."""
    point = Point(3.14, 2.71)
    print_if_printable(point)
    print_if_printable(42)  # Not Printable

"""
6. FAQs and Troubleshooting
---------------------------
Q: When should I use an ABC instead of a regular base class?
A: Use an ABC when you want to define an interface that must be implemented by subclasses, without providing a default implementation. ABCs are particularly useful when you want to enforce a contract for subclasses.

Q: Can I instantiate an ABC?
A: No, ABCs are designed to be subclassed, not instantiated directly. Attempting to instantiate an ABC will raise a TypeError.

Q: How do I create an ABC that can be used with isinstance() checks?
A: Inherit from abc.ABC and use the @abstractmethod decorator for methods that must be implemented by subclasses. This will make your ABC compatible with isinstance() checks.

Troubleshooting:
1. Issue: TypeError when instantiating a class
   Solution: Ensure all abstract methods are implemented in the concrete class.

2. Issue: Abstract method not recognized
   Solution: Make sure you're using the @abstractmethod decorator and that the ABC inherits from abc.ABC.

3. Issue: isinstance() check failing unexpectedly
   Solution: Verify that the class correctly inherits from the ABC and implements all required methods.
"""

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. mypy: Static type checker that works well with ABCs and Protocol classes.
2. pylint: Linter that can help identify issues with ABC implementations.
3. abc module: Built-in module for working with ABCs.
4. typing module: Provides support for type hints, including those involving ABCs.

Resources:
- "Fluent Python" by Luciano Ramalho (O'Reilly)
- "Python Cookbook" by David Beazley and Brian K. Jones (O'Reilly)
- PEP 3119 - Introducing Abstract Base Classes: https://www.python.org/dev/peps/pep-3119/
- Python's official documentation on ABCs: https://docs.python.org/3/library/abc.html
- Real Python's guide on Abstract Base Classes: https://realpython.com/python-interface/

8. Performance Analysis and Optimization
----------------------------------------
When working with ABCs, it's important to consider their performance implications, especially in performance-critical applications.
"""

import timeit

def performance_comparison():
    """Compare the performance of ABCs vs. regular classes."""
    
    class RegularBase:
        def method(self):
            pass
    
    class RegularDerived(RegularBase):
        def method(self):
            pass
    
    class AbstractBase(ABC):
        @abstractmethod
        def method(self):
            pass

    class AbstractDerived(AbstractBase):
        def method(self):
            pass
    
    def use_regular():
        obj = RegularDerived()
        obj.method()
    
    def use_abstract():
        obj = AbstractDerived()
        obj.method()
    
    regular_time = timeit.timeit(use_regular, number=1000000)
    abstract_time = timeit.timeit(use_abstract, number=1000000)
    
    print(f"Regular class time: {regular_time:.6f} seconds")
    print(f"Abstract class time: {abstract_time:.6f} seconds")
    print(f"Overhead of ABC: {(abstract_time - regular_time) / regular_time * 100:.2f}%")

"""
Performance Considerations:
1. Method Resolution: ABCs can introduce a slight overhead in method resolution due to the abstract method checks.
2. Instantiation: ABCs perform additional checks during instantiation to ensure all abstract methods are implemented.
3. isinstance() and issubclass() checks: These operations might be slightly slower with ABCs, especially with complex hierarchies.

Optimization Strategies:
1. Use ABCs judiciously: Only use them when the benefits of interface enforcement outweigh the minor performance cost.
2. Minimize deep inheritance hierarchies: Flatter hierarchies can reduce method resolution time.
3. Cache isinstance() and issubclass() results when used frequently.
4. Use __slots__ in concrete classes to reduce memory usage and slightly improve attribute access time.
"""

class OptimizedAbstractBase(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class OptimizedConcrete(OptimizedAbstractBase):
    __slots__ = ('_value',)
    
    def __init__(self, value):
        self._value = value
    
    def abstract_method(self):
        return self._value * 2

def demonstrate_optimized_abc():
    """Demonstrate an optimized concrete class derived from an ABC."""
    obj = OptimizedConcrete(21)
    result = obj.abstract_method()
    print(f"Optimized result: {result}")

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
- Relevance to the main topic of Abstract Base Classes in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to Abstract Base Classes.
    """
    print("Basic usage of Abstract Base Classes:")
    demonstrate_basic_usage()
    
    print("\nUsage of ABCs from collections module:")
    demonstrate_abc_collections()
    
    print("\nDemonstrating abstract class methods:")
    demonstrate_abstract_class_methods()
    
    print("\nAdvanced concepts with ABCs:")
    demonstrate_advanced_concepts()
    
    print("\nReal-world application: Plugin system using ABCs:")
    demonstrate_plugin_system()
    
    print("\nAdvanced typing with ABCs and Protocols:")
    demonstrate_advanced_typing()
    
    print("\nPerformance comparison of ABCs vs regular classes:")
    performance_comparison()
    
    print("\nDemonstrating optimized ABC usage:")
    demonstrate_optimized_abc()

if __name__ == "__main__":
    main()