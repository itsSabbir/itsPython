"""
Operators and Expressions - Operator precedence - in the Python Programming Language
====================================================================================

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
Operator precedence in Python defines the order in which operators are evaluated 
in an expression. It is a fundamental concept in programming languages, ensuring 
that expressions are interpreted consistently and as intended by the programmer.

Historical context:
- The concept of operator precedence dates back to the early days of programming 
  and mathematics.
- Python's operator precedence rules were established with the language's 
  creation by Guido van Rossum in the late 1980s.
- The precedence rules in Python have remained largely consistent throughout its 
  versions, with only minor additions for new operators.

Relevance in modern software development:
- Crucial for writing correct and predictable expressions in code.
- Essential for understanding and debugging complex expressions.
- Important for optimizing code readability and maintainability.

Comparison to other languages:
- Python's precedence rules are similar to those in C and Java, making it 
  familiar to developers coming from these backgrounds.
- Some unique aspects exist, such as the precedence of the 'not in' operator.

2. Syntax, Key Concepts, and Code Examples
==========================================
Python's operator precedence is defined in a specific order, from highest to 
lowest precedence. Let's explore this with examples:
"""

import math
import operator
import dis
import timeit
import unittest
from typing import List, Tuple, Callable

def parentheses_demo():
    """
    Demonstrates the highest precedence of parentheses.
    """
    result1 = 2 + 3 * 4  # 14
    result2 = (2 + 3) * 4  # 20
    print(f"2 + 3 * 4 = {result1}")
    print(f"(2 + 3) * 4 = {result2}")

def exponentiation_demo():
    """
    Demonstrates the precedence of exponentiation.
    """
    result1 = 2 ** 3 ** 2  # 512 (right-associative)
    result2 = (2 ** 3) ** 2  # 64
    print(f"2 ** 3 ** 2 = {result1}")
    print(f"(2 ** 3) ** 2 = {result2}")

def unary_operators_demo():
    """
    Demonstrates the precedence of unary operators.
    """
    x = 5
    result1 = -x ** 2  # -25
    result2 = (-x) ** 2  # 25
    print(f"-x ** 2 = {result1}")
    print(f"(-x) ** 2 = {result2}")

def multiplication_division_demo():
    """
    Demonstrates the precedence of multiplication and division.
    """
    result1 = 2 + 3 * 4 / 2  # 8.0
    result2 = (2 + 3) * 4 / 2  # 10.0
    print(f"2 + 3 * 4 / 2 = {result1}")
    print(f"(2 + 3) * 4 / 2 = {result2}")

def addition_subtraction_demo():
    """
    Demonstrates the precedence of addition and subtraction.
    """
    result = 10 - 5 + 3  # 8
    print(f"10 - 5 + 3 = {result}")

def comparison_operators_demo():
    """
    Demonstrates the precedence of comparison operators.
    """
    result1 = 5 > 3 < 4  # True
    result2 = (5 > 3) and (3 < 4)  # True
    print(f"5 > 3 < 4 = {result1}")
    print(f"(5 > 3) and (3 < 4) = {result2}")

def logical_operators_demo():
    """
    Demonstrates the precedence of logical operators.
    """
    result1 = True or False and False  # True
    result2 = (True or False) and False  # False
    print(f"True or False and False = {result1}")
    print(f"(True or False) and False = {result2}")

def assignment_operators_demo():
    """
    Demonstrates the lowest precedence of assignment operators.
    """
    x = y = 5
    z = x + y == 10  # True
    print(f"x = y = 5; z = x + y == 10; z = {z}")

def complex_expression_demo():
    """
    Demonstrates a complex expression involving multiple operators.
    """
    a, b, c = 2, 3, 4
    result = a + b * c ** 2 - (a + b) * c // 2
    print(f"a + b * c ** 2 - (a + b) * c // 2 = {result}")
    # Equivalent to: 2 + 3 * 4 ** 2 - (2 + 3) * 4 // 2
    # Step by step:
    # 1. 4 ** 2 = 16
    # 2. 3 * 16 = 48
    # 3. 2 + 3 = 5
    # 4. 5 * 4 = 20
    # 5. 20 // 2 = 10
    # 6. 2 + 48 - 10 = 40

