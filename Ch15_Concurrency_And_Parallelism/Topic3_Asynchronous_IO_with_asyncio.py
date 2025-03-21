# Concurrency and Parallelism - Asynchronous I/O with asyncio - in the Python Programming Language
# ===========================================================================================

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

import asyncio
import aiohttp
import time
from typing import List, Dict, Any, Coroutine
import random

# 1. Overview and Historical Context
# ----------------------------------
# Asynchronous I/O with asyncio is a concurrent programming paradigm in Python
# that allows efficient handling of I/O-bound operations without using threads.

# Historical context:
# - The asyncio module was introduced in Python 3.4 (2014) as a provisional API.
# - Python 3.5 (2015) added async and await keywords, simplifying asyncio usage.
# - Python 3.6 (2016) made asyncio a stable API and added asynchronous generators.
# - Python 3.7 (2018) introduced major improvements, including better performance and new syntax.

# Significance:
# - Enables efficient handling of thousands of concurrent connections.
# - Provides a foundation for building high-performance network applications.
# - Offers an alternative to thread-based concurrency for I/O-bound tasks.

# Common use cases:
# - Web scraping and API interactions
# - High-performance web servers and microservices
# - Real-time chat applications and websockets
# - Network protocols implementation

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

# Basic Coroutine
async def basic_coroutine():
    print("Start of coroutine")
    await asyncio.sleep(1)
    print("End of coroutine")

# Running a Coroutine
def run_coroutine():
    asyncio.run(basic_coroutine())

# Creating and Running Tasks
async def create_tasks():
    task1 = asyncio.create_task(asyncio.sleep(1))
    task2 = asyncio.create_task(asyncio.sleep(2))
    await task1
    await task2

# Coroutine with Return Value
async def coroutine_with_result():
    await asyncio.sleep(1)
    return "Result from coroutine"

# Gathering Multiple Coroutines
async def gather_coroutines():
    results = await asyncio.gather(
        coroutine_with_result(),
        coroutine_with_result(),
        coroutine_with_result()
    )
    print(f"Gathered results: {results}")

# Using aiohttp for Asynchronous HTTP Requests
async def fetch_url(url: str, session: aiohttp.ClientSession) -> str:
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls: List[str]):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Asynchronous Context Manager
class AsyncContextManager:
    async def __aenter__(self):
        print("Entering context")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        await asyncio.sleep(1)

async def use_async_context_manager():
    async with AsyncContextManager() as manager:
        print("Inside async context manager")

# Asynchronous Iterator
class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter < self.limit:
            await asyncio.sleep(0.1)
            self.counter += 1
            return self.counter
        raise StopAsyncIteration

