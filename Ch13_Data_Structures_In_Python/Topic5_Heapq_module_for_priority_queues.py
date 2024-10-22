# Data Structures in Python - Heapq module for priority queues - in the Python Programming Language
# =============================================================================================

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

import heapq
import time
import random
from typing import Any, List, Tuple, TypeVar, Generic
import unittest
import asyncio

T = TypeVar('T')

# 1. Overview and Historical Context
# ----------------------------------
# The heapq module in Python provides an implementation of the heap queue algorithm,
# also known as the priority queue algorithm. A heap is a specialized tree-based
# data structure that satisfies the heap property: in a max heap, for any given node I,
# the value of I is greater than or equal to the values of its children, whereas in a
# min heap, the value of I is less than or equal to the values of its children.

# Historical context:
# - The concept of a heap was introduced by J. W. J. Williams in 1964 as a data structure for heapsort.
# - The heapq module was introduced in Python 2.3 (2003) to provide a high-performance implementation of priority queues.
# - It has been continuously improved and optimized in subsequent Python versions.

# Significance:
# - Priority queues are essential in many algorithms, such as Dijkstra's algorithm for finding shortest paths in graphs.
# - They are used in operating systems for task scheduling and in data compression algorithms like Huffman coding.
# - The heapq module provides an efficient, easy-to-use implementation of priority queues in Python.

# Common use cases:
# - Task scheduling in operating systems and job queue management
# - Implementing efficient sorting algorithms like heapsort
# - Managing a collection of elements where the smallest (or largest) element needs to be retrieved quickly

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

def heapq_basics():
    """Demonstrate basic usage of heapq module."""
    # Creating a heap
    heap = []
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    for item in data:
        heapq.heappush(heap, item)
    
    print("Original data:", data)
    print("Heap:", heap)
    
    # Popping elements from the heap
    sorted_data = []
    while heap:
        sorted_data.append(heapq.heappop(heap))
    
    print("Sorted data:", sorted_data)

def heap_operations():
    """Demonstrate various heap operations."""
    heap = []
    
    # heappush: Add an element to the heap
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 7)
    print("After pushes:", heap)
    
    # heappop: Remove and return the smallest element
    smallest = heapq.heappop(heap)
    print("Popped smallest:", smallest)
    print("After pop:", heap)
    
    # heapify: Transform a list into a heap in-place
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    heapq.heapify(data)
    print("After heapify:", data)
    
    # heapreplace: Pop and return smallest, then push new item
    replaced = heapq.heapreplace(heap, 6)
    print("Replaced:", replaced)
    print("After replace:", heap)
    
    # nlargest and nsmallest: Return n largest or smallest elements
    numbers = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print("3 largest:", heapq.nlargest(3, numbers))
    print("3 smallest:", heapq.nsmallest(3, numbers))

class PriorityQueue(Generic[T]):
    """A priority queue implementation using heapq."""
    
    def __init__(self):
        self._queue: List[Tuple[int, int, T]] = []
        self._index = 0
    
    def push(self, item: T, priority: int):
        """Add an item to the queue with a given priority."""
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self) -> T:
        """Remove and return the item with the highest priority (lowest number)."""
        return heapq.heappop(self._queue)[-1]
    
    def peek(self) -> T:
        """Return the item with the highest priority without removing it."""
        return self._queue[0][-1]
    
    def __len__(self) -> int:
        return len(self._queue)

def demonstrate_priority_queue():
    """Demonstrate the usage of the PriorityQueue class."""
    pq = PriorityQueue()
    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)
    
    print("Priority Queue demonstration:")
    print("Next task:", pq.peek())
    
    while pq:
        next_task = pq.pop()
        print(f"Processing: {next_task}")

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------

# Best Practices:
# 1. Use tuple comparison for complex priorities: (priority, data)
# 2. Use the heapq module for simple priority queues, implement a class for more complex scenarios
# 3. Consider using a custom __lt__ method for complex objects in heaps
# 4. Use heapq.heapify() to convert an existing list to a heap in-place

