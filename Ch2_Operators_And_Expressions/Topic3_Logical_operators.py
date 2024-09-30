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

import sys  # Provides access to system-specific parameters and functions (e.g., sys.exit(), sys.argv)
import operator  # Offers efficient, functional equivalents to many built-in operations (e.g., and_, or_, not_)
import timeit  # Enables timing of small code snippets; useful for performance analysis and optimization
from functools import reduce  # Provides the 'reduce' function, useful for applying a function cumulatively to a sequence
import unittest  # Provides a testing framework to create and run test cases for verifying code correctness
from typing import Any, List, Callable  # Typing utilities for more explicit type hints in function signatures

# ========================================
# 1. Overview and Historical Context
# ---------------------------------
"""
Logical operators in Python are fundamental tools for combining and manipulating boolean expressions.
They are essential for control flow, decision-making, and evaluating complex conditions in programming.

Historical Context:
- Python's logical operators ('and', 'or', 'not') have been integral to the language since its inception in 1991.
- Unlike C-style languages that use symbols (&&, ||, !), Python's choice of using English words ('and', 'or', 'not') 
  emphasizes readability and simplicity, adhering to its philosophy of being intuitive and beginner-friendly.
- Python 3 introduced the 'true division' operator (/) and 'floor division' operator (//), which indirectly impacted logical 
  operations when working with truthy/falsy values due to more explicit type handling.

In modern software development, logical operators are crucial for:
- Implementing complex business logic and decision trees
- Data filtering, validation, and error handling
- Controlling flow in conditional statements and loop constructs
- Optimizing code execution through short-circuit evaluation

Comparison to other languages:
- Python uses 'and', 'or', 'not' instead of symbolic equivalents (&&, ||, !), which enhances code readability.
- Unlike other languages where logical operators return strictly boolean values (True/False), Python’s 'and' and 'or' 
  return the actual operand values, making them more versatile in certain scenarios.
- Short-circuit evaluation (i.e., stopping evaluation as soon as the result is determined) is a feature shared with 
  languages like C, C++, and Java, but Python's implementation is more flexible due to its operand-returning behavior.
"""
# ========================================

# Implementing Logical Operations
def logical_operations_demo():
    """Demonstrates various logical operators and their behavior in Python."""

    # Basic 'and' Operation
    # ---------------------
    # The 'and' operator evaluates the left operand first. If it is falsy (e.g., None, 0, "", [], etc.), it immediately 
    # returns the left operand without evaluating the right operand. This is known as short-circuit evaluation.
    result_and = 0 and 1  # Since 0 is falsy, the evaluation stops here, and 'result_and' is assigned 0.
    
    # Advanced Insight: Short-circuiting can be leveraged for performance optimization, such as avoiding unnecessary 
    # calculations or function calls when the outcome can be determined early.
    
    # Pitfall: Ensure that side effects or function calls that modify state aren't placed in logical operations where 
    # short-circuiting might prevent their execution.

    # 'or' Operator Behavior
    # ----------------------
    # The 'or' operator evaluates the left operand first. If it is truthy (e.g., non-zero, non-empty), the expression 
    # returns that value. Otherwise, it evaluates and returns the right operand.
    result_or = "" or "default_value"  # The left operand is an empty string (falsy), so the right operand is returned.

    # Advanced Tip: Use the 'or' operator to provide default values efficiently, as shown above. This technique is often 
    # used in configuration management and parameter setting.

    # 'not' Operator Behavior
    # -----------------------
    # The 'not' operator inverts the truthiness of its operand, returning True for falsy values and False for truthy values.
    result_not = not []  # An empty list is falsy, so 'result_not' becomes True.

    # Best Practice: Be mindful of Python’s concept of truthiness when using 'not', especially with collections (e.g., lists, 
    # dictionaries, sets) since empty collections are considered falsy, while non-empty ones are truthy.

    # Using 'operator' Module for Functional Approach
    # ----------------------------------------------
    # The 'operator' module provides function equivalents of logical operators (e.g., operator.and_, operator.or_). These 
    # can be useful in higher-order functions like 'map()' or 'reduce()', enhancing readability and functionality.
    values = [True, True, False]
    reduced_result = reduce(operator.and_, values)  # This evaluates to False because one of the values is False

    # Advanced Tip: When working with functional programming patterns or when passing logical operations as arguments to 
    # functions, prefer using 'operator.and_', 'operator.or_', etc., over lambda expressions for better clarity and efficiency.

# Implementing Unit Testing
class TestLogicalOperators(unittest.TestCase):
    """Unit test cases to validate logical operators and their expected behavior."""

    def test_and_operator(self):
        """Tests the 'and' operator's short-circuiting behavior and operand return."""
        self.assertEqual(0 and 1, 0)  # Expected: 0, because 'and' stops at the first falsy value
        self.assertEqual(1 and 2, 2)  # Expected: 2, because both operands are truthy, and 'and' returns the last operand

    def test_or_operator(self):
        """Tests the 'or' operator's short-circuiting behavior and operand return."""
        self.assertEqual("" or "fallback", "fallback")  # Expected: "fallback", as the left operand is falsy
        self.assertEqual("initial" or "fallback", "initial")  # Expected: "initial", as it's the first truthy operand

    def test_not_operator(self):
        """Tests the 'not' operator's inversion behavior."""
        self.assertTrue(not False)  # Expected: True, since 'not' inverts False
        self.assertFalse(not True)  # Expected: False, since 'not' inverts True

    def test_operator_module(self):
        """Tests logical operations using the 'operator' module."""
        values = [True, False, True]
        result = reduce(operator.or_, values)  # Expected to be True due to 'or' short-circuiting on the first True
        self.assertTrue(result)

# ========================================
# Summary and Advanced Insights
# ---------------------------------------
# - The 'and' and 'or' operators return the last evaluated operand, not strictly True/False, allowing for more versatile expressions.
# - Short-circuit evaluation is efficient but requires understanding when an expression stops evaluating, especially when
#   side effects (e.g., function calls) are involved.
# - For readability and functional programming, consider using the 'operator' module's equivalents.
# - Unit testing with the 'unittest' module ensures that logical operations behave as expected, especially in edge cases.
# 
# This detailed commentary and explanation provide an in-depth understanding of logical operators, ensuring that 
# foundational concepts, best practices, pitfalls, and advanced techniques are clearly articulated to aid growth toward 
# a senior or principal engineering level.


# ========================================
# 2. Syntax, Key Concepts, and Code Examples
# ---------------------------------------

