"""
Control Structures - for and while loops - in the Python Programming Language
=============================================================================

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
Control structures in Python, particularly 'for' and 'while' loops, are fundamental
constructs that allow for iterative execution of code blocks. These structures
have been an integral part of Python since its inception in 1991 by Guido van Rossum.

- 'for' loops in Python are used for iterating over a sequence (list, tuple, dictionary, set, or string) 
  or other iterable objects. They were inspired by the 'for' loops in C but with a more 
  versatile and Pythonic implementation.

- 'while' loops, on the other hand, repeatedly execute a block of code as long as a given 
  condition is true. This concept dates back to early programming languages and remains 
  a crucial tool in modern software development.

Python's implementation of these loops is notable for its simplicity and readability, 
aligning with the language's philosophy of clear and concise code. The 'for' loop, 
in particular, is more akin to "for each" loops in other languages, making it 
highly intuitive for iteration over collections.

In modern Python development, these control structures are essential for tasks ranging 
from simple data processing to complex algorithmic implementations. They form the 
backbone of many Python programs and are crucial in areas such as data science, 
web development, and automation scripts.

Compared to other languages:
- Python's 'for' loops are more similar to Java's enhanced for loop or C#'s foreach.
- Python's 'while' loops are conceptually similar to those in C, Java, and many other languages.

The evolution of these constructs in Python has focused on maintaining simplicity 
while adding powerful features like list comprehensions and generator expressions, 
which offer more concise ways to perform iterations.

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import time
import asyncio
from typing import List, Dict, Any


def for_loop_basics():
    """
    Demonstrates basic 'for' loop syntax and usage.
    """
    print("Basic for loop:")
    for i in range(5):
        print(i, end=" ")
    print("\n")

    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    print("Iterating over a list:")
    for fruit in fruits:
        print(fruit, end=" ")
    print("\n")

    # Iterating over a string
    print("Iterating over a string:")
    for char in "Python":
        print(char, end=" ")
    print("\n")

    # Using enumerate for index and value
    print("Using enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")
    print()


def while_loop_basics():
    """
    Demonstrates basic 'while' loop syntax and usage.
    """
    print("Basic while loop:")
    count = 0
    while count < 5:
        print(count, end=" ")
        count += 1
    print("\n")

    # While loop with a condition
    print("While loop with a condition:")
    number = 10
    while number > 0:
        print(number, end=" ")
        number -= 2
    print("\n")


def nested_loops():
    """
    Demonstrates nested loops and their applications.
    """
    print("Nested loops - Multiplication table:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} * {j} = {i*j}", end="  ")
        print()
    print()


def loop_control_statements():
    """
    Demonstrates loop control statements: break, continue, and else.
    """
    print("Using 'break':")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print("\n")

    print("Using 'continue':")
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print("\n")

    print("Using 'else' with for loop:")
    for i in range(5):
        print(i, end=" ")
    else:
        print("Loop completed normally")
    print()

    print("Using 'else' with while loop:")
    i = 0
    while i < 5:
        print(i, end=" ")
        i += 1
    else:
        print("While loop completed normally")
    print()


def advanced_for_loop_techniques():
    """
    Demonstrates advanced techniques with for loops.
    """
    # List comprehension
    squares = [x**2 for x in range(10)]
    print("List comprehension:", squares)

    # Dictionary comprehension
    char_count = {char: str.count(char) for char in "hello world"}
    print("Dictionary comprehension:", char_count)

    # Zip function for parallel iteration
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    print("Parallel iteration with zip:")
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")
    print()


def advanced_while_loop_techniques():
    """
    Demonstrates advanced techniques with while loops.
    """
    # Emulating do-while loop
    print("Emulating do-while loop:")
    i = 0
    while True:
        print(i, end=" ")
        i += 1
        if i >= 5:
            break
    print("\n")

    # Using while with else
    print("While with else:")
    n = 0
    while n < 5:
        print(n, end=" ")
        n += 1
    else:
        print("\nLoop completed without break")
    print()


async def async_for_example():
    """
    Demonstrates asynchronous for loop.
    """
    print("Asynchronous for loop:")
    async for i in async_generator():
        print(i, end=" ")
    print("\n")


async def async_generator():
    """
    An asynchronous generator for demonstration.
    """
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i


def performance_comparison():
    """
    Compares performance of different loop constructs.
    """
    print("Performance comparison:")
    
    # Using a for loop
    start_time = time.time()
    result = []
    for i in range(1000000):
        result.append(i ** 2)
    for_loop_time = time.time() - start_time
    print(f"For loop time: {for_loop_time:.6f} seconds")

    # Using list comprehension
    start_time = time.time()
    result = [i ** 2 for i in range(1000000)]
    list_comp_time = time.time() - start_time
    print(f"List comprehension time: {list_comp_time:.6f} seconds")

    # Using generator expression
    start_time = time.time()
    result = list((i ** 2 for i in range(1000000)))
    gen_exp_time = time.time() - start_time
    print(f"Generator expression time: {gen_exp_time:.6f} seconds")

    print(f"List comprehension is {for_loop_time / list_comp_time:.2f}x faster than for loop")
    print(f"Generator expression is {for_loop_time / gen_exp_time:.2f}x faster than for loop")
    print()


def error_handling_in_loops():
    """
    Demonstrates error handling within loops.
    """
    print("Error handling in loops:")
    numbers = [1, 2, 0, 4, 5]
    for num in numbers:
        try:
            result = 10 / num
            print(f"10 / {num} = {result}")
        except ZeroDivisionError:
            print(f"Cannot divide by zero (number: {num})")
    print()


def main():
    """
    Main function to demonstrate all loop concepts.
    """
    for_loop_basics()
    while_loop_basics()
    nested_loops()
    loop_control_statements()
    advanced_for_loop_techniques()
    advanced_while_loop_techniques()
    asyncio.run(async_for_example())
    performance_comparison()
    error_handling_in_loops()


if __name__ == "__main__":
    main()


"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use meaningful variable names in loop constructs.
2. Prefer 'for' loops over 'while' loops when the number of iterations is known.
3. Use list comprehensions for simple transformations on sequences.
4. Avoid modifying the sequence you're iterating over within the loop.
5. Use 'enumerate()' when you need both index and value in a 'for' loop.

Common Pitfalls:
1. Infinite loops: Always ensure a termination condition in while loops.
2. Off-by-one errors: Be careful with range bounds in for loops.
3. Forgetting to increment the counter in while loops.
4. Modifying a list while iterating over it can lead to unexpected behavior.

Advanced Tips:
1. Use 'itertools' module for efficient looping (e.g., itertools.cycle for infinite loops).
2. Implement custom iterators for complex data structures.
3. Use 'contextlib.ExitStack' for managing multiple context managers in a loop.
4. Profile your code to identify performance bottlenecks in loops.

4. Integration and Real-World Applications
------------------------------------------
- Data Processing: Loops are essential in data science for processing large datasets.
- Web Scraping: Iterating over web elements to extract information.
- Game Development: Game loops for continuous rendering and event handling.
- System Administration: Automating repetitive tasks across multiple systems.
- Machine Learning: Implementing iterative algorithms like gradient descent.

Example from TensorFlow (simplified):
```python
for epoch in range(num_epochs):
    for batch in dataset:
        with tf.GradientTape() as tape:
            predictions = model(batch['input'])
            loss = loss_function(batch['target'], predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

5. Advanced Concepts and Emerging Trends
----------------------------------------
- Asynchronous Loops: Using 'async for' in asynchronous programming.
- Parallel Processing: Utilizing multiprocessing to parallelize loops for performance.
- Generator-based Loops: Using generators for memory-efficient iteration.
- Pattern Matching in Loops: Proposed feature for future Python versions.

6. FAQs and Troubleshooting
---------------------------
Q: How do I iterate over two lists simultaneously?
A: Use the zip() function: for item1, item2 in zip(list1, list2):

Q: How can I break out of nested loops?
A: Use a flag variable or exceptions to break out of multiple loop levels.

Q: Why is my while loop not terminating?
A: Ensure that the condition eventually becomes false, or use a break statement.

Troubleshooting:
- For infinite loops, use Ctrl+C to interrupt execution.
- Use print statements or debuggers to track loop variables.
- Check for proper indentation, especially in nested loops.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools:
- PyCharm: IDE with excellent debugging capabilities for loops.
- Visual Studio Code: Lightweight editor with Python extensions.

Libraries:
- itertools: Provides efficient looping tools.
- more-itertools: Extended set of iteration tools.

Resources:
- "Fluent Python" by Luciano Ramalho: In-depth coverage of Python's features.
- Python official documentation: https://docs.python.org/3/tutorial/controlflow.html
- Real Python tutorials: https://realpython.com/python-for-loop/

8. Performance Analysis and Optimization
----------------------------------------
- Use the 'timeit' module for benchmarking loop performance.
- Consider using NumPy for numerical loops for significant speed improvements.
- Use 'map()' or list comprehensions instead of explicit for loops for simple operations.
- In CPython, avoid using 'globals()' or 'locals()' inside loops for better performance.

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
"""