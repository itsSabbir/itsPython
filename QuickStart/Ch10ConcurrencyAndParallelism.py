#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Cheat Sheet: Concurrency and Parallelism
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import threading
import multiprocessing
import asyncio
import time
import concurrent.futures
import queue
from typing import List, Callable, Any

# 1. Threading

def worker(name: str) -> None:
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} finished")

# Creating and starting threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Waiting for all threads to complete
for t in threads:
    t.join()

print("All threads completed")

# Tip: Use threading for I/O-bound tasks, not CPU-bound tasks due to the Global Interpreter Lock (GIL)

# Thread-safe counter using Lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        current = counter
        time.sleep(0.1)  # Simulate some work
        counter = current + 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter value: {counter}")

# Tip: Always use locks or other synchronization primitives to protect shared resources

# Using a ThreadPoolExecutor
def task(n: int) -> str:
    time.sleep(n)
    return f"Task {n} completed"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

# Tip: ThreadPoolExecutor is a higher-level interface for managing threads

# 2. Multiprocessing

def process_worker(num: int) -> int:
    return num * num

if __name__ == '__main__':
    # Using Pool for parallel processing
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(process_worker, range(10))
        print("Pool results:", results)

    # Using Process class
    def info(title: str) -> None:
        print(title)
        print('module name:', __name__)
        print('parent process:', multiprocessing.parent_process())
        print('process id:', multiprocessing.current_process().pid)

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=info, args=(f'Process {i}',))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Sharing data between processes
    def f(n: multiprocessing.Value, a: multiprocessing.Array) -> None:
        n.value = 3.14159265359
        for i in range(len(a)):
            a[i] = -a[i]

    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

# Tip: Use multiprocessing for CPU-bound tasks to bypass the GIL

# 3. Async Programming

async def say_after(delay: float, what: str) -> None:
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# Running the event loop
asyncio.run(main())

# Concurrent execution of tasks
async def main_concurrent():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_concurrent())

# Tip: Use asyncio for I/O-bound concurrent programming

# Asynchronous context managers
class AsyncContextManager:
    async def __aenter__(self):
        print("Entering the context")
        await asyncio.sleep(1)
        return "Context Value"

    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting the context")
        await asyncio.sleep(1)

async def use_context_manager():
    async with AsyncContextManager() as value:
        print(f"Inside the context with value: {value}")

asyncio.run(use_context_manager())

# Tip: Use async context managers for asynchronous resource management

# Asynchronous iteration
class AsyncIterator:
    def __init__(self, stop: int):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1)
            self.current += 1
            return self.current - 1
        else:
            raise StopAsyncIteration

async def use_async_iterator():
    async for num in AsyncIterator(5):
        print(num, end=' ')
    print()

asyncio.run(use_async_iterator())

# Tip: Use async iterators for asynchronous sequences

# 4. Combining Threading and Multiprocessing

def cpu_bound(number: int) -> int:
    return sum(i * i for i in range(number))

def find_sums(numbers: List[int]) -> List[int]:
    with multiprocessing.Pool() as pool:
        return pool.map(cpu_bound, numbers)

def main():
    numbers = [10000000 + x for x in range(20)]
    
    start_time = time.time()
    sums = find_sums(numbers)
    end_time = time.time()
    
    print(f"Sum of sums: {sum(sums)}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    main()

# Tip: Use multiprocessing for CPU-bound tasks and threading for I/O-bound tasks

# 5. Advanced Multiprocessing Techniques

# Inter-process communication using Queue
def producer(queue: multiprocessing.Queue) -> None:
    for i in range(10):
        queue.put(i)
        time.sleep(0.1)
    queue.put(None)  # Sentinel value to signal the end

def consumer(queue: multiprocessing.Queue) -> None:
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")

if __name__ == '__main__':
    q = multiprocessing.Queue()
    prod_proc = multiprocessing.Process(target=producer, args=(q,))
    cons_proc = multiprocessing.Process(target=consumer, args=(q,))
    
    prod_proc.start()
    cons_proc.start()
    
    prod_proc.join()
    cons_proc.join()

# Tip: Use Queue for thread-safe communication between processes

# Using Pipes for bi-directional communication
def ping(conn):
    conn.send('Ping')
    print(f"Ping received: {conn.recv()}")

def pong(conn):
    print(f"Pong received: {conn.recv()}")
    conn.send('Pong')

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    
    p1 = multiprocessing.Process(target=ping, args=(parent_conn,))
    p2 = multiprocessing.Process(target=pong, args=(child_conn,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

# Tip: Use Pipes for efficient bi-directional communication between two processes

# 6. Advanced Asyncio Techniques

# Asynchronous generators
async def async_range(start: int, stop: int, step: int = 1):
    for i in range(start, stop, step):
        await asyncio.sleep(0.1)
        yield i

async def use_async_generator():
    async for i in async_range(0, 5):
        print(i, end=' ')
    print()

asyncio.run(use_async_generator())

# Tip: Use asynchronous generators for producing asynchronous sequences of values

# Handling cancellation
async def cancelable_operation():
    try:
        while True:
            print("Operation in progress...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Operation was cancelled")
        raise

async def main_cancellation():
    task = asyncio.create_task(cancelable_operation())
    await asyncio.sleep(3)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Main: operation was cancelled")

asyncio.run(main_cancellation())

# Tip: Always handle cancellation in your coroutines for graceful shutdown

# 7. Concurrent.Futures for Easy Parallelism

def cpu_bound_task(n: int) -> int:
    return sum(i * i for i in range(n))

# Using ProcessPoolExecutor
with concurrent.futures.ProcessPoolExecutor() as executor:
    numbers = [10000000 + x for x in range(20)]
    results = list(executor.map(cpu_bound_task, numbers))
    print(f"Sum of results: {sum(results)}")

# Tip: Use ProcessPoolExecutor for easy parallelism of CPU-bound tasks

# 8. Best Practices and Tips

# 1. Use threading for I/O-bound tasks and multiprocessing for CPU-bound tasks.
# 2. Always use proper synchronization (locks, queues, etc.) when sharing resources between threads or processes.
# 3. Be aware of the Global Interpreter Lock (GIL) in CPython, which limits true parallelism in threading.
# 4. Use asyncio for I/O-bound concurrent programming, especially for network operations.
# 5. Prefer higher-level abstractions like ThreadPoolExecutor and ProcessPoolExecutor when possible.
# 6. Be cautious with shared state in multithreading; consider using thread-local storage when appropriate.
# 7. Handle cancellation and exceptions properly in asyncio coroutines.
# 8. Use multiprocessing.Queue or Pipe for inter-process communication.
# 9. Be aware of the overhead of creating processes; reuse them when possible using process pools.
# 10. Profile your concurrent code to ensure it's actually providing performance benefits.
# 11. Use async context managers and async iterators for more idiomatic asyncio code.
# 12. Consider using asyncio.gather() for running multiple coroutines concurrently.
# 13. Be mindful of potential deadlocks when using multiple locks.
# 14. Use concurrent.futures for simple parallelism tasks.
# 15. Always join threads and processes to prevent zombie processes and ensure proper cleanup.

# This concludes the enhanced detailed Python Cheat Sheet for Concurrency and Parallelism