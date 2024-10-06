#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Concurrency and Parallelism
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This section covers various methods for achieving concurrency and parallelism in Python.
# Understanding these concepts is critical for writing efficient programs that can handle multiple tasks simultaneously.

# Importing necessary modules for concurrency and parallelism.
import threading  # Provides tools for threading in Python.
import multiprocessing  # Enables parallel execution across multiple CPU cores.
import asyncio  # Supports asynchronous programming using the async/await syntax.
import time  # Provides time-related functions for managing time in code.
import concurrent.futures  # Facilitates launching parallel tasks with threads or processes.
import queue  # Implements a queue data structure for safe multi-threading communication.
from typing import List, Callable, Any  # Type hinting for better code clarity and error checking.

# Example 1: Using threading for concurrent tasks
# Threading is suitable for I/O-bound tasks where the program spends time waiting for external resources.
def thread_example():
    def print_numbers():
        for i in range(5):
            print(f"Thread: {i}")
            time.sleep(1)  # Simulates I/O-bound operation by sleeping for 1 second

    thread = threading.Thread(target=print_numbers)  # Create a thread
    thread.start()  # Start the thread
    thread.join()  # Wait for the thread to finish

# Example 2: Using multiprocessing for parallel tasks
# Multiprocessing is ideal for CPU-bound tasks as it runs separate processes, bypassing the Global Interpreter Lock (GIL).
def multiprocessing_example():
    def square(n):
        return n * n

    with multiprocessing.Pool(processes=4) as pool:  # Create a pool of 4 processes
        results = pool.map(square, range(10))  # Map function across a range
        print("Squares:", results)  # Output: Squares of numbers 0 to 9

# Example 3: Using asyncio for asynchronous programming
# Asyncio is used for writing single-threaded concurrent code using coroutines.
async def asyncio_example():
    async def print_async_numbers():
        for i in range(5):
            print(f"Async: {i}")
            await asyncio.sleep(1)  # Non-blocking sleep

    await print_async_numbers()  # Run the async function

# Example 4: Using concurrent.futures for easier thread/process management
# The concurrent.futures module simplifies the execution of concurrent tasks.
def futures_example():
    def fetch_data(n):
        time.sleep(1)  # Simulates a network call
        return f"Data {n}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:  # Thread pool for concurrent execution
        futures = [executor.submit(fetch_data, i) for i in range(5)]  # Submit tasks to the pool
        for future in concurrent.futures.as_completed(futures):
            print(future.result())  # Print results as they complete

# Example 5: Using queues for thread-safe communication
# The queue module provides a thread-safe FIFO implementation for managing shared data.
def queue_example():
    def worker(q):
        while not q.empty():
            item = q.get()  # Get an item from the queue
            print(f"Processing: {item}")
            q.task_done()  # Indicate that the item has been processed

    q = queue.Queue()  # Create a queue
    for i in range(5):
        q.put(i)  # Add items to the queue

    # Start worker threads
    threads = [threading.Thread(target=worker, args=(q,)) for _ in range(2)]
    for thread in threads:
        thread.start()

    q.join()  # Wait for all items to be processed

# In summary, understanding the different concurrency and parallelism methods in Python is essential.
# Use threading for I/O-bound tasks, multiprocessing for CPU-bound tasks, and asyncio for managing asynchronous workflows.
# The concurrent.futures module and queues enhance task management and thread safety.
# It is crucial to be aware of the GIL in Python and choose the right method based on the nature of the task.
# As a best practice, always handle exceptions in concurrent code to prevent silent failures.


#===============================================================================
# 1. Threading
#===============================================================================

# The threading module in Python allows concurrent execution of code,
# making it possible to run multiple threads (smaller units of a process) in parallel.
# This is especially useful for I/O-bound tasks, where waiting for external resources
# (like network calls or file I/O) is common.

# Example 1: Simple worker thread
import threading  # Importing the threading module
import time  # Importing the time module for sleep functionality

def worker(name: str) -> None:
    print(f"Worker {name} starting")  # Indicate the start of a worker thread
    time.sleep(2)  # Simulate a time-consuming operation
    print(f"Worker {name} finished")  # Indicate the end of the worker thread