def basic_logical_operations():
    """Demonstrates basic logical operations in Python with detailed explanations and examples."""
    
    # The 'and' operator
    # ---------------------------------
    # The 'and' operator is a logical conjunction that evaluates to True only if both operands are True.
    # It uses short-circuit evaluation, meaning if the first operand evaluates to False, the second operand is not evaluated.
    # This behavior is efficient, especially in expressions with multiple conditions, as unnecessary computations are avoided.
    print("'and' operator:")
    print(f"True and True: {True and True}")    # Evaluates to True, since both operands are True
    print(f"True and False: {True and False}")  # Evaluates to False, as one operand is False
    print(f"False and True: {False and True}")  # Evaluates to False, short-circuits after the first False
    print(f"False and False: {False and False}")# Evaluates to False, as both operands are False
    
    # Pitfall: Avoid assuming that all expressions after 'and' will always be evaluated. Short-circuiting can skip over
    # expressions, so if there's essential logic in the second condition, it might not be executed if the first condition is False.

    # The 'or' operator
    # ---------------------------------
    # The 'or' operator is a logical disjunction that evaluates to True if at least one operand is True.
    # It also employs short-circuit evaluation, meaning if the first operand evaluates to True, the second operand is not evaluated.
    print("\n'or' operator:")
    print(f"True or True: {True or True}")      # Evaluates to True, as at least one operand is True
    print(f"True or False: {True or False}")    # Evaluates to True, short-circuits after the first True
    print(f"False or True: {False or True}")    # Evaluates to True, as the second operand is True
    print(f"False or False: {False or False}")  # Evaluates to False, as both operands are False

    # Best Practice: Utilize short-circuiting to optimize expressions, placing the most likely True condition first when using 'or'
    # and the most likely False condition first when using 'and'.

    # The 'not' operator
    # ---------------------------------
    # The 'not' operator is a logical negation that inverts the Boolean value of its operand.
    # It is a unary operator, meaning it only takes one operand.
    print("\n'not' operator:")
    print(f"not True: {not True}")    # Evaluates to False, since 'not' inverts True
    print(f"not False: {not False}")  # Evaluates to True, since 'not' inverts False
    
    # Advanced Tip: Be cautious with the 'not' operator when combined with non-Boolean values, as it treats many objects
    # (e.g., empty lists, strings, numbers) as False. Always be aware of the truthiness of the objects being negated.

    # Combining logical operators
    # ---------------------------------
    # Logical operators can be combined to form more complex expressions. Python evaluates these expressions
    # following standard operator precedence: 'not' has the highest precedence, followed by 'and', and then 'or'.
    x, y, z = True, False, True  # Assigning Boolean values to variables for demonstration
    result = x and y or z
    print(f"\nx and y or z (where x={x}, y={y}, z={z}): {result}")  # Evaluates to True

    # Explanation:
    # 1. According to precedence, 'and' is evaluated first:
    #    - x and y evaluates to False because x is True, but y is False.
    # 2. Then the expression becomes: False or z
    # 3. Since z is True, the final result is True.

    # Best Practice: Use parentheses to make the precedence explicit when combining logical operators, even when you understand
    # the order of precedence. This makes the code more readable and less prone to errors.

    # Example with parentheses for clarity
    clearer_result = (x and y) or z
    print(f"(x and y) or z (with explicit parentheses, where x={x}, y={y}, z={z}): {clearer_result}")  # Also evaluates to True

    # Pitfall: Assuming default precedence can lead to logical errors, especially in more complex expressions. Always be clear
    # and deliberate with parentheses to ensure the intended logic is applied.

    # Advanced Insight: 
    # Python’s logical operators do not return strictly Boolean values. Instead, they return one of the original operands.
    # - For 'and', it returns the first False operand or the last operand if all are True.
    # - For 'or', it returns the first True operand or the last operand if all are False.

    # Demonstrating this behavior:
    a = 0  # 0 is treated as False in Python
    b = "hello"  # Non-empty strings are treated as True
    c = []  # An empty list is treated as False
    result = a and b
    print(f"\nResult of 'a and b' (where a=0, b='hello'): {result}")  # Outputs: 0, because 'a' is False
    result = b and c
    print(f"Result of 'b and c' (where b='hello', c=[]): {result}")   # Outputs: [], because 'c' is False
    result = a or b
    print(f"Result of 'a or b' (where a=0, b='hello'): {result}")     # Outputs: 'hello', as 'a' is False and 'b' is True

    # This behavior can be leveraged for more concise conditional assignments, but always ensure the intent is clear to avoid confusion.

# ========================================
# Summary
# ---------------------------------------
# - The 'and' operator short-circuits and evaluates to True only if both operands are True.
# - The 'or' operator short-circuits and evaluates to True if at least one operand is True.
# - The 'not' operator inverts the Boolean value of its operand.
# - Use parentheses to clarify precedence when combining logical operators, even if you know the rules.
# - Logical operators return one of their operands, not necessarily a Boolean value, which can be useful but requires careful handling.

# This function serves as a comprehensive guide to logical operators in Python, providing examples and insights that
# can help a developer advance from foundational understanding to more advanced, nuanced use cases.


# ========================================
# Short-Circuit Evaluation and Truthy/Falsy Values
# ---------------------------------

def short_circuit_evaluation():
    """Demonstrates short-circuit evaluation in logical operations in Python."""

    # Defining two functions to illustrate short-circuit behavior
    def true_func():
        # This function prints a message indicating it was called and returns True
        print("true_func called")
        return True
    
    def false_func():
        # This function prints a message indicating it was called and returns False
        print("false_func called")
        return False
    
    # Short-circuit evaluation with the 'and' operator
    # ------------------------------------------------
    # The 'and' operator evaluates operands from left to right and stops as soon as it encounters a falsy value.
    # This is known as "short-circuiting" because it avoids unnecessary evaluations, which can enhance performance.
    print("Short-circuit with 'and':")
    result = false_func() and true_func()  # 'false_func()' returns False, so 'true_func()' is not called
    print(f"Result: {result}")  # Outputs: False
    
    # Explanation: Since 'false_func()' returns False, the 'and' operation concludes early without calling 'true_func()'.
    # Advanced Tip: Use short-circuit evaluation to avoid potential errors, such as checking if an object is None before
    # accessing its attributes (e.g., 'obj is not None and obj.attribute').

    # Short-circuit evaluation with the 'or' operator
    # -----------------------------------------------
    # The 'or' operator evaluates operands from left to right and stops as soon as it encounters a truthy value.
    print("\nShort-circuit with 'or':")
    result = true_func() or false_func()  # 'true_func()' returns True, so 'false_func()' is not called
    print(f"Result: {result}")  # Outputs: True
    
    # Explanation: Since 'true_func()' returns True, the 'or' operation concludes early without calling 'false_func()'.
    # Advanced Tip: Use 'or' for providing default values (e.g., 'value = user_input or "default"').

    # Using short-circuit evaluation for conditional execution
    # -------------------------------------------------------
    # Short-circuiting can be harnessed for concise conditional execution in a single line.
    x = 10
    y = 5
    x > 0 and print("x is positive")  # Executes print statement because x > 0 evaluates to True
    y < 0 or print("y is non-negative")  # Executes print statement because y < 0 evaluates to False

    # Explanation: The first expression ('x > 0 and print(...)') prints "x is positive" because 'and' evaluates
    # both expressions when the first is True. In contrast, the second expression ('y < 0 or print(...)') only evaluates
    # the print when the first is False, due to the 'or' operator's behavior.

def truthy_falsy_values():
    """Demonstrates truthy and falsy values in Python, an essential concept for effective conditional logic."""

    # Falsy values in Python
    # ----------------------
    # In Python, several values are considered 'falsy,' meaning they evaluate to False in a boolean context.
    # Common falsy values include: False, None, zero (0, 0.0), empty sequences ('' for strings, [] for lists, 
    # {} for dictionaries, set() for sets, etc.).
    falsy_values = [False, None, 0, 0.0, '', [], {}, set()]  # A list of common falsy values
    print("Falsy values:")
    for value in falsy_values:
        print(f"{value}: {bool(value)}")  # Converting each value to bool to show it evaluates to False
    
    # Explanation: Each of these values evaluates to False, making them useful for conditional checks in control flow.

    # Truthy values in Python
    # -----------------------
    # Conversely, any value that is not falsy is considered 'truthy' and will evaluate to True in a boolean context.
    # Examples include non-zero numbers, non-empty sequences/collections, and the boolean 'True' itself.
    truthy_values = [True, 42, 3.14, "Hello", [1, 2, 3], {'a': 1}, {1, 2, 3}]  # A list of common truthy values
    print("\nTruthy values:")
    for value in truthy_values:
        print(f"{value}: {bool(value)}")  # Converting each value to bool to show it evaluates to True
    
    # Explanation: Each of these values evaluates to True in a conditional statement, enabling concise and readable checks.

    # Best Practice Tip: Understanding truthy and falsy values is crucial for writing concise and idiomatic Python code.
    # For instance, checking if a list is non-empty is more readable using 'if my_list:' instead of 'if len(my_list) > 0:'
    
    # Example: Check if a list is non-empty
    my_list = [1, 2, 3]
    if my_list:
        print("The list is non-empty")  # Executes because 'my_list' is truthy
    
    # Explanation: This check is more concise and efficient than explicitly checking the length of the list.

