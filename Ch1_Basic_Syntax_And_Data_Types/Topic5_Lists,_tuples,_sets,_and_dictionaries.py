"""
Expert-Level Cheat Sheet: Basic Syntax and Data Types - Lists, tuples, sets, and dictionaries - in the Python Programming Language

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

This cheat sheet serves as a comprehensive guide to lists, tuples, sets, and dictionaries in Python,
covering basic concepts to advanced techniques. It's designed for developers of all levels,
from beginners to senior/principal developers.

Author: Claude AI
Date: September 18, 2024
Python Version: 3.11+
"""

import sys
import timeit
import collections
import itertools
from typing import List, Tuple, Set, Dict, Any
import unittest

# 1. Overview and Historical Context
"""
Lists, tuples, sets, and dictionaries are fundamental data structures in Python, essential for
organizing and manipulating data efficiently.

Historical Context:
- Lists and dictionaries have been part of Python since its inception in 1991.
- Tuples were introduced in Python 1.4 (1996).
- Sets were added as a built-in type in Python 2.4 (2004).
- Dictionaries became ordered by default in Python 3.7 (2018).

In modern software development, these data structures are crucial for:
- Data organization and retrieval
- Algorithm implementation
- Configuration management
- Database operations
- API design and implementation

Compared to other languages:
- Python's list is similar to ArrayList in Java or vector in C++.
- Tuples are similar to structs in C or readonly lists in C#.
- Sets are comparable to HashSet in Java or std::unordered_set in C++.
- Dictionaries are similar to HashMap in Java or std::unordered_map in C++.
"""

# 2. Syntax, Key Concepts, and Code Examples

def list_basics():
    """Demonstrates basic concepts related to lists in Python."""
    # List creation
    fruits = ['apple', 'banana', 'cherry']
    numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
    
    # Accessing elements
    print(f"First fruit: {fruits[0]}")
    print(f"Last number: {numbers[-1]}")
    
    # Slicing
    print(f"First two fruits: {fruits[:2]}")
    print(f"Every other number: {numbers[::2]}")
    
    # Modifying lists
    fruits.append('date')
    fruits.insert(1, 'blueberry')
    fruits.extend(['elderberry', 'fig'])
    fruits.remove('banana')
    popped_fruit = fruits.pop()
    
    print(f"Modified fruits: {fruits}")
    print(f"Popped fruit: {popped_fruit}")
    
    # List comprehension
    squared_numbers = [x**2 for x in range(1, 6)]
    print(f"Squared numbers: {squared_numbers}")

def tuple_basics():
    """Demonstrates basic concepts related to tuples in Python."""
    # Tuple creation
    coordinates = (3, 4)
    person = ('Alice', 30, 'Engineer')
    single_element_tuple = (42,)  # Note the comma
    
    # Accessing elements
    print(f"X coordinate: {coordinates[0]}")
    print(f"Person's name: {person[0]}")
    
    # Tuple unpacking
    name, age, occupation = person
    print(f"{name} is {age} years old and works as an {occupation}")
    
    # Tuples are immutable
    try:
        coordinates[0] = 5
    except TypeError as e:
        print(f"Error: {e}")
    
    # Named tuples
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(5, 10)
    print(f"Point: x={p.x}, y={p.y}")

def set_basics():
    """Demonstrates basic concepts related to sets in Python."""
    # Set creation
    fruits = {'apple', 'banana', 'cherry'}
    numbers = set([1, 2, 2, 3, 3, 4])  # Removes duplicates
    
    # Adding and removing elements
    fruits.add('date')
    fruits.remove('banana')
    fruits.discard('elderberry')  # No error if not present
    
    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")
    print(f"Symmetric difference: {set1 ^ set2}")
    
    # Set comprehension
    even_squares = {x**2 for x in range(10) if x % 2 == 0}
    print(f"Even squares: {even_squares}")

