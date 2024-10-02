#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Exception Handling
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exception handling in Python is crucial for managing runtime errors and preventing crashes.
# It allows you to gracefully handle unexpected conditions, providing more control over the program's behavior.

# 1. Basic Try-Except Block
# This is the simplest form of exception handling. It tries to execute the code inside the 'try' block.
# If an exception is raised, it is caught by the 'except' block that matches the exception type.

def basic_try_except():
    try:
        # Attempting to divide by zero, which is mathematically undefined.
        # This line will raise a ZeroDivisionError.
        x = 1 / 0  
    except ZeroDivisionError:
        # When the ZeroDivisionError is caught, this block will execute.
        # We handle the error by printing a message instead of letting the program crash.
        print("Cannot divide by zero!")  

# Call the function
basic_try_except()  
# Output: Cannot divide by zero!

# Key Points:
# - 'try' block: This is where you place the code that may raise an exception.
# - 'except' block: Catches the exception that matches its type (in this case, ZeroDivisionError).
# - By catching exceptions, we ensure the program doesn't terminate abruptly.

# Tip: Always catch specific exceptions rather than using a bare except clause.
# Bare except (i.e., 'except:') catches all exceptions, which is generally considered bad practice
# because it may suppress legitimate errors like KeyboardInterrupt or MemoryError, making debugging difficult.

# Advanced insight:
# Catching specific exceptions allows for better control and debugging.
# You can also chain multiple 'except' clauses to handle different types of errors individually.

# Example 2: Handling multiple specific exceptions
def handle_multiple_exceptions():
    try:
        x = int("not_a_number")  # This will raise a ValueError because the string cannot be converted to an integer
        y = 1 / 0  # This will raise a ZeroDivisionError if the previous line succeeds
    except ValueError:
        print("ValueError: Could not convert string to an integer.")
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")

handle_multiple_exceptions()
# Output: ValueError: Could not convert string to an integer.
# Here, the ValueError is raised first, so the ZeroDivisionError is never reached.

# Best practice: 
# Catch the most specific exception possible to ensure you're addressing the correct issue. 
# Use multiple 'except' clauses to handle different errors if needed, each addressing specific error types.

# Potential pitfall:
# Overusing a bare 'except' (e.g., 'except:') can lead to catching and suppressing critical errors like SystemExit or KeyboardInterrupt, 
# which may prevent the program from terminating when needed.
# For instance, always use 'except Exception:' instead of 'except:', as it will only catch non-system-level errors.

# Tip: You can combine exception handling with 'else' and 'finally'.
# - 'else' executes when no exception occurs in the try block.
# - 'finally' runs regardless of whether an exception occurred, making it useful for cleanup tasks.

# Example 3: Using 'else' and 'finally'
def try_except_else_finally():
    try:
        result = 10 / 2  # No error here, so the 'else' block will run.
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        # Executes if no exception is raised in the 'try' block
        print(f"Division successful, result: {result}")
    finally:
        # Runs no matter what; often used for resource cleanup (e.g., closing files, database connections)
        print("This runs whether an error occurred or not.")

try_except_else_finally()
# Output: 
# Division successful, result: 5.0
# This runs whether an error occurred or not.

# Advanced tip:
# 'finally' is particularly useful when dealing with resources like file I/O or database connections,
# where you need to ensure proper cleanup (closing files, releasing locks, etc.), regardless of whether the try block succeeds or fails.

#=================================================================================
# 2. Catching the Exception Object
#=================================================================================

# In Python, exception handling is done using the 'try-except' block.
# When an exception is raised in the 'try' block, the 'except' block is executed.
# In this example, we demonstrate how to catch a specific exception and access its details.

# Function that demonstrates catching an exception object
def catch_exception_object():
    try:
        # Attempting to divide by zero, which raises a ZeroDivisionError
        x = 1 / 0
    except ZeroDivisionError as e:  
        # Catches the specific ZeroDivisionError exception and binds it to the variable 'e'
        # 'e' is an instance of the exception object, and it holds the error message and other information
        print(f"An error occurred: {e}")  # Prints the error message associated with the exception
        print(f"Error type: {type(e).__name__}")  # Prints the type of exception raised (ZeroDivisionError)

# Calling the function to see the exception handling in action
catch_exception_object()

# Output:
# An error occurred: division by zero
# Error type: ZeroDivisionError

# Explanation:
# 1. In the 'try' block, dividing by zero raises a ZeroDivisionError.
# 2. The 'except' block catches this specific error and assigns it to the variable 'e'.
# 3. We then use 'e' to retrieve and print more information about the error, such as the error message and the exception type.

# Use case:
# Catching an exception object is useful when you need detailed information about the error
# or when you want to handle specific types of exceptions in different ways.
# For instance, you might want to log the error or provide a detailed message to users or developers.

# Advanced tip:
# 'as e' allows access to the exception object, which contains valuable debugging information.
# You can print or log the exception message (e.g., division by zero) and the type of exception (e.g., ZeroDivisionError).
# This can also be helpful when you need to re-raise the exception after logging or handling it temporarily.

# Another advanced use case:
# You can define custom exceptions for specific error handling in your application, and catching exceptions this way allows you 
# to distinguish between different error types. For instance, if your application defines multiple error types (e.g., InputError, 
# FileError), you can catch them individually and handle them in different ways depending on the needs of the program.

# Potential pitfall:
# Overusing broad exception types like 'Exception' can make debugging more difficult because it can obscure the specific error type.
# It's a best practice to catch specific exceptions (like ZeroDivisionError) instead of catching all exceptions,
# unless you're dealing with unpredictable errors that need a general safety net.


#=================================================================================
# 3. Catching Multiple Exceptions
#=================================================================================

# In Python, when working with exception handling, multiple types of exceptions can be caught 
# using separate 'except' blocks. This allows for handling specific error cases individually.
# The 'try-except' structure tries a block of code and catches any exceptions that occur,
# allowing the program to continue running smoothly instead of crashing.

def multiple_exceptions():
    try:
        # This block contains code that could raise different exceptions.
        # The input function prompts the user to enter a number, which could raise a ValueError
        # if the input cannot be converted to an integer.
        x = int(input("Enter a number: "))  # Attempts to convert user input to an integer
        
        # This line performs a division operation.
        # If 'x' is 0, it raises a ZeroDivisionError.
        result = 10 / x  # Possible ZeroDivisionError if 'x' is 0
        
        # If no exception occurs, print the result of 10 divided by the input number.
        print(f"Result: {result}")
        
    except ValueError:
        # This block catches a ValueError, which occurs when the user inputs non-integer data.
        # It's specific to incorrect user input that can't be converted to an integer.
        # It gives feedback to the user that the input was invalid.
        print("Invalid input. Please enter a number.")
        
    except ZeroDivisionError:
        # This block handles the ZeroDivisionError, which is raised when attempting to divide by zero.
        # It informs the user that dividing by zero is not allowed in arithmetic.
        print("Cannot divide by zero!")

# Uncomment to test the function in a live environment:
# multiple_exceptions()

# Example usage:
# Input: 'abc' (ValueError) -> Output: "Invalid input. Please enter a number."
# Input: '0' (ZeroDivisionError) -> Output: "Cannot divide by zero!"
# Input: '5' (Valid input) -> Output: "Result: 2.0"

# Key insights:

# 1. Multiple except blocks: You can define multiple except blocks to catch different types of exceptions.
#    Each block corresponds to a specific exception type, allowing for customized error handling based on 
#    the type of error that occurs.