# Creating and starting threads
threads = []  # List to hold thread objects
for i in range(5):  # Loop to create 5 worker threads
    t = threading.Thread(target=worker, args=(i,))  # Create a thread targeting the worker function
    threads.append(t)  # Append the thread to the list
    t.start()  # Start the thread

# Waiting for all threads to complete
for t in threads:  # Loop through each thread
    t.join()  # Wait for the thread to finish execution

print("All threads completed")  # Indicate all threads have finished

# Tip: Use threading for I/O-bound tasks, not CPU-bound tasks due to the Global Interpreter Lock (GIL)
# The GIL allows only one thread to execute Python bytecode at a time,
# which means threading isn't ideal for CPU-bound tasks. Consider using multiprocessing for CPU-intensive operations.

# Example 2: Thread-safe counter using Lock
# A shared counter that multiple threads will increment safely
counter = 0  # Shared counter variable
lock = threading.Lock()  # Create a Lock object for synchronization

def increment():
    global counter  # Declare counter as global to modify it
    with lock:  # Acquire the lock to ensure thread safety
        current = counter  # Get the current value of counter
        time.sleep(0.1)  # Simulate some work (this can lead to race conditions without a lock)
        counter = current + 1  # Increment the counter

# Creating threads to increment the counter
threads = [threading.Thread(target=increment) for _ in range(10)]  # List of 10 threads
for t in threads:
    t.start()  # Start each thread
for t in threads:
    t.join()  # Wait for each thread to finish

print(f"Final counter value: {counter}")  # Display the final value of the counter

# Tip: Always use locks or other synchronization primitives to protect shared resources
# This prevents race conditions where multiple threads access and modify shared data simultaneously,
# leading to inconsistent results.

# Example 3: Using a ThreadPoolExecutor
# A higher-level interface for managing threads, simplifying thread management.
import concurrent.futures  # Importing the concurrent.futures module for ThreadPoolExecutor

def task(n: int) -> str:
    time.sleep(n)  # Simulate a variable delay
    return f"Task {n} completed"  # Return a string upon completion

# Using ThreadPoolExecutor for managing multiple threads
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:  # Limit to 3 concurrent threads
    futures = [executor.submit(task, i) for i in range(5)]  # Submit tasks to the executor
    for future in concurrent.futures.as_completed(futures):  # Iterate over completed futures
        print(future.result())  # Print the result of each completed task

# Tip: ThreadPoolExecutor is a higher-level interface for managing threads
# It handles thread creation and management automatically, providing an easy way to work with multiple threads,
# improving code readability and maintainability.

# In summary, threading can be a powerful tool for concurrent programming in Python,
# especially for I/O-bound tasks. Understanding locks, thread management, and best practices
# will lead to safer and more efficient threaded applications.

#===============================================================================
# 2. Multiprocessing
#===============================================================================

# Multiprocessing is a powerful module in Python that allows for the concurrent execution 
# of tasks across multiple CPU cores. This is particularly useful for CPU-bound tasks 
# where threading may not provide significant benefits due to the Global Interpreter Lock (GIL).

# Example 1: Using Pool for parallel processing
# A process pool allows us to manage a pool of worker processes.
# This example defines a simple worker function that squares a number.
def process_worker(num: int) -> int:
    return num * num  # The function returns the square of the input number

if __name__ == '__main__':
    import multiprocessing  # Ensure to import the multiprocessing module

    # Using Pool for parallel processing
    # Here, we create a pool of worker processes (4 in this case).
    with multiprocessing.Pool(processes=4) as pool:
        # The map function applies the process_worker function to each item in the iterable (range(10)).
        results = pool.map(process_worker, range(10))
        # This will return a list of results corresponding to the squared values of 0 to 9.
        print("Pool results:", results)  # Output: Pool results: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Use case:
# Pool is effective for tasks that are independent of each other and can be computed in parallel.
# Ideal for batch processing of data or running simulations where each task does not affect others.

