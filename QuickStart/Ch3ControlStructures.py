#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Control Structures
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Control structures dictate the flow of execution within the program. 
# They enable the program to make decisions and execute certain sections of code conditionally.

#===============================================================================
# 1. Conditional Statements
#===============================================================================

# if statement
# A simple if statement evaluates the condition and executes the indented block only if the condition is True.
x = 10  # Here, x is assigned a positive integer value
if x > 0:  # Condition: Checks if x is greater than 0
    print("x is positive")  # Output: "x is positive" will be printed since the condition is True

# Key insight:
# - The condition in an if statement must return a boolean value (True or False).
# - If x was a non-numeric type like a list or string, ">" could raise a TypeError, so it's crucial to validate types in more complex logic.

# if-else statement
y = -5  # y is initialized with a negative value
if y > 0:  # Condition: Checks if y is greater than 0
    print("y is positive")  # This will not be executed because y is negative
else:
    print("y is non-positive")  # Output: "y is non-positive" since y is less than or equal to zero

# Advanced tip:
# - The else block is optional, but it's good practice to include it when handling edge cases.
# - Best practice: Ensure that both branches of the if-else structure are equally likely to be executed for code readability.

# if-elif-else statement
z = 0  # Assigning z a value of zero for this case
if z > 0:  # Condition: Checks if z is greater than 0
    print("z is positive")
elif z < 0:  # Condition: Only evaluated if the first condition is False
    print("z is negative")
else:  # The final condition that will execute if all previous conditions are False
    print("z is zero")  # Output: "z is zero" because z equals 0

# Insight:
# - The elif clause allows checking multiple conditions in sequence.
# - The first true condition will trigger its block, and the rest will be skipped.
# - If none of the conditions are True, the else block is executed (optional).

# Nested if statements
num = 15  # Assigning a positive integer to num
if num >= 0:  # First condition checks if num is non-negative
    if num == 0:  # Nested condition: checks if num is exactly zero
        print("num is zero")  # This block won't be executed
    else:
        print("num is positive")  # Output: "num is positive" because num is greater than zero
else:
    print("num is negative")  # Will not be executed as the outer condition is True

# Advanced tip:
# - While nesting if statements is possible, deeply nested structures can be hard to read and maintain.
# - Consider using elif instead of nested if statements for cleaner code when multiple exclusive conditions are checked.

# Ternary operator (conditional expression)
# A more concise way to handle simple if-else logic.
a = 5  # Variable a is set to a positive integer
result = "positive" if a > 0 else "non-positive"  # Conditional expression: evaluates the condition and assigns based on the result
print(result)  # Output: "positive" because a is greater than 0

# Insight:
# - This single-line form of if-else is known as a "ternary operator" in Python.
# - It's ideal for cases where you need a simple decision-making structure with two outcomes.
# - Avoid overusing this for complex conditions, as it may reduce code clarity.

# Multiple conditions using logical operators
# Logical operators like 'and', 'or', and 'not' can be used to combine multiple conditions.
x, y = 5, 10  # Assigning values to x and y
if x > 0 and y < 20:  # Both conditions need to be True for the block to execute
    print("Both conditions are true")  # Output: "Both conditions are true" because both conditions evaluate to True

# Best practice:
# - Logical operators are short-circuit operators. For 'and', Python stops evaluating as soon as one condition is False.
# - Similarly, for 'or', Python stops evaluating if the first condition is True.
# - This short-circuiting behavior can optimize performance for expensive condition checks.

#===============================================================================
# 2. Loops
#===============================================================================

# Basic for loop with range:
# This loop iterates 5 times, where 'i' takes values from 0 to 4 (range is exclusive of the end value).
# The 'end=" "' argument in print() ensures all values are printed on the same line, separated by a space.
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()  # Prints a newline to keep output clean after the loop

# Usage example: 
# You can use this for simple iterations, like processing a known number of elements in a list or sequence.
# Advanced tip: Using range(len(some_list)) can lead to less readable code when you can iterate over the list itself.

# For loop with a list:
# This loop directly iterates over elements of the 'fruits' list. Using direct iteration over collections like lists
# is a Pythonic approach, as it avoids manual indexing and makes the code clearer and more concise.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")  # Output: apple banana cherry
print()  # Newline for clean output

# Best practice:
# Always prefer direct iteration over the elements of a list rather than using range(len(list)) unless indices are needed.
# Pitfall: Avoid modifying a list while iterating over it, as it can lead to unexpected behavior.

