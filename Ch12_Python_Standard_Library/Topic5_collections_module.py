"""
Python Standard Library - collections module - in the Python Programming Language
=================================================================================

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
The collections module in Python's Standard Library provides specialized container datatypes that serve as alternatives to Python's general-purpose built-in containers (dict, list, set, and tuple). These specialized containers offer additional functionality and optimizations for specific use cases.

Historical context:
- The collections module was introduced in Python 2.4 (2004) as part of PEP 3100.
- It has been continuously improved and expanded in subsequent Python versions.
- Many of its data structures were inspired by similar concepts in other programming languages and computer science literature.

Significance:
- Provides efficient and Pythonic implementations of common data structures.
- Offers more specialized containers for specific use cases, improving code readability and performance.
- Implements some of the Abstract Base Classes (ABCs) for Python's container types.

Common use cases:
- Counting and tallying with Counter
- Maintaining insertion order with OrderedDict
- Defining field names for tuple subclasses with namedtuple
- Implementing queues with deque
- Creating dictionaries with default values using defaultdict

2. Syntax, Key Concepts, and Code Examples
------------------------------------------
"""

from collections import (
    Counter, defaultdict, OrderedDict, namedtuple, deque, ChainMap
)
from typing import List, Tuple, Any
import time
import random

def demonstrate_counter():
    """Demonstrate the usage of Counter."""
    # Basic usage
    c = Counter('gallahad')
    print("1. Basic Counter:", c)

    # Counting words in a sentence
    sentence = "the quick brown fox jumps over the lazy dog"
    word_counts = Counter(sentence.split())
    print("2. Word counts:", word_counts)

    # Most common elements
    print("3. Most common words:", word_counts.most_common(2))

    # Arithmetic operations
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)
    print("4. Counter addition:", c1 + c2)
    print("5. Counter subtraction:", c1 - c2)

def demonstrate_defaultdict():
    """Demonstrate the usage of defaultdict."""
    # Using int as default_factory
    d = defaultdict(int)
    words = "the quick brown fox jumps over the lazy dog".split()
    for word in words:
        d[word] += 1
    print("1. Word counts with defaultdict:", dict(d))

    # Using list as default_factory
    d = defaultdict(list)
    for i, word in enumerate(words):
        d[word].append(i)
    print("2. Word positions with defaultdict:", dict(d))

    # Custom default_factory
    def constant_factory(value):
        return lambda: value
    d = defaultdict(constant_factory('Not Available'))
    d.update(name='John', age=30)
    print("3. Custom defaultdict:", d['name'], d['gender'])

def demonstrate_ordereddict():
    """Demonstrate the usage of OrderedDict."""
    # Basic usage
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print("1. Basic OrderedDict:", od)

    # Reordering
    od.move_to_end('b')
    print("2. After moving 'b' to end:", od)

    # Comparing dictionaries
    d1 = OrderedDict([('a', 1), ('b', 2)])
    d2 = OrderedDict([('b', 2), ('a', 1)])
    print("3. d1 == d2:", d1 == d2)

    # Using as a FIFO cache
    class FIFOCache(OrderedDict):
        def __init__(self, maxsize=10):
            super().__init__()
            self.maxsize = maxsize

        def __setitem__(self, key, value):
            if key in self:
                self.move_to_end(key)
            super().__setitem__(key, value)
            if len(self) > self.maxsize:
                oldest = next(iter(self))
                del self[oldest]

    cache = FIFOCache(maxsize=3)
    for i in range(5):
        cache[i] = i
    print("4. FIFO Cache:", cache)

def demonstrate_namedtuple():
    """Demonstrate the usage of namedtuple."""
    # Basic usage
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, y=22)
    print("1. Basic namedtuple:", p, p.x, p.y)

    # Converting to dictionary
    print("2. As dictionary:", p._asdict())

    # Creating a new instance with updated values
    p2 = p._replace(x=33)
    print("3. After replace:", p2)

    # Using default values
    Person = namedtuple('Person', ['name', 'age', 'gender'], defaults=['Unknown', 0, 'Unknown'])
    print("4. With defaults:", Person())
    print("5. Partial initialization:", Person("Alice", 30))