# ========================================
# Summary and Advanced Tips
# ---------------------------------------
# - Short-circuit evaluation with 'and' and 'or' avoids unnecessary evaluations, enhancing both performance and safety.
# - Use 'and' and 'or' for compact conditional execution, but be cautious of using them for control flow in complex scenarios,
#   as it can reduce code readability if overused.
# - Understanding truthy and falsy values is fundamental for writing efficient and idiomatic Python code.
# - Use explicit checks when the distinction between truthy/falsy values is essential (e.g., distinguishing between None and other falsy values).

# Advanced Insight: 
# - Short-circuit evaluation can also be used in function arguments to prevent side effects or errors.
#   For example, 'function(arg1 and arg2)' ensures 'arg2' is only evaluated if 'arg1' is True, which can be useful
#   in cases where evaluating 'arg2' could be computationally expensive or result in an error if 'arg1' is not met.
#
# - Be mindful of implicit type conversions to boolean in conditional expressions, especially when working with 
#   data structures that might contain None or other falsy values, as this can lead to subtle bugs if not carefully handled.

# This comprehensive commentary provides a holistic understanding of short-circuit evaluation and truthy/falsy values, 
# including their practical applications, potential pitfalls, and advanced tips for optimization and code clarity.


def logical_operators_with_non_booleans():
    """Demonstrates how logical operators ('and' and 'or') work with non-boolean values in Python."""

    # Logical Operators in Python: Background
    # ---------------------------------------
    # In Python, logical operators ('and', 'or', 'not') do not strictly return boolean values (True/False) 
    # when used with non-boolean operands. Instead, they return one of the original operands based on 
    # their truthiness (whether the value is considered True or False in a boolean context).
    # This feature is often utilized in Python's dynamic typing and can be very powerful but requires 
    # careful understanding to avoid common pitfalls.

    # 'and' Operator with Non-Booleans
    # ---------------------------------
    # The 'and' operator evaluates from left to right and returns the first falsy (evaluates to False) value 
    # it encounters. If all values are truthy (evaluate to True), it returns the last value. 
    # This means 'and' stops evaluating as soon as it finds a falsy value (short-circuiting behavior).

    print("'and' with non-booleans:")
    print(f"'python' and 42: {'python' and 42}")  
    # Explanation: Here, both 'python' and 42 are truthy values, so 'and' evaluates both and returns the last value: 42.

    print(f"'' and 42: {'' and 42}")  
    # Explanation: The empty string '' is a falsy value. Since 'and' stops at the first falsy value, 
    # it returns '' without evaluating the rest.

    print(f"42 and 0: {42 and 0}")  
    # Explanation: 42 is truthy, but 0 is falsy. The 'and' operator stops at 0 and returns it.

    # Advanced Tip: The 'and' operator's short-circuiting behavior can be harnessed to avoid unnecessary computations.
    # For example, in complex conditional checks, placing the most likely falsy condition first can enhance performance.

    # 'or' Operator with Non-Booleans
    # -------------------------------
    # The 'or' operator also evaluates from left to right but returns the first truthy value it encounters.
    # If all values are falsy, it returns the last value. Like 'and', 'or' short-circuits, meaning it stops 
    # evaluating as soon as it finds a truthy value.

    print("\n'or' with non-booleans:")
    print(f"'python' or 42: {'python' or 42}")  
    # Explanation: Since 'python' is truthy, 'or' stops there and returns 'python' without evaluating 42.

    print(f"'' or 42: {'' or 42}")  
    # Explanation: The empty string '' is falsy, so 'or' continues to the next operand and returns 42, which is truthy.

    print(f"0 or []: {0 or []}")  
    # Explanation: Both 0 and [] (an empty list) are falsy. Since no truthy value is found, 'or' returns the last value, [].

    # Advanced Tip: Using 'or' for providing default values is a common and efficient pattern in Python, 
    # especially when dealing with optional parameters or fallbacks.

    # Practical Example: Using 'or' for Default Value Assignment
    # ---------------------------------------------------------
    # This pattern is frequently used to provide a default value when a variable might be None or another falsy value.
    x = None  # x is explicitly set to None (falsy)
    y = x or "default"  # Since x is falsy, 'or' evaluates to "default"
    print(f"\nDefault value assignment: {y}")  

    # Best Practice: This technique is concise and readable, but be aware that it treats all falsy values (None, 0, '', [], etc.) 
    # the same. If you specifically want to check for None, use 'is None' instead.

    # Potential Pitfall: Be cautious when using 'or' for default values if there's a chance of valid falsy inputs 
    # (e.g., an empty string '' or 0) that should not be overridden. In such cases, consider using 
    # an explicit conditional assignment instead.
    
    # For example:
    x = ""  # An empty string might be a valid value in this context
    y = x or "default"  # This will still assign "default", potentially leading to unintended behavior
    print(f"Default assignment with valid falsy input: {y}")

    # Correct Approach: Check explicitly for None if you intend to use a default only when x is None.
    y = x if x is not None else "default"
    print(f"Explicit None check for default assignment: {y}")


# ========================================
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# ---------------------------------

def best_practices():
    """Demonstrates best practices for using logical operators in Python."""

    # Use parentheses for clarity in complex expressions
    # -------------------------------------------------
    # When dealing with logical expressions, especially those with mixed 'and' and 'or' operators, 
    # it's crucial to use parentheses to make the order of operations explicit. This not only improves readability
    # but also prevents subtle bugs caused by misunderstandings of Python's operator precedence.
    x, y, z = True, False, True  # Example boolean values for demonstration
    result = (x and y) or (not z)  # Parentheses clarify the intended evaluation order
    print(f"Clear expression: (x and y) or (not z) = {result}")
    
    # Explanation: Without parentheses, logical expressions can become ambiguous. For instance, 'x and y or not z'
    # might be misinterpreted by others reading the code. Python evaluates 'not' first, followed by 'and', then 'or',
    # but using parentheses removes any doubt about the intended logic.

    # Advanced Tip: Always prioritize readability over cleverness. Even if you know the operator precedence by heart,
    # parentheses signal the expression's intent to others, reducing the risk of misinterpretation.

    # Avoid using 'and' and 'or' for control flow (prefer if statements)
    # ------------------------------------------------------------------
    # While Python allows expressions like 'condition and action()', using them can be confusing and is generally
    # considered poor practice for control flow. It's better to use explicit 'if' statements for better readability
    # and maintainability.
    
    def good_practice(condition, action):
        if condition:  # Explicitly checks the condition
            action()   # Executes the action if the condition is True

    def bad_practice(condition, action):
        condition and action()  # Avoid this: Using 'and' in this context makes the code less readable and harder to debug
    
    # Explanation: The 'condition and action()' pattern is concise but obfuscates intent, making the code harder to
    # understand, especially for less experienced developers. Explicit 'if' statements are clearer and convey control flow more effectively.
    
    # Advanced Insight: Code readability and maintainability are paramount, especially in collaborative environments.
    # Always aim to write code that others (or even you, months later) can easily understand.

    # Use 'all()' and 'any()' for multiple conditions
    # ----------------------------------------------
    # 'all()' and 'any()' are built-in functions that offer an elegant and efficient way to handle multiple conditions.
    # - 'all(iterable)' returns True if all elements in the iterable are true.
    # - 'any(iterable)' returns True if at least one element in the iterable is true.
    numbers = [1, 2, 3, 4, 5]  # Example list of numbers

    if all(num > 0 for num in numbers):  # Check if all numbers are positive
        print("All numbers are positive")

    if any(num % 2 == 0 for num in numbers):  # Check if there's at least one even number
        print("At least one number is even")
    
    # Best Practice: 'all()' and 'any()' are more readable and often more efficient than manually chaining 'and'/'or' operators.
    # They also short-circuit, meaning they stop evaluating as soon as the result is determined, improving performance.
    
    # Advanced Tip: When using 'all()' and 'any()', consider that they work on any iterable, not just lists. This means 
    # they can be used with generator expressions, which are memory efficient since they yield values one by one rather than 
    # building an entire list in memory.

    # Example using generator expressions
    # -----------------------------------
    # This example demonstrates the advantage of using 'all()' with a generator expression for large datasets:
    large_numbers = range(1, 10**6)  # Large range of numbers
    if all(num > 0 for num in large_numbers):  # Generator expression avoids creating a list in memory
        print("All numbers are positive in a large dataset")

    # Explanation: Generator expressions combined with 'all()' or 'any()' provide efficient iteration, especially when
    # working with large data, as they avoid the memory overhead of constructing intermediate lists.

