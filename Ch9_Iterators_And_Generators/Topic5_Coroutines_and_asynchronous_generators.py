"""
Iterators and Generators - Coroutines and asynchronous generators - in the Python Programming Language
=====================================================================================================

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
Coroutines and asynchronous generators are advanced concepts in Python that enable efficient concurrent programming, particularly for I/O-bound tasks. They build upon the foundation of generators, providing powerful tools for managing asynchronous operations.

Historical context:
- Coroutines were introduced in Python 2.5 (2006) with PEP 342, enhancing generator functionality.
- The asyncio library was introduced in Python 3.4 (2014) with PEP 3156, providing a framework for asynchronous programming.
- Native coroutines (async/await syntax) were added in Python 3.5 (2015) with PEP 492.
- Asynchronous generators were introduced in Python 3.6 (2016) with PEP 525.

Significance:
- Coroutines and asynchronous generators allow for efficient handling of concurrent operations without the complexity of traditional multi-threading.
- They enable writing clear, sequential-looking code for asynchronous tasks, improving readability and maintainability.
- These concepts are crucial for building scalable, high-performance applications, especially in I/O-bound scenarios.

Common use cases:
- Web scraping and API interactions
- Real-time data processing and streaming
- Network servers and clients
- Database operations
- Microservices and distributed systems

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

import asyncio
import aiohttp
import time
from typing import AsyncGenerator, List, Dict, Any

async def main():
    """
    Main function to demonstrate coroutines and asynchronous generators.
    """
    print("1. Basic Coroutine")
    await basic_coroutine()
    
    print("\n2. Asynchronous Generator")
    async for num in async_countdown(5):
        print(num)
    
    print("\n3. Parallel Execution with asyncio.gather")
    await parallel_execution()
    
    print("\n4. Web Scraping with Asynchronous Generator")
    urls = [
        "https://api.github.com/events",
        "https://api.github.com/emojis",
        "https://api.github.com/meta"
    ]
    async for result in async_fetch_urls(urls):
        print(f"Fetched: {result['url']}, Status: {result['status']}")
    
    print("\n5. Error Handling in Coroutines")
    await error_handling_example()

async def basic_coroutine():
    """
    A simple coroutine demonstrating the basic syntax and behavior.
    """
    print("Starting coroutine")
    await asyncio.sleep(1)  # Simulate an I/O operation
    print("Coroutine completed")

async def async_countdown(n: int) -> AsyncGenerator[int, None]:
    """
    An asynchronous generator that counts down from n to 1.
    
    Args:
        n (int): The starting number for the countdown.
    
    Yields:
        int: The next number in the countdown sequence.
    """
    while n > 0:
        await asyncio.sleep(0.5)  # Simulate an I/O operation
        yield n
        n -= 1

async def parallel_execution():
    """
    Demonstrates parallel execution of coroutines using asyncio.gather.
    """
    async def task(name: str, duration: float) -> str:
        await asyncio.sleep(duration)
        return f"Task {name} completed in {duration} seconds"
    
    start_time = time.time()
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )
    end_time = time.time()
    
    for result in results:
        print(result)
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

async def async_fetch_urls(urls: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
    """
    An asynchronous generator that fetches multiple URLs concurrently.
    
    Args:
        urls (List[str]): A list of URLs to fetch.
    
    Yields:
        Dict[str, Any]: A dictionary containing the URL and the response status.
    """
    async with aiohttp.ClientSession() as session:
        for url in urls:
            try:
                async with session.get(url) as response:
                    yield {"url": url, "status": response.status}
            except aiohttp.ClientError as e:
                yield {"url": url, "status": f"Error: {str(e)}"}

async def error_handling_example():
    """
    Demonstrates error handling in coroutines.
    """
    try:
        await risky_coroutine()
    except ValueError as e:
        print(f"Caught an error: {e}")

async def risky_coroutine():
    """
    A coroutine that might raise an exception.
    """
    await asyncio.sleep(1)
    raise ValueError("This is a simulated error")

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------

Best Practices:
1. Use 'async with' for managing asynchronous context managers.
2. Prefer 'asyncio.create_task()' over 'asyncio.ensure_future()' for creating tasks.
3. Use 'asyncio.gather()' for concurrent execution of multiple coroutines.
4. Implement proper error handling and cancellation in asynchronous code.
5. Use type hints to improve code readability and catch potential errors.

Common Pitfalls:
1. Mixing synchronous and asynchronous code incorrectly.
2. Forgetting to await coroutines, leading to unexpected behavior.
3. Blocking the event loop with CPU-bound tasks.
4. Not handling exceptions in asynchronous code properly.

Advanced Tips:
1. Use 'asyncio.shield()' to protect critical operations from cancellation.
2. Implement custom asynchronous context managers using 'async with'.
3. Use 'asyncio.wait()' with timeout for more complex task management.
4. Implement backpressure mechanisms in asynchronous generators to control data flow.

Performance Considerations:
1. Use 'uvloop' as an alternative event loop implementation for improved performance.
2. Avoid excessive context switching by batching small I/O operations.
3. Profile asynchronous code to identify bottlenecks and optimize accordingly.

Edge Cases:
1. Handle 'asyncio.CancelledError' appropriately to ensure proper cleanup.
2. Be aware of the differences in exception handling between coroutines and regular functions.

Testing:
Here's an example of how to write unit tests for coroutines and asynchronous generators:
"""