# 2. Order matters: Python checks 'except' blocks in order. Therefore, more specific exceptions (like ValueError or 
#    ZeroDivisionError) should come before general exceptions (like Exception). Catching more general exceptions first 
#    can prevent specific ones from being handled correctly. If a general exception like 'Exception' is placed before
#    a specific one, it will catch all exceptions, including the specific ones, potentially leading to unintended behavior.

# Advanced tip:
# You can use a tuple of exceptions in a single 'except' block if you want to handle multiple exceptions in the same way.
# For instance:
# except (ValueError, ZeroDivisionError):
#     print("An error occurred with the input or division.")
# This can make your code more concise when multiple exceptions should be handled identically.

# Example:
# def multiple_exceptions_concise():
#     try:
#         x = int(input("Enter a number: "))
#         result = 10 / x
#         print(f"Result: {result}")
#     except (ValueError, ZeroDivisionError):
#         print("An error occurred with the input or division.")

# Potential Pitfalls:
# - Be cautious when using broad exception handling (e.g., 'except Exception:'). While it catches all exceptions,
#   it can mask underlying issues in the code that are better left unhandled for debugging.
# - Handling too many exceptions in a single block can reduce code clarity. It's usually better to handle each type of 
#   exception separately unless they truly warrant the same handling.

# Best practice:
# Always aim to catch only those exceptions that you can recover from or that require specific handling.
# It's important to provide meaningful error messages to users or log exceptions to aid in troubleshooting.

#=================================================================================
# 4. Catching Multiple Exceptions in One Line
#=================================================================================

# Python allows multiple exceptions to be caught in a single 'except' block by grouping them in parentheses.
# This is useful when multiple types of exceptions need to be handled in the same manner, 
# reducing redundant code and improving readability.
# The following example demonstrates catching both ValueError and ZeroDivisionError in a single line.

def multiple_exceptions_one_line():
    try:
        # First, we attempt to convert the user's input into an integer
        # If the input isn't a valid number, a ValueError will be raised
        x = int(input("Enter a number: "))
        
        # Then, we try to divide 10 by the input value 'x'
        # If 'x' is 0, a ZeroDivisionError will be raised because division by zero is undefined
        result = 10 / x
        print(f"Result: {result}")  # Print the result if no exceptions occur

    # Catching both ValueError (invalid input) and ZeroDivisionError (division by zero) in a single 'except' block
    except (ValueError, ZeroDivisionError) as e:
        # 'e' represents the caught exception instance
        # We print the type of the exception (e.g., ValueError or ZeroDivisionError) and the error message
        print(f"An error occurred: {type(e).__name__} - {e}")

# Uncomment the function call below to test the exception handling
# This will allow you to simulate input and trigger either ValueError or ZeroDivisionError
# multiple_exceptions_one_line()

# Usage example:
# 1. If the user enters a non-numeric string like "abc", a ValueError will be caught and handled.
#    Output: An error occurred: ValueError - invalid literal for int() with base 10: 'abc'
# 2. If the user enters '0', a ZeroDivisionError will be caught and handled.
#    Output: An error occurred: ZeroDivisionError - division by zero
# 3. If the user enters a valid number like '5', no exception will be raised.
#    Output: Result: 2.0

# Tip:
# Catching multiple exceptions in one line is a powerful tool when the handling for different errors is identical.
# This reduces the need for multiple 'except' blocks, improving both the conciseness and readability of the code.

# Advanced insight:
# The exception object 'e' not only provides the error message but also contains useful attributes such as the stack trace.
# For advanced logging, tools like the 'logging' module can be used to log the full exception details including tracebacks.
# For instance, in production code, you might replace the 'print' statement with logging:
#   logging.error(f"An error occurred: {type(e).__name__} - {e}", exc_info=True)
# The 'exc_info=True' provides more detailed debugging information (i.e., the stack trace).

# Potential pitfalls:
# While it's convenient to catch multiple exceptions in one block, be careful not to group unrelated exceptions.
# Grouping too many exception types together can make debugging harder, as the code will handle different errors in the same way,
# potentially masking specific issues. If different handling is required for each error type, it's better to use separate 'except' blocks.

#=================================================================================
# 5. Catching All Exceptions (use sparingly)
#=================================================================================

# In Python, exception handling is critical for making your code robust and preventing unexpected crashes.
# The try-except block allows you to "catch" exceptions and handle them appropriately.
# However, catching all exceptions with a broad 'except' clause should be done sparingly and with care.
# It can hide bugs or make debugging difficult, so always prefer catching specific exceptions unless you have a valid reason.

# Example: Catching all exceptions using 'Exception' as the base class
# The function 'catch_all' demonstrates a common pattern of catching all exceptions using 'Exception'.
def catch_all():
    try:
        # A risky operation that will raise an exception
        # In this case, dividing by zero triggers a ZeroDivisionError
        x = 1 / 0  # This will cause a ZeroDivisionError since division by zero is undefined
    except Exception as e:  
        # Catching the exception and printing the type of the exception and its message
        # 'Exception' is the base class for most built-in exceptions
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")
        # The 'type(e).__name__' gives the name of the exception class (e.g., ZeroDivisionError)
        # 'e' contains the exception message, which helps in debugging
        # Printing exception details allows you to log or track the issue while preventing the program from crashing

# Calling the function to see how it handles the ZeroDivisionError
catch_all()
# Output: An unexpected error occurred: ZeroDivisionError - division by zero
# In this example, ZeroDivisionError is raised and caught by the 'except Exception' block, preventing a crash.

# Best practice:
# It is essential to be cautious with broad exception handling:
# - Using 'except Exception' catches all subclasses of Exception, which can be useful for catching unexpected issues.
# - However, indiscriminate use can make your code less predictable or harder to debug since it masks specific error types.
# - For more control and better error handling, it's a good idea to catch specific exceptions like ValueError, TypeError, etc., when possible.

# Tip: Avoid bare 'except:' blocks.
# Bare 'except:' blocks catch *everything*, including critical system-level exceptions like KeyboardInterrupt or SystemExit,
# which should generally not be caught as they interfere with the normal operation of the program and the environment.
# To ensure you're only catching application-level errors, always use 'except Exception' or catch specific error types.

# Advanced tip:
# - When catching exceptions, consider logging the full stack trace using the 'traceback' module for more comprehensive error reporting.
#   This is particularly useful in larger applications where detailed logs help track down bugs.
# Example of logging the full stack trace:
#     import traceback
#     except Exception as e:
#         print(f"An unexpected error occurred: {type(e).__name__} - {e}")
#         traceback.print_exc()  # Prints the full stack trace to give more context about where the error occurred.

# Potential pitfalls:
# - Catching 'Exception' can suppress critical issues (e.g., bugs in your logic or code).
# - Overuse of broad exception handling can lead to silent failures, making it difficult to track the cause of issues.
# - If you catch 'Exception', ensure you at least log the error to avoid masking serious problems in your application.
# - Always consider whether a specific exception type can be caught instead of 'Exception'. This reduces the risk of unexpected behavior.

# Summary:
# Use the broad 'Exception' catching sparingly and with care, particularly in places where you want to safeguard code 
# against multiple possible exceptions without halting the application. Always ensure error logging is in place to track 
# these unexpected exceptions, and aim to catch specific exceptions wherever possible for better code reliability.

#=================================================================================
# 6. Else Clause in try-except blocks
#=================================================================================