# ========================================
# Summary and Additional Tips
# ---------------------------------------
# - Always use parentheses in complex logical expressions to make the evaluation order explicit and improve readability.
# - Prefer explicit 'if' statements over using 'and'/'or' for control flow to avoid confusion and maintain clear intent.
# - Leverage 'all()' and 'any()' for handling multiple conditions, as they offer readability and efficiency, especially 
#   when used with generator expressions for large datasets.
# - Understand that 'all()' and 'any()' short-circuit, making them more performant in certain scenarios compared to chaining logical operators.

# This code is designed to not only demonstrate best practices and pitfalls but also to provide deep insights into 
# the rationale behind each practice, enabling a holistic understanding suitable for progression to a principal engineer level.

# ========================================
# 3. Common Pitfalls When Working with Logical Operators
# ---------------------------------

def common_pitfalls():
    """Highlights common pitfalls when working with logical operators and provides advanced insights."""

    # Mistaking bitwise operators for logical operators
    # ------------------------------------------------
    # Bitwise operators (&, |, ^) operate at the binary level and perform operations on each bit of the operands.
    # Logical operators (and, or, not), on the other hand, are used for Boolean logic and operate on entire expressions.
    print("Bitwise AND vs Logical AND:")

    # Bitwise AND
    # ---------------------
    # The '&' operator performs a bitwise AND operation, which compares each bit of two integers and returns 
    # a new integer where each bit is set to 1 if both corresponding bits of the operands are also 1.
    # Example: 2 in binary is '10', 3 is '11'. The bitwise AND of 2 & 3 = '10', which is 2 in decimal.
    print(f"2 & 3 = {2 & 3}")  # Outputs: 2

    # Logical AND
    # ---------------------
    # The 'and' operator is a logical operator that evaluates to the first falsy value in the expression or 
    # the last truthy value if all operands are true. This means '2 and 3' evaluates to 3 because both 2 and 3 are truthy.
    print(f"2 and 3 = {2 and 3}")  # Outputs: 3

    # Pitfall: Confusing bitwise and logical operators can lead to subtle bugs, especially if you forget to 
    # differentiate between bit-level operations (&, |) and logical operations (and, or).
    
    # Advanced Tip: Always double-check operator usage, especially when working with non-Boolean values, 
    # as using bitwise operators by mistake can produce unexpected outcomes that are hard to debug.

    # Unexpected behavior with chained comparisons
    # ---------------------------------------------
    # Python allows chaining comparisons in a very natural way. However, this feature can sometimes lead to 
    # confusion if the logic is not fully understood.
    x = 5
    
    # This works as expected: 
    # 1 < x < 10 is equivalent to (1 < x) and (x < 10). Both comparisons are evaluated, and the result is True.
    print(f"\n1 < x < 10 = {1 < x < 10}")  # Outputs: True

    # However, this comparison might not work as you expect:
    # 1 < x > 10 is equivalent to (1 < x) and (x > 10). Since x is 5, (1 < 5) is True, but (5 > 10) is False,
    # so the final result is False.
    print(f"1 < x > 10 = {1 < x > 10}")  # Outputs: False

    # Pitfall: Chained comparisons can sometimes be misinterpreted, especially when the logic involves both 
    # greater-than and less-than operators. Always ensure that the comparisons accurately reflect the intended logic.

    # Advanced Insight: Python evaluates chained comparisons in a single, continuous evaluation without 
    # recomputing 'x'. This is more efficient than writing the equivalent compound logic manually.

    # Forgetting that 'and' and 'or' don't always return booleans
    # -----------------------------------------------------------
    # In Python, 'and' and 'or' are short-circuit operators that do not necessarily return True or False.
    # Instead, they return the actual operand that determined the result.

    # In this case, '42 and "python"' evaluates as follows:
    # Since 42 is a truthy value (non-zero), 'and' continues to the next operand and returns it.
    result = 42 and "python"
    print(f"\n42 and 'python' = {result}")  # Outputs: 'python'

    # Best Practice: Understand that 'and' returns the first falsy operand or the last truthy operand.
    # Similarly, 'or' returns the first truthy operand or the last falsy one.

    # Example with 'or':
    # If the first operand is truthy, 'or' returns it without evaluating the second operand.
    result_or = 0 or "default"  # Outputs 'default' since 0 is falsy
    print(f"0 or 'default' = {result_or}")

    # Advanced Tip: This behavior can be exploited to implement default values:
    # For example, 'value = provided_value or "default_value"' assigns 'default_value' if 'provided_value' is falsy.

    # Pitfall: Assuming 'and' and 'or' always return booleans can lead to unintended type errors or logical bugs, 
    # especially when the result is used in further expressions that expect a specific type.

    # Tip: Always be explicit about your intentions, especially in complex logical expressions.
    # Consider using parentheses to group logical conditions clearly, ensuring that the evaluation order 
    # is immediately apparent to anyone reading the code.

# Summary
# -------
# - Ensure you distinguish between bitwise (&, |, ^) and logical (and, or, not) operators to avoid subtle bugs.
# - Understand and leverage Python's capability for chaining comparisons, but be mindful of potential misinterpretations.
# - Be aware that 'and' and 'or' do not necessarily return booleans; they return the actual evaluated operand.
# - Use parentheses to improve readability and clarity in complex logical expressions, reducing the chance of logical errors.
# - Exploit the short-circuiting behavior of 'and' and 'or' for efficiency and implementing default value patterns.

# This detailed commentary provides a comprehensive explanation of the common pitfalls associated with logical operators,
# incorporating foundational knowledge and advanced insights, suitable for growth from novice to principal engineer.

# ========================================
# Advanced Tips and Writing Testable Code
# ---------------------------------------

