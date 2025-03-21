#===============================================================================
# Python Cheat Sheet: Debugging and Profiling
#===============================================================================

# In this section, we will cover debugging techniques using pdb (Python Debugger),
# which is a powerful tool for inspecting and controlling code execution in Python.

# 1. Debugging with pdb (Python Debugger)
import pdb  # Import the pdb module for debugging

def complex_function(x, y):
    # This function performs a simple calculation and demonstrates debugging
    result = x + y  # Initialize the result by adding x and y
    pdb.set_trace()  # Set a breakpoint; execution will pause here allowing inspection
    for i in range(5):  # Loop through the range of 5
        result *= i + 1  # Multiply result by (i + 1)
    return result  # Return the final computed result

# To run the function and enter the debugger:
# complex_function(3, 4)

# Basic pdb commands:
# n (next) - Execute the current line and move to the next line of code
# s (step) - Step into a function call, allowing you to debug that function
# c (continue) - Continue execution until the next breakpoint is reached
# p variable_name - Print the value of a variable (e.g., p result)
# l (list) - Show the current location in the code, providing context
# q (quit) - Exit the debugger and terminate the program

# Advanced tip: Instead of pdb.set_trace(), which is more verbose,
# consider using breakpoint() starting from Python 3.7+.
# It can automatically route to the appropriate debugger based on the configuration.

# Post-mortem debugging
def buggy_function():
    # This function will raise a ZeroDivisionError to demonstrate post-mortem debugging
    x = 5
    y = 0  # Division by zero will occur here
    return x / y  # This line will raise an error

try:
    buggy_function()  # Attempt to call the buggy function
except ZeroDivisionError:
    import pdb  # Import pdb only when needed
    pdb.post_mortem()  # Start post-mortem debugging to inspect the error context

# Conditional breakpoints
x = 10  # Example variable for demonstration
if x > 5:  # Conditional check
    breakpoint()  # Trigger a breakpoint if the condition is true

# Advanced tip: Control the behavior of breakpoints using the PYTHONBREAKPOINT environment variable.
# This allows for flexible debugging without changing the code.
# Examples of setting this variable in a shell:
# export PYTHONBREAKPOINT=0  # Disable all breakpoints
# export PYTHONBREAKPOINT=pdb.set_trace  # Set the default to use pdb for breakpoints

# Using pdb in command line
# You can also run pdb directly from the command line to debug an entire script.
# The command format is:
# python -m pdb script.py
# This allows you to step through the script execution from the start.

# In summary, mastering pdb can significantly enhance your debugging skills,
# making it easier to track down and resolve issues in your code.
# Always ensure to remove or disable breakpoints in production code to avoid unintended behavior.

#===============================================================================
# 2. Debugging with IDEs
#===============================================================================

# Debugging is a critical skill in software development, allowing developers to identify and resolve errors effectively.
# Most Integrated Development Environments (IDEs) like PyCharm and Visual Studio Code come equipped with powerful graphical debuggers.
# This section outlines the common features and best practices for debugging with IDEs.

# Most IDEs provide a graphical interface for debugging, making it easier to track down issues in code.
# This visual approach can help you understand the program flow and state at various points in execution.

# Common features of IDE debuggers include:

# 1. Setting breakpoints
# Breakpoints allow you to pause the execution of your program at specific lines of code.
# This is invaluable for inspecting the state of the program at a critical point.
# Example: 
print("Setting a breakpoint at line 10")  # You would set a breakpoint here in your IDE
# When the program execution reaches this line, it will pause, allowing you to examine variables and the call stack.

# 2. Step over, step into, step out
# - Step over: Execute the next line of code without entering any function calls. 
# This is useful when you want to skip over functions that you know are working correctly.
# Example:
print("Step over to the next line")  # Use this option to move to the next line without going inside any function

# - Step into: Move into the function called on the current line to debug it line by line.
# This is helpful when you suspect the issue lies within the function being called.
# Example:
print("Step into the function for detailed inspection")  # Use this option to investigate the function's execution