# The 'else' clause in a try-except block is often underutilized but can be very useful
# for keeping code cleaner and separating logic. The 'else' block runs only if no exception
# occurs in the 'try' block. It provides a way to place code that should only execute 
# if the 'try' block was successful, without being caught by any exceptions.

# Example: try-except-else structure
# In this function, we request a user input, attempt to convert it to an integer, and then
# divide 10 by the inputted number. Depending on the input, different exceptions may be raised.
# If the input is valid and no errors occur, the 'else' block executes.

def try_except_else():
    try:
        # Attempt to convert the user input into an integer
        x = int(input("Enter a number: "))  # May raise a ValueError if input is not an integer
        
        # Perform a division. If x is 0, a ZeroDivisionError will be raised
        result = 10 / x  # Potential division by zero, triggering ZeroDivisionError
    except ValueError:
        # This block runs if a ValueError occurs, i.e., when the input cannot be converted to an integer
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        # This block runs if the input was 0, causing a division by zero
        print("Cannot divide by zero!")
    else:
        # This block only executes if no exceptions (ValueError or ZeroDivisionError) are raised
        # It is used for handling the "normal" case, i.e., when the input is valid and no errors occur
        print(f"The result is: {result}")  # The result of the division is printed here

# Use case:
# In situations where you want certain code to run only when no exceptions are raised, 
# the 'else' clause provides clarity by separating error-handling logic from the normal flow of execution.
# Without 'else', you'd have to put the result handling inside the 'try' block, making the code messier.

# Uncomment to test the function:
# try_except_else()

# Example of potential outputs:
# Input: '5' -> Output: The result is: 2.0  (Normal flow, no exceptions)
# Input: 'a' -> Output: Invalid input. Please enter a number.  (ValueError)
# Input: '0' -> Output: Cannot divide by zero!  (ZeroDivisionError)

# Advanced tip:
# The 'else' clause in a try-except block is an excellent way to keep the main logic (in this case, the division and its result)
# separated from exception handling. This improves readability and ensures that the code in 'else' only runs if no exceptions occurred.
# If your 'try' block contains code that should be skipped in the event of an error, consider using 'else' instead of lumping everything inside 'try'.

# Potential pitfall:
# Be cautious with the placement of code in the 'try' block. Only put the code that may raise exceptions inside 'try'. 
# Anything that doesn't need exception handling should ideally be placed in the 'else' block or outside the 'try-except' altogether.
# This practice reduces the chances of accidentally catching unexpected exceptions, leading to more predictable behavior.

#=================================================================================
# 7. try-except-finally structure
#=================================================================================

# The 'try-except-finally' block in Python is used for exception handling.
# It allows you to catch and handle errors while ensuring that certain cleanup code 
# (in the 'finally' block) is always executed, whether an exception occurs or not.
# This is especially useful when working with resources like file handling, where
# you want to make sure the file is closed regardless of any errors.

def try_except_finally():
    try:
        # Attempt to open the file 'example.txt' in read mode ('r')
        # If the file does not exist, a FileNotFoundError will be raised
        f = open("example.txt", "r")
        # Placeholder for file operations (e.g., reading data, processing content)
    except FileNotFoundError:
        # This block catches the FileNotFoundError if the file is not found.
        # It allows for custom error handling, like logging or notifying the user.
        print("The file was not found.")
    finally:
        # The 'finally' block is executed no matter what happens in the try or except blocks.
        # It's typically used for cleanup operations, such as closing files or releasing resources.
        try:
            # Try to close the file, but if the file was never opened due to an exception,
            # 'f' will not be defined. This results in a NameError, which needs to be caught.
            f.close()
        except NameError:
            # The NameError will be raised if 'f' was never assigned (because the file was not found).
            # This ensures that we handle the case where the file was not opened, avoiding further errors.
            print("File was not opened successfully.")

# Call the function to execute the file handling code
try_except_finally()

# Output (if the file is not found):
# The file was not found.
# File was not opened successfully.

# Tip: Use 'finally' for cleanup code that should always run, regardless of exceptions
# For example, always close a file, release a lock, or free resources in the 'finally' block.

# Advanced insight:
# It's good practice to keep the try block minimal and focused only on the operations that may raise an exception.
# This reduces the risk of catching unrelated errors and makes it easier to debug.
# Also, having a nested try block inside the 'finally' clause ensures that even if the resource (e.g., file) 
# was not successfully created, the program can still handle the situation gracefully without breaking.

# Use case: 
# This pattern is common when working with files, database connections, or network resources.
# Even when an error occurs, you want to ensure that resources are cleaned up properly to prevent 
# memory leaks or locked resources.

# Potential pitfalls:
# Be cautious when accessing variables inside the 'finally' block. As demonstrated above, 
# if the variable (like 'f' here) is not initialized due to an exception in the 'try' block, 
# accessing it in 'finally' could result in another exception (e.g., NameError). 
# Adding an additional try-except inside 'finally' is a good safeguard in such cases.

# Advanced tip: In newer Python versions, 'with' statements (context managers) 
# are preferred for managing resources like file I/O since they automatically handle 
# opening and closing resources, making the 'finally' block unnecessary for many use cases.
# However, understanding the 'try-except-finally' structure is still crucial for more complex 
# resource management scenarios where context managers may not apply.

#=================================================================================
# 8. Combining Else and Finally in exception handling
#=================================================================================

# The 'try-except-else-finally' structure in Python allows for robust and clear error handling.
# This example demonstrates how 'else' and 'finally' blocks are integrated within exception handling.

def full_exception_handling():
    # 'try' block: This is where the code that might raise exceptions is placed.
    try:
        # Taking input from the user and attempting to convert it to an integer.
        # This can raise a ValueError if the input is not a valid integer.
        x = int(input("Enter a number: "))
        
        # Performing a division operation.
        # This can raise a ZeroDivisionError if the user inputs 0.
        result = 10 / x
    
    # 'except' blocks: These handle specific exceptions that might arise from the 'try' block.

    except ValueError:
        # Handles cases where the input cannot be converted to an integer (e.g., if the user inputs a non-numeric value).
        print("Invalid input. Please enter a number.")
    
    except ZeroDivisionError:
        # Handles the case where the user inputs 0, causing a division by zero error.
        print("Cannot divide by zero!")
    
    # 'else' block: Executes if no exceptions were raised in the 'try' block.
    # This block runs only if both the 'ValueError' and 'ZeroDivisionError' are not triggered.
    else:
        # If the input is valid and no exceptions occurred, the result of the division is printed here.
        print(f"The result is: {result}")
    
    # 'finally' block: Always executes, regardless of whether an exception was raised or not.
    # This is used for cleanup actions or final statements that should always run after the try-except sequence.
    finally:
        # Regardless of success or failure, this will execute at the end of the function.
        # It's often used to release resources like files, network connections, or close a database.
        print("Execution completed.")

# To test the function, uncomment the line below and provide input as prompted:
# full_exception_handling()

# Output (depending on input):
# Case 1: Enter a valid number (e.g., 5)
#         5 => The result is: 2.0
#         Execution completed.

# Case 2: Enter a non-number (e.g., 'abc')
#         abc => Invalid input. Please enter a number.
#         Execution completed.

# Case 3: Enter zero (0)
#         0 => Cannot divide by zero!
#         Execution completed.