import unittest

class TestAsyncCountdown(unittest.IsolatedAsyncioTestCase):
    async def test_async_countdown(self):
        result = []
        async for num in async_countdown(3):
            result.append(num)
        self.assertEqual(result, [3, 2, 1])
    
    async def test_async_countdown_empty(self):
        result = []
        async for num in async_countdown(0):
            result.append(num)
        self.assertEqual(result, [])

# Uncomment the following lines to run the tests
# if __name__ == '__main__':
#     unittest.main()

"""
4. Integration and Real-World Applications
------------------------------------------

1. Web Applications:
   Asynchronous frameworks like FastAPI and Sanic use coroutines to handle
   concurrent requests efficiently.

2. Microservices:
   Coroutines and asynchronous generators are used in microservices architectures
   for efficient inter-service communication and data streaming.

3. Database Operations:
   Libraries like asyncpg use coroutines to perform asynchronous database
   operations, improving throughput for I/O-bound database tasks.

4. Web Scraping and API Interactions:
   Libraries like aiohttp leverage coroutines for concurrent HTTP requests,
   significantly speeding up web scraping and API interactions.

5. Real-time Data Processing:
   Asynchronous generators are used in real-time data processing pipelines
   to handle streaming data efficiently.

Example: Implementing a simple asynchronous web scraper
"""

import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()

async def parse_html(html: str) -> List[str]:
    soup = BeautifulSoup(html, 'html.parser')
    return [a.get('href') for a in soup.find_all('a', href=True)]

async def crawl_website(start_url: str, max_depth: int = 2) -> AsyncGenerator[str, None]:
    visited = set()
    async with aiohttp.ClientSession() as session:
        async def crawl(url: str, depth: int):
            if url in visited or depth > max_depth:
                return
            visited.add(url)
            try:
                html = await fetch_url(session, url)
                links = await parse_html(html)
                yield url
                for link in links:
                    await crawl(link, depth + 1)
            except Exception as e:
                print(f"Error crawling {url}: {e}")
        
        async for url in crawl(start_url, 0):
            yield url

# Usage
# async for url in crawl_website("https://example.com"):
#     print(f"Crawled: {url}")

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------

1. Structured Concurrency:
   PEP 654 introduces structured concurrency to Python, providing better
   control over the lifetime and cancellation of concurrent tasks.

2. Asynchronous Comprehensions:
   PEP 530 introduced asynchronous comprehensions and generator expressions,
   allowing for more concise asynchronous code.

3. Type Hints for Coroutines:
   The typing module provides support for type hinting coroutines and
   asynchronous generators, improving code clarity and static analysis.

4. Integration with Other Paradigms:
   Exploring ways to integrate asynchronous programming with functional
   programming concepts and reactive programming paradigms.

5. Asynchronous Context Managers:
   PEP 492 introduced asynchronous context managers, allowing for resource
   management in asynchronous code.