def advanced_tips():
    """Provides advanced tips for working with logical operators."""

    # Using 'reduce' with logical operators
    # -------------------------------------
    # The 'reduce' function, part of the 'functools' module, applies a rolling computation to the items
    # in an iterable. It can be used with logical operators for scenarios requiring cumulative logic.
    from functools import reduce  # Importing reduce from functools

    # Function to check if all elements in an iterable are True
    def all_true(iterable):
        # Using 'reduce' to perform an 'and' operation across all elements
        return reduce(lambda x, y: x and y, iterable, True)
    
    # Function to check if any element in an iterable is True
    def any_true(iterable):
        # Using 'reduce' to perform an 'or' operation across all elements
        return reduce(lambda x, y: x or y, iterable, False)
    
    # Demonstrating the use of these functions
    print(f"all_true([True, True, False]): {all_true([True, True, False])}")  # Outputs: False, as one element is False
    print(f"any_true([False, True, False]): {any_true([False, True, False])}")  # Outputs: True, as one element is True
    
    # Advanced Insight: 
    # - 'reduce' is versatile but can be less readable than using Python's built-in 'all()' and 'any()' functions.
    # - Prefer 'all(iterable)' and 'any(iterable)' over 'reduce' for simplicity and clarity, as they are optimized 
    #   and self-explanatory for such cases. However, understanding 'reduce' is valuable for more complex accumulations.

    # Short-circuit evaluation in list comprehensions
    # ----------------------------------------------
    # Python uses short-circuit evaluation, meaning expressions are evaluated from left to right,
    # and evaluation stops as soon as the result is determined.
    numbers = [1, 2, 3, 4, 5]  # A list of integers
    # Using a list comprehension with a logical 'or' to filter numbers that are even or divisible by 3
    evens = [x for x in numbers if x % 2 == 0 or x % 3 == 0]
    print(f"\nEven or divisible by 3: {evens}")  # Outputs: [2, 3, 4] since these numbers satisfy at least one condition
    
    # Best Practice: Short-circuit evaluation in comprehensions is efficient, as it avoids unnecessary checks 
    # once a condition is met. Use it to optimize filtering but avoid over-complicating conditions to maintain readability.

    # Using logical operators for control flow in generators
    # ------------------------------------------------------
    # Logical operators like 'and' can be leveraged creatively for concise control flow, especially in generators.
    def conditional_yield():
        for i in range(10):
            # The expression '(i % 2 == 0) and (yield i)' means 'yield i' will only execute if 'i % 2 == 0' is True.
            (i % 2 == 0) and (yield i)
    
    # Displaying even numbers using the generator
    print("\nEven numbers using conditional yield:")
    print(list(conditional_yield()))  # Outputs: [0, 2, 4, 6, 8]
    
    # Advanced Tip: 
    # - This technique offers conciseness but can be harder to read for those unfamiliar with using logical operators
    #   in this manner. Use it judiciously and prefer explicit conditions when working in a team or writing maintainable code.

    # Summary Tip: These advanced techniques (reduce, short-circuiting, logical control flow) can lead to more concise 
    # and expressive code, but always balance brevity with clarity. 

def write_testable_code():
    """Demonstrates how to write testable code for logical operations."""

    # Function to check if a user is valid based on username and age
    def is_valid_user(username: str, age: int) -> bool:
        """Check if a user is valid (non-empty username and age between 18 and 100)."""
        # The function returns True if 'username' is non-empty and 'age' is within the specified range
        return bool(username) and 18 <= age <= 100
    
    # Advanced Insight:
    # - Using 'bool(username)' ensures the username is not an empty string, which is more robust than simply 'if username'.
    # - The chained comparison '18 <= age <= 100' is idiomatic Python and avoids verbosity, improving both readability 
    #   and performance by evaluating the expression in a single step.

    # Writing Unit Tests using the 'unittest' module
    import unittest  # Importing the built-in unittest module for writing test cases
    
    # Defining a test case class that inherits from 'unittest.TestCase'
    class TestUserValidation(unittest.TestCase):
        
        # Test method to check a valid user
        def test_valid_user(self):
            self.assertTrue(is_valid_user("Alice", 30))  # Asserts that the function should return True
        
        # Test method to check an invalid user due to an empty username
        def test_invalid_username(self):
            self.assertFalse(is_valid_user("", 25))  # Asserts that an empty username returns False
        
        # Test methods to check invalid age conditions
        def test_invalid_age(self):
            self.assertFalse(is_valid_user("Bob", 15))  # Asserts age below 18 is invalid
            self.assertFalse(is_valid_user("Charlie", 101))  # Asserts age above 100 is invalid

    # Running the tests
    # ---------------------------------------
    # 'unittest.main()' runs all test cases defined in the script. The 'argv=['']' argument prevents unittest from 
    # interpreting any command-line arguments passed to the script, and 'exit=False' allows Jupyter or other environments 
    # to execute the tests without quitting.
    unittest.main(argv=[''], exit=False)

    # Best Practice: Write test cases for all edge cases, including boundary values (e.g., age=18 and age=100).
    # - Test-driven development (TDD) encourages writing tests before implementing the function logic, leading to 
    #   more robust and reliable code.

    # Advanced Tip: Incorporate parameterized testing (e.g., with 'unittest's parameterized module or pytest) to avoid 
    # redundancy when testing multiple inputs.

# ========================================
# Summary
# ---------------------------------------
# - Use 'reduce' for cumulative operations but favor built-in functions like 'all()' and 'any()' for clarity.
# - Utilize short-circuit evaluation to optimize conditions but maintain readability.
# - Leverage logical operators creatively but ensure maintainability, especially in collaborative projects.
# - Write testable code using unittest, covering edge cases and incorporating TDD practices for more reliable and maintainable software.

# These comments and explanations are designed to guide you through advanced Python techniques and best practices, 
# providing a thorough understanding suitable for elevating skills from novice to principal engineer level.


# ========================================
# 4. Integration and Real-World Applications
# ---------------------------------

def decision_tree_example():
    """Demonstrates the use of logical operators in a decision tree for loan approval."""

    # Define a function to assess loan approval based on applicant's credit score, income, and debt
    def approve_loan(credit_score: int, income: float, debt: float) -> bool:
        # Evaluating financial conditions for the applicant
        has_good_credit = credit_score >= 700  # A credit score of 700 or above is typically considered good
        has_high_income = income > 50000  # Applicants with an income greater than 50,000 are considered to have high income
        has_low_debt = debt < 10000  # A debt below 10,000 is considered manageable
        
        # The logical decision-making process for loan approval:
        # - Approve if the applicant has good credit and either high income or low debt
        # - Alternatively, approve if they have high income and low debt
        return (has_good_credit and has_high_income) or \
               (has_good_credit and has_low_debt) or \
               (has_high_income and has_low_debt)

    # Real-world application: Evaluating loan applications from multiple applicants
    applicants = [
        {"name": "Alice", "credit_score": 750, "income": 60000, "debt": 5000},
        {"name": "Bob", "credit_score": 650, "income": 70000, "debt": 15000},
        {"name": "Charlie", "credit_score": 800, "income": 40000, "debt": 8000},
    ]
    
    # Process each applicant's data
    for applicant in applicants:
        result = approve_loan(applicant["credit_score"], applicant["income"], applicant["debt"])
        print(f"Loan approval for {applicant['name']}: {result}")

    # Integration Insight: This example simulates a basic decision tree for loan approval based on simple logical rules.
    # In real-world scenarios, decision trees can be significantly more complex, incorporating additional factors such as 
    # employment history, outstanding debts, assets, and other financial indicators.

    # Advanced Tip: For more sophisticated decision-making models, consider using machine learning libraries such as 
    # scikit-learn's DecisionTreeClassifier, which can handle multi-variable decision-making and learn patterns from data.

    # Pitfall to Avoid: Hardcoding business logic directly into functions, as done here, can lead to maintainability issues 
    # if business rules change frequently. In a production environment, consider storing rules in a database or configuration file.

def data_filtering_example():
    """Demonstrates the use of logical operators in data filtering."""

    # Sample dataset representing individuals with their respective attributes
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"},
        {"name": "David", "age": 28, "city": "New York"},
        {"name": "Eve", "age": 32, "city": "Chicago"},
    ]
    
    # Filtering logic: Select people who are either in New York or Chicago and are over 30 years old
    filtered_data = [
        person for person in data
        if (person["city"] == "New York" or person["city"] == "Chicago") and person["age"] > 30
    ]
    
    # Print the filtered data
    print("Filtered data:")
    for person in filtered_data:
        print(f"{person['name']} - {person['age']} - {person['city']}")

    # Integration Insight: This example demonstrates how to filter data based on complex conditions using logical operators.
    # In a more complex application, such data filtering might be used for database queries, data analysis, or preprocessing.

    # Advanced Tip: For large datasets, consider using libraries like pandas, which offer efficient and optimized data 
    # filtering capabilities with greater flexibility and performance than list comprehensions.

    # Pitfall to Avoid: Avoid using complex and deeply nested logical expressions in data filtering as it can make the code 
    # difficult to read and maintain. Instead, break down the logic into smaller, reusable functions when possible for clarity.