# - Step out: Complete the execution of the current function and return to the calling function.
# This is useful when you've finished inspecting a function and want to return to the broader context.
# Example:
print("Step out to return to the calling function")  # Use this option to exit the current function context

# 3. Variable inspection
# Inspecting variables allows you to see the current state of all variables at the breakpoint.
# This helps in understanding if the variables hold the expected values and diagnosing issues.
# Example:
print("Inspect variable values in the IDE's variables panel")  # Check current variable states at this point in execution

# 4. Watch expressions
# Watch expressions let you monitor the value of specific variables or expressions as you step through the code.
# This is useful for tracking changes in state without manually inspecting them at each step.
# Example:
print("Watch specific variables for changes in their state")  # Add variables to the watch list in the IDE

# 5. Call stack examination
# The call stack shows the sequence of function calls that led to the current point of execution.
# Understanding the call stack helps you trace back the origin of errors or unexpected behavior.
# Example:
print("Examine the call stack to trace function calls leading to this point")  # Look at the stack for function call sequence

# Tip: Learn keyboard shortcuts for efficient debugging in your IDE
# Mastering keyboard shortcuts can significantly speed up your debugging process.
# Common shortcuts include:
# - F5 (Start debugging)
# - F10 (Step over)
# - F11 (Step into)
# - Shift+F11 (Step out)
# Example:
print("Using keyboard shortcuts for debugging efficiency")  # Practice using shortcuts to streamline your workflow

# Advanced Tip:
# Consider using conditional breakpoints to pause execution only when certain conditions are met.
# This can reduce the number of times you need to stop and start debugging, making the process smoother.
# Example:
print("Set a conditional breakpoint for specific variable states")  # This allows you to skip unnecessary stops in execution

# Potential pitfalls:
# Relying solely on debugging tools can lead to overlooking the importance of code reviews and unit tests.
# Debuggers are powerful, but they should complement good coding practices, not replace them.
# Example:
print("Balance debugging with thorough testing and code reviews")  # Maintain good practices to ensure code quality

#===============================================================================
# 3. Logging for Debugging
#===============================================================================

# The logging module in Python is a powerful tool for tracking events that happen 
# during execution, which can be incredibly helpful for debugging and monitoring applications.

import logging  # Importing the logging module to utilize its capabilities

# Configuring the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the threshold for the logger to DEBUG level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Define the output format of log messages
)
# The format includes the timestamp, the severity level of the log message, 
# and the actual message itself. This helps in identifying when an event occurred 
# and its significance.

# Example function that performs division and logs its progress
def divide(x, y):
    logging.debug(f'Dividing {x} by {y}')  # Log the values of x and y at DEBUG level
    try:
        result = x / y  # Attempt to perform the division
    except ZeroDivisionError:
        logging.error('Division by zero!')  # Log an error message if division by zero occurs
        raise  # Reraise the exception to propagate it up the call stack
    logging.info(f'Result: {result}')  # Log the result at INFO level
    return result  # Return the computed result

# Tips for logging:
# Use different logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) 
# to provide appropriate granularity in log messages. This allows developers 
# to filter messages based on their severity, making it easier to focus on relevant information.

# Example usage of the divide function
try:
    print(divide(10, 2))  # Expected output: 5.0
    print(divide(10, 0))  # This will trigger a ZeroDivisionError
except ZeroDivisionError:
    print("Caught an exception: Division by zero is not allowed.")

# In the output log, the following messages would appear for the first call:
# [timestamp] - DEBUG - Dividing 10 by 2
# [timestamp] - INFO - Result: 5.0

# For the second call, the log would contain:
# [timestamp] - DEBUG - Dividing 10 by 0
# [timestamp] - ERROR - Division by zero!

# Best practices for logging:
# 1. Choose appropriate logging levels based on the message's significance. 
#    DEBUG for detailed information, INFO for routine messages, WARNING for potentially problematic situations,
#    ERROR for serious issues, and CRITICAL for very serious errors.
# 2. Avoid excessive logging in production environments to prevent performance issues and cluttered logs.
# 3. Consider logging to different outputs (files, streams, etc.) to facilitate monitoring and error tracking.
# 4. Utilize logging exceptions for stack traces when catching exceptions, which aids in troubleshooting.
# 5. Ensure sensitive information is not logged, especially in production systems.