# For loop with enumerate:
# This loop not only iterates over the 'fruits' list but also provides the index of each item using enumerate().
# 'enumerate()' is useful when both the index and value are needed, making the code cleaner and more readable
# than using a counter variable manually.
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Advanced insight:
# enumerate() is efficient and allows easy unpacking of index-value pairs. In performance-critical sections, avoid 
# creating additional counters when enumerate() can provide the same functionality in a single iteration.

# While loop:
# This loop continues as long as the condition 'count < 5' holds true. It's commonly used for scenarios where 
# the number of iterations is not known beforehand. The 'count += 1' line increments the counter to ensure
# the loop eventually terminates.
count = 0
while count < 5:
    print(count, end=" ")
    count += 1  # Output: 0 1 2 3 4
print()  # Newline for clean output

# Best practice:
# While loops are suitable for conditions that change during the loop execution (e.g., waiting for user input or an external event).
# Pitfall: Ensure the loop condition eventually becomes false, or you'll create an infinite loop. Careful handling of 
# incrementing or breaking from the loop is essential.

# Infinite loop (use with caution):
# The while True loop will run indefinitely unless there is a 'break' statement or some other way to exit.
# This is typically used in servers, real-time applications, or polling mechanisms.
# Uncommenting this block will cause the loop to run forever without stopping.
# To prevent it from running endlessly, use conditions and 'break' appropriately.
# while True:
#     print("This will run forever unless broken")
#     # Use a condition like an if statement with 'break' to stop execution when necessary.
# Advanced tip: In performance-sensitive applications, infinite loops combined with condition checks can lead to high CPU usage.
# Use time.sleep() or similar mechanisms to reduce CPU load when polling in an infinite loop.


#===============================================================================

# 3.  Loop Control Statements in Python

#===============================================================================

# This section demonstrates how to control the flow of loops using 'break', 'continue', and 'pass'.
# Each construct serves a specific purpose for altering the loop's behavior, with different use cases for handling loop execution.

# Example 1: Using 'break' to exit a loop prematurely.
# The 'break' statement is used to terminate the loop when a specific condition is met. 
# This can be useful when you've found what you're looking for and don't need to continue further.
for i in range(10):
    # The condition 'i == 5' triggers the break statement, which exits the loop completely.
    if i == 5:
        break  # The loop stops as soon as 'i' equals 5
    print(i, end=" ")  # Output will be: 0 1 2 3 4
    # After the break, none of the iterations 5 through 9 will execute
print()  # Newline to separate output from next example

# Advanced Tip: In nested loops, 'break' only breaks out of the innermost loop. To stop multiple nested loops,
# you'd need to use additional control mechanisms like flags or exception handling.

# Example 2: Using 'continue' to skip the current iteration.
# The 'continue' statement tells the loop to skip the remainder of the current iteration and move to the next one.
# This is useful when you want to ignore certain values but still continue processing the rest of the loop.
for i in range(5):
    # The condition 'i == 2' causes the loop to skip the 'print' statement for that iteration.
    if i == 2:
        continue  # Skips the rest of the current iteration when 'i' equals 2
    print(i, end=" ")  # Output will be: 0 1 3 4
    # The iteration for i == 2 is skipped, so '2' is not printed.
print()  # Newline to separate output from next example

# Advanced Insight: 'continue' can be helpful in filtering out certain conditions without breaking the loop entirely.
# However, overusing 'continue' in complex loops can lead to less readable code, especially if combined with multiple conditions.

# Example 3: Using 'pass' as a placeholder.
# The 'pass' statement is a no-op; it does nothing and allows you to define loops (or any code blocks) where code will eventually be written.
# 'pass' is often used during development to leave placeholders for code that will be implemented later.
for i in range(3):
    pass  # Loop runs but no action is taken during each iteration.

# Practical Tip: 'pass' ensures your code remains syntactically correct when you’re developing incrementally.
# It can be used in any block that requires an indented statement (like functions, classes, conditionals) but where no action is required yet.

# Advanced Tip: Use 'pass' in scenarios where you're designing a structure but want to implement the logic later,
# such as stubbing out parts of a function, class, or loop. Avoid using 'pass' unnecessarily in production code, as it indicates inactive logic that could lead to confusion or missed functionality.

# Additional Use Cases for Each:
# 1. Break: Often used in search algorithms where you want to stop once a match is found, avoiding unnecessary iterations.
# 2. Continue: Useful in data filtering operations, such as skipping invalid or incomplete records in a dataset.
# 3. Pass: Common in larger codebases for stubbing out functions or methods while designing the broader structure, ensuring the code compiles and runs without interruption.