def dict_basics():
    """Demonstrates basic concepts related to dictionaries in Python."""
    # Dictionary creation
    person = {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}
    scores = dict(alice=95, bob=87, charlie=92)
    
    # Accessing and modifying elements
    print(f"Name: {person['name']}")
    person['age'] = 31
    person['city'] = 'New York'
    
    # Dictionary methods
    print(f"Keys: {person.keys()}")
    print(f"Values: {person.values()}")
    print(f"Items: {person.items()}")
    
    # Get with default value
    salary = person.get('salary', 'Not specified')
    print(f"Salary: {salary}")
    
    # Dictionary comprehension
    squared_numbers = {x: x**2 for x in range(1, 6)}
    print(f"Squared numbers: {squared_numbers}")

def advanced_operations():
    """Demonstrates advanced operations on lists, tuples, sets, and dictionaries."""
    # List sorting and custom sort
    fruits = ['banana', 'apple', 'cherry', 'date']
    fruits.sort()
    print(f"Sorted fruits: {fruits}")
    fruits.sort(key=len, reverse=True)
    print(f"Fruits sorted by length (descending): {fruits}")
    
    # Tuple as dictionary keys
    coordinates = {(0, 0): 'origin', (1, 0): 'unit x', (0, 1): 'unit y'}
    print(f"Value at origin: {coordinates[(0, 0)]}")
    
    # Set operations with methods
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Is set1 a subset of set2? {set1.issubset(set2)}")
    print(f"Do set1 and set2 have any elements in common? {set1.isdisjoint(set2)}")
    
    # Dictionary merging (Python 3.9+)
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = dict1 | dict2
    print(f"Merged dictionary: {merged_dict}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def best_practices():
    """Demonstrates best practices for working with lists, tuples, sets, and dictionaries."""
    # Use list comprehensions for simple transformations
    numbers = [1, 2, 3, 4, 5]
    squared = [x**2 for x in numbers]  # Prefer this over map() for readability
    
    # Use generator expressions for large datasets to save memory
    sum_of_squares = sum(x**2 for x in range(1000000))
    
    # Use tuple unpacking for multiple assignment
    a, b = 1, 2
    a, b = b, a  # Swapping values
    
    # Use sets for membership testing when you have many items
    large_set = set(range(1000000))
    print(f"Is 500000 in the set? {500000 in large_set}")  # O(1) complexity
    
    # Use dict.get() with a default value instead of checking if key exists
    config = {'debug': True}
    verbose = config.get('verbose', False)
    
    # Use collections.defaultdict for handling missing keys
    from collections import defaultdict
    word_counts = defaultdict(int)
    for word in ['apple', 'banana', 'apple', 'cherry']:
        word_counts[word] += 1
    print(f"Word counts: {dict(word_counts)}")

def common_pitfalls():
    """Highlights common pitfalls when working with lists, tuples, sets, and dictionaries."""
    # Mutable default arguments
    def append_to(element, lst=[]):  # Dangerous!
        lst.append(element)
        return lst
    
    print(append_to(1))  # [1]
    print(append_to(2))  # [1, 2], not [2]
    
    # Proper way:
    def append_to_safe(element, lst=None):
        if lst is None:
            lst = []
        lst.append(element)
        return lst
    
    # Modifying a list while iterating over it
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)  # This can skip elements
    print(f"Attempted to remove even numbers: {numbers}")
    
    # Proper way:
    numbers = [1, 2, 3, 4, 5]
    numbers = [num for num in numbers if num % 2 != 0]
    print(f"Correctly removed even numbers: {numbers}")
    
    # Using a list when a set would be more appropriate
    def unique_numbers(numbers):
        unique = []
        for num in numbers:
            if num not in unique:  # O(n) operation for each number
                unique.append(num)
        return unique
    
    # More efficient way using a set:
    def unique_numbers_efficient(numbers):
        return list(set(numbers))

