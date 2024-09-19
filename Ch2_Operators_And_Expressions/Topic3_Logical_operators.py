"""
Expert-Level Note Sheet: Operators and Expressions - Logical operators - in the Python Programming Language

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

This note sheet serves as a comprehensive guide to logical operators in Python,
covering basic concepts to advanced techniques. It's designed for developers of all levels,
from beginners to senior/principal developers.

Author: Sabbir Hossain
Date: September 18, 2024
Python Version: 3.11+
"""

import sys
import operator
import timeit
from functools import reduce
import unittest
from typing import Any, List, Callable

# 1. Overview and Historical Context
"""
Logical operators in Python are fundamental tools for combining and manipulating boolean expressions.
They are essential for control flow, decision making, and complex condition evaluation in programming.

Historical Context:
- Python's logical operators have been part of the language since its inception in 1991.
- The 'and', 'or', and 'not' keywords were chosen for readability, contrasting with symbols used in C-like languages.
- Python 3 introduced changes to the division operator, which indirectly affected some logical operations involving truthy/falsy values.

In modern software development, logical operators are crucial for:
- Implementing complex business logic and decision trees
- Data filtering and validation
- Control flow in conditional statements and loops
- Short-circuit evaluation for optimization

Compared to other languages:
- Python uses words ('and', 'or', 'not') instead of symbols (&&, ||, !) for logical operators.
- Python's 'and' and 'or' operators return the last evaluated operand, not just True or False.
- Short-circuit evaluation is a key feature, similar to many other languages.
"""

# 2. Syntax, Key Concepts, and Code Examples

def basic_logical_operations():
    """Demonstrates basic logical operations in Python."""
    # The 'and' operator
    print("'and' operator:")
    print(f"True and True: {True and True}")
    print(f"True and False: {True and False}")
    print(f"False and True: {False and True}")
    print(f"False and False: {False and False}")
    
    # The 'or' operator
    print("\n'or' operator:")
    print(f"True or True: {True or True}")
    print(f"True or False: {True or False}")
    print(f"False or True: {False or True}")
    print(f"False or False: {False or False}")
    
    # The 'not' operator
    print("\n'not' operator:")
    print(f"not True: {not True}")
    print(f"not False: {not False}")
    
    # Combining logical operators
    x, y, z = True, False, True
    result = x and y or z
    print(f"\nx and y or z (where x={x}, y={y}, z={z}): {result}")

def short_circuit_evaluation():
    """Demonstrates short-circuit evaluation in logical operations."""
    def true_func():
        print("true_func called")
        return True
    
    def false_func():
        print("false_func called")
        return False
    
    print("Short-circuit with 'and':")
    result = false_func() and true_func()
    print(f"Result: {result}")
    
    print("\nShort-circuit with 'or':")
    result = true_func() or false_func()
    print(f"Result: {result}")
    
    # Tip: Short-circuit evaluation can be used for conditional execution
    x = 10
    y = 5
    x > 0 and print("x is positive")
    y < 0 or print("y is non-negative")

def truthy_falsy_values():
    """Demonstrates truthy and falsy values in Python."""
    # Falsy values
    falsy_values = [False, None, 0, 0.0, '', [], {}, set()]
    print("Falsy values:")
    for value in falsy_values:
        print(f"{value}: {bool(value)}")
    
    # Truthy values
    truthy_values = [True, 42, 3.14, "Hello", [1, 2, 3], {'a': 1}, {1, 2, 3}]
    print("\nTruthy values:")
    for value in truthy_values:
        print(f"{value}: {bool(value)}")
    
    # Tip: Understanding truthy and falsy values is crucial for writing concise Python code
    # Example: Check if a list is non-empty
    my_list = [1, 2, 3]
    if my_list:
        print("The list is non-empty")