def ternary_operator_demo():
    """
    Demonstrates the precedence of the ternary operator.
    """
    x = 10
    result = "Even" if x % 2 == 0 else "Odd"
    print(f"'Even' if x % 2 == 0 else 'Odd' (x = {x}): {result}")

def bitwise_operators_demo():
    """
    Demonstrates the precedence of bitwise operators.
    """
    result1 = 5 & 3 | 2  # 3
    result2 = 5 & (3 | 2)  # 1
    print(f"5 & 3 | 2 = {result1}")
    print(f"5 & (3 | 2) = {result2}")

def lambda_expression_demo():
    """
    Demonstrates the precedence of lambda expressions.
    """
    f = lambda x: x + 1 if x > 0 else x - 1
    print(f"f(1) = {f(1)}, f(-1) = {f(-1)}")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
=====================================================

Best Practices:
1. Use parentheses to make complex expressions more readable and to ensure 
   correct evaluation order.
2. Break complex expressions into smaller, more manageable parts.
3. Use meaningful variable names to improve expression readability.
4. Comment complex expressions to explain the intended logic.

Common Pitfalls:
1. Assuming left-to-right evaluation for operators with the same precedence.
2. Forgetting that comparison operators chain in Python.
3. Misunderstanding the precedence of bitwise operators.
4. Overlooking the right-associativity of the exponentiation operator.

Advanced Tips:
1. Use the `dis` module to inspect the bytecode of expressions:
"""

def inspect_bytecode(expr: str):
    """
    Inspects the bytecode of a given expression.
    """
    def wrapper():
        eval(expr)
    print(f"Bytecode for '{expr}':")
    dis.dis(wrapper)

"""
2. Utilize the `operator` module for programmatic operations:
"""

def operator_module_demo():
    """
    Demonstrates the use of the operator module.
    """
    numbers = [1, 2, 3, 4, 5]
    result = sum(map(operator.mul, numbers, range(1, 6)))
    print(f"Sum of element-wise multiplication: {result}")

"""
3. Implement custom classes with operator overloading:
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

def vector_operations_demo():
    """
    Demonstrates operator overloading with custom classes.
    """
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    result = v1 + v2 * 2
    print(f"v1 + v2 * 2 = {result}")

"""
4. Use functools.partial for partial application of operators:
"""

from functools import partial

def partial_application_demo():
    """
    Demonstrates partial application of operators.
    """
    double = partial(operator.mul, 2)
    numbers = [1, 2, 3, 4, 5]
    result = list(map(double, numbers))
    print(f"Doubled numbers: {result}")

"""
4. Integration and Real-World Applications
==========================================
Operator precedence is crucial in various real-world applications:

1. Financial Calculations:
   - Ensuring correct order of operations in complex financial formulas.
2. Scientific Computing:
   - Implementing mathematical models with precise operator precedence.
3. Game Development:
   - Calculating physics equations and game logic accurately.
4. Data Analysis:
   - Applying complex transformations and filters to datasets.
5. Compiler Design:
   - Parsing and evaluating expressions in programming languages.

Example: Implementing a simple calculator
"""

def tokenize(expression: str) -> List[str]:
    """Tokenize the input expression."""
    return expression.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(tokens: List[str]) -> List:
    """Parse the tokens into a nested list structure."""
    def parse_expression() -> List:
        token = tokens.pop(0)
        if token == '(':
            subexpr = []
            while tokens[0] != ')':
                subexpr.append(parse_expression())
            tokens.pop(0)  # Remove ')'
            return subexpr
        else:
            return token
    
    parsed = []
    while tokens:
        parsed.append(parse_expression())
    return parsed