# Example 2: Using Process class
# The Process class allows for more fine-grained control over the subprocesses.
# This example defines a function that prints information about the process.
    def info(title: str) -> None:
        print(title)  # Print the title for the process
        print('module name:', __name__)  # Display the module name
        print('parent process:', multiprocessing.parent_process())  # Show the parent process
        print('process id:', multiprocessing.current_process().pid)  # Show the current process ID

    processes = []  # List to keep track of process instances
    for i in range(5):  # Create 5 processes
        # Each process will run the 'info' function with a unique title
        p = multiprocessing.Process(target=info, args=(f'Process {i}',))
        processes.append(p)  # Append the process to the list
        p.start()  # Start the process

    for p in processes:  # Ensure all processes complete before continuing
        p.join()  # Wait for the process to finish

# Use case:
# The Process class is useful when you need to create and manage individual processes,
# allowing you to run different functions in parallel with more control over their execution.

# Example 3: Sharing data between processes
# When using multiple processes, you may need to share data between them.
# Here, we define a function that modifies a multiprocessing Value and Array.
    def f(n: multiprocessing.Value, a: multiprocessing.Array) -> None:
        n.value = 3.14159265359  # Set the value of the shared variable to Pi
        for i in range(len(a)):
            a[i] = -a[i]  # Negate the values in the shared array

    # Create a shared Value and Array to be used across processes
    num = multiprocessing.Value('d', 0.0)  # 'd' denotes a double precision float
    arr = multiprocessing.Array('i', range(10))  # 'i' denotes an array of integers initialized to 0-9

    # Create and start the process that will modify the shared data
    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()  # Start the process
    p.join()  # Wait for the process to finish

    # Print the updated values of the shared variables
    print(num.value)  # Output: 3.14159265359 (the value set in function f)
    print(arr[:])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] --> it will print the negated array: [-0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# Advanced tip:
# Use multiprocessing for CPU-bound tasks, such as mathematical computations or data processing,
# where the GIL would limit the performance of threads. 
# Be aware that inter-process communication can introduce overhead, so evaluate the trade-offs 
# when deciding between multiprocessing and multithreading.

# Potential pitfalls:
# 1. Overhead: Multiprocessing can have more overhead than multithreading due to process creation and inter-process communication.
# 2. Complexity: Managing state and data between processes can be complex. Use synchronization primitives (like Locks) when needed.
# 3. Debugging: Debugging multiprocessing code can be more challenging due to concurrent execution; consider using logging to track process behavior.

#===============================================================================
# 3. Async Programming
#===============================================================================

# Asynchronous programming allows for concurrent execution, enabling efficient management
# of I/O-bound tasks, such as file operations or network requests. Python's asyncio library
# provides tools to write concurrent code using the async/await syntax.

# Example 1: Simple asynchronous function
# The function 'say_after' takes a delay and a string, then waits for the specified
# time before printing the string. This demonstrates how asynchronous functions can 
# yield control back to the event loop during waiting periods.
import asyncio
import time  # Importing time to format timestamps

async def say_after(delay: float, what: str) -> None:
    await asyncio.sleep(delay)  # Asynchronously wait for the specified delay
    print(what)  # Print the message after the delay

# Example 2: Running the main async function
# The 'main' function orchestrates the calling of 'say_after' with specified delays.
async def main():
    print(f"started at {time.strftime('%X')}")  # Print the start time

    await say_after(1, 'hello')  # Waits 1 second, then prints 'hello'
    await say_after(2, 'world')  # Waits 2 seconds, then prints 'world'

    print(f"finished at {time.strftime('%X')}")  # Print the finish time

# Running the event loop to execute the main function
asyncio.run(main())

# Output:
# started at XX:XX:XX
# hello
# world
# finished at XX:XX:XX

# Example 3: Concurrent execution of tasks
# This example shows how to run multiple asynchronous tasks concurrently.
# 'asyncio.create_task' is used to schedule the execution of 'say_after' without 
# waiting for one to finish before starting the other.
async def main_concurrent():
    task1 = asyncio.create_task(say_after(1, 'hello'))  # Create a task for 'say_after'
    task2 = asyncio.create_task(say_after(2, 'world'))  # Create another task

    print(f"started at {time.strftime('%X')}")  # Print the start time
    await task1  # Await the completion of the first task
    await task2  # Await the completion of the second task
    print(f"finished at {time.strftime('%X')}")  # Print the finish time

# Running the event loop for concurrent execution
asyncio.run(main_concurrent())

# Output:
# started at XX:XX:XX
# hello
# world
# finished at XX:XX:XX

# Tip: Use asyncio for I/O-bound concurrent programming
# This approach is effective when tasks involve waiting for external resources,
# allowing the program to perform other operations during the wait.

# Example 4: Asynchronous context managers
# Context managers can manage resources efficiently. This class demonstrates an async
# context manager that prints messages upon entering and exiting a context.
class AsyncContextManager:
    async def __aenter__(self):
        print("Entering the context")  # Action when entering the context
        await asyncio.sleep(1)  # Simulate async resource acquisition
        return "Context Value"  # Value to be returned upon entering the context

    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting the context")  # Action when exiting the context
        await asyncio.sleep(1)  # Simulate async resource cleanup

# Using the asynchronous context manager
async def use_context_manager():
    async with AsyncContextManager() as value:  # Entering the context
        print(f"Inside the context with value: {value}")  # Using the value in the context

# Running the event loop to execute context manager usage
asyncio.run(use_context_manager())

# Output:
# Entering the context
# Inside the context with value: Context Value
# Exiting the context

# Tip: Use async context managers for asynchronous resource management
# They provide a clean way to manage resources, ensuring they are properly acquired 
# and released, even in asynchronous code.

# Example 5: Asynchronous iteration
# The AsyncIterator class demonstrates how to implement asynchronous iteration.
# It uses the 'await' keyword to pause execution while providing the next item.
class AsyncIterator:
    def __init__(self, stop: int):
        self.current = 0  # Starting point for iteration
        self.stop = stop   # Ending point for iteration

    def __aiter__(self):
        return self  # Return the iterator object itself

    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1)  # Simulate async operation
            self.current += 1  # Increment current value
            return self.current - 1  # Return the current value before increment
        else:
            raise StopAsyncIteration  # Signal that the iteration is complete