# Common Pitfalls:
# 1. Forgetting that heapq implements a min-heap (use negation for max-heap behavior)
# 2. Modifying the heap directly instead of using heapq functions
# 3. Not handling duplicate priorities correctly
# 4. Assuming that the heap is always fully sorted (only the top element is guaranteed to be the smallest)

# Advanced Tips:
# 1. Use the 'key' parameter in nlargest and nsmallest for custom sorting
# 2. Implement a remove() method for priority queues using the index technique
# 3. Use __slots__ for memory optimization in priority queue implementations
# 4. Utilize the merge() function for efficient merging of multiple sorted iterables

def advanced_heap_usage():
    """Demonstrate advanced usage of heapq."""
    
    # Using key function with nlargest
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    longest_words = heapq.nlargest(3, words, key=len)
    print("3 longest words:", longest_words)
    
    # Merging multiple sorted iterables
    iter1 = iter([1, 3, 5, 7, 9])
    iter2 = iter([2, 4, 6, 8, 10])
    merged = list(heapq.merge(iter1, iter2))
    print("Merged iterables:", merged)

class OptimizedPriorityQueue(Generic[T]):
    """A memory-optimized priority queue using __slots__."""
    
    __slots__ = ['_queue', '_index']
    
    def __init__(self):
        self._queue: List[Tuple[int, int, T]] = []
        self._index = 0
    
    def push(self, item: T, priority: int):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self) -> T:
        return heapq.heappop(self._queue)[-1]

def demonstrate_optimized_priority_queue():
    """Demonstrate the usage of the OptimizedPriorityQueue class."""
    opq = OptimizedPriorityQueue()
    opq.push("Task 1", 3)
    opq.push("Task 2", 1)
    opq.push("Task 3", 2)
    
    print("Optimized Priority Queue demonstration:")
    while opq._queue:  # Note: Accessing a private attribute for demonstration
        next_task = opq.pop()
        print(f"Processing: {next_task}")

# 4. Integration and Real-World Applications
# ------------------------------------------

def dijkstra_shortest_path(graph: dict, start: str, end: str) -> Tuple[float, List[str]]:
    """
    Implement Dijkstra's algorithm for finding the shortest path in a graph.
    
    Args:
    graph: A dictionary representing the graph. Each key is a node, and the value is a dictionary
           of neighboring nodes and their distances.
    start: The starting node.
    end: The target node.
    
    Returns:
    A tuple containing the shortest distance and the path as a list of nodes.
    """
    pq = [(0, start, [])]
    visited = set()
    
    while pq:
        (cost, node, path) = heapq.heappop(pq)
        
        if node not in visited:
            visited.add(node)
            path = path + [node]
            
            if node == end:
                return (cost, path)
            
            for neighbor, distance in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + distance, neighbor, path))
    
    return float('inf'), []