# Explanation of flow:
# - 'try': Executes the input and division logic.
# - 'except': Catches specific errors (ValueError for invalid input and ZeroDivisionError for division by zero).
# - 'else': Runs only if the 'try' block completes successfully, allowing further code to execute without interruption.
# - 'finally': Executes no matter what, making it ideal for final steps like cleanup or resource management.

# Use case:
# This structure is especially useful in scenarios where you want to clean up resources (e.g., file handling, database transactions) 
# or ensure that certain final operations are always performed, even if an error occurs.

# Advanced insight:
# The 'else' block is often underused but provides a clear separation between handling an exception and what should happen 
# if no exception occurred. Using 'else' can improve code readability by distinguishing between the normal flow of code execution 
# and the exception handling. 
# For example, you can place non-error-related logic in the 'else' block instead of inside the 'try', which focuses purely on potential exceptions.

# Best practices:
# 1. Keep the 'try' block minimal. Only include the code that might raise exceptions, so it's easier to track errors.
# 2. Use specific 'except' clauses to catch known exceptions. Avoid catching broad exceptions unless necessary.
# 3. 'finally' is essential for resource management, ensuring that resources are cleaned up regardless of success or failure.

# Potential pitfalls:
# 1. Overusing the 'try' block by placing too much logic inside it can make it hard to pinpoint where the error occurred.
# 2. Neglecting to use the 'else' block when appropriate can lead to code that mixes normal logic with exception-handling logic, reducing clarity.
# 3. Avoid placing critical code inside the 'finally' block that depends on the success of the 'try' block, as 'finally' always runs.

#=================================================================================
# 9. Raising Exceptions
#=================================================================================

# Raising exceptions is a fundamental way to handle invalid or unexpected conditions
# in Python. When an error condition is detected, the 'raise' statement is used to
# stop the normal flow of the program and signal that something went wrong.
# Exceptions can provide detailed feedback, enabling users to identify and correct issues.

# Example 1: A function to validate age using exception handling
# This function takes 'age' as an argument and checks whether it is a valid value.
# The raise statement triggers a ValueError if the age is negative or excessively high.

def validate_age(age):
    # Check if the provided age is negative
    if age < 0:
        # Raising a ValueError to indicate an invalid condition (negative age)
        raise ValueError("Age cannot be negative.")
    
    # Check if the provided age exceeds a reasonable upper limit (e.g., 120 years)
    if age > 120:
        # Raising a ValueError for the case where age is unreasonably high
        raise ValueError("Age is too high.")
    
    # If no exceptions are raised, the age is valid, so we return it
    return age

# Best practice: It’s important to use meaningful error messages to provide context.
# For example, "Age cannot be negative" clearly explains why the exception was raised.

# Example 2: Using a try-except block to handle exceptions
# Here, we invoke 'validate_age' and handle any potential ValueError exceptions.
# The try block allows us to attempt executing the function, and if an exception
# occurs, the program control jumps to the except block.

def raising_exceptions():
    try:
        # We are deliberately passing an invalid age (150) to trigger the exception
        validate_age(150)
    except ValueError as e:
        # When an exception is raised, it is caught here and handled gracefully
        # 'e' contains the exception message, which we print for debugging
        print(f"Invalid age: {e}")

# Call the function to see how exceptions are handled
raising_exceptions()  # Output: Invalid age: Age is too high.

# In this case, since 150 exceeds the allowed maximum (120), a ValueError is raised,
# and the exception is caught and printed.

# Advanced tip:
# Raising exceptions is a powerful technique to ensure robustness and maintainability.
# It's a good idea to raise exceptions as early as possible (sometimes called "fail fast")
# when encountering invalid input or unexpected states. This prevents the program from 
# executing with invalid data, which could lead to hard-to-debug errors later in the code.

# Another advanced practice is to create custom exception classes for more specific error handling.
# While built-in exceptions like ValueError, TypeError, etc., cover many cases, defining custom
# exceptions can make your code more modular and your error handling more precise.
# Example: You could define 'class AgeValidationError(ValueError)' to specifically handle age-related errors.

# Potential pitfalls:
# 1. Be careful not to raise too many generic exceptions, such as using ValueError or TypeError for unrelated issues.
#    This can confuse users of the code who may not understand the exact problem.
# 2. Avoid raising exceptions for flow control. While exceptions can handle unexpected conditions,
#    using them for routine control flow (such as breaking out of loops) can reduce readability and performance.
# 3. Ensure exceptions are handled properly. If exceptions aren't caught, they can cause the entire program to terminate unexpectedly.

# Summary:
# Use the 'raise' statement when invalid or unexpected conditions are encountered.
# Combine with try-except blocks to handle exceptions and prevent program crashes.
# Raising meaningful exceptions improves the clarity and robustness of your code.

#=================================================================================
# 10. Re-raising Exceptions
#=================================================================================

# Re-raising exceptions is a technique used when you want to catch an exception, handle part of it,
# but still allow the exception to propagate up the call stack for further handling.
# This can be useful when you want to log an error or perform some specific cleanup,
# but not suppress the exception entirely.

# Example: Re-raising a ZeroDivisionError exception
def re_raising_exceptions():
    try:
        # A deliberate division by zero error to trigger the exception
        x = 1 / 0  # This will raise a ZeroDivisionError immediately
    except ZeroDivisionError:
        # The exception is caught here first.
        # We can log the error, handle it in part, or perform specific actions like clean-up.
        print("Caught an error, re-raising...")  # Logs or prints a message when the exception is caught
        raise  # Re-raises the last exception, allowing it to propagate up the stack

# Now, we call the function that raises and re-raises the exception.
# We'll wrap the call in another try-except block to catch the re-raised exception.
try:
    re_raising_exceptions()  # This will cause a ZeroDivisionError, which is re-raised after being caught once
except ZeroDivisionError:
    # This will catch the re-raised ZeroDivisionError from the 're_raising_exceptions' function
    print("Caught re-raised exception")  # Confirms that the exception propagated up and was caught again

# Output:
# Caught an error, re-raising...
# Caught re-raised exception
# The output shows that the ZeroDivisionError was caught twice:
# first in the re_raising_exceptions function, and then again after it was re-raised.

# Advanced insight:
# Re-raising an exception can be particularly useful in multi-layered applications where an error occurs deep in the code.
# You can catch the error in an inner function, log it, perform local recovery steps, then re-raise it to allow the higher-level
# calling functions to handle or escalate the error appropriately.
# It also allows preserving the original traceback, which is important for debugging purposes.
# If a specific handling of exceptions is needed in multiple layers, this technique ensures errors are not silently consumed.

# Best practice:
# Be cautious when using 'raise' without specifying the exception, as it will re-raise the last caught exception.
# This is useful when you don't want to lose any details of the original exception, such as the traceback,
# which is often critical for debugging in larger applications. Avoid overusing this pattern if it's not necessary,
# as it can make the flow of exception handling harder to follow.

# Use case:
# Re-raising is typically used in scenarios where you want to log an error in a centralized manner 
# or when certain clean-up activities (like closing files, database connections) must be done locally 
# but the main error handling should happen at a higher level in the program.

# Pitfalls:
# If you re-raise an exception carelessly, it might make debugging harder if the exception is repeatedly caught and re-raised
# without appropriate handling. Ensure that the re-raising is intentional and serves a clear purpose, like logging or cleanup.
# For complex exceptions, consider using the 'raise from' syntax (Python 3 only), 
# which allows chaining exceptions and provides more context when exceptions are re-raised due to failures in nested try blocks.

