# Data Structures in Python - Stacks, Queues, and Deques - in the Python Programming Language
# =======================================================================================

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

import time
import unittest
from typing import Any, List, Tuple
from collections import deque
from queue import Queue, LifoQueue
import asyncio

# 1. Overview and Historical Context
# ----------------------------------
# Stacks, queues, and deques are fundamental data structures in computer science and programming.
# They provide different ways of organizing and accessing data, each with its own characteristics and use cases.

# Historical context:
# - These data structures have been part of computer science since its early days.
# - Stacks and queues were first described in the 1940s and 1950s.
# - Deques (double-ended queues) were introduced later as a generalization of stacks and queues.
# - In Python, these structures can be implemented using built-in lists, the collections.deque class (introduced in Python 2.4),
#   or the queue module (introduced in Python 1.4).

# Significance:
# - Stacks: LIFO (Last-In-First-Out) structure, crucial for function call management, expression evaluation, and backtracking algorithms.
# - Queues: FIFO (First-In-First-Out) structure, essential for task scheduling, breadth-first search, and buffer management.
# - Deques: Double-ended queues, combining features of both stacks and queues, useful for sliding window problems and certain algorithm implementations.

# Common use cases:
# - Stacks: Function call stack, undo mechanisms, syntax parsing in compilers.
# - Queues: Task scheduling in operating systems, breadth-first search in graph algorithms, print job spooling.
# - Deques: Implementing both stacks and queues, palindrome checking, sliding window problems in algorithms.

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from an empty stack")

    def peek(self) -> Any:
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from an empty stack")

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

def demonstrate_stack():
    stack = Stack()
    print("Push 1, 2, 3 onto the stack")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack size: {stack.size()}")
    print(f"Top item: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"New top item: {stack.peek()}")
    print(f"Is stack empty? {stack.is_empty()}")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item: Any) -> None:
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self) -> Any:
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from an empty queue")

    def front(self) -> Any:
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("front from an empty queue")

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)

def demonstrate_queue():
    queue = Queue()
    print("Enqueue 1, 2, 3 into the queue")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue size: {queue.size()}")
    print(f"Front item: {queue.front()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"New front item: {queue.front()}")
    print(f"Is queue empty? {queue.is_empty()}")

class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item: Any) -> None:
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def add_rear(self, item: Any) -> None:
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def remove_front(self) -> Any:
        """Remove and return the front item from the deque."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("remove_front from an empty deque")

    def remove_rear(self) -> Any:
        """Remove and return the rear item from the deque."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("remove_rear from an empty deque")

    def front(self) -> Any:
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("front from an empty deque")

    def rear(self) -> Any:
        """Return the rear item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("rear from an empty deque")

    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items in the deque."""
        return len(self.items)