def advanced_tips():
    """Provides advanced tips for working with lists, tuples, sets, and dictionaries."""
    # Using itertools for efficient iteration
    import itertools
    
    # Cartesian product
    colors = ['red', 'green']
    sizes = ['S', 'M', 'L']
    combinations = list(itertools.product(colors, sizes))
    print(f"Product combinations: {combinations}")
    
    # Grouping data
    data = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit')]
    grouped = itertools.groupby(sorted(data, key=lambda x: x[1]), key=lambda x: x[1])
    for key, group in grouped:
        print(f"{key}: {list(group)}")
    
    # Using functools.lru_cache for memoization
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(f"Fibonacci(100): {fibonacci(100)}")
    
    # Using collections.Counter for counting
    from collections import Counter
    
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
    word_counts = Counter(words)
    print(f"Word counts: {word_counts}")
    print(f"Most common word: {word_counts.most_common(1)}")

def write_testable_code():
    """Demonstrates how to write testable code for lists, tuples, sets, and dictionaries."""
    def flatten_list(nested_list):
        """Flatten a nested list."""
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list
    
    class TestFlattenList(unittest.TestCase):
        def test_flatten_list(self):
            self.assertEqual(flatten_list([1, [2, 3, [4, 5]], 6]), [1, 2, 3, 4, 5, 6])
            self.assertEqual(flatten_list([]), [])
            self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])
    
    # Run the tests
    unittest.main(argv=[''], exit=False)

# 4. Integration and Real-World Applications

def data_processing_example():
    """Demonstrates use of lists, tuples, sets, and dictionaries in data processing."""
    # Sample data: Employee records
    employees = [
        {'id': 1, 'name': 'Alice', 'department': 'IT', 'salary': 75000},
        {'id': 2, 'name': 'Bob', 'department': 'HR', 'salary': 65000},
        {'id': 3, 'name': 'Charlie', 'department': 'IT', 'salary': 80000},
        {'id': 4, 'name': 'David', 'department': 'Marketing', 'salary': 70000},
        {'id': 5, 'name': 'Eve', 'department': 'IT', 'salary': 78000},
    ]
    
    # Get unique departments
    departments = set(emp['department'] for emp in employees)
    print(f"Unique departments: {departments}")
    
    # Calculate average salary by department
    from collections import defaultdict
    salary_by_dept = defaultdict(list)
    for emp in employees:
        salary_by_dept[emp['department']].append(emp['salary'])
    
    avg_salary = {dept: sum(salaries) / len(salaries) for dept, salaries in salary_by_dept.items()}
    print(f"Average salary by department: {avg_salary}")
    
    # Find highest paid employee
    highest_paid = max(employees, key=lambda emp: emp['salary'])
    print(f"Highest paid employee: {highest_paid['name']}")
    
    # Group employees by department
    emp_by_dept = defaultdict(list)
    for emp in employees:
        emp_by_dept[emp['department']].append(emp['name'])
    print(f"Employees by department: {dict(emp_by_dept)}")

def api_design_example():
    """Demonstrates use of lists, tuples, sets, and dictionaries in API design."""
    class BookInventory:
        def __init__(self):
            self.books = {}  # ISBN: {title, author, quantity}
        
        def add_book(self, isbn: str, title: str, author: str, quantity: int) -> None:
            self.books[isbn] = {'title': title, 'author': author, 'quantity': quantity}
        
        def remove_book(self, isbn: str) -> bool:
            return self.books.pop(isbn, None) is not None
        
        def get_book(self, isbn: str) -> dict:
            return self.books.get(isbn, {})
        
        def update_quantity(self, isbn: str, quantity: int) -> bool:
            if isbn in self.books:
                self.books[isbn]['quantity'] = quantity
                return True
            return False
        
        def get_all_books(self) -> list:
            return [{'isbn': isbn, **book} for isbn, book in self.books.items()]
        
        def get_books_by_author(self, author: str) -> list:
            return [{'isbn': isbn, **book} for isbn, book in self.books.items() if book['author'] == author]
        
        def get_available_books(self) -> set:
            return {isbn for isbn, book in self.books.items() if book['quantity'] > 0}
    
    # Usage example
    inventory = BookInventory()
    inventory.add_book("978-1234567890", "Python Mastery", "John Doe", 5)
    inventory.add_book("978-0987654321", "Data Structures", "Jane Smith", 3)
    inventory.add_book("978-1111222233", "Algorithms", "John Doe", 7)
    
    print(f"All books: {inventory.get_all_books()}")
    print(f"Books by John Doe: {inventory.get_books_by_author('John Doe')}")
    print(f"Available books (ISBNs): {inventory.get_available_books()}")
    
    inventory.update_quantity("978-1234567890", 0)
    print(f"Updated available books (ISBNs): {inventory.get_available_books()}")