#=================================================================================
# 11. Custom Exceptions
#=================================================================================

# Custom exceptions allow you to define error conditions that are specific to your application or use case.
# They provide more meaningful error messages and can include additional context such as error codes or other data.
# By inheriting from the built-in Exception class, you can create your own exceptions with custom behavior.
# This is useful for handling domain-specific errors in a structured way.

# Example 1: Defining a custom exception class
# This class inherits from Python's built-in Exception class, which is a base class for all exceptions.
# We use the __init__ method to allow the passing of a custom error message and an error code.
class CustomError(Exception):
    """A custom exception class"""
    def __init__(self, message, error_code):
        # Initialize with a custom message and error code
        # The message provides context about the error, and the error_code gives a way to categorize errors
        self.message = message  # Storing the custom error message
        self.error_code = error_code  # Storing the custom error code, typically for easier identification of error types
        # The 'super().__init__(self.message)' ensures that the base class's initializer is called with the error message,
        # which is important for integrating with Python's standard exception handling system.
        super().__init__(self.message)

# Example 2: Raising the custom exception
# In this function, we explicitly raise the custom exception.
# This could be useful in situations where specific conditions are met (e.g., invalid input, failed processes, etc.).
def raise_custom_error():
    # 'raise' is used to trigger the exception. This stops the normal flow of the program and jumps to exception handling (if provided).
    # Here, we simulate an error condition with a custom error message and an associated error code (e.g., 500 for server-related errors).
    raise CustomError("This is a custom error", 500)

# Example 3: Handling the custom exception with try-except
# When an exception is raised, it must be handled to prevent the program from crashing.
# In this block, we try to call 'raise_custom_error'. If the custom exception is raised, it will be caught in the 'except' block.
try:
    raise_custom_error()  # This will raise the CustomError defined above
except CustomError as e:
    # This block catches the CustomError and allows you to handle it gracefully.
    # Here, we print a message that includes the custom error message and the error code.
    # The 'e' variable holds the exception object, giving us access to its attributes (message, error_code).
    print(f"Caught custom error: {e.message} (Error code: {e.error_code})")

# Output: Caught custom error: This is a custom error (Error code: 500)

# Use case:
# Custom exceptions are typically used when you want to signal that something has gone wrong in a specific, application-defined way.
# For example, in an API, you might use custom exceptions to handle different types of request errors (e.g., invalid input, server issues).
# Another scenario could be validating business logic, where specific violations of rules should raise their respective exceptions.

# Advanced tip:
# You can further extend custom exceptions by adding more attributes or methods, such as logging or recovery mechanisms.
# For example, adding methods to log error details to a file or external service could help in debugging production issues.
# Custom exception classes can also be used in complex inheritance chains where exceptions have various levels of specificity, making the code
# more maintainable and easier to debug by categorizing different types of errors.

# Potential pitfalls:
# Avoid overusing custom exceptions. It's important to only create them when they add real value, such as making error handling
# clearer or when you need to attach extra information (like error codes).
# If not used judiciously, custom exceptions can lead to unnecessary complexity.
# As a best practice, always inherit from built-in exceptions unless you need very specific behavior that can't be achieved otherwise.

#=================================================================================
# 12. Exception Hierarchy
#=================================================================================

# Python's exception handling system follows a hierarchy, where some exceptions are subclasses of more general ones.
# This is important because specific exceptions should be caught before general ones in a `try-except` block to avoid unintended behavior.
# Below, we explore different types of exceptions and how they are caught based on their position in the hierarchy.

def exception_hierarchy():
    try:
        # This block tries various operations that could raise different exceptions.
        # Uncomment one at a time to see the effect of each exception.
        # 1 / 0  # Uncomment to raise ZeroDivisionError (subclass of ArithmeticError)
        # int('a')  # Uncomment to raise ValueError (when a string can't be converted to an integer)
        # open('nonexistent.txt')  # Uncomment to raise FileNotFoundError (subclass of IOError)
        raise KeyboardInterrupt  # Manually raising a KeyboardInterrupt for demonstration purposes
    except ArithmeticError:
        # This block catches all exceptions that fall under ArithmeticError, such as ZeroDivisionError
        # ArithmeticError is a base class for errors related to numeric calculations
        print("Caught an arithmetic error")
    except ValueError:
        # Catches ValueError, which occurs when a function gets an argument of the right type but inappropriate value
        print("Caught a value error")
    except IOError:
        # This block catches IOError and its subclasses, such as FileNotFoundError
        # IOError deals with input/output operation failures, e.g., file not found or inaccessible.
        print("Caught an I/O error")
    except KeyboardInterrupt:
        # Catches KeyboardInterrupt, raised when the user interrupts program execution, usually with Ctrl+C
        print("Caught a keyboard interrupt")

# Calling the function triggers the KeyboardInterrupt block, as the raised exception is handled by the last except clause
exception_hierarchy()  # Output: Caught a keyboard interrupt

# Explanation of the example:
# - First, the `try` block attempts several operations, each of which can raise different exceptions.
# - Only one except block will be executed, based on the exception that occurs. 
# - If multiple exceptions are possible, catching the more specific ones first is critical to avoid more general exceptions overriding specific ones.
# - In this case, the `KeyboardInterrupt` is raised manually, and so the corresponding except block is triggered.

# Exception Hierarchy:
# - Exceptions in Python follow a class hierarchy.
#   For example, ZeroDivisionError is a subclass of ArithmeticError, which is itself a subclass of the base Exception class.
# - When you write multiple except blocks, Python matches the exception raised to the first block that corresponds to the exception type or its superclass.
# - This means if you placed a more general exception, such as `Exception`, before more specific ones (e.g., `ArithmeticError`), it would catch all exceptions, including those you might want to handle separately.

# Advanced tip:
# - Understanding the exception hierarchy helps in structuring your except blocks properly.
#   Always catch the most specific exceptions first, then more general ones later.
#   For example, placing `Exception` at the top can make the rest of your except blocks redundant as it will catch all exceptions.
# - Python also has a `BaseException` class, which is the parent class of `Exception` and includes exceptions that are not typical runtime errors, such as `KeyboardInterrupt` and `SystemExit`.

# Potential Pitfalls:
# - Be cautious when catching broad exceptions such as `Exception` or `BaseException` as they may suppress important errors, such as system-exit events or programming bugs.
#   It is usually better to catch specific exceptions so that your program handles errors you expect while letting unexpected errors surface for debugging.
# - It's generally good practice to log or re-raise exceptions when necessary to avoid silent failure, especially in larger or production applications.

# Best Practice:
# - Only catch exceptions you know how to handle. If unsure about handling an exception, it is often better to let it propagate rather than obscure the root cause of a failure.


#=================================================================================
# 13. Using assert Statements
#=================================================================================

# The 'assert' statement in Python is primarily used for debugging purposes.
# It allows the developer to set a condition that must be true; if it evaluates to False, 
# the program will raise an AssertionError with an optional message.
# Assertions are best used to catch "should never happen" conditions, 
# rather than expected runtime errors (for which you should use exceptions).

# Example function that calculates the average of a list of numbers.
# It includes an assert statement to ensure that the list is not empty before proceeding.
def calculate_average(numbers):
    # 'assert' checks if the length of the list is greater than 0
    # If the list is empty (len(numbers) == 0), the condition is False, 
    # and an AssertionError is raised with the message "List is empty"
    assert len(numbers) > 0, "List is empty"
    
    # If the assertion passes, this line calculates and returns the average of the list
    return sum(numbers) / len(numbers)  # Sum of elements divided by the number of elements