# Using the asynchronous iterator
async def use_async_iterator():
    async for num in AsyncIterator(5):  # Asynchronously iterate over the AsyncIterator
        print(num, end=' ')  # Print the numbers without new lines
    print()  # New line after iteration completion

# Running the event loop to execute async iteration
asyncio.run(use_async_iterator())

# Output:
# 0 1 2 3 4

# Tip: Use async iterators for asynchronous sequences
# This allows for efficient processing of sequences where each element requires 
# an asynchronous operation, ideal for handling streams of data or API responses.

#===============================================================================
# 4. Combining Threading and Multiprocessing
#===============================================================================

# In this section, we explore how to efficiently combine threading and multiprocessing 
# in Python to handle both CPU-bound and I/O-bound tasks. Understanding when to use 
# each method can significantly enhance application performance.

import multiprocessing  # Required for creating a pool of processes
import time  # Required for measuring time taken by operations
from typing import List  # Importing List for type hints

# This function is CPU-bound, meaning it performs computations that require significant CPU time.
# The function calculates the sum of squares of all integers up to 'number'.
def cpu_bound(number: int) -> int:
    return sum(i * i for i in range(number))  # Efficiently computes the sum of squares

# This function leverages multiprocessing to distribute the workload across multiple CPU cores.
# It takes a list of integers and returns a list of their corresponding sums of squares.
def find_sums(numbers: List[int]) -> List[int]:
    with multiprocessing.Pool() as pool:  # Create a pool of worker processes
        return pool.map(cpu_bound, numbers)  # Distributes 'numbers' across the worker pool

# The main function orchestrates the execution of the program.
# It sets up the data, measures execution time, and calls the find_sums function.
def main():
    numbers = [10000000 + x for x in range(20)]  # Generates a list of 20 integers starting from 10 million
    
    start_time = time.time()  # Record the start time for performance measurement
    sums = find_sums(numbers)  # Calls the function to calculate sums using multiprocessing
    end_time = time.time()  # Record the end time

    # Output the total of the computed sums and the time taken for computation
    print(f"Sum of sums: {sum(sums)}")  # Sum the results and print
    print(f"Time taken: {end_time - start_time:.2f} seconds")  # Print the time taken in seconds

