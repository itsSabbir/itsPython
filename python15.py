# Python Cheat Sheet: Debugging and Profiling

# 1. Debugging with pdb (Python Debugger)

import pdb

def complex_function(x, y):
    result = x + y
    pdb.set_trace()  # Breakpoint
    for i in range(5):
        result *= i + 1
    return result

# To run:
# complex_function(3, 4)

# Basic pdb commands:
# n (next) - Execute the current line
# s (step) - Step into a function call
# c (continue) - Continue execution until the next breakpoint
# p variable_name - Print the value of a variable
# l (list) - Show the current location in the code
# q (quit) - Quit the debugger

# Tip: Use breakpoint() instead of pdb.set_trace() in Python 3.7+

# Post-mortem debugging
def buggy_function():
    x = 5
    y = 0
    return x / y

try:
    buggy_function()
except ZeroDivisionError:
    import pdb
    pdb.post_mortem()

# Conditional breakpoints
x = 10
if x > 5:
    breakpoint()

# Tip: Use PYTHONBREAKPOINT environment variable to control breakpoint() behavior
# export PYTHONBREAKPOINT=0  # Disable breakpoints
# export PYTHONBREAKPOINT=pdb.set_trace  # Use pdb (default)

# Using pdb in command line
# python -m pdb script.py

# 2. Debugging with IDEs

# Most IDEs (PyCharm, VS Code, etc.) provide graphical debuggers
# Common features:
# - Setting breakpoints
# - Step over, step into, step out
# - Variable inspection
# - Watch expressions
# - Call stack examination

# Tip: Learn keyboard shortcuts for efficient debugging in your IDE

# 3. Logging for Debugging

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def divide(x, y):
    logging.debug(f'Dividing {x} by {y}')
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error('Division by zero!')
        raise
    logging.info(f'Result: {result}')
    return result

# Tip: Use different logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# for appropriate granularity

# 4. Assertions for Debugging

def calculate_average(numbers):
    assert len(numbers) > 0, "List is empty"
    return sum(numbers) / len(numbers)

# Tip: Use -O flag to disable assertions in production code
# python -O script.py

# 5. Profiling Code for Performance

# Using cProfile

import cProfile

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

cProfile.run('fibonacci(30)')

# Tip: Sort the output by cumulative time
# cProfile.run('fibonacci(30)', sort='cumtime')

# Using line_profiler for line-by-line profiling
# pip install line_profiler

@profile
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Run with: kernprof -l -v script.py

# Using memory_profiler to profile memory usage
# pip install memory_profiler

from memory_profiler import profile

@profile
def memory_hungry_function():
    return [i for i in range(1000000)]

# Run with: python -m memory_profiler script.py

# Tip: Use mprof for plotting memory usage over time
# mprof run script.py
# mprof plot

# 6. Timing Code Execution

import time

start_time = time.time()
# Your code here
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")

# Using timeit for more accurate timing
import timeit

def function_to_time():
    return sum(range(1000000))

execution_time = timeit.timeit(function_to_time, number=10)
print(f"Average execution time: {execution_time / 10} seconds")

# Tip: Use timeit in IPython/Jupyter for quick timing
# %timeit function_to_time()

# 7. Profiling with cProfile and visualization

import cProfile
import pstats
from pstats import SortKey

# Profile the code
cProfile.run('fibonacci(30)', 'output.prof')

# Analyze the results
with open('output_stats.txt', 'w') as f:
    p = pstats.Stats('output.prof', stream=f)
    p.sort_stats(SortKey.CUMULATIVE).print_stats(10)

# Tip: Use snakeviz for visualization
# pip install snakeviz
# snakeviz output.prof

# 8. Using tracemalloc for memory tracking

import tracemalloc

tracemalloc.start()

# Your code here

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

# 9. Debugging Multithreaded Applications

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s')

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def main():
    threading.Thread(target=worker, name='Worker-1').start()
    threading.Thread(target=worker, name='Worker-2').start()

# Tip: Use thread names for easier identification in logs

# 10. Remote Debugging

# For remote debugging, you can use tools like:
# - pdb over SSH
# - remote-pdb package
# - IDE remote debugging features (e.g., PyCharm Professional)

# Example using remote-pdb:
# pip install remote-pdb

from remote_pdb import set_trace
set_trace(host='0.0.0.0', port=4444)  # Listen on all interfaces

# Connect using: telnet localhost 4444

# Tips and Tricks

# 1. Use f-strings for easy debugging prints
x = 10
y = 20
print(f"{x=}, {y=}")  # Python 3.8+

# 2. Use breakpoint() with custom debuggers
# PYTHONBREAKPOINT=pudb.set_trace python script.py

# 3. Use @profile decorator selectively
if 'line_profiler' in globals():
    profile = globals()['profile']
else:
    profile = lambda x: x

# 4. Use context managers for timing
from contextlib import contextmanager
import time

@contextmanager
def timing(description: str) -> None:
    start = time.time()
    yield
    ellapsed_time = time.time() - start
    print(f"{description}: {ellapsed_time:.3f} seconds")

with timing("Complex operation"):
    # Your code here
    time.sleep(1)

# 5. Use functools.lru_cache for memoization and performance improvement
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 6. Use dis module to inspect bytecode
import dis

def simple_function(x, y):
    return x + y

dis.dis(simple_function)

# 7. Use sys.getsizeof() to check object memory usage
import sys

x = [1, 2, 3, 4, 5]
print(sys.getsizeof(x))  # Size in bytes

# 8. Use objgraph for object reference visualization
# pip install objgraph

import objgraph

x = [1, 2, 3]
y = [x, dict(key1=x)]
objgraph.show_refs([y], filename='sample-graph.png')

# 9. Use traceback module for better exception handling
import traceback

try:
    1 / 0
except Exception as e:
    print("An error occurred:")
    print(traceback.format_exc())

# 10. Use yappi for profiling multi-threaded applications
# pip install yappi

import yappi

yappi.set_clock_type("cpu")  # Use set_clock_type("wall") for wall time
yappi.start()

# Your multi-threaded code here

yappi.stop()
threads = yappi.get_thread_stats()
for thread in threads:
    print(f"Function stats for ({thread.name}) ({thread.id}):")
    yappi.get_func_stats(ctx_id=thread.id).print_all()

# Remember: "Premature optimization is the root of all evil" - Donald Knuth
# Profile first, optimize later, and always measure the impact of your optimizations.