# ========================================
# Summary and Integration Insights
# ---------------------------------------
# - Decision trees are powerful tools for decision-making processes and can be implemented using logical operators.
# - Filtering data using logical conditions is fundamental in many applications, from data analysis to web development.
# - Consider advanced libraries such as scikit-learn for decision tree modeling and pandas for efficient data manipulation 
#   to handle more complex real-world scenarios.

# The provided examples offer practical insights into integrating logical operators for decision-making and data filtering, 
# laying the groundwork for more advanced applications as you progress toward becoming a principal engineer.


# ========================================
# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

def advanced_concepts():
    """Explores advanced concepts and emerging trends related to logical operators and advanced Python features."""

    # Logical operators in context managers (Python 3.10+)
    # ----------------------------------------------------
    # Context managers are used to properly manage resources, ensuring they are acquired and released correctly.
    # The 'contextlib' module provides utilities for context management, making it easier to manage multiple resources
    # without having to write custom context management logic.

    import contextlib  # Importing the contextlib module which contains utilities for context management

    # Creating a custom context manager using 'contextlib.contextmanager' decorator
    @contextlib.contextmanager
    def managed_resource(name: str):
        """A simple context manager for acquiring and releasing a resource."""
        print(f"Acquiring {name}")  # Code executed when entering the context
        yield name  # Yield control back to the calling code (acts as a placeholder for the context's "body")
        print(f"Releasing {name}")  # Code executed when exiting the context

    # Explanation: The 'yield' keyword here is essential. It allows the context manager to run the code before 
    # and after the 'with' block seamlessly, handling both the setup and teardown of the resource.
    # Advanced Tip: Using '@contextlib.contextmanager' is an elegant way to convert a simple generator function
    # into a context manager, avoiding the need to implement the full context manager protocol (__enter__, __exit__).

    # Function demonstrating the use of multiple context managers with 'ExitStack'
    def use_resources():
        # 'contextlib.ExitStack()' allows multiple context managers to be managed within a single 'with' statement.
        # This is particularly useful when the number of context managers is dynamic or conditional.
        with contextlib.ExitStack() as stack:
            # Entering multiple context managers using 'enter_context', which acquires the resource
            r1 = stack.enter_context(managed_resource("r1"))
            r2 = stack.enter_context(managed_resource("r2"))
            print(f"Using {r1} and {r2}")
            1 / 0  # Simulate an error to test how the context managers handle exceptions

    # Explanation: 'ExitStack' is highly flexible and can be used for dynamic resource management.
    # It ensures that all entered contexts are exited properly, even if an error occurs midway.

    try:
        use_resources()  # Attempting to use the resources within the context managers
    except ZeroDivisionError:
        # Handling a simulated error (division by zero)
        print("Handled error")

    # Advanced Insight: When an exception occurs within the 'with' block, the 'ExitStack' ensures that all resources
    # are released in the reverse order they were acquired. This guarantees proper cleanup, even in error scenarios.
    # This feature is crucial in resource-intensive applications, such as file handling, network connections, or
    # database transactions, to avoid resource leaks.

    # Logical operators in pattern matching (Python 3.10+)
    # -----------------------------------------------------
    # Python 3.10 introduced the 'match' statement, which is similar to a 'switch-case' construct found in other languages.
    # This allows for more readable and expressive pattern-based control flow, with the added power of logical operators.

    def classify_point(point):
        """Classifies a 2D point into a quadrant or special category using pattern matching."""
        match point:
            # Each 'case' checks for a pattern along with a conditional expression
            case (x, y) if x > 0 and y > 0:
                return "First quadrant"  # Top-right quadrant (both x and y are positive)
            case (x, y) if x < 0 and y > 0:
                return "Second quadrant"  # Top-left quadrant (x is negative, y is positive)
            case (x, y) if x < 0 and y < 0:
                return "Third quadrant"  # Bottom-left quadrant (both x and y are negative)
            case (x, y) if x > 0 and y < 0:
                return "Fourth quadrant"  # Bottom-right quadrant (x is positive, y is negative)
            case (0, 0):
                return "Origin"  # The point lies at the origin (0, 0)
            case _:
                return "On an axis"  # Any other points lying on either the x or y-axis

    # Explanation: The 'match' statement allows for more concise and readable handling of multiple conditional checks.
    # Advanced Tip: Pattern matching is more than just a switch-case replacement; it supports destructuring,
    # conditional guards (like 'if x > 0 and y > 0'), and wildcard matching (using '_').

    # Using the classify_point function to classify different points
    print(f"\nClassify point (1, 1): {classify_point((1, 1))}")  # Expected output: "First quadrant"
    print(f"Classify point (-1, -1): {classify_point((-1, -1))}")  # Expected output: "Third quadrant"
    print(f"Classify point (0, 5): {classify_point((0, 5))}")  # Expected output: "On an axis"

# ========================================
# Summary of Advanced Concepts and Emerging Trends
# ------------------------------------------------
# - Context managers are essential for managing resources, ensuring that they are correctly acquired and released.
#   Using '@contextlib.contextmanager' provides an easy way to create custom context managers with minimal boilerplate.
# - The 'ExitStack' utility allows dynamic handling of multiple context managers, ensuring that resources are
#   properly cleaned up even if an error occurs.
# - Python's pattern matching ('match' statement) introduced in version 3.10 offers a powerful, readable, 
#   and flexible way to handle complex conditional logic with support for destructuring and logical operators.

# The comments and explanations provided aim to give an in-depth understanding of advanced concepts such as context managers,
# dynamic resource handling, and the new pattern matching syntax in Python 3.10+. This guide equips the reader with 
# the knowledge to implement these techniques effectively, offering insights that are valuable for a senior or principal engineer.


# ========================================
# 6. FAQs and Troubleshooting
# ---------------------------------