def demonstrate_dijkstra():
    """Demonstrate Dijkstra's algorithm using a priority queue."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    
    start, end = 'A', 'E'
    distance, path = dijkstra_shortest_path(graph, start, end)
    
    print(f"Shortest path from {start} to {end}:")
    print(f"Distance: {distance}")
    print(f"Path: {' -> '.join(path)}")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------

class ArrayHeap(Generic[T]):
    """
    A heap implementation using an array, demonstrating the underlying concept of heapq.
    This implementation uses 0-based indexing.
    """
    
    def __init__(self):
        self.heap: List[T] = []
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def left_child(self, i: int) -> int:
        return 2 * i + 1
    
    def right_child(self, i: int) -> int:
        return 2 * i + 2
    
    def swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def push(self, item: T):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)
    
    def pop(self) -> T:
        if not self.heap:
            raise IndexError("pop from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_item
    
    def _sift_up(self, i: int):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def _sift_down(self, i: int):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)

def demonstrate_array_heap():
    """Demonstrate the usage of the ArrayHeap class."""
    heap = ArrayHeap()
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    print("ArrayHeap demonstration:")
    for item in data:
        heap.push(item)
    
    print("Sorted data:")
    while heap.heap:
        print(heap.pop(), end=' ')
    print()

# Asynchronous Priority Queue
class AsyncPriorityQueue(Generic[T]):
    """An asynchronous priority queue implementation."""
    
    def __init__(self):
        self._queue: List[Tuple[int, int, T]] = []
        self._index = 0
        self._not_empty = asyncio.Condition()
    
    async def push(self, item: T, priority: int):
        async with self._not_empty:
            heapq.heappush(self._queue, (priority, self._index, item))
            self._index += 1
            self._not_empty.notify()
    
    async def pop(self) -> T:
        async with self._not_empty:
            while not self._queue:
                await self._not_empty.wait()
            return heapq.heappop(self._queue)[-1]

async def producer(queue: AsyncPriorityQueue, name: str):
    for i in range(5):
        priority = random.randint(1, 10)
        await queue.push(f"Task {i} from {name}", priority)
        print(f"{name} produced Task {i} with priority {priority}")
        await asyncio.sleep(random.random())

async def consumer(queue: AsyncPriorityQueue, name: str):
    for _ in range(10):
        item = await queue.pop()
        print(f"{name} consumed {item}")
        await asyncio.sleep(random.random())

async def run_async_priority_queue():
    queue = AsyncPriorityQueue()
    await asyncio.gather(
        producer(queue, "Producer 1"),
        producer(queue, "Producer 2"),
        consumer(queue, "Consumer")
    )

def demonstrate_async_priority_queue():
    """Demonstrate the usage of the AsyncPriorityQueue class."""
    print("Asynchronous Priority Queue demonstration:")
    asyncio.run(run_async_priority_queue())

# 6. FAQs and Troubleshooting
# ---------------------------

def faqs_and_troubleshooting():
    print("Q: How do I implement a max-heap using heapq?")
    print("A: heapq implements a min-heap by default. To create a max-heap, you can negate the values when pushing and popping:")
    
    def demonstrate_max_heap():
        max_heap = []
        for value in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
            heapq.heappush(max_heap, -value)
        
        max_values = []
        while max_heap:
            max_values.append(-heapq.heappop(max_heap))
        print("Max heap values (descending order):", max_values)
    
    demonstrate_max_heap()
    
    print("\nQ: How can I update the priority of an item in the heap?")
    print("A: heapq doesn't provide a direct method to update priorities. One approach is to add a new entry and mark the old one as removed:")
    
    def demonstrate_priority_update():
        class PriorityQueue:
            REMOVED = '<removed-task>'  # placeholder for a removed task
            
            def __init__(self):
                self.pq = []
                self.entry_finder = {}
                self.counter = 0
            
            def add_task(self, task, priority=0):
                if task in self.entry_finder:
                    self.remove_task(task)
                count = self.counter
                entry = [priority, count, task]
                self.entry_finder[task] = entry
                heapq.heappush(self.pq, entry)
                self.counter += 1
            
            def remove_task(self, task):
                entry = self.entry_finder.pop(task)
                entry[-1] = self.REMOVED
            
            def pop_task(self):
                while self.pq:
                    priority, count, task = heapq.heappop(self.pq)
                    if task is not self.REMOVED:
                        del self.entry_finder[task]
                        return task
                raise KeyError('pop from an empty priority queue')
        
        pq = PriorityQueue()
        pq.add_task('task1', 5)
        pq.add_task('task2', 3)
        pq.add_task('task3', 1)
        print("Original order:")
        print(pq.pop_task())
        print(pq.pop_task())
        
        pq.add_task('task1', 5)
        pq.add_task('task2', 3)
        pq.add_task('task3', 1)
        pq.add_task('task2', 0)  # Update priority
        print("\nAfter updating task2 priority:")
        print(pq.pop_task())
        print(pq.pop_task())
    
    demonstrate_priority_update()
    
    print("\nQ: Is the heapq module thread-safe?")
    print("A: No, the heapq module itself is not thread-safe. If you need thread-safety, consider using the queue.PriorityQueue class, which is a thread-safe wrapper around heapq.")

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

def recommended_resources():
    print("Recommended Tools, Libraries, and Resources:")
    print("1. Official Python heapq documentation: https://docs.python.org/3/library/heapq.html")
    print("2. 'Python Cookbook' by David Beazley and Brian K. Jones - Chapter 1.5 on Priority Queues")
    print("3. 'Data Structures and Algorithms in Python' by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser")
    print("4. queue.PriorityQueue for thread-safe priority queues: https://docs.python.org/3/library/queue.html#queue.PriorityQueue")
    print("5. 'Problem Solving with Algorithms and Data Structures using Python' by Bradley N. Miller and David L. Ranum")
    print("6. PyPi package 'heapdict' for a dict-like heap: https://pypi.org/project/HeapDict/")
    print("7. 'Fluent Python' by Luciano Ramalho - for advanced Python concepts including data structures")

# 8. Performance Analysis and Optimization
# ----------------------------------------

def performance_analysis():
    print("Performance Analysis of heapq operations:")
    
    def time_operation(operation, *args):
        start_time = time.time()
        operation(*args)
        end_time = time.time()
        return end_time - start_time
    
    # Test push operation
    heap = []
    push_times = []
    for i in range(1000000):
        push_times.append(time_operation(heapq.heappush, heap, random.random()))
    
    # Test pop operation
    pop_times = []
    while heap:
        pop_times.append(time_operation(heapq.heappop, heap))
    
    print(f"Average push time: {sum(push_times) / len(push_times):.8f} seconds")
    print(f"Average pop time: {sum(pop_times) / len(pop_times):.8f} seconds")
    
    # Compare with sorting
    unsorted = [random.random() for _ in range(1000000)]
    heap_sort_time = time_operation(lambda arr: [heapq.heappop(arr) for _ in range(len(arr))], unsorted.copy())
    python_sort_time = time_operation(sorted, unsorted)
    
    print(f"Heapsort time: {heap_sort_time:.4f} seconds")
    print(f"Python's Timsort time: {python_sort_time:.4f} seconds")

def optimize_heap_operations():
    print("Optimization strategies for heap operations:")
    print("1. Use heapq.heapify() for initial heap creation instead of repeated heappush():")
    
    def create_heap_push(data):
        heap = []
        for item in data:
            heapq.heappush(heap, item)
        return heap
    
    def create_heap_heapify(data):
        heap = data.copy()
        heapq.heapify(heap)
        return heap
    
    data = [random.random() for _ in range(1000000)]
    
    push_time = time_operation(create_heap_push, data)
    heapify_time = time_operation(create_heap_heapify, data)
    
    print(f"  Time to create heap using push: {push_time:.4f} seconds")
    print(f"  Time to create heap using heapify: {heapify_time:.4f} seconds")
    
    print("\n2. Use heapq.merge() for combining multiple sorted iterables:")
    
    def merge_sort(iterables):
        return sorted(itertools.chain(*iterables))
    
    def merge_heapq(iterables):
        return list(heapq.merge(*iterables))
    
    iterables = [sorted([random.random() for _ in range(10000)]) for _ in range(100)]
    
    sort_time = time_operation(merge_sort, iterables)
    merge_time = time_operation(merge_heapq, iterables)
    
    print(f"  Time to merge using sort: {sort_time:.4f} seconds")
    print(f"  Time to merge using heapq.merge: {merge_time:.4f} seconds")

# 9. How to Contribute
# --------------------

def how_to_contribute():
    print("How to Contribute to this Note Sheet:")
    print("1. Fork the repository containing this file.")
    print("2. Make your changes or additions.")
    print("3. Ensure all code examples are correct and follow the established style.")
    print("4. Add comments explaining new concepts or functions.")
    print("5. Update the Table of Contents if necessary.")
    print("6. Submit a pull request with a clear description of your changes.")
    print("\nGuidelines for contributions:")
    print("- Maintain the current format and style.")
    print("- Provide working code examples for new concepts.")
    print("- Include performance considerations for new functions.")
    print("- Add relevant references or citations for advanced topics.")

# Main function to demonstrate all concepts
def main():
    print("Demonstrating Heapq module for priority queues in Python")
    heapq_basics()
    heap_operations()
    demonstrate_priority_queue()
    advanced_heap_usage()
    demonstrate_optimized_priority_queue()
    demonstrate_dijkstra()
    demonstrate_array_heap()
    demonstrate_async_priority_queue()
    faqs_and_troubleshooting()
    recommended_resources()
    performance_analysis()
    optimize_heap_operations()
    how_to_contribute()

if __name__ == "__main__":
    main()