def demonstrate_deque():
    """Demonstrate the usage of deque."""
    # Basic usage
    d = deque('abcdefg')
    print("1. Basic deque:", d)

    # Rotating
    d.rotate(2)
    print("2. After rotating right:", d)
    d.rotate(-2)
    print("3. After rotating left:", d)

    # Using as a queue
    d = deque(maxlen=3)
    for i in range(5):
        d.append(i)
    print("4. Fixed-length queue:", d)

    # Efficient removal
    d = deque([1, 2, 3, 4, 5, 2, 3])
    d.remove(2)
    print("5. After removing first occurrence of 2:", d)

def demonstrate_chainmap():
    """Demonstrate the usage of ChainMap."""
    # Basic usage
    defaults = {'color': 'red', 'user': 'guest'}
    user_prefs = {'color': 'blue'}
    cm = ChainMap(user_prefs, defaults)
    print("1. ChainMap lookup:", cm['color'], cm['user'])

    # Updating
    cm['color'] = 'green'
    print("2. After update:", cm.maps)

    # Adding new map
    new_prefs = {'shape': 'square'}
    cm2 = cm.new_child(new_prefs)
    print("3. New ChainMap:", cm2['color'], cm2['user'], cm2['shape'])

"""
3. Best Practices, Common Pitfalls, and Advanced Tips
-----------------------------------------------------
Best Practices:
1. Use Counter for counting hashable objects efficiently.
2. Prefer defaultdict over manually checking and initializing dictionary values.
3. Use OrderedDict when order of insertion is important (Python 3.7+ dicts are ordered by default).
4. Use namedtuple to create lightweight, immutable data objects.
5. Use deque for efficient insertion and deletion at both ends of a sequence.

Common Pitfalls:
1. Forgetting that Counter does not raise KeyError for missing items.
2. Modifying a namedtuple thinking it's mutable.
3. Not considering the memory overhead of OrderedDict compared to regular dict.
4. Overlooking the maxlen parameter in deque, leading to unexpected behavior.

Advanced Tips:
1. Use Counter's mathematical operations for set-like operations on multisets.
2. Leverage defaultdict's default_factory for complex initializations.
3. Use OrderedDict's move_to_end method for efficient LRU cache implementations.
4. Utilize namedtuple's _fields attribute for introspection and dynamic creation.
5. Use deque's maxlen parameter for sliding window algorithms.
"""

def advanced_counter_operations():
    """Demonstrate advanced operations with Counter."""
    c1 = Counter(a=3, b=1, c=2)
    c2 = Counter(a=1, b=2, d=3)
    
    print("1. Counter intersection:", c1 & c2)
    print("2. Counter union:", c1 | c2)
    print("3. Positive differences:", c1 - c2)
    print("4. Negative differences:", -c1)

def advanced_defaultdict_usage():
    """Demonstrate advanced usage of defaultdict."""
    def tree():
        return defaultdict(tree)

    taxonomy = tree()
    taxonomy['Animal']['Mammal']['Canine']['Dog'] = ['Labrador', 'Poodle']
    taxonomy['Animal']['Mammal']['Feline']['Cat'] = ['Siamese', 'Persian']
    
    print("Nested defaultdict structure:")
    print(dict(taxonomy))

