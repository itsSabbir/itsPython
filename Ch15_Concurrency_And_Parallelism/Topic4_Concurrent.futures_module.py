# Concurrency and Parallelism - Concurrent.futures module - in the Python Programming Language
# ==========================================================================================

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

import concurrent.futures
import time
import requests
import random
import math
from typing import List, Callable, Any
import unittest

# 1. Overview and Historical Context
# ----------------------------------
# The concurrent.futures module provides a high-level interface for asynchronously
# executing callables using threads or processes. It simplifies the use of threads
# and processes, making it easier to write concurrent code in Python.

# Historical context:
# - Introduced in Python 3.2 (2011) as part of PEP 3148.
# - Designed to provide a simpler interface than the lower-level threading and multiprocessing modules.
# - Inspired by Java's java.util.concurrent package.

# Significance:
# - Provides a unified API for both thread-based and process-based parallelism.
# - Simplifies the implementation of common parallelization patterns.
# - Offers built-in support for task scheduling, result handling, and error management.

# Common use cases:
# - Parallelizing CPU-bound tasks (using ProcessPoolExecutor)
# - Concurrent I/O operations (using ThreadPoolExecutor)
# - Batch processing of large datasets
# - Implementing producer-consumer patterns

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Basic usage of ThreadPoolExecutor
def thread_pool_example():
    def worker(num):
        """A sample worker function that performs a time-consuming operation."""
        time.sleep(1)
        return f"Result: {num * num}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(worker, i) for i in range(10)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

# Basic usage of ProcessPoolExecutor
def process_pool_example():
    def cpu_bound_task(n):
        """A CPU-bound task that calculates the sum of squares."""
        return sum(i * i for i in range(n))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(cpu_bound_task, [1000000, 2000000, 3000000])
        for result in results:
            print(f"Sum of squares: {result}")

# Using as_completed for handling results as they become available
def as_completed_example():
    def fetch_url(url):
        """Fetch the content of a URL."""
        response = requests.get(url)
        return f"{url}: {len(response.content)} bytes"

    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com"
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")
            else:
                print(data)

# Handling timeouts
def timeout_example():
    def long_running_task(n):
        time.sleep(n)
        return f"Task completed after {n} seconds"

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(long_running_task, 3)
        try:
            result = future.result(timeout=2)
            print(result)
        except concurrent.futures.TimeoutError:
            print("The task took too long to complete")

# Cancelling tasks
def cancellation_example():
    def cancelable_task(n):
        for i in range(n):
            if i % 100000 == 0:
                print(f"Progress: {i}/{n}")
            if concurrent.futures.Future.cancel:
                print("Task was cancelled")
                return
        return "Task completed successfully"

    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(cancelable_task, 10000000)
        time.sleep(0.1)
        future.cancel()
        try:
            result = future.result()
            print(result)
        except concurrent.futures.CancelledError:
            print("The task was cancelled")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use context managers (with statements) when working with executors.
# 2. Choose the appropriate executor (ThreadPoolExecutor or ProcessPoolExecutor) based on the task type.
# 3. Set appropriate max_workers to avoid overwhelming system resources.
# 4. Use as_completed() for handling results as they become available.
# 5. Implement proper error handling and timeout mechanisms.

# Common Pitfalls:
# 1. Using ProcessPoolExecutor for I/O-bound tasks, which can be inefficient.
# 2. Not handling exceptions raised by worker functions.
# 3. Overusing thread/process pools for short-lived tasks, leading to overhead.
# 4. Trying to use non-picklable objects with ProcessPoolExecutor.
# 5. Failing to properly shut down executors, potentially leading to resource leaks.

# Advanced Tips:
# 1. Use executor.map() for simple parallel iterations over a sequence.
# 2. Implement custom ThreadPoolExecutor or ProcessPoolExecutor for fine-grained control.
# 3. Combine concurrent.futures with asyncio for complex asynchronous workflows.
# 4. Use shared memory objects for efficient data sharing between processes.
# 5. Implement proper logging and monitoring for concurrent tasks.

# Example: Custom ThreadPoolExecutor
class CustomThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.futures = set()

    def submit(self, fn, *args, **kwargs):
        future = super().submit(fn, *args, **kwargs)
        self.futures.add(future)
        future.add_done_callback(self.futures.remove)
        return future

    def wait_for_all(self, timeout=None):
        return concurrent.futures.wait(self.futures, timeout=timeout)

def custom_executor_example():
    def worker(n):
        time.sleep(random.random())
        return n * n

    with CustomThreadPoolExecutor(max_workers=5) as executor:
        for i in range(10):
            executor.submit(worker, i)
        done, not_done = executor.wait_for_all(timeout=5)
        print(f"Completed tasks: {len(done)}, Pending tasks: {len(not_done)}")

# 4. Integration and Real-World Applications
# ------------------------------------------
# concurrent.futures is widely used in various Python applications:

# 1. Web scraping and data collection
# 2. Image and video processing
# 3. Scientific computing and data analysis
# 4. Distributed computing frameworks
# 5. Testing frameworks for parallel test execution

# Real-world example: Parallel image processing
from PIL import Image, ImageFilter

def parallel_image_processing(image_paths: List[str], output_dir: str):
    def process_image(image_path):
        with Image.open(image_path) as img:
            # Apply some image processing operations
            img = img.filter(ImageFilter.SHARPEN)
            img = img.convert('L')  # Convert to grayscale
            output_path = f"{output_dir}/{image_path.split('/')[-1]}"
            img.save(output_path)
            return output_path

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_image, path) for path in image_paths]
        for future in concurrent.futures.as_completed(futures):
            print(f"Processed image: {future.result()}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# 1. Integration with asyncio for complex asynchronous workflows
# 2. Distributed computing using concurrent.futures with libraries like Dask
# 3. Adaptive thread/process pool sizes based on system load
# 4. Enhanced cancellation and progress tracking capabilities
# 5. Improved integration with type hinting and static analysis tools

# Example: Combining concurrent.futures with asyncio
import asyncio

async def async_worker(n):
    await asyncio.sleep(1)
    return n * n

async def run_in_executor(executor, func, *args):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, func, *args)

async def combined_async_example():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [run_in_executor(executor, async_worker, i) for i in range(10)]
        results = await asyncio.gather(*tasks)
        print(f"Results: {results}")

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: When should I use ThreadPoolExecutor vs ProcessPoolExecutor?
# A: Use ThreadPoolExecutor for I/O-bound tasks and ProcessPoolExecutor for CPU-bound tasks.
#    ThreadPoolExecutor is lighter and works well when waiting for external resources.
#    ProcessPoolExecutor bypasses the GIL but has more overhead.

# Q: How can I handle exceptions raised in worker functions?
# A: Exceptions are automatically captured and can be accessed through the Future object:

def exception_handling_example():
    def worker(n):
        if n == 5:
            raise ValueError("Error for number 5")
        return n * n

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(worker, i) for i in range(10)]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(f"Result: {result}")
            except Exception as e:
                print(f"An exception occurred: {e}")

# Q: How can I implement a producer-consumer pattern with concurrent.futures?
# A: You can use a combination of submit() and as_completed():

def producer_consumer_example():
    def producer():
        for i in range(10):
            time.sleep(0.5)
            yield i

    def consumer(n):
        time.sleep(random.random())
        return f"Consumed {n}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for item in producer():
            future = executor.submit(consumer, item)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            print(future.result())

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. futures: Backport of concurrent.futures to Python 2.x
# 2. loky: Robust implementation of concurrent.futures.ProcessPoolExecutor
# 3. pebble: Extension of concurrent.futures with additional features
# 4. distributed: Distributed computing library built on concurrent.futures
# 5. joblib: Simple parallel computing in Python

# Resources:
# 1. "Python Concurrency with asyncio" by Matthew Fowler
# 2. "High Performance Python" by Micha Gorelick and Ian Ozsvald
# 3. Python's official documentation on concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html
# 4. Real Python's guide on concurrent.futures: https://realpython.com/python-concurrency/
# 5. PEP 3148 - futures - execute computations asynchronously: https://www.python.org/dev/peps/pep-3148/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_comparison():
    def cpu_bound_task(n):
        return sum(i * i for i in range(n))

    numbers = [10000000 + i for i in range(20)]

    # Sequential execution
    start_time = time.time()
    sequential_results = [cpu_bound_task(n) for n in numbers]
    sequential_time = time.time() - start_time
    print(f"Sequential execution time: {sequential_time:.2f} seconds")

    # Parallel execution with ProcessPoolExecutor
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        parallel_results = list(executor.map(cpu_bound_task, numbers))
    parallel_time = time.time() - start_time
    print(f"Parallel execution time: {parallel_time:.2f} seconds")

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
# - Relevance to the main topic of concurrent.futures in Python.
# - Clarity and depth of explanations.
# - Practical applicability of examples and tips.
# - Up-to-date information on Python language features and best practices.

# Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

def main():
    print("1. Thread Pool Example")
    thread_pool_example()

    print("\n2. Process Pool Example")
    process_pool_example()

    print("\n3. As Completed Example")
    as_completed_example()

    print("\n4. Timeout Example")
    timeout_example()

    print("\n5. Cancellation Example")
    cancellation_example()

    print("\n6. Custom Executor Example")
    custom_executor_example()

    print("\n7. Exception Handling Example")
    exception_handling_example()

    print("\n8. Producer-Consumer Example")
    producer_consumer_example()

    print("\n9. Performance Comparison")
    performance_comparison()

    print("\n10. Async Combination Example")
    asyncio.run(combined_async_example())

if __name__ == "__main__":
    main()