"""
Control Structures - if-elif-else statements - in the Python Programming Language
=================================================================================

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
if-elif-else statements in Python are fundamental control structures that allow 
for conditional execution of code. They provide a way to make decisions in 
programs, executing different blocks of code based on specified conditions.

Historical context:
- Conditional statements have been a core feature of programming languages 
  since the early days of computing.
- Python's if-elif-else structure was introduced with the language's creation 
  by Guido van Rossum in the late 1980s.
- The 'elif' keyword, short for 'else if', was included to improve readability 
  and reduce nesting compared to languages that use 'else if'.

Relevance in modern software development:
- Essential for implementing decision-making logic in programs.
- Crucial for creating responsive and interactive applications.
- Fundamental in implementing complex algorithms and control flows.

Comparison to other languages:
- Python's if-elif-else structure is similar to many other languages but with 
  some unique syntax, such as using colons and indentation instead of brackets.
- The 'elif' keyword is relatively unique to Python, with most other languages 
  using 'else if' or similar constructs.

2. Syntax, Key Concepts, and Code Examples
==========================================
Let's explore the syntax and key concepts of if-elif-else statements with 
progressively complex examples:
"""

import random
import asyncio
import time
import unittest
from typing import List, Tuple, Callable

def basic_if_statement():
    """
    Demonstrates a basic if statement.
    """
    x = 10
    if x > 5:
        print("x is greater than 5")

def if_else_statement():
    """
    Demonstrates an if-else statement.
    """
    y = 3
    if y > 5:
        print("y is greater than 5")
    else:
        print("y is not greater than 5")

def if_elif_else_statement():
    """
    Demonstrates an if-elif-else statement.
    """
    z = 5
    if z > 5:
        print("z is greater than 5")
    elif z < 5:
        print("z is less than 5")
    else:
        print("z is equal to 5")

def nested_if_statements():
    """
    Demonstrates nested if statements.
    """
    a = 10
    b = 20
    if a > 5:
        if b > 15:
            print("Both conditions are true")
        else:
            print("Only the first condition is true")
    else:
        print("The first condition is false")

def multiple_conditions():
    """
    Demonstrates the use of multiple conditions in if statements.
    """
    age = 25
    has_license = True
    if age >= 18 and has_license:
        print("You can drive")
    elif age >= 18 and not has_license:
        print("You need to get a license")
    else:
        print("You're too young to drive")

def ternary_operator():
    """
    Demonstrates the use of the ternary operator.
    """
    x = 10
    result = "Even" if x % 2 == 0 else "Odd"
    print(f"{x} is {result}")

def conditional_expression():
    """
    Demonstrates a more complex conditional expression.
    """
    score = 85
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    print(f"Score: {score}, Grade: {grade}")

def short_circuit_evaluation():
    """
    Demonstrates short-circuit evaluation in conditional statements.
    """
    def check_positive(x):
        print(f"Checking if {x} is positive")
        return x > 0

    a, b = 5, -3
    if check_positive(a) and check_positive(b):
        print("Both numbers are positive")
    else:
        print("At least one number is not positive")

async def async_conditional_example():
    """
    Demonstrates the use of conditional statements in an asynchronous context.
    """
    async def fetch_data(id: int) -> dict:
        await asyncio.sleep(1)  # Simulating an API call
        return {"id": id, "value": random.randint(1, 100)}

    data = await fetch_data(1)
    if data["value"] > 50:
        print("High value")
    elif 20 <= data["value"] <= 50:
        print("Medium value")
    else:
        print("Low value")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
=====================================================

Best Practices:
1. Keep conditions simple and readable.
2. Use elif for multiple conditions instead of nested if statements when possible.
3. Consider using a dictionary or match statement (Python 3.10+) for complex 
   branching logic.
4. Use descriptive variable names to make conditions self-explanatory.
5. Avoid deep nesting of conditional statements.

Common Pitfalls:
1. Forgetting to use elif and writing multiple if statements instead.
2. Using = (assignment) instead of == (comparison) in conditions.
3. Not considering all possible cases, leading to unexpected behavior.
4. Overcomplicating conditions, making them hard to understand and maintain.

