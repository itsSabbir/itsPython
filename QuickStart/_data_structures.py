#=================================================================================
# Data Structures: Basic Data Structures - Arrays
#=================================================================================

# In Python, an array is a data structure that can hold a fixed number of elements of the same type.
# However, Python does not have a native array data type like some other languages (e.g., C, Java).
# Instead, lists are commonly used to implement array-like structures. For numeric data,
# the 'array' module or NumPy arrays are also options.

# Example: Using a list as an array
array_example = [10, 20, 30, 40, 50]  # A simple list to represent an array
print("Array Elements:", array_example)  # Outputs the elements of the array

# Best Practice: Prefer using lists for dynamic sizing; they automatically handle resizing.
# However, for large datasets, consider using the 'array' module for improved performance.
# Python lists have O(1) average time complexity for access and append operations,
# but insertion at arbitrary positions is O(n) due to the need for shifting elements.

# Accessing Elements
# Elements in an array (or list) can be accessed using their index.
# Python uses zero-based indexing, meaning the first element is at index 0.
first_element = array_example[0]  # Accessing the first element
print("First Element:", first_element)  # Outputs: 10

# Modifying Elements
# Elements can be modified by assigning a new value to a specific index.
array_example[2] = 35  # Changing the third element from 30 to 35
print("Modified Array Elements:", array_example)  # Outputs: [10, 20, 35, 40, 50]

# Iterating Through Arrays
# Iteration can be done using a simple for loop, which is a common practice to access 
# or modify elements in the array.
print("Iterating through the array:")
for index, value in enumerate(array_example):  # Using enumerate to get index and value
    print(f"Index {index}: {value}")

# Advanced Tip: When performance matters, prefer using the 'array' module for homogeneous data types.
# The 'array' module provides a space-efficient way to store arrays of basic numeric types.
import array

# Example of using the array module
numeric_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates the type is integer
print("Numeric Array Elements:", numeric_array.tolist())  # Convert to list for printing

# Operations on Arrays
# Common operations include finding the length, appending elements, and removing elements.

# Length of the array
length_of_array = len(array_example)  # Getting the number of elements in the list
print("Length of Array:", length_of_array)  # Outputs: 5

# Appending Elements
array_example.append(60)  # Adding a new element at the end
print("Array after Append:", array_example)  # Outputs: [10, 20, 35, 40, 50, 60]

# Removing Elements
array_example.remove(20)  # Removing the element with value 20
print("Array after Removal:", array_example)  # Outputs: [10, 35, 40, 50, 60]

# Potential Pitfalls:
# - Be cautious with index out of bounds errors; accessing an index that doesn't exist will raise an IndexError.
# - When working with large datasets, consider the time complexity of operations; for example, list insertions can be O(n).
# - Modifying elements in lists is efficient, but removing elements can be costly if they are not at the end of the list.

# Use Cases:
# - Arrays are widely used in scenarios like image processing (e.g., pixel data),
#   numerical computations (e.g., mathematical operations), and storing fixed-size collections of data.

# Run Time Analysis:
# - Accessing an element: O(1) - Direct access via index is very efficient.
# - Inserting an element at the end: O(1) amortized time, as Python lists dynamically resize.
# - Inserting/removing elements in the middle: O(n) due to the need to shift elements.
# - Searching for an element: O(n) in the worst case if the list is unsorted.

# Advanced Consideration:
# If using large datasets or requiring advanced operations (like multi-dimensional arrays), consider using NumPy arrays.
# NumPy offers a rich set of operations and optimizations, particularly for numerical data.

#=================================================================================
# Data Structures: Basic Data Structures - Linked Lists
#=================================================================================

# In this section, we focus on linked lists, a fundamental data structure 
# that allows for efficient insertion and deletion operations. Linked lists are 
# often preferred over arrays when the size of the data structure is not known 
# ahead of time or when frequent resizing is required.

# Linked Lists
# A linked list consists of nodes, where each node contains a data value and a 
# reference (or pointer) to the next node in the sequence. This enables efficient 
# dynamic memory allocation.

# Singly Linked List
# In a singly linked list, each node points to the next node and has no reference 
# to the previous node. This makes traversing the list straightforward, but 
# backward traversal is not possible.
class Node:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.next = None  # Pointer to the next node, initially set to None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, value):
        # Add a new node with the specified value at the end of the list
        new_node = Node(value)  # Create a new node
        if not self.head:  # If the list is empty, set new_node as the head
            self.head = new_node
            return
        last_node = self.head  # Start at the head of the list
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link the new node at the end

# Example usage of SinglyLinkedList
singly_linked_list = SinglyLinkedList()
singly_linked_list.append(10)
singly_linked_list.append(20)
singly_linked_list.append(30)

# Print elements of the singly linked list
current = singly_linked_list.head
while current:  # Traverse through the list and print values
    print("Singly Linked List Element:", current.value)
    current = current.next  # Move to the next node

# Time Complexity Analysis
# Best case for append: O(1) when adding to the empty list.
# Worst case for append: O(n) when traversing to the end of the list to add the new node.

# Tip: Use singly linked lists for stack or queue implementations 
# where frequent insertions and deletions occur, as they allow for O(1) 
# insertion at the beginning.

# Doubly Linked List
# A doubly linked list has nodes that contain two pointers: one to the next node 
# and another to the previous node. This allows traversal in both directions, 
# making certain operations more efficient.
class DoublyNode:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, value):
        # Add a new node at the end of the doubly linked list
        new_node = DoublyNode(value)  # Create a new node
        if not self.head:  # If the list is empty, set new_node as the head
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link the new node at the end
        new_node.prev = last_node  # Link the new node back to the last node

# Example usage of DoublyLinkedList
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(100)
doubly_linked_list.append(200)
doubly_linked_list.append(300)

# Print elements of the doubly linked list
current = doubly_linked_list.head
while current:  # Traverse through the list and print values
    print("Doubly Linked List Element:", current.value)
    current = current.next

# Time Complexity Analysis
# Best case for append: O(1) when adding to the empty list.
# Worst case for append: O(n) when traversing to the end of the list.

# Advanced Tip: Use doubly linked lists when you need bidirectional traversal, 
# which can improve performance for certain operations like deletion of a node 
# when only a reference to that node is available. Deletion in a doubly linked list 
# can be done in O(1) if you have a pointer to the node.

# Circular Linked List
# In a circular linked list, the last node points back to the first node, forming 
# a circle. This allows for continuous traversal of the list without the need to 
# reset to the head.
class CircularNode:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.next = None  # Pointer to the next node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, value):
        # Add a new node at the end of the circular linked list
        new_node = CircularNode(value)  # Create a new node
        if not self.head:  # If the list is empty, set new_node as the head
            self.head = new_node
            new_node.next = self.head  # Point to itself to create a circular structure
            return
        last_node = self.head
        while last_node.next != self.head:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link the new node at the end
        new_node.next = self.head  # Make it circular

# Example usage of CircularLinkedList
circular_linked_list = CircularLinkedList()
circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)

# Print first 5 elements to demonstrate circular nature
current = circular_linked_list.head
for _ in range(5):  # Limit to 5 to avoid infinite loop
    print("Circular Linked List Element:", current.value)
    current = current.next

# Time Complexity Analysis
# Best case for append: O(1) when adding to the empty list.
# Worst case for append: O(n) when traversing to the end of the list.

# Tip: Circular linked lists are useful in applications where the list needs to 
# be traversed repeatedly, such as in round-robin scheduling or implementing 
# certain types of queues.

# Summary
# Linked lists offer dynamic memory allocation and efficient insertion/deletion 
# but come with trade-offs in terms of memory overhead and cache performance 
# compared to arrays. 
# 
# Runtime Complexity:
# - Singly Linked List:
#   - Append: O(n) in the worst case.
#   - Search: O(n) in the worst case.
#
# - Doubly Linked List:
#   - Append: O(n) in the worst case.
#   - Search: O(n) in the worst case.
#
# - Circular Linked List:
#   - Append: O(n) in the worst case.
#   - Search: O(n) in the worst case.
#
# Understanding when to use each type of linked list is crucial for optimal 
# algorithm design. Look for scenarios with frequent insertions and deletions 
# or unknown sizes when choosing linked lists over arrays. 
# Be mindful of the trade-offs in memory overhead and access speed.


#=================================================================================
# Data Structures: Basic Data Structures, Stacks
#=================================================================================

# In this section, we delve into the basic data structure known as stacks.
# Stacks are critical for many algorithms and applications, particularly in scenarios 
# requiring backtracking or temporary storage of data.

# Stacks
# A stack is a last-in, first-out (LIFO) data structure. 
# This means the last element added to the stack is the first one to be removed. 
# Stacks can be implemented using lists or collections.deque in Python.

# Example 1: Using a list as a stack
stack = []  # Initialize an empty stack using a list

# Push operation: Adding elements to the stack
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
stack.append(3)  # Push 3 onto the stack
print("Stack after pushes:", stack)  # Outputs: [1, 2, 3]

# Pop operation: Removing the top element from the stack
popped_element = stack.pop()  # Pop the top element (3)
print("Popped element:", popped_element)  # Outputs: 3
print("Stack after pop:", stack)  # Outputs: [1, 2]

# Performance Analysis for List-based Stack:
# - Time Complexity for Push: O(1) on average, but can be O(n) if resizing occurs.
# - Time Complexity for Pop: O(1).
# - Worst Case: If the list needs to be resized during push, it can lead to O(n) complexity.
# - Best Case: If there’s no resizing, push and pop operations are O(1).

# Tip: Using a list for stack operations is convenient, but remember that
# lists are dynamic arrays, which can lead to performance overhead due to resizing.
# If you expect many push/pop operations, consider using collections.deque.

# Example 2: Using collections.deque as a stack
from collections import deque

stack_deque = deque()  # Initialize an empty deque to use as a stack

# Push operations using deque
stack_deque.append(4)  # Push 4 onto the stack
stack_deque.append(5)  # Push 5 onto the stack
print("Deque Stack after pushes:", stack_deque)  # Outputs: deque([4, 5])

# Pop operation using deque
popped_from_deque = stack_deque.pop()  # Pop the top element (5)
print("Popped from deque stack:", popped_from_deque)  # Outputs: 5
print("Deque Stack after pop:", stack_deque)  # Outputs: deque([4])

# Performance Analysis for Deque-based Stack:
# - Time Complexity for Push: O(1).
# - Time Complexity for Pop: O(1).
# - Deques are implemented as doubly linked lists, providing consistent O(1) time for 
#   appending and popping from both ends, making them suitable for stack implementations.

# Use Case: Stacks are widely used in algorithms like depth-first search (DFS)
# for trees and graphs, where you need to explore nodes and backtrack when necessary.
# They are also used in undo mechanisms in applications where you may need to revert
# to a previous state.