# Handling the case when the assertion fails using a try-except block.
try:
    # Attempt to calculate the average of an empty list
    result = calculate_average([])  # This will trigger the assertion because the list is empty
except AssertionError as e:
    # The AssertionError is caught here, and the error message is printed
    print(f"Assertion failed: {e}")

# Output: Assertion failed: List is empty

# How assert works:
# - assert <condition>, <optional_message>
# - If the condition evaluates to True, the program continues.
# - If the condition is False, an AssertionError is raised, halting the program unless handled with a try-except block.

# Advanced tip:
# Assertions are intended for catching errors during development, not for handling runtime errors in production.
# They can be disabled globally by running Python with the '-O' (optimize) flag, which ignores all assertions.
# Thus, don't use assert for essential checks that must always run (e.g., checking user input in production code).
# Use standard error handling (like 'if' statements and exceptions) for those cases.

# Use case:
# Assertions are particularly useful in scenarios where certain assumptions about program state are made 
# and you want to ensure that those assumptions hold true while debugging or testing.
# For instance, in complex algorithms, you might use assert to ensure invariants (conditions that should always be true).

# Best practice:
# - Keep assert statements simple and clear, without side effects. 
#   For example, don't perform any critical logic or data modifications inside an assert condition.
#   Their purpose is to check the state of the program, not alter it.
# - The message in the assert should be descriptive enough to help identify the issue if the assertion fails.

# Pitfall:
# A common mistake is using assert to handle expected runtime conditions, such as user inputs or file existence.
# Remember, assertions can be disabled in optimized mode, so relying on them for important checks is unsafe.
# In production code, use proper exception handling (try-except) or conditional checks instead of assert.

#=================================================================================
# 14. Context Managers for Exception Handling
#=================================================================================

# Context managers are used to manage resources like file operations, database connections, or network sockets.
# They ensure that resources are properly acquired and released, even if an exception occurs.
# The contextlib module allows us to create our own context managers using the @contextmanager decorator.
# Below is an example of a custom context manager that handles resource management along with exception handling.

from contextlib import contextmanager  # Importing the contextmanager decorator

# Define a custom context manager using the @contextmanager decorator
@contextmanager
def managed_resource():
    try:
        # Resource acquisition happens here. This is where you "acquire" the resource.
        # For example, it could be a file, a database connection, etc.
        print("Resource acquired")  # This will run when the context manager starts
        yield "Resource"  # Yield the resource to the block inside the 'with' statement
        
        # Note: 'yield' temporarily hands over control back to the block using the 'with' statement.
        # Once the block finishes (or an exception occurs), execution resumes after the yield.
    except Exception as e:
        # Exception handling block. If any exception occurs inside the 'with' block, it is caught here.
        print(f"An error occurred: {e}")  # Print out the error message for the caught exception
    finally:
        # Resource release happens here. This block runs no matter what, ensuring proper cleanup.
        # Whether an exception is raised or not, the resource will always be released.
        print("Resource released")  # Resource cleanup message after context block completes

# Using the custom context manager with a 'with' statement
with managed_resource() as resource:
    # The 'with' statement initializes the context manager, executing the 'try' block up to the 'yield' statement
    # 'resource' now holds the value "Resource" from the yield in the managed_resource function.
    print(f"Using {resource}")  # Prints "Using Resource", demonstrating usage of the acquired resource
    raise ValueError("Something went wrong")  # Intentionally raising an exception to demonstrate error handling

# Output:
# Resource acquired
# Using Resource
# An error occurred: Something went wrong
# Resource released

# Explanation of flow:
# 1. The 'with' statement calls the context manager, triggering resource acquisition ("Resource acquired").
# 2. The 'yield' statement passes control to the block inside the 'with' statement, where the resource is used.
# 3. When an exception (ValueError) is raised inside the 'with' block, control jumps to the 'except' block, where the error is caught.
# 4. Regardless of whether an exception occurs, the 'finally' block is executed, releasing the resource ("Resource released").

# Advanced insights:
# Context managers are powerful when managing external resources that need guaranteed cleanup (e.g., file closing, connection shutdown).
# They eliminate the need for manual try-finally blocks, improving code readability and reducing the risk of resource leaks.
# In some scenarios, you can use a 'try-except-finally' block without a context manager, but context managers are more elegant and reusable.

# Use case example:
# Context managers are widely used for file operations. For instance, using 'with open(filename)' ensures that the file is automatically closed.
# Similarly, they are crucial in managing locks in multithreading (e.g., acquiring and releasing locks safely) or database transactions.

# Pitfalls to avoid:
# - Forgetting to handle exceptions in the 'with' block may lead to unexpected program crashes. Always anticipate potential exceptions when using context managers.
# - Misunderstanding how 'yield' works in a context manager can lead to confusion. The context manager pauses at 'yield' and resumes afterward, managing the entire lifecycle.

# Tip:
# Use context managers for any resource that needs explicit setup and teardown (e.g., opening/closing files, connecting/disconnecting from services, or locking/unlocking in multi-threading).

#=================================================================================
# 15. Chaining Exceptions (Python 3.3+)
#=================================================================================

# Python introduced exception chaining in version 3.3, allowing you to raise a new exception
# while keeping the original exception context. This is useful for providing more detail about
# errors while preserving the original exception that caused the issue.
# Chaining exceptions can be done using the 'from' keyword, which ties the new exception
# to the original one. This helps when debugging by showing both the new error and
# the root cause.

# Example: Chaining exceptions with a nested try-except block
def chain_exceptions():
    try:
        # The first 'try' block attempts to divide by zero, which raises a ZeroDivisionError.
        try:
            1 / 0  # Division by zero triggers ZeroDivisionError
        except ZeroDivisionError as e:
            # The 'from e' syntax chains the ZeroDivisionError to this new ValueError
            # This provides additional context: we want to raise a ValueError because of an invalid operation,
            # but still want to show that the root cause was the ZeroDivisionError.
            raise ValueError("Invalid operation") from e  # Chaining a ValueError from the original ZeroDivisionError
    except ValueError as e:
        # When the ValueError is caught here, it contains both the new message ("Invalid operation")
        # and a reference to the original exception (ZeroDivisionError).
        print(f"Caught: {e}")  # Display the caught ValueError message
        print(f"Original exception: {e.__cause__}")  # Access the original exception using the '__cause__' attribute

# Call the function to demonstrate exception chaining
chain_exceptions()

# Output:
# Caught: Invalid operation
# Original exception: division by zero

# Explanation of output:
# The output shows that the ValueError was raised due to an invalid operation,
# and the '__cause__' attribute provides the root cause (ZeroDivisionError: division by zero).
# This maintains a clear error trace, helping developers understand both the immediate error
# and the underlying issue.

# Use case:
# Chaining exceptions is especially helpful in complex codebases where different layers of the system
# interact. If an error occurs deep in the stack, raising a more meaningful exception
# while preserving the original cause can give context to higher-level logic or debugging efforts.
# For instance, if an invalid user input leads to a failure in multiple layers of processing,
# chaining exceptions can show both the user input error and the lower-level technical issue.

# Advanced tip:
# Python also implicitly chains exceptions if an exception is raised while another exception is already active.
# This can happen in cases where an exception occurs in an 'except' block or 'finally' block.
# Implicit chaining stores the original exception in the '__context__' attribute of the new exception.
# While explicit chaining ('from') is preferred for clarity, being aware of implicit chaining
# can help diagnose issues when multiple errors occur together.

