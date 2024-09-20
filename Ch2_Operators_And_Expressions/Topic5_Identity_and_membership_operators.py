"""
Operators and Expressions - Identity and membership operators - in the Python Programming Language
==================================================================================================

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
==================================
Identity and membership operators in Python are essential tools for comparing 
objects and checking for the presence of elements in collections. These 
operators provide a way to perform specific types of comparisons that are 
fundamental to many programming tasks.

Identity Operators:
- 'is': Returns True if both operands refer to the same object in memory.
- 'is not': Returns True if both operands refer to different objects in memory.

Membership Operators:
- 'in': Returns True if the specified value is found in the sequence.
- 'not in': Returns True if the specified value is not found in the sequence.

Historical context:
- Identity operators have been part of Python since its early versions, 
  reflecting the language's object-oriented nature and focus on identity 
  comparison.
- Membership operators were introduced to provide a concise and readable way to 
  check for the presence of elements in collections, aligning with Python's 
  emphasis on clear and expressive code.

Relevance in modern software development:
- Identity operators are crucial for understanding object references and 
  managing memory efficiently.
- Membership operators simplify data structure operations and enhance code 
  readability, particularly when working with large datasets or complex 
  data structures.

Comparison to other languages:
- Python's 'is' operator is similar to '===' in JavaScript or 'ReferenceEquals' 
  in C#, but with some unique behaviors due to Python's object model.
- Membership operators are relatively unique to Python, though similar 
  functionality exists in other languages through methods or functions 
  (e.g., 'includes' in JavaScript arrays).

2. Syntax, Key Concepts, and Code Examples
==========================================
Let's explore each of these operators with examples:
"""

import sys
import time
import asyncio
from typing import List, Any

def identity_operators_demo():
    """
    Demonstrates the usage of identity operators 'is' and 'is not'.
    """
    # Basic usage
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(f"a is b: {a is b}")  # False: different objects with same value
    print(f"a is c: {a is c}")  # True: same object
    print(f"a is not b: {a is not b}")  # True: different objects

    # Identity vs Equality
    x = 1000
    y = 1000
    print(f"x == y: {x == y}")  # True: same value
    print(f"x is y: {x is y}")  # False: different objects

    # Special case: small integers
    small_x = 5
    small_y = 5
    print(f"small_x is small_y: {small_x is small_y}")  # True: integer interning

    # None comparison
    def func():
        pass

    print(f"func() is None: {func() is None}")  # True: function returns None by default

def membership_operators_demo():
    """
    Demonstrates the usage of membership operators 'in' and 'not in'.
    """
    # List membership
    fruits = ['apple', 'banana', 'cherry']
    print(f"'banana' in fruits: {'banana' in fruits}")  # True
    print(f"'orange' not in fruits: {'orange' not in fruits}")  # True

    # String membership
    text = "Hello, World!"
    print(f"'o' in text: {'o' in text}")  # True
    print(f"'x' not in text: {'x' not in text}")  # True

    # Dictionary membership (checks keys)
    person = {'name': 'Alice', 'age': 30}
    print(f"'name' in person: {'name' in person}")  # True
    print(f"'gender' not in person: {'gender' not in person}")  # True

    # Set membership
    numbers = {1, 2, 3, 4, 5}
    print(f"3 in numbers: {3 in numbers}")  # True
    print(f"6 not in numbers: {6 not in numbers}")  # True

def advanced_identity_comparison():
    """
    Demonstrates advanced concepts related to identity comparison.
    """
    # Custom class with __eq__ method
    class CustomObject:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    obj1 = CustomObject(5)
    obj2 = CustomObject(5)
    obj3 = obj1

    print(f"obj1 == obj2: {obj1 == obj2}")  # True: same value
    print(f"obj1 is obj2: {obj1 is obj2}")  # False: different objects
    print(f"obj1 is obj3: {obj1 is obj3}")  # True: same object

    # Identity comparison with mutable default arguments
    def append_to_list(item, lst=[]):
        lst.append(item)
        return lst

    list1 = append_to_list(1)
    list2 = append_to_list(2)
    print(f"list1: {list1}")  # [1, 2]
    print(f"list2: {list2}")  # [1, 2]
    print(f"list1 is list2: {list1 is list2}")  # True: same default list object