def demonstrate_deque():
    deque = Deque()
    print("Add 1, 2 to front and 3, 4 to rear of the deque")
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(f"Deque size: {deque.size()}")
    print(f"Front item: {deque.front()}")
    print(f"Rear item: {deque.rear()}")
    print(f"Remove front: {deque.remove_front()}")
    print(f"Remove rear: {deque.remove_rear()}")
    print(f"New front item: {deque.front()}")
    print(f"New rear item: {deque.rear()}")
    print(f"Is deque empty? {deque.is_empty()}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Choose the right data structure for your use case (stack, queue, or deque).
# 2. Use built-in implementations (list, collections.deque, queue.Queue) for better performance when possible.
# 3. Implement proper error handling for empty data structure operations.
# 4. Use type hints to improve code readability and catch potential type-related errors.

# Common Pitfalls:
# 1. Using a list as a queue (inefficient due to O(n) time complexity for dequeue operation).
# 2. Forgetting to handle empty data structure cases, leading to IndexError.
# 3. Misusing deque methods (e.g., using pop() instead of popleft() for queue-like behavior).
# 4. Not considering thread-safety in multi-threaded applications.

# Advanced Tips:
# 1. Use collections.deque for efficient implementation of both stacks and queues.
# 2. Implement custom iterators for your data structures to enable for-loop traversal.
# 3. Consider using the queue module for thread-safe implementations in multi-threaded scenarios.
# 4. Optimize memory usage by using __slots__ for large numbers of instances.

def demonstrate_advanced_usage():
    # Using collections.deque for efficient stack and queue operations
    stack_deque = deque()
    stack_deque.append(1)  # push
    stack_deque.append(2)
    print(f"Stack using deque: {stack_deque}")
    print(f"Pop from stack: {stack_deque.pop()}")

    queue_deque = deque()
    queue_deque.append(1)  # enqueue
    queue_deque.append(2)
    print(f"Queue using deque: {queue_deque}")
    print(f"Dequeue: {queue_deque.popleft()}")

    # Using queue module for thread-safe operations
    stack_thread_safe = LifoQueue()
    stack_thread_safe.put(1)
    stack_thread_safe.put(2)
    print(f"Thread-safe stack size: {stack_thread_safe.qsize()}")
    print(f"Pop from thread-safe stack: {stack_thread_safe.get()}")

    queue_thread_safe = Queue()
    queue_thread_safe.put(1)
    queue_thread_safe.put(2)
    print(f"Thread-safe queue size: {queue_thread_safe.qsize()}")
    print(f"Dequeue from thread-safe queue: {queue_thread_safe.get()}")

# 4. Integration and Real-World Applications
# ------------------------------------------

# Example: Using a stack to check for balanced parentheses
def is_balanced_parentheses(expression: str) -> bool:
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    pairs = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()

# Example: Using a queue for breadth-first search in a graph
def bfs(graph: dict, start: Any) -> List[Any]:
    visited = set()
    queue = Queue()
    queue.enqueue(start)
    visited.add(start)
    result = []

    while not queue.is_empty():
        vertex = queue.dequeue()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    
    return result

# Example: Using a deque for palindrome checking
def is_palindrome(s: str) -> bool:
    char_deque = Deque()
    for char in s.lower():
        if char.isalnum():
            char_deque.add_rear(char)
    
    while char_deque.size() > 1:
        if char_deque.remove_front() != char_deque.remove_rear():
            return False
    
    return True

def demonstrate_real_world_applications():
    # Balanced parentheses
    print(f"Is '((()))' balanced? {is_balanced_parentheses('((()))')}")
    print(f"Is '(()' balanced? {is_balanced_parentheses('(()')}")

    # BFS in a graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print(f"BFS traversal: {bfs(graph, 'A')}")

    # Palindrome checking
    print(f"Is 'A man, a plan, a canal: Panama' a palindrome? {is_palindrome('A man, a plan, a canal: Panama')}")
    print(f"Is 'race a car' a palindrome? {is_palindrome('race a car')}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

# Priority Queues
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item: Any, priority: int):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self) -> Any:
        return heapq.heappop(self._queue)[-1]

# Concurrent Deque
from concurrent.collections import ConcurrentDeque

# Example of using asyncio with queues
async def producer(queue: asyncio.Queue):
    for i in range(5):
        await queue.put(i)
        print(f"Produced: {i}")
        await asyncio.sleep(1)

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        queue.task_done()

async def main_async():
    queue = asyncio.Queue()
    prod = asyncio.create_task(producer(queue))
    cons = asyncio.create_task(consumer(queue))
    await asyncio.gather(prod)
    await queue.join()
    cons.cancel()