#===============================================================================
# 4. Nested Loops
#===============================================================================

# Nested for loops
# A nested loop is when one loop runs inside another loop. Here, we are using
# two loops. The outer loop runs over a sequence of 3 numbers (0, 1, 2) and
# for each iteration of the outer loop, the inner loop runs over a sequence
# of 2 numbers (0, 1).

# Outer loop (i) will take values from 0 to 2, as the range(3) function generates
# a sequence of 3 values starting from 0 up to but not including 3.
for i in range(3):  # Outer loop iterating through [0, 1, 2]

    # Inner loop (j) will take values from 0 to 1, as the range(2) generates
    # a sequence of 2 values, from 0 up to but not including 2.
    for j in range(2):  # Inner loop iterating through [0, 1]
        
        # Print the current values of (i, j) in tuple form.
        # The 'end=" "' argument ensures that each tuple is printed on the
        # same line, separated by a space, instead of starting a new line after
        # each print statement.
        print(f"({i}, {j})", end=" ")

    # After the inner loop finishes, the 'print()' statement adds a newline,
    # so that the next row of tuples is printed on a new line.
    print()  # Newline after the inner loop finishes one full iteration.

# Output:
# (0, 0) (0, 1)
# (1, 0) (1, 1)
# (2, 0) (2, 1)

#================================ Insights and Advanced Use Cases ================================

# 1. Time Complexity: The total number of iterations in a nested loop is the product
# of the number of iterations of the outer loop and the inner loop. In this case,
# it's 3 * 2 = 6 iterations. Be cautious when nesting multiple loops, as the time
# complexity can quickly grow (e.g., O(n^2), O(n^3)) leading to performance issues
# with large datasets.

# 2. End Parameter: 'end=" "' is a useful feature when formatting output.
# Without it, the default behavior of 'print()' is to add a newline after each
# statement, which would result in each tuple being printed on a new line.

# 3. Output Formatting: This method of formatting the output using 'f-strings'
# allows us to directly embed the values of i and j into the string. F-strings
# are an efficient and readable way of formatting strings introduced in Python 3.6.

# 4. Variations in Loop Depth: The depth of the loops can be easily extended.
# Adding a third loop would create a 3D grid structure. However, keep in mind that
# the readability of nested loops decreases with each additional level, so for
# deeper nesting, it is recommended to break down the problem or use more abstract
# approaches like recursion or specialized data structures.

# 5. Real-World Use Case:
# Nested loops are commonly used when working with multi-dimensional data structures,
# such as matrices (2D arrays) or tensors (higher-dimensional arrays). In image
# processing, for instance, nested loops might be used to traverse the pixels of an
# image where the outer loop goes through the rows and the inner loop goes through the
# columns of each row.

# 6. Pitfalls:
# One common issue is accidentally writing the inner loop to iterate over a range
# that is dependent on the outer loop variable when it's not intended, or modifying
# the outer loop variable inside the inner loop, which can lead to incorrect results.
# Another is inadvertently introducing off-by-one errors in the range definitions.

# 7. Optimization Tips:
# In cases where performance is critical, consider avoiding deeply nested loops by
# leveraging vectorized operations provided by libraries like NumPy, which perform
# better on large datasets because they use optimized C code under the hood.

# Example of extending the concept: Nested loop over a 3x3 grid (e.g., iterating over a matrix).
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # Newline
# Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)

# Example of dynamic ranges in the inner loop:
# Here, the range of the inner loop depends on the current value of the outer loop.
for i in range(3):
    for j in range(i + 1):  # Inner loop has a dynamic range
        print(f"({i}, {j})", end=" ")
    print()  # Newline
# Output:
# (0, 0)
# (1, 0) (1, 1)
# (2, 0) (2, 1) (2, 2)

# This dynamic range is useful in scenarios like generating triangular patterns or
# accessing part of a dataset based on prior conditions.





#===============================================================================
# 5. Comprehensions
#===============================================================================

# List comprehension example: Efficient way to create a list by applying a transformation (x**2) to each element 
# in a range of numbers. List comprehensions are more concise and often faster than using a loop for the same purpose.
# In this case, the expression x**2 squares each number in the range(5), which generates numbers from 0 to 4.
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")  # Output: [0, 1, 4, 9, 16]
# Use case: Often used when you need to transform a collection of data. 
# A foundational example of converting loops into comprehensions, which are more Pythonic.

