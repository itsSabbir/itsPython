# Concurrency and Parallelism - Threading and the Global Interpreter Lock (GIL) - in the Python Programming Language
# ================================================================================================================

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

import threading
import time
import queue
import concurrent.futures
import multiprocessing
import cProfile
import pstats
import io
from typing import List, Callable, Any

# 1. Overview and Historical Context
# ----------------------------------
# Concurrency and parallelism are fundamental concepts in modern software development,
# enabling efficient utilization of computing resources and improved performance.
# In Python, these concepts are closely tied to the Global Interpreter Lock (GIL).

# Historical context:
# - Python's threading module was introduced in Python 1.5.2 (1999).
# - The GIL has been part of CPython since its inception.
# - Python 2.6 (2008) introduced the multiprocessing module to bypass GIL limitations.
# - Python 3.2 (2011) saw improvements in GIL implementation, reducing lock contention.
# - Python 3.4 (2014) introduced the concurrent.futures module for higher-level abstractions.

# Significance:
# - Threading allows concurrent execution within a single process.
# - The GIL ensures thread safety but can limit parallelism in CPU-bound tasks.
# - Understanding the GIL is crucial for writing efficient concurrent Python code.

# Common use cases:
# - I/O-bound tasks (e.g., web scraping, network operations)
# - GUI applications to keep the interface responsive
# - Parallel processing of independent data

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Basic Threading Example
def basic_thread_example():
    def worker(name):
        print(f"Worker {name} starting")
        time.sleep(2)
        print(f"Worker {name} finished")

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All workers finished")

# Thread Synchronization with Lock
def thread_synchronization_example():
    counter = 0
    lock = threading.Lock()

    def increment(amount):
        nonlocal counter
        for _ in range(amount):
            with lock:
                counter += 1

    threads = []
    for _ in range(5):
        t = threading.Thread(target=increment, args=(1000000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value: {counter}")

# Producer-Consumer Pattern
def producer_consumer_example():
    q = queue.Queue(maxsize=10)

    def producer():
        for i in range(20):
            q.put(i)
            print(f"Produced: {i}")
            time.sleep(0.1)

    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            print(f"Consumed: {item}")
            q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    q.put(None)  # Signal to stop the consumer
    consumer_thread.join()

# Using concurrent.futures for Thread Pool
def concurrent_futures_example():
    def worker(n):
        time.sleep(n)
        return f"Slept for {n} seconds"

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_to_sleep = {executor.submit(worker, i): i for i in range(5)}
        for future in concurrent.futures.as_completed(future_to_sleep):
            sleep_time = future_to_sleep[future]
            try:
                result = future.result()
                print(f"Task {sleep_time}: {result}")
            except Exception as e:
                print(f"Task {sleep_time} generated an exception: {e}")

# Demonstrating GIL limitations
def gil_limitation_example():
    def cpu_bound_task(n):
        return sum(i * i for i in range(n))

    def run_single_threaded():
        start = time.time()
        results = [cpu_bound_task(10**7) for _ in range(4)]
        end = time.time()
        print(f"Single-threaded time: {end - start:.2f} seconds")

    def run_multi_threaded():
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(cpu_bound_task, [10**7] * 4))
        end = time.time()
        print(f"Multi-threaded time: {end - start:.2f} seconds")

    run_single_threaded()
    run_multi_threaded()

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use threading for I/O-bound tasks, multiprocessing for CPU-bound tasks.
# 2. Minimize shared state between threads to reduce lock contention.
# 3. Use higher-level abstractions like concurrent.futures when possible.
# 4. Always join threads to ensure proper cleanup and avoid zombie threads.
# 5. Use thread-safe data structures from the queue module for inter-thread communication.

# Common Pitfalls:
# 1. Race conditions due to improper synchronization.
# 2. Deadlocks from incorrect lock ordering.
# 3. Over-threading, which can lead to increased context switching overhead.
# 4. Relying on threads for CPU-bound tasks, ignoring GIL limitations.
# 5. Failing to handle exceptions in threads, which can silently crash the program.

# Advanced Tips:
# 1. Use thread local storage for thread-specific data.
# 2. Implement custom thread pools for fine-grained control.
# 3. Use condition variables for complex synchronization scenarios.
# 4. Leverage asyncio for cooperative multitasking in I/O-bound scenarios.
# 5. Profile threaded code to identify bottlenecks and optimize accordingly.

# Example: Custom Thread Pool
class CustomThreadPool:
    def __init__(self, num_threads):
        self.tasks = queue.Queue()
        self.results = queue.Queue()
        self.threads = [threading.Thread(target=self._worker) for _ in range(num_threads)]
        for thread in self.threads:
            thread.start()

    def _worker(self):
        while True:
            task = self.tasks.get()
            if task is None:
                break
            func, args = task
            try:
                result = func(*args)
                self.results.put((True, result))
            except Exception as e:
                self.results.put((False, e))
            self.tasks.task_done()

    def submit(self, func: Callable, *args):
        self.tasks.put((func, args))

    def shutdown(self):
        for _ in self.threads:
            self.tasks.put(None)
        for thread in self.threads:
            thread.join()

    def get_results(self):
        results = []
        while not self.results.empty():
            results.append(self.results.get())
        return results

def custom_thread_pool_example():
    def task(n):
        time.sleep(n)
        return f"Task {n} completed"

    pool = CustomThreadPool(3)
    for i in range(5):
        pool.submit(task, i)

    pool.shutdown()
    results = pool.get_results()
    for success, result in results:
        if success:
            print(result)
        else:
            print(f"Error: {result}")

# 4. Integration and Real-World Applications
# ------------------------------------------
# Threading and concurrency are widely used in various Python applications:

# 1. Web Scraping: Concurrent requests to improve data collection speed.
# 2. Web Servers: Handling multiple client connections simultaneously.
# 3. GUI Applications: Keeping the interface responsive while performing background tasks.
# 4. Data Processing: Parallel processing of large datasets.
# 5. Game Development: Managing game state and rendering concurrently.

# Real-world example: Concurrent Web Scraper
import requests
from bs4 import BeautifulSoup

def concurrent_web_scraper(urls: List[str]) -> List[str]:
    def fetch_url(url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string if soup.title else "No title found"

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}
        results = []
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                title = future.result()
                results.append(f"{url}: {title}")
            except Exception as e:
                results.append(f"{url}: Error - {str(e)}")
    return results

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# 1. Subinterpreters: A proposed feature to run multiple Python interpreters in the same process, each with its own GIL.
# 2. Nogil Python: An experimental implementation of Python without the GIL, allowing true parallelism.
# 3. Asynchronous I/O: Growing adoption of asyncio for concurrent I/O operations.
# 4. Just-In-Time (JIT) compilation: Projects like Pyston and PyPy aim to improve Python's performance, including concurrent execution.
# 5. Hybrid approaches: Combining threading with multiprocessing or distributed computing for scalable solutions.

# Example: Hybrid Threading and Multiprocessing
def hybrid_concurrent_example():
    def cpu_bound_task(n):
        return sum(i * i for i in range(n))

    def io_bound_task(url):
        response = requests.get(url)
        return len(response.content)

    cpu_intensive_numbers = [10**7] * 4
    io_intensive_urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org"
    ]

    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as process_executor:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as thread_executor:
            cpu_futures = [process_executor.submit(cpu_bound_task, n) for n in cpu_intensive_numbers]
            io_futures = [thread_executor.submit(io_bound_task, url) for url in io_intensive_urls]

            for future in concurrent.futures.as_completed(cpu_futures + io_futures):
                print(f"Task result: {future.result()}")

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: When should I use threading vs. multiprocessing?
# A: Use threading for I/O-bound tasks and multiprocessing for CPU-bound tasks.
#    Threading is lighter and works well when waiting for external resources.
#    Multiprocessing bypasses the GIL but has more overhead.