def demonstrate_advanced_concepts():
    # Priority Queue
    pq = PriorityQueue()
    pq.push('task1', 2)
    pq.push('task2', 1)
    pq.push('task3', 3)
    print(f"Highest priority task: {pq.pop()}")

    # Concurrent Deque
    cd = ConcurrentDeque()
    cd.append(1)
    cd.appendleft(2)
    print(f"Concurrent Deque: {cd}")

    # Asyncio with queues
    asyncio.run(main_async())

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    print("Q: When should I use a stack vs a queue?")
    print("A: Use a stack for LIFO (Last-In-First-Out) operations, like undo functionality or depth-first search.")
    print("   Use a queue for FIFO (First-In-First-Out) operations, like task scheduling or breadth-first search.")

    print("\nQ: How can I implement a thread-safe stack or queue?")
    print("A: Use the queue.LifoQueue for a thread-safe stack or queue.Queue for a thread-safe queue.")

    print("\nQ: What's the difference between collections.deque and the custom Deque implementation?")
    print("\nQ: What's the difference between collections.deque and the custom Deque implementation?")
    print("A: collections.deque is more efficient and provides thread-safe operations. It's implemented in C for better performance.")

    print("\nQ: How can I reverse a string using a stack?")
    print("A: Here's an example:")
    def reverse_string(s: str) -> str:
        stack = Stack()
        for char in s:
            stack.push(char)
        return ''.join(stack.pop() for _ in range(stack.size()))
    
    original = "Hello, World!"
    reversed_str = reverse_string(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. collections.deque: Efficient implementation of deques
# 2. queue module: Provides thread-safe Queue, LifoQueue (stack), and PriorityQueue
# 3. heapq module: Implementation of priority queues using binary heaps
# 4. asyncio.Queue: Asynchronous queue for use with asyncio

# Resources:
# - "Data Structures and Algorithms in Python" by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
# - "Problem Solving with Algorithms and Data Structures using Python" by Bradley N. Miller and David L. Ranum
# - Python official documentation: https://docs.python.org/3/tutorial/datastructures.html
# - Real Python's guide on stacks and queues: https://realpython.com/how-to-implement-python-stack/
# - GeeksforGeeks Python Data Structures: https://www.geeksforgeeks.org/python-data-structures/

# 8. Performance Analysis and Optimization
# ----------------------------------------

import timeit

def performance_comparison():
    def test_stack_list():
        stack = []
        for i in range(10000):
            stack.append(i)
        while stack:
            stack.pop()

    def test_stack_deque():
        stack = deque()
        for i in range(10000):
            stack.append(i)
        while stack:
            stack.pop()

    def test_queue_list():
        queue = []
        for i in range(10000):
            queue.append(i)
        while queue:
            queue.pop(0)

    def test_queue_deque():
        queue = deque()
        for i in range(10000):
            queue.append(i)
        while queue:
            queue.popleft()

    print("Performance comparison:")
    print(f"Stack using list: {timeit.timeit(test_stack_list, number=1000):.6f} seconds")
    print(f"Stack using deque: {timeit.timeit(test_stack_deque, number=1000):.6f} seconds")
    print(f"Queue using list: {timeit.timeit(test_queue_list, number=1000):.6f} seconds")
    print(f"Queue using deque: {timeit.timeit(test_queue_deque, number=1000):.6f} seconds")

# Memory optimization using __slots__
class OptimizedStack:
    __slots__ = ['items']

    def __init__(self):
        self.items = []

    # ... (rest of the methods remain the same as the Stack class)

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from an empty stack")

    def peek(self) -> Any:
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from an empty stack")

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

def memory_usage_comparison():
    import sys

    regular_stack = Stack()
    optimized_stack = OptimizedStack()

    for i in range(1000000):
        regular_stack.push(i)
        optimized_stack.push(i)

    print("Memory usage comparison:")
    print(f"Regular Stack: {sys.getsizeof(regular_stack) + sys.getsizeof(regular_stack.items):,} bytes")
    print(f"Optimized Stack: {sys.getsizeof(optimized_stack) + sys.getsizeof(optimized_stack.items):,} bytes")

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

# Example of a unit test for the Stack class
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

def main():
    print("Demonstrating Stacks, Queues, and Deques in Python")
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_deque()
    demonstrate_advanced_usage()
    demonstrate_real_world_applications()
    demonstrate_advanced_concepts()
    faqs_and_troubleshooting()
    performance_comparison()
    memory_usage_comparison()

    # Run unit tests
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main()