# This conditional ensures that the main function runs only when the script is executed directly.
if __name__ == '__main__':
    main()  # Invoke the main function to start the program

# Tip: Use multiprocessing for CPU-bound tasks like computations that require heavy processing,
# while threading is more suited for I/O-bound tasks, such as network operations or file I/O.
# Understanding this distinction can lead to more effective resource utilization and improved performance.

#===============================================================================
# 5. Advanced Multiprocessing Techniques
#===============================================================================

# In this section, we explore advanced techniques for inter-process communication (IPC)
# in Python using the multiprocessing module. IPC allows processes to communicate
# and synchronize their actions, which is crucial for multi-core processor utilization.

# Inter-process communication using Queue
# A Queue is a thread-safe FIFO (first-in, first-out) data structure suitable for 
# communication between multiple processes.

# Producer function: This function generates data and puts it into the queue.
# It simulates a production process by sending numbers 0-9 to the queue.
def producer(queue: multiprocessing.Queue) -> None:
    for i in range(10):
        queue.put(i)  # Put the current number into the queue
        time.sleep(0.1)  # Simulate some processing time
    queue.put(None)  # Sentinel value to signal the end of data production

# Consumer function: This function retrieves data from the queue and processes it.
# It continuously pulls items from the queue until it encounters the sentinel value.
def consumer(queue: multiprocessing.Queue) -> None:
    while True:
        item = queue.get()  # Retrieve the next item from the queue
        if item is None:  # Check for the sentinel value
            break  # Exit the loop if the sentinel is received
        print(f"Consumed: {item}")  # Print the consumed item

# Main execution block
if __name__ == '__main__':
    q = multiprocessing.Queue()  # Create a new Queue for inter-process communication
    # Create the producer process
    prod_proc = multiprocessing.Process(target=producer, args=(q,))
    # Create the consumer process
    cons_proc = multiprocessing.Process(target=consumer, args=(q,))
    
    prod_proc.start()  # Start the producer process
    cons_proc.start()  # Start the consumer process
    
    prod_proc.join()  # Wait for the producer process to finish
    cons_proc.join()  # Wait for the consumer process to finish

# Tip: Use Queue for thread-safe communication between processes.
# Queues manage locks internally, ensuring that data is not corrupted when multiple
# processes access it simultaneously. They can also handle complex data types since
# they utilize serialization.

# Using Pipes for bi-directional communication
# A Pipe provides a simpler way to establish a two-way communication channel
# between two processes, allowing data to be sent and received simultaneously.

# Ping function: This function sends a "Ping" message through the connection.
def ping(conn):
    conn.send('Ping')  # Send 'Ping' to the other end of the pipe
    print(f"Ping received: {conn.recv()}")  # Wait and receive a response

# Pong function: This function waits for a "Ping" message, then responds with "Pong".
def pong(conn):
    print(f"Pong received: {conn.recv()}")  # Wait for a message
    conn.send('Pong')  # Send 'Pong' back

# Main execution block
if __name__ == '__main__':
    # Create a Pipe with two ends: parent_conn and child_conn
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Create the ping process
    p1 = multiprocessing.Process(target=ping, args=(parent_conn,))
    # Create the pong process
    p2 = multiprocessing.Process(target=pong, args=(child_conn,))
    
    p1.start()  # Start the ping process
    p2.start()  # Start the pong process
    
    p1.join()  # Wait for the ping process to finish
    p2.join()  # Wait for the pong process to finish

# Tip: Use Pipes for efficient bi-directional communication between two processes.
# Pipes have lower overhead compared to Queues but are limited to two endpoints.
# They are ideal for tasks where processes need to exchange data back and forth quickly.

# Advanced tip: Always handle exceptions in your processes to prevent silent failures.
# You can implement logging within the producer or consumer functions to debug
# any issues that may arise during communication. Also, consider using timeouts
# on queue operations to avoid hanging indefinitely in scenarios where data may not be produced.