def evaluate(expr) -> float:
    """Evaluate the parsed expression."""
    if isinstance(expr, list):
        if len(expr) == 1:
            return evaluate(expr[0])
        op = expr[0]
        if op == '+':
            return sum(evaluate(arg) for arg in expr[1:])
        elif op == '-':
            return evaluate(expr[1]) - sum(evaluate(arg) for arg in expr[2:])
        elif op == '*':
            result = 1
            for arg in expr[1:]:
                result *= evaluate(arg)
            return result
        elif op == '/':
            result = evaluate(expr[1])
            for arg in expr[2:]:
                result /= evaluate(arg)
            return result
        elif op == '^':
            return evaluate(expr[1]) ** evaluate(expr[2])
    else:
        return float(expr)

def calculate(expression: str) -> float:
    """Calculate the result of the given expression."""
    tokens = tokenize(expression)
    parsed = parse(tokens)
    return evaluate(parsed[0])

def calculator_demo():
    """Demonstrates the use of the simple calculator."""
    expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "2 ^ 3 ^ 2",
        "10 / (2 + 3)"
    ]
    for expr in expressions:
        result = calculate(expr)
        print(f"{expr} = {result}")

"""
5. Advanced Concepts and Emerging Trends
========================================
1. Just-In-Time (JIT) Compilation:
   - Optimizing operator precedence at runtime for improved performance.
2. Domain-Specific Languages (DSLs):
   - Implementing custom operator precedence rules for specialized languages.
3. Quantum Computing:
   - Exploring operator precedence in quantum algorithms and simulations.
4. Symbolic Computation:
   - Using operator precedence in symbolic manipulation of mathematical expressions.
5. Natural Language Processing:
   - Applying operator precedence concepts to parsing and understanding natural language.

Example: Simple symbolic differentiation
"""

from typing import Union, Dict

class Expr:
    pass

class Num(Expr):
    def __init__(self, value: float):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Var(Expr):
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name

class BinOp(Expr):
    def __init__(self, left: Expr, op: str, right: Expr):
        self.left = left
        self.op = op
        self.right = right
    
    def __str__(self):
        return f"({self.left} {self.op} {self.right})"

def differentiate(expr: Expr, var: str) -> Expr:
    if isinstance(expr, Num):
        return Num(0)
    elif isinstance(expr, Var):
        return Num(1) if expr.name == var else Num(0)
    elif isinstance(expr, BinOp):
        if expr.op == '+':
            return BinOp(differentiate(expr.left, var), '+', differentiate(expr.right, var))
        elif expr.op == '*':
            return BinOp(
                BinOp(differentiate(expr.left, var), '*', expr.right),
                '+',
                BinOp(expr.left, '*', differentiate(expr.right, var))
            )
    raise ValueError(f"Unsupported expression type: {type(expr)}")

def symbolic_differentiation_demo():
    """Demonstrates simple symbolic differentiation."""
    expr = BinOp(BinOp(Num(2), '*', Var('x')), '+', Var('y'))
    print(f"Original expression: {expr}")
    deriv_x = differentiate(expr, 'x')
    print(f"Derivative with respect to x: {deriv_x}")
    deriv_y = differentiate(expr, 'y')
    print(f"Derivative with respect to y: {deriv_y}")

"""
6. FAQs and Troubleshooting
===========================
Q: Why does Python use 'and' and 'or' instead of '&&' and '||'?
A: Python's design philosophy emphasizes readability. Words like 'and' and 'or' 
   are more explicit and easier to read than symbols.

Q: How do I remember the precedence of all operators?
A: While memorizing the entire precedence table is challenging, focus on 
   common patterns like PEMDAS (Parentheses, Exponents, Multiplication, 
   Division, Addition, Subtraction) for arithmetic operations. For other 
   operators, use parentheses when in doubt to ensure correct evaluation order.

Q: Are there any differences in operator precedence between Python 2 and Python 3?
A: The core precedence rules remain largely the same. However, Python 3 
   introduced new operators (e.g., '@' for matrix multiplication) and removed 
   some old ones (e.g., '<>' for inequality), which slightly altered the 
   precedence table.

Q: How does operator precedence affect short-circuit evaluation?
A: Short-circuit evaluation in logical operations ('and', 'or') is governed by 
   precedence rules. The 'and' operator has higher precedence than 'or', which 
   can affect the order of evaluation in complex logical expressions.

Troubleshooting:

1. Unexpected results in arithmetic expressions:
"""