Advanced Tips:
1. Use any() and all() functions for complex boolean logic:
"""

def advanced_boolean_logic():
    numbers = [1, 2, 3, 4, 5]
    if any(num > 10 for num in numbers):
        print("At least one number is greater than 10")
    if all(num < 10 for num in numbers):
        print("All numbers are less than 10")

"""
2. Utilize the walrus operator (:=) for assignment expressions (Python 3.8+):
"""

def walrus_operator_example():
    numbers = []
    while (n := len(numbers)) < 5:
        numbers.append(n)
    print(numbers)

"""
3. Implement a custom switch-case using dictionaries:
"""

def dict_based_switch_case(day: str) -> str:
    return {
        "monday": "Start of the work week",
        "friday": "TGIF!",
        "saturday": "Weekend!",
        "sunday": "Weekend!"
    }.get(day.lower(), "Regular day")

"""
4. Use context managers with conditional logic:
"""

def conditional_context_manager():
    class ConditionalContext:
        def __init__(self, condition):
            self.condition = condition

        def __enter__(self):
            print("Entering context")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print("Exiting context")
            if exc_type is not None:
                print(f"An exception occurred: {exc_type}")
            return self.condition

    risky_operation = True
    with ConditionalContext(risky_operation):
        if risky_operation:
            raise ValueError("Something went wrong")
        print("Operation successful")

"""
5. Implement guard clauses for early returns:
"""

def process_data(data: List[int]) -> int:
    if not data:
        return 0
    if len(data) == 1:
        return data[0]
    return sum(data) // len(data)

"""
4. Integration and Real-World Applications
==========================================
if-elif-else statements are fundamental in various real-world applications:

1. User Authentication Systems:
   - Checking user credentials and permissions.
2. Data Validation and Error Handling:
   - Validating input data and handling different error scenarios.
3. Game Development:
   - Implementing game logic and state transitions.
4. Financial Systems:
   - Calculating taxes, interest rates, or loan eligibility.
5. Machine Learning:
   - Implementing decision trees or rule-based systems.

Example: Simple rule-based chatbot
"""

def simple_chatbot():
    greetings = ["hello", "hi", "hey"]
    farewells = ["bye", "goodbye", "see you"]

    while True:
        user_input = input("You: ").lower()
        if user_input in greetings:
            print("Bot: Hello! How can I help you today?")
        elif user_input in farewells:
            print("Bot: Goodbye! Have a great day!")
            break
        elif "weather" in user_input:
            print("Bot: I'm sorry, I don't have access to weather information.")
        elif "name" in user_input:
            print("Bot: My name is ChatBot. Nice to meet you!")
        else:
            print("Bot: I'm not sure how to respond to that. Can you please rephrase?")

"""
5. Advanced Concepts and Emerging Trends
========================================
1. Pattern Matching (Python 3.10+):
   - Using match-case statements for more expressive conditional logic.
2. Adaptive Decision Making:
   - Implementing machine learning models for dynamic decision-making.
3. Fuzzy Logic:
   - Extending traditional boolean logic to handle degrees of truth.
4. Quantum Computing:
   - Exploring quantum superposition for parallel evaluation of conditions.
5. Natural Language Processing:
   - Using advanced NLP techniques for more sophisticated chatbots and 
     language understanding systems.

Example: Pattern matching (Python 3.10+)
"""

def pattern_matching_example(value):
    match value:
        case int(x) if x < 0:
            print(f"{x} is a negative integer")
        case int(x):
            print(f"{x} is a positive integer")
        case str(s) if s.islower():
            print(f"{s} is a lowercase string")
        case str(s):
            print(f"{s} is a string")
        case _:
            print("Unknown type")

"""
6. FAQs and Troubleshooting
===========================
Q: Why use elif instead of multiple if statements?
A: elif is more efficient as it stops checking conditions once a true condition 
   is found, whereas multiple if statements would check all conditions.

Q: How can I simplify a long chain of if-elif-else statements?
A: Consider using a dictionary-based approach, a match statement (Python 3.10+), 
   or refactoring the logic into smaller functions.

Q: Is there a limit to the number of elif statements I can use?
A: While there's no hard limit, too many elif statements can make code harder 
   to read and maintain. Consider alternative approaches for complex branching.

Troubleshooting:

1. Unexpected behavior due to incorrect indentation:
"""

def troubleshoot_indentation():
    x = 5
    if x > 0:
        print("x is positive")
        print("This will always print regardless of x")  # Incorrect indentation
    else:
        print("x is not positive")

"""
2. Misuse of assignment (=) instead of comparison (==):
"""

def troubleshoot_assignment():
    x = 5
    if x == 10:  # This will raise a SyntaxError
        print("x is 10")

"""
3. Forgetting to handle all cases:
"""

def troubleshoot_missing_cases(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    # Missing case: x == 0

"""
7. Recommended Tools, Libraries, and Resources
==============================================
Tools and Libraries:
1. pylint: A static code analysis tool that can help identify issues with 
   conditional statements
   (https://www.pylint.org/)
2. coverage.py: A tool for measuring code coverage of Python programs
   (https://coverage.readthedocs.io/)
3. pytest: A testing framework that simplifies writing and running tests for 
   conditional logic
   (https://docs.pytest.org/)
4. Black: An uncompromising code formatter that ensures consistent styling 
   for conditional statements
   (https://black.readthedocs.io/)

Resources:
1. Python Official Documentation on Control Flow:
   https://docs.python.org/3/tutorial/controlflow.html
2. "Fluent Python" by Luciano Ramalho (Book)
3. "Clean Code: A Handbook of Agile Software Craftsmanship" by Robert C. Martin (Book)
4. Real Python Tutorial on Conditional Statements:
   https://realpython.com/python-conditional-statements/

8. Performance Analysis and Optimization
========================================
Let's analyze the performance of different conditional structures:
"""

import timeit

def performance_analysis():
    def if_else_chain(x):
        if x < 0:
            return "negative"
        elif x == 0:
            return "zero"
        else:
            return "positive"

    def dict_based(x):
        return {
            x < 0: "negative",
            x == 0: "zero",
            x > 0: "positive"
        }[True]

    def match_case(x):
        match x:
            case int(n) if n < 0:
                return "negative"
            case 0:
                return "zero"
            case int(n) if n > 0:
                return "positive"

    setup = "from __main__ import if_else_chain, dict_based, match_case"
    
    if_else_time = timeit.timeit("if_else_chain(5)", setup=setup, number=1000000)
    dict_time = timeit.timeit("dict_based(5)", setup=setup, number=1000000)
    match_time = timeit.timeit("match_case(5)", setup=setup, number=1000000)
    
    print(f"if-else chain time: {if_else_time:.6f} seconds")
    print(f"Dictionary-based time: {dict_time:.6f} seconds")
    print(f"match-case time: {match_time:.6f} seconds")

"""
Optimization strategies:
1. For a small number of conditions, if-elif-else is generally the most readable 
   and efficient.
2. For a large number of conditions, consider using a dictionary-based approach 
   or match-case statement.
3. Use short-circuit evaluation to your advantage by placing more likely 
   conditions first in compound conditions.
4. Consider using lookup tables for complex mappings instead of long chains of 
   conditions.

Example of optimizing a complex conditional structure:
"""

def optimize_complex_conditional(value: int) -> str:
    if 0 <= value < 10:
        if value % 2 == 0:
            return "Small Even"
        else:
            return "Small Odd"
    elif 10 <= value < 100:
        if value % 2 == 0:
            return "Medium Even"
        else:
            return "Medium Odd"
    else:
        if value % 2 == 0:
            return "Large Even"
        else:
            return "Large Odd"

def optimized_complex_conditional(value: int) -> str:
    size_category = "Small" if value < 10 else "Medium" if value < 100 else "Large"
    parity = "Even" if value % 2 == 0 else "Odd"
    return f"{size_category} {parity}"

def benchmark_conditional_optimization():
    """
    Benchmarks the original and optimized complex conditional functions.
    """
    setup = """
from __main__ import optimize_complex_conditional, optimized_complex_conditional
import random
values = [random.randint(0, 1000) for _ in range(1000)]
    """
    
    original_time = timeit.timeit('for v in values: optimize_complex_conditional(v)', setup=setup, number=1000)
    optimized_time = timeit.timeit('for v in values: optimized_complex_conditional(v)', setup=setup, number=1000)
    
    print(f"Original function time: {original_time:.6f} seconds")
    print(f"Optimized function time: {optimized_time:.6f} seconds")
    print(f"Speedup: {original_time / optimized_time:.2f}x")

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
- The relevance to if-elif-else statements in Python
- The depth of explanation required for expert-level understanding
- The practical applications of the concept in real-world scenarios
- The potential impact on performance and optimization

Your contributions will help keep this note sheet up-to-date and valuable for 
Python developers at all levels. Thank you for your interest in improving this 
resource!
"""

# Unit tests for the conditional functions
class TestConditionalFunctions(unittest.TestCase):
    def test_basic_if_statement(self):
        # We can't directly test print output, so we'll modify the function to return a value
        def modified_basic_if_statement(x):
            if x > 5:
                return "x is greater than 5"
            return "x is not greater than 5"
        
        self.assertEqual(modified_basic_if_statement(10), "x is greater than 5")
        self.assertEqual(modified_basic_if_statement(3), "x is not greater than 5")

    def test_if_else_statement(self):
        def modified_if_else_statement(y):
            if y > 5:
                return "y is greater than 5"
            else:
                return "y is not greater than 5"
        
        self.assertEqual(modified_if_else_statement(10), "y is greater than 5")
        self.assertEqual(modified_if_else_statement(3), "y is not greater than 5")

    def test_if_elif_else_statement(self):
        def modified_if_elif_else_statement(z):
            if z > 5:
                return "z is greater than 5"
            elif z < 5:
                return "z is less than 5"
            else:
                return "z is equal to 5"
        
        self.assertEqual(modified_if_elif_else_statement(10), "z is greater than 5")
        self.assertEqual(modified_if_elif_else_statement(3), "z is less than 5")
        self.assertEqual(modified_if_elif_else_statement(5), "z is equal to 5")

    def test_dict_based_switch_case(self):
        self.assertEqual(dict_based_switch_case("monday"), "Start of the work week")
        self.assertEqual(dict_based_switch_case("friday"), "TGIF!")
        self.assertEqual(dict_based_switch_case("tuesday"), "Regular day")

    def test_process_data(self):
        self.assertEqual(process_data([]), 0)
        self.assertEqual(process_data([5]), 5)
        self.assertEqual(process_data([1, 2, 3, 4, 5]), 3)

    def test_optimized_complex_conditional(self):
        self.assertEqual(optimized_complex_conditional(5), "Small Odd")
        self.assertEqual(optimized_complex_conditional(20), "Medium Even")
        self.assertEqual(optimized_complex_conditional(150), "Large Even")

# This is the main function that demonstrates the usage of if-elif-else statements
def main():
    print("Control Structures - if-elif-else statements in Python - Expert-Level Note Sheet")
    print("=============================================================================")
    
    basic_if_statement()
    print("\n" + "="*50 + "\n")
    
    if_else_statement()
    print("\n" + "="*50 + "\n")
    
    if_elif_else_statement()
    print("\n" + "="*50 + "\n")
    
    nested_if_statements()
    print("\n" + "="*50 + "\n")
    
    multiple_conditions()
    print("\n" + "="*50 + "\n")
    
    ternary_operator()
    print("\n" + "="*50 + "\n")
    
    conditional_expression()
    print("\n" + "="*50 + "\n")
    
    short_circuit_evaluation()
    print("\n" + "="*50 + "\n")
    
    asyncio.run(async_conditional_example())
    print("\n" + "="*50 + "\n")
    
    advanced_boolean_logic()
    print("\n" + "="*50 + "\n")
    
    walrus_operator_example()
    print("\n" + "="*50 + "\n")
    
    print("Dict-based switch case:")
    print(dict_based_switch_case("monday"))
    print(dict_based_switch_case("saturday"))
    print("\n" + "="*50 + "\n")
    
    print("Conditional context manager:")
    conditional_context_manager()
    print("\n" + "="*50 + "\n")
    
    print("Processing data:")
    print(process_data([1, 2, 3, 4, 5]))
    print("\n" + "="*50 + "\n")
    
    print("Simple chatbot (type 'bye' to exit):")
    simple_chatbot()
    print("\n" + "="*50 + "\n")
    
    print("Pattern matching example:")
    pattern_matching_example(42)
    pattern_matching_example("hello")
    pattern_matching_example(3.14)
    print("\n" + "="*50 + "\n")
    
    print("Troubleshooting examples:")
    troubleshoot_indentation()
    # Uncomment to see the SyntaxError:
    # troubleshoot_assignment()
    print("\n" + "="*50 + "\n")
    
    print("Performance Analysis:")
    performance_analysis()
    print("\n" + "="*50 + "\n")
    
    print("Conditional Optimization Benchmark:")
    benchmark_conditional_optimization()
    print("\n" + "="*50 + "\n")
    
    print("Running Unit Tests:")
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main()