# Q: How can I debug race conditions in threaded code?
# A: 1. Use logging to track thread execution.
#    2. Employ thread-safe data structures.
#    3. Use the threading.Lock() to synchronize access to shared resources.
#    4. Consider using the 'threading' module's debugging features (e.g., threading.settrace()).

# Q: How do I handle exceptions in threads?
# A: Wrap the thread's target function in a try-except block and log or queue the exceptions.
#    When using ThreadPoolExecutor, exceptions are preserved and can be retrieved from the Future objects.

def exception_handling_in_threads():
    def worker():
        raise ValueError("An error occurred in the thread")

    def exception_handler(args):
        print(f"Caught an exception: {args}")

    t = threading.Thread(target=worker)
    t.setDaemon(True)
    
    t.start()
    t.join()

    threading.excepthook = exception_handler

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. threading: Built-in module for working with threads
# 2. multiprocessing: Built-in module for spawning processes
# 3. concurrent.futures: High-level interface for asynchronous execution
# 4. asyncio: Built-in module for writing concurrent code using coroutines
# 5. queue: Thread-safe queue implementation
# 6. threading.local(): Thread-local storage of data

# Resources:
# 1. "Python Concurrency with asyncio" by Matthew Fowler
# 2. "High Performance Python" by Micha Gorelick and Ian Ozsvald
# 3. Python's official documentation on threading: https://docs.python.org/3/library/threading.html
# 4. David Beazley's "Python Concurrency From the Ground Up" talk: https://www.youtube.com/watch?v=MCs5OvhV9S4
# 5. Real Python's Concurrency guides: https://realpython.com/tutorials/concurrency/

# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_analysis():
    def cpu_bound_task(n):
        return sum(i * i for i in range(n))

    def run_threads(num_threads):
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            list(executor.map(cpu_bound_task, [10**6] * num_threads))

    def profile_threads(num_threads):
        profiler = cProfile.Profile()
        profiler.enable()
        run_threads(num_threads)
        profiler.disable()
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats()
        print(s.getvalue())

    print("Performance with 1 thread:")
    profile_threads(1)
    print("\nPerformance with 4 threads:")
    profile_threads(4)

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
# - Relevance to the main


# topic of concurrency, parallelism, threading, and the GIL in Python.
# - Clarity and depth of explanations.
# - Practical applicability of examples and tips.
# - Up-to-date information on Python language features and best practices.

# Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

def main():
    """
    Main function to demonstrate various concepts related to concurrency,
    parallelism, threading, and the GIL in Python.
    """
    print("1. Basic Threading Example")
    basic_thread_example()
    print("\n2. Thread Synchronization Example")
    thread_synchronization_example()
    print("\n3. Producer-Consumer Example")
    producer_consumer_example()
    print("\n4. Concurrent Futures Example")
    concurrent_futures_example()
    print("\n5. GIL Limitation Example")
    gil_limitation_example()
    print("\n6. Custom Thread Pool Example")
    custom_thread_pool_example()
    print("\n7. Concurrent Web Scraper Example")
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org"
    ]
    results = concurrent_web_scraper(urls)
    for result in results:
        print(result)
    print("\n8. Hybrid Concurrent Example")
    hybrid_concurrent_example()
    print("\n9. Exception Handling in Threads")
    exception_handling_in_threads()
    print("\n10. Performance Analysis")
    performance_analysis()

if __name__ == "__main__":
    main()