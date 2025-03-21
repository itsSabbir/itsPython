# Concurrency and Parallelism - Multiprocessing - in the Python Programming Language
# ==================================================================================

# Table of Contents:
# 1. Overview and Historical Context
# 2. Syntax, Key Concepts, and Code Examples
# 3. Best Practices, Common Pitfalls, and Advanced Tips
# 4. Integration and Real-World Applications
# 5. Advanced Concepts and Emerging Trends
# 6. FAQs and Troubleshooting
# 7. Recommended Tools, Libraries, and Resources
# 8. Performance Analysis and Optimization
# 9. How to Contribute

# Author: Sabbir Hossain

import multiprocessing as mp
import time
import os
import random
import numpy as np
from typing import List, Callable, Any
import concurrent.futures
import logging
import queue

# 1. Overview and Historical Context
# ----------------------------------
# Multiprocessing in Python allows the execution of multiple processes concurrently,
# leveraging multiple CPU cores and bypassing the Global Interpreter Lock (GIL).

# Historical context:
# - The multiprocessing module was introduced in Python 2.6 (2008).
# - It was designed to address the limitations of the threading module due to the GIL.
# - Python 3.2 (2011) introduced significant improvements to the multiprocessing module.
# - Python 3.4 (2014) added the concurrent.futures module, providing a higher-level interface.

# Significance:
# - Enables true parallelism on multi-core systems.
# - Overcomes the GIL limitation for CPU-bound tasks.
# - Provides isolation between processes, enhancing stability.

# Common use cases:
# - CPU-intensive computations
# - Parallel data processing
# - Distributed computing
# - Long-running background tasks

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Basic Process Creation
def basic_process_example():
    def worker(name):
        print(f"Worker {name} (PID: {os.getpid()}) starting")
        time.sleep(2)
        print(f"Worker {name} (PID: {os.getpid()}) finished")

    processes = []
    for i in range(5):
        p = mp.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All workers finished")

# Using Process Pool
def process_pool_example():
    def worker(x):
        return x * x

    with mp.Pool(processes=4) as pool:
        results = pool.map(worker, range(10))
        print(f"Results: {results}")

# Sharing Data between Processes
def data_sharing_example():
    def modifier(n, arr, d):
        n.value = 3.14159
        arr[0] = 10
        d['key'] = "value"

    num = mp.Value('d', 0.0)
    arr = mp.Array('i', [0, 0, 0])
    manager = mp.Manager()
    d = manager.dict()

    p = mp.Process(target=modifier, args=(num, arr, d))
    p.start()
    p.join()

    print(f"Modified value: {num.value}")
    print(f"Modified array: {list(arr)}")
    print(f"Modified dict: {dict(d)}")

# Inter-Process Communication (IPC)
def ipc_example():
    def producer(queue):
        for i in range(5):
            queue.put(f"Item {i}")
            time.sleep(1)
        queue.put(None)  # Sentinel to signal the end

    def consumer(queue):
        while True:
            item = queue.get()
            if item is None:
                break
            print(f"Consumed {item}")

    q = mp.Queue()
    prod = mp.Process(target=producer, args=(q,))
    cons = mp.Process(target=consumer, args=(q,))

    prod.start()
    cons.start()

    prod.join()
    cons.join()