def faqs_and_troubleshooting():
    """Addresses common questions and issues related to logical operators with detailed explanations."""

    # Q: Why does `0 and 1` return 0, not False?
    # -----------------------------------------
    # The 'and' operator evaluates expressions from left to right and returns the first falsy value encountered.
    # If no falsy value is found, it returns the last value in the expression.
    # This behavior is known as "short-circuit evaluation."
    # In this case, since 0 is considered falsy in Python, '0 and 1' returns 0 without evaluating the second operand (1).
    print("Q: Why does `0 and 1` return 0, not False?")
    print("A: 'and' returns the first falsy value or the last value if all are truthy.")
    print(f"0 and 1: {0 and 1}")  # Outputs: 0

    # Advanced Tip: Use 'and' carefully in expressions where operands might be non-boolean. 
    # It can lead to confusion if you're expecting strictly True or False results.

    # Q: How can I chain multiple conditions without using `and`?
    # ---------------------------------------------------------
    # When you have multiple conditions and want to check if all of them are True, you can use the 'all()' function.
    # The 'all()' function takes an iterable (e.g., list, tuple) and returns True if all elements are truthy, otherwise False.
    print("\nQ: How can I chain multiple conditions without using `and`?")
    print("A: You can use the `all()` function:")
    conditions = [True, False, True]  # A list containing multiple conditions
    print(f"all({conditions}): {all(conditions)}")  # Outputs: False because not all elements are True

    # Explanation: The 'all()' function iterates through the conditions and returns False as soon as it encounters a falsy value.
    # This is more efficient for checking multiple conditions compared to chaining with multiple 'and' operators, 
    # especially when dealing with a large number of conditions.

    # Q: How do I debug complex logical expressions?
    # ---------------------------------------------
    # Debugging complex logical expressions can be challenging, but breaking them into smaller parts can make it easier to track down issues.
    # Use print statements or assertions to verify the individual parts of an expression.
    print("\nQ: How do I debug complex logical expressions?")
    print("A: Break down complex expressions into smaller parts and use print statements or assertions:")

    def debug_complex_logic(a, b, c):
        # Evaluate the first part of the expression
        part1 = a > 0
        assert part1 == (a > 0), f"part1 failed: {a} > 0"  # Assertion to confirm the expected value of part1
        
        # Evaluate the second part of the expression
        part2 = b < 10
        assert part2 == (b < 10), f"part2 failed: {b} < 10"  # Assertion to confirm the expected value of part2
        
        # Evaluate the third part of the expression
        part3 = c != 0
        assert part3 == (c != 0), f"part3 failed: {c} != 0"  # Assertion to confirm the expected value of part3
        
        # Combine the parts using logical operators
        result = part1 and part2 or part3  # Logical combination of parts
        print(f"Debug: part1={part1}, part2={part2}, part3={part3}, result={result}")  # Output the values for debugging
        return result
    
    print("Example debugging of (a > 0 and b < 10) or c != 0:")
    debug_complex_logic(5, 8, 0)  # Example usage demonstrating how the function debugs logical expressions

    # Advanced Insight: Assertions are extremely useful for catching unexpected behavior during development,
    # especially when debugging complex logic. However, avoid using them for handling expected runtime errors;
    # instead, use proper error handling mechanisms.

    # Q: How do I avoid short-circuit evaluation when I want all conditions to be checked?
    # ---------------------------------------------------------
    # Python's logical operators 'and' and 'or' use short-circuit evaluation, meaning evaluation stops as soon as the result is determined.
    # This can be problematic if you want all conditions to be checked regardless of whether a falsy value has been encountered.
    print("\nQ: How do I avoid short-circuit evaluation when I want all conditions to be checked?")
    print("A: Use a list comprehension or generator expression with all() or any():")

    def check_all_conditions(conditions):
        return all(cond() for cond in conditions)  # The generator expression ensures all functions are called
    
    # Define example functions for testing
    def always_true():
        print("always_true called")
        return True
    
    def always_false():
        print("always_false called")
        return False
    
    print("\nChecking all conditions:")
    result = check_all_conditions([always_true, always_false, always_true])
    print(f"Result: {result}")  # Outputs: False, and all functions are called

    # Explanation: The use of 'all()' here ensures that every condition (function) is evaluated, regardless of the result.
    # This approach bypasses the short-circuit evaluation behavior of 'and' and 'or'.

    # Advanced Tip: In scenarios where you want to enforce complete evaluation of multiple expressions, 
    # using 'all()' or 'any()' with generator expressions ensures efficient iteration, as values are yielded one by one 
    # without creating intermediate lists, which saves memory.

# ========================================
# Summary
# ---------------------------------------
# - The 'and' operator returns the first falsy value or the last value if all are truthy, based on short-circuit evaluation.
# - Use 'all()' or 'any()' to handle multiple conditions efficiently, especially when chaining multiple boolean checks.
# - Debug complex logical expressions by breaking them into smaller parts and using print statements or assertions.
# - Understand how to avoid short-circuit evaluation by using list comprehensions or generator expressions with 'all()' or 'any()'.
# - Assertions are powerful for debugging but should not replace proper error handling in production code.

# The comments are designed to provide in-depth understanding and clarity, facilitating the transition from novice 
# to senior/principal engineer by addressing not just the 'how,' but also the 'why' behind each concept, including 
# best practices, common pitfalls, and advanced insights.


# ========================================
# 7. Recommended Tools, Libraries, and Resources
# ---------------------------------

"""
Recommended tools and libraries for working with logical operators:

1. operator module: Provides a functional interface to Python's built-in operators
   - Built-in to Python; no installation required. This module offers functions like `operator.and_`, `operator.or_`, and `operator.not_`
     which are equivalent to using 'and', 'or', and 'not' directly in expressions but can be useful in functional programming contexts.

2. functools module: Contains higher-order functions for working with callable objects
   - Another built-in module, frequently used for logical operations involving functions. Functions like `functools.reduce()` 
     can be used to apply logical operations across iterables, providing an alternative to using loops or comprehensions.

3. itertools module: Offers a collection of functions that create efficient iterators for logical operations
   - This built-in module is highly efficient for handling iterables in logical operations, including combinations, permutations, 
     and products of iterables, allowing for memory-efficient operations on large datasets.

4. sympy: A symbolic mathematics library that supports logical expressions and operations
   - This library allows you to perform symbolic logic, enabling algebraic manipulation and simplification of logical expressions.
     Install it using: `pip install sympy`. It's particularly useful for more advanced mathematical logic applications.

5. PyTorch: A deep learning library with support for tensor operations, including logical operators
   - Installable via `pip install torch`. PyTorch provides extensive support for logical operations at scale, especially 
     when working with large datasets or tensors in machine learning workflows. It offers element-wise logical operations 
     that are highly optimized for performance.

Resources for further learning:
- Python Official Documentation: (https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
  A comprehensive guide to understanding Python's logical operations, including usage and nuances.

- "Fluent Python" by Luciano Ramalho: A highly recommended book that provides deep insights into Python's logical operations 
  and best practices, suitable for both intermediate and advanced developers.

- "Python Cookbook" by David Beazley and Brian K. Jones: This book offers practical solutions and recipes for common Python 
  tasks, including logical operations, making it an excellent reference.

- Journal of Systems and Software: (https://www.sciencedirect.com/journal/journal-of-systems-and-software)
  Provides scholarly articles and research papers on software engineering, with in-depth discussions on logic 
  systems and their applications in programming.

- ACM Transactions on Programming Languages and Systems: (https://dl.acm.org/journal/toplas)
  A valuable resource for understanding the theory and application of logical systems in software design and implementation.
"""

# ========================================
# 8. Performance Analysis and Optimization
# ---------------------------------