def troubleshoot_arithmetic():
    result = 1 + 2 * 3 ** 2 - 4 / 2
    print(f"1 + 2 * 3 ** 2 - 4 / 2 = {result}")
    # Explanation:
    # 1. 3 ** 2 = 9 (exponentiation has highest precedence)
    # 2. 2 * 9 = 18 (multiplication before addition/subtraction)
    # 3. 4 / 2 = 2 (division before addition/subtraction)
    # 4. 1 + 18 - 2 = 17 (addition and subtraction from left to right)

"""
2. Confusion with comparison chaining:
"""

def troubleshoot_comparison_chaining():
    x, y, z = 5, 3, 7
    result = x > y < z
    print(f"x > y < z (x={x}, y={y}, z={z}): {result}")
    # Explanation: This is equivalent to (x > y) and (y < z)

"""
3. Bitwise operator precedence issues:
"""

def troubleshoot_bitwise_operators():
    result = 5 & 3 | 4
    print(f"5 & 3 | 4 = {result}")
    # Explanation: 
    # 1. 5 & 3 = 1 (bitwise AND has higher precedence than OR)
    # 2. 1 | 4 = 5

"""
4. Logical operator short-circuiting:
"""

def troubleshoot_short_circuiting():
    def true_func():
        print("true_func called")
        return True
    
    def false_func():
        print("false_func called")
        return False
    
    result = true_func() or false_func()
    print(f"true_func() or false_func() = {result}")
    # Explanation: false_func is not called due to short-circuiting

"""
7. Recommended Tools, Libraries, and Resources
==============================================
Tools and Libraries:
1. ast module: For parsing and analyzing Python abstract syntax trees
   (https://docs.python.org/3/library/ast.html)
2. pylint: A static code analysis tool that can help identify precedence issues
   (https://www.pylint.org/)
3. black: An opinionated code formatter that can help standardize expression formatting
   (https://black.readthedocs.io/)
4. SymPy: A library for symbolic mathematics, useful for working with complex expressions
   (https://www.sympy.org/)

Resources:
1. Python Language Reference on Operator Precedence:
   https://docs.python.org/3/reference/expressions.html#operator-precedence
2. "Fluent Python" by Luciano Ramalho (Book)
3. "Python Cookbook" by David Beazley and Brian K. Jones (Book)
4. PEP 8 -- Style Guide for Python Code:
   https://www.python.org/dev/peps/pep-0008/

8. Performance Analysis and Optimization
========================================
Let's analyze the performance impact of different expression structures:
"""

import timeit

def performance_analysis():
    setup = "import math"
    
    expr1 = "1 + 2 * 3 ** 2 - 4 / 2"
    expr2 = "((1 + (2 * (3 ** 2))) - (4 / 2))"
    expr3 = "3 ** 2 * 2 + 1 - 4 / 2"
    
    time1 = timeit.timeit(expr1, setup=setup, number=1000000)
    time2 = timeit.timeit(expr2, setup=setup, number=1000000)
    time3 = timeit.timeit(expr3, setup=setup, number=1000000)
    
    print(f"Time for '{expr1}': {time1:.6f} seconds")
    print(f"Time for '{expr2}': {time2:.6f} seconds")
    print(f"Time for '{expr3}': {time3:.6f} seconds")

"""
Optimization strategies:
1. Simplify complex expressions when possible.
2. Use built-in functions and operators instead of custom implementations.
3. Consider using libraries like NumPy for large-scale numerical operations.
4. Profile your code to identify bottlenecks related to expression evaluation.

Example of optimizing a complex expression:
"""