# Advanced tips:
# 1. Leverage structured logging to include context about the application state, which can improve the analysis of logs.
# 2. Integrate logging with external monitoring systems for real-time alerts on critical errors.
# 3. Utilize log rotation to manage log file sizes and prevent disk space issues in long-running applications.

# Potential pitfalls:
# 1. Using too many debug logs can clutter the output and make it harder to find relevant information.
# 2. Failing to set appropriate logging levels can lead to missed important messages or an overload of insignificant logs.
# 3. Not configuring log file handling can lead to lost logs in the event of application crashes or high-load scenarios.

#===============================================================================
# 4. Assertions for Debugging
#===============================================================================

# Assertions are a debugging aid that tests a condition as a way to catch 
# programming errors. If the condition evaluates to False, an AssertionError 
# is raised with an optional error message. Assertions should be used to check 
# for conditions that should never happen if the code is correct.

# Example: Calculate average of a list of numbers
# The following function calculates the average of a list. 
# Before proceeding with the computation, it asserts that the input list is not empty.
def calculate_average(numbers):
    # Assertion to check if the list is non-empty
    assert len(numbers) > 0, "List is empty"  # Raises an AssertionError if the condition is False
    
    # Calculate and return the average
    return sum(numbers) / len(numbers)  # Returns the average by dividing the total sum by the number of elements

# Use case:
# The function can be used in various scenarios where average calculations are necessary,
# such as in statistical analyses or performance metrics. It's crucial to ensure that 
# the input list is valid (non-empty) before performing operations that depend on it.

# Example usage:
try:
    print(calculate_average([10, 20, 30]))  # Outputs: 20.0
    print(calculate_average([]))  # Raises AssertionError: List is empty
except AssertionError as e:
    print(e)  # Catches and prints the assertion error message

# Tip: Use -O flag to disable assertions in production code
# When running Python scripts with the -O (optimize) flag, 
# all assert statements are ignored, which can improve performance.
# Example command to run the script with optimizations:
# python -O script.py

# Important considerations:
# - Assertions are meant to catch programmer errors, not user errors. 
# They should not be used for validating input from users or external sources.
# - Use assertions during development to verify assumptions and 
# to help with debugging; however, avoid using them for essential runtime checks 
# that could lead to application failure if violated.
# - Be cautious with heavy reliance on assertions in performance-critical sections 
# of code, as they can introduce overhead if not managed appropriately.

# Advanced tip:
# Consider using logging or error handling (try-except blocks) for runtime checks, 
# especially for inputs from external sources. This provides a more graceful way 
# to handle errors in production environments, as assertions are typically removed 
# in optimized runs, making it harder to diagnose issues that arise when they are 
# disabled. Assertions serve well for sanity checks during development.


#===============================================================================
# 5. Profiling Code for Performance
#===============================================================================

# Profiling is essential for identifying bottlenecks in code and optimizing performance.
# This section covers tools for profiling CPU and memory usage in Python programs.

# Example 1: Using cProfile
# cProfile is a built-in Python module for profiling the execution time of functions.
# It provides a detailed report of how much time is spent in each function.
import cProfile

# Fibonacci function implementation - a classic example, but inefficient for large 'n'.
def fibonacci(n):
    if n < 2:
        return n  # Base case: return n for 0 and 1
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive calls to calculate Fibonacci numbers

# Profiling the Fibonacci function with cProfile
# This line will execute fibonacci(30) and generate a profiling report.
cProfile.run('fibonacci(30)')  # This will output the time taken for each function call.

# Tip: Sort the output by cumulative time to identify which functions consume the most time.
# To do this, you can modify the run command as follows:
# cProfile.run('fibonacci(30)', sort='cumtime')

# This provides insights on which calls lead to the most cumulative time usage, aiding in optimization.

# Example 2: Using line_profiler for line-by-line profiling
# Line-by-line profiling gives a more granular view of performance.
# It requires the installation of line_profiler via pip: pip install line_profiler