# Potential pitfalls: Be cautious with resource management and avoid deadlocks.
# For example, ensure that all processes correctly signal completion (like the None value in the Queue).
# Otherwise, the consumer could wait indefinitely for more data, leading to a deadlock situation.

#===============================================================================
# 6. Advanced Asyncio Techniques
#===============================================================================

# This section covers advanced techniques in asynchronous programming using the asyncio library in Python.
# Asynchronous programming is essential for writing non-blocking code, especially in I/O-bound applications.

# Asynchronous generators
# Asynchronous generators allow the production of values asynchronously, providing a way to yield values 
# over time while still maintaining the ability to await other coroutines.
# This is particularly useful in scenarios like streaming data or fetching results from an API.

async def async_range(start: int, stop: int, step: int = 1):
    # This asynchronous generator yields a sequence of numbers from start to stop, incrementing by step.
    for i in range(start, stop, step):
        await asyncio.sleep(0.1)  # Simulates an asynchronous delay (e.g., I/O operation)
        yield i  # Yield the current value, allowing the caller to receive it asynchronously

# Example usage of the async generator
async def use_async_generator():
    # The 'async for' loop allows us to iterate over the values yielded by the async generator.
    async for i in async_range(0, 5):
        print(i, end=' ')  # Print each value in the sequence without a newline
    print()  # Print a newline after the loop completes

# Running the async generator
import asyncio  # Importing asyncio to enable asynchronous functionality
asyncio.run(use_async_generator())  # Entry point to run the asynchronous function

# Output: 0 1 2 3 4 
# The output is produced with a slight delay between each number due to the asyncio.sleep(0.1)

# Tip: Use asynchronous generators for producing asynchronous sequences of values
# They can significantly improve performance in scenarios where data is produced or retrieved over time.

# Handling cancellation
# Cancellation in asynchronous operations is crucial for managing long-running tasks,
# allowing for the graceful termination of coroutines without leaving resources hanging.

async def cancelable_operation():
    # A long-running asynchronous operation that can be cancelled.
    try:
        while True:  # Infinite loop, simulating ongoing work
            print("Operation in progress...")  # Notify that the operation is ongoing
            await asyncio.sleep(1)  # Simulates a delay, representing an ongoing task
    except asyncio.CancelledError:
        # This block executes if the operation is cancelled
        print("Operation was cancelled")  # Notify that the operation was cancelled
        raise  # Re-raise the exception to propagate the cancellation

# Example of handling cancellation in the main function
async def main_cancellation():
    # Creating a task that runs the cancelable_operation coroutine
    task = asyncio.create_task(cancelable_operation())
    await asyncio.sleep(3)  # Allow the task to run for 3 seconds
    task.cancel()  # Cancel the task
    try:
        await task  # Await the task to ensure we handle its cancellation
    except asyncio.CancelledError:
        print("Main: operation was cancelled")  # Confirm cancellation in the main context

# Running the cancellation example
asyncio.run(main_cancellation())  # Entry point to run the asynchronous cancellation handling

# Output:
# Operation in progress...
# Operation in progress...
# Operation in progress...
# Operation was cancelled
# Main: operation was cancelled
# The output shows the operation in progress followed by cancellation messages.

# Tip: Always handle cancellation in your coroutines for graceful shutdown
# This practice ensures that resources are properly released and any necessary cleanup can be performed.

# Advanced tip: Consider using cancellation tokens for more complex cancellation logic,
# allowing coroutines to be cancelled based on conditions or events beyond just the task cancellation.
# Additionally, ensure that long-running tasks are regularly checking for cancellation requests 
# to avoid holding onto resources unnecessarily.

#===============================================================================
# 7. Concurrent.Futures for Easy Parallelism
#===============================================================================

# The 'concurrent.futures' module in Python provides a high-level interface for asynchronously executing 
# callables using threads or processes. This section focuses on using ProcessPoolExecutor for CPU-bound tasks.

import concurrent.futures  # Importing the concurrent.futures module for parallel execution