Example: Using asynchronous comprehensions and context managers
"""

import asyncio
from typing import List, AsyncIterator

async def aiter(iterable):
    for item in iterable:
        yield item
        await asyncio.sleep(0.1)

async def async_comprehension_example(data: List[int]) -> List[int]:
    return [x async for x in aiter(data) if x % 2 == 0]

class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        print("Releasing resource")
        await asyncio.sleep(1)
    
    async def use_resource(self):
        print("Using resource")
        await asyncio.sleep(1)

async def async_context_manager_example():
    async with AsyncResource() as resource:
        await resource.use_resource()

# Usage
# asyncio.run(async_context_manager_example())

"""
6. FAQs and Troubleshooting
---------------------------

Q: What's the difference between a coroutine and an asynchronous generator?
A: A coroutine is a special function defined with 'async def' that can be paused
   and resumed. An asynchronous generator is a coroutine that can yield values
   using 'async for'.

Q: How do I run synchronous code in an asynchronous context?
A: Use 'asyncio.to_thread()' or 'loop.run_in_executor()' to run synchronous
   code without blocking the event loop.

Q: How can I debug asynchronous code effectively?
A: Use 'asyncio.run()' with debug mode enabled, utilize logging, and consider
   using tools like 'aiomonitor' for runtime introspection.

Q: How do I handle timeouts in asynchronous operations?
A: Use 'asyncio.wait_for()' or 'asyncio.timeout()' to set timeouts for
   asynchronous operations.

Troubleshooting Guide:
1. Event loop is closed error:
   - Ensure you're not closing the event loop prematurely.
   - Use 'asyncio.run()' instead of manually creating and closing loops.

2. Coroutine was never awaited warning:
   - Always await coroutines or wrap them in tasks using 'asyncio.create_task()'.

3. Unexpected hanging or blocking:
   - Check for synchronous operations blocking the event loop.
   - Use profiling tools to identify bottlenecks.

4. Task cancellation not working as expected:
   - Implement proper cancellation handling in your coroutines.
   - Use 'asyncio.shield()' to protect critical sections from cancellation.

7. Recommended Tools, Libraries, and Resources
----------------------------------------------

Tools and Libraries:
1. asyncio: Built-in library for writing asynchronous code
2. aiohttp: Asynchronous HTTP client/server framework
3. uvloop: Drop-in replacement for asyncio's event loop, offering better performance
4. aiodebug: Debugging and profiling tools for asyncio
5. aiomonitor: Monitor and manage asyncio programs

Resources:
1. "Python Concurrency with asyncio" by Matthew Fowler
2. "Asynchronous Programming in Python" by Caleb Hattingh
3. PEP 3156 - Asynchronous IO Support Rebooted: the "asyncio" Module
4. PEP 492 - Coroutines with async and await syntax
5. AsyncIO documentation: https://docs.python.org/3/library/asyncio.html

8. Performance Analysis and Optimization
----------------------------------------

Profiling asynchronous code:
Use 'aiodebug' or custom timing decorators to profile coroutines and asynchronous generators.

Example of a timing decorator for coroutines:
"""

import functools
import time

def async_timed():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func.__name__} took {total:.4f} seconds')
        return wrapped
    return wrapper

@async_timed()
async def timed_coroutine():
    await asyncio.sleep(1)

# Usage
# asyncio.run(timed_coroutine())

"""
Optimization strategies:
1. Use 'uvloop' for improved event loop performance
2. Implement caching for expensive computations or I/O operations
3. Use connection pooling for database and HTTP connections
4. Batch small I/O operations to reduce context switching

Example of connection pooling with aiohttp:
"""

async def fetch_with_pool(urls: List[str]):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(session.get(url)) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [await r.text() for r in responses]

# Usage
# results = asyncio.run(fetch_with_pool(['https://example.com', 'https://example.org']))

"""
9. How to Contribute (continued)
--------------------

4. Add comments explaining new concepts or functions.
5. Update the Table of Contents if necessary.
6. Submit a pull request with a clear description of your changes.

Guidelines for contributions:
- Maintain the current format and style.
- Provide working code examples for new concepts.
- Include performance considerations for new functions.
- Add relevant references or citations for advanced topics.
- Ensure compatibility with Python 3.7+ unless explicitly noted.
- Write clear, concise explanations for complex topics.
- Include unit tests for new functionality when applicable.