# Marking the function to be profiled using the @profile decorator
@profile
def slow_function():
    total = 0  # Initialize total for summation
    for i in range(1000000):  # Loop over a large range
        total += i  # Accumulate the sum
    return total  # Return the calculated total

# To run this profiling, execute the script using:
# kernprof -l -v script.py
# This command will generate a detailed report showing the time taken for each line.

# Example 3: Using memory_profiler to profile memory usage
# Memory profiling helps track memory consumption, which is crucial for optimizing resource usage.
# This requires installing the memory_profiler: pip install memory_profiler

from memory_profiler import profile  # Importing the profile decorator from memory_profiler

@profile
def memory_hungry_function():
    # This function creates a large list, showcasing memory consumption.
    return [i for i in range(1000000)]  # Generates a list of one million integers.

# To execute this memory profiling, run the script using:
# python -m memory_profiler script.py
# This will provide insights into how much memory is used at each line in the function.

# Tip: Use mprof for plotting memory usage over time
# mprof is another tool that helps visualize memory usage over time.
# To use it, run the following commands:
# mprof run script.py  # This command runs the script while tracking memory usage
# mprof plot           # This command plots the tracked memory usage

# In summary, effective profiling of both time and memory can lead to significant improvements
# in performance. Use the right tools based on the specific performance aspect you want to analyze.
# Understanding where time and memory are being consumed is key to optimizing and enhancing the efficiency
# of your code. Make sure to profile in a realistic environment to gather accurate data for optimization.


#===============================================================================
# 6. Timing Code Execution
#===============================================================================

# Timing code execution is crucial for performance optimization, helping developers 
# identify bottlenecks and improve efficiency. Python provides various tools to measure 
# execution time, with the 'time' module and the 'timeit' module being among the most commonly used.

# Example 1: Basic timing using the time module
import time  # Importing the time module to access time-related functions

start_time = time.time()  # Record the start time (in seconds since the epoch)
# Your code here
# This is where the code you want to measure goes. Replace with any block of code.
end_time = time.time()  # Record the end time after the code execution
execution_time = end_time - start_time  # Calculate the execution time by subtracting start from end
print(f"Execution time: {execution_time} seconds")  # Print the measured execution time

# Use case: This approach is straightforward and works well for measuring the time taken 
# by small blocks of code. However, it may not be suitable for measuring very short execution times 
# due to the overhead of time measurement itself.

# Example 2: Using timeit for more accurate timing
# The timeit module provides a simple way to time small bits of Python code with less overhead.
import timeit  # Importing the timeit module for performance measurement

# Define a function that we want to time
def function_to_time():
    return sum(range(1000000))  # Sum the numbers from 0 to 999999

# Measure the execution time of the function, running it 10 times to average out results
execution_time = timeit.timeit(function_to_time, number=10)  
# number=10 indicates the function will be executed 10 times for averaging

# Calculate the average execution time per execution
average_execution_time = execution_time / 10  
print(f"Average execution time: {average_execution_time} seconds")  # Print the average execution time

# Use case: The timeit module is ideal for measuring the performance of small code snippets 
# because it avoids common pitfalls like background processes affecting results. 
# It handles setup and teardown code gracefully, allowing more accurate measurements.

# Advanced tip: For quick timing in IPython or Jupyter notebooks, use the %timeit magic command.
# This command automatically runs the code multiple times and provides the best average time.
# %timeit function_to_time()  # Uncomment this line to use in IPython/Jupyter

# Potential pitfalls:
# - When using the time module, be cautious with measuring very fast code execution times, 
# as the resolution might not be sufficient to capture small time differences accurately.
# - Avoid including time measurement in production code unless necessary, as it can introduce 
# overhead and affect performance, especially if misused in critical paths.
# - Ensure that the code being measured is representative of the actual workloads expected 
# in the application, as benchmarks can vary significantly based on different factors.


#===============================================================================
# 7. Profiling with cProfile and visualization
#===============================================================================