# Function to simulate a CPU-bound task.
# This function calculates the sum of squares for integers in the range of 'n'.
def cpu_bound_task(n: int) -> int:
    # Using a generator expression to calculate the sum of squares up to 'n-1'.
    return sum(i * i for i in range(n))  # This is CPU-bound due to heavy computation

# Using ProcessPoolExecutor for parallel execution of CPU-bound tasks.
# The ProcessPoolExecutor spawns multiple processes, making it suitable for tasks that require significant CPU resources.
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Generating a list of numbers to process; each number is incremented by its index.
    # This creates a workload of CPU-bound tasks to be executed in parallel.
    numbers = [10000000 + x for x in range(20)]  # A list of 20 numbers starting from 10,000,000
    # The map method applies the 'cpu_bound_task' function to each item in the 'numbers' list concurrently.
    results = list(executor.map(cpu_bound_task, numbers))  # Collects the results as a list
    # Summing the results obtained from each parallel computation.
    print(f"Sum of results: {sum(results)}")  # Outputs the total sum of the results

# Output: The total sum of the computed squares for the range specified by each number in 'numbers'.
# Tip: Use ProcessPoolExecutor for easy parallelism of CPU-bound tasks.
# This allows for better CPU utilization, especially on multi-core systems, 
# leading to significant performance improvements over sequential execution.

# Advanced tip: 
# When using ProcessPoolExecutor, be aware of the overhead associated with inter-process communication.
# Each process has its own memory space, so passing large data structures can be costly. 
# Instead, consider passing simpler data types or using shared memory techniques if necessary.
# Additionally, for I/O-bound tasks, ThreadPoolExecutor is often a better choice due to its lighter overhead.

# Use case:
# The ProcessPoolExecutor is particularly useful in scenarios like data processing, 
# image manipulation, or any computationally intensive tasks where multiple CPU cores can be leveraged.
# It simplifies the parallelization process without the complexity of managing subprocesses manually.

#===============================================================================
# 8. Best Practices and Tips for Concurrency
#===============================================================================

# In this section, we outline best practices and tips for handling concurrency in Python.
# These principles are essential for writing efficient, robust, and maintainable concurrent code.

# 1. Use threading for I/O-bound tasks and multiprocessing for CPU-bound tasks.
# Threading is effective for tasks that spend time waiting for external resources (I/O).
# Multiprocessing is better suited for CPU-intensive tasks since it utilizes multiple CPU cores.
print("Use threading for I/O-bound tasks and multiprocessing for CPU-bound tasks.")

# Example: Reading a file (I/O-bound)
import threading

def read_file():
    with open("example.txt", "r") as file:
        data = file.read()
        print(data)

thread = threading.Thread(target=read_file)
thread.start()

# Example: Performing a heavy computation (CPU-bound)
from multiprocessing import Process

def heavy_computation():
    total = sum(i * i for i in range(10**6))  # Example CPU-intensive calculation
    print(total)

process = Process(target=heavy_computation)
process.start()

# 2. Always use proper synchronization (locks, queues, etc.) when sharing resources between threads or processes.
# Synchronization mechanisms ensure data integrity when multiple threads/processes access shared resources.
print("Always use proper synchronization (locks, queues, etc.) when sharing resources.")

# Example: Using a lock to prevent race conditions
lock = threading.Lock()

shared_resource = 0

def update_resource():
    global shared_resource
    with lock:  # Ensures exclusive access to the shared resource
        for _ in range(1000):
            shared_resource += 1

# 3. Be aware of the Global Interpreter Lock (GIL) in CPython, which limits true parallelism in threading.
# The GIL allows only one thread to execute Python bytecode at a time, limiting the performance gains from threading in CPU-bound tasks.
print("Be aware of the Global Interpreter Lock (GIL) in CPython, which limits true parallelism in threading.")

# 4. Use asyncio for I/O-bound concurrent programming, especially for network operations.
# asyncio is ideal for I/O-bound tasks due to its non-blocking nature.
print("Use asyncio for I/O-bound concurrent programming, especially for network operations.")