def advanced_namedtuple_usage():
    """Demonstrate advanced usage of namedtuple."""
    # Dynamic field names
    field_names = ['x', 'y', 'z']
    Point3D = namedtuple('Point3D', field_names)
    
    # Creating a subclass
    class Point(namedtuple('Point', ['x', 'y'])):
        __slots__ = ()
        def distance(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

    p = Point(3, 4)
    print(f"Distance from origin: {p.distance()}")

def demonstrate_lru_cache():
    """Demonstrate LRU (Least Recently Used) cache using OrderedDict."""
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    print([fib(n) for n in range(10)])
    print(f"Cache info: {fib.cache_info()}")

"""
4. Integration and Real-World Applications
------------------------------------------
The collections module is widely used in various Python libraries and frameworks:

1. Django: Uses namedtuple in its ORM for efficient database queries.
2. Flask: Utilizes OrderedDict for maintaining configuration options.
3. Pandas: Uses defaultdict in its internal data structures for efficient data manipulation.

Real-world example: Task Management System
"""

class Task(namedtuple('Task', ['id', 'title', 'priority', 'completed'])):
    __slots__ = ()

    def __str__(self):
        return f"Task {self.id}: {self.title} (Priority: {self.priority}, {'Completed' if self.completed else 'Pending'})"

class TaskManager:
    def __init__(self):
        self.tasks = defaultdict(list)
        self.task_counter = Counter()

    def add_task(self, title: str, priority: str) -> None:
        task_id = len(self.task_counter) + 1
        task = Task(task_id, title, priority, False)
        self.tasks[priority].append(task)
        self.task_counter[priority] += 1

    def complete_task(self, task_id: int) -> None:
        for priority, tasks in self.tasks.items():
            for i, task in enumerate(tasks):
                if task.id == task_id:
                    completed_task = task._replace(completed=True)
                    self.tasks[priority][i] = completed_task
                    return
        raise ValueError(f"Task with id {task_id} not found")

    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        return self.tasks[priority]

    def get_task_stats(self) -> str:
        total_tasks = sum(self.task_counter.values())
        stats = [f"Total tasks: {total_tasks}"]
        for priority, count in self.task_counter.most_common():
            stats.append(f"{priority}: {count}")
        return "\n".join(stats)

def demonstrate_task_manager():
    """Demonstrate the TaskManager application."""
    tm = TaskManager()
    
    # Adding tasks
    tm.add_task("Implement login functionality", "High")
    tm.add_task("Write unit tests", "Medium")
    tm.add_task("Update documentation", "Low")
    tm.add_task("Fix critical bug", "High")
    
    # Completing a task
    tm.complete_task(2)
    
    # Displaying tasks by priority
    print("High priority tasks:")
    for task in tm.get_tasks_by_priority("High"):
        print(task)
    
    # Displaying task statistics
    print("\nTask Statistics:")
    print(tm.get_task_stats())

"""
5. Advanced Concepts and Emerging Trends
----------------------------------------
1. Type hinting: Recent Python versions have improved support for type hinting with collections.
2. Asynchronous implementations: Exploring asynchronous versions of collections for use with asyncio.
3. Immutable variations: Consideration of immutable versions of mutable collections for thread-safety.
"""

from typing import DefaultDict, OrderedDict as OrderedDictType, NamedTuple, Deque

def demonstrate_type_hinting():
    """Demonstrate type hinting with collections."""
    def process_data(data: DefaultDict[str, List[int]]) -> OrderedDictType[str, int]:
        result = OrderedDict()
        for key, values in data.items():
            result[key] = sum(values)
        return result

    data: DefaultDict[str, List[int]] = defaultdict(list)
    data['a'] = [1, 2, 3]
    data['b'] = [4, 5, 6]
    
    result = process_data(data)
    print("Processed data:", result)

class Person(NamedTuple):
    name: str
    age: int

def demonstrate_async_deque():
    """Demonstrate a concept for an asynchronous deque."""
    import asyncio

    class AsyncDeque:
        def __init__(self):
            self._deque = deque()
            self._lock = asyncio.Lock()
        
        async def append(self, item):
            async with self._lock:
                self._deque.append(item)
        
        async def popleft(self):
            async with self._lock:
                return self._deque.popleft()

    async def producer(q: AsyncDeque):
        for i in range(5):
            await q.append(i)
            await asyncio.sleep(0.1)

    async def consumer(q: AsyncDeque):
        while True:
            item = await q.popleft()
            print(f"Consumed: {item}")
            await asyncio.sleep(0.2)

    async def main():
        q = AsyncDeque()
        await asyncio.gather(producer(q), consumer(q))

    asyncio.run(main())

"""
6. FAQs and Troubleshooting
---------------------------
Q1: When should I use Counter instead of a regular dictionary?
A1: Use Counter when you need to count hashable objects and perform set-like operations on the counts.

Q2: What's the difference between dict and OrderedDict in Python 3.7+?
A2: In Python 3.7+, regular dicts maintain insertion order. OrderedDict provides additional methods like move_to_end() and is more suitable for certain use cases like implementing LRU caches.

Q3: How can I create a namedtuple with optional fields?
A3: You can use the 'defaults' parameter in the namedtuple constructor to specify default values for optional fields.

Q4: Is deque thread-safe?
A4: While individual operations on a deque are atomic, the deque itself is not fully thread-safe. For multi-threaded applications, you may need to use additional synchronization mechanisms.

Q5: How does ChainMap differ from updating dictionaries?
A5: ChainMap provides a view into multiple dictionaries without merging them. It's more memory-efficient and allows for dynamic updating of the underlying mappings.

Troubleshooting guide:
1. Issue: Counter not counting as expected
   Solution: Ensure you're using hashable objects as keys. For custom objects, implement __hash__ and __eq__ methods.

2. Issue: defaultdict raising KeyError
   Solution: This occurs when trying to access the default_factory attribute directly. Use the dict.get() method instead.

3. Issue: OrderedDict not maintaining order in Python 2
   Solution: Upgrade to Python 3. If not possible, ensure you're using collections.OrderedDict and not a regular dict.

4. Issue: namedtuple instances taking up too much memory
   Solution: Use __slots__ = () in a subclass of namedtuple to prevent the creation of a per-instance __dict__.

5. Issue: deque not bounded as expected
   Solution: Ensure you've set the maxlen parameter when initializing the deque.

"""

def demonstrate_troubleshooting():
    """Demonstrate solutions to common issues with collections."""
    
    # 1. Counter with unhashable keys
    try:
        Counter([[], []])  # This will raise a TypeError
    except TypeError as e:
        print(f"1. TypeError with unhashable keys: {e}")
        print("   Solution: Use immutable types like tuples instead of lists.")
    
    # 2. defaultdict KeyError
    d = defaultdict(list)
    try:
        print(d.default_factory['key'])  # This will raise a KeyError
    except KeyError as e:
        print(f"2. KeyError with defaultdict: {e}")
        print("   Solution: Use d.get('key', d.default_factory()) instead.")
    
    # 3. OrderedDict in Python 2 vs 3
    print("3. OrderedDict behavior:")
    print("   In Python 3.7+, regular dict maintains order.")
    print("   For earlier versions, use collections.OrderedDict explicitly.")
    
    # 4. Memory optimization for namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    
    class OptimizedPoint(Point):
        __slots__ = ()
    
    p1 = Point(1, 2)
    p2 = OptimizedPoint(1, 2)
    print(f"4. Memory usage: Point: {p1.__sizeof__()} bytes, OptimizedPoint: {p2.__sizeof__()} bytes")
    
    # 5. Bounded deque
    d = deque(maxlen=3)
    for i in range(5):
        d.append(i)
    print(f"5. Bounded deque (maxlen=3): {d}")

"""
7. Recommended Tools, Libraries, and Resources
----------------------------------------------
Tools and Libraries:
1. more-itertools: Extends itertools and includes additional collection-related utilities.
2. pyrsistent: Provides immutable variants of collections.
3. sortedcontainers: Offers sorted versions of list, dict, and set.
4. multiset: Implements a mutable set-like container that allows duplicates.
5. bidict: Provides bidirectional dictionaries.

Resources:
- "Fluent Python" by Luciano Ramalho (chapters on data structures)
- "Python Cookbook" by David Beazley and Brian K. Jones (recipes using collections)
- Python's official documentation on collections: https://docs.python.org/3/library/collections.html
- Real Python's guide on Python collections: https://realpython.com/python-collections-module/
- Raymond Hettinger's talks on Python's collections (available on YouTube)
- PEP 3100 - Miscellaneous Python 3.0 Plans (introduced collections): https://www.python.org/dev/peps/pep-3100/

8. Performance Analysis and Optimization
----------------------------------------
When working with collections, it's important to consider their performance implications, especially in large-scale applications or performance-critical code.
"""

import timeit

def performance_comparison():
    """Compare performance of different collection types."""
    
    setup = """
from collections import defaultdict, Counter
data = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    """
    
    dict_test = """
d = {}
for k, v in data:
    if k in d:
        d[k].append(v)
    else:
        d[k] = [v]
    """
    
    defaultdict_test = """
d = defaultdict(list)
for k, v in data:
    d[k].append(v)
    """
    
    counter_test = """
d = Counter()
for k, v in data:
    d[k] += v
    """
    
    print("Performance comparison:")
    print(f"1. Dict:        {timeit.timeit(dict_test, setup, number=1000000):.6f} seconds")
    print(f"2. defaultdict: {timeit.timeit(defaultdict_test, setup, number=1000000):.6f} seconds")
    print(f"3. Counter:     {timeit.timeit(counter_test, setup, number=1000000):.6f} seconds")

"""
Performance Considerations:
1. defaultdict is generally faster than manual dictionary initialization for multi-value dictionaries.
2. Counter is highly optimized for counting operations and set-like math.
3. OrderedDict has slightly higher memory usage compared to regular dict (in Python 3.7+).
4. deque offers O(1) append and pop from both ends, compared to O(n) for list.
5. namedtuple creates lightweight objects with little overhead compared to full classes.

Optimization Strategies:
1. Use the most appropriate collection for your use case to leverage built-in optimizations.
2. For large datasets, consider using generators or itertools to reduce memory usage.
3. Use Counter's most_common() method instead of sorting a dictionary by values.
4. Leverage deque for sliding window problems instead of repeatedly slicing lists.
5. Use ChainMap instead of updating dictionaries when a view of multiple dicts is sufficient.

Example of optimizing a frequently called method:
"""

def optimize_word_frequency(text: str, n: int) -> List[Tuple[str, int]]:
    """
    Optimize word frequency calculation using Counter.
    
    Args:
    text (str): Input text
    n (int): Number of top frequent words to return
    
    Returns:
    List[Tuple[str, int]]: Top n frequent words with their counts
    """
    words = text.lower().split()
    return Counter(words).most_common(n)

def demonstrate_optimization():
    """Demonstrate optimization of word frequency calculation."""
    text = "the quick brown fox jumps over the lazy dog" * 1000
    
    def naive_approach(text, n):
        words = text.lower().split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]
    
    print("Word frequency calculation:")
    
    start = time.time()
    naive_result = naive_approach(text, 5)
    naive_time = time.time() - start
    print(f"1. Naive approach: {naive_time:.6f} seconds")
    print(f"   Result: {naive_result}")
    
    start = time.time()
    optimized_result = optimize_word_frequency(text, 5)
    optimized_time = time.time() - start
    print(f"2. Optimized approach: {optimized_time:.6f} seconds")
    print(f"   Result: {optimized_result}")
    
    print(f"Speedup: {naive_time / optimized_time:.2f}x")