Remember, the goal is to keep this note sheet as an authoritative and up-to-date resource for Python developers of all skill levels.

Conclusion
----------
Coroutines and asynchronous generators are powerful features in Python that enable efficient concurrent programming, particularly for I/O-bound tasks. They provide a way to write clear, sequential-looking code for asynchronous operations, improving both performance and readability.

As the Python language and its ecosystem continue to evolve, so too will the patterns and best practices surrounding asynchronous programming. Stay informed about new developments in the Python community, and don't hesitate to experiment with innovative uses of coroutines and asynchronous generators in your projects.

Thank you for using this expert-level note sheet on coroutines and asynchronous generators in Python. Happy coding!
"""

# Additional examples and advanced concepts

import asyncio
import aiohttp
from typing import List, Dict, Any

async def rate_limited_fetch(urls: List[str], rate_limit: int) -> AsyncGenerator[Dict[str, Any], None]:
    """
    An asynchronous generator that fetches URLs with a rate limit.

    Args:
        urls (List[str]): A list of URLs to fetch.
        rate_limit (int): The maximum number of concurrent requests.

    Yields:
        Dict[str, Any]: A dictionary containing the URL and the response content.
    """
    semaphore = asyncio.Semaphore(rate_limit)
    async with aiohttp.ClientSession() as session:
        async def fetch(url: str) -> Dict[str, Any]:
            async with semaphore:
                try:
                    async with session.get(url) as response:
                        content = await response.text()
                        return {"url": url, "content": content}
                except aiohttp.ClientError as e:
                    return {"url": url, "error": str(e)}

        tasks = [asyncio.create_task(fetch(url)) for url in urls]
        for task in asyncio.as_completed(tasks):
            yield await task

async def pipeline_example() -> None:
    """
    Demonstrates an asynchronous pipeline using coroutines and generators.
    """
    async def producer() -> AsyncGenerator[int, None]:
        for i in range(1, 6):
            await asyncio.sleep(0.1)
            yield i

    async def square(numbers: AsyncGenerator[int, None]) -> AsyncGenerator[int, None]:
        async for number in numbers:
            yield number ** 2

    async def consumer(squares: AsyncGenerator[int, None]) -> None:
        async for square in squares:
            print(f"Consumed: {square}")

    numbers = producer()
    squares = square(numbers)
    await consumer(squares)

async def timeout_handling_example() -> None:
    """
    Demonstrates handling timeouts in asynchronous operations.
    """
    async def long_running_task() -> str:
        await asyncio.sleep(5)
        return "Task completed"

    try:
        result = await asyncio.wait_for(long_running_task(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("The task took too long and was cancelled")

class AsyncIteratorWrapper:
    """
    A wrapper class that converts a synchronous iterator into an asynchronous one.
    """
    def __init__(self, sync_iter):
        self.sync_iter = sync_iter

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self.sync_iter)
        except StopIteration:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)  # Simulate asynchronous behavior
        return value

async def async_iterator_example() -> None:
    """
    Demonstrates the use of a custom asynchronous iterator.
    """
    sync_list = [1, 2, 3, 4, 5]
    async_iter = AsyncIteratorWrapper(iter(sync_list))
    
    async for item in async_iter:
        print(f"Async Item: {item}")

async def main():
    print("1. Rate Limited URL Fetching")
    urls = [
        "https://api.github.com/events",
        "https://api.github.com/emojis",
        "https://api.github.com/meta",
        "https://api.github.com/feeds",
        "https://api.github.com/notifications"
    ]
    async for result in rate_limited_fetch(urls, rate_limit=2):
        print(f"Fetched: {result['url']}")
    
    print("\n2. Asynchronous Pipeline")
    await pipeline_example()
    
    print("\n3. Timeout Handling")
    await timeout_handling_example()
    
    print("\n4. Custom Asynchronous Iterator")
    await async_iterator_example()

if __name__ == "__main__":
    asyncio.run(main())

# Uncomment the following lines to run the unit tests
# import unittest
# unittest.main(argv=[''], exit=False)