# Example 3: Implementing a stack with limited capacity
class LimitedStack:
    def __init__(self, capacity):
        self.capacity = capacity  # Set the maximum capacity of the stack
        self.stack = []  # Initialize the stack

    def push(self, value):
        if len(self.stack) >= self.capacity:
            print("Stack is full. Cannot push:", value)  # Handle overflow
            return
        self.stack.append(value)  # Push value onto the stack
        print("Pushed onto stack:", value)

    def pop(self):
        if not self.stack:  # Handle underflow
            print("Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()  # Pop the top element

limited_stack = LimitedStack(3)  # Create a limited stack with capacity of 3
limited_stack.push(1)  # Push 1 onto the stack
limited_stack.push(2)  # Push 2 onto the stack
limited_stack.push(3)  # Push 3 onto the stack
limited_stack.push(4)  # Attempt to push 4 (should fail due to capacity)
print("Current stack:", limited_stack.stack)  # Outputs: [1, 2, 3]

# Popping elements from the limited stack
print("Popped from limited stack:", limited_stack.pop())  # Outputs: 3
print("Current stack after pop:", limited_stack.stack)  # Outputs: [1, 2]

# Advanced Tip: 
# When implementing your own stack, consider the implications of resizing,
# especially in high-performance applications. Deques provide O(1) time complexity 
# for append and pop operations, while lists may have O(n) complexity in some cases 
# due to dynamic resizing. 

# Runtime Analysis for Limited Stack:
# - Time Complexity for Push: O(1) if not full, otherwise returns immediately.
# - Time Complexity for Pop: O(1) if not empty, otherwise returns immediately.
# - Ensuring a maximum capacity prevents memory overflow but requires checking 
#   conditions before performing operations, which could add slight overhead.

# Pitfalls to Avoid:
# - Failing to check for underflow (popping from an empty stack) can lead to errors.
# - Allowing unbounded stack growth can cause memory issues in long-running applications.
# - Be mindful of performance implications when using lists versus deques based on your use case.
# - When designing custom structures, consider implementing methods for size checks or capacity management.


#=================================================================================
# Data Structures, Basic Data Structures, Queues
#=================================================================================

# In this section, we focus specifically on queues, a fundamental data structure.
# A queue follows the first-in, first-out (FIFO) principle, meaning the first element added 
# to the queue will be the first one to be removed. This characteristic makes queues 
# particularly useful for scenarios such as scheduling, buffering, and managing resources.

# 1. Basic Data Structures: Queues

# Simple Queue
# Python's collections module provides a deque (double-ended queue) that can be 
# used to implement a simple queue. The deque allows efficient appending and popping 
# from both ends, making it a versatile choice for queue operations.

from collections import deque

simple_queue = deque()  # Initialize an empty deque to represent the queue
simple_queue.append(1)  # Enqueue: add an element to the back of the queue
simple_queue.append(2)  # Enqueue another element
print("Queue after enqueues:", simple_queue)  # Outputs: deque([1, 2])

dequeued_element = simple_queue.popleft()  # Dequeue: remove the front element
print("Dequeued element:", dequeued_element)  # Outputs: 1
print("Queue after dequeue:", simple_queue)  # Remaining elements in the queue

# Use case: Simple queues are ideal for handling requests in order, such as print jobs 
# sent to a printer or tasks in a task scheduling system.

# Time Complexity Analysis:
# - Enqueue operation: O(1) average time complexity for appending to the end of the deque.
# - Dequeue operation: O(1) average time complexity for removing from the front of the deque.
# - Best and worst case scenarios are consistent in this implementation due to the 
#   underlying data structure used by deque.

# Circular Queue
# A circular queue is an extension of the standard queue where the last position is connected 
# back to the first position. This implementation helps in efficiently utilizing space, 
# particularly when the queue is represented with a fixed-size array.

class CircularQueue:
    def __init__(self, size):
        self.size = size  # Fixed size of the queue
        self.queue = [None] * size  # Initialize an array with the given size
        self.front = self.rear = -1  # Pointers for front and rear

    def enqueue(self, value):
        # Add an element to the queue
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")  # Circular condition: queue is full
            return
        if self.front == -1:  # If the queue is empty
            self.front = self.rear = 0  # Set front and rear to 0
        else:
            self.rear = (self.rear + 1) % self.size  # Move rear circularly
        self.queue[self.rear] = value  # Insert the new value

    def dequeue(self):
        # Remove an element from the queue
        if self.front == -1:  # If the queue is empty
            print("Queue is empty")
            return None
        value = self.queue[self.front]  # Store the front value to return
        if self.front == self.rear:  # If the queue has only one element
            self.front = self.rear = -1  # Reset the queue
        else:
            self.front = (self.front + 1) % self.size  # Move front circularly
        return value

circular_queue = CircularQueue(5)  # Create a circular queue of size 5
circular_queue.enqueue(1)  # Enqueue 1
circular_queue.enqueue(2)  # Enqueue 2
print("Circular Queue Dequeued Element:", circular_queue.dequeue())  # Outputs: 1

# Time Complexity Analysis:
# - Enqueue operation: O(1) since we are performing a constant time calculation and assignment.
# - Dequeue operation: O(1) since moving the front pointer is a constant time operation.
# - Best and worst case scenarios are consistent; however, careful implementation is needed 
#   to avoid overflow conditions, particularly in circular implementations.

# Advanced tip:
# When implementing a circular queue, ensure to properly handle the wrap-around 
# condition with the modulo operator. This approach optimizes space by allowing 
# reusing freed spaces once elements are dequeued.

# Priority Queue
# A priority queue is an abstract data type where each element is associated with a priority. 
# Elements with higher priorities are served before those with lower priorities. 
# In Python, the heapq module provides an efficient implementation of a priority queue.

import heapq

priority_queue = []  # Initialize an empty list to represent the priority queue
heapq.heappush(priority_queue, (2, "Task 2"))  # Lower number indicates higher priority
heapq.heappush(priority_queue, (1, "Task 1"))  # Higher priority task
print("Priority Queue after adds:", priority_queue)  # Outputs: [(1, 'Task 1'), (2, 'Task 2')]

priority_task = heapq.heappop(priority_queue)  # Remove the highest priority task
print("Dequeued Priority Task:", priority_task)  # Outputs: (1, 'Task 1')

# Use case: Priority queues are widely used in scheduling algorithms, such as 
# Dijkstra's algorithm for finding the shortest path in graphs or managing tasks 
# in operating systems based on their priority levels.

# Time Complexity Analysis:
# - Insertion operation (heappush): O(log n) where n is the number of elements in the heap.
# - Deletion operation (heappop): O(log n) due to the need to reheapify the remaining elements.
# - This structure is optimal for scenarios where quick access to the highest priority element 
#   is essential, but performance can degrade if the queue grows excessively large.

# Deque (Double-ended Queue)
# A deque allows adding and removing elements from both ends efficiently. 
# This structure is beneficial when you need both FIFO and LIFO functionalities.

deque_example = deque()  # Create an empty deque
deque_example.append(1)  # Add to the right
deque_example.appendleft(2)  # Add to the left
print("Deque after additions:", deque_example)  # Outputs: deque([2, 1])

removed_element = deque_example.pop()  # Remove from the right end
print("Removed from Deque (right):", removed_element)  # Outputs: 1
print("Deque after removal:", deque_example)  # Remaining elements in the deque

# Time Complexity Analysis:
# - Adding elements (append, appendleft): O(1) since they directly modify the ends of the deque.
# - Removing elements (pop, popleft): O(1) as they also operate on the ends.
# - Deques are particularly useful when your algorithm requires both stack and queue operations 
#   efficiently without compromising performance.

# Advanced tip:
# Deques are highly efficient for implementing both queues and stacks with 
# O(1) time complexity for append and pop operations on both ends. This makes 
# them ideal for applications that require both queue and stack functionalities.

# Potential pitfalls:
# When using queues or deques, be mindful of the maximum size you allow, especially 
# in resource-limited environments. Implementing bounds checks can prevent overflow 
# and underflow issues, ensuring stability in your application.
# Additionally, ensure that your algorithm does not unintentionally create situations 
# where elements are not processed in the expected order, leading to incorrect results.


#=================================================================================
# Data Structures: Hash-based Structures, Hash Table
#=================================================================================

# Hash tables are a fundamental data structure providing efficient key-value storage.
# They use a hashing function to compute an index (hash) into an array of buckets or slots,
# allowing for average time complexity of O(1) for insertions, deletions, and lookups.

# Time Complexity Analysis:
# - Best Case: O(1) - When no collisions occur and the hash function distributes keys uniformly.
# - Average Case: O(1) - Generally expected with a good hash function and proper collision handling.
# - Worst Case: O(n) - In cases of many collisions (e.g., if all keys hash to the same index), leading to linear searches.

# Space Complexity: O(n) - Where n is the number of key-value pairs in the hash table.

# Hash Table Implementation
class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a fixed size.
        # Size defines the number of buckets available for storing key-value pairs.
        self.size = size  # Size of the array
        self.table = [[] for _ in range(size)]  # Create a list of empty buckets (each bucket is a list)

    def hash(self, key):
        # Compute the hash for the given key using modulo operation.
        # The modulo operation ensures the hash fits within the table's bounds.
        # This uses Python's built-in hash function for initial hashing.
        return hash(key) % self.size  # Use built-in hash function

    def insert(self, key, value):
        # Insert a key-value pair into the hash table.
        index = self.hash(key)  # Find the appropriate index using the hash function
        # Check if the key already exists in the bucket for updates.
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:  # Update the value if the key is found
                self.table[index][i] = (key, value)  # Update existing key-value pair
                return  # Exit after updating
        # If the key is not found, append the new key-value pair.
        self.table[index].append((key, value))  # Collision handling via chaining

    def lookup(self, key):
        # Retrieve a value by its key from the hash table.
        index = self.hash(key)  # Find the appropriate index
        # Search through the bucket for the key.
        for k, v in self.table[index]:  # Iterate through the list of key-value pairs
            if k == key:  # If key is found, return the corresponding value
                return v
        return None  # Return None if the key is not found

    def delete(self, key):
        # Remove a key-value pair from the hash table.
        index = self.hash(key)  # Find the appropriate index
        # Search for the key in the bucket.
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:  # If key is found, remove it
                del self.table[index][i]  # Delete the key-value pair
                return True  # Return True to indicate successful deletion
        return False  # Return False if the key was not found

# Example usage of the hash table
hash_table = HashTable()  # Create a new hash table
hash_table.insert("name", "Alice")  # Insert key-value pair for name
hash_table.insert("age", 30)  # Insert another pair for age
hash_table.insert("city", "New York")  # Insert third pair for city
print("Inserted key-value pairs.")

# Lookup examples
print("Lookup for 'name':", hash_table.lookup("name"))  # Expected output: Alice
print("Lookup for 'age':", hash_table.lookup("age"))  # Expected output: 30
print("Lookup for 'unknown':", hash_table.lookup("unknown"))  # Expected output: None (not found)

# Deletion example
hash_table.delete("city")  # Remove the key 'city'
print("Deleted key 'city'.")
print("Lookup for 'city':", hash_table.lookup("city"))  # Expected output: None (not found)

# Potential Pitfalls
# 1. Hash collisions: When multiple keys hash to the same index. 
#   - Handling can be done via chaining (as shown) or open addressing.
# 2. Performance degrades if the load factor (number of elements/size of table) is too high.
#   - A common practice is to resize the hash table when the load factor exceeds a threshold (e.g., 0.7).
# 3. Choosing a good hash function is critical for performance. A poor hash function can lead to excessive collisions.
#   - Aim for uniform distribution across the hash table to minimize clustering.

# Advanced Tips
# - Consider using built-in dictionaries in Python, as they are implemented as hash tables and are highly optimized.
# - When implementing your own hash table, consider dynamic resizing (doubling the size) when the load factor exceeds 0.7.
# - Explore different collision resolution strategies (e.g., linear probing, quadratic probing) in scenarios requiring 
#   special performance characteristics, like real-time data processing.
# - Profiling your hash table's performance with different datasets can provide insights into potential bottlenecks.
# - Always document the expected behavior of your hash table's methods, especially regarding handling collisions and resizing.

#=================================================================================
# Data Structures: Hash-based Structures, Hash Set
#=================================================================================

# Hash-based structures, such as hash tables, provide an efficient way to store and 
# retrieve data based on keys. They leverage a hash function to compute an index 
# (hash code) where the corresponding value is stored, allowing for average-case 
# time complexity of O(1) for lookup, insert, and delete operations.

# Hash Set
# A hash set is an unordered collection of unique elements. It is implemented 
# using a hash table, where each value is stored in a way that allows for fast 
# access and ensures no duplicates.

# Example: Creating a hash set using Python's built-in set
hash_set = set()  # Initialize an empty hash set
print("Initial Hash Set:", hash_set)

# Adding elements to the hash set
hash_set.add(1)  # Add an integer
hash_set.add(2)  # Add another integer
hash_set.add(2)  # Attempt to add a duplicate, which will be ignored
hash_set.add('a')  # Add a string
hash_set.add((1, 2))  # Add a tuple (hashable type)

print("Hash Set after additions:", hash_set)
# Output: Hash Set after additions: {1, 2, 'a', (1, 2)}

# Note: Only hashable types can be added to a hash set, which means mutable types 
# (like lists) cannot be included.

# Runtime Analysis:
# - Average Case: O(1) for add, remove, and check existence (contains).
# - Worst Case: O(n) for add and remove in scenarios of hash collisions (many items hashing to the same index).

# Tip: A good hash function minimizes collisions by distributing elements uniformly 
# across the hash table. Python's built-in hashing mechanism is generally robust 
# and handles a wide range of types.

# Removing elements from the hash set
hash_set.remove(1)  # Remove the integer 1 from the set
print("Hash Set after removal of 1:", hash_set)  # Output: {2, 'a', (1, 2)}

# Check for existence
exists = 2 in hash_set  # Check if 2 exists in the set
print("Does 2 exist in the Hash Set?", exists)  # Output: True

# Use case:
# Hash sets are commonly used for membership testing, ensuring uniqueness, 
# and implementing algorithms like the two-sum problem, where you check if 
# a complement exists for a given number.

# Iterating over a hash set
print("Iterating over Hash Set:")
for element in hash_set:
    print("Element:", element)

# Best Practices:
# - Keep the load factor (number of entries divided by the number of buckets) 
# below a certain threshold (commonly 0.7) to maintain performance. 
# Rehashing occurs when this threshold is exceeded, which involves creating 
# a new, larger table and re-inserting existing elements, leading to O(n) 
# time complexity for the operation.
# - Use immutable types as set elements to prevent accidental mutations that 
# can break the hash table's integrity.

# Potential Pitfalls:
# - Be cautious of hash collisions; they can degrade performance from O(1) to O(n).
# - The order of elements in a hash set is not guaranteed, as sets are unordered collections. 
# If order matters, consider using `collections.OrderedDict` or a sorted data structure.

# Advanced Insights:
# - In Python, the built-in `set` is implemented as a hash table that uses a dynamic 
# array for its underlying storage. This implementation ensures efficient use of 
# memory and speed. Understanding how these low-level operations work can help 
# in optimizing performance-critical applications.
# - Hash functions should ideally exhibit uniform distribution to minimize collisions. 
# You can create custom hash functions, but be aware of their impact on performance.

# Example: Using a custom hash function (not directly for set, but for understanding)
class CustomHashSet:
    def __init__(self):
        self.data = [None] * 10  # Fixed size for simplicity

    def _hash(self, key):
        return key % len(self.data)  # Simple hash function using modulus

    def add(self, key):
        index = self._hash(key)
        if self.data[index] is None:
            self.data[index] = [key]  # Start a new bucket
        else:
            if key not in self.data[index]:  # Ensure uniqueness
                self.data[index].append(key)

custom_hash_set = CustomHashSet()
custom_hash_set.add(1)
custom_hash_set.add(2)
custom_hash_set.add(2)  # Duplicate will be ignored
print("Custom Hash Set Data:", custom_hash_set.data)  # Visualize underlying data structure

#=================================================================================
# Data Structures: Hash-based Structures, Hash Map (Dictionary)
#=================================================================================

# In this section, we delve into hash-based data structures, focusing specifically 
# on hash maps, commonly implemented in Python as dictionaries. Hash maps provide 
# efficient key-value pair storage and retrieval through hashing techniques.

# Hash Map (Dictionary)
# A hash map is a collection of key-value pairs where each key is unique.
# Python dictionaries are implemented as hash tables, offering average-case O(1) 
# time complexity for lookups, insertions, and deletions. This efficiency stems from 
# the use of a hash function that converts keys into indices in an underlying array.

# Creating a dictionary
hash_map = {}  # Empty dictionary
print("Initial Hash Map:", hash_map)

# Inserting key-value pairs
hash_map['apple'] = 1  # Adds the key 'apple' with a value of 1
hash_map['banana'] = 2  # Adds the key 'banana' with a value of 2
hash_map['orange'] = 3  # Adds the key 'orange' with a value of 3
print("Hash Map after insertions:", hash_map)

# Retrieving values by keys
apple_count = hash_map['apple']  # Retrieves the value associated with the key 'apple'
print("Count of apples:", apple_count)

# Advanced tip: 
# Always use immutable types (like strings, numbers, and tuples) as keys since 
# mutable types (like lists or dictionaries) are not hashable and will raise a TypeError.

# Deleting a key-value pair
del hash_map['banana']  # Removes the key 'banana' and its associated value
print("Hash Map after deletion:", hash_map)

# Checking for key existence
key_exists = 'banana' in hash_map  # Returns False since 'banana' was deleted
print("Does 'banana' exist in the Hash Map?", key_exists)

# Iterating over keys and values
for key, value in hash_map.items():
    print(f"Key: {key}, Value: {value}")  # Outputs all key-value pairs

# Runtime Analysis
# The average time complexity for insertion, deletion, and lookup in a hash map is O(1).
# However, the worst-case time complexity can degrade to O(n) in scenarios of excessive collisions,
# which occurs when multiple keys hash to the same index, leading to chaining or probing.
# To mitigate this, a good hash function should distribute keys uniformly across the hash table.

# Best Case: O(1)
# - When keys are well distributed and no collisions occur, resulting in direct access.

# Worst Case: O(n)
# - Occurs when many keys hash to the same index, necessitating iteration through all the keys 
#   at that index, which leads to a linear search.

# Use Cases
# Hash maps are widely used for:
# - Implementing associative arrays where keys map to values, such as in caches or databases.
# - Counting occurrences of items (e.g., word frequencies in a document).
# - Grouping data by unique keys (e.g., creating a contact list by names).

# Potential Pitfalls
# - Be cautious about key collisions and choose a proper hash function to minimize them.
# - Managing the load factor is crucial; if the number of entries grows too close to the size of the array,
#   rehashing may be necessary, which is an O(n) operation. Python handles this automatically with 
#   its dictionary implementation, resizing the underlying array when necessary.
# - Be aware of the trade-off between time and space; using more memory can lead to faster access times.

# Advanced Implementation Considerations
# - Consider using collections.defaultdict or collections.Counter for specialized use cases where 
#   default values or counting capabilities are needed.
from collections import defaultdict, Counter

# Example of defaultdict to automatically initialize missing keys
default_dict = defaultdict(int)  # Default value of 0 for missing keys
default_dict['fruit'] += 1  # Automatically initializes 'fruit' to 0 and then adds 1
print("Default Dictionary Example:", default_dict)

# Example of Counter to count occurrences of elements in a list
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
item_counts = Counter(items)  # Counts occurrences of each unique item
print("Counter Example:", item_counts)  # Outputs: Counter({'banana': 3, 'apple': 2, 'orange': 1})


#=================================================================================
# Data Structures: Tree Structures, BST
#=================================================================================

# In this section, we explore tree structures, specifically binary trees.
# Trees are hierarchical data structures that consist of nodes connected by edges.
# Each tree has a root node and can have child nodes, which makes them useful for various applications.

# Binary Tree
# A binary tree is a type of tree where each node has at most two children, referred to as the left and right child.
# It can be used to implement various data structures and algorithms.

class TreeNode:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child

# Example of creating a simple binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)  # Create root node
root.left = TreeNode(2)  # Set left child of root
root.right = TreeNode(3)  # Set right child of root
root.left.left = TreeNode(4)  # Set left child of node 2
root.left.right = TreeNode(5)  # Set right child of node 2

# Example: Print the values of the binary tree using in-order traversal
def in_order_traversal(node):
    if node:  # Base case: If the node is not None
        in_order_traversal(node.left)  # Traverse the left subtree
        print("In-order traversal value:", node.value)  # Visit the node
        in_order_traversal(node.right)  # Traverse the right subtree

in_order_traversal(root)  # Output: 4, 2, 5, 1, 3

# Runtime Analysis:
# - The time complexity for tree traversal (like in-order) is O(n), where n is the number of nodes,
#   since each node is visited exactly once.
# - The space complexity is O(h), where h is the height of the tree, due to the recursion stack.

# Best and Worst Cases:
# - Best Case: A balanced binary tree leads to O(log n) height and faster operations.
# - Worst Case: An unbalanced binary tree (essentially a linked list) leads to O(n) height,
#   resulting in slower operations for searching, inserting, and deleting.

# Practical Use Cases:
# - Binary trees are commonly used in searching and sorting algorithms, 
#   like binary search trees (BSTs).
# - They can represent hierarchical data, such as file systems, 
#   organization structures, or expression parsing (syntax trees).

# Binary Search Tree (BST)
# A binary search tree is a special kind of binary tree that maintains order:
# for any given node, all values in the left subtree are smaller, and all values 
# in the right subtree are larger.

class BSTNode(TreeNode):
    def insert(self, value):
        # Insert a new value in the BST
        if value < self.value:  # If the new value is less, go left
            if self.left is None:
                self.left = BSTNode(value)  # Place new node here if empty
            else:
                self.left.insert(value)  # Recursive insert in left subtree
        else:  # If the new value is greater or equal, go right
            if self.right is None:
                self.right = BSTNode(value)  # Place new node here if empty
            else:
                self.right.insert(value)  # Recursive insert in right subtree

bst_root = BSTNode(10)  # Create a BST root node
bst_root.insert(5)  # Insert 5
bst_root.insert(15)  # Insert 15
bst_root.insert(3)  # Insert 3
bst_root.insert(7)  # Insert 7

# Example: Print the values of the BST using in-order traversal to verify sorted order
in_order_traversal(bst_root)  # Output: 3, 5, 7, 10, 15

# Runtime Analysis for BST Operations:
# - Insertion: Average case O(log n), worst case O(n) (if unbalanced).
# - Searching: Average case O(log n), worst case O(n).
# - Deletion: Average case O(log n), worst case O(n).

# What to Look for When Implementing:
# - Ensure that the tree remains balanced to maintain optimal performance.
# - Consider using self-balancing trees (e.g., AVL trees or Red-Black trees) 
#   to guarantee O(log n) operations.
# - Test edge cases like inserting duplicate values or maintaining tree integrity after deletions.

# Summary:
# Tree structures, especially binary trees and binary search trees, provide 
# an efficient way to manage and organize data hierarchically.
# Understanding their properties and operations is essential for effective algorithm design.


#=================================================================================
# Data Structures
# Tree Structures
# AVL Tree
#=================================================================================

# An AVL Tree is a self-balancing binary search tree where the difference between
# the heights of the left and right subtrees (balance factor) for any node 
# is at most 1. This property ensures that the tree remains balanced,
# enabling efficient operations such as insertion, deletion, and search.

# Characteristics of AVL Trees:
# 1. Binary Search Tree property: Left child < Parent < Right child
# 2. Balance factor (height difference) must be -1, 0, or 1 for all nodes.
# 3. Rotations are performed to maintain balance after insertions and deletions.

# Time Complexity:
# - Search: O(log n) - Balanced structure allows for efficient searching.
# - Insertion: O(log n) - Due to potential rotations to maintain balance.
# - Deletion: O(log n) - Similar to insertion, with rotations if needed.
# Best case: O(log n) when the tree is perfectly balanced.
# Worst case: O(n) when the tree becomes unbalanced (linear structure), but AVL guarantees O(log n) through balancing.

# Example Node Structure for AVL Tree
class AVLNode:
    def __init__(self, key):
        self.key = key  # The value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.height = 1  # Initial height of the node

# Utility function to get the height of a node
def get_height(node):
    if not node:
        return 0  # Height of None is 0
    return node.height  # Return the height of the current node

# Utility function to calculate balance factor
def get_balance(node):
    if not node:
        return 0  # Balance factor of None is 0
    return get_height(node.left) - get_height(node.right)  # Height difference between left and right

# Right Rotation
# Used to balance the tree when left subtree is heavier (Left-Left Case)
def right_rotate(z):
    y = z.left  # Set y as the left child of z
    T3 = y.right  # T3 is the right subtree of y
    y.right = z  # Perform rotation
    z.left = T3  # Update the left child of z to T3
    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y  # Return the new root

# Left Rotation
# Used to balance the tree when right subtree is heavier (Right-Right Case)
def left_rotate(z):
    y = z.right  # Set y as the right child of z
    T2 = y.left  # T2 is the left subtree of y
    y.left = z  # Perform rotation
    z.right = T2  # Update the right child of z to T2
    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y  # Return the new root

# Insertion into AVL Tree
# This function inserts a key into the AVL tree and balances the tree if necessary.
def insert(root, key):
    # Step 1: Perform normal BST insert
    if not root:
        return AVLNode(key)  # Create a new node if root is None
    elif key < root.key:
        root.left = insert(root.left, key)  # Insert into the left subtree
    else:
        root.right = insert(root.right, key)  # Insert into the right subtree

    # Step 2: Update height of this ancestor node
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Step 3: Get the balance factor to check whether this node became unbalanced
    balance = get_balance(root)

    # Step 4: If this node becomes unbalanced, there are 4 cases

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)  # Perform right rotation

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)  # Perform left rotation

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)  # Perform left rotation on left child
        return right_rotate(root)  # Perform right rotation

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)  # Perform right rotation on right child
        return left_rotate(root)  # Perform left rotation

    return root  # Return the (unchanged) node pointer