async def use_async_iterator():
    async for i in AsyncCounter(5):
        print(f"Async iteration: {i}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use 'async def' for all coroutines, even if they don't contain 'await'.
# 2. Avoid blocking calls inside coroutines; use asyncio-compatible libraries.
# 3. Use asyncio.create_task() to run coroutines concurrently.
# 4. Prefer asyncio.gather() for running multiple coroutines in parallel.
# 5. Use asyncio.run() as the main entry point for asyncio programs.

# Common Pitfalls:
# 1. Mixing synchronous and asynchronous code incorrectly.
# 2. Forgetting to await coroutines or Tasks.
# 3. Using time.sleep() instead of asyncio.sleep() in coroutines.
# 4. Not handling exceptions in gathered tasks properly.
# 5. Creating too many tasks and overwhelming system resources.

# Advanced Tips:
# 1. Use asyncio.Queue for producer-consumer patterns.
# 2. Implement custom protocol with asyncio.Protocol for low-level networking.
# 3. Use asyncio.Lock, asyncio.Semaphore, and asyncio.Condition for synchronization.
# 4. Implement graceful shutdown mechanisms for long-running asyncio applications.
# 5. Use asyncio.shield() to protect critical operations from cancellation.

# Example: Producer-Consumer Pattern with asyncio.Queue
async def producer(queue: asyncio.Queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(f"Item {i}")
    await queue.put(None)  # Sentinel to signal end of production

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()

async def producer_consumer_example():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(producer_task, consumer_task)

# Example: Custom Protocol Implementation
class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print(f'Connection from {peername}')
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print(f'Data received: {message}')
        self.transport.write(data)

    def connection_lost(self, exc):
        print('Connection closed')

async def run_echo_server():
    server = await asyncio.get_event_loop().create_server(
        EchoServerProtocol, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

# 4. Integration and Real-World Applications
# ------------------------------------------
# asyncio is widely used in various Python applications:

# 1. Web Frameworks: aiohttp, FastAPI, Sanic for building high-performance web applications.
# 2. Database Drivers: asyncpg for PostgreSQL, aiomysql for MySQL, allowing non-blocking database operations.
# 3. Message Queues: aio-pika for RabbitMQ, allowing asynchronous message processing.
# 4. Websockets: websockets library for real-time communication in web applications.
# 5. Microservices: Used in conjunction with tools like Docker and Kubernetes for scalable microservices.

# Real-world example: Asynchronous Web Scraper
async def fetch_and_parse(url: str, session: aiohttp.ClientSession) -> Dict[str, Any]:
    async with session.get(url) as response:
        html = await response.text()
        # Simulate parsing (replace with actual parsing logic)
        await asyncio.sleep(0.1)
        return {"url": url, "title": html[:50]}  # Return first 50 chars as "title"

async def bulk_scrape(urls: List[str]) -> List[Dict[str, Any]]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_parse(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# 1. Structured Concurrency: Ensuring all started tasks are properly awaited and exceptions are propagated.
# 2. Asynchronous Context Managers and Iterators: For more idiomatic async code.
# 3. Type Hinting for Coroutines: Improved static type checking for async code.
# 4. Integration with other async frameworks: Combining asyncio with frameworks like Twisted or Tornado.
# 5. Asynchronous GUI Programming: Using asyncio with GUI frameworks for responsive applications.

# Example: Structured Concurrency with asyncio.TaskGroup (Python 3.11+)
async def structured_concurrency_example():
    async def worker(name: str, duration: float) -> str:
        await asyncio.sleep(duration)
        return f"Worker {name} finished after {duration} seconds"

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(worker("A", 2))
        task2 = tg.create_task(worker("B", 1))
        task3 = tg.create_task(worker("C", 3))

    results = [task1.result(), task2.result(), task3.result()]
    print("All tasks completed:", results)

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: How do I run a coroutine from synchronous code?
# A: Use asyncio.run() or create an event loop:
#    asyncio.run(coroutine())
#    or
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(coroutine())

# Q: How can I debug asyncio code?
# A: 1. Use logging to track coroutine execution.
#    2. Set the asyncio debug mode: asyncio.run(main(), debug=True)
#    3. Use 'async def main()' as the entry point for better error messages.
#    4. Use asyncio.get_event_loop().set_debug(True) for additional debug info.

# Q: How do I handle exceptions in asyncio?
# A: Use try/except blocks within coroutines, or handle exceptions when gathering tasks:

async def exception_handling_example():
    async def might_raise():
        await asyncio.sleep(1)
        raise ValueError("An error occurred")

    try:
        await asyncio.gather(might_raise(), might_raise(), return_exceptions=True)
    except Exception as e:
        print(f"Caught exception: {e}")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. aiohttp: Asynchronous HTTP client/server framework
# 2. uvloop: Drop-in replacement for asyncio event loop, offering better performance
# 3. aiodns: Asynchronous DNS resolver
# 4. aiofiles: Asynchronous file operations
# 5. asyncpg: High-performance PostgreSQL client library
# 6. pytest-asyncio: Pytest support for asyncio

# Resources:
# 1. "Python Asyncio" by Caleb Hattingh
# 2. "Using Asyncio in Python" by Caleb Hattingh
# 3. Python's official asyncio documentation: https://docs.python.org/3/library/asyncio.html
# 4. Real Python's asyncio guide: https://realpython.com/async-io-python/
# 5. PEP 3156 - Asynchronous IO Support Rebooted: https://www.python.org/dev/peps/pep-3156/

# 8. Performance Analysis and Optimization
# ----------------------------------------

async def io_bound_task(id: int):
    await asyncio.sleep(1)  # Simulate I/O operation
    return f"Task {id} completed"

def sync_io_bound_task(id: int):
    time.sleep(1)  # Simulate I/O operation
    return f"Task {id} completed"

async def performance_comparison():
    # Asynchronous execution
    start_time = time.time()
    async_results = await asyncio.gather(*(io_bound_task(i) for i in range(10)))
    async_time = time.time() - start_time
    print(f"Async execution time: {async_time:.2f} seconds")

    # Synchronous execution
    start_time = time.time()
    sync_results = [sync_io_bound_task(i) for i in range(10)]
    sync_time = time.time() - start_time
    print(f"Sync execution time: {sync_time:.2f} seconds")

    print(f"Speedup: {sync_time / async_time:.2f}x")

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
# - Relevance to the main topic of asyncio in Python.
# - Clarity and depth of explanations.
# - Practical applicability of examples and tips.
# - Up-to-date information on Python language features and best practices.

# Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

async def main():
    print("1. Basic Coroutine")
    await basic_coroutine()

    print("\n2. Creating and Running Tasks")
    await create_tasks()

    print("\n3. Gathering Multiple Coroutines")
    await gather_coroutines()

    print("\n4. Fetching Multiple URLs")
    urls = ["https://example.com", "https://python.org", "https://github.com"]
    results = await fetch_multiple_urls(urls)
    print(f"Fetched {len(results)} URLs")

    print("\n5. Using Async Context Manager")
    await use_async_context_manager()

    print("\n6. Using Async Iterator")
    await use_async_iterator()

    print("\n7. Producer-Consumer Example")
    await producer_consumer_example()

    print("\n8. Web Scraping Example")
    scrape_urls = ["https://news.ycombinator.com", "https://reddit.com", "https://python.org"]
    scrape_results = await bulk_scrape(scrape_urls)
    for result in scrape_results:
        print(f"Scraped {result['url']}: {result['title']}")

    print("\n9. Structured Concurrency Example")
    await structured_concurrency_example()

    print("\n10. Exception Handling Example")
    await exception_handling_example()

    print("\n11. Performance Comparison")
    await performance_comparison()

if __name__ == "__main__":
    asyncio.run(main())

# Additional Examples and Demonstrations

# Demonstrating asyncio.wait with timeout
async def wait_with_timeout_example():
    async def slow_operation(id):
        await asyncio.sleep(random.uniform(1, 5))
        return f"Result from operation {id}"

    tasks = [asyncio.create_task(slow_operation(i)) for i in range(5)]
    done, pending = await asyncio.wait(tasks, timeout=3.0)

    print(f"Completed tasks: {len(done)}")
    print(f"Pending tasks: {len(pending)}")

    for task in pending:
        task.cancel()

# Demonstrating asyncio.as_completed
async def as_completed_example():
    async def fetch_data(delay):
        await asyncio.sleep(delay)
        return f"Data fetched after {delay} seconds"

    delays = [3, 1, 4, 1, 5]
    tasks = [asyncio.create_task(fetch_data(delay)) for delay in delays]

    for coro in asyncio.as_completed(tasks):
        earliest_result = await coro
        print(earliest_result)

# Demonstrating asyncio.Lock for synchronization
async def lock_example():
    lock = asyncio.Lock()
    shared_resource = 0

    async def increment():
        nonlocal shared_resource
        async with lock:
            current_value = shared_resource
            await asyncio.sleep(0.1)  # Simulate some processing
            shared_resource = current_value + 1

    await asyncio.gather(*(increment() for _ in range(10)))
    print(f"Final value of shared resource: {shared_resource}")

# Demonstrating error handling and task cancellation
async def error_handling_and_cancellation():
    async def worker(id):
        try:
            while True:
                print(f"Worker {id} is running")
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            print(f"Worker {id} was cancelled")
            raise
        finally:
            print(f"Worker {id} is cleaning up")

    task1 = asyncio.create_task(worker(1))
    task2 = asyncio.create_task(worker(2))

    await asyncio.sleep(3)
    task1.cancel()
    task2.cancel()

    try:
        await asyncio.gather(task1, task2)
    except asyncio.CancelledError:
        print("Tasks were cancelled")

# Demonstrating asyncio with aiofiles for asynchronous file I/O
import aiofiles

async def file_io_example():
    async with aiofiles.open('example.txt', mode='w') as f:
        await f.write("Hello, Async World!")

    async with aiofiles.open('example.txt', mode='r') as f:
        content = await f.read()
        print(f"File content: {content}")

# Demonstrating integration with external event loops (e.g., Qt)
try:
    from PyQt5.QtWidgets import QApplication, QPushButton
    from PyQt5.QtCore import QTimer
    from qasync import QEventLoop, asyncSlot

    def qt_integration_example():
        app = QApplication([])
        loop = QEventLoop(app)
        asyncio.set_event_loop(loop)

        window = QPushButton("Click me")

        @asyncSlot()
        async def on_click():
            print("Button clicked")
            await asyncio.sleep(1)
            print("Async operation completed")

        window.clicked.connect(on_click)
        window.show()

        with loop:
            loop.run_forever()

except ImportError:
    print("PyQt5 and qasync are required for the Qt integration example")

# Update the main function to include the new examples
async def main():
    # ... (previous examples)

    print("\n12. Wait with Timeout Example")
    await wait_with_timeout_example()

    print("\n13. As Completed Example")
    await as_completed_example()

    print("\n14. Lock Example")
    await lock_example()

    print("\n15. Error Handling and Cancellation Example")
    await error_handling_and_cancellation()

    print("\n16. Asynchronous File I/O Example")
    await file_io_example()

    print("\n17. Qt Integration Example (run separately if PyQt5 and qasync are installed)")
    # Uncomment the following line to run the Qt example:
    # qt_integration_example()

if __name__ == "__main__":
    asyncio.run(main())