def optimize_expression():
    def complex_calc(x, y, z):
        return (x**2 + y**2)**0.5 * math.sin(z) / (1 + x*y)
    
    def optimized_calc(x, y, z):
        xy_product = x * y
        return math.hypot(x, y) * math.sin(z) / (1 + xy_product)
    
    x, y, z = 2, 3, 1
    
    time_complex = timeit.timeit(lambda: complex_calc(x, y, z), number=100000)
    time_optimized = timeit.timeit(lambda: optimized_calc(x, y, z), number=100000)
    
    print(f"Time for complex calculation: {time_complex:.6f} seconds")
    print(f"Time for optimized calculation: {time_optimized:.6f} seconds")
    print(f"Speedup: {time_complex / time_optimized:.2f}x")

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
- The relevance to operator precedence in Python
- The depth of explanation required for expert-level understanding
- The practical applications of the concept in real-world scenarios
- The potential impact on performance and optimization

Your contributions will help keep this note sheet up-to-date and valuable for 
Python developers at all levels. Thank you for your interest in improving this 
resource!
"""

# Unit tests for the calculator implementation
class TestCalculator(unittest.TestCase):
    def test_simple_addition(self):
        self.assertAlmostEqual(calculate("3 + 4"), 7)
    
    def test_complex_expression(self):
        self.assertAlmostEqual(calculate("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"), 3.0001220703125)
    
    def test_parentheses(self):
        self.assertAlmostEqual(calculate("(3 + 4) * 2"), 14)
    
    def test_exponentiation(self):
        self.assertAlmostEqual(calculate("2 ^ 3 ^ 2"), 512)

# This is the main function that demonstrates the usage of operator precedence concepts
def main():
    print("Operator Precedence in Python - Expert-Level Note Sheet")
    print("=======================================================")
    
    parentheses_demo()
    print("\n" + "="*50 + "\n")
    
    exponentiation_demo()
    print("\n" + "="*50 + "\n")
    
    unary_operators_demo()
    print("\n" + "="*50 + "\n")
    
    multiplication_division_demo()
    print("\n" + "="*50 + "\n")
    
    addition_subtraction_demo()
    print("\n" + "="*50 + "\n")
    
    comparison_operators_demo()
    print("\n" + "="*50 + "\n")
    
    logical_operators_demo()
    print("\n" + "="*50 + "\n")
    
    assignment_operators_demo()
    print("\n" + "="*50 + "\n")
    
    complex_expression_demo()
    print("\n" + "="*50 + "\n")
    
    ternary_operator_demo()
    print("\n" + "="*50 + "\n")
    
    bitwise_operators_demo()
    print("\n" + "="*50 + "\n")
    
    lambda_expression_demo()
    print("\n" + "="*50 + "\n")
    
    print("Bytecode Inspection:")
    inspect_bytecode("2 + 3 * 4")
    print("\n" + "="*50 + "\n")
    
    operator_module_demo()
    print("\n" + "="*50 + "\n")
    
    vector_operations_demo()
    print("\n" + "="*50 + "\n")
    
    partial_application_demo()
    print("\n" + "="*50 + "\n")
    
    print("Calculator Demo:")
    calculator_demo()
    print("\n" + "="*50 + "\n")
    
    print("Symbolic Differentiation Demo:")
    symbolic_differentiation_demo()
    print("\n" + "="*50 + "\n")
    
    print("Troubleshooting Demos:")
    troubleshoot_arithmetic()
    troubleshoot_comparison_chaining()
    troubleshoot_bitwise_operators()
    troubleshoot_short_circuiting()
    print("\n" + "="*50 + "\n")
    
    print("Performance Analysis:")
    performance_analysis()
    print("\n" + "="*50 + "\n")
    
    print("Expression Optimization:")
    optimize_expression()
    print("\n" + "="*50 + "\n")
    
    print("Running Unit Tests:")
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main()