# Creating an AVL tree and inserting elements
root = None  # Starting with an empty tree
keys_to_insert = [30, 20, 40, 10, 5, 3]  # Sample keys for insertion
for key in keys_to_insert:
    root = insert(root, key)  # Insert each key

# Example: print height of the root to confirm AVL properties
print("Height of root after insertions:", get_height(root))  # Should reflect the tree's balance

# Example: Displaying the balance factor for the root
print("Balance factor of root:", get_balance(root))  # Should be in the range of -1, 0, 1

# Use case: AVL Trees are particularly useful in applications where frequent 
# insertions and deletions occur, such as in databases or memory management systems 
# that require maintaining a sorted order with efficient access times.

# Pitfalls and Considerations:
# - Rotations can add overhead during insertions and deletions; consider the use case.
# - If frequent random insertions/deletions occur, an AVL Tree might be beneficial 
# over a basic binary search tree due to its guaranteed O(log n) performance.
# - Be cautious about the complexity of maintaining balance; this adds to code complexity.
# - For datasets with mostly sorted data, AVL trees can become unbalanced quickly, 
# leading to potential performance issues if not managed properly.

#=================================================================================
# Data Structures - Tree Structures
#=================================================================================

# In this section, we will discuss tree structures, focusing specifically on the 
# Red-Black Tree. A Red-Black Tree is a self-balancing binary search tree where 
# each node contains an extra bit for denoting the color of the node, either red or black.
# This property helps maintain balance during insertions and deletions, ensuring efficient 
# performance for operations such as search, insert, and delete.