# Potential pitfalls:
# - Overusing exception chaining can create verbose error traces, which may make debugging harder if not done carefully.
# - It’s important to provide meaningful messages for the new exceptions, rather than simply re-raising the original error,
#   which would add unnecessary complexity without providing additional value.
# - Always ensure that the chained exceptions provide distinct and helpful context. Otherwise, it can create confusion,
#   especially if the original exception is already descriptive enough.

# Best practice:
# Use explicit chaining (`from`) when a higher-level exception adds meaningful context to the lower-level error.
# Implicit chaining should be understood but managed carefully to avoid convoluted error messages.

#=================================================================================
# 16. Suppressing Exceptions (Python 3.3+)
#=================================================================================

# This example demonstrates how to suppress the original exception when raising a new one.
# In Python 3.3+, the 'raise ... from' syntax allows you to chain exceptions, which is useful
# for providing context when one exception leads to another. However, sometimes you may not
# want the original exception to appear in the traceback, which is where 'from None' comes in.

# Function to demonstrate exception suppression
def suppress_exception():
    # Outer try-except block to catch any exceptions raised in the inner block
    try:
        # Inner try-except block to trigger and handle the original exception
        try:
            1 / 0  # This will raise a ZeroDivisionError, as dividing by zero is not allowed
        except ZeroDivisionError:
            # Here, we catch the ZeroDivisionError, but instead of letting it propagate,
            # we raise a new exception (ValueError), indicating a more specific issue.
            # The 'from None' syntax is used to suppress the original exception (ZeroDivisionError),
            # so that it won't appear in the traceback. This keeps the error message cleaner and
            # avoids confusing the user with unnecessary details about the original error.
            raise ValueError("Invalid operation") from None
    # The outer 'except' block catches the ValueError raised above
    except ValueError as e:
        # Print the custom error message from the ValueError
        print(f"Caught: {e}")
        # Attempt to access the cause of the exception (i.e., the original exception).
        # Since 'from None' was used, the original exception (ZeroDivisionError) is suppressed,
        # and e.__cause__ will return None.
        print(f"Original exception: {e.__cause__}")

# Calling the function to see the exception handling in action
suppress_exception()

# Output:
# Caught: Invalid operation
# Original exception: None

# Explanation of the output:
# 1. The ZeroDivisionError occurs when attempting 1 / 0, but it gets caught.
# 2. A new ValueError is raised with the message "Invalid operation".
# 3. Because of the 'from None' statement, the traceback for the original ZeroDivisionError
#    is suppressed, and the output shows "Original exception: None" instead of displaying the cause.

# Advanced tip: 
# The 'raise ... from' syntax is especially useful when you want to maintain a clean exception 
# hierarchy while preserving the context for debugging or logging. However, if you want to hide 
# the original exception (perhaps for security reasons or to simplify the error message for users),
# using 'from None' allows you to suppress the chained exception.

# A more common use case for 'from None' might involve libraries or APIs where you want 
# to raise a user-friendly error message without exposing lower-level implementation details 
# (like a ZeroDivisionError or IndexError).

# Potential pitfalls:
# - Misusing 'from None' can make debugging more difficult if you suppress an exception 
#   that would provide valuable context for identifying the root cause of an error.
#   It's best used when the original exception doesn't add meaningful information or could
#   confuse the end user.
# - Always ensure that raising a new exception actually provides better clarity than the original 
#   one. In some cases, chaining exceptions without suppression (i.e., without 'from None') 
#   might offer better visibility for debugging purposes.

#=================================================================================
# 17. Exception Groups (Python 3.11+)
#=================================================================================

# Exception groups, introduced in Python 3.11, provide a way to handle multiple exceptions
# raised during execution as a single "group" of exceptions.
# This is especially useful when dealing with tasks like batch processing, where multiple errors
# can occur simultaneously, and you want to collect and process them as a group.

# The 'ExceptionGroup' class allows you to encapsulate multiple exceptions into one,
# and the 'except*' clause lets you catch specific exceptions from the group.

from exceptiongroup import ExceptionGroup  # Importing the ExceptionGroup class for grouping exceptions

# Function to process a list of 'data'
def process_data(data):
    errors = []  # List to collect any errors encountered during processing
    
    for item in data:  # Loop through each 'item' in the 'data' list
        try:
            # Simulate processing of the item (in real cases, this could be any operation)
            if item < 0:  # If the item is negative, it raises a ValueError
                raise ValueError(f"Negative value: {item}")  # Custom error message with the problematic value
        except ValueError as e:  # Catch the ValueError raised above
            errors.append(e)  # Add the caught exception to the 'errors' list
    
    # After processing all items, if any errors were encountered, raise them as a group
    if errors:  # If there are any exceptions in the 'errors' list
        raise ExceptionGroup("Processing errors", errors)  # Raise them as an ExceptionGroup with a description

# Example use case where multiple data items are processed, and some could raise errors
try:
    # Passing a list with both positive and negative integers
    process_data([1, -2, 3, -4])  # This will raise ValueErrors for -2 and -4
except* ValueError as eg:  # The 'except*' syntax catches exceptions of the specified type from the group
    print(f"Caught {len(eg.exceptions)} ValueError(s):")  # Prints how many ValueErrors were caught in the group
    for i, e in enumerate(eg.exceptions, 1):  # Loop through each individual exception in the group
        print(f"  {i}. {e}")  # Print the index and the exception message

# Output:
# Caught 2 ValueError(s):
#   1. Negative value: -2
#   2. Negative value: -4

# This example demonstrates how multiple exceptions raised during the processing of a list
# can be handled together using ExceptionGroup. Two ValueErrors were raised for -2 and -4,
# which were grouped into a single exception and caught using the 'except*' clause.

# Advanced use cases:
# Exception groups are particularly useful when working with parallel or asynchronous tasks
# where multiple errors may occur simultaneously. Instead of handling each error separately,
# ExceptionGroup allows you to aggregate them and handle them all at once.
# This can also simplify error handling in batch processing, data pipelines, or network requests.

# Best practice:
# Only use ExceptionGroup when multiple exceptions are expected, such as in scenarios
# where you're processing multiple independent tasks that might fail.
# This avoids unnecessary complexity in simple use cases where a single exception is expected.

# Potential pitfalls:
# The 'except*' clause is new to Python 3.11+, so if backward compatibility with earlier
# versions is required, you should avoid using this syntax or provide an alternative for those versions.
# Ensure that you clearly distinguish between 'except' and 'except*'—the former catches
# a single exception (or its subclasses), while the latter catches exceptions of a specific type within an ExceptionGroup.

#=================================================================================
# 18. Best Practices and Tips for Exception Handling in Python
#=================================================================================

# Exception handling is a critical part of writing robust and maintainable Python code.
# It helps you gracefully manage errors and edge cases in your application.
# Below are best practices and tips to elevate your understanding and implementation of exception handling.

# 1. Be specific with your exception handling. Catch specific exceptions, not just Exception.
#    Catching broad exceptions like 'Exception' can mask real issues and make debugging harder.
#    It's better to catch specific exceptions such as ValueError, TypeError, or KeyError.
try:
    value = int("abc")  # This will raise a ValueError since "abc" cannot be converted to an integer
except ValueError:  # Catching a specific exception
    print("Conversion failed: Invalid integer value")