"""
9. How to Contribute
--------------------
To contribute to this note sheet:
1. Fork the repository containing this file.
2. Make your changes or additions.
3. Ensure all code examples are correct and follow the established style.
4. Add comments explaining new concepts or functions.
5. Update the Table of Contents if necessary.
6. Submit a pull request with a clear description of your changes.

Guidelines for contributions:
- Maintain the current format and style.
- Provide working code examples for new concepts.
- Include performance considerations for new functions.
- Add relevant references or citations for advanced topics.

When adding new sections or expanding existing ones, consider the following:
- Relevance to the main topic of the collections module in Python.
- Clarity and depth of explanations.
- Practical applicability of examples and tips.
- Up-to-date information on Python language features and best practices.

Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!
"""

def main():
    """
    Main function to demonstrate various concepts related to the collections module.
    """
    print("1. Counter Demonstration:")
    demonstrate_counter()
    
    print("\n2. defaultdict Demonstration:")
    demonstrate_defaultdict()
    
    print("\n3. OrderedDict Demonstration:")
    demonstrate_ordereddict()
    
    print("\n4. namedtuple Demonstration:")
    demonstrate_namedtuple()
    
    print("\n5. deque Demonstration:")
    demonstrate_deque()
    
    print("\n6. ChainMap Demonstration:")
    demonstrate_chainmap()
    
    print("\n7. Advanced Counter Operations:")
    advanced_counter_operations()
    
    print("\n8. Advanced defaultdict Usage:")
    advanced_defaultdict_usage()
    
    print("\n9. Advanced namedtuple Usage:")
    advanced_namedtuple_usage()
    
    print("\n10. LRU Cache Demonstration:")
    demonstrate_lru_cache()
    
    print("\n11. Task Manager Application:")
    demonstrate_task_manager()
    
    print("\n12. Type Hinting with Collections:")
    demonstrate_type_hinting()
    
    print("\n13. Troubleshooting Common Issues:")
    demonstrate_troubleshooting()
    
    print("\n14. Performance Comparison:")
    performance_comparison()
    
    print("\n15. Optimization Demonstration:")
    demonstrate_optimization()

if __name__ == "__main__":
    main()