# Characteristics of Red-Black Trees:
# 1. Each node is colored either red or black.
# 2. The root is always black.
# 3. All leaves (NIL nodes) are black.
# 4. If a node is red, both its children must be black (no two reds in a row).
# 5. Every path from a node to its descendant NIL nodes must have the same number of black nodes.

# The Red-Black Tree maintains its balance using rotations during insertion and deletion.
# This ensures that the tree height remains logarithmic relative to the number of nodes, 
# providing efficient operations.

# Example implementation of a Red-Black Tree
class RedBlackNode:
    def __init__(self, value, color='red'):
        self.value = value  # Store the value of the node
        self.color = color  # Color of the node ('red' or 'black')
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.parent = None  # Pointer to the parent node

# The RedBlackTree class manages the overall structure of the tree
class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(value=None, color='black')  # Sentinel node representing leaves
        self.root = self.NIL  # Initialize the root as NIL

    def insert(self, value):
        # Insertion follows binary search tree rules, then colors the node and fixes violations
        new_node = RedBlackNode(value)  # Create a new node
        new_node.left = new_node.right = self.NIL  # Initialize children to NIL
        self._insert_node(new_node)  # Insert the node using BST logic
        self._fix_insertion(new_node)  # Fix any violations of Red-Black properties

    def _insert_node(self, new_node):
        # Standard BST insert logic
        current = self.root
        parent = None
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left  # Move left
            else:
                current = current.right  # Move right
        new_node.parent = parent  # Set parent
        if parent is None:  # Tree was empty
            self.root = new_node  # New node is the root
        elif new_node.value < parent.value:
            parent.left = new_node  # Set new node as left child
        else:
            parent.right = new_node  # Set new node as right child

    def _fix_insertion(self, node):
        # Fixes violations of Red-Black Tree properties after insertion
        while node != self.root and node.parent.color == 'red':  # While the parent is red
            # If the parent is the left child of the grandparent
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right  # Get the uncle
                if uncle.color == 'red':  # Case 1: Uncle is red
                    node.parent.color = 'black'  # Recolor parent
                    uncle.color = 'black'  # Recolor uncle
                    node.parent.parent.color = 'red'  # Recolor grandparent
                    node = node.parent.parent  # Move up the tree
                else:  # Case 2: Uncle is black
                    if node == node.parent.right:  # Left-Right case
                        node = node.parent  # Perform left rotation
                        self._rotate_left(node)
                    # Left-Left case
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_right(node.parent.parent)  # Perform right rotation
            else:  # Mirror image of the above case
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_left(node.parent.parent)
        self.root.color = 'black'  # Ensure root is always black

    def _rotate_left(self, node):
        # Perform a left rotation around the given node
        right_child = node.right
        node.right = right_child.left  # Move the left subtree of right_child
        if right_child.left != self.NIL:
            right_child.left.parent = node
        right_child.parent = node.parent  # Link the parent of node to right_child
        if node.parent is None:
            self.root = right_child  # If node was root, update root
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node  # Make node the left child of right_child
        node.parent = right_child

    def _rotate_right(self, node):
        # Perform a right rotation around the given node
        left_child = node.left
        node.left = left_child.right  # Move the right subtree of left_child
        if left_child.right != self.NIL:
            left_child.right.parent = node
        left_child.parent = node.parent  # Link the parent of node to left_child
        if node.parent is None:
            self.root = left_child  # If node was root, update root
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node  # Make node the right child of left_child
        node.parent = left_child

# Create an instance of the RedBlackTree
red_black_tree = RedBlackTree()
# Insert elements into the Red-Black Tree
values_to_insert = [10, 20, 30, 15]
for value in values_to_insert:
    red_black_tree.insert(value)  # Insert values into the tree

# Best and Worst Case Runtime Analysis:
# - The time complexity for insertion in a Red-Black Tree is O(log n) in both best and worst cases,
#   due to the self-balancing property that ensures the height of the tree is logarithmic with respect to the number of nodes.
# - The worst-case height of the tree is 2*log(n+1), ensuring that the tree remains balanced.
# - It is essential to implement the rotation and fixing logic carefully to maintain the Red-Black properties after insertions and deletions.

# Pitfalls to Avoid:
# - Failing to maintain the properties of the Red-Black Tree can lead to unbalanced trees, 
#   resulting in performance degradation (i.e., degrading to O(n) in the worst case).
# - Ensure proper handling of colors during rotations and fix-ups to maintain balance.
# - Testing with a variety of input scenarios, especially edge cases, is crucial for validating the implementation.

# Use Cases:
# Red-Black Trees are widely used in applications that require efficient search, insertion, and deletion operations, 
# such as associative arrays, database indexing, and memory management systems.
# Their self-balancing property makes them suitable for scenarios where frequent modifications are expected.


#=================================================================================
# Data Structures - Tree Structures
#=================================================================================

# In this section, we will explore tree structures, which are fundamental data 
# structures used to represent hierarchical relationships. 
# Trees consist of nodes connected by edges, with each tree having a root node 
# and potentially many child nodes.

# Segment Tree
# A segment tree is a binary tree used for storing intervals or segments. 
# It allows querying and updating of range-based data efficiently. 
# Segment trees are particularly useful for scenarios like range queries 
# (sum, minimum, maximum) and point updates.

# Basic structure of a segment tree node
class SegmentTreeNode:
    def __init__(self, start, end, sum):
        self.start = start  # Starting index of the segment
        self.end = end      # Ending index of the segment
        self.sum = sum      # Sum of the values in this segment
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child

# Example: Building a segment tree
def build_segment_tree(nums, start, end):
    if start == end:  # Leaf node
        return SegmentTreeNode(start, end, nums[start])  # Create a leaf node with the value
    mid = (start + end) // 2  # Midpoint to split the segment
    left_child = build_segment_tree(nums, start, mid)  # Build left subtree
    right_child = build_segment_tree(nums, mid + 1, end)  # Build right subtree
    # Create the current node with the sum of left and right children
    current_node = SegmentTreeNode(start, end, left_child.sum + right_child.sum)
    current_node.left = left_child  # Assign left child
    current_node.right = right_child  # Assign right child
    return current_node  # Return the current node

# Example usage of building a segment tree
nums = [1, 3, 5, 7, 9, 11]  # Array of numbers
segment_tree_root = build_segment_tree(nums, 0, len(nums) - 1)

# Output the root of the segment tree
print("Segment Tree Root Sum:", segment_tree_root.sum)  # Outputs the total sum of the array

# Run Time Analysis:
# Building the segment tree takes O(n) time, where n is the number of elements in the array.
# This is because each element is visited once to construct the tree.
# The space complexity is O(n) as well, due to the additional nodes created.