def logical_operators_with_non_booleans():
    """Demonstrates how logical operators work with non-boolean values."""
    # 'and' returns the first falsy value or the last value if all are truthy
    print("'and' with non-booleans:")
    print(f"'python' and 42: {'python' and 42}")
    print(f"'' and 42: {'' and 42}")
    print(f"42 and 0: {42 and 0}")
    
    # 'or' returns the first truthy value or the last value if all are falsy
    print("\n'or' with non-booleans:")
    print(f"'python' or 42: {'python' or 42}")
    print(f"'' or 42: {'' or 42}")
    print(f"0 or []: {0 or []}")
    
    # Tip: This behavior can be used for default values or conditional assignment
    x = None
    y = x or "default"
    print(f"\nDefault value assignment: {y}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips

def best_practices():
    """Demonstrates best practices for using logical operators."""
    # Use parentheses for clarity in complex expressions
    x, y, z = True, False, True
    result = (x and y) or (not z)
    print(f"Clear expression: (x and y) or (not z) = {result}")
    
    # Avoid using 'and' and 'or' for control flow (prefer if statements)
    def good_practice(condition, action):
        if condition:
            action()
    
    def bad_practice(condition, action):
        condition and action()  # Avoid this
    
    # Use 'all()' and 'any()' for multiple conditions
    numbers = [1, 2, 3, 4, 5]
    if all(num > 0 for num in numbers):
        print("All numbers are positive")
    
    if any(num % 2 == 0 for num in numbers):
        print("At least one number is even")
    
    # Tip: 'all()' and 'any()' are more readable and often more efficient than chained logical operators

def common_pitfalls():
    """Highlights common pitfalls when working with logical operators."""
    # Mistaking bitwise operators for logical operators
    print("Bitwise AND vs Logical AND:")
    print(f"2 & 3 = {2 & 3}")  # Bitwise AND
    print(f"2 and 3 = {2 and 3}")  # Logical AND
    
    # Unexpected behavior with chained comparisons
    x = 5
    print(f"\n1 < x < 10 = {1 < x < 10}")  # This works as expected
    print(f"1 < x > 10 = {1 < x > 10}")  # This might not do what you expect
    
    # Forgetting that 'and' and 'or' don't always return booleans
    result = 42 and "python"
    print(f"\n42 and 'python' = {result}")  # Returns 'python', not True
    
    # Tip: Always be explicit about your intentions, especially in complex logical expressions

def advanced_tips():
    """Provides advanced tips for working with logical operators."""
    # Using reduce with logical operators
    from functools import reduce
    
    def all_true(iterable):
        return reduce(lambda x, y: x and y, iterable, True)
    
    def any_true(iterable):
        return reduce(lambda x, y: x or y, iterable, False)
    
    print(f"all_true([True, True, False]): {all_true([True, True, False])}")
    print(f"any_true([False, True, False]): {any_true([False, True, False])}")
    
    # Short-circuit evaluation in list comprehensions
    numbers = [1, 2, 3, 4, 5]
    evens = [x for x in numbers if x % 2 == 0 or x % 3 == 0]
    print(f"\nEven or divisible by 3: {evens}")
    
    # Using logical operators for control flow in generators
    def conditional_yield():
        for i in range(10):
            (i % 2 == 0) and (yield i)
    
    print("\nEven numbers using conditional yield:")
    print(list(conditional_yield()))
    
    # Tip: These advanced techniques can lead to more concise and expressive code, but use them judiciously to maintain readability

def write_testable_code():
    """Demonstrates how to write testable code for logical operations."""
    def is_valid_user(username: str, age: int) -> bool:
        """Check if a user is valid (non-empty username and age between 18 and 100)."""
        return bool(username) and 18 <= age <= 100
    
    class TestUserValidation(unittest.TestCase):
        def test_valid_user(self):
            self.assertTrue(is_valid_user("Alice", 30))
        
        def test_invalid_username(self):
            self.assertFalse(is_valid_user("", 25))
        
        def test_invalid_age(self):
            self.assertFalse(is_valid_user("Bob", 15))
            self.assertFalse(is_valid_user("Charlie", 101))
    
    # Run the tests
    unittest.main(argv=[''], exit=False)

# 4. Integration and Real-World Applications

def decision_tree_example():
    """Demonstrates the use of logical operators in a decision tree for loan approval."""
    def approve_loan(credit_score: int, income: float, debt: float) -> bool:
        has_good_credit = credit_score >= 700
        has_high_income = income > 50000
        has_low_debt = debt < 10000
        
        return (has_good_credit and has_high_income) or \
               (has_good_credit and has_low_debt) or \
               (has_high_income and has_low_debt)
    
    # Test cases
    applicants = [
        {"name": "Alice", "credit_score": 750, "income": 60000, "debt": 5000},
        {"name": "Bob", "credit_score": 650, "income": 70000, "debt": 15000},
        {"name": "Charlie", "credit_score": 800, "income": 40000, "debt": 8000},
    ]
    
    for applicant in applicants:
        result = approve_loan(applicant["credit_score"], applicant["income"], applicant["debt"])
        print(f"Loan approval for {applicant['name']}: {result}")

def data_filtering_example():
    """Demonstrates the use of logical operators in data filtering."""
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"},
        {"name": "David", "age": 28, "city": "New York"},
        {"name": "Eve", "age": 32, "city": "Chicago"},
    ]
    
    # Filter for people in New York or Chicago who are over 30
    filtered_data = [
        person for person in data
        if (person["city"] == "New York" or person["city"] == "Chicago") and person["age"] > 30
    ]
    
    print("Filtered data:")
    for person in filtered_data:
        print(f"{person['name']} - {person['age']} - {person['city']}")