# List comprehension with condition: Here, the same list comprehension is extended with a conditional clause.
# x**2 for even numbers only (x % 2 == 0) over a range of numbers from 0 to 9.
# This filters the numbers that are even before squaring them.
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")  # Output: [0, 4, 16, 36, 64]
# Advanced tip: Using comprehensions with conditions is more readable and typically faster than filtering with a loop.
# Potential pitfall: Overly complex comprehensions with multiple conditions may harm readability.

# Set comprehension: Similar to list comprehension but produces a set (an unordered collection of unique elements).
# This comprehension calculates the length of each string in the 'fruits' list, and stores only unique lengths in a set.
# Set comprehensions are useful when uniqueness is important.
fruits = ["apple", "banana", "cherry", "apple", "kiwi"]  # Sample list for context
unique_lengths = {len(fruit) for fruit in fruits}
print(f"Unique lengths: {unique_lengths}")  # Output: {5, 6}
# Use case: When dealing with datasets where you want to eliminate duplicates or ensure uniqueness.
# Best practice: Set comprehensions automatically eliminate duplicates, so no need for an extra step for that.

# Dictionary comprehension: Constructs a dictionary from an iterable. 
# Here, it counts the occurrences of the characters 'a', 'b', and 'c' in the fruits list.
# A dictionary comprehension is both concise and efficient, especially compared to manually looping and populating the dictionary.
char_count = {char: fruits.count(char) for char in "abc"}
print(f"Character count: {char_count}")  # Output: {'a': 3, 'b': 1, 'c': 1}
# Advanced insight: While using count() is quick and readable for small datasets, for larger datasets with many lookups, 
# a collections.Counter() might be more efficient. Dictionary comprehensions shine when you need to transform or filter keys/values.
# Pitfall: Overusing comprehensions with complex expressions can lead to less readable code.