# Use Case: Segment trees are particularly useful in scenarios that require
# frequent range queries and updates, such as:
# - Finding the sum of elements in a given range.
# - Updating a specific element in the array while maintaining the ability to query.

# Querying a Segment Tree
# To find the sum of elements in a given range [query_start, query_end],
# we need to implement a function that recursively traverses the tree.

def range_sum_query(node, query_start, query_end):
    if node.start > query_end or node.end < query_start:  # No overlap
        return 0
    if node.start >= query_start and node.end <= query_end:  # Total overlap
        return node.sum
    # Partial overlap, query both children
    left_sum = range_sum_query(node.left, query_start, query_end)
    right_sum = range_sum_query(node.right, query_start, query_end)
    return left_sum + right_sum  # Combine results from both sides

# Example of querying a segment tree
query_start = 1
query_end = 3
result_sum = range_sum_query(segment_tree_root, query_start, query_end)
print("Range Sum Query [1, 3]:", result_sum)  # Outputs: 15 (3 + 5 + 7)

# Run Time Analysis for Queries:
# Each query takes O(log n) time since the tree is balanced.
# This logarithmic time complexity allows for efficient range queries.

# Updating a Segment Tree
# To update a specific element at index 'idx' to a new value 'val',
# we need to traverse the tree to find the corresponding node.

def update_segment_tree(node, idx, val):
    if node.start == node.end:  # Leaf node
        node.sum = val  # Update the sum
        return
    mid = (node.start + node.end) // 2  # Find the midpoint
    if idx <= mid:  # If the index is in the left child
        update_segment_tree(node.left, idx, val)  # Update left child
    else:  # If the index is in the right child
        update_segment_tree(node.right, idx, val)  # Update right child
    # Update the current node's sum after the update
    node.sum = node.left.sum + node.right.sum

# Example of updating the segment tree
update_segment_tree(segment_tree_root, 1, 10)  # Update index 1 to value 10
print("Updated Segment Tree Root Sum:", segment_tree_root.sum)  # Outputs updated sum

# Run Time Analysis for Updates:
# Each update operation also takes O(log n) time due to the tree structure,
# allowing for efficient modifications to the data.

# Best and Worst Case Scenarios:
# - Best Case: For a balanced segment tree, both query and update operations perform in O(log n) time.
# - Worst Case: In a degenerate case (like a linked list), the performance could degrade to O(n),
# but this is avoided by ensuring the segment tree remains balanced.

# Potential Pitfalls:
# - Implementing the segment tree can be complex, especially when handling edge cases.
# - Ensure correct handling of ranges during queries and updates to avoid incorrect results.

# Advanced Tip:
# Segment trees can also be enhanced with lazy propagation for efficient range updates, 
# which allows for updating a range of values in O(log n) time while maintaining the 
# efficiency of queries. Lazy propagation stores pending updates at the nodes, deferring 
# them until necessary.


#=================================================================================
# Data Structures: Tree Structures and Fenwick Tree (Binary Indexed Tree)
#=================================================================================

# In this section, we explore tree data structures and specifically focus on the Fenwick Tree, 
# also known as a Binary Indexed Tree (BIT). These structures are useful for efficient 
# querying and updating of prefix sums.

# Tree Structures
# A tree is a hierarchical data structure consisting of nodes connected by edges. 
# It has the following characteristics:
# - One node is designated as the root.
# - Every node (except the root) has one parent and may have zero or more children.
# - Trees are non-linear, allowing for efficient representation of hierarchical data.

# Example of a simple binary tree node structure
class TreeNode:
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# Creating a binary tree manually
root = TreeNode(1)  # Root node
root.left = TreeNode(2)  # Left child
root.right = TreeNode(3)  # Right child
root.left.left = TreeNode(4)  # Left grandchild
root.left.right = TreeNode(5)  # Right grandchild

# Example: Printing the binary tree's structure (simple representation)
print("Binary Tree Structure:")
print("       ", root.value)  # Root
print("      / \\")
print("     ", root.left.value, " ", root.right.value)  # First level children
print("    / \\  / \\")
print("   ", root.left.left.value, " ", root.left.right.value)  # Second level children

# Use cases:
# - Trees are widely used for hierarchical data representation, 
# such as file systems, organizational structures, and databases.
# - Binary trees are used in search algorithms and binary search trees (BST).

# Fenwick Tree (Binary Indexed Tree)
# A Fenwick Tree is a data structure that allows efficient updates and queries on 
# cumulative frequency tables or prefix sums. It is particularly useful when you 
# need to handle a large number of updates and queries efficiently.

# Basic structure of a Fenwick Tree
class FenwickTree:
    def __init__(self, size):
        self.size = size  # Size of the Fenwick Tree
        self.tree = [0] * (size + 1)  # Index 0 is not used

    def update(self, index, delta):
        # Updates the Fenwick Tree by adding 'delta' to the element at 'index'
        while index <= self.size:
            self.tree[index] += delta  # Update the tree at the index
            index += index & -index  # Move to the next index

    def query(self, index):
        # Returns the cumulative frequency from index 1 to index 'index'
        result = 0
        while index > 0:
            result += self.tree[index]  # Sum values up to the index
            index -= index & -index  # Move to the parent index
        return result

# Example usage of Fenwick Tree
fenwick_tree = FenwickTree(5)  # Initialize a Fenwick Tree of size 5
fenwick_tree.update(1, 5)  # Update index 1 by adding 5
fenwick_tree.update(2, 3)  # Update index 2 by adding 3
fenwick_tree.update(3, 7)  # Update index 3 by adding 7

# Query the cumulative sum from index 1 to 3
cumulative_sum = fenwick_tree.query(3)
print("Cumulative sum from index 1 to 3:", cumulative_sum)  # Outputs: 15 (5 + 3 + 7)

# Runtime Analysis:
# - The update operation runs in O(log n) time because the index is updated logarithmically.
# - The query operation also runs in O(log n) time for the same reason.
# - The Fenwick Tree is particularly space-efficient, using O(n) space.

# Best and Worst Cases:
# - Both update and query operations will consistently have O(log n) time complexity, 
# making Fenwick Trees effective for dynamic cumulative frequency problems.
# - The worst-case scenario involves frequent updates and queries, but the logarithmic 
# time ensures that performance remains manageable.

# Advanced Tips:
# - Fenwick Trees can be used for problems like finding the frequency of elements 
# in a dynamic array, computing range sums, and maintaining cumulative frequency tables.
# - They are often preferred over segment trees when you need simpler implementation 
# and more space efficiency, though segment trees provide more flexibility for range queries.

# Potential Pitfalls:
# - Ensure correct index handling since Fenwick Trees typically use 1-based indexing.
# - Be mindful of the initial array size and ensure updates do not exceed the bounds 
# of the tree, as this could lead to unexpected behavior.


#=================================================================================
# Data Structures: Tree Structures, B-Trees
#=================================================================================

# Tree structures are hierarchical data structures that consist of nodes connected by edges.
# Each tree has a root node and child nodes. Trees are particularly useful for representing 
# hierarchical relationships and allow for efficient searching, insertion, and deletion.

# Characteristics of Trees:
# - Each tree has a root node, which is the topmost node.
# - Nodes can have zero or more children.
# - Nodes with the same parent are called siblings.
# - A leaf node is a node with no children.
# - The height of a tree is the length of the longest path from the root to a leaf.

# Common operations on trees:
# - Insertion
# - Deletion
# - Traversal (in-order, pre-order, post-order)

# 1. Binary Tree
# A binary tree is a tree data structure where each node has at most two children.
# This structure allows for efficient searching and sorting.

class TreeNode:
    def __init__(self, value):
        self.value = value  # Node value
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child

# Example: Creating a simple binary tree
root = TreeNode(1)  # Root node
root.left = TreeNode(2)  # Left child
root.right = TreeNode(3)  # Right child
print("Binary Tree Root Value:", root.value)  # Outputs: 1
print("Left Child Value:", root.left.value)  # Outputs: 2
print("Right Child Value:", root.right.value)  # Outputs: 3

# Time complexity for operations:
# - Insertion: O(log n) on average for balanced trees, O(n) in the worst case (unbalanced).
# - Searching: O(log n) on average for balanced trees, O(n) in the worst case.
# - Deletion: O(log n) on average for balanced trees, O(n) in the worst case.

# 2. Binary Search Tree (BST)
# A binary search tree is a binary tree with the following properties:
# - The left subtree of a node contains only nodes with values less than the node's value.
# - The right subtree contains only nodes with values greater than the node's value.

# Example: Inserting nodes in a BST
def insert_bst(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

bst_root = None
bst_values = [5, 3, 7, 2, 4, 6, 8]
for value in bst_values:
    bst_root = insert_bst(bst_root, value)

print("BST Root Value:", bst_root.value)  # Outputs: 5

# Traversal example (In-order)
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print("Visited Node:", node.value)
        in_order_traversal(node.right)

print("In-Order Traversal of BST:")
in_order_traversal(bst_root)  # Outputs the nodes in sorted order

# Time complexity for BST operations:
# - Insertion: O(log n) on average, O(n) in the worst case (unbalanced).
# - Searching: O(log n) on average, O(n) in the worst case.
# - Deletion: O(log n) on average, O(n) in the worst case.

# 3. Balanced Trees (e.g., AVL Tree, Red-Black Tree)
# Balanced trees maintain a balanced height to ensure O(log n) performance for all operations.
# This is crucial to prevent performance degradation seen in unbalanced trees.

# Example: AVL tree
class AVLNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1  # Height of the node for balancing purposes

# AVL trees automatically adjust their height during insertion and deletion,
# maintaining balance for efficient operations.

# 4. B-Trees
# A B-tree is a self-balancing tree data structure that maintains sorted data 
# and allows searches, sequential access, insertions, and deletions in logarithmic time.
# It is commonly used in databases and file systems due to its efficiency in reading and writing large blocks of data.

# Properties of B-Trees:
# - A B-tree of order m can have at most m children.
# - Each node has at most m-1 keys.
# - All leaves are at the same level, which maintains balance.

# Example: Creating a simple B-tree node
class BTreeNode:
    def __init__(self, t):
        self.t = t  # Minimum degree (defines the range for the number of keys)
        self.keys = []  # List of keys
        self.children = []  # List of child nodes
        self.leaf = True  # True if leaf node, false otherwise

# Example of inserting a key into a B-tree
def insert_b_tree(root, key):
    if len(root.keys) == (2 * root.t) - 1:  # Node is full
        # Create a new root and split the old root
        new_root = BTreeNode(root.t)
        new_root.leaf = False
        new_root.children.append(root)  # Old root becomes a child of new root
        split_child(new_root, 0)  # Split the old root
        insert_non_full(new_root, key)  # Insert the new key
        return new_root
    else:
        insert_non_full(root, key)
        return root

def split_child(parent, index):
    # Split the child node of the parent at the specified index
    t = parent.t
    full_child = parent.children[index]
    new_child = BTreeNode(t)  # New child node
    parent.keys.insert(index, full_child.keys[t - 1])  # Move median key up to parent
    parent.children.insert(index + 1, new_child)  # New child added to parent

    new_child.keys = full_child.keys[t:]  # Transfer keys to new child
    full_child.keys = full_child.keys[:t - 1]  # Retain left keys in old child

    if not full_child.leaf:  # If not a leaf, transfer children
        new_child.children = full_child.children[t:]
        full_child.children = full_child.children[:t]

def insert_non_full(node, key):
    # Insert a key into a non-full B-tree node
    i = len(node.keys) - 1
    if node.leaf:
        # If the node is a leaf, insert the key directly
        while i >= 0 and key < node.keys[i]:
            i -= 1
        node.keys.insert(i + 1, key)  # Insert key in sorted order
    else:
        # Find the child to insert the key into
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        if len(node.children[i].keys) == (2 * node.t) - 1:
            split_child(node, i)  # Split child if it's full
            if key > node.keys[i]:  # Adjust index if key is greater than the new key
                i += 1
        insert_non_full(node.children[i], key)  # Insert in the chosen child

# Example of inserting keys into a B-tree
b_tree_root = BTreeNode(2)  # Create a B-tree of order 2
keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]
for key in keys_to_insert:
    b_tree_root = insert_b_tree(b_tree_root, key)