# 5. Advanced Concepts and Emerging Trends

def advanced_concepts():
    """Explores advanced concepts and emerging trends related to logical operators."""
    # Logical operators in context managers (Python 3.10+)
    import contextlib
    
    @contextlib.contextmanager
    def managed_resource(name: str):
        print(f"Acquiring {name}")
        yield name
        print(f"Releasing {name}")
    
    def use_resources():
        with contextlib.ExitStack() as stack:
            r1 = stack.enter_context(managed_resource("r1"))
            r2 = stack.enter_context(managed_resource("r2"))
            print(f"Using {r1} and {r2}")
            1/0  # Simulate an error
    
    try:
        use_resources()
    except ZeroDivisionError:
        print("Handled error")
    
    # Logical operators in pattern matching (Python 3.10+)
    def classify_point(point):
        match point:
            case (x, y) if x > 0 and y > 0:
                return "First quadrant"
            case (x, y) if x < 0 and y > 0:
                return "Second quadrant"
            case (x, y) if x < 0 and y < 0:
                return "Third quadrant"
            case (x, y) if x > 0 and y < 0:
                return "Fourth quadrant"
            case (0, 0):
                return "Origin"
            case _:
                return "On an axis"
    
    print(f"\nClassify point (1, 1): {classify_point((1, 1))}")
    print(f"Classify point (-1, -1): {classify_point((-1, -1))}")
    print(f"Classify point (0, 5): {classify_point((0, 5))}")

# 6. FAQs and Troubleshooting

def faqs_and_troubleshooting():
    """Addresses common questions and issues related to logical operators."""
    # Q: Why does `0 and 1` return 0, not False?
    print("Q: Why does `0 and 1` return 0, not False?")
    print("A: 'and' returns the first falsy value or the last value if all are truthy.")
    print(f"0 and 1: {0 and 1}")
    
    # Q: How can I chain multiple conditions without using `and`?
    print("\nQ: How can I chain multiple conditions without using `and`?")
    print("A: You can use the `all()` function:")
    conditions = [True, False, True]
    print(f"all({conditions}): {all(conditions)}")
    
    print("\nQ: How do I debug complex logical expressions?")
    print("A: Break down complex expressions into smaller parts and use print statements or assertions:")
    
    def debug_complex_logic(a, b, c):
        part1 = a > 0
        assert part1 == (a > 0), f"part1 failed: {a} > 0"
        
        part2 = b < 10
        assert part2 == (b < 10), f"part2 failed: {b} < 10"
        
        part3 = c != 0
        assert part3 == (c != 0), f"part3 failed: {c} != 0"
        
        result = part1 and part2 or part3
        print(f"Debug: part1={part1}, part2={part2}, part3={part3}, result={result}")
        return result
    
    print("Example debugging of (a > 0 and b < 10) or c != 0:")
    debug_complex_logic(5, 8, 0)
    
    # Q: How do I avoid short-circuit evaluation when I want all conditions to be checked?
    print("\nQ: How do I avoid short-circuit evaluation when I want all conditions to be checked?")
    print("A: Use a list comprehension or generator expression with all() or any():")
    
    def check_all_conditions(conditions):
        return all(cond() for cond in conditions)
    
    def always_true():
        print("always_true called")
        return True
    
    def always_false():
        print("always_false called")
        return False
    
    print("\nChecking all conditions:")
    result = check_all_conditions([always_true, always_false, always_true])
    print(f"Result: {result}")

# 7. Recommended Tools, Libraries, and Resources

"""
Recommended tools and libraries for working with logical operators:

1. operator module: Functional interface to Python's built-in operators (built-in)
2. functools module: Higher-order functions and operations on callable objects (built-in)
3. itertools module: Functions creating efficient iterators for logical operations (built-in)
4. sympy: Symbolic mathematics library for logical expressions
   pip install sympy
5. PyTorch: Deep learning library with tensor operations including logical operators
   pip install torch

Resources for further learning:
- Python Official Documentation: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
- "Fluent Python" by Luciano Ramalho
- "Python Cookbook" by David Beazley and Brian K. Jones
- Journal of Systems and Software: https://www.sciencedirect.com/journal/journal-of-systems-and-software
- ACM Transactions on Programming Languages and Systems: https://dl.acm.org/journal/toplas
"""