# Nested comprehension: This is a more advanced comprehension technique where we use multiple levels of comprehension.
# It creates a matrix (list of lists) by adding 'i' and 'j' for each element in a range(3).
# Nested comprehensions can replace nested loops, offering a compact way to handle two-dimensional structures like matrices.
matrix = [[i+j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")  # Output: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
# Use case: Often used for creating grids or 2D structures like matrices in numerical or graphical applications.
# Advanced tip: Avoid overly deep nesting as it can become unreadable. For more complex logic, consider splitting into functions.
# Best practice: Nested comprehensions are fine for simple operations, but readability declines with depth.



#===============================================================================
# 6. else clause in loops
#===============================================================================

# The 'else' clause in loops in Python is a lesser-known construct but can be quite useful.
# It executes after the loop completes normally (i.e., without encountering a 'break' statement).
# If the loop is terminated prematurely via 'break', the 'else' clause is skipped.
# Below are examples using both 'for' and 'while' loops.

# Example 1: for-else loop example
# A for loop iterating over a range from 0 to 4 (i.e., range(5))
# The 'if' condition inside the loop checks if i == 10, which will never be true
# Because the loop runs without interruption ('break' never occurs), the 'else' clause is executed
for i in range(5):
    if i == 10:  # This condition will never be met, so the loop proceeds normally
        break  # If this condition were met, the loop would break, and 'else' would not execute
    print(i, end=" ")  # Print the current value of 'i' followed by a space, instead of a new line
else:
    # This runs because the loop wasn't interrupted by 'break'
    # Often used to indicate successful completion when a loop completes as expected
    print("Loop completed normally")

# Output: 0 1 2 3 4 Loop completed normally
# The 'else' prints after the loop since no 'break' was triggered.

# Use case:
# The 'for-else' construct can be useful when searching for an item in a sequence.
# If the item is found, break is used, and the else block is skipped.
# If the item is not found, the else block can handle that case.

# Example 2: while-else loop example
# A while loop, similar to the for-else structure but controlled by a condition.
# This loop runs while 'count' is less than 3.
# When 'count' reaches 3, the condition becomes false, and the loop exits normally.
count = 0  # Initializing count to 0
while count < 3:  # Loop runs as long as count is less than 3
    print(count, end=" ")  # Prints the current value of 'count' followed by a space
    count += 1  # Increment 'count' by 1 after each iteration
else:
    # This block runs because the loop condition becomes false (i.e., count >= 3) without a 'break'
    print("While loop completed normally")

# Output: 0 1 2 While loop completed normally
# Similar to the for-else loop, the 'else' clause here is executed when the loop ends normally.

# Advanced tip: 
# The 'else' clause is especially useful when combined with 'break' inside a loop 
# that searches through items or performs a task where an early exit condition is needed.
# If the loop completes without hitting the 'break', the 'else' handles the "default" case.
# It's an elegant alternative to using a flag variable to track completion status.
# The key concept here is that the else block is tied to the loop completion status, not the 'if' condition within the loop.

# Potential pitfalls:
# Misunderstanding the scope of the 'else' clause. It is often mistaken as being linked to the 'if' statement
# inside the loop rather than the loop itself. The 'else' is connected to the loop's completion, not the conditional checks within it.
# As a best practice, limit the usage of the 'else' in loops to scenarios where its behavior significantly improves readability 
# and reduces complexity, such as handling searches or looped error-checking processes.



#===============================================================================
# 7. Switch-Case Alternative (Python 3.10+)
#===============================================================================

# Python does not have a built-in switch-case statement like some other languages (e.g., C, Java).
# However, Python 3.10 introduced the 'match' statement, which serves as a flexible and readable alternative.
# 'match' provides pattern matching capabilities that go beyond simple switch-case behavior, allowing for more advanced use cases.

# Example 1: Basic match-case structure
# The 'check_status' function uses the 'match' statement to handle different 'status' codes, similar to a switch-case.
# This is useful when you have multiple conditions to check against a single value.

def check_status(status):
    # The 'match' statement compares the 'status' argument against predefined cases.
    match status:
        # Each 'case' defines a condition to check, much like the 'case' in a switch-case block.
        case 200:
            return "OK"  # Returns "OK" when the status is 200
        case 404:
            return "Not Found"  # Returns "Not Found" for a 404 status
        case 500:
            return "Internal Server Error"  # Returns "Internal Server Error" for status 500
        case _:
            # The underscore (_) acts as a "default" case, handling any values not explicitly matched.
            # This is similar to the 'default' case in a traditional switch-case statement.
            return "Unknown Status"

# Testing the check_status function with various status codes
print(check_status(200))  # Output: OK
print(check_status(404))  # Output: Not Found
print(check_status(500))  # Output: Internal Server Error
print(check_status(302))  # Output: Unknown Status

# Explanation:
# The match-case statement makes the code more readable and manageable, especially when handling many conditions.
# The underscore (_) as a wildcard case ensures that unhandled conditions are caught, avoiding unexpected behavior.
# In earlier versions of Python (pre-3.10), this might have been done with multiple 'if-elif' blocks, which can become
# harder to maintain when there are many cases.

# Advanced tip:
# Match-case can handle more complex data structures and patterns, including lists, tuples, and even classes.
# This makes it much more powerful than a simple switch-case from other languages, offering enhanced flexibility.

# Example 2: More complex pattern matching with lists
# The following example demonstrates how 'match' can be used to match patterns within lists, split by spaces.

def process_command(command):
    # The match statement compares the split list returned by command.split()
    match command.split():
        case ["quit"]:
            # Matches the list ['quit'], meaning the user wants to exit the program
            return "Exiting program"
        case ["hello", name]:
            # Matches a two-item list where the first element is "hello" and the second is a name
            # The second part is treated as a variable 'name' that can be used in the return statement
            return f"Hello, {name}!"  # Example: If command is "hello Sabbir", this returns "Hello, Sabbir!"
        case ["add", x, y]:
            # Matches a three-item list where the first element is "add", and the second and third are numbers
            # The x and y are cast to floats for numeric addition, and the result is returned
            return f"Result: {float(x) + float(y)}"  # Example: "add 5 3" returns "Result: 8.0"
        case _:
            # The underscore (_) acts as a wildcard, capturing any other unhandled input.
            return "Invalid command"

# Testing the process_command function with various commands
print(process_command("quit"))  # Output: Exiting program
print(process_command("hello Sabbir"))  # Output: Hello, Sabbir!
print(process_command("add 5 3"))  # Output: Result: 8.0
print(process_command("invalid"))  # Output: Invalid command

# Explanation:
# This example shows how to use pattern matching with lists. Each case matches a specific pattern within the command.
# In the first case, it matches a list with a single string "quit".
# In the second case, it matches a list where the first element is "hello" and binds the second element to the 'name' variable.
# The third case matches when the first element is "add" and extracts the second and third elements as variables 'x' and 'y'.
# The last case, using '_', matches any command that doesn't fit the previous patterns.

# Advanced use case:
# Pattern matching with the 'match' statement can be used with more complex data structures like dictionaries, classes, or nested patterns.
# This makes it highly suitable for tasks such as parsing complex inputs, building command-line interfaces, or implementing state machines.
# In future Python projects, consider leveraging the 'match' statement to enhance code readability and reduce the complexity 
# of if-elif chains, especially when handling a variety of conditions or inputs.

# Best practice:
# Use the 'match' statement when there are multiple potential outcomes based on a single value or pattern.
# It helps to simplify code and makes it more readable, especially in scenarios where there are many cases.
# For simpler scenarios or if working with older Python versions (<3.10), stick to the traditional if-elif structure.

# Pitfall:
# Remember that the 'match' statement is only available in Python 3.10 and later.
# Be cautious when using it in environments where you may need to support earlier Python versions.


#===============================================================================
# 8. Exception Handling
#===============================================================================

# Exception handling in Python is done using 'try', 'except', 'else', and 'finally' blocks.
# It's a crucial mechanism for handling errors that can occur during runtime, 
# allowing the program to recover or handle exceptional situations gracefully.
# Below are detailed examples covering various aspects of exception handling.

# Example 1: Basic try-except block
# This demonstrates a basic structure of a try-except where a potential error is caught.
# In this case, dividing by zero raises a 'ZeroDivisionError'.
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:  # Catches the specific exception and handles it
    print("Cannot divide by zero!")

# Output: Cannot divide by zero!

# Use case:
# Basic try-except is useful when you expect a specific type of error and want to handle it in a controlled manner.
# Always handle exceptions as close to the source of the problem as possible for better debugging and maintenance.

# Example 2: Multiple except blocks
# This demonstrates handling different types of exceptions separately.
try:
    x = int(input("Enter a number: "))  # Input is cast to an integer, which may raise ValueError
    result = 10 / x  # Potential ZeroDivisionError if x is 0
except ValueError:  # Handles invalid input, i.e., non-numeric values
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:  # Handles division by zero
    print("Cannot divide by zero!")

# If the input is not a valid integer, a ValueError will be caught.
# If the user inputs 0, a ZeroDivisionError will be caught.

# Use case:
# When a block of code can raise multiple different exceptions, it's a best practice to handle each one separately
# to provide specific and meaningful error messages to the user.

# Example 3: Catching multiple exceptions in one line
# You can catch multiple exceptions in a single except clause by using a tuple.
try:
    # Imagine there's some risky operation here that can raise multiple errors
    pass  # Replace with actual code that may raise exceptions
except (ValueError, ZeroDivisionError) as e:  # Catches both ValueError and ZeroDivisionError
    # 'as e' captures the exception object, which can be useful for debugging or logging purposes
    print(f"An error occurred: {e}")

# Use case:
# This is helpful when you want to handle multiple exceptions in the same way,
# simplifying the code and reducing repetition. Be cautious not to overuse this as it can obscure which exception occurred.

# Advanced tip:
# Use exception chaining with `raise from` to preserve the original context of an exception when re-raising, 
# making debugging easier by showing both the original and new exception.

# Example 4: try-except-else-finally block
# The 'else' block is executed if the try block doesn't raise any exceptions.
# The 'finally' block is always executed, regardless of whether an exception was raised or not.
try:
    x = int(input("Enter a number: "))  # Input casting to integer
    result = 10 / x  # Potential ZeroDivisionError
except ValueError:  # Handles invalid input
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:  # Handles division by zero
    print("Cannot divide by zero!")
else:
    # This block only runs if no exceptions were raised in the try block
    print(f"The result is: {result}")
finally:
    # This block always runs, regardless of whether an exception occurred or not
    print("This will always execute.")

# Use case:
# The 'finally' block is typically used for cleanup actions, such as closing a file or releasing external resources.
# The 'else' block is useful when you want to execute some code only when no exceptions are raised, 
# often for success-related logic.

# Advanced tip:
# Avoid putting return statements inside 'finally' blocks, as they override exceptions raised in the 'try' block,
# making debugging harder.

# Example 5: Raising exceptions manually
# You can raise exceptions manually using the 'raise' keyword.
def validate_age(age):
    # A function that validates an age input and raises exceptions based on conditions
    if age < 0:  # If age is negative, raise a ValueError
        raise ValueError("Age cannot be negative.")
    if age > 120:  # If age is unrealistically high, raise another ValueError
        raise ValueError("Age is too high.")

try:
    validate_age(150)  # This will raise a ValueError because age > 120
except ValueError as e:  # Catch the raised exception
    print(f"Invalid age: {e}")

# Output: Invalid age: Age is too high.

# Use case:
# Raising exceptions manually is useful when validating inputs or when encountering an invalid state in your program.
# By raising an exception, you force the calling code to handle the error in a structured way.

# Advanced tip:
# When raising exceptions in larger applications, consider creating custom exception classes
# to provide more specific error information relevant to the domain.

# Example 6: Custom exceptions
# You can define your own exceptions by subclassing the built-in 'Exception' class.
class CustomError(Exception):
    pass  # A custom exception class; you can extend it to add more functionality

try:
    raise CustomError("This is a custom error")  # Manually raising the custom exception
except CustomError as e:  # Catching the custom exception
    print(f"Caught custom error: {e}")

# Output: Caught custom error: This is a custom error

# Use case:
# Custom exceptions are highly useful in complex applications where built-in exceptions may not convey 
# enough context or specificity. They can also be used for handling domain-specific errors in a more structured way.

# Advanced tip:
# When creating custom exceptions, always derive from 'Exception' (not 'BaseException') and include helpful error messages.
# This improves error tracking and can assist in debugging and logging.

# Best Practice:
# Always handle exceptions gracefully to avoid cryptic error messages and ensure your application can recover from errors when appropriate.


#===============================================================================
# 9. Context Managers (with statement)
#===============================================================================

# Context managers are designed to manage resources efficiently and cleanly.
# They allow for setup and teardown of resources, ensuring that no matter how the block exits,
# the resources are cleaned up properly (e.g., closing files, releasing locks, etc.).
# The 'with' statement is used to work with context managers. It ensures that resources are 
# automatically managed when entering and exiting the block of code.

# Example 1: File handling with a built-in context manager
# Using 'with' to handle file operations is a common example.
# The 'with' statement opens the file and ensures that it is properly closed after the block,
# even if an exception occurs during the file operations.

# In this case, 'example.txt' is opened in write mode ('w'), and 
# the context manager automatically closes the file after the block of code is executed.
with open('example.txt', 'w') as file:
    file.write('Hello, World!')  # Writing 'Hello, World!' to the file

# Advanced insight:
# Without using 'with', you would need to explicitly call file.close() after file.write().
# However, if an error occurs before closing the file, the file might remain open.
# 'with' ensures the file is always closed, preventing potential resource leakage.

# Example 2: Custom context manager using 'contextlib' library
# In addition to built-in context managers like file handling, you can create your own custom context managers.
# The 'contextlib' module provides a decorator (@contextmanager) to simplify the creation of context managers.
# This approach uses 'yield' to return a resource, and the code after 'yield' is executed 
# once the 'with' block exits, ensuring proper cleanup.

from contextlib import contextmanager  # Importing the contextmanager decorator

# Define a custom context manager using a generator function
@contextmanager
def managed_resource():
    # This code runs when entering the 'with' block
    print("Acquiring resource")  # Simulate resource acquisition, such as opening a connection or locking a file
    try:
        yield "Resource"  # This is the resource provided to the 'with' block
    finally:
        # This block always runs, even if an exception occurs in the 'with' block
        print("Releasing resource")  # Simulate resource release, such as closing a connection or unlocking

# Using the custom context manager
with managed_resource() as resource:
    # Inside the 'with' block, the resource is accessible, here it's just a string "Resource"
    print(f"Using {resource}")  # Outputting the resource for demonstration

# Output:
# Acquiring resource
# Using Resource
# Releasing resource

# Explanation of the flow:
# 1. Upon entering the 'with' block, the code before 'yield' (i.e., "Acquiring resource") is executed.
# 2. The 'yield' statement pauses the function, passing control to the 'with' block and returning "Resource".
# 3. After the 'with' block completes (whether normally or due to an exception), 
#    the code after 'yield' (i.e., "Releasing resource") is executed to clean up.

# Advanced tip:
# Custom context managers are especially useful for managing complex resources like database connections, 
# file locks, or expensive network calls. They guarantee that resources are always properly released, 
# even if an error occurs during processing.

# Potential pitfall:
# Ensure that the resource is safely used within the 'try' block. If exceptions are thrown in the 'yield',
# the 'finally' block still executes, but if misused, it could cause issues where resources are left in an inconsistent state.
# Avoid performing resource allocation directly in the 'yield' statement to ensure a clean separation 
# between resource setup and the usage inside the 'with' block.

# Best practice:
# Always use context managers when dealing with resources that need setup and teardown, such as file operations, 
# network connections, or lock acquisition. It greatly simplifies resource management by avoiding explicit 
# resource cleanup, improving code readability and reducing errors related to manual handling.


#===============================================================================
# 10. Advanced Control Flow Techniques
#===============================================================================

# Advanced control flow techniques allow for more efficient and expressive logic in Python.
# Here, we'll explore short-circuit evaluation, the walrus operator, and using functions in control flow.

# Example 1: Short-circuit evaluation
# In Python, logical operators like 'and' and 'or' use short-circuit evaluation.
# This means Python will stop evaluating expressions as soon as the outcome is determined.

x = 5
y = 10
# The 'and' operator checks if both conditions are True.
# Since 'x < y' is True, Python continues and evaluates the second part, which is the print statement.
# If 'x < y' were False, the print would not be executed because Python would short-circuit the evaluation.
result = x < y and print("x is less than y")  # Output: x is less than y

# Output: x is less than y
# If 'x < y' was False, nothing would be printed, since Python wouldn’t evaluate the right-hand side.

# Use case:
# Short-circuiting is useful for optimizing conditions, especially when checking expensive operations.
# It’s also frequently used in default assignment patterns, e.g., `a or b` will return `a` if it's True, otherwise `b`.

# Potential pitfall:
# While this technique improves efficiency, it can sometimes obscure readability if overused.
# For instance, relying too heavily on short-circuiting in complex expressions can make the logic harder to follow.

# Example 2: Walrus operator (introduced in Python 3.8+)
# The walrus operator (':=') allows assignment and evaluation in a single expression.
# This can be particularly helpful in loops or conditionals where you need to both assign and use a value.

numbers = [1, 2, 3, 4, 5]
# Here, 'n := len(numbers)' assigns the length of 'numbers' to 'n' and then checks if 'n' is greater than 3.
# If the condition is True, it prints the result.
if (n := len(numbers)) > 3:
    # By using the walrus operator, we avoid calculating the length twice and reduce redundancy.
    print(f"List has {n} items, which is more than 3")  # Output: List has 5 items, which is more than 3

# Output: List has 5 items, which is more than 3

# Advanced tip:
# The walrus operator is particularly helpful in loops where you need to evaluate and use an expression in the same line.
# Example: while (line := f.readline()) could reduce boilerplate code in file reading.

# Potential pitfalls:
# Some developers find the walrus operator makes code less readable, especially if used in non-obvious places.
# It should be used in scenarios where it enhances clarity and reduces duplication rather than complicating logic.

# Example 3: Function as control flow
# Functions can be used as an elegant way to manage control flow, especially for operations that depend on user input or logic.
# Instead of using a long series of if-elif-else statements, you can use a dictionary of functions to handle operations.

# A function that takes an operation type (e.g., 'add', 'subtract') and two numbers (x, y)
# Inside the function, we use a dictionary to map operation names to corresponding lambda functions
def perform_operation(operation, x, y):
    # Defining a dictionary where keys are operation names, and values are lambda functions
    operations = {
        'add': lambda: x + y,  # Adds x and y
        'subtract': lambda: x - y,  # Subtracts y from x
        'multiply': lambda: x * y,  # Multiplies x and y
        'divide': lambda: x / y if y != 0 else "Cannot divide by zero"  # Divides x by y, with a check to avoid division by zero
    }
    # Return the result of the function associated with the given operation
    # If the operation is not found, it defaults to an "Invalid operation" lambda
    return operations.get(operation, lambda: "Invalid operation")()

# Testing the function with different operations
print(perform_operation('add', 5, 3))  # Output: 8
print(perform_operation('divide', 10, 2))  # Output: 5.0
print(perform_operation('power', 2, 3))  # Output: Invalid operation

# Use case:
# This pattern allows for extensibility and cleaner control flow, especially when you need to handle many operations.
# Adding new operations is easy—just add them to the dictionary without altering the main control flow.

# Advanced tip:
# This design can be extended for more complex applications, such as using this pattern to manage permissions or routing in web applications.

# Potential pitfalls:
# Be cautious when using this for operations that could raise exceptions (e.g., division by zero).
# Make sure to handle edge cases explicitly inside the lambda or function definitions to avoid runtime errors.

# Summary:
# These advanced control flow techniques, from short-circuit evaluation and the walrus operator to function-based control flow, 
# offer powerful ways to reduce redundancy, improve performance, and write more expressive code.