# Example: Print the keys in the B-tree
print("B-Tree Keys after Insertions:", b_tree_root.keys)  # Shows the keys in the root node
# Note: This is a simplified representation. In a full implementation, we would need
# to traverse the entire B-tree to print all keys.

# Time complexity for B-Tree operations:
# - Insertion: O(log n)
# - Deletion: O(log n)
# - Searching: O(log n)

# When implementing tree structures, consider the following:
# - Balance: Use self-balancing trees like AVL or Red-Black trees for guaranteed performance.
# - Use appropriate data structures (e.g., B-Trees) for disk storage and retrieval in databases.
# - Analyze space complexity alongside time complexity; trees can require significant memory overhead.
# - Test for edge cases (e.g., inserting into a full tree, deleting from a tree with one node).

#=================================================================================
# Data Structures, Tree Structures, N-ary Tree
#=================================================================================

# In this section, we will discuss tree structures, focusing on N-ary trees.
# Trees are hierarchical data structures that consist of nodes connected by edges.
# Each tree has a root node and can have child nodes. N-ary trees generalize binary trees 
# by allowing each node to have up to N children.

# Tree Structures
# Trees are widely used in computer science for various applications, including 
# representing hierarchical data, parsing expressions, and searching algorithms.

# 1. N-ary Tree
# An N-ary tree is a tree data structure where each node can have up to N children.
# N-ary trees are useful for representing data with multiple relationships.

# Node class for N-ary tree
class NaryNode:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.children = []  # Initialize an empty list for children nodes

# Example: Creating an N-ary tree
root = NaryNode(1)  # Create the root node with value 1
child1 = NaryNode(2)  # Create a child node with value 2
child2 = NaryNode(3)  # Create a child node with value 3
child3 = NaryNode(4)  # Create a child node with value 4

# Adding children to the root node
root.children.append(child1)  # Add child1 to the root's children
root.children.append(child2)  # Add child2 to the root's children
root.children.append(child3)  # Add child3 to the root's children

# Printing the root's value and its children's values
print("Root Value:", root.value)  # Outputs: 1
for child in root.children:  # Iterate over the root's children
    print("Child Value:", child.value)  # Outputs: 2, 3, 4

# Use case:
# N-ary trees can be used to represent data like file systems, organizational structures, 
# or any other data that naturally fits a hierarchical model.

# Traversal Methods for N-ary Trees
# Traversing a tree involves visiting each node in a specific order. Common traversal methods 
# include pre-order, post-order, and level-order.

# Pre-order Traversal: Visit the root, then each child recursively.
def pre_order_traversal(node):
    if node is not None:
        print(node.value, end=" ")  # Process the node (here, we print its value)
        for child in node.children:  # Traverse each child
            pre_order_traversal(child)

# Example: Perform pre-order traversal on the N-ary tree
print("Pre-order Traversal:", end=" ")
pre_order_traversal(root)  # Outputs: 1 2 3 4

# Post-order Traversal: Visit each child recursively, then the root.
def post_order_traversal(node):
    if node is not None:
        for child in node.children:  # Traverse each child
            post_order_traversal(child)  # Visit child first
        print(node.value, end=" ")  # Process the node after children

# Example: Perform post-order traversal on the N-ary tree
print("\nPost-order Traversal:", end=" ")
post_order_traversal(root)  # Outputs: 2 3 4 1

# Level-order Traversal: Visit nodes level by level.
def level_order_traversal(root):
    if not root:
        return
    queue = [root]  # Initialize a queue with the root node
    while queue:
        current = queue.pop(0)  # Dequeue the front element
        print(current.value, end=" ")  # Process the node
        for child in current.children:  # Enqueue all children
            queue.append(child)

# Example: Perform level-order traversal on the N-ary tree
print("\nLevel-order Traversal:", end=" ")
level_order_traversal(root)  # Outputs: 1 2 3 4

# Runtime Analysis
# The runtime for traversing an N-ary tree depends on the number of nodes 'V' in the tree.
# - Time Complexity: O(V) for all traversal methods as each node is visited once.
# - Space Complexity: O(h) for recursive methods, where h is the height of the tree due to the call stack.
# For level-order traversal, the space complexity is O(w), where w is the maximum width of the tree.

# Best and Worst Cases:
# - Best Case: The tree is balanced, leading to efficient traversal and low height (h).
# - Worst Case: The tree is skewed (like a linked list), increasing the height and space complexity.

# Considerations when implementing:
# - Determine the appropriate traversal method based on the use case.
# - Be mindful of the tree's height and structure when planning for memory usage.
# - Ensure that children are managed correctly to avoid memory leaks or references to deleted nodes.
# - When building N-ary trees, consider using a list for children for simplicity but be aware of its performance characteristics.

#=================================================================================
# Data Structures: Tree Structures and Tries (Prefix Trees)
#=================================================================================

# Trees are hierarchical data structures consisting of nodes connected by edges.
# They are widely used for representing data that has a parent-child relationship, 
# making them essential for various applications in computer science.

# Tree Structures
# A basic tree consists of nodes, where each node contains a value and references to its children.
# The top node is called the root, and nodes without children are leaves.

class TreeNode:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.children = []  # Initialize an empty list for child nodes

    def add_child(self, child_node):
        # Add a child node to the current node
        self.children.append(child_node)

# Example: Building a simple tree structure
root = TreeNode(1)  # Create root node with value 1
child1 = TreeNode(2)  # Create child node with value 2
child2 = TreeNode(3)  # Create child node with value 3
root.add_child(child1)  # Add child1 to the root
root.add_child(child2)  # Add child2 to the root

# Example: Printing tree structure
print("Root Value:", root.value)
for child in root.children:
    print("Child Value:", child.value)

# Time Complexity:
# - Adding a child node is O(1) because it involves appending to a list.
# - Traversing a tree to find a value can be O(n) in the worst case, where n is the number of nodes.

# Common Use Cases:
# - Representing hierarchical data, such as organizational structures or file systems.
# - Implementing algorithms like depth-first search (DFS) or breadth-first search (BFS).

# Trie (Prefix Tree)
# A trie is a specialized tree used to store a dynamic set of strings, 
# where the keys are usually strings. Each node represents a single character of a key.

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the trie with a root node

    def insert(self, word):
        # Insert a word into the trie
        current_node = self.root  # Start from the root node
        for char in word:  # For each character in the word
            if char not in current_node.children:
                current_node.children[char] = TrieNode()  # Create a new node if char not present
            current_node = current_node.children[char]  # Move to the child node
        current_node.is_end_of_word = True  # Mark the end of the word

    def search(self, word):
        # Search for a word in the trie
        current_node = self.root
        for char in word:  # Traverse the trie according to the characters in the word
            if char not in current_node.children:
                return False  # Return False if char not found
            current_node = current_node.children[char]
        return current_node.is_end_of_word  # Return True if end of word is reached

    def starts_with(self, prefix):
        # Check if any word starts with the given prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False  # Return False if prefix not found
            current_node = current_node.children[char]
        return True  # Return True if prefix is found

# Example: Inserting and searching words in a trie
trie = Trie()
trie.insert("hello")
trie.insert("hell")
trie.insert("heaven")

print("Search 'hello':", trie.search("hello"))  # Outputs: True
print("Search 'hell':", trie.search("hell"))    # Outputs: True
print("Search 'heav':", trie.search("heav"))     # Outputs: False
print("Prefix 'hea':", trie.starts_with("hea"))   # Outputs: True

# Time Complexity:
# - Inserting a word is O(m), where m is the length of the word.
# - Searching for a word is also O(m).
# - The space complexity can be O(n * m) in the worst case, where n is the number of words and m is the average length of the words.

# Advanced Tip:
# When implementing a trie, consider using a list for children instead of a dictionary if the character set is limited (e.g., lowercase letters).
# This can improve memory efficiency and access speed. 

# Potential Pitfalls:
# - A trie can consume a lot of memory, especially for large character sets. Use character compression techniques if necessary.
# - Ensure to properly handle the case sensitivity of words if the application requires it.


#=================================================================================
# Data Structures: Graph Structures, Adjacency Matrix
#=================================================================================

# Graphs are abstract data types that consist of a finite set of vertices (or nodes)
# and a set of edges connecting these vertices. They are used to model relationships
# between pairs of objects and are fundamental in various applications like social networks,
# route navigation systems, and dependency graphs.

# One common way to represent a graph is through an adjacency matrix.
# An adjacency matrix is a 2D array (or list of lists) where the element at row i 
# and column j indicates the presence (and sometimes the weight) of an edge between 
# vertex i and vertex j.

# 1. Adjacency Matrix
# The adjacency matrix is efficient for dense graphs (where the number of edges is close 
# to the maximum possible), but less efficient for sparse graphs (with relatively few edges).

# Example: Creating an adjacency matrix for a simple undirected graph
# Consider the graph with vertices A, B, C, D:
# A -- B
# |  /
# | /
# C -- D

# Here we represent vertices as indices: A=0, B=1, C=2, D=3.
# The adjacency matrix will look like this:
#   A B C D
# A 0 1 1 0
# B 1 0 0 0
# C 1 0 0 1
# D 0 0 1 0

# Initialize the adjacency matrix for 4 vertices
num_vertices = 4
adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

# Adding edges to the adjacency matrix
adjacency_matrix[0][1] = 1  # Edge A-B
adjacency_matrix[1][0] = 1  # Edge B-A (undirected graph, so symmetric)
adjacency_matrix[0][2] = 1  # Edge A-C
adjacency_matrix[2][0] = 1  # Edge C-A (undirected)
adjacency_matrix[2][3] = 1  # Edge C-D
adjacency_matrix[3][2] = 1  # Edge D-C (undirected)

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(row)

# Output:
# Adjacency Matrix:
# [0, 1, 1, 0]
# [1, 0, 0, 0]
# [1, 0, 0, 1]
# [0, 0, 1, 0]

# Runtime Analysis:
# - Space Complexity: O(V^2), where V is the number of vertices, due to the storage 
# of a 2D array that represents all possible edges.
# - Time Complexity for adding an edge: O(1) as we directly access the matrix 
# using the vertex indices.

# Best Case: The best case is when the graph is dense, making the adjacency matrix 
# representation space-efficient and access time optimal.
# Worst Case: The worst case occurs with sparse graphs, where a lot of memory is wasted 
# on storing zeros, leading to inefficient space usage.

# Use Case:
# The adjacency matrix is particularly useful for algorithms that require quick 
# lookups to check if an edge exists between two vertices (constant time complexity).