# Profiling is essential for understanding the performance characteristics of Python code.
# The cProfile module provides a way to measure where time is being spent in your application.

# Importing the necessary modules for profiling and analyzing performance
import cProfile  # Provides profiling of Python programs
import pstats    # Provides classes for reading and analyzing profile statistics
from pstats import SortKey  # Allows sorting of statistics by various keys

# Example: Profile a specific piece of code
# The 'run' method executes the specified statement and collects profiling data.
# Here, we're profiling the execution of the 'fibonacci(30)' function and saving the stats to 'output.prof'.
cProfile.run('fibonacci(30)', 'output.prof')

# When profiling, it’s important to choose representative examples of your actual workload.
# This will ensure that the profiling results are meaningful.

# Analyzing the results
# After profiling, you can analyze the results to understand the time spent in different functions.
# The following code snippet opens a file to write the statistics.
with open('output_stats.txt', 'w') as f:
    # Create a Stats object from the profile data
    p = pstats.Stats('output.prof', stream=f)
    
    # Sorting the statistics by cumulative time spent in each function
    p.sort_stats(SortKey.CUMULATIVE).print_stats(10)  # Print the top 10 stats

# Tip: Use snakeviz for visualization
# Visualizing profiling data can help identify bottlenecks quickly and intuitively.
# Snakeviz is a graphical viewer for the output of Python's profiling tools.
# To install snakeviz, run the following command in your terminal:
# pip install snakeviz

# Once installed, you can run the following command to visualize the profiling data:
# snakeviz output.prof
# This command opens a web-based interface to explore the profiling data interactively.

# Advanced tip:
# While cProfile is a powerful tool, consider using it in combination with other profiling tools like memory_profiler
# to get a comprehensive understanding of both time and space performance.
# Memory leaks can often be as detrimental as slow code, so profiling both aspects is ideal.

# Potential pitfalls:
# Avoid profiling code that has side effects or relies on external systems unless you can control those aspects.
# This can lead to inconsistent results. Always aim to profile pure functions or those with known inputs and outputs.
# Additionally, profiling can introduce overhead, so be cautious about interpreting results from small datasets or brief execution times.


#===============================================================================
# 8. Using tracemalloc for memory tracking
#===============================================================================

# tracemalloc is a built-in Python library that helps track memory allocations.
# It is particularly useful for identifying memory leaks and optimizing memory usage
# in Python applications. This tool captures snapshots of memory allocations, allowing
# developers to analyze memory usage over time.

import tracemalloc  # Import the tracemalloc module

# Start tracing memory allocations. This must be called before any memory allocations
# are made to get accurate tracking results.
tracemalloc.start()

# Your code here
# Place the code that you want to analyze for memory usage below this comment.
# For demonstration purposes, you could create a list of large objects or perform 
# operations that involve significant memory usage.

# Example: Creating a large list of integers to simulate memory allocation
large_list = [i for i in range(100000)]  # Allocate memory for 100,000 integers

# After executing the code you want to analyze, take a snapshot of the current memory usage.
# This captures the state of memory allocations at this point in time.
snapshot = tracemalloc.take_snapshot()

# Retrieve memory statistics, grouping by line number to see where the most memory
# is being allocated in the code. This allows developers to pinpoint memory-intensive
# lines or operations.
top_stats = snapshot.statistics('lineno')

# Print the top 10 lines of code consuming the most memory.
print("[ Top 10 ]")
for stat in top_stats[:10]:
    # Each stat provides detailed information about memory allocation, including the line number
    # where the allocation occurred and the amount of memory used.
    print(stat)

# Output example:
# [ Top 10 ]
# <filename>:<line_number>: <memory_usage> bytes
# ...
# Each printed line will indicate the file and line number where the memory allocation occurred,
# helping identify potential issues with memory usage.

# Advanced tip:
# When using tracemalloc, consider taking multiple snapshots at different points in your code.
# This allows you to compare memory usage over time and understand how specific code changes 
# affect memory allocation patterns. 