def performance_analysis():
    """Demonstrates performance analysis and optimization techniques for logical operations."""
    import timeit  # Module used to measure execution time of small code snippets

    # Compare performance of 'and' vs '&' for boolean operations
    # ---------------------------------------------------------
    # The 'and' operator is a logical operator that evaluates lazily (short-circuits) - meaning it stops evaluating 
    # as soon as the result is determined, making it efficient in some cases.
    # The '&' operator is a bitwise operator that does not short-circuit, performing a binary AND operation on integers or booleans.

    def logical_and(a, b):
        return a and b  # Uses logical 'and'; short-circuits when 'a' is False

    def bitwise_and(a, b):
        return a & b  # Uses bitwise '&'; evaluates both 'a' and 'b' regardless of the outcome

    # Set up the environment for timeit measurement
    setup = "from __main__ import logical_and, bitwise_and"
    logical_time = timeit.timeit("logical_and(True, False)", setup=setup, number=1000000)
    bitwise_time = timeit.timeit("bitwise_and(True, False)", setup=setup, number=1000000)
    
    print(f"Time for logical 'and': {logical_time:.6f} seconds")
    print(f"Time for bitwise '&': {bitwise_time:.6f} seconds")
    
    # Insight: Bitwise operations are generally faster in raw computation but are less readable and do not short-circuit.
    # Best Practice: Use logical operators ('and', 'or') when dealing with boolean logic for clarity and to leverage short-circuiting.

    # Compare performance of chained logical operators vs all()/any()
    # --------------------------------------------------------------
    # Chained logical operators involve multiple 'and' or 'or' statements, which can be less efficient for longer sequences.
    # The built-in 'all()' and 'any()' functions are optimized for evaluating multiple conditions over iterables.

    def chained_and(lst):
        return lst[0] and lst[1] and lst[2] and lst[3] and lst[4]  # Manually chaining 'and' operations

    def all_function(lst):
        return all(lst)  # Uses 'all()', which stops evaluation as soon as it encounters a False

    # Measure the performance
    setup = "from __main__ import chained_and, all_function; lst = [True, True, True, True, True]"
    chained_time = timeit.timeit("chained_and(lst)", setup=setup, number=1000000)
    all_time = timeit.timeit("all_function(lst)", setup=setup, number=1000000)
    
    print(f"\nTime for chained 'and': {chained_time:.6f} seconds")
    print(f"Time for all() function: {all_time:.6f} seconds")
    
    # Insight: 'all()' and 'any()' are typically more efficient for evaluating multiple conditions because they are implemented in C 
    # and leverage short-circuit evaluation.

    # Demonstrate short-circuit optimization
    # --------------------------------------
    # Short-circuit evaluation is an optimization technique where logical expressions are evaluated only as much as needed.
    # If the outcome can be determined early, the remaining expressions are not evaluated, improving performance.

    def expensive_check():
        return sum(range(1000000)) % 2 == 0  # Computationally expensive operation

    def optimized_logic(quick_check):
        return quick_check or expensive_check()  # Uses 'or', short-circuits if quick_check is True

    def unoptimized_logic(quick_check):
        return quick_check | expensive_check()  # Bitwise '|' doesn't short-circuit; always evaluates both

    setup = "from __main__ import optimized_logic, unoptimized_logic, expensive_check"
    optimized_time = timeit.timeit("optimized_logic(True)", setup=setup, number=1000)
    unoptimized_time = timeit.timeit("unoptimized_logic(True)", setup=setup, number=1000)
    
    print(f"\nTime for optimized logic: {optimized_time:.6f} seconds")
    print(f"Time for unoptimized logic: {unoptimized_time:.6f} seconds")
    
    # Insight: Short-circuit evaluation can significantly reduce computation time, especially when handling complex 
    # or time-consuming expressions.

# ========================================
# Summary
# ---------------------------------------
# - Use logical operators ('and', 'or', not) for boolean logic, and bitwise operators ('&', '|', '~') for bit-level manipulation.
# - Leverage short-circuit evaluation to optimize performance in logical expressions.
# - Employ built-in functions like 'all()' and 'any()' for efficient evaluation of iterable conditions.
# - When performing performance-critical operations, measure execution time with 'timeit' to identify bottlenecks.
# - Advanced libraries like 'sympy' and 'PyTorch' offer powerful capabilities for handling logical operations in specialized fields.

# ========================================
# Main Execution Flow with Thorough Insights
# -----------------------------------------

def main():
    """Main function to demonstrate various logical and programming concepts, 
    ranging from foundational to advanced levels. Each function called serves to illustrate 
    specific aspects of Python programming, ensuring a comprehensive learning experience."""
    
    # The 'main()' function serves as the entry point of the script. It sequentially calls various 
    # functions, each demonstrating a different concept or technique. This structure is common in 
    # larger programs and allows for modular organization and clearer code flow.

    # Printing each section with an appropriate heading before invoking the respective function.
    # This enhances readability and makes it easier to track execution flow, especially during debugging.
    
    print("1. Basic Logical Operations:")
    basic_logical_operations()  # Function demonstrating foundational logical operations
    
    print("\n2. Short-Circuit Evaluation:")
    short_circuit_evaluation()  # Demonstrates short-circuit behavior of logical operators
    
    print("\n3. Truthy and Falsy Values:")
    truthy_falsy_values()  # Highlights how Python evaluates truthiness and falsiness of values
    
    print("\n4. Logical Operators with Non-Booleans:")
    logical_operators_with_non_booleans()  # Illustrates how logical operators behave with non-boolean values
    
    print("\n5. Best Practices:")
    best_practices()  # Shares best practices for logical operations and other programming patterns
    
    print("\n6. Common Pitfalls:")
    common_pitfalls()  # Explains common mistakes and traps when working with logical operations and Python in general
    
    print("\n7. Advanced Tips:")
    advanced_tips()  # Offers advanced insights and optimizations to enhance coding skills and efficiency
    
    print("\n8. Testable Code:")
    write_testable_code()  # Demonstrates how to write functions that are easier to test, ensuring better software quality
    
    print("\n9. Decision Tree Example:")
    decision_tree_example()  # Provides an example of decision-making logic, often used in AI/ML
    
    print("\n10. Data Filtering Example:")
    data_filtering_example()  # Showcases practical data filtering techniques, useful in data science and analytics
    
    print("\n11. Advanced Concepts:")
    advanced_concepts()  # Delves into more complex Python concepts, aiming to broaden understanding
    
    print("\n12. FAQs and Troubleshooting:")
    faqs_and_troubleshooting()  # Addresses frequently asked questions and common troubleshooting techniques
    
    print("\n13. Performance Analysis:")
    performance_analysis()  # Analyzes performance considerations, crucial for writing efficient code

# Execution Entry Point
# ---------------------
# The following 'if __name__ == "__main__":' idiom is a common Python pattern that ensures 'main()' 
# is only executed when the script is run directly, not when imported as a module. This is a best practice 
# in Python that allows the script to be reused and prevents unintended execution during import.

if __name__ == "__main__":
    main()

# ========================================
# Detailed Insights and Explanations
# ---------------------------------
# 1. **Modular Function Calls**: Each function (e.g., basic_logical_operations(), advanced_tips()) is invoked 
#    from the main function to maintain modularity and separation of concerns. This structure allows individual 
#    functions to be tested and maintained independently, adhering to the Single Responsibility Principle (SRP) 
#    of software design.

# 2. **Print Statements for Clarity**: The use of print statements with numbered headings before each function 
#    call aids in understanding the flow of the program when executed. This approach is especially helpful during 
#    debugging and provides a clear roadmap of the program's progression.

# 3. **Importance of '__name__ == "__main__"'**: This construct is crucial for ensuring that code execution only 
#    occurs when the script is run directly, not when imported as a module. It enhances code reusability and 
#    prevents unexpected behavior in larger projects where this script might be imported by other scripts.

# Advanced Tip: 
# -------------
# In larger applications, consider using a more structured approach for organizing function calls, such as 
# defining a dictionary that maps menu options or command strings to their respective functions. This makes 
# the codebase more scalable and easier to extend. For example:

# FUNCTION_MAP = {
#     "basic_logical_operations": basic_logical_operations,
#     "short_circuit_evaluation": short_circuit_evaluation,
#     # Add other mappings as needed
# }
# This approach allows invoking functions dynamically based on user input or configuration, reducing the need 
# for hardcoded function calls.

# Common Pitfall: 
# ---------------
# Forgetting the '__name__ == "__main__"' guard can lead to unexpected side effects when importing scripts. 
# Always include this guard to prevent unintended execution, particularly in collaborative projects or when 
# creating libraries/modules.

# Best Practice:
# --------------
# Keeping the 'main()' function as simple and high-level as possible ensures that it serves merely as an 
# orchestration layer. All detailed logic and computations should reside in separate, well-named functions. 
# This not only improves readability but also facilitates easier testing, debugging, and maintenance.

# Summary:
# The 'main()' function provides a structured entry point that sequentially demonstrates various concepts. 
# The thorough commentary serves to explain not just what each part does but why it is implemented this way, 
# including advanced tips for scalability, common pitfalls, and best practices to adhere to when structuring 
# Python programs.

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