# Advanced Tips:
# - When implementing graph algorithms, consider the trade-offs between 
# adjacency matrix and adjacency list representations.
# - Adjacency matrices are less memory efficient for sparse graphs compared to adjacency lists,
# which only store edges that exist, typically using a dictionary or list of lists.
# - In case of weighted edges, the value in the matrix can represent the weight, 
# while a value of 0 (or some sentinel value) can denote the absence of an edge.

# Potential Pitfalls:
# - When using an adjacency matrix, be cautious of memory usage for very large graphs, 
# as the space grows quadratically with the number of vertices.
# - Ensure that you handle both directed and undirected graphs correctly 
# to maintain the symmetry of the matrix appropriately.

#=================================================================================
# Data Structures, Graph Structures, Adjacency List
#=================================================================================

# In this section, we delve into graph structures, specifically focusing on 
# the adjacency list representation. Graphs are essential for modeling 
# relationships in data, such as social networks, transportation systems, 
# and more. 

# Graph Structures
# A graph is made up of nodes (or vertices) and edges (connections between the nodes).
# Graphs can be directed (edges have a direction) or undirected (edges are bidirectional).
# There are different ways to represent graphs in programming, with the adjacency list 
# being one of the most efficient methods for sparse graphs.

# Adjacency List
# An adjacency list represents a graph as an array (or list) of linked lists or arrays.
# Each index of the array corresponds to a vertex, and each entry in the linked list 
# represents the vertices that are adjacent to that vertex.

# Example: Adjacency List Representation
# Let's create a simple graph with 4 vertices (0, 1, 2, 3) and the following edges:
# 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3

# Create an adjacency list using a dictionary where the keys are vertices 
# and the values are lists of adjacent vertices.
graph = {
    0: [1, 2],  # Vertex 0 is connected to Vertex 1 and Vertex 2
    1: [2],     # Vertex 1 is connected to Vertex 2
    2: [0, 3],  # Vertex 2 is connected to Vertex 0 and Vertex 3
    3: []       # Vertex 3 has no connections
}

# Print the adjacency list representation of the graph
print("Graph Adjacency List:")
for vertex, edges in graph.items():
    print(f"Vertex {vertex}: Edges {edges}")

# Runtime Analysis:
# - Space Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
#   Each vertex stores a list of edges, hence the total space grows with the number of edges.
# - Time Complexity for traversing all edges: O(V + E). This is efficient for sparse graphs, 
#   where E is significantly less than V^2 (as would be the case for an adjacency matrix).

# Best Case and Worst Case Scenarios:
# - Best Case: Accessing an isolated vertex (no edges), which takes O(1) time.
# - Worst Case: Traversing all vertices and edges, which takes O(V + E) time.

# Considerations When Implementing:
# 1. Choosing between an adjacency list and an adjacency matrix depends on the graph's density:
#    - Use an adjacency list for sparse graphs (fewer edges).
#    - Use an adjacency matrix for dense graphs (many edges), as it provides O(1) access 
#      to check for the existence of an edge.
# 2. Be aware of the trade-offs regarding memory usage versus time complexity.
# 3. In cases of directed graphs, ensure edges are added in the correct direction.
# 4. When implementing algorithms (e.g., Dijkstra's, BFS, DFS), be mindful of 
#    how the data structure affects the performance.

# Example Use Cases:
# - Social networks (e.g., representing friendships or connections).
# - Web page link structures (e.g., each page is a vertex, and links are edges).
# - Route mapping systems (e.g., cities as vertices and roads as edges).

# Advanced Tips:
# - Consider using a default dictionary from the collections module to simplify 
#   edge addition and avoid key errors when adding edges.
# - Implement a method to handle undirected edges by adding two directed edges 
#   (one for each direction) if the graph is undirected.
# - To optimize space for very sparse graphs, consider using a compressed data structure 
#   or a set to store edges.

from collections import defaultdict

# Example of using defaultdict for adjacency list creation
graph_defaultdict = defaultdict(list)
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3)]  # List of edges

# Adding edges to the graph
for start, end in edges:
    graph_defaultdict[start].append(end)  # For directed graph

# Print the adjacency list created using defaultdict
print("Graph Adjacency List using defaultdict:")
for vertex, edges in graph_defaultdict.items():
    print(f"Vertex {vertex}: Edges {edges}")


#=================================================================================
# Data Structures
#=================================================================================

# In this section, we focus on graph structures and specifically the incidence matrix.
# Graphs are a fundamental data structure used to represent relationships between 
# entities in various domains, such as social networks, transportation systems, and 
# web structures. An incidence matrix is one way to represent a graph using a 
# two-dimensional array.

# Graph Structures
# A graph consists of vertices (or nodes) and edges (connections between nodes).
# There are various representations for graphs, including adjacency lists, 
# adjacency matrices, and incidence matrices.

# Incidence Matrix
# An incidence matrix is a rectangular array that represents a finite graph.
# For a directed graph with n vertices and m edges, the incidence matrix has 
# n rows (vertices) and m columns (edges). Each cell indicates the relationship 
# between a vertex and an edge. 

# For directed graphs:
# - If vertex i is the tail of edge j, the entry is -1.
# - If vertex i is the head of edge j, the entry is +1.
# - If vertex i is not connected to edge j, the entry is 0.

# Example of an incidence matrix representation for a simple directed graph
# Consider a graph with 3 vertices (A, B, C) and 2 edges (e1: A -> B, e2: B -> C).

vertices = ['A', 'B', 'C']  # List of vertices
edges = ['e1', 'e2']  # List of edges

# Incidence matrix initialization for 3 vertices and 2 edges
# Rows represent vertices, columns represent edges
incidence_matrix = [
    [1, 0],  # Vertex A: Outgoing edge e1
    [-1, 1],  # Vertex B: Incoming edge e1, outgoing edge e2
    [0, -1]   # Vertex C: Incoming edge e2
]

# Printing the incidence matrix
print("Incidence Matrix:")
print("Vertices -> Edges")
for i in range(len(vertices)):
    print(f"{vertices[i]}:", incidence_matrix[i])

# Output example:
# Incidence Matrix:
# Vertices -> Edges
# A: [1, 0]
# B: [-1, 1]
# C: [0, -1]

# Runtime analysis:
# - Constructing an incidence matrix for a graph takes O(n + m) time, 
# where n is the number of vertices and m is the number of edges. 
# This is due to needing to iterate over the edges to populate the matrix.
# - Space complexity is O(n * m) for storing the matrix, which can be significant for 
# dense graphs. 

# Best and Worst Cases:
# - The best case occurs when the graph has minimal connections (sparse), leading to 
# a smaller number of edges and lower space requirements.
# - The worst case occurs with dense graphs where the number of edges approaches n^2, 
# leading to high space and time requirements for operations involving the incidence matrix.

# Use cases:
# - The incidence matrix is beneficial for algorithms that require quick edge lookups, 
# such as finding the in-degree or out-degree of a vertex.
# - It is particularly useful in network flow problems, circuit design, and 
# topological sorting.

# Potential pitfalls:
# - Incidence matrices can consume considerable memory for large graphs. 
# For very large graphs, consider using sparse representations like 
# adjacency lists or matrices.
# - Understanding the indexing of the matrix is crucial, especially when 
# working with directed graphs to ensure correct interpretations of entries.

# Advanced tips:
# - When implementing graph algorithms (like depth-first search or Dijkstra's), 
# choose the representation (incidence, adjacency list, or matrix) based on 
# the graph's density and the operations you need to perform most frequently.
# - If a graph is dynamic (edges and vertices change frequently), consider 
# using data structures that support efficient modifications, such as an 
# adjacency list combined with a hash table for quick lookups.



#=================================================================================
# Data Structures: Specialized Data Structures
#=================================================================================

# In this section, we will discuss specialized data structures that are commonly used 
# in algorithm implementations, particularly heaps. Heaps are an important 
# type of binary tree used for efficient priority queue implementations.

# Heaps
# A heap is a specialized tree-based data structure that satisfies the heap property.
# There are two types of heaps: 
# 1. Max Heap: The value of each node is greater than or equal to the values of its children. 
# 2. Min Heap: The value of each node is less than or equal to the values of its children.
# Heaps are commonly used to implement priority queues, where the highest (or lowest) 
# priority element is served before other elements.

# Python provides a built-in library for heaps via the 'heapq' module, which implements a 
# min-heap by default. We will explore various operations that can be performed on heaps.

# Initializing a heap
import heapq  # Import the heapq module to utilize heap functionalities

# Creating an empty list to represent the heap
heap = []

# Inserting elements into the heap using heappush
# Using the heappush function to maintain the heap property
heapq.heappush(heap, 5)  # Insert 5
heapq.heappush(heap, 3)  # Insert 3
heapq.heappush(heap, 8)  # Insert 8
heapq.heappush(heap, 1)  # Insert 1
print("Heap after insertions:", heap)  # Outputs: [1, 3, 8, 5]
# Note: The smallest element (1) is at the root of the heap.

# Runtime analysis for insertion (heappush):
# - Average case: O(log n) due to the need to maintain the heap property.
# - Worst case: O(log n) when inserting into an unbalanced tree.
# - Best case: O(1) if the heap property is already satisfied.

# Removing the smallest element using heappop
# The heappop function removes and returns the smallest element (the root) from the heap
smallest_element = heapq.heappop(heap)  # Removes the smallest element
print("Removed smallest element:", smallest_element)  # Outputs: 1
print("Heap after removal:", heap)  # Outputs: [3, 5, 8]

# Runtime analysis for removal (heappop):
# - Average case: O(log n) as the heap needs to be restructured after the root removal.
# - Worst case: O(log n) similarly for restructuring.
# - Best case: O(1) if the heap is already balanced.

# Peek at the smallest element without removing it
# To peek at the smallest element, simply access the first element of the heap list
if heap:
    print("Smallest element (peek):", heap[0])  # Outputs: 3

# Use case: Heaps are widely used in algorithms such as Dijkstra's shortest path and 
# Prim's algorithm for minimum spanning trees due to their efficient priority management.

# Building a heap from an iterable
# Using heapify to convert an existing list into a heap in-place
unsorted_list = [10, 5, 3, 8, 6]
heapq.heapify(unsorted_list)  # Transform the unsorted list into a heap
print("Heap after heapify:", unsorted_list)  # Outputs: [3, 5, 10, 8, 6]

# Runtime analysis for heapify:
# - Average case: O(n) because each element is considered in a bottom-up manner.
# - Worst case: O(n) as it processes each node effectively.
# - Best case: O(n) when constructing from a complete binary tree.

# Priority Queue Implementation with Heaps
# We can implement a priority queue using the heapq module. Each element is a tuple where the 
# first element represents the priority.
priority_queue = []
heapq.heappush(priority_queue, (2, "Task 2"))  # Lower number indicates higher priority
heapq.heappush(priority_queue, (1, "Task 1"))  # Higher priority
heapq.heappush(priority_queue, (3, "Task 3"))  # Lower priority
print("Priority Queue after additions:", priority_queue)  # Outputs: [(1, 'Task 1'), (2, 'Task 2'), (3, 'Task 3')]

# Dequeuing tasks based on priority
while priority_queue:
    priority_task = heapq.heappop(priority_queue)  # Dequeue the highest priority task
    print("Dequeued Task:", priority_task)  # Outputs: (1, 'Task 1'), (2, 'Task 2'), (3, 'Task 3')