# Potential pitfalls:
# Be mindful that tracing memory can introduce overhead, slightly affecting performance.
# Therefore, it is best to enable tracemalloc only during debugging or when investigating 
# memory issues in a controlled environment, rather than in production code.

# Remember to disable tracemalloc with tracemalloc.stop() when you no longer need it to avoid 
# unnecessary memory tracking and potential performance impacts.

#===============================================================================
# 9. Debugging Multithreaded Applications
#===============================================================================

# Multithreading allows concurrent execution of code, which can improve performance 
# for I/O-bound tasks but introduces complexity in debugging due to shared state.
# Below are best practices and examples for debugging multithreaded applications.

import threading  # Importing the threading module to work with threads
import logging  # Importing the logging module for logging debug messages

# Configure the logging system to display messages with level DEBUG or higher.
# The format includes the thread name for easier identification of messages.
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s')

# Example 1: Worker function simulating some work in a thread
# This function will be executed by each thread, performing a task and logging its progress.
def worker():
    logging.debug('Starting')  # Log that the worker has started
    # Simulate a task that takes some time to complete (e.g., I/O operation)
    import time  # Import time here to avoid unnecessary imports at the top
    time.sleep(2)  # Pause execution for 2 seconds
    logging.debug('Exiting')  # Log that the worker has finished

# Example 2: Main function that starts multiple threads
# This function creates and starts two threads that execute the worker function.
def main():
    # Creating and starting the first worker thread
    threading.Thread(target=worker, name='Worker-1').start()
    # Creating and starting the second worker thread
    threading.Thread(target=worker, name='Worker-2').start()

# Note: The main function will return immediately after starting the threads
# without waiting for them to complete, which can lead to the program terminating
# before the threads have finished their execution.

# Tip: Use thread names for easier identification in logs.
# By assigning unique names to threads, developers can trace the flow of execution 
# more effectively when analyzing logs, especially in complex multithreaded applications.

# Advanced Tip: To manage the lifetime of threads better, consider using ThreadPoolExecutor from 
# the concurrent.futures module. It provides a high-level interface for asynchronously executing 
# callables using a pool of threads, allowing for better control and management.

# Example usage of the main function
# Uncomment the following line to execute the main function and start the threads.
# main()

# Pitfalls:
# - Be cautious of race conditions when multiple threads access shared resources simultaneously.
# - Always ensure proper synchronization (e.g., using locks or semaphores) when modifying shared data.
# - Debugging multithreaded applications can be tricky due to the non-deterministic nature of thread scheduling.
# Thus, logging with clear messages is crucial for tracking down issues.


#===============================================================================
# 10. Remote Debugging
#===============================================================================

# Remote debugging allows developers to troubleshoot and diagnose issues in code that 
# is running on a different machine or environment. This can be particularly useful 
# for debugging production systems or remote servers.

# Common tools for remote debugging include:
# - pdb over SSH: Using the built-in Python debugger over an SSH connection.
# - remote-pdb package: A library that facilitates remote debugging.
# - IDE remote debugging features: Integrated Development Environments (IDEs) like 
# PyCharm Professional offer built-in support for remote debugging.

# Example using remote-pdb:
# To install the remote-pdb package, run:
# pip install remote-pdb

from remote_pdb import set_trace
# Set a trace that listens on all interfaces (0.0.0.0) and on port 4444.
# This allows remote clients to connect to this debugger.
set_trace(host='0.0.0.0', port=4444)  

# Connect to the debugger using telnet: 
# telnet localhost 4444
# This allows you to step through the code and inspect variables remotely.

# Tips and Tricks

# 1. Use f-strings for easy debugging prints.
# f-strings (formatted string literals) were introduced in Python 3.6 and provide 
# a concise way to include variable values directly in strings.
x = 10
y = 20
# The expression f"{x=}, {y=}" prints the variable names and their values.
# Output: x=10, y=20
print(f"{x=}, {y=}")

# 2. Use breakpoint() with custom debuggers.
# The built-in breakpoint() function allows you to easily set breakpoints in your code.
# You can customize which debugger is used by setting the environment variable 
# PYTHONBREAKPOINT before running your script.
# Example command: PYTHONBREAKPOINT=pudb.set_trace python script.py