def advanced_membership_operations():
    """
    Demonstrates advanced concepts related to membership operations.
    """
    # Custom class with __contains__ method
    class CustomContainer:
        def __init__(self, data):
            self.data = data

        def __contains__(self, item):
            return item in self.data

    container = CustomContainer([1, 2, 3, 4, 5])
    print(f"3 in container: {3 in container}")  # True
    print(f"6 not in container: {6 not in container}")  # True

    # Membership check in a large dataset
    large_set = set(range(1000000))
    start_time = time.time()
    result = 999999 in large_set
    end_time = time.time()
    print(f"Membership check in large set: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    # Membership check with generator expression
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

    primes = (x for x in range(2, 100) if is_prime(x))
    print(f"17 is in primes: {17 in primes}")  # True
    print(f"18 is not in primes: {18 not in primes}")  # True, but exhausts the generator

async def async_membership_check(items: List[Any], target: Any) -> bool:
    """
    Demonstrates an asynchronous membership check.
    """
    for item in items:
        await asyncio.sleep(0.01)  # Simulate an asynchronous operation
        if item == target:
            return True
    return False

async def async_membership_demo():
    """
    Demonstrates asynchronous usage of membership operations.
    """
    items = list(range(1000))
    target = 750

    print("Starting asynchronous membership check...")
    result = await async_membership_check(items, target)
    print(f"Async membership check result: {result}")

def main():
    print("Identity and Membership Operators in Python - Expert-Level Note Sheet")
    print("=====================================================================")

    identity_operators_demo()
    print("\n" + "="*50 + "\n")

    membership_operators_demo()
    print("\n" + "="*50 + "\n")

    advanced_identity_comparison()
    print("\n" + "="*50 + "\n")

    advanced_membership_operations()
    print("\n" + "="*50 + "\n")

    # Run async demo
    asyncio.run(async_membership_demo())

    print("\n" + "="*50 + "\n")
    print("Performance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
=====================================================

Best Practices:
1. Use 'is' for comparing with None, True, and False.
2. Prefer '==' for value comparison unless object identity is specifically required.
3. Use membership operators for readable and efficient element checks in collections.
4. Be aware of the performance implications of membership checks in different data structures.

Common Pitfalls:
1. Misusing 'is' for value comparison, especially with integers and strings.
2. Overlooking the behavior of 'is' with string and integer interning.
3. Assuming that 'in' always checks for exact matches (e.g., with floating-point numbers).
4. Using membership operators on unhashable types in sets or as dictionary keys.

Advanced Tips:
1. Understand the implications of object interning in Python:
"""

def object_interning_demo():
    # Integer interning
    a = 256
    b = 256
    print(f"a is b for 256: {a is b}")  # True

    c = 257
    d = 257
    print(f"c is d for 257: {c is d}")  # False (may be True in some Python implementations)

    # String interning
    s1 = "hello"
    s2 = "hello"
    print(f"s1 is s2: {s1 is s2}")  # True

    s3 = "hello world"
    s4 = "hello world"
    print(f"s3 is s4: {s3 is s4}")  # May be True or False depending on implementation

"""
2. Use custom __eq__ and __hash__ methods for class identity and membership operations:
"""

class CustomHashable:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, CustomHashable) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

def custom_hashable_demo():
    a = CustomHashable(5)
    b = CustomHashable(5)
    c = CustomHashable(6)

    print(f"a == b: {a == b}")  # True
    print(f"a is b: {a is b}")  # False
    print(f"hash(a) == hash(b): {hash(a) == hash(b)}")  # True

    s = {a, b, c}
    print(f"Length of set s: {len(s)}")  # 2

"""
3. Optimize membership checks for large datasets:
"""

def optimize_membership_checks():
    large_list = list(range(1000000))
    large_set = set(large_list)

    start = time.time()
    999999 in large_list
    list_time = time.time() - start

    start = time.time()
    999999 in large_set
    set_time = time.time() - start

    print(f"Time for list membership: {list_time:.6f} seconds")
    print(f"Time for set membership: {set_time:.6f} seconds")

"""
4. Use identity checks for sentinel values in algorithms:
"""

def find_sentinel(lst, sentinel):
    for item in lst:
        if item is sentinel:
            return True
    return False

"""
4. Integration and Real-World Applications
==========================================
Identity and membership operators are widely used in various real-world applications:

1. Caching and Memoization:
   - Using identity checks to compare complex objects in cache systems.
   - Implementing memoization techniques for optimizing recursive algorithms.

2. Data Structures and Algorithms:
   - Implementing efficient search algorithms using membership checks.
   - Optimizing graph traversal algorithms with visited node checks.

3. Configuration Management:
   - Checking for the presence of configuration options using membership operators.
   - Using identity checks for singleton configuration objects.

4. Security and Authentication:
   - Implementing role-based access control using membership checks.
   - Using identity checks for secure token comparison.

5. Database Operations:
   - Optimizing database queries by checking membership in sets before querying.
   - Implementing caching mechanisms using identity checks for database connections.

Example: Role-based access control
"""

class User:
    def __init__(self, name, roles):
        self.name = name
        self.roles = set(roles)

def has_permission(user, required_role):
    return required_role in user.roles

def perform_admin_action(user):
    if has_permission(user, 'admin'):
        print(f"User {user.name} performed admin action")
    else:
        print(f"User {user.name} does not have admin permission")

"""
5. Advanced Concepts and Emerging Trends
========================================
1. Identity Preservation in Serialization:
   - Ensuring object identity is maintained when serializing and deserializing complex object graphs.

2. Memory Management and Weak References:
   - Using identity checks in conjunction with weak references for advanced memory management techniques.

3. Metaclasses and Identity:
   - Exploring how metaclasses can affect identity comparisons and membership checks.

4. Quantum Computing and Identity:
   - Investigating how classical concepts of identity and membership translate to quantum computing paradigms.

5. Machine Learning Model Comparison:
   - Using identity checks for efficient model comparison in ensemble learning techniques.

Example: Identity preservation in serialization
"""

import pickle

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_circular_reference():
    a = Node(1)
    b = Node(2)
    a.next = b
    b.next = a
    return a

def serialize_and_check_identity():
    original = create_circular_reference()
    serialized = pickle.dumps(original)
    deserialized = pickle.loads(serialized)

    print(f"Original object: {original}")
    print(f"Deserialized object: {deserialized}")
    print(f"Identity preserved: {original is deserialized}")  # False
    print(f"Circular reference preserved: {deserialized.next.next is deserialized}")  # True

"""
6. FAQs and Troubleshooting
===========================
Q: Why does 'is' sometimes give unexpected results with integers?
A: Python interns small integers (usually -5 to 256) for efficiency. Larger integers may or may not be interned, leading to inconsistent behavior with 'is'.

Q: How can I efficiently check for membership in a large dataset?
A: Use sets for O(1) average case lookup time. For very large datasets, consider using specialized data structures like Bloom filters.

Q: Is it safe to use 'is' for string comparison?
A: Generally, no. Use '==' for string comparison unless you specifically need to check for object identity. String interning in Python can lead to unexpected results with 'is'.

Troubleshooting:

1. Inconsistent behavior with 'is' for integers:
"""

def troubleshoot_integer_identity():
    a = 256
    b = 256
    c = 257
    d = 257
    print(f"256: a is b = {a is b}")  # True
    print(f"257: c is d = {c is d}")  # Might be True or False

    # Solution: Use equality operator for value comparison
    print(f"256: a == b = {a == b}")  # True
    print(f"257: c == d = {c == d}")  # True

"""
2. Unexpected membership check results with floating-point numbers:
"""

def troubleshoot_float_membership():
    numbers = {0.1, 0.2, 0.3}
    check = 0.1 + 0.2
    print(f"0.1 + 0.2 = {check}")
    print(f"0.3 in numbers: {0.3 in numbers}")  # True
    print(f"check in numbers: {check in numbers}")  # Might be False

    # Solution: Use approximate equality for floating-point comparisons
    def approx_equal(a, b, tolerance=1e-9):
        return abs(a - b) < tolerance

    print(f"Approximate equality check: {any(approx_equal(check, x) for x in numbers)}")

"""
3. Memory leaks with default mutable arguments:
"""

def troubleshoot_mutable_defaults(item, lst=[]):
    lst.append(item)
    return lst

def fix_mutable_defaults(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

def demonstrate_mutable_default_issue():
    print("Problematic function:")
    print(troubleshoot_mutable_defaults(1))  # [1]
    print(troubleshoot_mutable_defaults(2))  # [1, 2]
    
    print("\nFixed function:")
    print(fix_mutable_defaults(1))  # [1]
    print(fix_mutable_defaults(2))  # [2]

"""
7. Recommended Tools, Libraries, and Resources
==============================================
Tools and Libraries:
1. dis module: For disassembling Python bytecode to understand how identity and membership operators are implemented.
   (https://docs.python.org/3/library/dis.html)
2. objgraph: For visualizing Python object graphs, useful for understanding object identity.
   (https://mg.pov.lt/objgraph/)
3. Python Tutor: For visualizing code execution and object references.
   (http://pythontutor.com/)
4. pyuca: For proper Unicode collation, which can affect string comparisons and membership checks.
   (https://pypi.org/project/pyuca/)

Resources:
1. Python Language Reference on Comparisons:
   https://docs.python.org/3/reference/expressions.html#comparisons
2. "Fluent Python" by Luciano Ramalho (Book)
3. "Effective Python: 90 Specific Ways to Write Better Python" by Brett Slatkin (Book)
4. PEP 8 -- Style Guide for Python Code:
   https://www.python.org/dev/peps/pep-0008/

8. Performance Analysis and Optimization
========================================
Let's analyze the performance of identity and membership operators:
"""

import timeit
import random

def performance_analysis():
    # Setup
    lst = list(range(10000))
    set_version = set(lst)
    dict_version = dict.fromkeys(lst)
    
    # Identity check vs Equality check
    id_check = timeit.timeit("a is b", setup="a = b = object()")
    eq_check = timeit.timeit("a == b", setup="a = b = object()")
    print(f"Identity check time: {id_check:.6f}")
    print(f"Equality check time: {eq_check:.6f}")
    
    # Membership check: list vs set vs dict
    list_check = timeit.timeit("9999 in lst", globals=globals())
    set_check = timeit.timeit("9999 in set_version", globals=globals())
    dict_check = timeit.timeit("9999 in dict_version", globals=globals())
    print(f"List membership check time: {list_check:.6f}")
    print(f"Set membership check time: {set_check:.6f}")
    print(f"Dict membership check time: {dict_check:.6f}")

    # Custom class with __eq__ and __hash__
    class CustomObject:
        def __init__(self, value):
            self.value = value
        def __eq__(self, other):
            return isinstance(other, CustomObject) and self.value == other.value
        def __hash__(self):
            return hash(self.value)

    custom_objects = [CustomObject(i) for i in range(1000)]
    custom_set = set(custom_objects)
    
    custom_list_check = timeit.timeit("CustomObject(999) in custom_objects", globals=globals())
    custom_set_check = timeit.timeit("CustomObject(999) in custom_set", globals=globals())
    print(f"Custom object list membership check time: {custom_list_check:.6f}")
    print(f"Custom object set membership check time: {custom_set_check:.6f}")

"""
Optimization strategies:
1. Use sets or dictionaries instead of lists for frequent membership checks on large collections.
2. Prefer 'is' over '==' when comparing with None, True, or False.
3. Use custom __eq__ and __hash__ methods for efficient custom object comparisons.
4. Consider using `__slots__` for classes with many instances to reduce memory usage and slightly speed up attribute access.

Example of using __slots__:
"""

class OptimizedCustomObject:
    __slots__ = ['value']
    
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return isinstance(other, OptimizedCustomObject) and self.value == other.value
    
    def __hash__(self):
        return hash(self.value)

def measure_memory_usage(cls):
    import sys
    objects = [cls(i) for i in range(100000)]
    return sys.getsizeof(objects)

print(f"Memory usage without __slots__: {measure_memory_usage(CustomObject)}")
print(f"Memory usage with __slots__: {measure_memory_usage(OptimizedCustomObject)}")

"""
9. How to Contribute
====================
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

When adding new sections or expanding existing ones, consider:
- The relevance to identity and membership operators in Python
- The depth of explanation required for expert-level understanding
- The practical applications of the concept in real-world scenarios
- The potential impact on performance and optimization

Your contributions will help keep this note sheet up-to-date and valuable for 
Python developers at all levels. Thank you for your interest in improving this 
resource!
"""

# This is the main function that demonstrates the usage of identity and membership operators
def main():
    print("Identity and Membership Operators in Python - Expert-Level Note Sheet")
    print("=====================================================================")
    
    identity_operators_demo()
    print("\n" + "="*50 + "\n")
    
    membership_operators_demo()
    print("\n" + "="*50 + "\n")
    
    advanced_identity_comparison()
    print("\n" + "="*50 + "\n")
    
    advanced_membership_operations()
    print("\n" + "="*50 + "\n")
    
    # Run async demo
    asyncio.run(async_membership_demo())
    print("\n" + "="*50 + "\n")
    
    print("Object Interning Demo:")
    object_interning_demo()
    print("\n" + "="*50 + "\n")
    
    print("Custom Hashable Demo:")
    custom_hashable_demo()
    print("\n" + "="*50 + "\n")
    
    print("Membership Check Optimization:")
    optimize_membership_checks()
    print("\n" + "="*50 + "\n")
    
    print("Serialization and Identity Preservation:")
    serialize_and_check_identity()
    print("\n" + "="*50 + "\n")
    
    print("Troubleshooting Demos:")
    troubleshoot_integer_identity()
    print()
    troubleshoot_float_membership()
    print()
    demonstrate_mutable_default_issue()
    print("\n" + "="*50 + "\n")
    
    print("Performance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()