# Advanced Tip:
# When implementing heaps, consider the following:
# - Choose between a min-heap or max-heap based on the application's needs.
# - Heaps provide efficient access to the smallest or largest element, but searching 
# for arbitrary elements is not efficient (O(n)).
# - If frequent access to arbitrary elements is required, consider using additional 
# data structures (like dictionaries) to maintain mappings.
# - Remember to evaluate the trade-offs between different data structures for your specific use case.

# Potential Pitfalls:
# - Be cautious with the assumptions about the heap properties; invalidating these properties 
# can lead to unexpected results during operations.
# - Always check if the heap is empty before calling heappop to avoid IndexError.
# - Understand that heaps are not sorted; the elements can be out of order except for the root element.


#=================================================================================
# Specialized Data Structures: Heaps and Min-Heaps
#=================================================================================

# Heaps are a specialized tree-based data structure that satisfies the heap property.
# They are particularly useful for implementing priority queues, where the highest 
# (or lowest) priority elements can be accessed quickly. In this context, we will focus 
# on the min-heap structure, which allows for efficient retrieval of the minimum element.

# Definition of a Min-Heap:
# A min-heap is a binary tree where:
# - The value of each node is less than or equal to the values of its children.
# - The tree is complete, meaning all levels are fully filled except possibly for the last,
#   which is filled from left to right.

# Characteristics:
# - Insertion time complexity: O(log n)
# - Deletion (extract min) time complexity: O(log n)
# - Accessing the minimum element time complexity: O(1)
# - The worst-case scenario for both insertion and deletion occurs when the tree needs to be rebalanced.

# Example: Implementing a Min-Heap using a list
class MinHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty list to store heap elements

    def insert(self, value):
        # Insert a new value into the heap
        self.heap.append(value)  # Add value to the end of the list (heap)
        self._heapify_up(len(self.heap) - 1)  # Restore heap property

    def _heapify_up(self, index):
        # Move the newly added value up to restore the min-heap property
        parent_index = (index - 1) // 2  # Calculate the parent index
        if index > 0 and self.heap[index] < self.heap[parent_index]:  # If current value is less than parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Swap
            self._heapify_up(parent_index)  # Continue heapifying up

    def extract_min(self):
        # Remove and return the smallest value (root of the min-heap)
        if not self.heap:
            return None  # If heap is empty, return None
        min_value = self.heap[0]  # Store the minimum value to return
        last_value = self.heap.pop()  # Remove the last value in the heap
        if self.heap:  # If the heap is not empty after popping
            self.heap[0] = last_value  # Replace root with the last value
            self._heapify_down(0)  # Restore heap property
        return min_value

    def _heapify_down(self, index):
        # Move the root value down to restore the min-heap property
        smallest = index  # Assume the smallest is the root
        left_child_index = 2 * index + 1  # Calculate left child index
        right_child_index = 2 * index + 2  # Calculate right child index

        # Check if left child exists and is less than the smallest value
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        
        # Check if right child exists and is less than the smallest value
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        # If the smallest is not the root, swap and continue heapifying down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  # Swap
            self._heapify_down(smallest)  # Continue heapifying down

min_heap = MinHeap()
min_heap.insert(5)  # Insert elements into the min-heap
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)
min_heap.insert(6)

print("Min-Heap after insertions:", min_heap.heap)

min_element = min_heap.extract_min()  # Extract the minimum element
print("Extracted minimum element:", min_element)  # Outputs: 1
print("Min-Heap after extracting min:", min_heap.heap)

# Use case: Min-Heaps are used in algorithms like Dijkstra's shortest path 
# and Prim's minimum spanning tree, where the minimum element needs to be accessed frequently.

# Advanced tip:
# When implementing a heap, consider using a dynamic array (like Python lists) to store elements.
# This provides efficient access and resizing capabilities. Ensure to handle edge cases,
# such as trying to extract from an empty heap.

# Potential pitfalls:
# - Mismanaging the heap property during insertion or extraction can lead to unexpected behavior.
# - Be cautious about index calculations; off-by-one errors are common when dealing with binary trees.
# - For large datasets, be aware of the trade-offs between using a heap and other data structures,
# such as balanced binary search trees (BSTs), depending on the frequency of insertions and deletions.


#=================================================================================
# Data Structures
#=================================================================================

# In this section, we explore specialized data structures, focusing on heaps,
# particularly max-heaps. Understanding these structures is essential for 
# efficient data management and algorithm design.

# Specialized Data Structures

# Heaps
# A heap is a complete binary tree that satisfies the heap property:
# - In a max-heap, for any given node I, the value of I is greater than or 
# equal to the values of its children. This property allows for efficient retrieval
# of the maximum element.
# Heaps are commonly implemented using arrays to take advantage of the complete 
# binary tree structure without requiring additional pointers.

# Array Representation of a Max-Heap
# In a max-heap represented as an array:
# - The parent node of any node at index i is located at index (i - 1) // 2
# - The left child of a node at index i is located at index 2 * i + 1
# - The right child is located at index 2 * i + 2

# Example of a max-heap represented in an array
max_heap = [10, 9, 8, 7, 6, 5, 4]  # This array represents a max-heap

print("Max-Heap Array Representation:", max_heap)

# Best and Worst Case Time Complexity for Operations
# - Insertion: O(log n) in both best and worst cases because 
#   you may need to traverse the height of the tree to maintain the heap property.
# - Deletion (removing the maximum element): O(log n) for the same reason.
# - Accessing the maximum element (root): O(1), as it is always at the root of the heap.

# Implementing a Max-Heap
# Below is a simple implementation of a max-heap with insertion and deletion operations.

class MaxHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty heap

    def insert(self, value):
        self.heap.append(value)  # Add the new value to the end of the list
        self._heapify_up(len(self.heap) - 1)  # Restore heap property

    def _heapify_up(self, index):
        # Move the newly added element up the heap to maintain max-heap property
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Swap
            self._heapify_up(parent_index)  # Recursively heapify up

    def delete_max(self):
        if not self.heap:
            return None  # Return None if the heap is empty
        max_value = self.heap[0]  # Store the maximum value (root)
        last_value = self.heap.pop()  # Remove the last element
        if self.heap:  # If there's still an element in the heap
            self.heap[0] = last_value  # Move the last element to the root
            self._heapify_down(0)  # Restore heap property
        return max_value

    def _heapify_down(self, index):
        # Move the root element down the heap to maintain max-heap property
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Check if the left child exists and is greater than the current largest
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        # Check if the right child exists and is greater than the current largest
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        # If the largest is not the current index, swap and continue heapifying down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  # Swap
            self._heapify_down(largest)  # Recursively heapify down

# Example Usage of MaxHeap
max_heap_instance = MaxHeap()
max_heap_instance.insert(10)
max_heap_instance.insert(20)
max_heap_instance.insert(15)
max_heap_instance.insert(30)

print("Max Heap after insertions:", max_heap_instance.heap)  # Outputs the current max-heap state

# Deleting the maximum element
max_element = max_heap_instance.delete_max()
print("Deleted Maximum Element:", max_element)  # Outputs: 30
print("Max Heap after deletion:", max_heap_instance.heap)  # Current state of the heap

# Advanced Insights:
# - Heaps are crucial in implementing priority queues, where each element has a 
#   priority associated with it. They can efficiently manage tasks that need 
#   to be processed based on their priority level.
# - When implementing heaps, always consider edge cases, such as trying to 
#   delete from an empty heap or inserting duplicate values.
# - The heap property should be maintained after each insertion and deletion 
#   to ensure efficient operation.

# Potential Pitfalls:
# - Not managing the index calculations correctly can lead to index errors. 
#   Ensure you are familiar with the parent/child relationships in the heap.
# - Be cautious of the heap's structure when using it in multi-threaded environments; 
#   consider using locks or other synchronization methods to manage access.

# Summary
# Max-heaps provide a powerful way to manage data with priority, 
# allowing for efficient access to the largest elements and can be 
# leveraged in various algorithms, such as heapsort, which uses the 
# properties of heaps to sort data efficiently.

#=================================================================================
# Data Structures: Specialized Data Structures
#=================================================================================

# Specialized data structures are tailored to address specific types of problems more efficiently than general-purpose structures.
# One such example is the Disjoint Set, also known as Union-Find. This structure efficiently handles dynamic connectivity queries.
# It's widely used in algorithms related to network connectivity, clustering, and Kruskal's algorithm for Minimum Spanning Trees.

# Disjoint Set (Union-Find)
# A disjoint set is a collection of non-overlapping subsets. 
# It supports two primary operations:
# 1. Find: Determine which subset a particular element belongs to.
# 2. Union: Join two subsets into a single subset.

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))  # Each element is its own parent initially
        self.rank = [1] * size  # Rank is used for union by rank optimization

    def find(self, item):
        # Find the root of the set in which element 'item' is located.
        # Path compression is applied to flatten the structure of the tree whenever 'find' is called.
        if self.parent[item] != item:  # If the item is not its own parent
            self.parent[item] = self.find(self.parent[item])  # Recursively find the root
        return self.parent[item]  # Return the root element

    def union(self, set1, set2):
        # Perform union of two sets identified by their respective roots.
        root1 = self.find(set1)  # Find root of the first set
        root2 = self.find(set2)  # Find root of the second set

        if root1 != root2:  # Only union if they are in different sets
            # Union by rank optimization: attach smaller tree under the larger tree
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1  # Make root1 the parent of root2
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2  # Make root2 the parent of root1
            else:
                self.parent[root2] = root1  # Attach root2 to root1
                self.rank[root1] += 1  # Increment rank of the new root

# Example of using Disjoint Set
size = 10  # Initialize a disjoint set with 10 elements
disjoint_set = DisjointSet(size)

# Perform some unions
disjoint_set.union(1, 2)  # Merge sets containing 1 and 2
disjoint_set.union(2, 3)  # Merge sets containing 2 and 3
disjoint_set.union(4, 5)  # Merge sets containing 4 and 5

# Check the roots after unions
print("Root of 1:", disjoint_set.find(1))  # Should output root of the set containing 1
print("Root of 2:", disjoint_set.find(2))  # Should output root of the set containing 1 (same set as 1)
print("Root of 3:", disjoint_set.find(3))  # Should output root of the set containing 1
print("Root of 4:", disjoint_set.find(4))  # Should output root of 4 (separate set)
print("Root of 5:", disjoint_set.find(5))  # Should output root of 4 (same set as 4)

# Performance Analysis:
# The union-find data structure provides very efficient operations. 
# - The average time complexity for both find and union operations is nearly O(1) due to path compression and union by rank.
# - In the worst case, the time complexity is O(log* n), where log* is the iterated logarithm, which grows extremely slowly.
# This efficiency makes it suitable for applications in network connectivity and clustering algorithms.

# Best Practices:
# - Always implement path compression and union by rank for optimized performance.
# - Ensure the initial size of the disjoint set is adequate for all elements to avoid out-of-bounds errors.
# - When implementing algorithms like Kruskal's, use the union-find structure to efficiently manage connected components.

# Potential Pitfalls:
# - Failing to apply path compression can lead to deep trees and poor performance.
# - Mismanaging ranks during union operations can also result in inefficient tree structures.
# - Always validate inputs to ensure they are within the bounds of the initialized data structure.