# Example: Asyncio for making HTTP requests
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# 5. Prefer higher-level abstractions like ThreadPoolExecutor and ProcessPoolExecutor when possible.
# These abstractions simplify the management of threads and processes, reducing boilerplate code.
print("Prefer higher-level abstractions like ThreadPoolExecutor and ProcessPoolExecutor when possible.")

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Example: Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(read_file) for _ in range(5)]  # Submitting multiple tasks

# Example: Using ProcessPoolExecutor
with ProcessPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(heavy_computation) for _ in range(5)]  # Submitting CPU-bound tasks

# 6. Be cautious with shared state in multithreading; consider using thread-local storage when appropriate.
# Thread-local storage allows threads to maintain their own copies of data, preventing conflicts.
print("Be cautious with shared state in multithreading; consider using thread-local storage when appropriate.")

import threading

thread_local_data = threading.local()

def process_data():
    thread_local_data.value = 42  # Each thread has its own 'value' attribute
    print(thread_local_data.value)

# 7. Handle cancellation and exceptions properly in asyncio coroutines.
# Ensure that coroutines can be cancelled and exceptions are handled gracefully.
print("Handle cancellation and exceptions properly in asyncio coroutines.")

async def risky_operation():
    try:
        await asyncio.sleep(2)
        raise ValueError("An error occurred!")
    except ValueError as e:
        print(f"Caught an exception: {e}")

# 8. Use multiprocessing.Queue or Pipe for inter-process communication.
# These mechanisms provide a way to share data between processes safely.
print("Use multiprocessing.Queue or Pipe for inter-process communication.")

from multiprocessing import Queue

queue = Queue()

def producer():
    for i in range(5):
        queue.put(i)  # Sending data to the queue

def consumer():
    while not queue.empty():
        item = queue.get()  # Receiving data from the queue
        print(f"Consumed: {item}")

# 9. Be aware of the overhead of creating processes; reuse them when possible using process pools.
# Creating processes can be expensive; using pools can minimize this overhead.
print("Be aware of the overhead of creating processes; reuse them when possible using process pools.")

# 10. Profile your concurrent code to ensure it's actually providing performance benefits.
# Use profiling tools to measure performance and identify bottlenecks in concurrent applications.
print("Profile your concurrent code to ensure it's actually providing performance benefits.")

# 11. Use async context managers and async iterators for more idiomatic asyncio code.
# These constructs enhance readability and ensure resources are managed properly.
print("Use async context managers and async iterators for more idiomatic asyncio code.")

# Example: Async context manager
async def async_resource_manager():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://example.com") as response:
            return await response.text()

# 12. Consider using asyncio.gather() for running multiple coroutines concurrently.
# asyncio.gather allows you to run several coroutines at once, simplifying concurrent programming.
print("Consider using asyncio.gather() for running multiple coroutines concurrently.")

async def main():
    await asyncio.gather(fetch_data("http://example.com"), fetch_data("http://example.org"))

# 13. Be mindful of potential deadlocks when using multiple locks.
# Deadlocks can occur if two or more threads wait indefinitely for resources held by each other.
print("Be mindful of potential deadlocks when using multiple locks.")

# 14. Use concurrent.futures for simple parallelism tasks.
# This library simplifies parallel task execution without low-level threading or multiprocessing management.
print("Use concurrent.futures for simple parallelism tasks.")

# Example: Simple usage of concurrent.futures
from concurrent.futures import ThreadPoolExecutor

def compute_square(n):
    return n * n

with ThreadPoolExecutor() as executor:
    results = list(executor.map(compute_square, range(10)))  # Compute squares in parallel
    print(results)

# 15. Always join threads and processes to prevent zombie processes and ensure proper cleanup.
# Joining ensures that the main program waits for threads/processes to complete before exiting.
print("Always join threads and processes to prevent zombie processes and ensure proper cleanup.")

# Example: Joining threads
thread.join()  # Wait for the thread to complete
process.join()  # Wait for the process to complete

# In summary, these best practices for concurrency in Python help ensure efficient, maintainable, 
# and robust code, leveraging the strengths of threading, multiprocessing, and asynchronous programming effectively.

# This concludes the enhanced detailed Python Cheat Sheet for Concurrency and Parallelism