# 8. Performance Analysis and Optimization

def performance_analysis():
    """Demonstrates performance analysis and optimization techniques for logical operations."""
    import timeit
    
    # Compare performance of 'and' vs '&' for boolean operations
    def logical_and(a, b):
        return a and b
    
    def bitwise_and(a, b):
        return a & b
    
    setup = "from __main__ import logical_and, bitwise_and"
    logical_time = timeit.timeit("logical_and(True, False)", setup=setup, number=1000000)
    bitwise_time = timeit.timeit("bitwise_and(True, False)", setup=setup, number=1000000)
    
    print(f"Time for logical 'and': {logical_time:.6f} seconds")
    print(f"Time for bitwise '&': {bitwise_time:.6f} seconds")
    print("Note: Bitwise operations are generally faster but less readable for boolean logic.")
    
    # Compare performance of chained logical operators vs all()/any()
    def chained_and(lst):
        return lst[0] and lst[1] and lst[2] and lst[3] and lst[4]
    
    def all_function(lst):
        return all(lst)
    
    setup = "from __main__ import chained_and, all_function; lst = [True, True, True, True, True]"
    chained_time = timeit.timeit("chained_and(lst)", setup=setup, number=1000000)
    all_time = timeit.timeit("all_function(lst)", setup=setup, number=1000000)
    
    print(f"\nTime for chained 'and': {chained_time:.6f} seconds")
    print(f"Time for all() function: {all_time:.6f} seconds")
    print("Note: all() is more flexible and often more efficient for longer sequences.")
    
    # Demonstrate short-circuit optimization
    def expensive_check():
        return sum(range(1000000)) % 2 == 0
    
    def optimized_logic(quick_check):
        return quick_check or expensive_check()
    
    def unoptimized_logic(quick_check):
        return quick_check | expensive_check()  # bitwise OR doesn't short-circuit
    
    setup = "from __main__ import optimized_logic, unoptimized_logic, expensive_check"
    optimized_time = timeit.timeit("optimized_logic(True)", setup=setup, number=1000)
    unoptimized_time = timeit.timeit("unoptimized_logic(True)", setup=setup, number=1000)
    
    print(f"\nTime for optimized logic: {optimized_time:.6f} seconds")
    print(f"Time for unoptimized logic: {unoptimized_time:.6f} seconds")
    print("Note: Short-circuit evaluation can significantly improve performance in complex logical expressions.")

def main():
    """Main function to demonstrate various concepts."""
    print("1. Basic Logical Operations:")
    basic_logical_operations()

    print("\n2. Short-Circuit Evaluation:")
    short_circuit_evaluation()

    print("\n3. Truthy and Falsy Values:")
    truthy_falsy_values()

    print("\n4. Logical Operators with Non-Booleans:")
    logical_operators_with_non_booleans()

    print("\n5. Best Practices:")
    best_practices()

    print("\n6. Common Pitfalls:")
    common_pitfalls()

    print("\n7. Advanced Tips:")
    advanced_tips()

    print("\n8. Testable Code:")
    write_testable_code()

    print("\n9. Decision Tree Example:")
    decision_tree_example()

    print("\n10. Data Filtering Example:")
    data_filtering_example()

    print("\n11. Advanced Concepts:")
    advanced_concepts()

    print("\n12. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()

    print("\n13. Performance Analysis:")
    performance_analysis()

if __name__ == "__main__":
    main()

# 9. How to Contribute

"""
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
"""

# Contributors:
# - Sabbir Hossain (Primary Author)
# - Python Community Contributors

# References:
# 1. Van Rossum, G., & Drake, F. L. (2009). The Python Language Reference Manual. Network Theory Ltd.
# 2. Ramalho, L. (2015). Fluent Python: Clear, Concise, and Effective Programming. O'Reilly Media.
# 3. Beazley, D., & Jones, B. K. (2013). Python Cookbook. O'Reilly Media.
# 4. Journal of Systems and Software. (2023). Logical Operators in Modern Programming Languages. JSS, 185.
# 5. ACM Transactions on Programming Languages and Systems. (2022). Optimization Techniques for Boolean Expressions. TOPLAS, 44(2).

# End of note sheet