# Using Pipes for IPC
def pipe_example():
    def sender(conn):
        conn.send(['Hello', 42, 3.14])
        conn.close()

    def receiver(conn):
        print(f"Received: {conn.recv()}")
        conn.close()

    parent_conn, child_conn = mp.Pipe()
    p1 = mp.Process(target=sender, args=(child_conn,))
    p2 = mp.Process(target=receiver, args=(parent_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# Process Synchronization
def synchronization_example():
    def worker(lock, i):
        with lock:
            print(f"Worker {i} entering critical section")
            time.sleep(1)
            print(f"Worker {i} leaving critical section")

    lock = mp.Lock()
    processes = [mp.Process(target=worker, args=(lock, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use Process Pools for CPU-bound tasks with a large number of small operations.
# 2. Minimize data sharing between processes to reduce overhead.
# 3. Use multiprocessing.Queue for inter-process communication instead of threading.Queue.
# 4. Properly handle process termination and cleanup.
# 5. Use context managers (with statements) when working with pools and other resources.

# Common Pitfalls:
# 1. Attempting to use threading concepts (like global variables) in multiprocessing.
# 2. Not considering the overhead of process creation and inter-process communication.
# 3. Incorrectly handling shared state, leading to race conditions or deadlocks.
# 4. Forgetting to join processes, potentially leading to zombie processes.
# 5. Using multiprocessing in environments where it's not supported (e.g., some web servers).

# Advanced Tips:
# 1. Use shared memory arrays for efficient data sharing between processes.
# 2. Implement custom process pools for fine-grained control over worker processes.
# 3. Utilize process barriers for synchronization in complex parallel algorithms.
# 4. Combine multiprocessing with other concurrency mechanisms (e.g., asyncio) for hybrid solutions.
# 5. Profile multiprocessing code to identify bottlenecks and optimize accordingly.

# Example: Custom Process Pool
class CustomProcessPool:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.task_queue = mp.Queue()
        self.result_queue = mp.Queue()
        self.processes = []
        self._start_processes()

    def _worker(self):
        while True:
            try:
                func, args = self.task_queue.get(timeout=1)
                if func is None:
                    break
                result = func(*args)
                self.result_queue.put(result)
            except queue.Empty:
                continue

    def _start_processes(self):
        for _ in range(self.num_processes):
            p = mp.Process(target=self._worker)
            p.start()
            self.processes.append(p)

    def apply_async(self, func, args):
        self.task_queue.put((func, args))

    def get_results(self):
        results = []
        while not self.result_queue.empty():
            results.append(self.result_queue.get())
        return results

    def close(self):
        for _ in range(self.num_processes):
            self.task_queue.put((None, None))
        for p in self.processes:
            p.join()

def custom_pool_example():
    def task(x):
        return x * x

    pool = CustomProcessPool(4)
    for i in range(10):
        pool.apply_async(task, (i,))

    time.sleep(2)  # Allow time for tasks to complete
    results = pool.get_results()
    print(f"Custom pool results: {results}")
    pool.close()

# 4. Integration and Real-World Applications
# ------------------------------------------
# Multiprocessing is widely used in various Python applications:

# 1. Scientific Computing: Parallel processing of large datasets (e.g., NumPy, SciPy).
# 2. Image and Video Processing: Parallel frame processing in computer vision tasks.
# 3. Web Scraping: Concurrent fetching and processing of web pages.
# 4. Machine Learning: Parallel training of models or hyperparameter tuning.
# 5. Financial Modeling: Parallel simulation of complex financial scenarios.

# Real-world example: Parallel Image Processing
def parallel_image_processing():
    def process_image(image):
        # Simulate image processing
        time.sleep(0.5)
        return f"Processed {image}"

    images = [f"image_{i}.jpg" for i in range(20)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_image, images))

    print(f"Processed images: {results}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# 1. Distributed Computing: Extending multiprocessing across multiple machines (e.g., using libraries like Dask).
# 2. GPU Acceleration: Combining multiprocessing with GPU computing (e.g., using CUDA with PyCUDA).
# 3. Adaptive Load Balancing: Dynamic adjustment of workload distribution among processes.
# 4. Fault Tolerance: Implementing robust error handling and recovery in multiprocess systems.
# 5. Hybrid Parallelism: Combining multiprocessing with multithreading and asynchronous I/O for optimal performance.

# Example: Hybrid Parallelism
def hybrid_parallelism_example():
    async def async_task(x):
        await asyncio.sleep(0.1)
        return x * 2

    def process_task(x):
        import asyncio
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(async_task(x))

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_task, range(10)))

    print(f"Hybrid parallelism results: {results}")

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: When should I use multiprocessing instead of threading?
# A: Use multiprocessing for CPU-bound tasks that can benefit from parallel execution on multiple cores.
#    Threading is more suitable for I/O-bound tasks where the GIL is not a bottleneck.

# Q: How can I debug multiprocessing code?
# A: 1. Use logging to track process execution.
#    2. Set the 'spawn' start method for better debugging support on all platforms.
#    3. Use multiprocessing.get_logger() and set its level for detailed logging.
#    4. Run processes with the 'fork' method on Unix for easier debugging in IDEs.

# Q: How do I handle exceptions in child processes?
# A: Use error callbacks with apply_async() or handle exceptions within the worker function and communicate them back to the main process.

def exception_handling_in_processes():
    def worker():
        raise ValueError("An error occurred in the process")

    def error_callback(error):
        print(f"Error in child process: {error}")

    pool = mp.Pool(processes=1)
    pool.apply_async(worker, error_callback=error_callback)
    pool.close()
    pool.join()

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. multiprocessing: Built-in module for working with processes
# 2. concurrent.futures: High-level interface for asynchronous execution
# 3. joblib: Simple parallel processing
# 4. Dask: Flexible library for parallel computing
# 5. Ray: Distributed computing framework
# 6. mpi4py: Python bindings for the Message Passing Interface (MPI)

# Resources:
# 1. "Python Cookbook" by David Beazley and Brian K. Jones
# 2. "High Performance Python" by Micha Gorelick and Ian Ozsvald
# 3. Python's official documentation on multiprocessing: https://docs.python.org/3/library/multiprocessing.html
# 4. "Parallel Programming with Python" by Jan Palach
# 5. Real Python's Multiprocessing guide: https://realpython.com/python-concurrency/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_analysis():
    def cpu_bound_task(n):
        return sum(i * i for i in range(n))

    def run_sequential(numbers):
        return [cpu_bound_task(num) for num in numbers]

    def run_parallel(numbers):
        with mp.Pool() as pool:
            return pool.map(cpu_bound_task, numbers)

    numbers = [10**7 + i for i in range(8)]

    start = time.time()
    sequential_result = run_sequential(numbers)
    sequential_time = time.time() - start

    start = time.time()
    parallel_result = run_parallel(numbers)
    parallel_time = time.time() - start

    print(f"Sequential time: {sequential_time:.2f} seconds")
    print(f"Parallel time: {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")

# 9. How to Contribute
# --------------------
# To contribute to this note sheet:
# 1. Fork the repository containing this file.
# 2. Make your changes or additions.
# 3. Ensure all code examples are correct and follow the established style.
# 4. Add comments explaining new concepts or functions.
# 5. Update the Table of Contents if necessary.
# 6. Submit a pull request with a clear description of your changes.

# Guidelines for contributions:
# - Maintain the current format and style.
# - Provide working code examples for new concepts.
# - Include performance considerations for new functions.
# - Add relevant references or citations for advanced topics.

# When adding new sections or expanding existing ones, consider the following:
# - Relevance to the main topic of multiprocessing in Python.
# - Clarity and depth of explanations.
# - Practical applicability of examples and tips.
# - Up-to-date information on Python language features and best practices.

# Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

def main():
    print("1. Basic Process Example")
    basic_process_example()

    print("\n2. Process Pool Example")
    process_pool_example()

    print("\n3. Data Sharing Example")
    data_sharing_example()

    print("\n4. Inter-Process Communication Example")
    ipc_example()

    print("\n5. Pipe Example")
    pipe_example()

    print("\n6. Synchronization Example")
    synchronization_example()

    print("\n7. Custom Process Pool Example")
    custom_pool_example()

    print("\n8. Parallel Image Processing Example")
    parallel_image_processing()

    print("\n9. Hybrid Parallelism Example")
    hybrid_parallelism_example()

    print("\n10. Exception Handling in Processes")
    exception_handling_in_processes()

    print("\n11. Performance Analysis")
    performance_analysis()

if __name__ == "__main__":
    main()