# 5. Advanced Concepts and Emerging Trends

def advanced_concepts():
    """Explores advanced concepts and emerging trends related to lists, tuples, sets, and dictionaries."""
    
    # Type hinting with generics (Python 3.9+)
    from typing import List, Dict, Tuple, Set, TypeVar

    T = TypeVar('T')

    def process_list(items: List[T]) -> List[Tuple[T, int]]:
        return [(item, len(str(item))) for item in items]

    numbers: List[int] = [1, 22, 333]
    strings: List[str] = ["a", "bb", "ccc"]
    print(f"Processed numbers: {process_list(numbers)}")
    print(f"Processed strings: {process_list(strings)}")

    # Structural Pattern Matching (Python 3.10+)
    def analyze_data_structure(data):
        match data:
            case []:
                return "Empty list"
            case [_]:
                return "Single-element list"
            case [_, _]:
                return "Two-element list"
            case [*_, last]:
                return f"List with {len(data)} elements, last is {last}"
            case {}:
                return "Empty dict"
            case {'name': str(name), 'age': int(age)}:
                return f"Person dict with name {name} and age {age}"
            case _:
                return "Unknown data structure"

    print(analyze_data_structure([]))
    print(analyze_data_structure([1, 2, 3, 4, 5]))
    print(analyze_data_structure({'name': 'Alice', 'age': 30}))

    # Using collections.ChainMap for layered dictionaries
    from collections import ChainMap

    defaults = {'color': 'red', 'user': 'guest'}
    user_prefs = {'color': 'blue'}
    combined = ChainMap(user_prefs, defaults)
    print(f"Combined preferences: {dict(combined)}")

    # Using types.MappingProxyType for read-only dictionaries
    from types import MappingProxyType

    writable = {'one': 1, 'two': 2}
    read_only = MappingProxyType(writable)
    # read_only['three'] = 3  # This would raise a TypeError

    # Immutable sets with frozenset
    immutable_set = frozenset([1, 2, 3])
    # immutable_set.add(4)  # This would raise an AttributeError

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Addresses common questions and issues related to lists, tuples, sets, and dictionaries."""
    
    # Q: How do I remove duplicates from a list while preserving order?
    def remove_duplicates(lst):
        return list(dict.fromkeys(lst))

    original = [1, 2, 3, 2, 4, 1, 5]
    print(f"Original: {original}")
    print(f"Without duplicates: {remove_duplicates(original)}")

    # Q: How can I sort a list of dictionaries by a specific key?
    people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    sorted_people = sorted(people, key=lambda x: x['age'])
    print(f"Sorted by age: {sorted_people}")

    # Q: How do I merge two dictionaries?
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged = {**dict1, **dict2}  # Python 3.5+
    print(f"Merged dictionary: {merged}")

    # Q: How can I create a dictionary from two lists?
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    new_dict = dict(zip(keys, values))
    print(f"Dictionary from lists: {new_dict}")

    # Q: How do I find the intersection of two lists?
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    intersection = list(set(list1) & set(list2))
    print(f"Intersection: {intersection}")

# 7. Recommended Tools, Libraries, and Resources

"""
Recommended tools and libraries for working with lists, tuples, sets, and dictionaries:

1. Collections module: Provides specialized container datatypes
   https://docs.python.org/3/library/collections.html

2. Itertools module: Functions creating efficient iterators
   https://docs.python.org/3/library/itertools.html

3. Functools module: Higher-order functions and operations on callable objects
   https://docs.python.org/3/library/functools.html

4. Numpy: Efficient operations on large, multi-dimensional arrays and matrices
   https://numpy.org/

5. Pandas: Data manipulation and analysis library
   https://pandas.pydata.org/

Resources for further learning:
- Python Official Documentation: https://docs.python.org/3/tutorial/datastructures.html
- "Fluent Python" by Luciano Ramalho
- "Python Cookbook" by David Beazley and Brian K. Jones
- Real Python tutorials: https://realpython.com/tutorials/data-structures/
- PyData conference talks on YouTube for advanced data structure usage
"""

# 8. Performance Analysis and Optimization

def performance_analysis():
    """Demonstrates performance analysis and optimization techniques."""
    import timeit
    
    # List vs. Set for membership testing
    def list_membership(n):
        lst = list(range(n))
        return n-1 in lst

    def set_membership(n):
        st = set(range(n))
        return n-1 in st

    n = 10000
    list_time = timeit.timeit(lambda: list_membership(n), number=1000)
    set_time = timeit.timeit(lambda: set_membership(n), number=1000)
    print(f"List membership time: {list_time:.6f} seconds")
    print(f"Set membership time: {set_time:.6f} seconds")

    # Dict vs. List for counting elements
    def count_with_list(elements):
        counts = []
        for element in elements:
            for item in counts:
                if item[0] == element:
                    item[1] += 1
                    break
            else:
                counts.append([element, 1])
        return counts

    def count_with_dict(elements):
        return {element: elements.count(element) for element in set(elements)}

    elements = [1, 2, 3, 1, 2, 1, 4, 5, 4] * 1000
    list_count_time = timeit.timeit(lambda: count_with_list(elements), number=10)
    dict_count_time = timeit.timeit(lambda: count_with_dict(elements), number=10)
    print(f"List counting time: {list_count_time:.6f} seconds")
    print(f"Dict counting time: {dict_count_time:.6f} seconds")

    # List comprehension vs. map() for simple transformations
    def square_list_comp(n):
        return [x**2 for x in range(n)]

    def square_map(n):
        return list(map(lambda x: x**2, range(n)))

    n = 10000
    list_comp_time = timeit.timeit(lambda: square_list_comp(n), number=1000)
    map_time = timeit.timeit(lambda: square_map(n), number=1000)
    print(f"List comprehension time: {list_comp_time:.6f} seconds")
    print(f"Map time: {map_time:.6f} seconds")

def main():
    """Main function to demonstrate various concepts."""
    print("1. List Basics:")
    list_basics()

    print("\n2. Tuple Basics:")
    tuple_basics()

    print("\n3. Set Basics:")
    set_basics()

    print("\n4. Dictionary Basics:")
    dict_basics()

    print("\n5. Advanced Operations:")
    advanced_operations()

    print("\n6. Best Practices:")
    best_practices()

    print("\n7. Common Pitfalls:")
    common_pitfalls()

    print("\n8. Advanced Tips:")
    advanced_tips()

    print("\n9. Testable Code:")
    write_testable_code()

    print("\n10. Data Processing Example:")
    data_processing_example()

    print("\n11. API Design Example:")
    api_design_example()

    print("\n12. Advanced Concepts:")
    advanced_concepts()

    print("\n13. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()

    print("\n14. Performance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()

# To contribute to this cheat sheet:
# 1. Fork the repository containing this file.
# 2. Make your changes, ensuring they follow the existing style and structure.
# 3. Add your name to the list of contributors at the end of the file.
# 4. Submit a pull request with a clear description of your changes.

# Contributors:
# - Claude AI

# End of cheat sheet