# 3. Use @profile decorator selectively.
# The line_profiler library allows you to measure the execution time of individual lines in functions.
# Use the 'profile' decorator from line_profiler only if it's available.
if 'line_profiler' in globals():
    profile = globals()['profile']  # Assign profile if line_profiler is loaded
else:
    profile = lambda x: x  # No-op if not available

# 4. Use context managers for timing operations.
# Context managers provide a way to allocate and release resources cleanly.
# Here, we define a timing context manager to measure the duration of code execution.
from contextlib import contextmanager
import time

@contextmanager
def timing(description: str) -> None:
    start = time.time()  # Record the start time
    yield  # This yields control back to the block of code using the context manager
    ellapsed_time = time.time() - start  # Calculate elapsed time
    # Print out the time taken for the operation
    print(f"{description}: {ellapsed_time:.3f} seconds")

# Using the timing context manager to measure a simulated operation
with timing("Complex operation"):
    # Simulate a complex operation using sleep
    time.sleep(1)  # Sleep for 1 second

# 5. Use functools.lru_cache for memoization and performance improvement.
# The lru_cache decorator caches the results of function calls, which can greatly improve 
# performance for functions with expensive computations that are called with the same arguments.
from functools import lru_cache

@lru_cache(maxsize=None)  # maxsize=None allows unlimited caching
def fibonacci(n):
    # Base case for the Fibonacci sequence
    if n < 2:
        return n
    # Recursive calls for Fibonacci numbers
    return fibonacci(n-1) + fibonacci(n-2)

# 6. Use dis module to inspect bytecode.
# The dis module allows you to analyze the bytecode generated by Python functions, which 
# can be valuable for optimization and understanding how Python executes code.
import dis

def simple_function(x, y):
    return x + y

# Disassemble the simple_function to view its bytecode
dis.dis(simple_function)

# 7. Use sys.getsizeof() to check object memory usage.
# The sys.getsizeof() function returns the size of an object in bytes, which can help 
# you understand memory consumption.
import sys

x = [1, 2, 3, 4, 5]  # A list of integers
# Output the size of the list object in bytes
print(sys.getsizeof(x))  # Outputs the size in bytes

# 8. Use objgraph for object reference visualization.
# objgraph is a powerful tool for visualizing the relationships and references between 
# objects in memory, which is useful for identifying memory leaks.
# To install objgraph, run:
# pip install objgraph

import objgraph

x = [1, 2, 3]  # A list object
y = [x, dict(key1=x)]  # A list and a dictionary containing a reference to 'x'
# Visualize references to 'y' and save the graph as an image
objgraph.show_refs([y], filename='sample-graph.png')

# 9. Use traceback module for better exception handling.
# The traceback module provides a way to format and print stack traces for exceptions, 
# making it easier to debug errors in your code.
import traceback

try:
    # Intentionally cause a division by zero error
    1 / 0
except Exception as e:
    print("An error occurred:")
    # Print the formatted stack trace
    print(traceback.format_exc())

# 10. Use yappi for profiling multi-threaded applications.
# yappi (Yet Another Python Profiler) is specifically designed for profiling multi-threaded 
# applications and can help you analyze performance bottlenecks.
# To install yappi, run:
# pip install yappi

import yappi

yappi.set_clock_type("cpu")  # Use set_clock_type("wall") for wall-clock timing
yappi.start()  # Start profiling

# Place your multi-threaded code here
# e.g., threading.Thread(target=some_function).start()

yappi.stop()  # Stop profiling
# Retrieve statistics for all threads
threads = yappi.get_thread_stats()
# Print profiling results for each thread
for thread in threads:
    print(f"Function stats for ({thread.name}) ({thread.id}):")
    # Print function stats specific to each thread
    yappi.get_func_stats(ctx_id=thread.id).print_all()

# Remember: "Premature optimization is the root of all evil" - Donald Knuth
# Always profile your code first to identify bottlenecks before attempting to optimize.
# Focus on measuring the impact of optimizations to ensure meaningful improvements.