# Bad practice: catching all exceptions (including system-level errors)
# except Exception:  # This would catch all exceptions, including ones you might not want to handle
#     print("An error occurred")  # This hides the root cause and makes debugging more difficult

# 2. Use 'finally' for cleanup code that must always run.
#    The 'finally' block is useful for code that needs to run regardless of whether an exception occurred or not.
try:
    file = open("data.txt", "r")  # Attempt to open a file
    # Some file operations here
except FileNotFoundError:  # Handling specific file-related error
    print("File not found")
finally:
    # This block will always run, even if an exception occurs.
    # It's ideal for cleanup tasks, such as closing a file or releasing resources.
    print("Cleanup action: Closing the file.")
    if 'file' in locals() and not file.closed:
        file.close()

# 3. Don't catch exceptions you can't handle properly.
#    If you catch an exception, make sure you have a valid reason and can properly handle it.
#    Swallowing exceptions without handling them properly can lead to silent failures.
try:
    result = 10 / 0  # This raises a ZeroDivisionError
except ZeroDivisionError:  # Only catch if you can meaningfully handle the exception
    print("Cannot divide by zero")
# Good practice: If you're unsure how to handle it, let the exception propagate up.

# 4. Use 'else' clause for code that should only run if no exception occurred.
#    The 'else' clause ensures that code runs only if no exceptions are raised in the 'try' block.
try:
    result = 10 / 2  # This won't raise an exception
except ZeroDivisionError:
    print("Division by zero error")
else:
    # Runs only if no exception occurs
    print("Successful division:", result)
# The 'else' block makes the code more readable by separating the normal execution flow from the exception handling.

# 5. Raise exceptions early, catch them late.
#    Raising exceptions early means detecting problems as soon as possible and raising an exception immediately.
#    Catch them as late as possible, at the level where you can handle them meaningfully.
def validate_input(value):
    if not isinstance(value, int):
        raise TypeError("Expected an integer")  # Raising an exception early to avoid issues later
validate_input(10)  # No exception
# Catching the exception later in the main execution flow where it can be handled properly.

# 6. Use custom exceptions for application-specific errors.
#    Custom exceptions make your error handling more meaningful and readable in the context of your application.
class InvalidConfigurationError(Exception):
    """Custom exception for invalid configuration errors."""
    pass
# Now you can raise this specific exception when a configuration issue occurs.
raise InvalidConfigurationError("Configuration file is missing required fields")

# 7. Use context managers (with statements) for resource management.
#    Context managers help manage resources like files or network connections, ensuring they're cleaned up properly.
#    You don't need to manually handle closing files or connections.
with open("data.txt", "r") as file:
    content = file.read()  # No need for a 'finally' block to close the file, 'with' does it automatically
# Context managers are cleaner and less error-prone than manually managing resources.

# 8. Don't use exceptions for flow control in normal operations.
#    Exceptions are meant for exceptional situations, not for controlling normal program flow.
#    Using exceptions for flow control can lead to hard-to-read and inefficient code.
try:
    value = int("abc")  # This raises an exception
except ValueError:  # Handling the exception
    value = 0  # Setting a default value
# Instead of this, it's often better to use normal conditionals to check for errors.
# Preferred way:
value = "abc"
if value.isdigit():  # Check if it's a valid number first
    value = int(value)
else:
    value = 0

# 9. Log exceptions for debugging purposes.
#    Always log exceptions, especially in production code, so you have traceable records for debugging.
import logging
logging.basicConfig(level=logging.ERROR)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Error occurred: %s", e)  # Logs the exception details for future review

# 10. Use exception chaining to provide more context about errors.
#     Exception chaining using 'raise ... from' lets you provide context about the original exception while raising a new one.
try:
    raise ValueError("Initial error")
except ValueError as e:
    raise RuntimeError("New error with more context") from e  # Keeps the original exception context

# 11. Use assertions for debugging and internal checks, not for data validation.
#     Assertions should be used for sanity checks during development, not for validating user input or external data.
assert 2 + 2 == 4  # This should always be true; if not, it will raise an AssertionError
# Avoid using assertions for runtime data validation; use explicit exceptions for that.

# 12. Be aware of the performance impact of try/except blocks in critical loops.
#     Try/except blocks have a small overhead, but when placed inside performance-critical loops, they can cause slowdowns.
#     If you're inside a loop, especially one that runs many iterations, minimize exception handling within the loop body.
for i in range(1000000):
    try:
        result = 10 / i  # Risk of ZeroDivisionError, but it only occurs once
    except ZeroDivisionError:
        result = 0  # This exception handling is necessary but can affect performance if frequent

# Advanced tip: 
# It's generally better to handle exceptions outside the loop in most cases unless each iteration requires independent handling.

#=================================================================================
# 19. Debugging with pdb (Python Debugger)
#=================================================================================

# The Python Debugger (pdb) is a powerful tool for debugging your code.
# It allows you to set breakpoints, inspect variables, step through code line by line, 
# and even modify the program's state during runtime.
# Below is an example where pdb is used to debug a function that will raise an exception.

import pdb  # Importing the pdb module, which is Python's built-in debugger

# A simple function that will trigger a division by zero error.
# pdb.set_trace() is used to start debugging right before the error occurs.
def buggy_function():
    x = 5  # Assigning 5 to variable 'x'
    y = 0  # Assigning 0 to variable 'y', which will cause a division by zero error
    pdb.set_trace()  # Starts the debugger at this point in the code
    result = x / y  # This line will raise a ZeroDivisionError
    return result  # This return statement will not be reached due to the error

# To test this function and start debugging, uncomment the following line:
# buggy_function()

# Here's how pdb works when you run the function:
# - Execution will stop at the line with 'pdb.set_trace()'.
# - You'll enter an interactive debugging session in the terminal.
# - You can use pdb commands like 'n' (next), 's' (step into), 'p <variable>' (print the value of a variable), etc.

# Example pdb commands:
# - 'n' (next): Moves to the next line of code.
# - 's' (step): Steps into a function call.
# - 'p <variable>': Prints the value of a variable (e.g., p x will print 5).
# - 'c' (continue): Continues execution until the next breakpoint or error.
# - 'q' (quit): Exits the debugger.

# Tip: 
# Starting with Python 3.7, you can use 'breakpoint()' as a more convenient alternative to 'pdb.set_trace()'.
# 'breakpoint()' is more flexible because it respects the PYTHONBREAKPOINT environment variable,
# allowing you to easily swap out debuggers or disable breakpoints entirely.

# Example:
# Instead of 'pdb.set_trace()', you could write:
# breakpoint()
# This would function exactly the same but is easier to use and more readable.

# Advanced debugging tip:
# When debugging complex applications, you can set multiple breakpoints at different points in your code
# to inspect variables and step through the logic. You can also conditionally break only if a certain
# condition is met, like so:
# pdb.set_trace() if condition else None
# This can help you focus on specific issues without stopping execution unnecessarily.

# Additionally, you can integrate pdb with automated testing frameworks like pytest. For instance,
# running 'pytest --pdb' will drop you into a pdb session automatically if a test fails, 
# allowing you to inspect and debug the issue immediately.

# Potential pitfalls:
# One common mistake is leaving pdb.set_trace() or breakpoint() in your production code.
# Always ensure that you remove or disable these breakpoints before deploying the code to production, 
# as they can pause execution unexpectedly and affect performance.

# This concludes the enhanced detailed Python Cheat Sheet for Exception Handling