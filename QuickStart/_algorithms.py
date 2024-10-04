# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                 Algorithms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#===============================================================================
# Algorithms, Sorting Algorithms, Bubble Sort
#===============================================================================

# In this section, we explore sorting algorithms, specifically the Bubble Sort algorithm.
# Sorting algorithms are foundational for efficient data organization, enhancing performance
# in both searching and other data manipulation tasks.
# Bubble Sort, while simple and easy to implement, has significant limitations in terms of performance
# when dealing with larger datasets, making it an educational example or suitable only for small datasets.

# Bubble Sort Algorithm Overview:
# - Bubble Sort works by repeatedly traversing the list, comparing adjacent elements, 
#   and swapping them if they are out of order. This process continues until no swaps are necessary,
#   meaning the list is sorted.
# - The name "Bubble Sort" comes from the smaller elements "bubbling" to the top of the list as the process repeats.

# Time Complexity:
# - Best Case: O(n) - When the list is already sorted, the algorithm only needs to traverse the list once.
#   This is an uncommon case and can only be achieved with the optimized version of Bubble Sort that includes
#   the 'swapped' flag to detect an early exit.
# - Average Case: O(n^2) - In a typical random list, each element needs to be compared with others,
#   leading to a quadratic number of comparisons and swaps.
# - Worst Case: O(n^2) - The worst case occurs when the list is sorted in reverse order, 
#   requiring maximum number of swaps and passes through the list.

# Space Complexity:
# - O(1) - Bubble Sort is an in-place sorting algorithm, meaning it does not require extra space 
#   proportional to the input size. Only a few auxiliary variables (like 'swapped') are needed.

# Stability:
# - Bubble Sort is stable, meaning that if two elements have the same value, they will remain 
#   in the same relative positions after sorting. This is an important feature in cases where 
#   the relative order of equal elements is significant (e.g., sorting by secondary criteria).

# Example of Bubble Sort Implementation
def bubble_sort(arr):
    # Get the length of the array to determine how many passes are required
    n = len(arr)
    
    # Outer loop represents multiple passes through the array.
    # Each pass ensures the next largest element is "bubbled" to its correct position.
    for i in range(n):
        swapped = False  # This flag helps us optimize the algorithm by stopping early if no swaps occur
        
        # The inner loop runs from the beginning of the array to the unsorted portion
        # After each pass, the largest element is guaranteed to be in its correct position
        for j in range(0, n - i - 1):
            
            # Compare the current element with the next one
            # If the current element is greater, they are swapped to ensure the larger one moves right
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap adjacent elements
                swapped = True  # Indicate that a swap has occurred, meaning the array is not yet sorted
        
        # If no swaps occurred during this pass, the array is already sorted, so we can exit early
        if not swapped:
            break  # Exit the loop early for a more efficient sort (this brings the best-case performance to O(n))

# Example array to sort
array_to_sort = [64, 34, 25, 12, 22, 11, 90]  # This array contains a mix of unordered numbers
print("Original Array:", array_to_sort)

# Perform Bubble Sort on the array
bubble_sort(array_to_sort)
print("Sorted Array:", array_to_sort)

# Detailed Insights:

# 1. The outer loop: It iterates n times, where n is the number of elements in the list.
#    In each pass, the largest unsorted element is placed in its correct position, so 
#    after i passes, the last i elements are already sorted.

# 2. The inner loop: This compares adjacent elements and swaps them if the previous element is greater
#    than the next. After each complete pass of the inner loop, the largest element moves to the end.

# 3. Early termination: The 'swapped' flag ensures that if a pass doesn't swap any elements,
#    the algorithm terminates early, reducing the number of unnecessary comparisons.
#    This makes the best-case time complexity O(n), when the array is already sorted.

# Advanced Tips:
# - Bubble Sort is inefficient for large datasets due to its O(n^2) time complexity in the average and worst cases.
#   For performance-critical applications, use more advanced algorithms like Quick Sort (O(n log n) on average) 
#   or Merge Sort (O(n log n) guaranteed).
# - Bubble Sort is, however, easy to implement and can be useful for small or nearly sorted datasets 
#   where simplicity is a priority.
# - It is also useful in scenarios where stability is a requirement and the dataset is small enough 
#   to make performance less of an issue.

# Use Cases:
# - Educational Tool: Bubble Sort is often used to introduce the concept of sorting algorithms because
#   it is easy to understand and visualize.
# - Small Datasets: It can be used in cases where the dataset is small (e.g., less than 100 elements) 
#   and performance isn't critical.
# - Stable Sorting: In cases where maintaining the relative order of equal elements is important (like 
#   sorting by multiple criteria), Bubble Sort can be used since it is a stable sorting algorithm.

# Runtime Analysis:
# - Best Case (O(n)): The algorithm stops early when the list is already sorted (thanks to the swapped flag).
# - Average and Worst Case (O(n^2)): In these cases, each element must be compared with nearly all other elements, 
#   leading to quadratic time complexity.

# Pitfalls:
# - Performance: Bubble Sort performs poorly with large datasets. Its quadratic time complexity means
#   that for larger arrays, sorting time increases dramatically. 
#   For example, sorting an array of 1,000 elements would require up to 1,000,000 comparisons.
# - Always use more efficient algorithms like Quick Sort or Python’s built-in Timsort (which is O(n log n))
#   for handling larger arrays or more complex real-world data sets.

#===============================================================================
# Algorithms, Sorting Algorithms, Selection Sort
#===============================================================================

# In this section, we will discuss selection sort, a simple comparison-based sorting algorithm.
# We will cover its mechanism, implementation, time complexity analysis, and use cases.

# Selection Sort Overview:
# Selection sort is an in-place comparison sorting algorithm that divides the input list into two parts:
# - A sorted sublist which is built from left to right.
# - An unsorted sublist which consists of the remaining elements.
# The algorithm works by repeatedly selecting the smallest (or largest, depending on sorting order) element 
# from the unsorted sublist and moving it to the sorted sublist.
# Note: Selection sort is not stable, meaning that it does not preserve the relative order of equal elements.

# Example of Selection Sort Implementation:
# Let's consider a simple list of integers that we want to sort in ascending order.
array = [64, 25, 12, 22, 11]  # The unsorted list, containing integers in arbitrary order.
print("Original Array:", array)

# Start of the selection sort algorithm:
n = len(array)  # `n` is the length of the array. This remains constant throughout the sorting process.

# Outer loop: Iterates over each element, assuming it will be placed in its correct position.
for i in range(n):
    min_index = i  # Assume the first element of the unsorted sublist is the minimum initially.
    
    # Inner loop: Finds the actual minimum element in the unsorted part of the list.
    for j in range(i + 1, n):
        # Comparison step: Check if the current element is smaller than the assumed minimum.
        if array[j] < array[min_index]:
            min_index = j  # Update min_index to the index of the new minimum element.
    
    # Swap operation: Move the found minimum element to its correct position.
    # This operation is in-place, meaning no additional memory is used.
    array[i], array[min_index] = array[min_index], array[i]  # Swap the minimum element with the first unsorted element.

print("Sorted Array:", array)  # Output: [11, 12, 22, 25, 64] - The array is now sorted in ascending order.

# Time Complexity Analysis:
# The time complexity of selection sort remains O(n^2) for all cases (best, average, and worst):
# - Outer loop runs `n` times (one for each element).
# - Inner loop runs approximately `n/2` times on average, leading to n * (n-1) comparisons.
# - Since both loops are nested, the overall time complexity is O(n^2).
# Best Case: O(n^2) - Even if the list is already sorted, the algorithm will still perform comparisons.
# Average Case: O(n^2) - Each element is compared with every other element in the list.
# Worst Case: O(n^2) - Even in reverse order, selection sort still performs n-1 comparisons for every element.

# Space Complexity:
# Space complexity is O(1), as it sorts the array in place. 
# Only a constant amount of extra space is used for variables like `min_index` and loop counters.
# Unlike algorithms like mergesort or quicksort (with recursive calls), no additional stack or heap memory is required.

# Use Cases:
# - Selection sort is easy to understand and implement, making it a good choice for educational purposes.
# - It works well for small datasets or cases where simplicity is more important than performance.
# - Since selection sort only makes O(n) swaps (compared to O(n^2) comparisons), it might be preferable in scenarios
#   where writes (like memory access or disk writes) are costly, and minimizing swaps is necessary.
# - However, it is generally unsuitable for large datasets, as more efficient algorithms (e.g., quicksort, mergesort)
#   offer better time complexities.

# Best Practices and Potential Pitfalls:
# - Selection sort is rarely used in practice for large datasets due to its O(n^2) complexity.
#   More efficient algorithms, like Timsort (Python's built-in sort) or quicksort, should be considered.
# - Another consideration is stability: Selection sort is not stable, meaning that the relative order of equal elements
#   may not be preserved after sorting. If stability is required, consider using a stable sort like mergesort.
# - Python's built-in sorting functions (sorted() or list.sort()) use Timsort, which is highly optimized and stable.
#   These are generally better for most applications in Python.

# Advanced Tip:
# If performance becomes a concern for certain parts of your program, consider using hybrid sorting techniques.
# For example, selection sort could be used for small, nearly sorted arrays as part of a larger sorting algorithm.
# Additionally, combining selection sort with algorithms like insertion sort in a hybrid manner can help optimize for specific datasets.
# Always evaluate the characteristics of your data before deciding on a sorting algorithm.


#===============================================================================
# Algorithms, Sorting Algorithms, Insertion Sort
#===============================================================================

# Sorting algorithms are essential for organizing data, enabling efficient data retrieval 
# and manipulation. Each sorting algorithm has its strengths, weaknesses, and best use cases. 
# Here, we focus on Insertion Sort, a straightforward algorithm suitable for small datasets.

# Insertion Sort Overview
# Insertion sort builds a sorted array (or list) one element at a time by comparing 
# each new element with those already sorted and inserting it into its correct position.

# Characteristics:
# - Time Complexity: O(n^2) in the worst case (when the array is sorted in reverse order)
# - Best Case: O(n) when the array is already sorted
# - Space Complexity: O(1) since it sorts in place, requiring no additional storage.
# - Stable: Yes, it maintains the relative order of equal elements.
# - Adaptive: Efficient for data that is already substantially sorted.

# Example Implementation of Insertion Sort
# An array of integers that we will sort using insertion sort.
array = [5, 2, 9, 1, 5, 6]

print("Original array:", array)  # Display the original array

# The outer loop runs from the second element (index 1) to the last element of the array
# because we assume the first element is trivially sorted.
for i in range(1, len(array)):
    key = array[i]  # The current element to be inserted into the sorted portion of the array
    j = i - 1  # Index of the last element of the sorted portion
    
    # Move elements of the sorted portion that are greater than key
    # to one position ahead of their current position.
    while j >= 0 and array[j] > key:  # As long as j is within bounds and array[j] is greater than key
        array[j + 1] = array[j]  # Shift element to the right
        j -= 1  # Move to the previous index
    
    # Insert the key in its correct position after all larger elements have been shifted
    array[j + 1] = key

print("Sorted array:", array)  # Display the sorted array

# Detailed Explanation:

# The outer loop (for i in range(1, len(array))) iterates over each element starting from index 1.
# The first element at index 0 is assumed to be sorted by default (since a single element is trivially sorted).

# Inside the loop, the 'key' variable stores the current element to be placed in the sorted portion of the array.

# The 'j' variable points to the last element in the sorted portion. We start by comparing the key with the 
# element at 'j' (the largest in the sorted portion). If it's larger, we shift it one place to the right.

# The inner while loop runs as long as j >= 0 (i.e., we haven't reached the start of the array) and 
# array[j] > key (i.e., the sorted element is larger than the key). Each iteration shifts elements to the right 
# until the correct spot for 'key' is found. Finally, we insert the key in the correct position by setting array[j + 1] = key.

# Runtime Analysis:
# - The worst-case scenario occurs when the array is sorted in descending order. In this case, for each element, we 
#   must shift all previously sorted elements, resulting in n*(n-1)/2 comparisons, leading to O(n^2) time complexity.
# - The best case occurs when the array is already sorted. In this case, the while loop is never entered, resulting 
#   in only n comparisons, leading to O(n) time complexity.
# - Average case: O(n^2) as, on average, each element will need to be inserted somewhere in the middle of the sorted portion.

# Space Complexity:
# - Insertion sort has a space complexity of O(1) since it operates in place, meaning it does not require 
#   additional storage beyond the input array.

# Use Cases:
# - Insertion sort is particularly efficient for small datasets or nearly sorted datasets, where the adaptive nature 
#   (best case O(n)) becomes an advantage.
# - It is commonly used in practice for small arrays (often as part of hybrid sorting algorithms like Timsort, 
#   where insertion sort is applied to small partitions).
# - Insertion sort can also be useful in scenarios where stability is required (i.e., when maintaining the relative 
#   order of equal elements is essential).

# Tips for Implementation:
# - Ensure to handle edge cases, such as arrays with fewer than two elements, where the function should return 
#   the array as is.
# - Insertion sort's simplicity and in-place sorting make it a preferred choice for small datasets, 
#   but it scales poorly for larger datasets due to its O(n^2) time complexity.
# - Consider using insertion sort within hybrid algorithms. For example, many real-world sorting functions (such 
#   as Python’s built-in sort) use insertion sort for small sections of data, where it outperforms more complex 
#   algorithms like quicksort.
# - Be mindful of integer overflow when implementing in languages that have fixed integer limits, although this is 
#   not a concern in Python due to its handling of arbitrarily large integers.
# - Lastly, remember to take advantage of built-in sorting functions if available in your environment, as these are 
#   often optimized with advanced techniques like Timsort, which is based on insertion sort and mergesort.

# Best Practices:
# - Always check for edge cases in sorting functions, like arrays with a single element or already sorted arrays.
# - Use insertion sort when dealing with nearly sorted data, as it performs close to linear in such cases.
# - If performance is critical and you are dealing with large datasets, consider using more efficient algorithms 
#   like mergesort or quicksort. Alternatively, break the problem into smaller subproblems where insertion sort shines.


#===============================================================================
# Algorithms, Sorting Algorithms, Merge Sort
#===============================================================================

# Sorting algorithms are essential for organizing data in a specific order.
# Merge Sort is one of the most efficient sorting algorithms, leveraging the
# divide-and-conquer paradigm. It works by recursively dividing the list into
# smaller sublists until each contains a single element, then merging those
# sublists to produce the final sorted list.

# Key Characteristics of Merge Sort:
# - Time Complexity: O(n log n) in the best, average, and worst cases.
#   This is due to the divide-and-conquer approach that recursively splits the list
#   and performs log(n) merging steps for n elements.
# - Space Complexity: O(n) due to the need for temporary arrays to store the merged
#   results, unlike in-place algorithms like Quick Sort.
# - Stability: Merge Sort is stable, meaning that equal elements retain their relative
#   positions, which can be important for certain data sorting scenarios.

# Example: Merge Sort Implementation
def merge_sort(arr):
    # Base case: If the array contains one or zero elements, it's already sorted
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2  # The middle index for splitting the array
        
        # Recursively split the array into left and right halves
        left_half = arr[:mid]  # Left half contains elements from the start to mid
        right_half = arr[mid:]  # Right half contains elements from mid to the end

        # Recursive sorting of the two halves
        merge_sort(left_half)  # Sort the left half recursively
        merge_sort(right_half)  # Sort the right half recursively

        # Initialize pointers for left_half (i), right_half (j), and the main array (k)
        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            # Compare elements from both halves to maintain sorted order
            if left_half[i] < right_half[j]:
                # If the left element is smaller, place it in the main array
                arr[k] = left_half[i]
                i += 1  # Move to the next element in left_half
            else:
                # Otherwise, place the right element in the main array
                arr[k] = right_half[j]
                j += 1  # Move to the next element in right_half
            k += 1  # Move to the next position in the main array

        # If there are any remaining elements in left_half, copy them to the main array
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Similarly, copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Use case: Sorting a list of numbers
numbers = [38, 27, 43, 3, 9, 82, 10]  # Example unsorted list
print("Unsorted numbers:", numbers)

# Apply merge sort to the list
merge_sort(numbers)

# Output the sorted result
print("Sorted numbers:", numbers)  # Expected Output: [3, 9, 10, 27, 38, 43, 82]

#===============================================================================
# Explanation of Runtime Analysis
#===============================================================================
# Merge Sort has a time complexity of O(n log n) across all cases:
# - Best Case: O(n log n), even if the array is already sorted. Splitting and merging
#   operations are still required.
# - Average Case: O(n log n), as the algorithm performs consistent splits and merges.
# - Worst Case: O(n log n), unlike other algorithms like Quick Sort, where certain
#   input arrangements (e.g., already sorted) can degrade performance.

# Merge Sort remains one of the few algorithms with such consistent runtime, which is
# critical for handling large datasets where performance predictability is key.

#===============================================================================
# Additional Considerations and Best Practices
#===============================================================================
# When implementing Merge Sort, keep in mind:
# - Stability The fact that Merge Sort preserves the order of equal elements is
#   useful for sorting datasets where stability is a concern, such as when sorting
#   records by multiple fields.
# - Memory Overhead Merge Sort's O(n) space complexity arises from the need to
#   allocate temporary arrays during merging. This can be an issue for systems with
#   memory constraints.
# - Applications Merge Sort is well-suited for sorting linked lists, where pointer
#   manipulation is preferred over in-place sorting.

#===============================================================================
# Advanced Tips and Uncommon Insights
#===============================================================================
# - Iterative Merge Sort Merge Sort can be implemented in a non-recursive fashion
#   (iteratively), which avoids issues of stack overflow with deep recursion. Instead of
#   recursively splitting the array, iteratively merge subarrays of increasing size.
# - Hybrid Sorting Algorithms For smaller subarrays, switching to a simpler algorithm
#   like insertion sort can improve performance. Insertion sort performs better on small
#   datasets due to lower constant factors, even though its time complexity is O(n^2).

# Example of a Hybrid Approach:
# - Modify Merge Sort to switch to insertion sort when subarray size is less than a
#   certain threshold, improving performance in real-world scenarios where the dataset
#   contains small partitions.

# This hybrid approach is used in practical implementations such as Timsort, which
# is the default sorting algorithm in Python. Timsort combines the efficiency of Merge
# Sort and insertion sort, optimizing for real-world data.



#===============================================================================
# Algorithms, Sorting Algorithms, Quick Sort
#===============================================================================

# Sorting algorithms are crucial for organizing data, enabling faster searches, 
# improved data presentation, and optimized storage use. Quick Sort stands out 
# for its efficiency and wide application in sorting large datasets.

# The core principle of Quick Sort is the divide-and-conquer paradigm. By recursively 
# dividing the data into smaller subsets around a selected 'pivot', the algorithm 
# achieves faster sorting compared to simple iterative methods like Bubble Sort.

# Steps involved in Quick Sort:
# 1. Choose a 'pivot' element from the array. The choice of pivot affects performance.
# 2. Partition the array into two sub-arrays: elements smaller than the pivot 
#    and elements greater than the pivot.
# 3. Recursively apply the process to the sub-arrays.
# 4. Merge the sorted sub-arrays into the final sorted array.

# The performance of Quick Sort largely depends on the choice of pivot and 
# the partitioning scheme used.

# Basic Implementation of Quick Sort:

def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are inherently sorted.
    if len(arr) <= 1:
        return arr
    
    # Pivot selection: picking the middle element provides a fair division 
    # in most cases, avoiding worst-case scenarios (like already sorted arrays).
    pivot = arr[len(arr) // 2]
    
    # Partitioning: we create three partitions:
    # 1. 'left' for elements smaller than the pivot.
    # 2. 'middle' for elements equal to the pivot (handles duplicates).
    # 3. 'right' for elements greater than the pivot.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursive sorting: applying quick_sort on the left and right partitions
    # ensures that we sort the sub-arrays before merging them.
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
array_to_sort = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(array_to_sort)
print("Sorted Array using Quick Sort:", sorted_array)

# Output: Sorted Array using Quick Sort: [1, 1, 2, 3, 6, 8, 10]

# Run Time Analysis:
# - Best and average case time complexity: O(n log n).
#   In the average case, the pivot divides the array in half at each step.
#   The logarithmic factor comes from the depth of recursion (dividing in half).
# - Worst case time complexity: O(n^2). This occurs when the pivot consistently
#   results in unbalanced partitions, such as in an already sorted or reverse-sorted array.

# Best Case:
# - The best case occurs when the pivot divides the array into two equal-sized parts 
#   on each recursion. In this case, the number of comparisons is minimized.

# Worst Case:
# - The worst case occurs when the pivot is always the smallest or largest element,
#   resulting in unbalanced divisions (i.e., one sub-array is empty). 
#   For instance, if the input array is already sorted.

# Key considerations for improving Quick Sort performance:
# 1. Randomized Pivoting: Randomly selecting a pivot element can prevent worst-case performance.
# 2. Median-of-Three Pivoting: Choose the pivot as the median of the first, middle, and last elements 
#    to ensure better partitioning for nearly sorted arrays.
# 3. Switch to Insertion Sort: For small arrays (typically 10 elements or fewer), Insertion Sort 
#    is faster and avoids the overhead of recursion.

# Advanced Insight:
# Quick Sort's partitioning strategy is central to its efficiency. A good partitioning scheme 
# minimizes the number of swaps and comparisons needed, and smaller recursive calls result 
# in better memory utilization, especially in the in-place version.

# In-Place Quick Sort Implementation:
# In this variation, the array is sorted without using extra space for new sub-arrays. 
# Instead, indices are used to track the partitions, making it more space-efficient (O(log n) space complexity).

def in_place_quick_sort(arr, low, high):
    # Recursive case: sort the sub-arrays between low and high indices
    if low < high:
        # Partition the array and find the correct position of the pivot
        pi = partition(arr, low, high)
        
        # Recursively apply the sorting to the left and right sub-arrays
        in_place_quick_sort(arr, low, pi - 1)  # Left sub-array
        in_place_quick_sort(arr, pi + 1, high)  # Right sub-array

# Partitioning function: handles the in-place rearrangement of elements
def partition(arr, low, high):
    # Choosing the last element as the pivot
    pivot = arr[high]
    
    # 'i' is the index for elements smaller than the pivot
    i = low - 1
    
    # Traverse the array, rearranging elements based on the pivot
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than the pivot
            i += 1  # Move the boundary of smaller elements to the right
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements to maintain order
    
    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the partition index where the pivot is placed
    return i + 1

# Example usage:
array_to_sort_in_place = [3, 6, 8, 10, 1, 2, 1]
in_place_quick_sort(array_to_sort_in_place, 0, len(array_to_sort_in_place) - 1)
print("In-Place Sorted Array using Quick Sort:", array_to_sort_in_place)

# Output: In-Place Sorted Array using Quick Sort: [1, 1, 2, 3, 6, 8, 10]

# Key Performance Considerations:
# - In-Place Quick Sort is more space-efficient than the standard version, 
#   using O(log n) additional space due to recursion rather than creating new sub-arrays.
# - While the time complexity remains the same (O(n log n) average case, O(n^2) worst case),
#   the in-place variant is more suitable for systems with limited memory.
# - As with the standard Quick Sort, careful pivot selection mitigates the risk of worst-case performance.

# Takeaway:
# Quick Sort is highly efficient, but its success hinges on good pivot selection and partitioning.
# For practical use, combining randomized pivoting with in-place sorting offers excellent 
# performance across different datasets, making Quick Sort a versatile choice in software development.


#===============================================================================
# Algorithms, Sorting Algorithms, Heap Sort
#===============================================================================

# In this section, we explore heap sort, a popular comparison-based sorting algorithm.
# Heap sort is particularly notable for its efficiency and ability to sort in-place.

# Heap Sort Overview:
# Heap sort leverages a data structure called a heap, specifically a binary heap,
# which allows for efficient retrieval of the largest (or smallest) element.
# The process consists of two main phases:
# 1. Building a max heap from the input data.
# 2. Repeatedly extracting the maximum element from the heap and rebuilding the heap 
# until all elements are sorted.

# Time Complexity:
# - Best Case: O(n log n) - Occurs when the input is already sorted, as heapify still processes each level.
# - Average Case: O(n log n) - Consistent time complexity as the heap must be built and elements extracted.
# - Worst Case: O(n log n) - No worse behavior due to the nature of heap operations.

# Space Complexity:
# - O(1) - Heap sort is an in-place sorting algorithm, meaning it requires only a constant amount of additional memory.

# Implementation:
import heapq  # Importing heapq for heap operations

# Example array to be sorted
array = [12, 11, 13, 5, 6, 7]

print("Original array:", array)

# Step 1: Build a max heap
# In a max heap, the parent node is always greater than its children.
# We start heapification from the last non-leaf node and move upwards.
# This ensures the heap property is maintained as we process each node.
def build_max_heap(arr):
    n = len(arr)
    # Start from the last parent node and heapify each node
    # n//2 - 1 is the last parent node in a zero-indexed array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# The heapify function ensures the subtree rooted at index 'i' is a max heap.
# A max heap means the root node is larger than both of its children.
# We recursively enforce this property by ensuring that if a swap is made, 
# we reheapify the affected subtree.
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Compare left child with root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare right child with largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

# Build the max heap from the original array
build_max_heap(array)
print("Max heap:", array)

# Step 2: Extract elements from the heap one by one.
# After extracting the maximum element, we place it at the end of the array
# and heapify the root to maintain the max heap property in the reduced array.
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    build_max_heap(arr)

    # One by one extract elements from the heap
    # After each extraction, we reduce the size of the heap (by i)
    # and heapify the root to restore the heap property.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
        heapify(arr, i, 0)  # Call heapify on the reduced heap

# Perform heap sort on the array
heap_sort(array)
print("Sorted array:", array)

# Use case:
# Heap sort is useful for large datasets and scenarios where a stable sorting algorithm is not required.
# It is particularly effective in environments with limited memory since it operates in-place.

# Advanced tip:
# While heap sort has a consistent time complexity of O(n log n), it may not be the fastest in practice
# due to cache inefficiencies compared to algorithms like quicksort. Always profile sorting 
# algorithms based on the context in which they are used (data size, memory constraints, etc.).
# When implementing, consider using a priority queue (implemented via a heap) 
# if you're sorting partially sorted data, as it can improve efficiency in some cases.

# Potential pitfalls:
# Ensure that the heapify function correctly maintains the max heap property after every extraction.
# Debugging heap sort can be tricky; carefully verify the indices and swap operations.
# It may also be beneficial to implement a visual representation of the heap structure to aid understanding.

#=#======================================================================================================================================================================
# Algorithms, Sorting Algorithms, Counting Sort
#===============================================================================

# Sorting algorithms are critical in data processing, allowing efficient access and manipulation.
# Counting Sort, unlike comparison-based sorts (e.g., Quick Sort, Merge Sort), leverages the properties of the data 
# (specifically integers within a known range) to achieve linear time complexity under certain conditions.

# Counting Sort works well for small, non-negative integer ranges, where the range of possible values (k) 
# is not significantly larger than the number of input elements (n). 
# It achieves linear time by avoiding comparisons between elements, instead relying on counting their occurrences.

# Example input array: Mixed, small-range integer values.
input_array = [4, 2, 2, 8, 3, 3, 1]
print("Input Array:", input_array)

# Step 1: Determine the range of input values
# The algorithm starts by identifying the minimum and maximum values in the input.
# This helps set up the counting array to accommodate all possible input values.
max_value = max(input_array)  # Find the maximum value, used to size the counting array.
min_value = min(input_array)  # Find the minimum value, useful for handling arrays with negative integers.
range_of_elements = max_value - min_value + 1  # Calculate range, +1 to accommodate both bounds inclusively.
# The size of the counting array is proportional to the range of elements (max - min + 1).

# Important to note:
# For large ranges, counting arrays can consume significant memory, 
# which might offset the linear time complexity benefit in terms of space.
print("Range of elements:", range_of_elements)

# Step 2: Initialize a count array to zero
# The count array is created with size equal to the range of input values, and it will store 
# the frequency of each number in the input array.
count_array = [0] * range_of_elements  # Prepares the count array to store the frequency of each element.
print("Initialized Count Array:", count_array)

# Step 3: Count occurrences of each element
# We traverse the input array, incrementing the corresponding index in the count array.
for number in input_array:
    count_array[number - min_value] += 1  # Adjust for min_value to support arrays with negative numbers.
# This operation runs in O(n), as it involves a single pass through the input array.
print("Count Array after counting occurrences:", count_array)

# Step 4: Calculate the cumulative count
# Cumulative counting helps place the elements in the correct position in the final sorted array.
for i in range(1, len(count_array)):
    count_array[i] += count_array[i - 1]  # Summing up counts from left to right.
# The cumulative count array effectively tells us where each element should go in the sorted array.
# This step also runs in O(k), where k is the size of the counting array (range of elements).
print("Cumulative Count Array:", count_array)

# Step 5: Build the output sorted array
# Using the cumulative count, we place elements from the original array into the output sorted array.
# Traversing the input array in reverse order preserves the stability of the sort.
output_array = [0] * len(input_array)  # Prepare output array to store sorted elements.
for number in reversed(input_array):  # Reverse traversal ensures stable sorting.
    output_array[count_array[number - min_value] - 1] = number  # Place element at correct sorted position.
    count_array[number - min_value] -= 1  # Decrement count after placing element.
# The reverse traversal ensures that elements with the same value appear in the same order as in the input array.
# This guarantees Counting Sort is stable, an important property for certain applications (e.g., radix sort).
print("Output Sorted Array:", output_array)

# Runtime Analysis:
# Time complexity: O(n + k), where n is the size of the input array and k is the range of the input values.
# The linear time is achieved by leveraging the input's properties rather than comparing elements.
# Best, average, and worst case time complexities are all O(n + k), as Counting Sort processes each element in the array.
# This consistency makes Counting Sort predictable and efficient for specific datasets.

# Space Complexity:
# O(k + n) due to the count array (size k) and the output array (size n). 
# This can become a limitation if the range of elements is significantly larger than the number of elements.

# Example Use Cases:
# 1. Counting Sort is ideal for sorting a set of grades (e.g., 0-100) where the input range is known and limited.
# 2. It also works for sorting data like ages or categories where elements fall within a small range.

# Key Insights for Senior Engineers:
# - Always verify the input range before deciding to use Counting Sort. If the range (k) is much larger than the input size (n), 
#   the space complexity of Counting Sort can become prohibitive.
# - When sorting larger integers or floating-point numbers, consider alternative algorithms like Quick Sort or Merge Sort.
# - Counting Sort can be a precursor to Radix Sort, which works by applying Counting Sort at each digit level for more complex data types.

#===============================================================================
# Algorithms, Sorting Algorithms, Radix Sort
#===============================================================================

# In this section, we delve into sorting algorithms, with a focus on Radix Sort.
# Sorting algorithms are fundamental in computer science for organizing data in a specific order,
# which facilitates efficient searching and data manipulation. Understanding the characteristics,
# time complexity, and best practices of sorting algorithms is crucial for optimizing performance.

# Common sorting algorithms include:
# 1. Bubble Sort
# 2. Selection Sort
# 3. Insertion Sort
# 4. Merge Sort
# 5. Quick Sort
# 6. Heap Sort
# 7. Radix Sort (focus of this section)

# Radix Sort
# Radix Sort is a non-comparative integer sorting algorithm that sorts numbers by processing 
# individual digits. It is particularly effective for sorting large numbers or data with a fixed 
# range of integer keys. It works by sorting the data in multiple passes based on each digit's significance.

# Key Characteristics:
# - Time Complexity:
#   - Best Case: O(nk)
#   - Average Case: O(nk)
#   - Worst Case: O(nk)
#   Here, 'n' is the number of elements and 'k' is the number of digits in the largest number.
# - Space Complexity: O(n + k) for auxiliary storage, where 'k' is the range of the digit values.
# - Stable: Yes, Radix Sort preserves the order of equal elements.

# Implementation Steps:
# 1. Determine the maximum number in the array to find the number of digits.
# 2. Perform counting sort on each digit, starting from the least significant digit (LSD) to the most significant digit (MSD).

# Example implementation of Radix Sort

def counting_sort(arr, exp):
    """
    Counting sort function to sort elements based on a specific digit.
    The 'exp' parameter represents the current digit's significance (units, tens, etc.).
    
    - Time Complexity: O(n) where 'n' is the number of elements in the array.
    - Space Complexity: O(n + 10) due to the auxiliary 'output' and 'count' arrays.
    
    This function is integral to Radix Sort as it ensures stable sorting of digits without comparisons.
    """

    n = len(arr)  # Get the number of elements in the array
    output = [0] * n  # Output array to store sorted elements temporarily
    count = [0] * 10  # Initialize count array for digit values (0-9)

    # Step 1: Store the count of occurrences of each digit
    for i in range(n):
        index = arr[i] // exp  # Extract the relevant digit using the 'exp' divisor
        count[index % 10] += 1  # Count how many times each digit occurs

    # Step 2: Modify count so that each position contains the actual position of the digit in the output array
    # This step converts the count array to a cumulative count array, which ensures stable sorting.
    for i in range(1, 10):
        count[i] += count[i - 1]  # Accumulate the count

    # Step 3: Build the output array by placing elements in their sorted positions
    # We traverse the array from the end to maintain stability in case of equal digits
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]  # Place element at its correct position
        count[index % 10] -= 1  # Decrease the count after placing the element

    # Step 4: Copy the sorted output array back into the original array 'arr'
    for i in range(n):
        arr[i] = output[i]  # Update original array with sorted values

def radix_sort(arr):
    """
    Radix sort implementation. Sorts an array of non-negative integers using digit-based sorting.
    
    Radix Sort is efficient for integers with fixed-width digits and performs sorting by 
    processing one digit at a time from least significant to most significant.

    - Time Complexity: O(nk), where 'n' is the number of elements and 'k' is the number of digits in the largest element.
    - Space Complexity: O(n + k), due to auxiliary arrays and handling of digit positions.

    Edge Cases:
    - Empty list: Radix Sort handles it as there’s nothing to sort.
    - Uniform data (e.g., [1, 1, 1]): Performs well as the sort stabilizes without significant iterations.
    """

    # Step 1: Find the maximum number to determine the number of digits to process
    max_num = max(arr)  # The number of digits in 'max_num' dictates how many passes are needed

    exp = 1  # We start with the least significant digit (units place)

    # Step 2: Perform counting sort for each digit, moving from least significant to most significant
    # The loop continues until we’ve processed all digits (exp > max_num ensures all digits are handled)
    while max_num // exp > 0:
        counting_sort(arr, exp)  # Sort elements based on the current digit
        exp *= 10  # Move to the next more significant digit (units -> tens -> hundreds)

# Example input for Radix Sort
arr = [170, 45, 75, 90, 802, 24, 2, 66]  # A mix of multi-digit and single-digit numbers
print("Original Array:", arr)  # Output before sorting

# Perform Radix Sort
radix_sort(arr)  # Sorts the array using Radix Sort

# Display the sorted array
print("Sorted Array:", arr)  # Outputs: [2, 24, 45, 66, 75, 90, 170, 802]

# =======================================================================================================================================================================
# Use cases for Radix Sort:
# - Efficient for sorting large datasets where integer keys are prevalent and the number of digits is manageable.
# - Frequently used in database management systems or when sorting large datasets with integer identifiers.
# - Suitable when all numbers have a fixed range (e.g., [0-9999]).

# Advanced insights:
# - Although Radix Sort's time complexity is O(nk), where 'k' is the number of digits, it performs well when 'k' is small,
#   making it a good alternative to comparison-based sorts (O(n log n)).
# - The sort's stability is crucial when used as part of a larger sorting system where maintaining order matters (e.g., sorting names after sorting by ID).
# - While Radix Sort uses Counting Sort internally, its efficiency depends on the data distribution. Sparse or widely varying data might degrade its performance due to large count arrays.
# - One optimization is limiting the range of 'k' if data values have a known limit, thus avoiding unnecessary passes for digits that are insignificant.

# Potential pitfalls:
# - Radix Sort does not handle negative numbers directly; consider splitting the array into positive and negative values,
#   then sort them separately and merge the results (negatives in reverse).
# - The performance degrades if 'k', the number of digits, becomes excessively large, leading to multiple passes and higher memory overhead.
# - Memory usage should be monitored, as large auxiliary arrays can lead to performance hits, especially with high 'k' values.

# When implementing Radix Sort:
# - Always verify input data is non-negative integers for simplicity. Modifications are needed for signed integers or floating points.
# - Test against edge cases such as empty arrays, single-element arrays, and arrays with repeated elements.
# - Understand that while Radix Sort is optimal in certain scenarios, other algorithms (like Quick Sort) might be preferable for general-purpose sorting.



#===============================================================================
# Algorithms, Sorting Algorithms, Bucket Sort
#===============================================================================

# In this section, we will delve into sorting algorithms, focusing on bucket sort.
# Sorting algorithms are essential for organizing data efficiently, which can 
# significantly affect the performance of other algorithms that operate on 
# sorted data, such as search algorithms.

# Bucket Sort
# Bucket sort is a distribution-based sorting algorithm that is particularly 
# effective for uniformly distributed data. It works by dividing the data 
# into several "buckets," sorting each bucket individually, and then 
# combining the sorted buckets to form the final sorted list.

# The basic steps of bucket sort are:
# 1. Create an empty array of buckets.
# 2. Distribute the input elements into the buckets based on a defined range.
# 3. Sort each bucket individually (using another sorting algorithm).
# 4. Concatenate the sorted buckets to get the final sorted array.

# Example usage:
import random

# Step 1: Create a random list of numbers
data = [random.uniform(0, 100) for _ in range(10)]  # Generate 10 random numbers between 0 and 100
print("Unsorted Data:", data)

# The use of `random.uniform` here ensures that we generate floating-point numbers between 0 and 100.
# Floating-point numbers are typically well-suited for bucket sort, as the algorithm is designed
# for use cases where numbers are distributed across a continuous range.

# Step 2: Implement bucket sort
def bucket_sort(data):
    # Create 10 empty buckets for the range 0-100
    # We are assuming here that the input values fall within the range [0, 100).
    # Each bucket will be responsible for a range of size 10 (0-9.99, 10-19.99, ..., 90-99.99).
    buckets = [[] for _ in range(10)]
    
    # Distribute the elements into buckets
    for number in data:
        # Dividing by 10 gives an index between 0 and 9 based on which range the number falls into.
        # Example: a number like 24.5 will go into the 2nd bucket (index 2).
        index = int(number // 10)  
        buckets[index].append(number)  # Place the number in the corresponding bucket
    
    # Step 3: Sort individual buckets and concatenate
    sorted_data = []
    
    # We are using Python's built-in `sorted()` function here to sort each bucket.
    # This function uses Timsort, which has a time complexity of O(n log n).
    for bucket in buckets:
        sorted_data.extend(sorted(bucket))  # Sort each bucket and extend the sorted_data list

    return sorted_data

# Call the bucket_sort function and display the sorted data
sorted_data = bucket_sort(data)
print("Sorted Data:", sorted_data)

#===============================================================================================
# Detailed Explanation of Bucket Sort Workflow
#===============================================================================================

# The input data is first distributed across multiple buckets. The range of each bucket
# is determined based on the input's expected range. For this example, we assume all 
# numbers are between 0 and 100, and we create 10 buckets, each corresponding to a range 
# of 10 units (e.g., bucket 0 contains numbers from 0 to 9.99, bucket 1 from 10 to 19.99, etc.).

# Each bucket contains a subset of the data, which is then sorted individually.
# Once all the buckets are sorted, we concatenate them to form the final sorted array.

#===============================================================================================
# Runtime Analysis
#===============================================================================================
# - Best Case: O(n + k)
#   This occurs when the input is uniformly distributed, and each bucket contains a small number 
#   of elements, making the sorting of each bucket trivial. `n` is the total number of input elements, 
#   and `k` is the number of buckets.

# - Average Case: O(n + k)
#   This is the most common scenario under the assumption that the data is uniformly distributed 
#   across the buckets, and sorting each bucket can be done efficiently.

# - Worst Case: O(n^2)
#   The worst case occurs when all elements are placed into a single bucket, reducing the problem to 
#   sorting `n` elements using a suboptimal sorting algorithm like insertion sort, which has O(n^2) 
#   complexity for the worst case.

#===============================================================================================
# Best Practices
#===============================================================================================
# 1. Uniform Distribution: Bucket sort is most effective when the input data is uniformly distributed
#    across a known range. If the data is heavily skewed, many buckets may remain empty, leading to inefficiencies.
# 2. Number of Buckets: Choosing the right number of buckets is essential. Too few buckets lead to 
#    excessive sorting within each bucket, while too many buckets may waste memory and time in handling empty buckets.
# 3. Combining with Other Algorithms: Often, a more efficient sorting algorithm like quicksort or mergesort 
#    can be used to sort individual buckets, depending on the characteristics of the data.

#===============================================================================================
# Potential Pitfalls
#===============================================================================================
# - Non-uniform data: If the input data is not uniformly distributed, some buckets may contain many elements, 
#   while others are almost empty, leading to inefficient sorting. This would degrade the performance to O(n^2) 
#   in extreme cases.
# - Range assumptions: The algorithm assumes prior knowledge of the input data's range. If the range is 
#   unknown or miscalculated, the bucket distribution could become imbalanced.
# - Bucket Overflows: If the data range is too wide, you may need too many buckets, leading to memory overhead.

#===============================================================================================
# Use Cases
#===============================================================================================
# - Floating-point numbers: Sorting floating-point numbers uniformly distributed over a range is a 
#   common application for bucket sort, making it ideal for tasks like grading exams or processing 
#   measurements within a fixed interval.
# - Parallel Processing: Bucket sort can be parallelized effectively. Each bucket can be processed 
#   independently on a different thread or processor core, making it suitable for large datasets 
#   processed on multi-core systems.

#===============================================================================================
# Advanced Tip
#===============================================================================================
# - Parallelizing the Sorting Step: If dealing with very large datasets, consider parallelizing the sorting 
#   of individual buckets. Python’s `multiprocessing` module or frameworks like Dask or Ray can be used 
#   to distribute the sorting tasks across multiple cores, reducing the overall sorting time.

# - Dynamic Bucket Allocation: Instead of predefining bucket ranges, dynamically adjust the number 
#   and size of buckets based on the actual distribution of input data. This adaptive strategy can 
#   mitigate inefficiencies in cases where the data distribution is not perfectly uniform.



#===============================================================================
# Algorithms, Sorting Algorithms, Shell Sort
#===============================================================================

# In this section, we explore the Shell Sort algorithm in detail, focusing on how it works,
# its runtime characteristics, and considerations when implementing it in practice.

# Shell Sort is a comparison-based, in-place sorting algorithm, making it an extension
# of the simpler insertion sort. The key enhancement here is that Shell Sort compares
# and swaps elements that are far apart initially, which helps to reduce large-scale 
# disorder more quickly. The gap between elements being compared gets progressively
# smaller as the algorithm runs, culminating in a final pass that uses insertion sort
# on elements that are already partially sorted.

#===============================================================================
# Function to perform Shell Sort
def shell_sort(arr):
    # The length of the array determines the number of elements to sort
    n = len(arr)  
    
    # The gap starts as half the length of the array and reduces by half in each iteration
    # Using n//2 is a common choice for the initial gap, but other sequences can be explored
    gap = n // 2  
    
    # The outer loop continues until the gap becomes 0, meaning the final pass is an
    # insertion sort with gap = 1, ensuring that the array is fully sorted.
    while gap > 0:
        # Perform a gapped insertion sort for this gap size.
        # Starting from index `gap`, move through the array, treating the elements
        # gap-distance apart as part of a sublist.
        for i in range(gap, n):
            # Store the element at index `i` in `temp` to compare with earlier elements
            temp = arr[i]
            
            # The index `j` tracks the position within the sublist as we move backward
            # to find the correct spot for `temp`.
            j = i
            
            # Continue shifting elements until the correct location for `temp` is found.
            # This loop checks whether the element at index `j-gap` is greater than `temp`,
            # and if so, moves that element up one position.
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]  # Shift larger element to the right
                j -= gap  # Move to the next position to the left (gap distance away)
            
            # After the shifting is done, insert the `temp` element in its correct position.
            arr[j] = temp
        
        # After completing one pass with the current gap, reduce the gap size by half.
        # Eventually, the gap becomes 1, and the final pass ensures the list is fully sorted.
        gap //= 2

#===============================================================================
# Example array to sort using Shell Sort
# This is a simple list of integers that is not sorted.
array_to_sort = [12, 34, 54, 2, 3]

# Print the original array before sorting
print("Original array:", array_to_sort)

# Perform Shell Sort on the array
shell_sort(array_to_sort)

# Print the sorted array after applying Shell Sort
print("Sorted array using Shell Sort:", array_to_sort)

#===============================================================================
# Runtime Analysis of Shell Sort
#---------------------------------------------------------------------------------
# Best Case: O(n log n)
# - This happens when the input array is already partially sorted. The early passes 
#   with larger gaps quickly bring elements close to their correct positions, so 
#   the final insertion sort pass is highly efficient.

# Average Case: O(n^(3/2)) or O(n^(1.5))
# - On average, Shell Sort performs better than quadratic algorithms like Bubble Sort 
#   or Insertion Sort, but it depends heavily on the gap sequence. The performance 
#   can vary based on the choice of the gap sequence.

# Worst Case: O(n^2)
# - The worst case occurs when the elements are in reverse order or arranged in a 
#   way that requires many comparisons and swaps. In these situations, Shell Sort 
#   degenerates to a performance similar to Insertion Sort, especially with poor 
#   gap sequences.

#===============================================================================
# Space Complexity of Shell Sort
#---------------------------------------------------------------------------------
# Space Complexity: O(1)
# - Shell Sort is an in-place sorting algorithm, meaning it does not require any
#   additional space other than the input array itself. This is a significant
#   advantage in memory-constrained environments compared to other algorithms
#   that use extra space (like Merge Sort).

#===============================================================================
# Pros and Cons of Shell Sort
#---------------------------------------------------------------------------------
# Pros:
# - More efficient than basic quadratic algorithms (e.g., Bubble Sort, Selection Sort) 
#   for moderately sized lists.
# - Adaptive to partially sorted data, improving its practical performance in real-world 
#   scenarios.
# - In-place sorting with minimal overhead, making it suitable for memory-constrained
#   environments.

# Cons:
# - The performance of Shell Sort is highly dependent on the choice of the gap sequence.
#   Poor gap choices can lead to suboptimal performance (close to O(n^2)).
# - Shell Sort is not a stable sorting algorithm, meaning that it does not guarantee the 
#   relative order of equal elements will be preserved.

#===============================================================================
# Advanced Tips for Optimizing Shell Sort
#---------------------------------------------------------------------------------
# 1. Gap Sequence Choice:
# - The performance of Shell Sort is greatly influenced by the sequence of gaps used. 
#   While the simple n//2, n//4, ..., 1 gap sequence is common, alternative sequences 
#   such as the Hibbard sequence (1, 3, 7, 15, ...) or Sedgewick sequence (1, 5, 19, ...) 
#   can provide better performance for specific datasets.

# 2. When to Use Shell Sort:
# - Shell Sort is often a good choice when dealing with datasets that are already somewhat
#   sorted or when memory constraints make more complex algorithms like Merge Sort less 
#   desirable.
# - It is also a good option when sorting in-place is essential, and you need a 
#   performance improvement over simple algorithms like Insertion Sort or Bubble Sort.

# 3. Minimizing Expensive Writes:
# - In situations where minimizing memory writes is critical (e.g., when sorting data 
#   on flash memory), Shell Sort's ability to perform fewer writes compared to algorithms 
#   like Merge Sort can be a significant advantage.

#===============================================================================


#===============================================================================
# Algorithms, Sorting Algorithms, Tim Sort
#===============================================================================

# In this section, we explore sorting algorithms, focusing on Tim Sort,
# which is a hybrid sorting algorithm derived from merge sort and insertion sort.
# Understanding sorting algorithms is essential for optimizing performance 
# in various applications, as they directly affect the time complexity of 
# data manipulation operations.

# Sorting algorithms can be categorized based on their characteristics:
# - Stability: Whether equal elements maintain their relative order.
# - Time Complexity: How the algorithm performs based on input size.
# - Space Complexity: Memory usage during the sorting process.

# Overview of Tim Sort:
# Tim Sort is the default sorting algorithm used in Python's built-in sorted() 
# function and the list.sort() method. It is designed to perform well on 
# many kinds of real-world data.

# Key Features of Tim Sort:
# - Hybrid algorithm: Combines the best features of merge sort and insertion sort.
# - Adaptive: It takes advantage of existing order in data, making it efficient on 
#   partially sorted datasets.
# - Stable: Maintains the relative order of equal elements.

# Time Complexity:
# - Best Case: O(n) when the array is already sorted or nearly sorted, as it will 
#   only require minimal work to verify order.
# - Average Case: O(n log n), as it divides the array and applies merge sort principles.
# - Worst Case: O(n log n), consistent performance even in the least favorable scenarios.
# - Space Complexity: O(n) due to the use of temporary arrays for merging.

# Example of Tim Sort implementation using Python's built-in sorted function.
array_to_sort = [5, 2, 9, 1, 5, 6]  # Sample array

# The sorted() function uses Tim Sort behind the scenes, providing an efficient sorting mechanism.
# It performs exceptionally well when the input array is partially sorted, as the algorithm
# will quickly identify ordered "runs" and minimize the number of operations.
sorted_array = sorted(array_to_sort)  # Using Tim Sort for sorting

# The output will be a new sorted array, as the sorted() function returns a sorted copy 
# without modifying the original list.
print("Sorted Array using Tim Sort:", sorted_array)

# Insights:
# - Tim Sort divides the input list into smaller "runs" of consecutive ordered elements.
# - The algorithm uses insertion sort to sort small runs, which is efficient for small datasets.
# - After sorting individual runs, it merges them using a modified merge sort approach.

# Insertion sort is used for small subarrays (runs), taking advantage of the low overhead
# for small datasets where an O(n^2) algorithm is efficient due to the low constant factors.
# For larger datasets, the divide-and-conquer strategy of merge sort is applied.

# Potential Pitfalls:
# - While Tim Sort is efficient for most data, it may not perform well on data 
#   that is randomly distributed without any order, though this is mitigated by its 
#   adaptive properties.
# - Care should be taken when sorting very large datasets due to the space complexity 
#   requirements, which could lead to increased memory usage.

# As Tim Sort uses additional memory (O(n) space complexity), sorting extremely large
# datasets can result in high memory consumption, especially when the list size 
# exceeds the available physical memory, causing performance bottlenecks.

# Use Cases:
# Tim Sort is particularly effective for:
# - Sorting large datasets where the input data has some order.
# - Situations where stability is required, such as sorting records by multiple fields.
# - Real-time applications where partial sorting may occur frequently.

# Real-world applications of Tim Sort include database sorting where stability matters,
# and web servers where large datasets need to be sorted frequently and efficiently.

# Advanced Tip:
# When implementing a sorting algorithm, consider:
# - The nature of the data (e.g., sorted, nearly sorted, random).
# - The importance of stability in your specific use case.
# - The available memory and whether space complexity could become a concern.
# - Always test your sorting implementation with edge cases, such as:
#   - Empty arrays
#   - Arrays with one element
#   - Arrays with duplicate values
#   - Large arrays with varying distributions

# Testing a variety of edge cases ensures robustness and uncovers potential issues
# that could arise in practical applications. For instance, handling an empty array 
# should not result in an error, while sorting arrays with one element should quickly 
# return without unnecessary operations.

# Example of edge cases:

# An empty array, which should result in an empty array being returned.
# Edge Case 1: An empty array is the simplest case and should return immediately.
empty_array = []
print("Sorted Empty Array using Tim Sort:", sorted(empty_array))  # Outputs: []

# An array with a single element, which is trivially sorted by definition.
# Edge Case 2: Arrays with only one element should return the same array without modification.
single_element_array = [42]
print("Sorted Single Element Array using Tim Sort:", sorted(single_element_array))  # Outputs: [42]

# An array with duplicate values, where stability is critical to ensure that 
# equal elements retain their original relative positions after sorting.
# Edge Case 3: Arrays with duplicate values should maintain the relative order of equal elements.
duplicate_values_array = [3, 1, 2, 1, 3, 2]
print("Sorted Array with Duplicate Values using Tim Sort:", sorted(duplicate_values_array))  # Outputs: [1, 1, 2, 2, 3, 3]

# Edge Case Insights:
# - Empty arrays are trivially sorted and should return quickly.
# - Single-element arrays are always sorted.
# - Arrays with duplicate values should maintain stability, ensuring the 
#   relative order of equal elements remains unchanged.

# The adaptive nature of Tim Sort allows it to perform exceptionally well on 
# real-world data that is partially sorted or contains repeating patterns. However, 
# testing with random or unsorted data is crucial to understanding the behavior in less ideal conditions.

# Always assess the nature of your dataset to choose the best sorting strategy.
# When working with specialized applications where memory constraints or performance 
# requirements are strict, be mindful of Tim Sort's space complexity and test for any 
# potential memory issues on large datasets.

#===============================================================================
# Algorithms, Searching Algorithms, Linear Search
#===============================================================================

# In this section, we explore searching algorithms, focusing on linear search.
# Searching algorithms are fundamental for finding elements in data structures efficiently.
# Understanding their time complexity and use cases is crucial for optimal algorithm design.

# Linear Search:
# Linear search is the simplest searching algorithm. It checks each element of the list 
# sequentially until the desired element is found or the list ends. 
# This algorithm works on both sorted and unsorted data.

# Time Complexity:
# - Best Case: O(1) - The target element is at the first position.
# - Average Case: O(n) - On average, half of the elements will be checked.
# - Worst Case: O(n) - The target element is not present, requiring a full traversal.
# For n elements, linear search performance degrades linearly as the dataset size increases.

# Example: Searching for an element in a list using linear search
def linear_search(arr, target):
    # Loop through each index in the array, using the range() function to access indices
    for index in range(len(arr)):  
        # If the element at the current index matches the target, return the index
        if arr[index] == target:  
            return index  # Found, return the index where the target is located
    return -1  # If no match is found, return -1 to indicate the target is not in the list

# Testing the linear search implementation with a sample dataset
array = [5, 3, 8, 1, 2, 7]  # Example array
target_value = 2  # Target value we are searching for

# Execute linear search and store the result (either the index or -1)
result_index = linear_search(array, target_value)

# Based on the result, display whether the target was found or not
if result_index != -1:
    # Success case, target found at result_index
    print("Element", target_value, "found at index:", result_index)
else:
    # Failure case, target not found in the array
    print("Element", target_value, "not found in the array")

# Use Case:
# Linear search is useful for small datasets or when the data is unsorted.
# It's also applicable when the cost of sorting the data outweighs the search cost, 
# such as in real-time applications where data is constantly changing.

# Use Case Examples:
# - Searching through a list of unsorted user data where new users are frequently added, 
#   and maintaining sorted order is not required.
# - Quick lookup in small datasets (e.g., a list of application settings).
# - Performing lookups in a dynamically generated list where sorting is not efficient.

# Pitfalls:
# 1. Performance: Linear search is inefficient for large datasets.
#    The performance worsens as the size of the list grows, requiring O(n) comparisons.
# 2. Not suitable for sorted datasets where more efficient algorithms like binary search exist.
#    Binary search can achieve O(log n) time complexity but requires sorted data.
# 3. If the dataset contains duplicate values, linear search will only return the first occurrence.

# Advanced Tips:
# - Consider using linear search as a fallback for searching in data structures that don't support 
#   efficient searching methods (e.g., linked lists).
#   Since linked lists require sequential access, linear search becomes inevitable.
# - In scenarios where elements may frequently change, maintaining a sorted structure for more efficient searches 
#   (like binary search) might not be feasible.
#   Sorting on every update could incur significant overhead, so linear search is useful when frequent updates occur.
# - Combining linear search with other algorithms, such as during the initial phases of sorting,
#   can provide quick access to unsorted data (e.g., while preparing a dataset for a more efficient sorting/searching algorithm).

# Edge Case Considerations:
# - Empty Lists: Ensure to handle cases where the list is empty, in which case the search should immediately return -1.
# - Non-existent Elements: Make sure the function properly handles the scenario where the target doesn't exist in the list.

# Run-time Analysis:
# When implementing linear search, keep in mind the following factors:
# - Data Structure: Linear search is inherently less efficient in linked lists than in arrays due to pointer traversals.
#   While arrays offer O(1) access per element, linked lists require sequential node access.
# - Size of Dataset: For large datasets, consider using more advanced search algorithms like binary search or hash tables.
#   Hash tables can offer O(1) average-time complexity for search operations, drastically improving performance.
# - Type of Data: Ensure to assess the data type; searching for complex objects may require more sophisticated search criteria.
#   When searching within objects, comparison operations might involve looking through multiple attributes.
# - Parallel Processing: For extremely large datasets, consider parallel processing approaches to divide and conquer.
#   While basic linear search is sequential, it can be optimized in distributed systems by splitting the data.

# Example - Empty List Case:
# Let's consider an edge case where the array is empty:
empty_array = []  # No elements
result_empty = linear_search(empty_array, target_value)
print("Result for empty array:", result_empty)  # Expected: -1 since there's no element to search

# Example - Element Not Found:
# In this case, we search for an element that doesn't exist in the array:
missing_target = 10  # Element not in the array
result_missing = linear_search(array, missing_target)
print("Result for missing target:", result_missing)  # Expected: -1 since 10 is not in the array

# Summary:
# Linear search is straightforward but inefficient for large datasets. It's essential to analyze the nature 
# of the data and the specific requirements of your application when deciding whether to implement linear search 
# or consider more efficient alternatives.

#===============================================================================
# Algorithms, Searching Algorithms, Binary Search
#===============================================================================

# Searching algorithms are fundamental techniques used to locate specific elements within a data structure.
# This section focuses on binary search, which is an efficient algorithm for finding an item in a sorted list.

# Key Points:
# - Binary search operates on a sorted array or list, making it significantly faster than linear search methods.
# - Its average and worst-case time complexity is O(log n), where n is the number of elements in the list.
# - The best case occurs when the middle element is the target, leading to a time complexity of O(1).

# Example 1: Binary Search Implementation
# This example demonstrates a classic binary search algorithm implemented iteratively.

# Sorted list of integers to search within
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7  # Element to search for
low = 0  # Start index
high = len(sorted_list) - 1  # End index

while low <= high:  # Continue until the search space is exhausted
    mid = (low + high) // 2  # Calculate the middle index
    print(f"Checking middle index {mid}, value: {sorted_list[mid]}")  # Debugging output

    if sorted_list[mid] == target:  # If the target is found
        print(f"Element {target} found at index {mid}")  # Target found
        break
    elif sorted_list[mid] < target:  # If the target is greater, ignore the left half
        low = mid + 1
    else:  # If the target is smaller, ignore the right half
        high = mid - 1

# If the loop exits without finding the target
if low > high:
    print(f"Element {target} not found in the list")  # Target not found

# Use case: Binary search is ideal for searching in sorted datasets, 
# such as looking up values in a database or finding the position of 
# an element in a sorted list efficiently.

# Explanation:
# Binary search uses a divide-and-conquer strategy, repeatedly splitting the search space in half.
# It is much faster than linear search, but its prerequisite is a sorted list. 
# During each iteration, the algorithm checks the middle element. If it's the target, the search ends.
# If not, the search continues on either the left or right half, depending on whether the target is smaller or larger than the middle element.

# Runtime Analysis:
# - Best Case: O(1) - The target is at the middle index during the first comparison.
# - Worst and Average Case: O(log n) - With each iteration, the search space is halved. In the worst case, we need to halve the list log n times until the search space becomes empty.

# Example 2: Recursive Binary Search Implementation
# Binary search can also be implemented using recursion, which simplifies the code but may introduce
# additional overhead due to recursive function calls and stack depth.

def recursive_binary_search(arr, target, low, high):
    if low > high:  # Base case: the target is not found
        return -1  # Indicate that the target is not found
    mid = (low + high) // 2  # Calculate the middle index
    if arr[mid] == target:  # If the middle element is the target
        return mid
    elif arr[mid] < target:  # Target is in the right half
        return recursive_binary_search(arr, target, mid + 1, high)
    else:  # Target is in the left half
        return recursive_binary_search(arr, target, low, mid - 1)

# Example of using the recursive binary search
result = recursive_binary_search(sorted_list, target, 0, len(sorted_list) - 1)
if result != -1:
    print(f"Element {target} found at index {result}")  # Outputs: Element 7 found at index 3
else:
    print(f"Element {target} not found in the list")  # In case the element is not found

# Explanation:
# The recursive version of binary search uses function calls to repeatedly split the list in half, just like the iterative version.
# Recursion simplifies the code by eliminating the loop, but it may cause memory overhead because each function call adds to the call stack.

# Performance considerations:
# - Iterative binary search is more memory-efficient as it avoids the function call overhead present in recursion.
# - Recursive binary search might be more elegant in small data sets but is generally avoided in large data sets due to the risk of exceeding recursion depth limits in Python (typically ~1000 calls).
# - For very large data sets, the iterative method is preferred to prevent stack overflow.

# Runtime Analysis:
# - Best Case: O(1) - Target is at the middle index during the first check.
# - Average and Worst Case: O(log n) - The search space is halved with each recursive call.

# Pitfalls:
# - The list must be sorted before binary search is applied, as the algorithm relies on sorted order.
# - Incorrect calculation of the middle index (e.g., not using integer division) can lead to infinite loops or incorrect behavior.
# - Stack overflow can occur in recursive implementations if the list is too large and exceeds the maximum recursion depth.

# Advanced Tips:
# - Optimized Variants: For example, if you want to find the first or last occurrence of a repeated element, slight modifications to binary search can be made. By adjusting the logic to keep searching after a match is found, you can find the first or last occurrence in O(log n) time.
# - Rotated Sorted Array: If the list is sorted but rotated (e.g., [13, 15, 17, 19, 1, 3, 5, 7, 9, 11]), binary search can be adapted to find the pivot and then apply binary search to the appropriate half. This also runs in O(log n) time.
# - Data Caching: For frequently searched data, using a caching layer or index structure can reduce the search overhead in real-world applications. Caching can avoid repetitive searches, especially when searching large datasets.


#===============================================================================
# Algorithms, Searching Algorithms, Ternary Search
#===============================================================================

# Searching algorithms are fundamental for efficiently locating specific elements in data structures.
# This section explains ternary search, which divides the search space into three parts rather than two.
# While it offers a different approach to search, it has niche use cases compared to binary search.

# 1. Overview of Ternary Search
# Ternary search is a divide-and-conquer algorithm that works similarly to binary search,
# but instead of dividing the search interval into two parts, it divides it into three parts.

# Key properties:
# - Requires the array to be sorted beforehand, like binary search.
# - Divides the array into three parts by calculating two midpoints.
# - Time complexity is O(log3(n)), which in theory could be better than binary search's O(log2(n)),
#   but in practice, ternary search often performs slightly worse due to the extra comparisons.

# Ternary Search Implementation
def ternary_search(arr, left, right, target):
    # Ensure the search space is valid
    if right >= left:
        # Calculate the two midpoints that divide the array into three parts
        mid1 = left + (right - left) // 3  # First third midpoint
        mid2 = right - (right - left) // 3  # Second third midpoint
        
        # Check if the target is at one of the midpoints
        if arr[mid1] == target:
            return mid1  # Return index of first midpoint if target is found
        if arr[mid2] == target:
            return mid2  # Return index of second midpoint if target is found
        
        # If the target is smaller than the first midpoint, search the left third
        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        # If the target is greater than the second midpoint, search the right third
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        # Otherwise, search the middle third between mid1 and mid2
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)
    
    # Return -1 if the target is not found
    return -1

# Example usage
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]  # Example sorted array
target_value = 13  # Target value to search for
result_index = ternary_search(sorted_array, 0, len(sorted_array) - 1, target_value)

# Output the result
if result_index != -1:
    print("Ternary Search: Target found at index", result_index)  # Output if the target is found
else:
    print("Ternary Search: Target not found")  # Output if the target is not found

# Explanation:
# Ternary search works by splitting the array into three parts rather than two.
# Two midpoints are calculated, and the target is compared with both.
# Depending on the comparison results, the search continues in one of three parts:
# - Left third, if the target is smaller than the first midpoint.
# - Right third, if the target is greater than the second midpoint.
# - Middle third, if the target lies between the two midpoints.

# Use case:
# - Ternary search can be useful in optimization problems where a function is unimodal (e.g., it has a single peak or trough),
#   allowing us to quickly converge on the maximum or minimum value. However, for typical search tasks,
#   binary search is preferred due to lower overhead.

# Runtime Analysis:
# - Best Case: O(1) if the target is at one of the midpoints during the first comparison.
# - Average Case: O(log3(n)) as the array is divided into three parts.
# - Worst Case: O(log3(n)) when the search continuously narrows down the segments but doesn't find the target.
# The difference between log base 2 (binary search) and log base 3 (ternary search) is minimal,
# and ternary search generally requires more comparisons per iteration.

# Best Practices and Considerations:
# - Ternary search requires that the array be sorted. If the input is not sorted, the search will yield incorrect results.
# - Ternary search performs more comparisons per iteration compared to binary search, which can lead to worse performance in practice.
# - Avoid using ternary search for small arrays, where linear search can often be faster due to lower overhead.
# - Be careful with calculating the midpoints. Ensure that index calculations are correct to avoid out-of-bounds errors.
#   This can occur if the midpoints are not calculated properly or if there are off-by-one errors when adjusting the search space.

# Advanced Insight:
# - In optimization problems, ternary search can be used for finding the extremum (maximum or minimum) of a unimodal function,
#   where we can narrow down the search space more effectively.
# - In theory, O(log3(n)) is faster than O(log2(n)), but this marginal improvement is rarely seen in practice due to the additional comparisons involved.
# - Binary search is generally faster in most scenarios because it requires fewer comparisons in each step, despite the logarithmic base difference.

# Pitfalls:
# - Not verifying that the input list is sorted is a common issue that can lead to incorrect results.
# - Miscalculating the midpoints or incorrectly adjusting the search space after a comparison can result in infinite loops or missed target values.
# - Ternary search adds complexity and is rarely used outside of specific cases like function optimization or when dealing with extremely large datasets where the slight theoretical advantage can matter.


#===============================================================================
# Algorithms, Searching Algorithms, Jump Search
#===============================================================================

# Searching algorithms are fundamental in computer science and software development.
# They allow us to efficiently find specific data within a collection. 
# In this section, we will explore the Jump Search algorithm, which is particularly effective 
# for sorted arrays.

# Jump Search
# Jump Search is a searching algorithm designed for sorted arrays. It works by dividing the 
# search space into blocks and jumping ahead by a fixed number of steps (typically the square 
# root of the array size) until it finds the block where the target element could be present. 
# Once the potential block is identified, it performs a linear search within that block.

# Time Complexity:
# - Best Case: O(1) - If the target element happens to be the first element checked.
# - Average Case: O(√n) - The search space is reduced by making jumps of √n steps.
# - Worst Case: O(√n) - The element is present but requires scanning the entire block after the jumps.

# Space Complexity: O(1) - No additional data structures are required beyond simple variables.

# Let's illustrate the Jump Search algorithm with an example.

# Example array (must be sorted for Jump Search)
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
target = 10  # The target element to search for
length = len(array)  # Get the length of the array
step = int(length ** 0.5)  # Optimal jump size is the square root of the array length
prev = 0  # To track the previous jump position

# Jump search algorithm implementation
while array[min(step, length) - 1] < target:  
    # Jump forward in blocks of 'step' size and compare the value at the end of the block with the target.
    prev = step  # Move the previous index to the current jump position
    step += int(length ** 0.5)  # Increase the jump step by the optimal block size
    if prev >= length:  # If the previous index exceeds the array bounds, the element is not in the array.
        print("Element not found")
        break

# Linear search within the identified block
for i in range(prev, min(step, length)):  # Perform a linear search between 'prev' and 'step' to locate the target.
    if array[i] == target:  # If the current element matches the target
        print(f"Element found at index {i}")  # Output the index of the found element
        break
else:
    print("Element not found")  # If no match is found in the linear search block

# Example output: Element found at index 10

# Explanation:
# 1. The algorithm first makes large jumps of size √n until it finds the block where the target 
#    might be. By doing so, it avoids having to check every element as in a linear search.
# 2. Once it identifies the block where the target could reside, it performs a linear search 
#    within that block. 
# 3. This two-step approach balances between the efficiency of skipping large portions of the list 
#    and the precision needed for finding the exact target in a smaller section.

# Best and Worst Cases:
# - Best Case: O(1) - The target is the first element checked.
# - Worst Case: O(√n) - In the worst case, the algorithm needs to check the entire last block 
#   after jumping through most of the list.

# Space Complexity:
# - The algorithm requires O(1) space, as only a few variables are needed to track indices, steps, and the target.

# Use Case:
# Jump Search is particularly useful for large, sorted datasets where a binary search may not be practical 
# due to computational overhead (e.g., calculating midpoints in a very large dataset or dealing with disk-based 
# storage where frequent access to the middle may be costly). 
# It offers a balance between reducing the search space quickly and using linear search for precision.

# Implementation Considerations:
# 1. Sorted Input: The array must be sorted for Jump Search to function correctly. Unsorted arrays 
#    will result in incorrect behavior.
# 2. Optimal Step Size: In most cases, using the square root of the array length (√n) is the optimal step size.
#    However, for specific datasets or access patterns, experimenting with different step sizes might yield better performance.
# 3. Balance Between Jump and Linear Search: Jump Search strikes a balance between the large strides of the jump phase 
#    and the precision of the linear search. If the dataset is small or the step size is too large, the performance gain 
#    compared to a simpler binary search may diminish.

# Advanced Tip:
# Secondary Indexing: For very large datasets, consider combining Jump Search with a secondary index structure. 
# By maintaining a smaller, separate index of block ranges or key data points, you can skip entire blocks more efficiently 
# without having to perform linear searches within each block. This hybrid approach can further optimize search performance, 
# especially when dealing with datasets stored on external storage (e.g., databases or files).

#===============================================================================
# Algorithms, Searching Algorithms, Interpolation Search Algorithm
#===============================================================================
# Example 1: Basic use case where the array is sorted and values are uniformly distributed
# The goal of interpolation search is to improve the efficiency over binary search by predicting where
# the value might be based on its value relative to the current search space, making it faster when
# the data is uniformly distributed.

# Interpolation search is generally faster than binary search for uniformly distributed data,
# but it falls back to O(n) in the worst case (non-uniform or skewed data).

def interpolation_search(arr, target):
    # Start and end indices for the search range
    low = 0  # Start of the array
    high = len(arr) - 1  # End of the array
    
    # Edge case: if array is empty, return -1 immediately as no search is needed
    if high < 0:
        return -1

    # The loop runs as long as the target is within the range of arr[low] and arr[high]
    # Note: arr[low] <= target <= arr[high] ensures that the search remains valid
    while low <= high and target >= arr[low] and target <= arr[high]:
        # Prevent division by zero when all values in the array are the same
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low  # If the target matches the value at low (or high, since they're equal)
            else:
                return -1  # If not, return -1 as the target cannot exist

        # Calculate the position where the target is likely to be using interpolation formula:
        # The formula estimates the position based on the distance of the target from arr[low]
        # relative to the total range of values in arr[low:high+1].
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])

        # Advanced Insight: The above formula can be seen as a weighted ratio. It estimates
        # the position by proportionally adjusting the distance between `low` and `high` based on
        # the difference between the target and the low value. This works best when the array has
        # a uniform distribution, as it assumes values are evenly spaced.

        # Check if the value at the estimated position is the target
        if arr[pos] == target:
            return pos  # If match is found, return the index
        
        # If the target is larger than arr[pos], search in the right half (higher values)
        if arr[pos] < target:
            low = pos + 1  # Shift the lower bound to the right
        
        # If the target is smaller than arr[pos], search in the left half (lower values)
        else:
            high = pos - 1  # Shift the upper bound to the left

    # If the loop exits without finding the target, return -1 to indicate failure
    return -1

#===============================================================================
# Example 2: Test with a uniformly distributed sorted array
# This array is uniformly distributed, so interpolation search will perform well, likely in O(log log n) time
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70
result = interpolation_search(arr, target)
print(f"Target {target} found at index {result}")

#===============================================================================
# Example 3: Test with a non-uniform array, where interpolation search may not perform as well
# The array is sorted but not uniformly distributed, causing the estimated positions to potentially
# mislead the search, falling back to O(n) behavior in the worst case.
arr = [10, 15, 30, 45, 47, 90, 100, 120, 150]
target = 45
result = interpolation_search(arr, target)
print(f"Target {target} found at index {result}")

#===============================================================================
# Example 4: Edge case where all elements are the same, testing for correctness and prevention
# of division by zero in the interpolation formula.
arr = [50, 50, 50, 50, 50]
target = 50
result = interpolation_search(arr, target)
print(f"Target {target} found at index {result}")

#===============================================================================
# Example 5: Testing with an empty array
# This checks the edge case where there is nothing to search.
arr = []
target = 100
result = interpolation_search(arr, target)
print(f"Target {target} found at index {result}")

#===============================================================================
# Example 6: Worst-case scenario where interpolation search behaves like a linear search
# A highly skewed array where the interpolation formula doesn't estimate positions well.
arr = [1, 1000, 10000, 100000, 1000000, 10000000]
target = 10000000
result = interpolation_search(arr, target)
print(f"Target {target} found at index {result}")

#===============================================================================
# Runtime Analysis:
# Best case: O(1) when the target is located on the first guess, which happens when the target
#            is uniformly distributed and the formula accurately predicts the position.
# Average case: O(log log n) when the data is uniformly distributed, as interpolation search makes better
#               predictions compared to binary search, narrowing the search range faster.
# Worst case: O(n) when the data is highly skewed or non-uniform, leading the search to behave more
#             like a linear search due to poor positional estimates.

# Implementation considerations:
# 1. The array must be sorted. If not, the search will not work correctly.
# 2. The array should ideally be uniformly distributed. The closer the array is to uniform, the better
#    interpolation search performs.
# 3. The algorithm handles cases where the values are all the same gracefully (to prevent division by zero),
#    but in practice, binary search might be more predictable in such cases.
# 4. When implementing, remember that interpolation search performs poorly for non-uniformly distributed data,
#    and in such cases, binary search would be a better alternative with its guaranteed O(log n) complexity.

# Advanced Tips:
# - For datasets where you know the distribution is highly skewed, avoid interpolation search and stick with binary search.
# - Consider using binary search as a fallback when interpolation search fails, or if you expect that your data distribution
#   may not be uniform.
# - If you're working with floating-point data, be cautious about precision errors in the interpolation formula, as it can
#   introduce inaccuracies in position calculation, especially with large datasets.

#===============================================================================
# Algorithms, Searching Algorithms, Exponential Search
#===============================================================================

# Exponential search is a combination of binary search and a sequential step.
# It is used when we don't know the bounds of the array or list where the target element resides.
# It efficiently narrows down the search range to a subarray in which the element might exist,
# and then applies binary search to find the element in that smaller range.

# Key Points:
# - Exponential search is ideal for unbounded or infinite lists, where the size of the list is unknown.
# - The algorithm works by first finding a range where the target might be located by exponentially increasing the index.
# - After determining the range, binary search is applied to that specific segment.
# - The overall time complexity of exponential search is O(log n), similar to binary search, with a slight overhead for finding the range.

# Example 1: Exponential Search Implementation

# Sorted list of integers to search within
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
target = 27  # Element to search for

# Initial boundary setup
if sorted_list[0] == target:  # Check if the first element is the target
    print(f"Element {target} found at index 0")  # Early exit, element found at index 0
else:
    index = 1  # Start searching with an exponential growth pattern

    # Exponentially increase the index until we find a range where the target may exist
    while index < len(sorted_list) and sorted_list[index] < target:
        print(f"Exponential growth: checking index {index}, value: {sorted_list[index]}")
        index *= 2  # Double the index each time to find the range

    # Once the range is determined, apply binary search in the narrowed down range
    low = index // 2  # The lower boundary of the range
    high = min(index, len(sorted_list) - 1)  # The upper boundary (make sure it doesn't exceed the list length)

    print(f"Applying binary search between indexes {low} and {high}")

    # Now performing binary search within the range [low, high]
    while low <= high:  # Standard binary search loop
        mid = (low + high) // 2  # Calculate the middle index
        print(f"Checking middle index {mid}, value: {sorted_list[mid]}")  # Debugging output

        if sorted_list[mid] == target:  # If the target is found
            print(f"Element {target} found at index {mid}")  # Target found
            break
        elif sorted_list[mid] < target:  # If the target is greater, ignore the left half
            low = mid + 1
        else:  # If the target is smaller, ignore the right half
            high = mid - 1

    # If the loop exits without finding the target
    if low > high:
        print(f"Element {target} not found in the list")  # Target not found

# Explanation:
# - The first phase of exponential search quickly finds a range where the target could reside.
# - In the second phase, a binary search is applied to the narrowed range, leading to an efficient search process.
# - This is particularly useful when searching in very large or infinite datasets (e.g., reading data from a file or a stream).
# - The exponential search takes advantage of the sorted property and logarithmically shrinks the problem space.

# Use case: Exponential search is efficient for cases where the size of the input is not known or is extremely large.
# This applies to unbounded data structures, like searching in a large database or in a file where we don't know the total number of entries.

# Best and Worst Cases:
# - Best Case: O(1) - The target is at the first index, or within the first exponential check.
# - Average Case: O(log n) - Most of the time, after identifying the range, binary search operates in logarithmic time.
# - Worst Case: O(log n) - Exponential growth leads to a binary search that operates on a narrowed-down range.

# Pitfalls to Avoid:
# - If the array isn't sorted, exponential search (like binary search) won't work correctly, as it assumes sorted input.
# - Exponentially increasing the index can lead to out-of-bounds errors. Always ensure that the index does not exceed the length of the list.
# - Be cautious of handling very small arrays or cases where the target is near the beginning of the list, as exponential search can overestimate the required range.

# Advanced Tips:
# - **Handling Infinite or Large Datasets**: For data that is unbounded or dynamically generated (e.g., data streams or web-scraped lists), exponential search can be an ideal method, as it allows us to find a range without needing to know the dataset's size beforehand.
# - **Search in Dynamic Data Structures**: In real-world scenarios where data size grows over time, using exponential search is beneficial because you can dynamically adjust the search space without having to predefine it.
# - **Variants**: Exponential search can be extended or modified for multi-dimensional search spaces, where the growth strategy might be adjusted to accommodate non-linear data structures.

#===============================================================================
# Algorithms, Graph Algorithms, Traversal Algorithms, Depth-First Search (DFS)
#===============================================================================

# Graph traversal algorithms are essential for exploring nodes and edges in a graph.
# Depth-First Search (DFS) is one of the core traversal algorithms, used to explore a graph by 
# starting from a source node and diving as deep as possible before backtracking.

# Key Points:
# - DFS explores as far along each branch of the graph as possible before backtracking.
# - It can be applied to both directed and undirected graphs.
# - DFS can be implemented iteratively (using a stack) or recursively.

# Example 1: DFS Using a Stack (Iterative Approach)
# In this implementation, we'll use an explicit stack to handle the traversal order.

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# The starting node for DFS traversal
start_node = 'A'

# Using a list as a stack to maintain nodes to be visited
stack = [start_node]

# Set to track visited nodes to avoid cycles
visited = set()

# Iterative DFS loop
while stack:
    # Pop a node from the stack to explore
    node = stack.pop()
    if node not in visited:
        print(f"Visiting node: {node}")  # Process the current node
        visited.add(node)  # Mark the node as visited
        # Push all unvisited neighbors to the stack (order matters here)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

# Use case:
# DFS is useful in scenarios like pathfinding, topological sorting, or detecting cycles.
# It's also applied in AI for decision trees, network traversal, and solving mazes.

# Explanation:
# DFS dives deep into the graph before backtracking, which is controlled using a stack.
# The stack helps mimic the behavior of recursion without the overhead of function calls.
# The graph is explored until all possible nodes reachable from the starting node are visited.

# Runtime Analysis:
# - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# - Space complexity: O(V), due to the stack and visited set.

# Pitfalls:
# - DFS may not find the shortest path in an unweighted graph (unlike Breadth-First Search).
# - In large graphs with deep recursion (e.g., a long chain of nodes), recursion depth limits could be hit in the recursive version.
# - Be cautious of infinite loops or stack overflow if cycles aren't handled (by tracking visited nodes).

# Advanced Tips:
# - **Graph Representation**: The adjacency list is memory efficient for sparse graphs but can be inefficient for dense graphs where adjacency matrices may be better suited.
# - **Edge Weights**: While DFS itself doesn't consider edge weights, it can be modified to work in weighted graph traversal by including logic to handle edge weights in applications like maze solving.
# - **Cycle Detection**: DFS can detect cycles in directed graphs by maintaining additional data structures such as a recursion stack to track back edges.

# Example 2: Recursive DFS Implementation
# DFS can also be written in a recursive style, which is simpler to understand but could lead to 
# stack overflow in very large or deep graphs.

# Starting node for DFS traversal
visited.clear()  # Resetting visited set for the recursive example

def dfs_recursive(node):
    if node not in visited:
        print(f"Visiting node: {node}")  # Process the current node
        visited.add(node)  # Mark the node as visited
        # Recursively visit all unvisited neighbors
        for neighbor in graph[node]:
            dfs_recursive(neighbor)

# Starting DFS from node 'A'
dfs_recursive('A')

# Explanation:
# The recursive version of DFS is straightforward: for each node, we visit it, mark it as visited,
# and recursively call DFS on all its neighbors. The function call stack implicitly manages 
# backtracking when we reach a dead end or all neighbors of a node have been visited.

# Runtime Analysis:
# - Time complexity: O(V + E), same as the iterative version, as each vertex and edge is processed once.
# - Space complexity: O(V) in the worst case due to the recursive call stack (or more if the graph is deeply nested).

# Pitfalls:
# - Recursive DFS can lead to stack overflow for very large graphs due to Python’s recursion depth limit (~1000 calls by default).
# - Handling cycles is crucial in recursive DFS, as failing to mark visited nodes may result in infinite recursion.
# - For disconnected graphs, this version will only traverse the connected component of the start node. 
#   To traverse the entire graph, multiple DFS calls might be necessary.

# Use case:
# Recursive DFS is commonly used in algorithms such as solving mazes or puzzles (like the 8-puzzle), 
# finding connected components in graphs, or in algorithms that rely on tree-like structures.

# Best and Worst Cases:
# - Best Case: O(V) - All nodes are directly connected to the start node.
# - Worst Case: O(V + E) - The graph is highly connected, meaning DFS has to traverse all vertices and edges.

# Advanced Tips:
# - **Tail Recursion Optimization**: In languages that support tail-call optimization, recursive DFS can be optimized to prevent stack overflow. However, Python does not support tail-call optimization, making the iterative version safer for deep graphs.
# - **Edge Classifications**: When applying DFS in directed graphs, edges can be classified into tree edges, back edges, forward edges, and cross edges, which is useful in algorithms like topological sorting or finding strongly connected components.

#===============================================================================
# Algorithms, Graph Algorithms, Traversal Algorithms, Breadth-First Search (BFS)
#===============================================================================

# BFS (Breadth-First Search) is a fundamental graph traversal algorithm.
# It explores the graph level by level, visiting all neighbors of a node before moving to the next level.
# BFS is commonly used for shortest path problems on unweighted graphs, connectivity checks, and other scenarios
# where traversing the graph in layers is advantageous.

# Key Points:
# - BFS is optimal for finding the shortest path in an unweighted graph.
# - It works for both directed and undirected graphs.
# - It is typically implemented using a queue to maintain the order of node exploration.
# - Time complexity is O(V + E), where V is the number of vertices and E is the number of edges.
# - The space complexity is O(V) due to the need to store the visited nodes and the queue.

# Graph representation using an adjacency list (dictionary):
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Example 1: BFS traversal starting from node 'A'
start_node = 'A'  # Starting point for the BFS
visited = []  # List to keep track of visited nodes
queue = [start_node]  # Queue initialized with the start node

print(f"Starting BFS from {start_node}")

# Traverse the graph using BFS
while queue:
    node = queue.pop(0)  # Dequeue the first node in the queue
    if node not in visited:  # Process the node only if it hasn't been visited
        print(f"Visiting node {node}")  # Debugging output showing current node being processed
        visited.append(node)  # Mark the node as visited
        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                print(f"Queueing neighbor {neighbor} of node {node}")  # Debugging output for neighbors
                queue.append(neighbor)

print(f"BFS traversal complete. Nodes visited: {visited}")  # Final output of visited nodes

# Explanation:
# BFS starts at the initial node ('A') and explores all its direct neighbors ('B' and 'C').
# It continues by visiting neighbors of 'B' ('D' and 'E') and then moves to 'C' and its neighbor ('F').
# The key to BFS is using a queue to maintain the exploration order, ensuring all nodes at the current level are
# visited before moving to the next level.

# Use case:
# BFS is particularly useful in scenarios where you need to explore all nodes at the same depth level first.
# Examples include finding the shortest path in an unweighted graph or solving puzzle-like problems where
# you expand all possible states at each step.

# Runtime Analysis:
# - Best Case: O(V) - If the graph has only vertices with minimal edges, BFS will visit each vertex exactly once.
# - Worst Case: O(V + E) - In a dense graph with many edges, BFS will traverse every edge in addition to visiting every vertex.
# - Space Complexity: O(V) - The queue holds at most V nodes, and we need additional space to store visited nodes.

# Pitfalls to avoid:
# - Not marking nodes as visited immediately can lead to infinite loops, especially in cyclic graphs.
# - Ensure the graph is connected; otherwise, BFS will not traverse the entire graph. In a disconnected graph, 
# additional logic may be needed to handle disconnected components.
# - Be cautious when using BFS on large graphs, as the space requirements can grow significantly in dense graphs.

# Advanced Tip:
# - BFS can be adapted for weighted graphs, but in that case, Dijkstra's algorithm (a priority-queue-based approach) is preferred
# for finding the shortest path. BFS only works for shortest path calculations in unweighted graphs.
# - For certain applications like web crawlers or network scans, where you might revisit nodes or need to handle very large graphs,
# optimizing the queue structure (e.g., using deque instead of list for O(1) pops) can significantly reduce overhead.

# Example 2: BFS with a goal check (shortest path)
# In this example, we modify BFS to stop when a target node is found, commonly used in shortest path problems.

start_node = 'A'  # Starting point for the BFS
goal_node = 'F'  # Goal node to search for
visited = []  # List to keep track of visited nodes
queue = [start_node]  # Queue initialized with the start node

print(f"Starting BFS from {start_node} to find {goal_node}")

# Traverse the graph using BFS
while queue:
    node = queue.pop(0)  # Dequeue the first node in the queue
    if node not in visited:  # Process the node only if it hasn't been visited
        print(f"Visiting node {node}")  # Debugging output showing current node being processed
        visited.append(node)  # Mark the node as visited
        if node == goal_node:  # If the goal node is found
            print(f"Goal node {goal_node} found during BFS traversal")
            break  # Stop the search once the goal is found
        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                print(f"Queueing neighbor {neighbor} of node {node}")  # Debugging output for neighbors
                queue.append(neighbor)

# If the loop completes without finding the goal
if goal_node not in visited:
    print(f"Goal node {goal_node} not found in the graph")

# Explanation:
# This variant of BFS halts once the target node (goal) is found. It's useful in scenarios like searching for a specific
# node in a large graph. BFS guarantees the shortest path in unweighted graphs, so the first time you encounter the goal,
# you have already found the shortest path.

# Runtime Analysis:
# - Best Case: O(V) - If the goal node is located early in the traversal.
# - Worst Case: O(V + E) - In the worst case, the algorithm traverses the entire graph before finding the goal.
# - Space Complexity: O(V) - Similar to the standard BFS, memory usage depends on the number of nodes.

# Pitfalls:
# - Ensure the goal node exists in the graph. If not, the algorithm will traverse the entire graph unnecessarily.
# - If there are multiple possible shortest paths, BFS will find one of them, but it won't necessarily explore
# all shortest paths unless modified.

# Advanced Tip:
# - BFS can be used in solving problems like the "Six Degrees of Separation," where it checks the minimum number of connections between people in a social network.
# - In competitive programming, BFS is often combined with a depth limit or bidirectional search to speed up solutions for large graphs. Bidirectional BFS, for instance, starts from both the source and the goal, meeting in the middle to reduce the search space to O(b^(d/2)) instead of O(b^d) where b is the branching factor and d is the depth of the search.

#===============================================================================
# Algorithms, Graph Algorithms, Shortest Path Algorithms, Dijkstra’s Algorithm
#===============================================================================

# Graph algorithms are essential in computer science, particularly when dealing with problems 
# involving networks, routing, and optimization.
# This section focuses on Dijkstra's algorithm, a well-known algorithm used to find the shortest 
# path from a source node to all other nodes in a graph with non-negative weights.

# Key Points:
# - Dijkstra's algorithm works efficiently for graphs with non-negative edge weights.
# - The algorithm computes the shortest path from a given source node to all other nodes, ensuring optimal paths.
# - It uses a greedy approach, expanding the nearest unvisited node each step.
# - Time complexity is O((V + E) log V) with a priority queue, where V is the number of vertices and E is the number of edges.

# Example 1: Dijkstra's Algorithm Implementation (Using a Priority Queue)
# This example demonstrates Dijkstra's algorithm to find the shortest path from a source node
# to all other nodes in a graph, represented using an adjacency list.

import heapq  # The heapq library provides an efficient priority queue implementation.

# Graph represented as an adjacency list where each node points to a list of tuples (neighbor, weight).
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
source = 'A'  # Starting point for the shortest path calculation

# Priority queue to hold nodes for exploration. Starts with the source node, with a distance of 0.
priority_queue = [(0, source)]

# Dictionary to store the shortest distance from the source node to each other node.
distances = {node: float('inf') for node in graph}  # Initialize all distances to infinity.
distances[source] = 0  # Distance to the source node is always 0.

# Set to track visited nodes
visited = set()

# Process the graph
while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)  # Get the node with the smallest distance.
    if current_node in visited:  # Skip already visited nodes to avoid unnecessary processing.
        continue
    visited.add(current_node)

    print(f"Visiting node {current_node} with current distance {current_distance}")

    # Check all neighbors of the current node
    for neighbor, weight in graph[current_node]:
        distance = current_distance + weight  # Calculate new distance for the neighbor.

        # Only update if the calculated distance is smaller than the known distance.
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(priority_queue, (distance, neighbor))  # Push the neighbor to the queue for future exploration.
            print(f"Updated distance for node {neighbor} to {distance}")

# Final shortest distances from the source node to all other nodes
print(f"Shortest distances from node {source}: {distances}")

# Explanation:
# - A priority queue (min-heap) is used to always expand the nearest unvisited node.
# - The algorithm repeatedly selects the node with the smallest known distance, then updates the distances 
#   to its neighbors if a shorter path is found.
# - The complexity is driven by the heap operations (logarithmic in the number of nodes) and 
#   the exploration of edges (linear in the number of edges).

# Use cases:
# - Dijkstra's algorithm is ideal for network routing problems, finding optimal paths in road networks,
#   or even in more abstract domains like game development (pathfinding for NPCs).
# - It is particularly useful when the graph has non-negative edge weights and finding the exact shortest 
#   path from a single source to all other nodes is required.

# Runtime Analysis:
# - Best Case: O(E + V log V), where E is the number of edges and V is the number of vertices. This occurs when 
#   each vertex has a minimal number of edges, and the graph is sparsely connected.
# - Worst Case: O(E log V), in highly connected graphs where nearly every node is connected to every other node.
#   The algorithm will have to examine many edges and maintain an extensive priority queue.

# Example 2: Dijkstra’s Algorithm with Dense Graphs
# In dense graphs (many edges), the number of edges E approaches V^2. The priority queue becomes crucial in 
# managing the number of distance updates efficiently.

dense_graph = {
    'A': [('B', 1), ('C', 2), ('D', 6), ('E', 3)],
    'B': [('A', 1), ('C', 2), ('D', 3), ('E', 7)],
    'C': [('A', 2), ('B', 2), ('D', 4), ('E', 1)],
    'D': [('A', 6), ('B', 3), ('C', 4), ('E', 5)],
    'E': [('A', 3), ('B', 7), ('C', 1), ('D', 5)]
}
source = 'A'  # Starting point for the shortest path calculation

priority_queue = [(0, source)]  # Priority queue starts with the source node
distances = {node: float('inf') for node in dense_graph}  # Initialize distances to infinity
distances[source] = 0  # Distance to source is always 0
visited = set()

while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)
    if current_node in visited:
        continue
    visited.add(current_node)

    print(f"Visiting node {current_node} with current distance {current_distance}")

    # Explore all neighbors
    for neighbor, weight in dense_graph[current_node]:
        distance = current_distance + weight
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(priority_queue, (distance, neighbor))
            print(f"Updated distance for node {neighbor} to {distance}")

# Final shortest distances from source to all other nodes
print(f"Shortest distances from node {source} in dense graph: {distances}")

# Explanation:
# - In dense graphs, the number of edges grows significantly, making the number of distance updates more frequent.
# - The priority queue (min-heap) becomes even more critical in ensuring the algorithm remains efficient.
# - Since the heapq ensures that the smallest distance node is processed first, the algorithm can maintain its logarithmic behavior
#   for each edge traversal even in dense networks.

# Performance Considerations:
# - Dijkstra’s algorithm assumes that all edge weights are non-negative. If negative weights exist, use Bellman-Ford or Johnson’s algorithm.
# - The priority queue should be carefully managed. Direct array-based implementations would make the algorithm slower, 
#   turning it into O(V^2) in dense graphs.

# Pitfalls:
# - Make sure to use a priority queue to maintain efficiency. Without it, Dijkstra’s algorithm can degrade to a slower version.
# - Ensure all edge weights are non-negative. Dijkstra’s algorithm does not handle negative edge weights properly 
#   and can result in incorrect shortest paths.
# - Updating distances without checking for shorter paths can lead to incorrect results or unnecessary processing.

# Advanced Tips:
# - In real-world applications, a more space-efficient adjacency list representation can be used, especially for large graphs.
# - For applications involving multiple shortest path queries, techniques like bidirectional Dijkstra or A* (with heuristics) can significantly reduce computation time.
# - Dijkstra’s algorithm can also be optimized using Fibonacci heaps for even better time complexity in theoretical settings,
#   reducing heap operations to amortized O(1) for decreases in key values.


#===============================================================================
# Algorithms, Graph Algorithms, Shortest Path Algorithms, Bellman-Ford Algorithm
#===============================================================================

# Shortest path algorithms are designed to find the shortest route from one vertex to another in a graph.
# Bellman-Ford is an algorithm that computes shortest paths from a single source vertex to all other vertices in a weighted graph.

# Key Points:
# - The Bellman-Ford algorithm is capable of handling graphs with negative edge weights, unlike Dijkstra’s algorithm.
# - It detects negative cycles in the graph, which can be important in certain real-world applications (e.g., financial arbitrage, network routing).

# Algorithm Overview:
# - Bellman-Ford works by iteratively relaxing all edges, meaning it attempts to shorten the path to each vertex step by step.
# - It performs |V| - 1 passes over all the edges (where |V| is the number of vertices).
# - If any distance can still be shortened after |V| - 1 passes, it indicates a negative weight cycle.

# Example 1: Simple Bellman-Ford Algorithm Walkthrough (no functions)

# Let's represent the graph as a list of edges where each edge is a tuple (source, destination, weight).
edges = [
    (0, 1, 5),  # Edge from vertex 0 to vertex 1 with weight 5
    (1, 2, -2),  # Edge from vertex 1 to vertex 2 with weight -2
    (0, 2, 3),  # Edge from vertex 0 to vertex 2 with weight 3
    (2, 3, 4),  # Edge from vertex 2 to vertex 3 with weight 4
    (3, 1, 6)   # Edge from vertex 3 to vertex 1 with weight 6
]
num_vertices = 4  # Number of vertices in the graph
source_vertex = 0  # The starting vertex for the algorithm

# Initialize the distance to all vertices to infinity except the source vertex, which is set to 0.
distance = [float('inf')] * num_vertices
distance[source_vertex] = 0  # Distance to the source vertex is always 0
print(f"Initial distances: {distance}")

# Bellman-Ford works by relaxing all edges V-1 times.
for i in range(num_vertices - 1):
    print(f"Iteration {i+1}:")
    for u, v, w in edges:  # For each edge (u, v, w)
        if distance[u] + w < distance[v]:  # Relax the edge
            distance[v] = distance[u] + w  # Update the distance to the destination vertex
            print(f"Relaxed edge ({u}, {v}), updated distance: {distance}")

# After V-1 iterations, check for negative weight cycles.
print("Checking for negative weight cycles...")
for u, v, w in edges:
    if distance[u] + w < distance[v]:
        print("Negative weight cycle detected!")  # If this condition holds, there's a negative cycle.
        break
else:
    print("No negative weight cycles detected.")
    print(f"Final distances: {distance}")

# Use Case:
# Bellman-Ford is useful in systems where negative edges may occur, such as financial models, 
# where losses or reductions are represented as negative weights, and we need to detect negative cycles.

# Explanation:
# - In the Bellman-Ford algorithm, we perform |V| - 1 iterations, as each iteration guarantees that
# the shortest paths are found for at least one more vertex.
# - By relaxing each edge repeatedly, we progressively ensure the shortest distance from the source to each vertex.
# - If after |V| - 1 iterations, the distances can still be improved, the graph must contain a negative weight cycle.

# Runtime Analysis:
# - Time Complexity: O(V * E), where V is the number of vertices, and E is the number of edges.
#   Each iteration relaxes all edges, and there are V - 1 iterations.
# - Space Complexity: O(V), as we need space to store the distances to each vertex.

# Best and Worst Cases:
# - Best Case: O(V * E) - The algorithm always takes the same time regardless of the input. There is no early exit.
# - Worst Case: O(V * E) - The worst case occurs when the graph has many edges and the shortest paths must be calculated for all vertices.

# Example 2: Another Bellman-Ford Walkthrough with Negative Cycle Detection

# Let's take another graph with a negative cycle.
edges_with_negative_cycle = [
    (0, 1, 4),
    (1, 2, -10),
    (2, 0, 3)
]
num_vertices_with_cycle = 3
source_vertex_with_cycle = 0

# Initialize distances again for this graph
distance_with_cycle = [float('inf')] * num_vertices_with_cycle
distance_with_cycle[source_vertex_with_cycle] = 0
print(f"Initial distances for graph with negative cycle: {distance_with_cycle}")

# Relax all edges V-1 times.
for i in range(num_vertices_with_cycle - 1):
    print(f"Iteration {i+1}:")
    for u, v, w in edges_with_negative_cycle:
        if distance_with_cycle[u] + w < distance_with_cycle[v]:
            distance_with_cycle[v] = distance_with_cycle[u] + w
            print(f"Relaxed edge ({u}, {v}), updated distance: {distance_with_cycle}")

# Check for negative weight cycles again.
print("Checking for negative weight cycles in the new graph...")
for u, v, w in edges_with_negative_cycle:
    if distance_with_cycle[u] + w < distance_with_cycle[v]:
        print("Negative weight cycle detected!")
        break
else:
    print("No negative weight cycles detected.")
    print(f"Final distances for graph with negative cycle: {distance_with_cycle}")

# Explanation:
# - In this second example, we encounter a negative cycle, as the distances continue to decrease even after V-1 iterations.
# - Bellman-Ford detects this cycle and flags it, which is important in graphs where such cycles are possible.
# - The algorithm stops early if a negative cycle is detected during the extra iteration after the V-1 passes.

# Pitfalls to Avoid:
# - Forgetting to handle negative cycles properly can lead to incorrect results. Always check for them after the relaxation process.
# - Bellman-Ford is slower than Dijkstra’s algorithm (O(V^2) or O(E log V) with a priority queue), so it may not be ideal for large graphs where all edges have non-negative weights.
# - Watch out for floating point precision issues when dealing with very large graphs or weights, which could cause unexpected behaviors during comparisons.

# Advanced Tips:
# - Bellman-Ford can be adapted to work in distributed systems where the graph is represented across multiple nodes, making it useful in network routing protocols (e.g., distance-vector routing).
# - In certain applications like competitive programming, the Bellman-Ford algorithm can be used to detect arbitrage opportunities in currency exchange rates, as negative cycles indicate profitable trades.

# Summary:
# Bellman-Ford is a versatile algorithm, especially in graphs with negative weights or cycles. 
# It’s slower than Dijkstra’s for non-negative graphs but uniquely suited for handling negative weights and cycles, making it valuable in specific problem domains.

#===============================================================================
# Algorithms, Graph Algorithms, Shortest Path Algorithms, Floyd-Warshall Algorithm
#===============================================================================

# The Floyd-Warshall algorithm is a classic dynamic programming algorithm used to find the shortest
# paths between all pairs of nodes in a weighted graph. This is particularly useful in dense graphs
# where you need to compute shortest paths between all pairs efficiently.

# Key Points:
# - It works on both directed and undirected graphs, as long as they do not have negative cycles.
# - It finds the shortest path between all pairs of vertices in O(V^3) time, where V is the number of vertices.
# - The algorithm handles negative weights but does not work correctly in the presence of negative cycles.

# Example 1: Floyd-Warshall Algorithm for All-Pairs Shortest Paths

# Adjacency matrix representation of the graph where `graph[i][j]` holds the weight of the edge from i to j.
# If there's no edge between vertices i and j, we use infinity (inf) to represent that.
inf = float('inf')  # Using Python's representation of infinity
graph = [
    [0, 3, inf, 5],
    [2, 0, inf, 4],
    [inf, 1, 0, inf],
    [inf, inf, 2, 0]
]

# Number of vertices in the graph
n = len(graph)

# The core of Floyd-Warshall is based on updating the graph in place to hold shortest path values.
for k in range(n):  # k represents the "intermediate" node
    for i in range(n):  # i is the source node
        for j in range(n):  # j is the destination node
            # Check if passing through vertex k provides a shorter path from i to j
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]  # Update with the shorter path
                print(f"Updated shortest path from {i} to {j} through {k}: {graph[i][j]}")

# Explanation:
# - The algorithm works by iteratively checking if a path from vertex i to j through an intermediate vertex k 
#   is shorter than the current known path.
# - It dynamically updates the adjacency matrix as it finds shorter paths, and after n iterations (one for each 
#   intermediate vertex), the matrix will hold the shortest paths between all pairs of nodes.

# Runtime Analysis:
# - Time Complexity: O(V^3), where V is the number of vertices. This is due to the three nested loops over the vertices.
# - Space Complexity: O(V^2) since we are storing the adjacency matrix.

# Best and Worst Cases:
# - Best Case: O(V^3), even if no updates are needed. This is because the algorithm always processes each pair of vertices.
# - Worst Case: O(V^3), when all possible paths are shorter and updates occur in every iteration.

# Use Case:
# - Floyd-Warshall is typically used in small to medium-sized dense graphs or for all-pairs shortest path problems.
#   It is often useful in routing algorithms where multiple sources and destinations are involved.

# Example 2: Detecting Negative Cycles
# The algorithm can also detect negative weight cycles, which occur when a loop in the graph results in an overall negative cost.

negative_cycle_detected = False
for i in range(n):
    if graph[i][i] < 0:  # If the distance from a node to itself becomes negative
        print(f"Negative cycle detected at node {i}")
        negative_cycle_detected = True
        break

if not negative_cycle_detected:
    print("No negative cycles detected.")

# Explanation:
# - To detect a negative cycle, we check the diagonal of the adjacency matrix (i.e., graph[i][i]).
# - If any element graph[i][i] is negative after running the algorithm, it indicates that the graph contains a negative cycle.
# - This works because if a node can have a shorter path to itself, the cycle it forms must have a negative weight.

# Advanced Tips:
# - Floyd-Warshall works well for dense graphs where many edges exist between vertices. For sparse graphs, other algorithms like Dijkstra's (for single source shortest path) or Bellman-Ford may be more efficient.
# - Although the algorithm updates in place, if the graph is large and the memory footprint is a concern, consider optimizing space usage by only storing the shortest path results in a separate, smaller data structure if the original adjacency matrix is not needed after execution.
# - If you're working with floating-point weights, be cautious of precision errors during summation, especially when paths have very small or large weights.

# Common Pitfalls:
# - Ensure that the graph does not have negative weight cycles before using the resulting shortest paths. Negative cycles can lead to incorrect or meaningless results.
# - Be mindful of the performance in large graphs. Although O(V^3) is manageable for moderate-sized graphs, it may become prohibitive as the number of vertices grows.
# - When updating graph[i][j], the condition must use '>' to ensure that only shorter paths replace the existing ones.

# Example 3: Handling Disconnected Nodes
# If some nodes in the graph are disconnected, the adjacency matrix should be initialized with infinity (inf) values
# for those edges. Floyd-Warshall handles this naturally by not updating those distances unless a shorter path is found.

# Consider another graph with a disconnected node
graph_with_disconnected_node = [
    [0, inf, 3, inf],
    [2, 0, inf, inf],
    [inf, 7, 0, 1],
    [6, inf, inf, 0]
]

# Re-running Floyd-Warshall for the new graph
for k in range(n):  
    for i in range(n):  
        for j in range(n):  
            if graph_with_disconnected_node[i][j] > graph_with_disconnected_node[i][k] + graph_with_disconnected_node[k][j]:
                graph_with_disconnected_node[i][j] = graph_with_disconnected_node[i][k] + graph_with_disconnected_node[k][j]
                print(f"Updated shortest path from {i} to {j} through {k}: {graph_with_disconnected_node[i][j]}")

# Explanation:
# - The Floyd-Warshall algorithm seamlessly handles graphs with disconnected nodes by maintaining the infinity values
#   in the adjacency matrix. If no path exists between two nodes, the value remains as infinity.
# - This approach allows the algorithm to process incomplete or partially connected graphs without modifications.

# Final Considerations:
# - The Floyd-Warshall algorithm is well-suited for educational purposes to understand dynamic programming and
#   graph traversal concepts but may not always be practical for very large graphs due to its cubic time complexity.
# - For real-time systems, where performance is critical, using more specialized algorithms like A* for specific paths
#   or Johnson’s algorithm (which combines Bellman-Ford and Dijkstra) for sparse graphs can be more efficient.

#===============================================================================
# Algorithms, Graph Algorithms, Minimum Spanning Tree Algorithms, Prim’s Algorithm
#===============================================================================

# Graph algorithms are used to solve problems related to graphs, where nodes represent elements 
# and edges represent relationships or connections between them. This section focuses on Prim’s Algorithm,
# a greedy algorithm for finding the Minimum Spanning Tree (MST) of a weighted, undirected graph.

# Key Points:
# - A Minimum Spanning Tree connects all nodes of a graph with the minimum possible total edge weight.
# - Prim’s algorithm builds the MST by selecting the smallest edge that connects a vertex in the growing MST 
#   to a vertex outside it.
# - The algorithm is efficient with a time complexity of O(E log V) using priority queues, where E is the 
#   number of edges and V is the number of vertices.

# Example: Prim’s Algorithm using a priority queue
# Here, we represent the graph using an adjacency list, and we use a priority queue to select the 
# next smallest edge efficiently.

import heapq  # Python's built-in priority queue (min-heap)

# Adjacency list representation of the graph where each node has a list of tuples (neighbor, weight)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

# Number of vertices
V = len(graph)

# We start Prim’s algorithm from vertex 0
start_vertex = 0

# Priority queue to select the smallest edge at each step, initialized with edges from start_vertex
pq = [(0, start_vertex)]  # (weight, vertex), the weight for the start vertex is 0 to start the algorithm

# Boolean array to track visited vertices to prevent cycles
visited = [False] * V

# List to store the edges in the resulting Minimum Spanning Tree (MST)
mst_edges = []

# Variable to keep track of the total weight of the MST
total_weight = 0

# While the priority queue is not empty, process the smallest edge
while pq:
    weight, u = heapq.heappop(pq)  # Get the smallest edge and its corresponding vertex
    if visited[u]:  # If the vertex has already been visited, skip it to avoid cycles
        continue

    # Mark this vertex as visited
    visited[u] = True

    # Add this edge to the MST (ignore the first edge with weight 0, which is the starting point)
    if weight != 0:  
        mst_edges.append((u, weight))
        total_weight += weight

    print(f"Adding vertex {u} to the MST with edge weight {weight}, total weight now {total_weight}")

    # Add all edges from the current vertex to the priority queue, if the neighbor hasn't been visited
    for neighbor, edge_weight in graph[u]:
        if not visited[neighbor]:
            heapq.heappush(pq, (edge_weight, neighbor))
            print(f"Considering edge from {u} to {neighbor} with weight {edge_weight}")

# After the loop ends, the MST has been fully constructed

# Printing the resulting MST
print("Minimum Spanning Tree contains the following edges:")
for edge in mst_edges:
    print(edge)
print(f"Total weight of the MST is {total_weight}")

# Use case: Prim's algorithm is suitable for dense graphs where there are many edges, as it efficiently
# selects the minimum edge using a priority queue. It is often used in network design, such as laying 
# out cables or designing least-cost spanning trees in telecommunication networks.

# Explanation:
# Prim’s algorithm starts from an arbitrary vertex and builds the MST one edge at a time by selecting
# the smallest edge that connects a vertex already in the MST to a vertex outside it. A priority queue 
# (min-heap) is used to always select the smallest edge efficiently. This is why the algorithm has a 
# time complexity of O(E log V), where E is the number of edges and V is the number of vertices.

# Runtime Analysis:
# - Time Complexity: O(E log V), where E is the number of edges and V is the number of vertices.
#   The log V comes from the operations on the priority queue, and the algorithm processes each edge at least once.
# - Space Complexity: O(V + E), as we need to store the adjacency list and the priority queue.

# Best and Worst Cases:
# - Best Case: O(E log V), occurs in a graph where the priority queue allows us to select the minimum edges quickly.
# - Worst Case: O(E log V), the performance is tied to the number of edges and vertices in the graph,
#   and the priority queue operations dominate the time complexity.

# Pitfalls:
# - Ensure that the graph is undirected, as Prim's algorithm is designed for undirected graphs. 
#   Applying it to a directed graph will produce incorrect results.
# - Prim’s algorithm requires a connected graph; otherwise, it will not be able to find an MST.
#   In disconnected graphs, an MST does not exist for the entire graph, though it can be applied to 
#   individual connected components.

# Advanced Tips:
# - In certain situations, Prim’s algorithm can be optimized further using more advanced data structures 
#   like Fibonacci heaps, reducing the time complexity of the algorithm to O(E + log V), though the 
#   practical improvement is often marginal compared to using a binary heap (priority queue).
# - If the graph is sparse (few edges relative to the number of vertices), an alternative algorithm like 
#   Kruskal’s may be preferred due to simpler implementation and reduced complexity in such cases.
# - Prim’s algorithm can be modified to handle edge weights dynamically or in streaming scenarios 
#   where the graph changes over time, although this increases the algorithm's complexity and memory usage.


#===============================================================================
# Algorithms, Graph Algorithms, Minimum Spanning Tree Algorithms, Kruskal's Algorithm
#===============================================================================

# Graph algorithms are a foundational part of computer science and are used to solve problems involving networks of nodes (vertices) and connections (edges).
# A Minimum Spanning Tree (MST) is a subset of the edges in a weighted, undirected graph that connects all vertices with the minimum possible total edge weight, without any cycles.
# Kruskal's algorithm is a greedy algorithm used to find the MST of a graph. It operates by sorting all edges and including the smallest edges while avoiding cycles.

# Key Points:
# - Kruskal’s algorithm focuses on adding the shortest available edge to the MST, provided it does not form a cycle.
# - The graph must be undirected, and all edges must have non-negative weights for Kruskal’s algorithm to work correctly.
# - The algorithm uses the Union-Find data structure to efficiently check and merge connected components.

# Example 1: Kruskal's Algorithm for Minimum Spanning Tree
# This example demonstrates Kruskal’s algorithm to find the MST in a graph.

# Define a graph as a list of edges where each edge is represented as a tuple: (weight, vertex1, vertex2)
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (3, 'B', 'C'),
    (6, 'B', 'D'),
    (4, 'C', 'D'),
    (2, 'A', 'D'),
]

# Sort the edges based on weight (Kruskal's algorithm starts by sorting edges by weight)
edges.sort()  # This step takes O(E log E), where E is the number of edges
print(f"Sorted edges by weight: {edges}")  # Debugging output to show the sorted edges

# Set up the Union-Find data structure (also known as Disjoint-Set Union)
parent = {}  # To store the leader (root) of each vertex’s set
rank = {}  # To keep track of tree heights for union by rank optimization

# Initialize each vertex as its own parent and rank as 0
for edge in edges:
    parent[edge[1]] = edge[1]
    parent[edge[2]] = edge[2]
    rank[edge[1]] = 0
    rank[edge[2]] = 0

# Helper function to find the root parent of a vertex (with path compression)
def find(vertex):
    if parent[vertex] != vertex:  # If vertex is not its own parent
        parent[vertex] = find(parent[vertex])  # Path compression: make the parent point to the root
    return parent[vertex]

# Helper function to perform union of two sets (union by rank)
def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    
    # Union by rank optimization
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1  # Make root1 the parent of root2
        elif rank[root1] < rank[root2]:
            parent[root1] = root2  # Make root2 the parent of root1
        else:
            parent[root2] = root1  # If equal, make one root parent of the other
            rank[root1] += 1  # Increase the rank of the new root

# Kruskal's Algorithm to find the MST
mst = []  # List to store the Minimum Spanning Tree edges
total_weight = 0  # Variable to store the total weight of the MST

for edge in edges:
    weight, vertex1, vertex2 = edge
    if find(vertex1) != find(vertex2):  # Check if including this edge creates a cycle
        union(vertex1, vertex2)  # Perform the union operation
        mst.append(edge)  # Add the edge to the MST
        total_weight += weight  # Add the edge weight to the total weight of the MST
        print(f"Edge {edge} added to the MST.")  # Debugging output to show added edges

print(f"Final MST: {mst}")
print(f"Total weight of MST: {total_weight}")

# Explanation:
# Kruskal's algorithm begins by sorting all edges of the graph by their weight. Then, it processes each edge in ascending order, using the Union-Find data structure to 
# ensure that the edge does not form a cycle. If the edge can be safely added (i.e., it connects two previously unconnected components), it is included in the MST.

# Runtime Analysis:
# - Sorting the edges takes O(E log E), where E is the number of edges.
# - Each find and union operation takes almost constant time, O(α(V)), due to the use of path compression and union by rank, where V is the number of vertices and α is the inverse Ackermann function.
# - Overall time complexity: O(E log E) because sorting dominates the process.

# Use case:
# Kruskal's algorithm is ideal for sparse graphs with many vertices and fewer edges because it efficiently handles disjoint sets of vertices.
# It is used in network design (e.g., laying out electrical circuits or road networks) where minimizing total cost is crucial.

# Best and Worst Cases:
# - Best case: O(E log E) - The algorithm always sorts the edges and checks for cycles regardless of the graph's structure.
# - Worst case: O(E log E) - The worst case is no worse than the best case because the algorithm must examine all edges.

# Advanced Tips:
# - **Union by Rank and Path Compression**: These optimizations in the Union-Find structure significantly reduce the time complexity of checking and merging components. Without these, each find or union operation could degrade to O(V), making the algorithm much slower.
# - **Cycle Detection**: Kruskal’s algorithm ensures no cycles are formed by leveraging the Union-Find structure, which is faster than checking for cycles explicitly via DFS or BFS.
# - **Handling Large Graphs**: For very large graphs, especially sparse graphs, Kruskal’s algorithm is generally more efficient than Prim’s algorithm because it processes only the edges and doesn’t require a priority queue for vertices.
# - **Edge Cases**: Ensure the graph is connected before applying Kruskal’s algorithm. If the graph is disconnected, Kruskal’s algorithm will return a forest of MSTs, one for each connected component, rather than a single spanning tree.

# Potential Pitfalls:
# - Not initializing the Union-Find structure correctly can lead to incorrect results, such as forming cycles or missing edges in the MST.
# - If the graph is not connected, Kruskal’s algorithm won’t yield a valid MST for the entire graph, only for the connected components.
# - Beware of negative weights in real-world applications; Kruskal’s algorithm can handle them, but they may lead to unintended results in certain contexts.

# Alternative Considerations:
# - In denser graphs, consider Prim's algorithm, which may be more efficient due to its vertex-based approach, particularly when used with a priority queue.
# - For edge-dense graphs, using adjacency matrix representations may increase memory usage but could lead to different performance characteristics when used with Kruskal’s algorithm.

#===============================================================================
# Algorithms, Graph Algorithms, Topological Sorting
#===============================================================================

# Graph algorithms provide mechanisms to work with graph structures (vertices and edges), 
# often used to model various problems like dependency resolution, network flows, and scheduling.

# Topological sorting is a linear ordering of vertices in a directed acyclic graph (DAG) 
# such that for every directed edge u -> v, vertex u comes before vertex v in the ordering.

# Key Points:
# - Topological sorting is only applicable to directed acyclic graphs (DAGs).
# - A typical use case is scheduling tasks that have dependencies (e.g., job scheduling, course prerequisite ordering).
# - There are two common methods to perform topological sorting:
#   1. **Kahn’s Algorithm** (Iterative)
#   2. **Depth-First Search (DFS)** based method (Recursive)

# Time Complexity:
# - Both Kahn’s Algorithm and the DFS-based method have a time complexity of O(V + E),
#   where V is the number of vertices, and E is the number of edges in the graph.

# Example 1: Topological Sorting Using Kahn's Algorithm (Iterative Approach)
# This example demonstrates Kahn’s Algorithm, which uses an in-degree approach.

# Directed acyclic graph represented as an adjacency list
graph = {
    0: [1, 3],
    1: [2],
    2: [4],
    3: [2, 4],
    4: []
}

# List to store the in-degrees (number of incoming edges) of each vertex
in_degree = [0] * len(graph)  # Initially, set all in-degrees to zero

# Calculate the in-degree of each vertex
for node in graph:
    for neighbor in graph[node]:
        in_degree[neighbor] += 1  # Increment the in-degree of the target vertex

print("In-degree of vertices:", in_degree)  # Output: [0, 1, 2, 1, 2]

# Use case: Kahn’s algorithm is useful for scheduling problems, 
# like determining the order in which tasks with dependencies should be performed.

# Queue to store all vertices with in-degree of 0 (i.e., no dependencies)
queue = [node for node in range(len(graph)) if in_degree[node] == 0]

# List to store the topological order
topological_order = []

while queue:  # Continue until there are no vertices with 0 in-degree
    current_node = queue.pop(0)  # Dequeue a vertex
    topological_order.append(current_node)  # Add it to the topological order
    
    # Reduce the in-degree of all adjacent vertices by 1
    for neighbor in graph[current_node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:  # If in-degree becomes 0, add it to the queue
            queue.append(neighbor)

print("Topological Order:", topological_order)  # Output: [0, 3, 1, 2, 4]

# Explanation:
# - The algorithm starts by calculating the in-degree for each vertex.
# - All vertices with 0 in-degree (i.e., no dependencies) are placed in a queue.
# - We then process each vertex in the queue, appending it to the topological order,
#   and reducing the in-degree of its adjacent vertices (outgoing edges).
# - If an adjacent vertex’s in-degree becomes 0, it is added to the queue to be processed next.
# - The process continues until all vertices are processed.

# Runtime Analysis:
# - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
#   Each vertex and edge are processed exactly once.
# - Space complexity: O(V), required for storing the in-degrees and the queue.

# Best Case:
# - O(V + E), since all vertices and edges must be processed at least once.

# Worst Case:
# - O(V + E), as the algorithm always processes the entire graph regardless of how it's structured.

# Pitfalls:
# - This algorithm will not work if the graph contains cycles. Ensure the graph is a DAG before applying topological sorting.
# - A common mistake is neglecting to initialize the in-degrees of vertices correctly, which will lead to incorrect results.

# Advanced Tip:
# - Topological sorting is useful for detecting cycles in a graph. If there are vertices left in the graph 
#   with non-zero in-degrees after processing, this indicates the presence of a cycle (i.e., the graph is not a DAG).
# - Combining topological sorting with dynamic programming can solve complex scheduling and resource allocation problems.

# Example 2: Topological Sorting Using DFS (Recursive Approach)
# This method uses a depth-first search to generate a topological ordering by 
# finishing vertices in reverse post-order.

visited = [False] * len(graph)  # To track visited vertices
topo_stack = []  # Stack to store the topological order

# Helper function to perform DFS
def dfs(node):
    visited[node] = True  # Mark the current node as visited
    print(f"Visiting node {node}")  # Debug output

    for neighbor in graph[node]:
        if not visited[neighbor]:  # Recur for all unvisited adjacent vertices
            dfs(neighbor)

    topo_stack.append(node)  # Once all neighbors are visited, push the current node onto the stack

# Perform DFS for each unvisited vertex
for vertex in range(len(graph)):
    if not visited[vertex]:
        dfs(vertex)

# Reverse the stack to get the topological order
topological_order_dfs = topo_stack[::-1]
print("Topological Order (DFS):", topological_order_dfs)  # Output: [0, 3, 1, 2, 4]

# Explanation:
# - The DFS-based approach explores each vertex and its neighbors recursively.
# - After visiting all neighbors of a vertex, it pushes the vertex onto the stack.
# - Once all vertices are processed, the stack contains the topological order in reverse post-order.
# - This method is conceptually simpler than Kahn's algorithm but can be less intuitive in practice.

# Runtime Analysis:
# - Time complexity: O(V + E), similar to Kahn's algorithm. Each vertex and edge are visited exactly once.
# - Space complexity: O(V) for the visited array and stack.

# Best and Worst Case:
# - O(V + E), as each vertex and edge are visited exactly once in a depth-first manner.

# Pitfalls:
# - Be cautious with cyclic graphs, as DFS will not explicitly handle cycles. The graph must be a DAG for this method to work correctly.
# - The recursion depth can become an issue with very large graphs, potentially causing stack overflow.

# Advanced Tip:
# - In practical scenarios, topological sorting using DFS can be combined with cycle detection mechanisms 
#   (such as using a stack-based approach to detect back edges) to avoid processing graphs that aren’t DAGs.

#===============================================================================
# Algorithms, Graph Algorithms, Graph Cycle Detection
#===============================================================================

# Graph algorithms are crucial in solving problems involving networks, where nodes (vertices) are connected
# by edges. Detecting cycles in graphs is a common problem, particularly when working with directed or 
# undirected graphs. A cycle in a graph occurs when a path leads back to the same node, indicating 
# a loop or circular dependency.

# Key Points:
# - Cycle detection is useful in scenarios such as deadlock detection, dependency resolution, and topological sorting.
# - Different techniques are used to detect cycles in directed and undirected graphs.
# - The time complexity of cycle detection depends on the traversal approach, typically O(V + E), where V is the 
#   number of vertices and E is the number of edges.

# Example 1: Detecting a Cycle in a Directed Graph using Depth First Search (DFS)
# This approach uses DFS to explore nodes. If we encounter a node that has already been visited
# in the current recursion stack, a cycle exists.

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['A'],
    'E': ['D']
}

visited = set()  # Set to store visited nodes
rec_stack = set()  # Recursion stack to track the path in the current DFS

# We will print the process instead of using a function to adhere to the requirements.
nodes = list(graph.keys())  # Get all the nodes in the graph

for node in nodes:
    if node not in visited:
        print(f"Starting DFS from node {node}")
        stack = [(node, None)]  # Stack to simulate the recursion for this node
        while stack:
            current, parent = stack.pop()
            print(f"Visiting node {current}")

            if current in rec_stack:
                print(f"Cycle detected! Node {current} is part of a cycle.")
                break

            if current not in visited:
                visited.add(current)
                rec_stack.add(current)
                print(f"Marking node {current} as visited and adding it to the recursion stack.")

                # Push adjacent nodes onto the stack
                for neighbor in graph.get(current, []):
                    stack.append((neighbor, current))
            else:
                print(f"Node {current} has already been visited. Backtracking.")
                rec_stack.discard(current)  # Remove from recursion stack when backtracking

# Explanation:
# This code simulates a depth-first search (DFS) to detect cycles in a directed graph.
# By maintaining a recursion stack (rec_stack), we keep track of the current path. If a node 
# is encountered that is already in the recursion stack, it indicates a back edge, implying a cycle.

# Runtime Analysis:
# - Best Case: O(V) - In a case where no cycle exists and we traverse all vertices without revisiting them.
# - Worst and Average Case: O(V + E) - In the worst case, all vertices and edges need to be explored to detect the cycle.

# Pitfalls:
# - Forgetting to clear the node from the recursion stack when backtracking can cause false-positive cycle detection.
# - This approach only works for directed graphs. For undirected graphs, a modified approach is needed, as backtracking can lead to cycles in undirected graphs.

# Example 2: Detecting a Cycle in an Undirected Graph using DFS
# In undirected graphs, cycles are detected when an adjacent node is revisited but is not the direct parent.
# This ensures that cycles aren't falsely detected due to simple backtracking.

# Graph represented as an adjacency list (Undirected Graph)
graph_undirected = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E'],
    'E': ['D']
}

visited = set()  # Reset visited set for this example

for node in graph_undirected.keys():
    if node not in visited:
        print(f"Starting DFS from node {node} in undirected graph")
        stack = [(node, None)]  # Stack to simulate the recursion for this node
        while stack:
            current, parent = stack.pop()
            print(f"Visiting node {current}")

            if current not in visited:
                visited.add(current)
                print(f"Marking node {current} as visited.")

                # Push adjacent nodes onto the stack, ensuring we don't revisit the parent
                for neighbor in graph_undirected[current]:
                    if neighbor != parent:  # Avoid backtracking to parent
                        stack.append((neighbor, current))
            else:
                print(f"Cycle detected! Node {current} revisited, not the parent.")
                break

# Explanation:
# The approach for undirected graphs differs slightly. When a node is revisited (except its parent), 
# it indicates a cycle. This ensures that the backtracking in undirected graphs doesn't falsely signal a cycle.

# Runtime Analysis:
# - Best Case: O(V) - No cycle exists, and the DFS completes without revisiting nodes unnecessarily.
# - Worst and Average Case: O(V + E) - All nodes and edges must be explored to check for a cycle.

# Pitfalls:
# - Incorrectly comparing the parent node can lead to false-positive cycle detections. Ensure that only non-parent nodes are considered for cycle checking.

# Advanced Tips:
# - For large graphs, optimizing cycle detection using Union-Find (disjoint-set) can further reduce the complexity of cycle detection, especially in undirected graphs. Union-Find can detect cycles in O(E log* V) with path compression, making it more efficient for dense graphs.
# - In directed acyclic graphs (DAGs), cycle detection is useful in topological sorting. If a cycle is detected during the sort, the graph cannot be sorted, and the cycle indicates a dependency issue.
# - Another optimization technique is "Tarjan's Algorithm," which can be used to find all strongly connected components in a graph, efficiently identifying cycles in O(V + E) time.

#===============================================================================
# Algorithms, Graph Algorithms, Strongly Connected Components, Kosaraju’s Algorithm
#===============================================================================

# Graph algorithms are essential for solving problems related to connectivity, flow, and structure.
# This section focuses on finding strongly connected components (SCCs) in a directed graph using Kosaraju’s algorithm.

# Key Points:
# - A strongly connected component (SCC) is a maximal subgraph in which every pair of vertices are reachable from each other.
# - Kosaraju’s algorithm is efficient for finding SCCs in a directed graph.
# - The algorithm performs two depth-first searches (DFS), first on the original graph, and then on the transposed (reversed) graph.
# - Kosaraju’s algorithm has a time complexity of O(V + E), where V is the number of vertices and E is the number of edges.

# Step 1: Define a directed graph using adjacency lists.
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3],
    6: [4]
}

print("Graph defined as adjacency list:", graph)

# Explanation:
# Here, we represent a directed graph as a dictionary, where each key is a node and the corresponding value is 
# a list of nodes to which it has outgoing edges. This representation is both memory-efficient and intuitive 
# for traversing the graph using depth-first search (DFS).

# Step 2: Perform the first depth-first search (DFS) on the graph to determine the finishing order of vertices.
visited = set()  # Set to track visited nodes
finish_stack = []  # Stack to store the finishing order of nodes

# Manually simulating a DFS process to understand how Kosaraju’s algorithm works
def dfs_first_pass(node):
    print(f"Visiting node {node} in the first pass")
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_first_pass(neighbor)
    finish_stack.append(node)  # Push node to stack after exploring all neighbors
    print(f"Node {node} finished, adding to stack")

# Execute DFS for each unvisited node
for vertex in graph:
    if vertex not in visited:
        dfs_first_pass(vertex)

print("Order of nodes after first DFS pass:", finish_stack)

# Explanation:
# In the first pass, we perform a DFS on the original graph to record the finishing times of each node. 
# This finishing time helps to reverse the order in which nodes are visited in the second DFS pass, 
# which is crucial to correctly identifying SCCs.
# The use of a set ensures that nodes are only visited once, preventing redundant operations.

# Step 3: Transpose the graph (reverse the direction of all edges).
transposed_graph = {
    0: [2],
    1: [0],
    2: [1],
    3: [2, 5],
    4: [3, 6],
    5: [4]
}

print("Transposed graph:", transposed_graph)

# Explanation:
# Transposing the graph means reversing the direction of all edges. In Kosaraju’s algorithm, the transposed 
# graph is necessary for the second DFS pass. Transposing ensures that we explore the SCCs correctly by reversing 
# the reachability relationships between nodes.

# Step 4: Perform the second depth-first search (DFS) on the transposed graph, processing nodes in the order 
# defined by the finish_stack (from Step 2).
visited.clear()  # Reset visited set for the second pass
scc_list = []  # List to store all the strongly connected components

# Manually simulating the DFS process on the transposed graph
def dfs_second_pass(node, scc):
    print(f"Visiting node {node} in the second pass")
    visited.add(node)
    scc.append(node)  # Add node to the current SCC
    for neighbor in transposed_graph[node]:
        if neighbor not in visited:
            dfs_second_pass(neighbor, scc)

# Process nodes in the order defined by the finish_stack (in reverse order)
while finish_stack:
    vertex = finish_stack.pop()
    if vertex not in visited:
        current_scc = []  # Temporary list to hold the current SCC
        dfs_second_pass(vertex, current_scc)
        scc_list.append(current_scc)  # Add the current SCC to the list of SCCs
        print(f"SCC found: {current_scc}")

print("All SCCs:", scc_list)

# Explanation:
# In the second pass, we perform DFS on the transposed graph, processing nodes in the reverse finishing order 
# obtained from the first DFS pass. Each DFS call discovers one strongly connected component (SCC). By clearing the 
# visited set, we ensure that nodes are not revisited across different SCCs.

# Use case: Kosaraju’s algorithm is particularly useful for analyzing the structure of directed graphs, such as 
# detecting cycles in dependency graphs, finding clusters in social networks, or optimizing programs with control 
# flow graphs.

# Runtime Analysis:
# - Time Complexity: O(V + E) because each node and edge is processed twice, once in the original graph and once 
# in the transposed graph.
# - Space Complexity: O(V) due to the need to store visited nodes and the finish stack. The adjacency list 
# representation also requires O(V + E) space to store the graph structure.

# Best and Worst Cases:
# - Best Case: O(V + E) - The algorithm's complexity is optimal for all cases, as it processes every node and edge exactly twice.
# - Worst Case: O(V + E) - The performance remains the same regardless of the graph structure (e.g., dense vs sparse).

# Common pitfalls to avoid:
# - Forgetting to reverse the graph properly, which would prevent SCCs from being identified correctly.
# - Failing to reset the visited set between the two passes could result in incorrect results, as nodes would 
# already be marked as visited in the second pass.
# - Mismanaging the stack order in the first DFS pass, which could lead to an incorrect traversal sequence in 
# the second pass.

# Advanced Tips:
# - Kosaraju’s algorithm works well in conjunction with other graph algorithms. For instance, after identifying SCCs, 
# you can collapse them into single nodes and perform further analysis on the reduced graph.
# - For performance optimization in large-scale graphs, consider combining Kosaraju’s algorithm with parallel 
# processing techniques, where different components of the graph are processed concurrently.
# - Tarjan's algorithm is another efficient alternative for finding SCCs, which uses a single DFS pass and keeps 
# track of nodes using low-link values.

#===============================================================================
# Algorithms, Graph Algorithms, Strongly Connected Components, Tarjan’s Algorithm
#===============================================================================

# Tarjan’s Algorithm is used to find all the Strongly Connected Components (SCCs) in a directed graph.
# A strongly connected component is a subgraph where every vertex is reachable from every other vertex in the subgraph.

# Key Points:
# - Tarjan’s algorithm finds all SCCs in O(V + E) time, where V is the number of vertices and E is the number of edges.
# - It uses a Depth First Search (DFS) strategy, with an additional low-link value to identify the head (root) of each SCC.
# - The algorithm can be visualized as tracking the earliest point a vertex can be reached in its DFS subtree.
# - Tarjan’s is more efficient than the naive approach of computing the transitive closure of the graph, which would take O(V^3).

# Example 1: Tarjan’s Algorithm for SCC (Debugging with print statements)

# Adjacency list for the directed graph
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3]
}

# Global variables for tracking the discovery times, low-link values, and the current state of the recursion
discovery_time = {}
low_link = {}
stack = []  # Stack to hold the vertices in the current SCC exploration
on_stack = {}  # Boolean map to track vertices currently on the stack
time = [0]  # Single-element list to maintain the current time during DFS exploration (needed due to Python's scoping rules)

# The recursive depth-first search (DFS) function
def dfs(vertex):
    print(f"Starting DFS at vertex {vertex}")  # Debugging output
    discovery_time[vertex] = low_link[vertex] = time[0]
    time[0] += 1  # Increment the global time counter
    stack.append(vertex)
    on_stack[vertex] = True  # Mark the vertex as being on the stack

    # Explore all neighbors of the current vertex
    for neighbor in graph[vertex]:
        if neighbor not in discovery_time:  # If the neighbor hasn't been visited yet
            print(f"Visiting unvisited neighbor {neighbor} from vertex {vertex}")
            dfs(neighbor)  # Perform DFS on the neighbor
            low_link[vertex] = min(low_link[vertex], low_link[neighbor])  # Update low-link value of the current vertex
        elif on_stack[neighbor]:  # If the neighbor is already on the stack, it's part of the current SCC
            print(f"Back edge detected from vertex {vertex} to {neighbor} (already on stack)")
            low_link[vertex] = min(low_link[vertex], discovery_time[neighbor])

    # After exploring all neighbors, check if the current vertex is the root of an SCC
    if low_link[vertex] == discovery_time[vertex]:
        print(f"Vertex {vertex} is a root of an SCC")
        scc = []
        while True:
            w = stack.pop()  # Pop vertices until we reach the root of the SCC
            on_stack[w] = False
            scc.append(w)
            if w == vertex:
                break
        print(f"Strongly Connected Component: {scc}")  # Output the SCC

# Initialize all the global variables for tracking discovery time and on-stack status
for v in graph.keys():
    discovery_time[v] = low_link[v] = -1
    on_stack[v] = False

# Start DFS from each unvisited vertex
for v in graph.keys():
    if discovery_time[v] == -1:  # Vertex hasn't been visited yet
        dfs(v)

# Use case: Tarjan's algorithm is particularly useful in analyzing dependency graphs, identifying cycles in scheduling problems, or determining the modular structure of complex systems.

# Explanation:
# The algorithm is based on depth-first search (DFS) but adds an additional layer of tracking "low-link" values for each vertex.
# These low-link values help in determining whether the current vertex can "reach back" to a previously visited vertex, forming a cycle or an SCC.
# The discovery time is used to track the order in which vertices are visited, while low-link is used to track the earliest visited vertex that can be reached.

# Runtime Analysis:
# - Best Case: O(V + E), where V is the number of vertices and E is the number of edges. This occurs regardless of graph structure since the algorithm only visits each edge and vertex once.
# - Worst Case: O(V + E) as well, as Tarjan's algorithm is linear in the number of vertices and edges.
# - Space Complexity: O(V), due to the need for the stack and auxiliary arrays to track discovery times and low-link values.

# Example 2: Advanced Insight with Edge Cases

# Consider a graph with no edges (isolated nodes). Each node is an SCC by itself.
# Graph:  {0: [], 1: [], 2: []}

graph_no_edges = {
    0: [],
    1: [],
    2: []
}

discovery_time.clear()
low_link.clear()
stack.clear()
on_stack.clear()
time[0] = 0

# Reinitialize tracking variables
for v in graph_no_edges.keys():
    discovery_time[v] = low_link[v] = -1
    on_stack[v] = False

# Start DFS from each unvisited vertex
for v in graph_no_edges.keys():
    if discovery_time[v] == -1:  # Vertex hasn't been visited yet
        dfs(v)

# Explanation:
# Even in graphs without edges, each vertex is considered an SCC because there's no path between vertices, making each one strongly connected to itself.
# This highlights a property of Tarjan's algorithm: in a graph with no connections, every vertex forms its own SCC.
# This behavior remains consistent, ensuring that the algorithm performs well under all graph structures, even when edge cases are involved.

# Advanced Tips:
# - In certain applications, Tarjan’s algorithm can be used for "cycle detection." If the SCC contains more than one vertex, a cycle exists.
# - Tarjan’s algorithm can be modified to detect articulation points or bridges by observing which vertices are the root of an SCC.
# - For graphs with millions of nodes and edges (e.g., social networks or web graphs), efficient implementations of Tarjan's algorithm are crucial for performance. Utilizing adjacency lists and iterators can save memory and improve performance.

#===============================================================================
# Algorithms, Graph Algorithms, Eulerian Path/Circuit
#===============================================================================

# Eulerian Path/Circuit is a fundamental graph theory concept that deals with traversing all edges in a graph.
# The Eulerian Path visits every edge exactly once, while the Eulerian Circuit is a path that starts and ends at the same vertex, 
# covering all edges exactly once. These algorithms are widely used in various applications like network analysis, 
# DNA sequencing, and route optimization.

# Key Points:
# - An Eulerian Circuit exists in a graph if and only if all vertices have an even degree (even number of edges connected to them).
# - An Eulerian Path exists if exactly zero or two vertices have an odd degree.
# - Both problems can be solved using depth-first search (DFS) or hierarchical algorithms, depending on the graph representation.

# Example 1: Simple illustration of checking for Eulerian Path and Circuit using vertex degrees.
# This example provides insights into how we can check for the existence of an Eulerian Path or Circuit.

# A simple graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# We will calculate the degree of each vertex
for vertex in graph:
    degree = len(graph[vertex])  # Degree is simply the number of adjacent vertices (edges connected to the vertex)
    print(f"Vertex {vertex} has degree {degree}")

# Explanation:
# This section calculates the degree of each vertex in the graph. The degree is the number of edges connected to the vertex.
# For a graph to have an Eulerian Circuit, all vertices should have even degrees.
# If exactly two vertices have odd degrees, the graph has an Eulerian Path but not a circuit.
# This can be used as a preliminary check before running any graph traversal algorithms like DFS or Hierholzer's Algorithm.

# Best Practice:
# - Ensure that the graph is connected before checking for an Eulerian Path or Circuit. 
#   If the graph is disconnected, it's impossible to have an Eulerian Path/Circuit because all edges won't be reachable.

# Example 2: Check if the graph has an Eulerian Path or Circuit by analyzing vertex degrees.

# Variables to track the number of odd-degree vertices
odd_degree_count = 0

# Loop over each vertex to count odd-degree vertices
for vertex in graph:
    degree = len(graph[vertex])  # Degree of current vertex
    if degree % 2 != 0:  # If degree is odd
        odd_degree_count += 1  # Increment the count of odd-degree vertices

# Now, determine if the graph has an Eulerian Path or Circuit
if odd_degree_count == 0:
    print("The graph has an Eulerian Circuit")
elif odd_degree_count == 2:
    print("The graph has an Eulerian Path but not an Eulerian Circuit")
else:
    print("The graph has neither an Eulerian Path nor an Eulerian Circuit")

# Explanation:
# We count the number of vertices with an odd degree. If there are no vertices with an odd degree, the graph has an Eulerian Circuit.
# If there are exactly two vertices with an odd degree, the graph has an Eulerian Path but not an Eulerian Circuit.
# If more than two vertices have odd degrees, neither an Eulerian Path nor an Eulerian Circuit exists.

# Pitfalls:
# - Forgetting to check for a connected graph before applying Eulerian Path/Circuit algorithms. 
#   Even if the degree conditions are satisfied, a disconnected graph can't have a valid path or circuit.
# - Not considering multi-edges (two or more edges between the same pair of vertices) can complicate the degree calculations.

# Example 3: Use case: Eulerian Circuit in a network traversal problem.
# Imagine a scenario where a mailman wants to walk every street (edge) in a neighborhood (graph) exactly once 
# and return to the starting point. This problem can be modeled as finding an Eulerian Circuit.

# In this case, the algorithm checks the degree of each intersection (vertex). If all intersections have an even degree,
# the mailman can traverse all streets and return to the starting point.

# The next example extends the concept and implements a simple Eulerian path using print statements to simulate the traversal.

# Example 4: Simple illustration of Eulerian Path traversal in an undirected graph.

# To simplify, let's assume the following graph for traversal:
simple_graph = {
    '0': ['1', '2'],
    '1': ['0', '2', '3'],
    '2': ['0', '1', '3'],
    '3': ['1', '2']
}

# Visited edges, starting from vertex '0'
visited_edges = []  # List to store the edges traversed

# Initial traversal starting at vertex '0'
start_vertex = '0'
current_vertex = start_vertex
print(f"Starting at vertex {start_vertex}")

# Traversing edges
while simple_graph[current_vertex]:  # Continue until all edges are traversed
    next_vertex = simple_graph[current_vertex].pop(0)  # Select and remove the first adjacent vertex (simulating traversal)
    print(f"Traversing edge {current_vertex} -> {next_vertex}")
    visited_edges.append((current_vertex, next_vertex))  # Track visited edge
    current_vertex = next_vertex  # Move to the next vertex

# If all edges are traversed, check if it's an Eulerian Path or Circuit
if current_vertex == start_vertex and not simple_graph[start_vertex]:
    print(f"All edges traversed, Eulerian Circuit found.")
else:
    print(f"All edges traversed, Eulerian Path completed but not a circuit.")

# Explanation:
# This example demonstrates a simple traversal of an Eulerian Path, simulating edge removal and visiting each vertex.
# In a real-world algorithm, Hierholzer’s algorithm would be used to efficiently traverse all edges in linear time.
# In this simulation, edges are visited one by one, and the traversal terminates when no more edges are left.
# Depending on whether the final vertex is the same as the starting point, the algorithm can determine if it's a circuit or a path.

# Runtime Analysis:
# - Best Case: O(E) where E is the number of edges. This happens if all edges can be traversed directly without significant backtracking.
# - Worst Case: O(E) - The algorithm must traverse all edges, but inefficiencies might arise if not properly optimized.

# Advanced Tip:
# - If the graph is large, consider using more advanced graph traversal techniques like Hierholzer's Algorithm, which is specifically 
#   designed for finding Eulerian circuits in O(E) time.
# - In directed graphs, the Eulerian Path/Circuit conditions slightly change: for a circuit, each vertex must have an equal in-degree and out-degree. 
#   For a path, one vertex must have an out-degree greater by one, and another vertex must have an in-degree greater by one.
# - Eulerian Path algorithms are particularly useful in bioinformatics, such as in genome assembly problems where DNA sequences are treated as edges in a graph.

#===============================================================================
# Algorithms, Graph Algorithms, Hamiltonian Path/Circuit
#===============================================================================

# Graph algorithms provide a way to traverse or search through graphs, which are structures made up of nodes (vertices)
# and edges (connections between nodes). One such set of algorithms deals with finding Hamiltonian paths and circuits.

# Hamiltonian Path:
# - A Hamiltonian path is a path in a graph that visits every vertex exactly once. 
# - Unlike the Eulerian path, which concerns itself with edges, the Hamiltonian path focuses on vertices.

# Hamiltonian Circuit:
# - A Hamiltonian circuit (or cycle) is a Hamiltonian path that is also a cycle, meaning it starts and ends at the same vertex.

# These problems are NP-complete, meaning no polynomial-time solution is known, and solving them for large graphs is computationally expensive.

# Example: Print whether a graph contains a Hamiltonian path
# For simplicity, this example uses a small undirected graph where the edges are defined as pairs of vertices.

# Vertices of the graph
vertices = [0, 1, 2, 3]

# Edges of the graph (represented as pairs of vertices)
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]

# Adjacency list representation of the graph
graph = {0: [1, 3, 2], 1: [0, 2], 2: [1, 3, 0], 3: [0, 2]}

# For a Hamiltonian Path, we need to visit all vertices exactly once
# Example: Check if a path visits all vertices

# Simple path representing a potential Hamiltonian path
path = [0, 1, 2, 3]

# Check if all vertices are visited exactly once
visited = set(path)  # Use a set to track visited vertices for efficiency
if len(visited) == len(vertices):  # Ensure all vertices are visited exactly once
    print(f"The path {path} visits all vertices once, potentially a Hamiltonian path.")
else:
    print(f"The path {path} does not visit all vertices, so it's not a Hamiltonian path.")

# Use case: Hamiltonian paths are used in optimization problems, such as the Traveling Salesman Problem (TSP),
# where the goal is to find the shortest Hamiltonian circuit.

# Common pitfall:
# - Ensure that the path doesn't revisit any vertex. If a vertex is visited more than once, the path is not Hamiltonian.

# Example: Print whether a path forms a Hamiltonian Circuit

# A Hamiltonian circuit must start and end at the same vertex
circuit = [0, 1, 2, 3, 0]  # Path starts and ends at vertex 0

# Check if the circuit visits all vertices once, excluding the starting/ending vertex
visited = set(circuit[:-1])  # Exclude the last vertex to avoid counting it twice
if len(visited) == len(vertices) and circuit[0] == circuit[-1]:  # All vertices visited, and start == end
    print(f"The path {circuit} is a Hamiltonian circuit.")
else:
    print(f"The path {circuit} is not a Hamiltonian circuit.")

# Best and Worst Case Complexity:
# - For small graphs, a brute-force approach might work, but the worst-case time complexity is O(n!), 
#   where n is the number of vertices. This factorial growth occurs because there are n! possible ways to arrange the vertices.
# - The best case (for certain graph structures) could involve early pruning using heuristics, but this is rare.

# Use case: Hamiltonian circuits are critical in routing and scheduling problems where a circular tour must visit every location.

# Advanced Tip:
# - For larger graphs, heuristic or approximation algorithms (like genetic algorithms or dynamic programming for the TSP) 
#   are used to find near-optimal solutions in reasonable time.
# - Backtracking is a common technique used to solve Hamiltonian Path/Circuit problems. It involves exploring potential paths
#   and abandoning ("backtracking") from paths that do not lead to a valid solution. Pruning unnecessary searches can 
#   significantly improve performance but does not reduce worst-case complexity.

# Example: Print the adjacency matrix of the graph for visualization
# The adjacency matrix is another way to represent a graph where each cell (i, j) is 1 if there is an edge between vertex i and j.

# Initialize an empty adjacency matrix with zeroes
adj_matrix = [[0] * len(vertices) for _ in range(len(vertices))]

# Fill the adjacency matrix based on the edges
for u, v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1  # Since the graph is undirected, both directions are valid

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Explanation:
# The adjacency matrix is a useful tool for visualizing the graph's structure.
# It's especially helpful for dense graphs, but for sparse graphs (graphs with fewer edges), an adjacency list like the one
# shown earlier is more space-efficient.
# - Time complexity for creating the adjacency matrix is O(n^2), where n is the number of vertices.
# - Accessing the matrix is O(1) for any specific vertex pair, which can be faster than an adjacency list in some cases.

# Advanced Pitfall:
# - Using an adjacency matrix for sparse graphs can lead to excessive memory usage, as it uses O(n^2) space regardless of how many edges exist.
# - For graphs with millions of vertices but few edges, this could become impractical. An adjacency list would be more efficient for such cases.

# Use case: Adjacency matrices are often used in algorithms where constant-time edge lookup is required, such as in graph-theoretical algorithms like the Floyd-Warshall algorithm for shortest paths.

# Final Remarks:
# - Hamiltonian path/circuit problems are crucial in many optimization and computational problems, but due to their NP-complete nature, they are computationally challenging.
# - Various approximation, heuristic, or even quantum algorithms may be explored to tackle these problems more efficiently for real-world applications.


#===============================================================================
# Algorithms, Dynamic Programming Algorithms, Fibonacci Sequence
#===============================================================================

# Dynamic programming is an optimization approach that solves problems by 
# breaking them into smaller subproblems. It is effective for problems where 
# overlapping subproblems and optimal substructure exist.
# The Fibonacci sequence is a classical example of such a problem.

# Example 1: Simple Fibonacci sequence with recursion
def fib_recursive(n):
    """
    A recursive function to calculate the nth Fibonacci number.
    
    Recursion is the simplest way to express the Fibonacci sequence. 
    However, this approach has exponential time complexity, O(2^n),
    since it recalculates the Fibonacci values multiple times for 
    the same input, resulting in inefficient performance for larger n.
    
    Best case: O(1) when n = 0 or n = 1 (base cases).
    Worst case: O(2^n) due to repeated calculations of subproblems.
    
    Use case: Conceptually simple for small n, but should not be used 
    in performance-critical applications.
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(10))  # Example use: Expected output is 55

# Potential pitfall: For large n, the recursive approach causes significant 
# performance bottlenecks due to recalculating subproblems. 
# For instance, fib_recursive(50) would take an unreasonably long time 
# to compute due to overlapping subproblems.

# Advanced tip: Recursion depth can be a concern with Python, especially 
# with large n. Python's default recursion limit (usually 1000) can 
# lead to a RecursionError for large inputs.
# It can be manually increased using sys.setrecursionlimit, but this is 
# not a recommended approach for performance optimization.

# Example 2: Optimized Fibonacci sequence using dynamic programming (memoization)
def fib_memoized(n, memo={}):
    """
    A dynamic programming approach using memoization to cache previously 
    computed Fibonacci values, avoiding redundant computations.
    
    Time complexity: O(n) since each Fibonacci number is calculated once 
    and stored in the memo.
    
    Space complexity: O(n) due to the extra space used by the memo dictionary.
    
    Best case: O(1) if the value is already in the memo.
    Worst case: O(n) if the value is not cached and needs to be computed.
    
    Use case: Suitable for large n as it significantly reduces the time 
    complexity while maintaining conceptual simplicity.
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]

print(fib_memoized(10))  # Example use: Expected output is 55

# Advanced insight: Memoization is one of the simplest forms of dynamic 
# programming, where previously computed results are reused. 
# This eliminates redundant calculations and transforms the recursive 
# O(2^n) complexity into O(n).

# Potential pitfall: Although memoization optimizes recursive approaches, 
# it still uses recursion, which can result in stack overflow for large n 
# in languages without tail call optimization, including Python.

# Example 3: Bottom-up approach for Fibonacci using dynamic programming (tabulation)
def fib_tabulation(n):
    """
    A bottom-up dynamic programming approach using tabulation.
    
    Time complexity: O(n), since it iterates from 0 to n once.
    
    Space complexity: O(1) because we only keep track of the last two Fibonacci 
    numbers, instead of maintaining the entire sequence.
    
    Best case: O(n), as the function must calculate each Fibonacci number up to n.
    Worst case: O(n), no redundant calculations but must iterate through all.
    
    Use case: Most efficient for very large n, both in terms of time and space.
    """
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fib_tabulation(10))  # Example use: Expected output is 55

# Advanced tip: The tabulation approach is often preferred in performance-critical 
# applications because it runs in O(n) time and O(1) space, making it the most 
# efficient solution for this problem in terms of both time and space.

# Potential pitfall: Though tabulation is more efficient, it can be slightly 
# harder to debug than memoization for those who are new to dynamic programming, 
# since it doesn't provide the intuitive recursive breakdown.

# Example 4: Matrix Exponentiation approach for Fibonacci sequence
def fib_matrix(n):
    """
    Fibonacci using matrix exponentiation to achieve O(log n) time complexity.
    
    The idea is based on the property of the Fibonacci sequence that can be 
    represented in matrix form, where repeated multiplication of the matrix 
    gives the nth Fibonacci number.
    
    Time complexity: O(log n), achieved by exponentiating the matrix.
    
    Space complexity: O(1), as only constant space is used.
    
    Best case: O(1) if n = 0 or n = 1.
    Worst case: O(log n), as we exponentially reduce the number of operations.
    
    Use case: Suitable for very large values of n where both time and space 
    optimization are critical.
    """
    def multiply_matrices(a, b):
        return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    def matrix_power(matrix, power):
        result = [[1, 0], [0, 1]]  # Identity matrix
        base = matrix
        while power:
            if power % 2 == 1:
                result = multiply_matrices(result, base)
            base = multiply_matrices(base, base)
            power //= 2
        return result

    if n <= 1:
        return n
    fibonacci_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fibonacci_matrix, n - 1)
    return result_matrix[0][0]

print(fib_matrix(10))  # Example use: Expected output is 55

# Advanced insight: Matrix exponentiation leverages the mathematical property 
# of Fibonacci and reduces the time complexity to O(log n) by utilizing the 
# divide-and-conquer approach of exponentiation by squaring.

# Potential pitfall: The matrix exponentiation approach is overkill for 
# smaller n and can introduce unnecessary complexity where O(n) algorithms 
# such as tabulation would suffice.

# Overall use case: Depending on the input size, different Fibonacci algorithms 
# are optimal. For small inputs, simple recursion or memoization works well.
# For large inputs, tabulation or matrix exponentiation are ideal.

#===============================================================================
# Algorithms, Dynamic Programming Algorithms, Knapsack Problem
#===============================================================================

# The knapsack problem is a classic problem where we are given a set of items,
# each with a weight and value, and a knapsack with a fixed capacity. The goal 
# is to determine the maximum value we can achieve by selecting items such that 
# their total weight does not exceed the knapsack capacity.

# This implementation uses dynamic programming to solve the problem, ensuring 
# that we avoid recomputation by storing intermediate results in a table.

# Example use case: Maximizing profit for a thief who can carry a limited weight 
# of goods but wants the highest value.

# Define the function to solve the knapsack problem using dynamic programming.
def knapsack(weights, values, capacity):
    # 'weights' is the list of weights for each item.
    # 'values' is the list of corresponding values for each item.
    # 'capacity' is the maximum weight the knapsack can carry.
    
    # The number of items is derived from the length of the weights or values list.
    n = len(weights)
    
    # Initialize a table where dp[i][j] represents the maximum value that can 
    # be achieved with the first 'i' items and a knapsack capacity of 'j'.
    # Using zero-based indexing, we create a table with (n+1) rows and (capacity+1) columns.
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    #===============================================================================
    # Fill the dynamic programming table
    #===============================================================================
    
    # Loop over each item (i) from 1 to n (inclusive).
    for i in range(1, n + 1):
        # Loop over each knapsack capacity (j) from 0 to 'capacity' (inclusive).
        for j in range(capacity + 1):
            
            # If the weight of the current item (weights[i-1]) is less than or equal 
            # to the current capacity (j), we have two choices:
            # 1. We don't take the item, which leaves the value as dp[i-1][j].
            # 2. We take the item, which adds the item's value (values[i-1]) 
            #    to the remaining capacity value (dp[i-1][j - weights[i-1]]).
            # We select the maximum of these two options.
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                # If the current item's weight exceeds the capacity, we can't take it,
                # so we just carry over the value from dp[i-1][j].
                dp[i][j] = dp[i - 1][j]
    
    #===============================================================================
    # Return the maximum value possible with all items and the full capacity.
    # The final answer will be in dp[n][capacity], where 'n' represents all items.
    #===============================================================================
    return dp[n][capacity]

#===============================================================================
# Example to illustrate how the function works:
#===============================================================================
weights = [1, 3, 4, 5]  # Weights of the items
values = [1, 4, 5, 7]   # Values of the items
capacity = 7            # Maximum capacity of the knapsack

# This call will output the maximum value that can be carried in the knapsack
print(knapsack(weights, values, capacity))  # Expected output: 9

#===============================================================================
# Explanation of Runtime and Space Complexity:
#===============================================================================

# Time Complexity: O(n * capacity)
# - We fill an n x capacity table, where 'n' is the number of items and 
#   'capacity' is the maximum weight the knapsack can carry.
# - For each item, we iterate through each possible capacity value from 0 to 'capacity'.
# - Best case: The algorithm will still iterate over the full table, 
#   so time complexity is consistently O(n * capacity).

# Space Complexity: O(n * capacity)
# - We use a 2D table to store the results of subproblems. The size of this table 
#   is (n+1) x (capacity+1), so space complexity is proportional to the number 
#   of items and the capacity of the knapsack.
# - If space is a concern, this can be optimized to O(capacity) using a 1D array 
#   by iterating in reverse to prevent overwriting values before they are used.
#===============================================================================

#===============================================================================
# Advanced Insights:
#===============================================================================
# 1. Handling floating-point weights/values: This algorithm assumes integer weights 
#    and values. For fractional knapsack problems (where you can take portions 
#    of an item), a greedy approach would be better suited. This can be a pitfall 
#    if the problem allows fractions, as the dynamic programming approach is not 
#    optimal in such cases.

# 2. Edge cases:
#    - If the capacity is zero, the maximum value is zero.
#    - If all items are heavier than the knapsack's capacity, the maximum value 
#      is zero.
#    - If all items have the same value-to-weight ratio, any combination that 
#      fills the knapsack can give the same result, so the algorithm needs 
#      careful consideration in such scenarios for alternate solutions.

# 3. Optimizations: In specific cases, such as when all weights are small integers, 
#    an optimized knapsack problem using bit manipulation or recursive memoization 
#    may outperform this dynamic programming table approach.

# 4. Real-world applications: The knapsack problem has applications in resource allocation,
#    financial portfolio optimization, cargo loading, and even file compression algorithms.
#===============================================================================

# 0/1 Knapsack Problem: Dynamic Programming Approach
# The 0/1 knapsack problem is a classic dynamic programming problem.
# The problem aims to maximize the total value in the knapsack without exceeding its weight capacity.
# Each item can either be included (1) or excluded (0), hence the name "0/1 knapsack".
# Unlike the fractional knapsack, in this problem, we cannot take a fraction of an item.

# Example setup:
# weights[] represents the weights of the items.
# values[] represents the corresponding values of the items.
# W represents the maximum weight capacity of the knapsack.
# n represents the total number of items.

def knapsack(W, weights, values, n):
    # Create a DP table where dp[i][j] represents the maximum value for a knapsack with
    # capacity j using the first i items. The table is initialized with zeros, as no value
    # can be obtained with 0 items or 0 capacity.
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    # Fill the DP table. We iterate over all items (1 to n) and weight capacities (0 to W).
    for i in range(n + 1):
        for w in range(W + 1):
            # Base case: When no items or capacity is 0, the max value is 0.
            if i == 0 or w == 0:
                dp[i][w] = 0
            # If the current item's weight is less than or equal to the current capacity `w`, 
            # we decide whether to include or exclude the item.
            # 1. Include the item: The value is the sum of the item's value and the maximum value
            #    of the remaining capacity (dp[i-1][w-weights[i-1]]).
            # 2. Exclude the item: The value is the maximum value obtained by excluding it (dp[i-1][w]).
            # We take the maximum of these two choices.
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            # If the item's weight exceeds the current capacity `w`, we cannot include it.
            # Thus, the value remains the same as without the current item (dp[i-1][w]).
            else:
                dp[i][w] = dp[i - 1][w]
    
    # After populating the table, the maximum value for the knapsack of capacity `W` using all `n` items
    # is stored at dp[n][W].
    return dp[n][W]

# Example use case:
# We have 4 items with the following weights and values:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
# The knapsack has a maximum weight capacity of 5.
W = 5
n = len(weights)

# We call the knapsack function to find the maximum value we can achieve.
print("Maximum value in knapsack =", knapsack(W, weights, values, n))

#===============================================================================
# Key insights for implementation and potential pitfalls:
#===============================================================================

# 1. Time Complexity:
#    - The time complexity of this dynamic programming solution is O(n * W), where `n` is the number of items,
#      and `W` is the knapsack's capacity. This is because we are filling a DP table with `n * W` elements.
#    - Space complexity is also O(n * W) due to the DP table.
#    - Best Case: Even in the best case (e.g., where we find the optimal solution early), the entire table
#      needs to be filled, leading to no reduction in the overall complexity.

# 2. Optimal Substructure:
#    - This algorithm leverages the optimal substructure property of dynamic programming.
#      The solution to the knapsack problem depends on solutions to smaller subproblems.
#      Specifically, the decision to include or exclude an item depends on the solution to smaller knapsack capacities.

# 3. Trade-offs: 
#    - Although this approach is efficient compared to brute force (which would have a complexity of O(2^n)), 
#      it still consumes a lot of space when `W` and `n` are large.
#    - In practice, we may encounter memory constraints when dealing with very large knapsack capacities or many items.

# 4. Space Optimization Insight:
#    - Instead of using a 2D table (O(n * W) space), we can optimize this solution to use O(W) space by storing only
#      the current and previous rows of the DP table. This optimization can reduce memory usage significantly.

#    Example space optimization (O(W) space):

def knapsack_optimized(W, weights, values, n):
    # Instead of a 2D array, we maintain a single array to store the current max values for all capacities.
    dp = [0 for x in range(W + 1)]
    
    # Iterate over all items.
    for i in range(n):
        # Traverse the dp array backward (from W to weights[i]), because we are updating
        # dp[w] based on the previous state, and we don't want to overwrite results prematurely.
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    # The result is stored at dp[W], which gives the maximum value for capacity W.
    return dp[W]

# Space-optimized example call:
print("Maximum value in knapsack (optimized) =", knapsack_optimized(W, weights, values, n))

#===============================================================================
# Best Practices:
#===============================================================================

# 1. Edge Case Handling:
#    - It's crucial to handle edge cases, such as when `W = 0` (zero capacity), or when there are no items (`n = 0`).
#    - The algorithm gracefully handles these by returning 0, as no value can be obtained in these cases.

# 2. Avoid Redundant Computations:
#    - Always make sure the DP table is filled iteratively (bottom-up) to avoid recomputing subproblems,
#      which is a common pitfall in recursive solutions.
#    - Recursive backtracking methods would require recalculating the same subproblems multiple times, leading
#      to exponential time complexity (O(2^n)).

# 3. Memory Management:
#    - Be mindful of memory usage, especially when handling large data sets. Use the space-optimized version
#      if memory is a limiting factor.

#===============================================================================
# Runtime Considerations:
#===============================================================================
# In this implementation, there are no explicit early exits, and the entire DP table must be filled,
# regardless of the items' values or weights. Thus, runtime depends purely on the input size (W and n).

# For inputs with large `W` and `n`, this algorithm is significantly better than brute force, 
# but can still be inefficient if either `n` or `W` grows too large. 
# In such cases, additional techniques like branch and bound or approximation algorithms may be needed.

#===============================================================================
# Example 1: Fractional Knapsack Algorithm using Greedy Approach
# This example demonstrates how the fractional knapsack problem can be solved using a greedy strategy. 
# The objective is to maximize the total value we can get by filling a knapsack of limited capacity
# with a given set of items, where each item has a weight and a value. Unlike the traditional knapsack 
# problem, here we are allowed to take fractional parts of items. This is why the greedy approach works
# optimally, as opposed to dynamic programming used in the 0/1 knapsack.
#===============================================================================

# Let's define a list of items with their respective weights and values
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)

# Define the maximum capacity of the knapsack
capacity = 50

# Step 1: Sort items based on the value-to-weight ratio in descending order.
# Sorting by v/w ensures that we are picking the most value-dense items first. This greedy approach
# guarantees the maximum value for the fractional knapsack problem.
items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

# Print out sorted items to verify correct sorting by value-to-weight ratio
print("Sorted items based on value-to-weight ratio:", items)

# Initialize variables for total value we will accumulate and the remaining capacity of the knapsack
total_value = 0
remaining_capacity = capacity

# Iterate through the sorted list of items
for value, weight in items:
    if remaining_capacity >= weight:
        # If the current item fits entirely in the remaining capacity, take it all
        total_value += value
        remaining_capacity -= weight
        print(f"Taking full item with value {value} and weight {weight}")
    else:
        # If the current item doesn't fit entirely, take only the fractional part that fits
        fraction = remaining_capacity / weight
        total_value += value * fraction  # Add the proportional value of the fraction taken
        print(f"Taking {fraction * 100:.2f}% of item with value {value} and weight {weight}")
        break  # Once the knapsack is filled, exit the loop

# Print the total value accumulated in the knapsack
print("Total value in knapsack:", total_value)

#===============================================================================
# Runtime Analysis:
# Sorting the items takes O(n log n) due to the sorting algorithm used. Iterating through the list to pick
# items is O(n). Therefore, the overall time complexity of the fractional knapsack problem is 
# O(n log n) because sorting dominates the iteration.

# Best Case: O(n log n) when all items can be fully taken, the runtime remains dominated by sorting.
# Worst Case: O(n log n), as sorting is always required, and the iteration still takes linear time.

# Insights:
# - This greedy approach works for the fractional knapsack because of the ability to take fractional
#   parts of items, which ensures optimal value by focusing on high value-to-weight ratios.
# - This would not work for the 0/1 knapsack problem, where an item must be either fully taken or
#   not taken at all; in such cases, dynamic programming would be needed for an optimal solution.
#===============================================================================


#===============================================================================
# Example 2: 0/1 Knapsack Problem using Dynamic Programming
# In the 0/1 knapsack problem, unlike the fractional version, items cannot be broken into fractional
# parts. This requires a different approach, namely dynamic programming, as a greedy solution
# would not always yield the optimal result.
#===============================================================================

# Define the list of items with their respective weights and values
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# Define the number of items
n = len(values)

# Create a 2D array 'dp' where dp[i][w] will store the maximum value that can be attained 
# with the first i items and a capacity of w
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Iterate through each item and capacity combination
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        # If the current item's weight is more than the current capacity, skip it
        if weights[i - 1] > w:
            dp[i][w] = dp[i - 1][w]  # Value carried forward without including the current item
        else:
            # Otherwise, consider the maximum value obtainable by either including or excluding the current item
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

        # Print the current state of the dp table for analysis
        print(f"dp[{i}][{w}] = {dp[i][w]}")

# The value in dp[n][capacity] will hold the maximum value that can be obtained with the full capacity
print("Maximum value in knapsack:", dp[n][capacity])

#===============================================================================
# Runtime Analysis:
# The time complexity of the dynamic programming approach is O(n * W), where n is the number of items and W 
# is the capacity of the knapsack. This is because we iterate over each item for each capacity value.
# Space complexity is also O(n * W) due to the use of a 2D array to store subproblem results.

# Best Case: O(n * W), no improvement since we must solve every subproblem.
# Worst Case: O(n * W), worst and best cases are the same for dynamic programming as all subproblems 
# must be computed.

# Insights:
# - The dynamic programming solution is optimal for the 0/1 knapsack because it explores all possible combinations
#   of items and capacities, ensuring that no potential solution is missed.
# - Dynamic programming can also be optimized in terms of space by using a 1D array, but it will still have
#   the same time complexity.
# - Pitfall: Although dynamic programming guarantees an optimal solution, it can be impractical for large 
#   values of capacity, leading to high memory usage.
#===============================================================================


#===============================================================================
# Example 3: Greedy Knapsack Solution - Edge Case
# Now let's examine an edge case where all items have the same value-to-weight ratio. In this scenario, 
# any item or fractional part of an item should yield the same value per unit weight, and the choice of 
# items becomes arbitrary as the greedy approach will perform equally for all of them.
#===============================================================================

# Define a list of items with identical value-to-weight ratios
items = [(30, 10), (60, 20), (90, 30)]  # (value, weight)

# Define the maximum capacity of the knapsack
capacity = 40

# Sort items based on the value-to-weight ratio
items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

# Initialize total value and remaining capacity
total_value = 0
remaining_capacity = capacity

# Iterate through the sorted items and fill the knapsack
for value, weight in items:
    if remaining_capacity >= weight:
        total_value += value
        remaining_capacity -= weight
    else:
        fraction = remaining_capacity / weight
        total_value += value * fraction
        break

print("Total value in knapsack (identical value-to-weight ratio):", total_value)

#===============================================================================
# Insights:
# - When all items have the same value-to-weight ratio, any combination of items will yield the same
#   value per unit of weight, and the selection becomes arbitrary.
# - The greedy approach still works, but it is important to recognize that in such cases, there is no 
#   advantage to sorting or specific selection of items since all are equivalent in terms of value-to-weight.
#===============================================================================

#===============================================================================
#   
# Algorithms, Dynamic Programming Algorithms, Longest Common Subsequence
#
#===============================================================================

# Print statement explaining the LCS problem:
print("The Longest Common Subsequence (LCS) is the longest sequence that can be obtained by deleting characters from two sequences, without changing their order.")

# Example 1: Basic LCS comparison between two strings
X = "AGGTAB"
Y = "GXTXAYB"

# Print statements showing the two strings that will be compared
print(f"Comparing strings X = {X} and Y = {Y}")

# n and m represent the lengths of the two strings
n = len(X)
m = len(Y)

#===============================================================================
# Initialize a 2D table for dynamic programming solution.
# The table stores lengths of LCSs for substrings.
# The size of the table is (n+1) x (m+1) because we also consider empty substrings.
#===============================================================================
# Table initialization: creating a (n+1) by (m+1) matrix filled with zeros.
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Print the initial DP table
print("Initialized DP table with zeros:")
for row in dp:
    print(row)

#===============================================================================
# Filling the DP table based on recurrence relation:
# If characters match, LCS length at (i, j) is 1 + LCS at (i-1, j-1)
# Otherwise, take the maximum of LCS at (i-1, j) or (i, j-1).
# This recurrence allows the algorithm to build the solution incrementally.
#===============================================================================
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if X[i - 1] == Y[j - 1]:  # If characters match
            dp[i][j] = dp[i - 1][j - 1] + 1
            print(f"Characters match: X[{i-1}] = Y[{j-1}] = {X[i-1]}, DP[{i}][{j}] updated to {dp[i][j]}")
        else:  # If characters don't match, take max value from either direction
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            print(f"Characters don't match: X[{i-1}] = {X[i-1]}, Y[{j-1}] = {Y[j-1]}, DP[{i}][{j}] updated to {dp[i][j]}")

#===============================================================================
# The final value at dp[n][m] contains the length of the LCS of X and Y.
# This is the core of dynamic programming: building the solution bottom-up
# to avoid recalculating overlapping subproblems.
#===============================================================================
lcs_length = dp[n][m]
print(f"The length of the Longest Common Subsequence is: {lcs_length}")

#===============================================================================
# Backtracking to find the LCS string:
# Starting from dp[n][m], trace back to reconstruct the LCS by checking matches.
#===============================================================================
lcs = []
i, j = n, m

while i > 0 and j > 0:
    if X[i - 1] == Y[j - 1]:  # If characters match, it's part of the LCS
        lcs.append(X[i - 1])
        print(f"Character {X[i-1]} is part of the LCS, moving diagonally to DP[{i-1}][{j-1}]")
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:  # Move in the direction of the larger value
        print(f"Moving up: DP[{i-1}][{j}] > DP[{i}][{j-1}], go to DP[{i-1}][{j}]")
        i -= 1
    else:
        print(f"Moving left: DP[{i}][{j-1}] >= DP[{i-1}][{j}], go to DP[{i}][{j-1}]")
        j -= 1

# The LCS will be constructed in reverse order, so we reverse the list
lcs.reverse()

# Print the final LCS
print("The Longest Common Subsequence is:", ''.join(lcs))

#===============================================================================
# Example 2: Edge cases to consider when working with the LCS algorithm
#===============================================================================

# Edge Case 1: Empty strings
X_empty = ""
Y_empty = ""
print(f"Comparing empty strings X = '{X_empty}' and Y = '{Y_empty}'")
n_empty = len(X_empty)
m_empty = len(Y_empty)

# Expected output: LCS length is 0 since there are no characters to compare
dp_empty = [[0] * (m_empty + 1) for _ in range(n_empty + 1)]
print(f"LCS length for empty strings: {dp_empty[n_empty][m_empty]}")

# Edge Case 2: One string is entirely different from the other
X_diff = "ABC"
Y_diff = "XYZ"
print(f"Comparing completely different strings X = '{X_diff}' and Y = '{Y_diff}'")
n_diff = len(X_diff)
m_diff = len(Y_diff)

# Expected output: LCS length is 0 since no characters match
dp_diff = [[0] * (m_diff + 1) for _ in range(n_diff + 1)]
for i in range(1, n_diff + 1):
    for j in range(1, m_diff + 1):
        if X_diff[i - 1] == Y_diff[j - 1]:
            dp_diff[i][j] = dp_diff[i - 1][j - 1] + 1
        else:
            dp_diff[i][j] = max(dp_diff[i - 1][j], dp_diff[i][j - 1])

print(f"LCS length for completely different strings: {dp_diff[n_diff][m_diff]}")

#===============================================================================
# Time Complexity Analysis:
# The time complexity of this dynamic programming approach is O(n * m),
# where n is the length of string X and m is the length of string Y.
# This is because we need to fill an n x m table.

# Space Complexity Analysis:
# The space complexity is also O(n * m) because we maintain a DP table of size (n+1) by (m+1).

# Best Case:
# In the best case, the two strings are identical, and the algorithm still needs to fill the entire DP table.
# So, the best-case time complexity remains O(n * m), as every element must still be processed.

# Worst Case:
# In the worst case, there are no common subsequences (like completely different strings).
# The time complexity is still O(n * m), as the DP table still needs to be fully populated.

#===============================================================================


#===============================================================================
# Algorithms, Dynamic Programming Algorithms, Longest Increasing Subsequence
#===============================================================================

# Example use case: Finding the longest subsequence of a sequence where all elements
# are sorted in increasing order. This has applications in pattern recognition, data 
# analysis, and several optimization problems.

#---------------------------------------------------------------------------------
# Problem Overview:
# Given an array of integers, the task is to find the length of the longest 
# increasing subsequence (LIS). A subsequence is defined as a sequence derived by 
# deleting some or no elements without changing the order of the remaining elements.

#---------------------------------------------------------------------------------
# Complexity Consideration:
# Time Complexity: O(n^2) - Two nested loops to compare each pair of elements
# Space Complexity: O(n) - A single DP array to store intermediate LIS values

# Best Case: If all elements are equal or strictly decreasing, each element is its 
# own subsequence, making the LIS of length 1. 
# Worst Case: If the array is strictly increasing, every element contributes 
# to the subsequence, making the LIS length equal to n.
#---------------------------------------------------------------------------------

# Step 1: Initialize the array
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

# The DP table will store the LIS value up to each index.
# Tip: Use a list initialized with 1s because the minimum LIS for any individual 
# element is 1 (each element is a subsequence by itself).
dp = [1] * len(arr)

# Step 2: Compute LIS using DP
# The outer loop fixes one element as the end of the subsequence.
for i in range(1, len(arr)):
    # The inner loop compares the current element with all previous elements
    for j in range(0, i):
        # If the current element is greater than a previous element, and the DP 
        # value at that previous element can help form a longer subsequence, 
        # we update the current DP value.
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)  # Update the LIS length at i
            # Advanced insight: 'max' ensures that we always track the longest 
            # subsequence possible for any given index i.

# Step 3: Output the result
# The length of the longest increasing subsequence is the maximum value in the DP array.
print("Length of Longest Increasing Subsequence is:", max(dp))

#-------------------------------------------------------
# Example:
# Input: arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# Output: Length of LIS = 6 
# Explanation: The LIS is [10, 22, 33, 50, 60, 80]
#-------------------------------------------------------

#=================================================================================================================
# Detailed Explanation:
#=================================================================================================================

# 1. Step 1 initializes the DP array, where dp[i] represents the length of the 
# longest increasing subsequence ending at index i. Each element starts with 
# a default value of 1, as the smallest possible subsequence is the element itself.

# 2. The outer loop iterates over each element of the array, treating each element 
# as the potential endpoint of an increasing subsequence. This loop runs O(n) times.

# 3. The inner loop runs O(n) times for each element, comparing it to all previous 
# elements. If a smaller element is found before the current element, and the 
# subsequence up to that smaller element combined with the current element forms 
# a longer subsequence than previously known, we update dp[i].

# 4. At the end of the nested loops, dp[i] will store the length of the LIS ending 
# at index i. The overall LIS for the entire array is the maximum value found in dp[].

#=================================================================================================================
# Uncommon Insight:
# - Though this algorithm solves the problem in O(n^2), there is a more efficient 
# O(n log n) approach using binary search and dynamic programming. However, this 
# O(n^2) approach is easier to implement and understand, making it useful for 
# educational purposes and small inputs.
#=================================================================================================================

#===============================================================================
# Example 2: Edge Case Handling
#===============================================================================

# Case: Array with all equal elements
arr_equal = [7, 7, 7, 7]
# All elements are equal, hence the LIS is of length 1, as no element can 
# form an increasing subsequence with any other element.
dp_equal = [1] * len(arr_equal)

# Process the DP logic
for i in range(1, len(arr_equal)):
    for j in range(0, i):
        if arr_equal[i] > arr_equal[j]:
            dp_equal[i] = max(dp_equal[i], dp_equal[j] + 1)

# Result for equal elements
print("LIS for array of equal elements:", max(dp_equal))

#-----------------------------------------------------------------------
# Runtime Analysis for Edge Case:
# Time Complexity: O(n^2) remains, as we still loop through all elements.
# However, since the array has no increasing pairs, the LIS remains 1.
#-----------------------------------------------------------------------

#===============================================================================
# Example 3: Handling Strictly Increasing Array
#===============================================================================

# Case: Strictly increasing array
arr_increasing = [1, 2, 3, 4, 5]
# In this case, every element forms part of the subsequence, so the LIS 
# length is equal to the length of the array itself.
dp_increasing = [1] * len(arr_increasing)

# Process the DP logic
for i in range(1, len(arr_increasing)):
    for j in range(0, i):
        if arr_increasing[i] > arr_increasing[j]:
            dp_increasing[i] = max(dp_increasing[i], dp_increasing[j] + 1)

# Result for strictly increasing array
print("LIS for strictly increasing array:", max(dp_increasing))

#-----------------------------------------------------------------------
# Runtime Analysis for Increasing Case:
# Best Case: O(n^2) remains unchanged, but dp[i] will always increase as 
# we move along the array. The final LIS equals the array length.
#-----------------------------------------------------------------------

#===============================================================================
# Example 4: Handling Strictly Decreasing Array
#===============================================================================

# Case: Strictly decreasing array
arr_decreasing = [5, 4, 3, 2, 1]
# In this case, no element can form an increasing subsequence with any 
# other element, so the LIS length is 1 for each element individually.
dp_decreasing = [1] * len(arr_decreasing)

# Process the DP logic
for i in range(1, len(arr_decreasing)):
    for j in range(0, i):
        if arr_decreasing[i] > arr_decreasing[j]:
            dp_decreasing[i] = max(dp_decreasing[i], dp_decreasing[j] + 1)

# Result for strictly decreasing array
print("LIS for strictly decreasing array:", max(dp_decreasing))

#-----------------------------------------------------------------------
# Runtime Analysis for Decreasing Case:
# The LIS remains 1, as no increasing subsequences are possible. The 
# time complexity is still O(n^2), but all comparisons fail to produce 
# an update in the dp[] array.
#-----------------------------------------------------------------------

#===============================================================================
# Algorithms, Dynamic Programming Algorithms, Edit Distance
#===============================================================================
# The Edit Distance problem is a classic dynamic programming problem used to 
# determine the minimum number of operations (insertions, deletions, substitutions) 
# required to convert one string into another. This is useful in many applications, 
# such as spell-checking, natural language processing, and bioinformatics (comparing DNA sequences).

# Example:
# Convert "kitten" to "sitting":
# - kitten -> sitten (substitute 'k' with 's')
# - sitten -> sittin (substitute 'e' with 'i')
# - sittin -> sitting (insert 'g')
# In this case, the edit distance is 3.

# Dynamic Programming Approach:
# A 2D table (matrix) is used to store the results of subproblems, ensuring each subproblem is only solved once.
# The matrix has dimensions (len(string1) + 1) x (len(string2) + 1).

# Each cell in the matrix represents the minimum number of operations needed to convert 
# the substring from string1[0...i] to string2[0...j].

# Time Complexity: O(m * n), where m is the length of string1 and n is the length of string2.
# This is because we fill an m x n matrix. This is the best case and worst case time complexity as well.

# Space Complexity: O(m * n), since we need a 2D table to store the intermediate results.
# Although this can be optimized to O(min(m, n)) if we only need the last row of the matrix at any given time.

def print_edit_distance(string1, string2):
    # Initialize variables to store lengths of input strings
    m = len(string1)
    n = len(string2)

    # Edge case: If either string is empty, the edit distance is the length of the other string.
    # (Insert all characters of the non-empty string)
    if m == 0:
        print(f"Edit distance (empty string to '{string2}'): {n}")
        return
    if n == 0:
        print(f"Edit distance ('{string1}' to empty string): {m}")
        return

    # Initialize the DP table with dimensions (m+1) x (n+1)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base cases:
    # If one string is empty, the only option is to insert all characters of the other string.
    for i in range(m + 1):
        dp[i][0] = i  # Cost of converting string1[0...i] to an empty string
    for j in range(n + 1):
        dp[0][j] = j  # Cost of converting an empty string to string2[0...j]

    # Fill the DP table row by row, column by column
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the current characters are the same, no new operation is needed. 
            # We take the result from the previous subproblem (i-1, j-1)
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Otherwise, we consider three possible operations:
                # 1. Insert: Convert string1[0...i] to string2[0...j-1], then insert string2[j]
                # 2. Delete: Convert string1[0...i-1] to string2[0...j], then delete string1[i]
                # 3. Substitute: Convert string1[0...i-1] to string2[0...j-1], then replace string1[i] with string2[j]
                # We take the minimum of these operations and add 1 (for the current operation)
                dp[i][j] = min(
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i - 1][j - 1] + 1  # Substitution
                )

    # The final answer, which is the edit distance between the two strings, 
    # will be in the bottom-right corner of the DP table (dp[m][n])
    print(f"Edit distance between '{string1}' and '{string2}': {dp[m][n]}")

#===============================================================================
# Example Use Cases
#===============================================================================

# Example 1: Strings with minimal differences
# 'cat' to 'cut' requires one substitution (replace 'a' with 'u')
print_edit_distance("cat", "cut")  # Output: 1

# Example 2: Strings with no common characters
# 'abc' to 'xyz' requires three substitutions
print_edit_distance("abc", "xyz")  # Output: 3

# Example 3: String conversion where insertions and deletions are needed
# 'kitten' to 'sitting' requires 3 operations (as described in the top comment)
print_edit_distance("kitten", "sitting")  # Output: 3

# Example 4: Converting a string to an empty string
# 'hello' to '' requires 5 deletions (one for each character)
print_edit_distance("hello", "")  # Output: 5

# Example 5: Converting an empty string to a non-empty string
# '' to 'world' requires 5 insertions (one for each character)
print_edit_distance("", "world")  # Output: 5

#===============================================================================
# Performance Considerations
#===============================================================================

# 1. If the input strings are very large, the O(m * n) time complexity can become a bottleneck.
#    In this case, an optimized approach using space optimization (reducing space complexity from O(m * n) to O(min(m, n))) can be implemented.
#    We only need to keep track of the current and previous rows of the DP table, as the rest are not required once processed.

# 2. For certain types of strings (e.g., those that share many common prefixes or suffixes), 
#    memoization or more advanced algorithms like the Wagner-Fischer algorithm can offer further performance improvements.

# 3. Edge cases such as empty strings, identical strings, or strings with entirely different characters 
#    should always be tested to ensure correct handling and prevent unnecessary computational overhead.

# 4. Practical applications such as DNA sequence analysis or text processing benefit greatly from this algorithm, 
#    but large-scale data often requires distributed or parallel computing techniques to handle the computational load.

# 5. Cache Efficiency: Given that the algorithm fills out a 2D table, memory locality is important.
#    Ensuring the table is filled row-wise (or column-wise consistently) can improve cache hits and thus performance.

#===============================================================================
# Coin Change Problem using Dynamic Programming
#===============================================================================

# Problem Overview:
# Given an integer amount and a list of coin denominations, find the minimum number of coins 
# that make up that amount. If the amount cannot be made up by any combination of the coins, 
# return -1. This is a classic example of a dynamic programming problem due to its overlapping 
# subproblems and optimal substructure properties.

# Dynamic programming approach:
# We create an array (dp) where dp[i] represents the minimum number of coins needed to make amount 'i'.
# The key idea is to break the problem down into smaller subproblems (solving for each amount from 0 
# to the target amount) and build the solution using previously computed results (bottom-up approach).

# Example use case:
# If the coins available are [1, 2, 5] and the target amount is 11, the minimum number of coins 
# required to make 11 would be 3 (5 + 5 + 1).

def coin_change(coins, amount):
    # Create an array for storing the results of subproblems
    # Initialize dp array with a very large number (float('inf')) because we're looking for the minimum
    # Using float('inf') ensures that any valid coin combination will overwrite this initial value
    dp = [float('inf')] * (amount + 1)
    
    # Base case: the minimum number of coins needed to make 0 amount is 0 (no coins are needed)
    dp[0] = 0
    
    # Iterate over each subproblem (amounts from 1 to 'amount')
    for i in range(1, amount + 1):
        # For each subproblem, check each coin
        for coin in coins:
            # Check if the current coin can be used (coin should be less than or equal to the current amount)
            if i - coin >= 0:
                # Transition equation: dp[i] = min(dp[i], dp[i - coin] + 1)
                # If we can use the current coin, we take the minimum between the current dp value 
                # and the value of the subproblem (amount - coin) plus 1 (since we used one coin)
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # After the loop ends, dp[amount] will either contain the minimum number of coins needed to make 'amount',
    # or it will still be float('inf') if it's impossible to make the amount with the given coins.
    # In case it's impossible, return -1
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage of the coin_change function:
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Expected output: 3 (coins used: 5 + 5 + 1)

#===============================================================================
# Detailed Explanation and Insights:
#===============================================================================

# dp Array Structure:
# dp is an array where each index i represents the minimum number of coins required to achieve the amount i.
# Example: dp[7] gives the minimum number of coins needed to make amount 7.

# The reason why dp[0] is initialized to 0 is because no coins are required to make the amount 0, 
# which serves as the base of our dynamic programming solution.

# Time Complexity:
# The time complexity of this approach is O(n * m), where n is the amount and m is the number of coins.
# This is because we iterate over every possible amount (n) and for each amount, we iterate over all the coins (m).

# Space Complexity:
# The space complexity is O(n) because we use a single array (dp) of size n + 1 to store the minimum number of coins.

# Worst Case:
# The worst case happens when none of the coins can be combined to form the target amount.
# In this case, the dp array never gets updated from its initial values (float('inf')), 
# and we return -1.

# Pitfalls to Avoid:
# 1. Forgetting to initialize dp[0] = 0. This is a critical base case because it allows us to 
#    start the dynamic programming recurrence correctly.
# 2. Using inappropriate values for initializing the dp array. Using float('inf') ensures that 
#    we always compute the minimum correctly and no valid combination of coins is missed.
# 3. Forgetting to handle the case where it's impossible to form the target amount (returning -1).

# Advanced Insight - Optimizing for Larger Inputs:
# If the list of coins contains large values (e.g., 1000, 5000, etc.), we might face performance 
# issues, especially for large amounts. One optimization technique is to sort the coins in descending 
# order and try to use the largest denominations first. This will lead to fewer recursive checks and 
# can slightly reduce the number of iterations required. However, it does not change the overall 
# time complexity.

# Edge Cases:
# - If the coins list is empty, the problem becomes unsolvable (dp[i] remains float('inf') for all i > 0).
# - If the amount is 0, we should always return 0 since no coins are required.
# - If all coin values are larger than the amount, it's impossible to make the change, so we return -1.
# - If the coins contain 1, the solution will always be possible (since any amount can be formed by 1s).

# Use Case Example 1:
# Coins: [2, 3, 5], Amount: 7
# The minimum number of coins to make 7 is 2 (using coins 2 + 5).
print(coin_change([2, 3, 5], 7))  # Expected output: 2

# Use Case Example 2:
# Coins: [2], Amount: 3
# It is impossible to make the amount 3 using only coin 2, so the function should return -1.
print(coin_change([2], 3))  # Expected output: -1

# Use Case Example 3:
# Coins: [1, 2, 5], Amount: 0
# Since the amount is 0, no coins are needed, so the expected output is 0.
print(coin_change([1, 2, 5], 0))  # Expected output: 0




#===============================================================================
# Algorithms, Dynamic Programming Algorithms, Matrix Chain Multiplication
#===============================================================================
# The matrix chain multiplication problem is about finding the most efficient way to multiply
# a sequence of matrices. The order of multiplying the matrices greatly affects the number of 
# scalar multiplications required. The objective is to minimize the number of these multiplications.
# This dynamic programming approach breaks the problem down into smaller subproblems.

# Example: 
# Given matrices A, B, C with dimensions 10x20, 20x30, 30x40,
# we need to compute (AB)C or A(BC) in such a way that minimizes cost.

#===============================================================================
# Importing necessary library
#===============================================================================
import sys  # sys library is used here to assign a large value to variables initially.

#===============================================================================
# Matrix Chain Multiplication function
#===============================================================================
def matrix_chain_order(p):
    """
    Function to determine the minimum number of multiplications needed to multiply the sequence of matrices.
    
    Args:
    p (list): A list where the i-th element represents the number of rows in the i-th matrix, 
              and the (i+1)-th element represents the number of columns in the i-th matrix.
              Hence, if A is a matrix of dimension 10x20, and B is 20x30, p = [10, 20, 30].
    
    Returns:
    m (2D list): A 2D list that stores the minimum number of multiplications for each subproblem.
    s (2D list): A 2D list that stores the split points for optimal multiplication sequence.
    """
    
    # Length of the input list p, which contains the matrix dimensions.
    n = len(p) - 1  # If p has length n+1, there are 'n' matrices.
    
    # Initialize the m and s tables.
    # m[i][j] will store the minimum cost (in terms of number of scalar multiplications)
    # for multiplying matrices Ai to Aj.
    m = [[0 for x in range(n)] for y in range(n)]  # Initialize to zero for subproblems of length 1.
    
    # s[i][j] will store the index at which to split the product for the optimal solution.
    s = [[0 for x in range(n)] for y in range(n)]  # Initialize for recording optimal splits.

    #===============================================================================
    # Main DP computation
    #===============================================================================
    
    # We start with chains of length 2 and increase the chain length progressively.
    # l is the chain length, i.e., how many matrices are being multiplied together.
    for l in range(2, n + 1):  # l ranges from 2 to n, starting with chain length 2.
        
        # i is the start index of the matrix chain.
        for i in range(n - l + 1):  # i varies from 0 to n-l (i.e., start of matrix chain)
            
            # j is the end index of the matrix chain.
            j = i + l - 1  # Ending matrix in the chain being considered.
            m[i][j] = sys.maxsize  # Initialize the cost to a very high value (infinity).
            
            # Try all possible splits and choose the one with the minimum cost.
            # k is the splitting point between matrices Ai and Aj.
            for k in range(i, j):
                #===============================================================================
                # Cost calculation for splitting between matrices Ak and Ak+1
                #===============================================================================
                
                # The cost of multiplying matrices A[i:k], A[k+1:j] and then multiplying the 
                # resulting two matrices.
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                
                # If the current cost is less than the previously recorded cost, update it.
                if cost < m[i][j]:
                    m[i][j] = cost  # Update the minimum cost for multiplying matrices from Ai to Aj.
                    s[i][j] = k  # Record the index of the split where the minimum cost occurs.
    
    #===============================================================================
    # Return values
    #===============================================================================
    
    # The m table stores the minimum multiplication cost for every subproblem.
    # The s table stores the optimal split points for reconstructing the solution.
    return m, s

#===============================================================================
# Helper function to print the optimal order of matrix multiplication
#===============================================================================
def print_optimal_parens(s, i, j):
    """
    Recursive function to print the optimal parenthesization of matrix multiplication.
    
    Args:
    s (2D list): The split points from the dynamic programming solution.
    i (int): Start index of the matrix chain.
    j (int): End index of the matrix chain.
    """
    if i == j:
        # Base case: If there's only one matrix, there's no need for parenthesis.
        print(f"A{i}", end="")
    else:
        # Recursive case: Split at the index k, print left and right recursively.
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])  # Print left subproblem.
        print_optimal_parens(s, s[i][j] + 1, j)  # Print right subproblem.
        print(")", end="")

#===============================================================================
# Example of usage
#===============================================================================
# Consider a chain of matrices A1 (10x20), A2 (20x30), A3 (30x40), A4 (40x30)
# The input p represents the matrix dimensions: A1 is 10x20, A2 is 20x30, and so on.
# Hence, p = [10, 20, 30, 40, 30]
p = [10, 20, 30, 40, 30]

# Compute the minimum cost of multiplying these matrices.
m, s = matrix_chain_order(p)

# Output the minimum number of multiplications required.
print(f"Minimum number of multiplications is: {m[0][len(p) - 2]}")

# Output the optimal parenthesization.
print("Optimal parenthesization is: ", end="")
print_optimal_parens(s, 0, len(p) - 2)
print()

#===============================================================================
# Time Complexity and Best/Worst Cases
#===============================================================================

# Time Complexity: The time complexity of this dynamic programming solution is O(n^3),
# where 'n' is the number of matrices (or len(p) - 1). This is because there are
# O(n^2) subproblems (for different chain lengths and subarrays), and each subproblem
# requires evaluating O(n) possible split points. Hence, O(n^3) total.

# Space Complexity: The space complexity is O(n^2) due to the storage of the m and s
# tables, each of which stores information for O(n^2) subproblems.

# Best Case: When the matrices are such that the split points minimize multiplications
# early in the sequence, the solution can be close to optimal quickly. However, this
# is determined dynamically, not via a predefined scenario.

# Worst Case: When the dimensions of matrices are such that no matter how we split them,
# the number of multiplications remains high (e.g., matrices with dimensions like 10x100, 
# 100x10, 10x100, which leads to high multiplications regardless of the order).

#===============================================================================
# Algorithms, Dynamic Programming Algorithms, Subset Sum Problem
#===============================================================================

# The subset sum problem is a classic NP-complete problem where, given a set of 
# non-negative integers and a target sum, we determine if there exists a subset 
# of the given set whose sum equals the target.

# The problem is typically solved using dynamic programming to avoid recalculating 
# the sum for different subsets repeatedly. Instead, we store intermediate results 
# in a table (a common DP approach known as memoization or tabulation).

# We will create a boolean table `dp` such that dp[i][j] will be True if there is a 
# subset of the first `i` elements that has a sum equal to `j`.

# Let's look at an example for better understanding:
# Example Set: [3, 34, 4, 12, 5, 2]
# Target Sum: 9
# Our goal is to find if there exists a subset with sum = 9.

# Initialize the set and the target sum
example_set = [3, 34, 4, 12, 5, 2]
target_sum = 9

#===============================================================================
# Initialize DP Table
#===============================================================================

# Initialize the DP table with dimensions (len(example_set) + 1) x (target_sum + 1)
# We add 1 to the lengths to account for the case where we have 0 elements or a sum of 0.

# Time complexity insight:
# The initialization here is O(n * m), where n is the number of elements in the set 
# and m is the target sum. This step ensures that we cover all possible subset sizes 
# (0 to len(set)) and all sums (0 to target_sum).

dp = [[False for _ in range(target_sum + 1)] for _ in range(len(example_set) + 1)]

#===============================================================================
# Base Case Initialization
#===============================================================================

# A subset with sum 0 is always possible by selecting no elements. Hence, we set 
# dp[i][0] to True for all `i`, meaning for any number of elements, a sum of 0 
# can always be achieved by selecting an empty subset.

for i in range(len(example_set) + 1):
    dp[i][0] = True

# Edge case:
# If the target_sum is 0, we automatically return True without needing to check 
# the elements of the set.

#===============================================================================
# Fill DP Table
#===============================================================================

# Now, we start filling the DP table. The idea is to iterate through each element 
# and update the table based on whether including or excluding the current element 
# can lead to the target sum.

# Iterate over each element in the set.
for i in range(1, len(example_set) + 1):
    # Iterate over each possible sum from 1 to target_sum.
    for j in range(1, target_sum + 1):
        # If the current element is greater than the sum we are checking (j), 
        # we cannot include it in the subset. Hence, we carry forward the result 
        # from the previous element (dp[i-1][j]).
        if example_set[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            # Otherwise, we check if either:
            # 1. We can form the sum without including the current element (dp[i-1][j])
            # 2. We can form the sum by including the current element (dp[i-1][j - example_set[i-1]]).
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - example_set[i - 1]]

# Runtime complexity analysis:
# The time complexity of filling the DP table is O(n * m), where n is the number 
# of elements in the set and m is the target sum. This is because for each element, 
# we check all possible sums from 1 to target_sum. The space complexity is also 
# O(n * m) due to the DP table size.

# Best Case: O(n), if the target sum is 0, we exit early.
# Worst Case: O(n * m), where n is the length of the set and m is the target sum.

#===============================================================================
# Final Output: Checking for Subset with Target Sum
#===============================================================================

# The result will be stored in dp[len(example_set)][target_sum], which indicates 
# whether a subset with the target sum exists using all available elements.

# Output whether a subset with the given target sum exists.
if dp[len(example_set)][target_sum]:
    print(f"A subset with the sum {target_sum} exists.")
else:
    print(f"No subset with the sum {target_sum} exists.")

# Potential pitfalls:
# 1. Be cautious about initializing the DP table and edge cases (like a target sum 
#    of 0 or an empty set).
# 2. Ensure that the condition example_set[i-1] > j is properly handled to avoid 
#    index out-of-bounds errors.
# 3. If you are working with large sets or target sums, consider space optimization 
#    strategies such as using a 1D DP table instead of a 2D table.

# Advanced optimization tip:
# Space optimization can be achieved by realizing that the DP table only requires 
# the current and previous row at any given time. Instead of maintaining a 2D array, 
# we can use a 1D array and update it iteratively. This reduces space complexity 
# from O(n * m) to O(m).

#===============================================================================
# Space Optimized Version of Subset Sum Problem
#===============================================================================

# The key insight for space optimization is that we only need the current and 
# previous states of the DP table, which allows us to reduce the space complexity 
# to O(m), where m is the target sum.

def subset_sum_optimized(set_, target):
    # Initialize a 1D DP array where dp[j] will be True if a subset with sum `j` 
    # can be formed.
    dp = [False] * (target + 1)
    
    # Base case: A sum of 0 can always be achieved with an empty subset.
    dp[0] = True

    # Iterate through each element in the set
    for num in set_:
        # Traverse the DP array backwards to ensure that each element is only 
        # considered once. This prevents overwriting results that depend on 
        # previous elements.
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    # The final result is in dp[target], indicating if we can form the target sum.
    return dp[target]

# Example Usage:
if subset_sum_optimized(example_set, target_sum):
    print(f"A subset with the sum {target_sum} exists (Optimized).")
else:
    print(f"No subset with the sum {target_sum} exists (Optimized).")

# Runtime complexity:
# The time complexity remains O(n * m), but the space complexity is reduced to O(m), 
# as we only maintain a 1D array. This optimization is particularly useful for 
# large sets or when memory is a constraint.
 # N-Queens problem solution using backtracking algorithm
# The goal is to place N queens on an NxN chessboard such that no two queens threaten each other.
# Queens can attack in horizontal, vertical, and diagonal directions.

# Function to print the board configuration
def print_board(board):
    """Prints the chessboard's current configuration."""
    # Loop through each row in the board
    for row in board:
        print(" ".join(row))  # Print each row's elements separated by spaces
    print()  # Print a blank line after the board for better readability

# Function to check if placing a queen at board[row][col] is safe
def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col). This checks all possible attacks."""
    
    # Check this row on the left side (no two queens can be in the same row)
    for i in range(col):
        if board[row][i] == 'Q':
            return False  # There's already a queen in this row to the left
    
    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False  # There's already a queen on the upper diagonal
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 'Q':
            return False  # There's already a queen on the lower diagonal
        i += 1
        j -= 1

    # If all checks pass, it's safe to place the queen here
    return True

# Function to solve the N-Queens problem using backtracking
def solve_n_queens(board, col):
    """Use backtracking to find all valid N-Queens solutions starting from column 'col'."""

    # Base case: If all queens are placed, print the solution
    if col >= len(board):
        print_board(board)  # Print the current board configuration as a solution
        return True  # Return True indicating that a valid solution is found
    
    res = False  # Flag to track if at least one solution exists
    
    # Try placing the queen in every row of this column
    for i in range(len(board)):
        # Check if placing the queen at (i, col) is safe
        if is_safe(board, i, col):
            # Place the queen at (i, col)
            board[i][col] = 'Q'
            
            # Recur to place the rest of the queens
            res = solve_n_queens(board, col + 1) or res
            
            # Backtrack: Remove the queen and try next possibility
            board[i][col] = '.'  # Reset the position for backtracking
    
    return res

# Function to initiate the N-Queens problem
def n_queens(N):
    """Initialize the chessboard and solve the N-Queens problem."""
    
    # Initialize the NxN board with empty spaces represented by '.'
    board = [['.' for _ in range(N)] for _ in range(N)]
    
    # Start solving from the first column (index 0)
    if not solve_n_queens(board, 0):
        print("No solution exists.")  # Print if no solution exists for the given N

# Example usage:
# Solve the N-Queens problem for N=4
n_queens(4)


# Example Sudoku Board (0s represent empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to print the board
def print_board(b):
    # Iterating through each row in the board
    for row in b:
        # Printing the current row
        print(row)
    print("\n")

# Check if it's valid to place a number in a given cell
def is_valid(b, num, pos):
    # First, check the row for duplicates
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            # If the number already exists in the row and it's not in the current column, it's invalid
            return False
    
    # Check the column for duplicates
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            # If the number exists in the column, it's invalid
            return False
    
    # Check the 3x3 box for duplicates
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # Iterate over the 3x3 sub-grid the current cell belongs to
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                # If number is found within the same sub-grid, it's invalid
                return False

    # If no conflicts are found, the placement is valid
    return True

# Find an empty cell on the board (cells with value 0)
def find_empty(b):
    # Iterating through every cell
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:  # Empty cell found
                return (i, j)  # Return the position (row, col)
    return None  # No empty cells left, puzzle might be solved

# Backtracking function to solve the Sudoku
def solve(b):
    # Print the current state of the board at each call of solve()
    print("Current board state:")
    print_board(b)
    
    # Find an empty position on the board
    find = find_empty(b)
    if not find:  # If there's no empty position, the board is solved
        print("Solved board state:")
        print_board(b)
        return True
    else:
        row, col = find

    # Try placing digits 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(b, num, (row, col)):
            print(f"Placing {num} at position {row, col}")
            b[row][col] = num  # Place the number

            # Recursively attempt to solve the rest of the board
            if solve(b):
                return True

            # If placing num didn't lead to a solution, reset the cell (backtrack)
            print(f"Backtracking from position {row, col}")
            b[row][col] = 0  # Reset the value

    # If no valid numbers can be placed, backtrack to the previous state
    return False

# Run the Sudoku solver and print the solved board
solve(board)

#=================================================================================
# Subset Generation Using Backtracking
#=================================================================================

# Example: Generating all subsets (also known as the power set) of a given list using backtracking.

def generate_subsets(nums):
    # The function takes a list of numbers and prints all possible subsets.
    
    # Edge case: if the list is empty, the only subset is the empty set itself.
    if not nums:
        print("Subset: []")  # base case for an empty input list
        return
    
    result = []  # this will store all generated subsets
    
    def backtrack(start, current_subset):
        # The backtrack function recursively builds subsets by either including or excluding the next element.
        
        # Print the current subset - this is a key step where we can see subsets as they are built.
        print(f"Current Subset: {current_subset}")
        
        # Advanced Insight: Once we have a valid subset, append it to the result list.
        # We use 'current_subset.copy()' to ensure we're not modifying the reference in subsequent operations.
        result.append(current_subset.copy())
        
        # Loop through the remaining elements starting from 'start'.
        for i in range(start, len(nums)):
            # Add nums[i] to the current subset.
            current_subset.append(nums[i])
            print(f"Include {nums[i]}: {current_subset}")  # print step after including element
            
            # Recurse to explore further subsets with this inclusion.
            backtrack(i + 1, current_subset)
            
            # Backtrack: Remove the last element to explore the next subset without this element.
            removed_element = current_subset.pop()  
            print(f"Backtrack (remove {removed_element}): {current_subset}")  # print step after excluding element

    # Starting the backtracking algorithm.
    backtrack(0, [])
    
    # Print the final result which contains all subsets.
    print(f"All subsets: {result}")

# Testing with an example
nums = [1, 2, 3]
generate_subsets(nums)

#=================================================================================
# Explanation of Key Components
#=================================================================================

# - 'nums': This is the input list for which we want to generate all possible subsets.
#   Example input: [1, 2, 3]. The expected output for this input will be all subsets of this list, 
#   including the empty subset, i.e., [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]].

# - 'result': This stores all generated subsets. It starts as an empty list and gets populated as the 
#   algorithm explores all possibilities. At each step of the backtracking process, the current subset 
#   is added to the result.

# - 'backtrack(start, current_subset)': The core recursive function that builds subsets by including 
#   or excluding the elements in 'nums'. 
#   Key insight: The 'start' index ensures that we only move forward in the list, preventing duplicates 
#   and revisiting the same element, which is essential for correct subset generation.

# Advanced Tips:
# - Backtracking works by recursively exploring all possibilities, but it only commits to a decision 
#   (like including an element in a subset) temporarily. By removing the element (i.e., "backtracking"), 
#   it ensures that the algorithm explores all paths. 
#   This makes the approach efficient and avoids unnecessary recalculations or duplicate subsets.

# - The use of 'current_subset.copy()' is a subtle but crucial point. If we directly append 'current_subset' 
#   to 'result', future modifications to 'current_subset' would also modify the subsets already in 'result'. 
#   Copying ensures that each subset is added as it is, without unintended side effects.

#=================================================================================
# Runtime Analysis
#=================================================================================

# Time Complexity: O(2^n)
# - Each element can either be included or excluded from a subset, leading to 2 choices for each element. 
#   Since there are 'n' elements, the total number of subsets is 2^n, and the time complexity is O(2^n).
#   In the worst case, where all elements are included in the subsets, the algorithm visits all possible 
#   subsets, resulting in exponential growth.

# Space Complexity: O(n)
# - The algorithm uses space proportional to the depth of the recursion tree, which is 'n'. Each recursive 
#   call requires space to store the current subset, so the space complexity is O(n).

# Best Case Scenario:
# - The best case occurs when the input list is empty. The algorithm immediately returns the empty subset, 
#   which requires O(1) time and space.

# Worst Case Scenario:
# - The worst case occurs when the input list is large (e.g., [1, 2, 3, ..., n]). The algorithm generates 
#   all 2^n subsets, leading to O(2^n) time and O(n) space usage.

# Uncommon Insights:
# - Backtracking is a general framework not just for subset generation but for solving many combinatorial 
#   problems like permutations, combinations, and even solving puzzles like Sudoku or N-Queens. The key 
#   idea is to explore all potential solutions and discard them when they lead to a dead end, which is 
#   the essence of backtracking.
# - You can easily modify this subset generation algorithm to handle additional constraints. For instance, 
#   if you wanted to generate only subsets of a certain size (e.g., k-sized subsets), you could add an 
#   additional condition in the backtracking function.

#=================================================================================
# Use Cases
#=================================================================================

# Subset generation is a powerful technique used in various fields:
# - In computer science, it is essential for solving combinatorial problems, like generating all possible 
#   configurations or testing all combinations of features.
# - In cryptography, subsets can help in brute-force attacks, where all possible key combinations are tried.
# - In dynamic programming problems, subset generation helps when we need to examine all possible subsets 
#   of data to find an optimal solution, such as the Knapsack problem.
# - In set theory and mathematical problems, subsets represent the building blocks for power sets.

# Example Use Case:
# - You can use this approach to generate all possible combinations of toppings for a pizza order. 
#   Given a list of toppings, this algorithm will output every possible combination of those toppings, 
#   which is useful for menu design or customer choice simulations.

#=================================================================================
# Permutations - All possible arrangements of a set of elements
#=================================================================================

# Function to generate permutations of a list using backtracking
# Example list for permutations: ['a', 'b', 'c']

# Step 1: Define the function that will handle the permutation logic
def generate_permutations(current_perm, remaining_items):
    # Base case: When no items are left, the current permutation is complete
    if not remaining_items:
        print(f"Complete permutation: {current_perm}")
        return

    # Iterate through all remaining items, choosing one item at a time
    for i in range(len(remaining_items)):
        # Backtracking approach: Choose an item, then generate permutations for the rest
        next_perm = current_perm + [remaining_items[i]]
        rest_items = remaining_items[:i] + remaining_items[i+1:]
        
        # Advanced insight: Notice how `remaining_items[:i] + remaining_items[i+1:]` removes the
        # chosen element at index `i`. This avoids modifying the original list (best practice).
        print(f"Current permutation: {next_perm} | Remaining items: {rest_items}")
        
        # Recursively call the function to continue building the permutation
        generate_permutations(next_perm, rest_items)

# Initialize with an empty permutation and the full list of items to permute
items = ['a', 'b', 'c']
generate_permutations([], items)
# Time Complexity: O(n!) - where n is the number of items, because for every element there are
# (n-1)! possible permutations of the rest.
# Space Complexity: O(n!) - storing all permutations.

# Note: Recursive depth is limited by the number of items (n), as each recursive call picks one item.
# Pitfall: Deep recursion could cause a stack overflow for larger lists in languages without tail call optimization.
# In Python, be cautious about the recursion limit with larger input sizes (e.g., >1000 items).

#=================================================================================
# Combinations - All possible selections of elements (order doesn't matter)
#=================================================================================

# Step 1: Define the function that will generate combinations
def generate_combinations(current_comb, remaining_items, k):
    # Base case: When the current combination reaches the desired size `k`
    if len(current_comb) == k:
        print(f"Complete combination: {current_comb}")
        return

    # Iterate through the remaining items to pick elements for the combination
    for i in range(len(remaining_items)):
        # Backtracking approach: Choose an item and generate combinations for the rest
        next_comb = current_comb + [remaining_items[i]]
        rest_items = remaining_items[i+1:]  # Exclude the current element and all prior elements
        
        # Advanced insight: Notice how we exclude elements prior to the current index.
        # This ensures we only move forward in the list, preventing duplicate combinations.
        print(f"Current combination: {next_comb} | Remaining items: {rest_items}")
        
        # Recursively call the function to continue building the combination
        generate_combinations(next_comb, rest_items, k)

# Initialize with an empty combination and the full list of items
items = ['a', 'b', 'c']
k = 2  # Choose 2 elements at a time
generate_combinations([], items, k)
# Time Complexity: O(nCk) - where n is the number of items and k is the number of elements per combination.
# In combinations, the time complexity is often expressed as "n choose k", which is n! / (k! * (n-k)!)
# Space Complexity: O(nCk) - due to storing combinations.

# Best Case: We immediately find the desired combination size `k` when iterating, and the recursive calls are minimal.
# Worst Case: The function has to explore all possible combinations, making O(nCk) recursive calls.

# Pitfall: Similar to permutations, be aware of recursion limits when dealing with large input sizes or `k`.

#=================================================================================
# Advanced Example: Generate Permutations of Strings with Duplicates
#=================================================================================

# If the list of items has duplicates, we may want to avoid generating the same permutation multiple times.
# Use a set to avoid duplicate permutations.

def generate_unique_permutations(current_perm, remaining_items, used_permutations):
    # Base case: When no items are left, the current permutation is complete
    if not remaining_items:
        # If this permutation is new, print it
        perm_tuple = tuple(current_perm)  # Tuples are hashable, so they can be added to sets
        if perm_tuple not in used_permutations:
            used_permutations.add(perm_tuple)
            print(f"Unique permutation: {current_perm}")
        return

    for i in range(len(remaining_items)):
        # Same backtracking logic, but now we track seen permutations
        next_perm = current_perm + [remaining_items[i]]
        rest_items = remaining_items[:i] + remaining_items[i+1:]
        
        print(f"Current unique permutation attempt: {next_perm} | Remaining items: {rest_items}")
        generate_unique_permutations(next_perm, rest_items, used_permutations)

# Initialize with an empty permutation, the list, and an empty set to store used permutations
items_with_duplicates = ['a', 'b', 'b']
used_permutations = set()
generate_unique_permutations([], items_with_duplicates, used_permutations)
# Time Complexity: Still O(n!) for permutations, but the set ensures each is only generated once.
# Advanced Insight: Using sets for uniqueness checking adds an O(1) average time complexity check for each permutation.

# Space Complexity: O(n!) - The set stores permutations as tuples, and permutations are generated recursively.
# Tip: For larger lists, managing memory for large sets can become an issue; consider iterative approaches or memory-efficient algorithms.

# Common Pitfall: If you don't track used permutations, duplicate permutations will appear.
# Ensure the elements you choose to permute have unique identifiers when generating combinations or permutations of objects.

#=================================================================================
# Rat in a Maze Problem - Backtracking Algorithm
#=================================================================================

# This problem involves finding a path for a rat from the top-left corner to the bottom-right corner
# of a maze. The maze is represented by a grid (2D array), and the rat can move only right or down.
# Cells that are part of the path will be marked as 1, and obstacles (blocked cells) are marked as 0.

# Let's start by setting up the grid (maze). This is a simple 4x4 maze for demonstration purposes.
maze = [[1, 0, 0, 0],  # Start point is maze[0][0]
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]  # Destination is maze[3][3]

# The solution path will be stored in another grid of the same size as the maze. Initially,
# all cells are set to 0, indicating no path is found yet.
solution = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

# Now, we define a utility function that checks if a move to a particular cell (x, y) is valid.
# A valid move is when:
# 1. The cell is within the grid boundaries.
# 2. The cell is not blocked (i.e., maze[x][y] == 1).
def is_valid_move(maze, x, y):
    """Checks if (x, y) is a valid move in the maze."""
    if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 1:
        return True  # Move is valid if inside bounds and not blocked
    return False  # Invalid move if out of bounds or blocked

# Runtime analysis for `is_valid_move`:
# - Time complexity: O(1) because we are only checking conditions on the given coordinates.
# - Space complexity: O(1), no extra space is used aside from input parameters.

# The main function to solve the maze using backtracking is `solve_maze`.
# The function recursively attempts to move the rat through the maze by exploring all possible moves.
def solve_maze(maze, x, y, solution):
    """Attempts to solve the maze using backtracking starting from (x, y)."""
    
    # Base case: If the rat reaches the bottom-right corner of the maze (destination).
    if x == len(maze) - 1 and y == len(maze[0]) - 1 and maze[x][y] == 1:
        solution[x][y] = 1  # Mark the destination cell as part of the path
        return True  # Solution found, end recursion

    # Check if the current move (x, y) is valid
    if is_valid_move(maze, x, y):
        # Mark the current cell as part of the path
        solution[x][y] = 1

        # Explore the possibility of moving right (x, y + 1)
        if solve_maze(maze, x, y + 1, solution):
            return True  # Return true if moving right leads to a solution

        # If moving right fails, explore moving down (x + 1, y)
        if solve_maze(maze, x + 1, y, solution):
            return True  # Return true if moving down leads to a solution

        # Backtracking: If neither move works, unmark the current cell and return false.
        # This is the essence of the backtracking algorithm: undoing moves that don't work.
        solution[x][y] = 0

    # Return false if no solution exists from this point
    return False

# Runtime analysis for `solve_maze`:
# - Best case: O(M+N) where M is the number of rows and N is the number of columns, occurs when there is
#   a clear path without backtracking.
# - Worst case: O(2^(M+N)) in cases where the maze is filled with obstacles and the algorithm explores every possible path.
# - Space complexity: O(M * N) due to the recursive call stack and the solution matrix.

# Use case 1: Solving a simple 4x4 maze
if solve_maze(maze, 0, 0, solution):
    # If a solution exists, print the solution path
    for row in solution:
        print(row)
else:
    # If no solution exists, print "No solution found."
    print("No solution found.")

# Advanced tip: The algorithm can be optimized in certain scenarios by using techniques such as dynamic programming
# or memoization to avoid redundant calculations, although these are not commonly needed in standard backtracking.

# Common pitfall: Not marking the current cell as unvisited during backtracking can lead to infinite loops
# or incorrect paths. Always ensure that cells are "unmarked" if the current path doesn't lead to a solution.

# Example 2: Edge case - if the maze has no valid solution
maze_no_solution = [[1, 0, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1]]

solution_no_solution = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

if solve_maze(maze_no_solution, 0, 0, solution_no_solution):
    for row in solution_no_solution:
        print(row)
else:
    print("No solution found.")  # Expected output: "No solution found." since no path exists.

#=================================================================================
# Algorithms, Greedy Algorithms
#=================================================================================

# Greedy algorithms build up a solution piece by piece, always choosing the next piece 
# that offers the most immediate benefit (greedily) without considering the overall problem.
# Greedy algorithms are generally efficient but do not always produce the globally optimal solution.
# They work well when the problem has the 'greedy-choice property,' meaning a locally optimal choice 
# leads to a globally optimal solution.

# Example 1: Coin change problem
# Given an amount of money, the goal is to make change using the fewest number of coins
# This is a classic example of a problem that can be solved by a greedy algorithm, assuming
# the coin denominations are such that the greedy strategy produces an optimal solution.

print("Greedy algorithm: Coin change problem")

# We start with an example where the coin denominations are [1, 5, 10, 25]
# We are asked to make change for a total of 67 cents.
# The greedy algorithm works by selecting the largest coin denomination that is less than or equal
# to the remaining amount.

amount = 67  # Total amount of change required
coins = [25, 10, 5, 1]  # Available denominations in descending order

# Initialize an empty list to hold the selected coins
selected_coins = []

# Greedily select coins
# Time complexity of this loop: O(n) where n is the number of coin denominations
# This is because the loop checks each denomination once
# In this case, n = 4 (for the 4 coin denominations), which is constant time in practice
while amount > 0:
    for coin in coins:
        if coin <= amount:  # Greedy choice: pick the largest coin that fits the remaining amount
            print(f"Selected coin: {coin}")
            selected_coins.append(coin)  # Add the coin to the solution
            amount -= coin  # Reduce the remaining amount
            print(f"Remaining amount: {amount}")
            break  # Break and start over to make another greedy choice

# This algorithm works optimally in cases where coin denominations are well-suited (e.g., US coins).
# But it doesn't guarantee optimality in cases where denominations are irregular (e.g., 1, 3, 4).
# In such cases, a dynamic programming approach would be necessary for optimality.

print(f"Selected coins for making change: {selected_coins}")

#==============================================================
# Considerations:
#==============================================================

# Best case: If the amount is an exact multiple of the largest denomination (e.g., 25, 10), 
# the algorithm will finish quickly. The best-case runtime is O(1) because the first coin immediately solves the problem.

# Worst case: The worst-case runtime occurs when the algorithm has to iteratively subtract small denominations.
# Example: making change for 99 cents, where 4 steps of 25 cents each and then multiple smaller coins are needed.
# The worst-case time complexity remains O(n), but the number of steps grows depending on how many coins must be chosen.

# Runtime analysis:
# Overall time complexity is O(n) where n is the number of coin denominations.
# The algorithm loops over each coin denomination, but the overall number of coins used is relatively small 
# (bounded by the amount), so in practice, this algorithm is fast.

# Limitations and improvements:
# 1. This algorithm works for denominations like [1, 5, 10, 25] but would fail for irregular denominations
# like [1, 3, 4] since the greedy approach doesn't yield optimal results for such combinations.
# 2. In real-world applications, testing for the greedy-choice property is important to ensure optimality.

# Example 2: Greedy algorithm for interval scheduling
# The problem is to select the maximum number of non-overlapping intervals from a set of intervals.
# This is a classic greedy problem where at each step, the algorithm selects the interval that finishes the earliest.

print("Greedy algorithm: Interval scheduling problem")

# Given a set of intervals [(1, 3), (2, 5), (4, 6), (6, 8)], the goal is to select the maximum number
# of non-overlapping intervals. In this case, we choose the interval that ends the earliest at each step.

intervals = [(1, 3), (2, 5), (4, 6), (6, 8)]

# Step 1: Sort intervals by their ending time
# This ensures that we can always select the interval that finishes the earliest, maximizing the remaining time.
# Time complexity: O(n log n) due to sorting, where n is the number of intervals.
intervals.sort(key=lambda x: x[1])
print(f"Sorted intervals by end time: {intervals}")

# Initialize a list to store selected intervals
selected_intervals = []

# The first interval is always selected because it ends the earliest after sorting.
# Time complexity: O(n) to iterate through the intervals after sorting.
selected_intervals.append(intervals[0])
print(f"Selected interval: {intervals[0]}")

# Greedily select the next non-overlapping interval
for i in range(1, len(intervals)):
    if intervals[i][0] >= selected_intervals[-1][1]:  # Check if the current interval starts after the last selected ends
        selected_intervals.append(intervals[i])
        print(f"Selected interval: {intervals[i]}")

# Final list of selected intervals
print(f"Selected non-overlapping intervals: {selected_intervals}")

#==============================================================
# Considerations:
#==============================================================

# Best case: The algorithm performs well when intervals are already sorted by end time. In this case, the sort step
# becomes trivial, and the greedy selection runs in O(n).

# Worst case: The worst case occurs when the intervals are given in reverse order, requiring a full sort
# before the selection process can start. This results in an O(n log n) time complexity.

# Runtime analysis:
# The overall time complexity is O(n log n) because of the sorting step. After sorting, the selection of intervals
# runs in O(n). Therefore, the overall complexity is dominated by the sorting operation.

# Limitations and improvements:
# 1. This approach works optimally only when intervals are not overlapping.
# 2. A potential improvement could be parallel processing to handle multiple batches of interval selections
# if the input size becomes very large.
# 3. Another advanced technique might involve segment trees for range queries, reducing the need for sorting
# in certain complex scenarios.


#=================================================================================
# Topic: Algorithms, Greedy Algorithms, Activity Selection Problem
#=================================================================================

# The activity selection problem is a classic problem that can be solved efficiently using a greedy algorithm.
# Given a set of activities with start and finish times, the goal is to select the maximum number of activities
# that don't overlap with each other. This problem demonstrates how a greedy choice at each step can lead to an optimal solution.

# Initial input: a list of activities, where each activity has a start and finish time.
# Greedy choice: always pick the next activity that finishes the earliest and is compatible with previously selected activities.

#---------------------------------------------------------------------------------
# Subtopic: Input definition and edge cases
#---------------------------------------------------------------------------------
# Example scenario 1: activities sorted by their finish times
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

# This input represents 11 activities, where each tuple (a, b) is an activity that starts at time 'a' and finishes at time 'b'.
# The activities are unsorted in this example, but the algorithm will work as long as we first sort them by finish time.

#---------------------------------------------------------------------------------
# Subtopic: Sorting activities by finish time
#---------------------------------------------------------------------------------
# Sort the activities by their finish time. This is a key step in the greedy algorithm because 
# choosing the activity that finishes the earliest increases the chance of selecting more activities.
activities.sort(key=lambda x: x[1])

# Sorting the activities has O(n log n) runtime complexity due to the nature of Python's Timsort.
# Sorting ensures that the activity that leaves the most time for other activities (by finishing the earliest) is considered first.

#---------------------------------------------------------------------------------
# Subtopic: Initializing the first selection
#---------------------------------------------------------------------------------
# Select the first activity since it finishes the earliest and by definition does not conflict with any prior activity.
selected_activities = [activities[0]]

# This operation is O(1), as we are simply initializing the first activity as the selected one.
# Potential Pitfall: Ensure that the list of activities is not empty to avoid an index error here.

#---------------------------------------------------------------------------------
# Subtopic: Iterating through the remaining activities
#---------------------------------------------------------------------------------
# Iterate over the sorted activities starting from the second one.
# For each activity, check if its start time is after or exactly when the last selected activity finishes.
for i in range(1, len(activities)):
    # If the current activity starts after the last selected activity finishes, select it.
    if activities[i][0] >= selected_activities[-1][1]:
        selected_activities.append(activities[i])

# This loop has O(n) complexity, where 'n' is the number of activities. We iterate over the activities exactly once.
# Best-case scenario: All activities are compatible (O(n) after sorting).
# Worst-case scenario: No activities are compatible (O(n) after sorting).
# Greedy Insight: We are making a local optimal choice (earliest finish time) at each step, ensuring that we maximize the number of non-overlapping activities.

#---------------------------------------------------------------------------------
# Subtopic: Output the result
#---------------------------------------------------------------------------------
# The selected_activities list now contains the maximum number of non-overlapping activities.
print("Selected Activities:", selected_activities)

# Print operation is O(1) but depends on the number of selected activities, making it technically O(k), where k is the number of selected activities.

# Example scenario 2: Input with fewer activities
# Edge case: Input with only one activity
activities_small = [(2, 3)]
activities_small.sort(key=lambda x: x[1])  # Sorting still takes place, but it's trivial in this case.
selected_activities_small = [activities_small[0]] if activities_small else []  # Handling empty list edge case.
print("Selected Activities for small input:", selected_activities_small)

# In this case, sorting is O(1) due to the small input size, and the selection loop is trivial.
# Handling an empty list ensures that no operations fail and the algorithm gracefully handles edge cases like no activities being provided.

# Example scenario 3: Large dataset of activities
# For large datasets (e.g., thousands of activities), the complexity breakdown becomes more significant.
# Sorting O(n log n) dominates, and the selection process remains O(n), making this algorithm very efficient for larger inputs.

#---------------------------------------------------------------------------------
# Subtopic: Greedy Algorithm Justification
#---------------------------------------------------------------------------------
# The greedy approach works because:
# 1. Selecting the activity that finishes the earliest leaves the maximum possible room for subsequent activities.
# 2. No other selection strategy (e.g., selecting the longest or selecting based on start time) provides an optimal solution.
# 3. This local optimal choice (earliest finish) leads to a global optimal solution (maximum number of activities).

#---------------------------------------------------------------------------------
# Subtopic: Advanced Considerations
#---------------------------------------------------------------------------------
# 1. If the activities are already sorted by finish time, the sorting step can be skipped, reducing the time complexity to O(n).
# 2. Modifying the problem: If the activity durations are also of interest (e.g., to maximize total time spent in activities),
#    this would no longer be solvable by a greedy approach. In that case, dynamic programming or other strategies may be necessary.
# 3. Edge cases: What if two activities have the same finish time? The algorithm still works, as ties in finish time do not affect the
#    compatibility check. However, for other variations, such as prioritizing shorter activities when finish times are tied, modifications
#    would be required.


#=================================================================================
# Example of a Greedy Algorithm: Huffman Coding for Optimal Data Compression
#=================================================================================

# Input: A string of characters, where each character has a frequency of occurrence.
# The goal is to minimize the total length of the encoded data using a binary tree.
# Huffman coding is a lossless data compression algorithm that works by assigning 
# variable-length codes to characters based on their frequencies.

# Let's begin by considering a basic input, a frequency table of characters
char_freq = [('a', 45), ('b', 13), ('c', 12), ('d', 16), ('e', 9), ('f', 5)]

#=================================================================================
# Step 1: Build a Min-Heap (Priority Queue)
#=================================================================================
# Huffman coding requires repeatedly extracting the two lowest frequency nodes,
# making this data structure an optimal choice for efficient extraction of minimum elements.

# Import heapq, which provides an implementation of a priority queue
import heapq

# The heapq library transforms a list into a min-heap, ensuring the smallest element 
# is always accessible in O(1) time, with insertion and deletion costing O(log n).
heap = [[weight, [char, ""]] for char, weight in char_freq]

# heapq.heapify() efficiently rearranges the list into a heap structure in O(n) time
# This is a critical optimization step, especially for large inputs.
heapq.heapify(heap)

#=================================================================================
# Step 2: Build the Huffman Tree
#=================================================================================
# We repeatedly combine the two lowest frequency nodes until one node remains, 
# which becomes the root of the Huffman tree.

while len(heap) > 1:
    # Extract the two nodes with the smallest frequency values
    lo = heapq.heappop(heap)  # O(log n) to remove the smallest element
    hi = heapq.heappop(heap)  # O(log n) to remove the next smallest element
    
    # Assign binary codes: 0 to one subtree, 1 to the other
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    
    # Combine the two nodes and push the result back into the heap
    # The new node's frequency is the sum of the two combined nodes
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])  # O(log n) insertion

# At this point, the heap contains the root node of the Huffman tree
huffman_tree = heap[0]

#=================================================================================
# Step 3: Extract the Huffman Codes
#=================================================================================
# Traverse the tree to extract the Huffman codes for each character. Since we 
# assign shorter codes to more frequent characters, the encoded data is minimized.

# Huffman codes are stored in the second element of each pair in huffman_tree[1:]
huffman_codes = sorted(huffman_tree[1:], key=lambda p: (len(p[-1]), p))
print("Huffman Codes:")
for char, code in huffman_codes:
    print(f"{char}: {code}")

#=================================================================================
# Performance and Runtime Analysis
#=================================================================================

# Step 1: Min-Heap Construction:
#   heapq.heapify() operates in O(n) time, where n is the number of characters.
#   This is due to the nature of heaps, where reordering a list of size n requires
#   O(n) comparisons in a bottom-up manner.

# Step 2: Huffman Tree Construction:
#   The while loop executes n-1 times, as we combine two nodes at a time until only
#   one node remains. For each iteration, the heap operations (pop and push) take O(log n),
#   resulting in an overall complexity of O(n log n) for building the Huffman tree.

# Step 3: Extracting Huffman Codes:
#   Traversing the tree and assigning binary codes to each character takes O(n), where n
#   is the number of characters, because each character is visited once.

# Overall Time Complexity:
#   The dominant term is O(n log n), primarily due to the heap operations in Step 2.
#   This is the best-case and worst-case time complexity, as each step depends on the
#   number of characters, irrespective of their frequencies.

#=================================================================================
# Best Practices and Considerations
#=================================================================================
# - It's crucial to understand that Huffman coding works best when character frequencies
#   vary significantly. If all characters have roughly equal frequencies, the benefits
#   of variable-length encoding diminish.
#
# - Edge case: Single character input. In this scenario, Huffman coding assigns a single
#   bit (e.g., '0') to the only character. Special handling might be necessary for
#   decoding, as a single bit can create ambiguity without additional context.
#
# - Avoid pitfalls with floating-point weights (e.g., probabilities instead of frequencies).
#   When dealing with floating-point numbers, rounding errors can introduce bugs.
#   Always normalize weights to avoid such issues, or consider using fractions if precision
#   is critical.

#=================================================================================
# Use Cases for Huffman Coding
#=================================================================================
# 1. Compression Algorithms: Huffman coding is widely used in compression formats like
#    ZIP, GZIP, and JPEG to minimize storage space by encoding frequent characters with
#    shorter codes.
#
# 2. Network Transmission: In bandwidth-constrained environments, Huffman coding helps
#    reduce the size of transmitted data, improving efficiency.
#
# 3. Compiler Optimization: Some compilers use Huffman coding to compress intermediate
#    representation files, speeding up I/O operations.

#=================================================================================
# Potential Improvements
#=================================================================================
# - In practice, more advanced data compression algorithms, such as arithmetic coding,
#   outperform Huffman coding by generating fractional-length codes. However, they
#   are computationally more complex.
#
# - If space is a concern, implement the Huffman tree as a binary array (i.e., store the
#   tree as a bitstream). This reduces overhead compared to using pointer-based tree
#   structures.

#=================================================================================
# Debugging and Testing Strategies
#=================================================================================
# - Ensure your implementation handles edge cases, such as single character inputs and
#   characters with zero frequency (e.g., due to filtering).
#
# - Use known test cases from textbooks or online resources to validate your implementation.
#   Compare the generated codes with expected outputs for correctness.
#
# - For large datasets, profile the performance to identify bottlenecks, especially during
#   heap operations. In Python, you can use the cProfile module to track time spent in each
#   function.


#=================================================================================
# Topic: Algorithms, Greedy Algorithms, Kruskal’s Algorithm
#=================================================================================

# Kruskal's algorithm finds the Minimum Spanning Tree (MST) of a graph.
# This algorithm works by sorting all edges in non-decreasing order of their weight
# and then picking the smallest edge that does not form a cycle with the MST.

#=================================================================================
# Sub-topic: Edge class representation
#=================================================================================

# Print an edge representation. In Kruskal's algorithm, each edge is considered independently.
# Each edge connects two nodes (u, v) with a specific weight (w), which is critical in 
# determining which edge to include in the MST.
print("Edge (u, v, w): (1, 2, 10)")

# Runtime consideration: Printing a simple string or tuple (like this edge) is an O(1) operation.
# This is because string formatting operations are constant time, unaffected by graph size.

# Use case: You would typically store edges in a list or array before processing them.
# In a real Kruskal implementation, this edge would be part of an edge list: 
# edges = [(1, 2, 10), (2, 3, 15), (1, 3, 5), ...]

#=================================================================================
# Sub-topic: Sort edges by weight
#=================================================================================

# Kruskal's algorithm begins by sorting all the edges by weight. Sorting ensures that 
# we process the smallest edges first, adhering to the greedy approach.
print("Sorting edges by weight: [(1, 3, 5), (1, 2, 10), (2, 3, 15)]")

# Sorting a list of edges is O(E log E), where E is the number of edges.
# This is because sorting algorithms like Timsort (used in Python's sorted function) 
# have an average case complexity of O(n log n).

# Best case: Already sorted edges, minimal operations for sorting, still O(E log E).
# Worst case: Completely unsorted, requiring full sorting effort, O(E log E).

# Insight: Sorting is the most expensive part of Kruskal’s algorithm. Therefore, it dominates 
# the overall time complexity, which becomes O(E log E), assuming a connected graph 
# where E is the number of edges, and V is the number of vertices.

#=================================================================================
# Sub-topic: Disjoint-set (Union-Find) data structure for cycle detection
#=================================================================================

# In Kruskal’s algorithm, we use a Disjoint-Set or Union-Find structure to efficiently
# check if adding an edge will form a cycle. Each node starts in its own set, and as edges 
# are added to the MST, nodes are merged into a single set.

# Print initial disjoint sets.
print("Initial disjoint sets: {1: {1}, 2: {2}, 3: {3}}")

# Best case: Every node is in its own set, O(1) time complexity for set initialization.
# Worst case: O(V) where V is the number of vertices if initializing disjoint sets for a 
# large number of vertices, though this is rare as typically initialization happens all at once.

# Insight: The Disjoint-Set data structure is key for the efficiency of Kruskal's algorithm.
# Operations such as `find` and `union` must be efficient to keep the algorithm performant.

#=================================================================================
# Sub-topic: Greedy edge selection
#=================================================================================

# As Kruskal's algorithm progresses, we iteratively select the smallest edge that does not
# form a cycle. This print statement shows a selected edge.
print("Selected edge: (1, 3, 5)")

# The edge (1, 3, 5) is chosen because it is the smallest available edge. Adding it does
# not form a cycle, so we include it in the MST.

# Runtime: O(1) for a simple comparison and selection operation, assuming sorted edges.

# Pitfall: If you do not have an efficient method for cycle detection, you could end up with
# quadratic time complexity. Using Disjoint-Set ensures that each edge selection takes near
# constant time due to path compression and union by rank.

#=================================================================================
# Sub-topic: Union operation (Merge sets)
#=================================================================================

# When an edge is selected, we merge the sets of the two vertices it connects, ensuring that 
# we don't later form a cycle by connecting vertices that are already part of the same set.

# Print after union operation.
print("After union: {1: {1, 3}, 2: {2}, 3: {1, 3}}")

# This shows that after adding the edge (1, 3), nodes 1 and 3 are now in the same set, 
# meaning they are connected in the MST. 

# Best case: Union by rank ensures this takes O(1) time in the average case.
# Worst case: Without path compression, the union could degrade to O(V) in some tree-like 
# structures, but this is avoided by using proper Union-Find optimizations.

# Insight: Efficient union operations are critical in keeping the algorithm fast, especially 
# for larger graphs with thousands of nodes and edges.

#=================================================================================
# Sub-topic: Print MST progress
#=================================================================================

# As edges are selected and added to the MST, we can print the current state of the MST.
print("Current MST: [(1, 3, 5)]")

# This shows that only one edge has been added to the MST so far. Kruskal's algorithm 
# will continue selecting edges and adding them, provided they don't form a cycle.

# Best case: Every edge added takes constant time, O(1), in terms of updating the MST set.
# Worst case: Checking for cycles without Disjoint-Set could increase complexity 
# to O(V^2) but typically remains constant with proper Union-Find.

# Use case: You might want to visualize or debug the state of the MST as the algorithm 
# progresses, especially when working with large graphs or complex datasets.

#=================================================================================
# Sub-topic: Algorithm termination
#=================================================================================

# The algorithm terminates when we have V-1 edges in the MST (where V is the number of vertices).
# This is because a Minimum Spanning Tree of a connected graph with V vertices always has exactly V-1 edges.

# Print final MST.
print("Final MST: [(1, 3, 5), (1, 2, 10)]")

# In this case, after selecting the edges (1, 3, 5) and (1, 2, 10), we have a valid MST 
# because we now have two edges, and the graph has 3 vertices.

# Best case: Early termination can occur in sparse graphs when the MST is found quickly.
# Worst case: Dense graphs may require checking all edges before termination, O(E log E).

# Insight: Kruskal’s algorithm is particularly well-suited for graphs with many edges because 
# sorting and the Union-Find structure keep the complexity manageable.

#=================================================================================
# Sub-topic: Complexity and efficiency
#=================================================================================

# The overall time complexity of Kruskal's algorithm is O(E log E), dominated by sorting.
# This makes it highly efficient for graphs where the number of edges is not significantly
# larger than the number of vertices.

# Space complexity is O(V + E), where V is the number of vertices, and E is the number of edges.
# The algorithm stores disjoint sets, sorted edges, and the MST edges, all of which contribute
# to memory usage.


#=================================================================================
# Algorithms, Greedy Algorithms, Prim’s Algorithm
#=================================================================================

# Prim's algorithm is a greedy algorithm that finds a Minimum Spanning Tree (MST)
# for a weighted, undirected graph. It starts with an arbitrary node and 
# expands the tree by adding the minimum edge connecting the tree to a vertex 
# not yet in the tree. The algorithm repeats until all vertices are included.

# Print starting point of the algorithm
print("Starting Prim's algorithm to find MST.")

# Scenario 1: Basic example of initializing a graph using an adjacency matrix.
# Each value in the matrix represents the weight of the edge between nodes.
# If nodes are not directly connected, the weight is typically set to infinity.
# Initializing with infinity allows the algorithm to focus on smaller edge weights first.
infinity = float('inf')  # We define infinity to represent no direct edge between nodes
graph = [
    [0, 2, infinity, 6, infinity],  # Row represents connections from the first node
    [2, 0, 3, 8, 5],                # Row represents connections from the second node
    [infinity, 3, 0, infinity, 7],   # infinity signifies no direct edge between nodes
    [6, 8, infinity, 0, 9],          # Symmetric matrix implies undirected graph
    [infinity, 5, 7, 9, 0]           # Weights on diagonal (0) represent no self-loop
]

# Runtime consideration:
# Accessing a graph stored as an adjacency matrix requires O(1) access time to any edge weight.
# However, adjacency matrices have a space complexity of O(V^2), where V is the number of vertices.
# This can be inefficient for sparse graphs (graphs with few edges) where adjacency lists
# might be a better alternative with space complexity O(V + E), where E is the number of edges.

# Scenario 2: Initialize an array to track the minimum cost of adding each vertex to the MST.
# The 'key' array keeps the minimum edge weight for each node that connects it to the MST.
# Initially, all values are set to infinity because no edges have been explored yet.
key = [infinity, infinity, infinity, infinity, infinity]
print("Initialized key array with infinite values:", key)

# Best practice:
# Initializing values with infinity is useful for algorithms that seek to minimize values, 
# as any encountered weight will naturally be smaller than infinity.

# The 'parent' array stores the MST structure. parent[i] holds the index of the node 
# that connects node 'i' to the MST. This allows reconstruction of the MST once the 
# algorithm completes. Initialize with -1, indicating no parent assigned yet.
parent = [-1, -1, -1, -1, -1]
print("Initialized parent array with -1 values to store MST structure:", parent)

# Scenario 3: Keep track of vertices included in the MST using a boolean array 'mstSet'.
# Initially, all vertices are set to False because no vertex is included in the MST yet.
mstSet = [False, False, False, False, False]
print("Initialized mstSet array to track vertices included in MST:", mstSet)

# Runtime consideration:
# Access time for the 'mstSet' array is O(1), making inclusion checks constant in time.
# However, since the algorithm must eventually visit all vertices, total runtime includes
# iterating through this list multiple times, contributing to the overall time complexity.

# Scenario 4: Start Prim's algorithm by choosing an arbitrary vertex as the starting point.
# The standard approach is to start from the first vertex (index 0).
key[0] = 0  # Set the weight of the starting node to 0 so it's picked first
print("Starting from vertex 0, updated key array:", key)

# Runtime consideration:
# Setting an element in the 'key' array is an O(1) operation. However, 
# choosing an efficient starting node can influence performance in some variations
# of the problem where node distribution or edge weights are not uniform.

# The core operation of Prim’s algorithm is to repeatedly pick the vertex not 
# included in the MST that has the smallest edge weight. This requires a helper
# function to find the smallest 'key' value among the vertices not yet in the MST.
# For now, assume such a function exists (in actual implementation, a min-heap would be used).
# Here we simulate picking vertex 0 since its 'key' value is 0.
u = 0
mstSet[u] = True  # Mark vertex 0 as included in the MST
print(f"Vertex {u} is picked and added to the MST.")

# Best Practice:
# To optimize the search for the minimum key, a priority queue or min-heap can be used.
# This reduces the time complexity of finding the next vertex from O(V) to O(log V).

# Scenario 5: Once a vertex is added to the MST, update the 'key' and 'parent' values for
# the adjacent vertices. For each vertex 'v' adjacent to 'u', if 'v' is not yet included in 
# the MST and the edge weight from 'u' to 'v' is smaller than the current 'key[v]', 
# update the 'key' and set 'u' as the parent of 'v'.
for v in range(5):  # Assume the graph has 5 vertices (size of the adjacency matrix)
    # Check if there is an edge between u and v, and if v is not yet in the MST
    if graph[u][v] and not mstSet[v] and key[v] > graph[u][v]:
        key[v] = graph[u][v]  # Update the key with the new minimum weight
        parent[v] = u  # Set 'u' as the parent of 'v'
        print(f"Updated key and parent for vertex {v}: key = {key[v]}, parent = {parent[v]}")

# Considerations:
# Updating each adjacent vertex requires iterating over all vertices, leading to 
# an O(V^2) time complexity in the case of using an adjacency matrix without a heap.
# This can be optimized to O(E log V) by using a binary heap or O(E + V log V) with a Fibonacci heap.

# Scenario 6: Repeat the process for all remaining vertices. Each iteration adds 
# one vertex to the MST and updates the 'key' and 'parent' arrays accordingly. 
# After all vertices are included in the MST, Prim's algorithm terminates.

# Print final key and parent arrays after completing the algorithm
print("Final key array (minimum edge weights):", key)
print("Final parent array (MST structure):", parent)

# Runtime Summary:
# Time Complexity: O(V^2) with adjacency matrix and simple min-key extraction.
#                  O(E log V) with binary heap.
#                  O(E + V log V) with Fibonacci heap (best for dense graphs).
# Space Complexity: O(V^2) for adjacency matrix, O(V + E) for adjacency list.
# Pitfall: If the graph is not connected, Prim's algorithm will only find the MST for
# the connected component containing the starting vertex.

#=================================================================================
# Main Topic: Fractional Knapsack Problem - Greedy Algorithm Implementation
#=================================================================================

# Subtopic: Problem Overview
# In the Fractional Knapsack problem, the goal is to maximize the value of items placed in a knapsack 
# without exceeding the capacity. Each item can be divided (fractionally), meaning part of an item can be added to the knapsack.
# This differs from the classic 0/1 Knapsack Problem where an item must be either fully taken or left behind.

# Subtopic: Greedy Algorithm Approach
# The greedy approach works by selecting the item with the highest value-to-weight ratio first, 
# and continues selecting items in descending order of this ratio. This ensures we are maximizing the value 
# at every step of the selection process. This method does not guarantee an optimal solution for the 0/1 Knapsack 
# but does for the fractional variant.

# Subtopic: Input Details and Assumptions
# Assume we are given two arrays:
#   - values[]: which stores the values of each item.
#   - weights[]: which stores the corresponding weights of each item.
# Additionally, we are given a 'capacity' which is the total weight limit of the knapsack.

# Subtopic: Implementation Considerations
# Before implementation, ensure the following:
#   - We have items to choose from (i.e., lengths of 'values' and 'weights' arrays should be equal and > 0).
#   - Capacity should be positive; otherwise, no items can be selected.

#=================================================================================
# Code Implementation (without functions as per the requirement):
#=================================================================================

# Example input setup:
values = [60, 100, 120]    # Array representing the value of each item
weights = [10, 20, 30]     # Array representing the corresponding weight of each item
capacity = 50              # Maximum weight capacity of the knapsack

# Step 1: Calculating value-to-weight ratios
# The ratio of value to weight is critical in greedy selection. Higher ratios are prioritized.
# We are using list comprehension here to create a list of tuples where each tuple consists of 
# (value-to-weight ratio, value, weight) for each item. Sorting will be based on the first element of these tuples.
items = [(v / w, v, w) for v, w in zip(values, weights)]  

# Best practice: zip() is used to combine values and weights in pairs, ensuring index consistency.
# Advanced tip: Using zip() avoids index errors that might arise from iterating separately through values[] and weights[].

# Step 2: Sorting items by value-to-weight ratio in descending order
# Since we are maximizing the total value, the item with the highest value per unit of weight should be considered first.
items.sort(reverse=True, key=lambda x: x[0])  

# Best practice: Sorting with reverse=True ensures descending order. Lambda function is used for readability, 
# specifying that the first element (x[0], the ratio) is the sorting key.

# Subtopic: Time Complexity of Sorting
# Sorting the items takes O(n log n), where n is the number of items. This is a significant part of the algorithm's runtime.

# Step 3: Greedily selecting items to fill the knapsack
# We'll iterate through the sorted items and add as much of each item as possible until the knapsack is full.
total_value = 0    # Initialize the total value to 0
remaining_capacity = capacity  # Track the remaining capacity of the knapsack

# Begin the greedy selection loop.
for ratio, value, weight in items:
    # If the remaining capacity can fit the entire item, take all of it
    if remaining_capacity >= weight:
        total_value += value       # Add the full value of the item
        remaining_capacity -= weight  # Subtract the item's weight from the remaining capacity
    else:
        # If the remaining capacity cannot fit the entire item, take the fractional part
        total_value += ratio * remaining_capacity  # Add the proportional value
        remaining_capacity = 0  # The knapsack is now full, break the loop
        break

# Subtopic: Time Complexity of Selection
# The greedy selection process runs in O(n), where n is the number of items. Each item is considered once in the loop.

# Subtopic: Best and Worst Case Analysis
# Best case: If the capacity is large enough to fit all items, we take all items, 
# so the runtime remains O(n log n) dominated by the sorting step.
# Worst case: In scenarios where the capacity is very small, we may need to take fractional parts of the first or second item,
# but the time complexity remains O(n log n) due to sorting.

# Subtopic: Space Complexity Analysis
# The space complexity is O(n) because we store the ratio list of size n and track variables like total_value and remaining_capacity.
# In-place sorting means we don’t require additional space for sorting.

# Subtopic: Special Considerations and Edge Cases
# 1. Edge Case 1: No items to choose from
#    - If the values[] or weights[] are empty, we directly conclude that total_value is 0 and the algorithm terminates.
# 2. Edge Case 2: Zero capacity
#    - If the capacity is 0 or negative, the algorithm stops immediately without selecting any items.
# 3. Unusual Case: Items with zero weight
#    - If any item's weight is zero, this leads to a division-by-zero error in the value-to-weight ratio calculation. 
#      Such cases should be handled separately in practice by filtering out zero-weight items or assigning a special condition.

#=================================================================================
# Output the total maximum value that can be achieved
print("Total value in the knapsack:", total_value)

# Use Case 1: Standard example where items are added in descending order of value-to-weight ratio.
# Example values: values = [60, 100, 120], weights = [10, 20, 30], capacity = 50
# Expected result: The total maximum value in the knapsack will be 240.

# Use Case 2: Edge case where the knapsack has zero capacity.
# Example values: values = [60, 100, 120], weights = [10, 20, 30], capacity = 0
# Expected result: The total maximum value in the knapsack will be 0.

# Use Case 3: Items with identical value-to-weight ratios.
# Example values: values = [60, 90, 120], weights = [20, 30, 40], capacity = 50
# Since the ratios are identical (all 3.0), any combination will provide the maximum value, but the algorithm still works optimally.

# Use Case 4: High capacity allowing all items.
# Example values: values = [60, 100, 120], weights = [10, 20, 30], capacity = 60
# Expected result: The total maximum value in the knapsack will be 280, as all items fit.

#=================================================================================
# Algorithms: Mathematical Algorithms - Demonstrating concepts through print statements
#=================================================================================

# Main Topic: Sum of the first 'n' natural numbers
#-----------------------------------------------------------
# Subtopic: Direct formula to calculate the sum of first 'n' natural numbers.
# Formula: sum = n * (n + 1) / 2
# This formula derives from the arithmetic series summation and computes the sum in constant time O(1).
# Using the formula avoids the need for looping, making it efficient for large values of 'n'.
n = 10  # Example input for n
print(f"The sum of the first {n} natural numbers is: {n * (n + 1) // 2}")

# Analysis:
# Time Complexity: O(1) - This algorithm runs in constant time since it directly computes the result with a few operations.
# Space Complexity: O(1) - Only stores the integer 'n' and intermediate results, independent of the input size.
# Best and Worst Case: Both are O(1), as the number of operations does not depend on 'n'.

# Use case:
# This formula is ideal when you need to compute the sum of natural numbers quickly, such as when dealing with very large datasets or real-time systems.
# Example: In financial computations, summing up numbers or quantities for fast reporting.

# Consideration:
# In languages without arbitrary-precision integers (like C or C++), integer overflow could occur for very large values of 'n'. 
# Python automatically handles large integers, but in other environments, you may need to check for overflow.

# Pitfall:
# When 'n' is negative, the formula still works mathematically, but logically, summing a negative count of natural numbers doesn't make sense.
# Ensure input validation to avoid applying the formula in inappropriate contexts.

# Improvement:
# While this formula is already optimal, ensure it's applied only when summing sequential natural numbers; for other sequences, different formulas apply.

#-----------------------------------------------------------
# Subtopic: Iterative approach to calculate the sum of the first 'n' natural numbers.
# Though less efficient, iterating through each number and summing them is another way to achieve the same result.
# This serves as an example of an O(n) approach, where 'n' influences the number of operations.
n = 10  # Example input for n
total_sum = 0  # Initialize sum accumulator
for i in range(1, n + 1):  # Loop through all numbers from 1 to n
    total_sum += i  # Add current number to the running total

print(f"The iterative sum of the first {n} natural numbers is: {total_sum}")

# Analysis:
# Time Complexity: O(n) - We perform 'n' additions, making it proportional to the size of 'n'.
# Space Complexity: O(1) - The space used is independent of 'n'; only 'total_sum' and 'i' are stored.
# Best Case: O(n) - Regardless of the input size, the loop always runs 'n' times.
# Worst Case: O(n) - Same as the best case.

# Use case:
# Iterative summation is useful when you cannot use the closed-form formula, such as when you need to compute a sum of non-sequential or filtered numbers.
# Example: Summing even numbers, odd numbers, or elements matching certain conditions.

# Pitfall:
# This method is inefficient for large values of 'n' compared to the direct formula. As 'n' increases, the time required increases linearly.

# Improvement:
# For summing specific numbers (e.g., only even numbers), you can modify the iteration to skip irrelevant numbers, reducing the number of operations.

#-----------------------------------------------------------
# Subtopic: Sum of the squares of the first 'n' natural numbers
# Formula: sum = n * (n + 1) * (2n + 1) / 6
# This formula gives the sum of squares of the first 'n' natural numbers in constant time O(1).
# It's derived from a well-known mathematical pattern for squared numbers.
n = 10  # Example input for n
print(f"The sum of squares of the first {n} natural numbers is: {n * (n + 1) * (2 * n + 1) // 6}")

# Analysis:
# Time Complexity: O(1) - The formula computes the result in constant time, independent of 'n'.
# Space Complexity: O(1) - Only stores 'n' and intermediate values, requiring constant space.
# Best and Worst Case: Both are O(1), as the computation doesn't depend on the input size.

# Use case:
# This formula is useful in physics, engineering, and financial modeling where sums of squared values occur frequently.
# Example: Calculating variance in statistics or moments of inertia in physics.

# Pitfall:
# As with the sum of natural numbers, overflow can be a concern in environments with fixed-width integers.
# Additionally, like before, ensure the formula isn't applied to inappropriate sequences of numbers.

#-----------------------------------------------------------
# Subtopic: Iterative approach to calculate the sum of the squares of the first 'n' natural numbers.
# Like the iterative approach for summing natural numbers, this method iterates through all numbers, squaring each one and summing them.
n = 10  # Example input for n
sum_of_squares = 0  # Initialize sum accumulator
for i in range(1, n + 1):  # Loop through all numbers from 1 to n
    sum_of_squares += i * i  # Square the current number and add to the running total

print(f"The iterative sum of squares of the first {n} natural numbers is: {sum_of_squares}")

# Analysis:
# Time Complexity: O(n) - We perform 'n' squaring operations and 'n' additions, making it proportional to 'n'.
# Space Complexity: O(1) - The space required remains constant, only storing the sum and loop variables.
# Best Case: O(n) - The loop always runs 'n' times.
# Worst Case: O(n) - Same as best case.

# Use case:
# Useful when you need to compute the sum of squares for numbers that don’t follow a simple pattern, such as non-sequential numbers or when certain conditions are applied.
# Example: Summing squares of even numbers only.

# Improvement:
# If you only need to sum squares of specific numbers (like every other number), you can adjust the loop to skip unnecessary iterations, saving computation time.

# Pitfall:
# As with the sum of natural numbers, this approach becomes inefficient for large 'n'. Using the closed-form formula is significantly faster when possible.

# Consideration:
# While iterating through the sequence is simple, think about using vectorized operations or libraries like NumPy for more complex scenarios, which can optimize these calculations further.

#=================================================================================



#=================================================================================
# Algorithms, Mathematical Algorithms, Greatest Common Divisor (GCD)
#=================================================================================

# Topic: Greatest Common Divisor (GCD) of two numbers
#-----------------------------------------------------------
# The GCD of two numbers is the largest integer that divides both numbers without leaving a remainder.
# One of the most efficient algorithms to compute the GCD is the Euclidean algorithm.
# The Euclidean algorithm is based on the principle that GCD(a, b) = GCD(b, a % b), and continues recursively until b == 0.
# When b is 0, the GCD is 'a'.

# Euclidean Algorithm Example (Iterative)
a = 60
b = 48
while b != 0:
    a, b = b, a % b
print(f"The GCD of 60 and 48 is: {a}")

# Explanation:
# - Initially, we take two integers a = 60 and b = 48.
# - Using a loop, we repeatedly apply the Euclidean algorithm: replace 'a' with 'b' and 'b' with 'a % b' until 'b' becomes 0.
# - Once 'b' is 0, 'a' contains the GCD, which in this case is 12.
# - This method is highly efficient for computing the GCD, especially with large numbers.

# Runtime Analysis:
# - Time Complexity: O(log(min(a, b))), where 'a' and 'b' are the input integers. This logarithmic complexity stems from the fact 
#   that the size of the numbers reduces significantly in each iteration by using modulus.
# - Space Complexity: O(1) as the algorithm only uses a constant amount of space for variables 'a' and 'b'.
# Best Case: The best-case scenario occurs when one of the numbers is already the GCD. For instance, GCD(60, 60) would take one step.
# Worst Case: The worst-case scenario is when the numbers are large and their difference is minimal (e.g., consecutive Fibonacci numbers).
#   In such cases, the algorithm will take the longest time, but the complexity still remains logarithmic.

# Use case:
# The Euclidean algorithm is practical in areas where divisibility properties are essential, such as cryptography (RSA algorithm),
# simplifying fractions, and lattice reduction problems.

# Pitfall:
# Ensure that both 'a' and 'b' are non-negative integers; the algorithm does not inherently handle negative numbers well. 
# If negative inputs are possible, consider taking the absolute value of both numbers before applying the algorithm.

#-----------------------------------------------------------
# Topic: Least Common Multiple (LCM) of two numbers
#-----------------------------------------------------------
# LCM is the smallest number that is a multiple of both numbers. The relationship between LCM and GCD is given by:
# LCM(a, b) = abs(a * b) / GCD(a, b)
# This formula works because multiplying the two numbers gives a product that contains all factors of both numbers, 
# and dividing by their GCD eliminates common factors to obtain the smallest common multiple.

# LCM Example:
a = 60
b = 48
gcd = 12  # GCD is precomputed using the above method.
lcm = abs(a * b) // gcd
print(f"The LCM of 60 and 48 is: {lcm}")

# Explanation:
# - The absolute value ensures the result is positive, even if 'a' or 'b' were negative.
# - Multiplying 'a' and 'b' gives a product that contains all the factors of both numbers.
# - Dividing by the GCD removes the common factors, leaving the least common multiple.
# - In this example, LCM(60, 48) = (60 * 48) / 12 = 240.

# Runtime Analysis:
# - Time Complexity: O(log(min(a, b))) for the GCD calculation, followed by O(1) for the multiplication and division.
# - Space Complexity: O(1) since we're only storing the LCM result.
# Best Case: Both 'a' and 'b' are small, resulting in quick calculations.
# Worst Case: Large numbers or numbers that are co-prime (i.e., their GCD is 1) would require slightly more time for GCD computation.

# Use case:
# LCM is commonly used in problems involving scheduling or finding common periods, such as when two signals overlap periodically.

# Pitfall:
# Integer overflow can occur with large values of 'a' and 'b' during multiplication in languages without automatic big integer handling, 
# though Python handles arbitrarily large integers natively. Be cautious if porting this logic to languages like C or Java.

#-----------------------------------------------------------
# Topic: Checking Co-prime Numbers
#-----------------------------------------------------------
# Two numbers are said to be co-prime if their GCD is 1, meaning they have no common divisors other than 1.

# Co-prime Example:
a = 17
b = 29
while b != 0:
    a, b = b, a % b
if a == 1:
    print("17 and 29 are co-prime.")
else:
    print("17 and 29 are not co-prime.")

# Explanation:
# - Similar to the GCD calculation, we use the Euclidean algorithm to find the GCD.
# - If the GCD turns out to be 1, the two numbers are co-prime.
# - Here, 17 and 29 are co-prime because their GCD is 1.

# Runtime Analysis:
# - Time Complexity: O(log(min(a, b))) for GCD computation.
# - Space Complexity: O(1).
# Best Case: If one of the numbers is 1 (e.g., GCD(1, 29)), it will be instantly co-prime.
# Worst Case: The numbers have no common factors except 1, but the algorithm will still have logarithmic complexity.

# Use case:
# Determining co-prime numbers is useful in number theory and cryptography, especially in public key cryptosystems where co-prime pairs 
# are used in key generation.

# Pitfall:
# The numbers should be positive integers; otherwise, additional handling is required for negative or zero values.

#=================================================================================
# Algorithms, Mathematical Algorithms, Prime Number Algorithms (Sieve of Eratosthenes)
#=================================================================================

# Topic: Prime Number Generation using Sieve of Eratosthenes
#-----------------------------------------------------------
# The Sieve of Eratosthenes is an efficient algorithm to generate all prime numbers up to a given limit 'n'.
# It marks the multiples of each prime number starting from 2, the first prime number, as composite.
# Prime numbers are left unmarked.
# The time complexity of this algorithm is O(n log log n), which makes it significantly faster 
# than checking each number for primality individually (which would take O(n^1.5) or worse).

n = 30  # Set the upper limit for prime number generation

# Initialize a boolean array (list) where index represents the number and value represents if it is prime.
# Initially, we assume all numbers are prime (True) except for 0 and 1 which are not prime by definition.
prime = [True for _ in range(n+1)]  # Creates a list with 'n+1' elements, all set to True.

# Index 0 and 1 are marked as False because 0 and 1 are not prime.
prime[0] = prime[1] = False

# Now, we start marking non-prime numbers. We begin from 2, the first prime number.
p = 2
while (p * p <= n):  # We only need to check numbers up to √n.
    # If prime[p] is still True, it means 'p' is a prime number.
    if (prime[p] == True):
        # Mark all multiples of 'p' starting from p^2 as non-prime.
        # The reason we start from p^2 is that any number less than p^2 will already have been marked by smaller primes.
        for i in range(p * p, n+1, p):
            prime[i] = False  # Marking the multiples of p as False, meaning not prime.
    p += 1  # Move to the next number to check for primality.

# After the above loop finishes, the prime list now holds True for prime indices and False for non-prime ones.

# Print all prime numbers by checking the boolean list 'prime'.
# This loop iterates over all numbers and prints only those which are marked as True (prime).
print(f"Prime numbers up to {n} are:", [p for p in range(n+1) if prime[p]])

# Runtime Analysis:
# - Time Complexity: O(n log log n) due to the nature of the Sieve of Eratosthenes algorithm.
# - Space Complexity: O(n) because we maintain a list of size 'n+1' to store the primality of each number.
# Best Case: O(n log log n) because every number less than or equal to 'n' is processed.
# Worst Case: Same as best case, as the algorithm consistently operates within its time complexity bounds.

# Use case:
# This method is ideal when generating a list of primes up to a large number, such as in cryptography, 
# where large prime numbers are essential for algorithms like RSA.
# It’s also used in number theory research, prime factorization, and situations requiring fast prime checking.

# Considerations:
# - The space complexity could be a concern if 'n' is very large (millions or billions).
# - Sieve of Eratosthenes works well for batch prime number generation but is not efficient for testing 
#   primality of individual numbers in isolation.
# - Starting the inner loop at p^2 instead of p*2 is critical to optimizing the performance. Any number 
#   smaller than p^2 would have already been marked by smaller primes.



#=================================================================================
# Algorithms: Mathematical Algorithms - Fermat’s Little Theorem
#=================================================================================

# Topic: Fermat's Little Theorem
#-----------------------------------------------------------
# Fermat's Little Theorem states that if p is a prime number and a is an integer not divisible by p, then:
# a^(p-1) ≡ 1 (mod p)
# This theorem is widely used in modular arithmetic, especially for calculating large powers in modular contexts efficiently.
# One of the most common applications is in modular exponentiation and number theory-based algorithms like RSA encryption.

# Subtopic: Use in Modular Exponentiation
#-----------------------------------------------------------
# Instead of directly computing 'a^(p-1)' which can lead to very large numbers, 
# Fermat's theorem allows reducing computations by taking mod 'p' at each step.
# It is particularly useful when we need to compute 'a^b % p', where 'p' is a prime number.

# Example: Compute large exponentiation under modulo using Fermat's Theorem
# Here, we compute (3^7) % 13. Instead of computing 3^7 directly, we leverage mod operations.
a = 3
b = 7
p = 13

# Performing modular exponentiation:
# The direct computation of 3^7 would yield 2187. Instead of dealing with large numbers,
# we reduce intermediate steps using mod 13 at each step.
# 3^7 ≡ (3 * 3 * 3 * 3 * 3 * 3 * 3) % 13

# Step-by-step calculation:
# 3^1 % 13 = 3
# 3^2 % 13 = (3 * 3) % 13 = 9
# 3^4 % 13 = (9 * 9) % 13 = 81 % 13 = 3
# 3^7 % 13 = (3^4 * 3^2 * 3^1) % 13 = (3 * 9 * 3) % 13 = 81 % 13 = 3
print(f"Using Fermat's Theorem: (3^7) % 13 = {pow(a, b, p)}")

# The built-in Python pow() function efficiently computes modular exponentiation using the method of "exponentiation by squaring," 
# reducing the overall time complexity to O(log(b)), where 'b' is the exponent.
# Without such an algorithm, the brute-force approach would take O(b) time, making it less efficient for large 'b'.

# Runtime Analysis:
# - Time Complexity: O(log(b)) due to exponentiation by squaring.
# - Space Complexity: O(1), as no additional memory usage grows with input size.
# Best Case: The exponent is small, making it closer to O(1) in practice.
# Worst Case: Large exponent, but still O(log(b)) due to the efficient algorithm.

# Use case:
# Fermat's theorem-based modular exponentiation is critical in cryptographic applications such as RSA, where we often deal with 
# very large exponents and need efficient computation of powers under a modulus.

# Considerations:
# - This method only applies when 'p' is prime. In non-prime cases, alternative methods such as Euler's theorem must be used.
# - Overflow issues are avoided by modular reduction, making this efficient even for large numbers in practice.

# Subtopic: Fermat’s Little Theorem for Modular Inverses
#-----------------------------------------------------------
# Fermat’s Little Theorem is also used for calculating modular inverses.
# The modular inverse of 'a' under prime 'p' can be computed as:
# a^(p-2) ≡ a^(-1) (mod p)
# This avoids the need for extended Euclidean algorithms in modular inverse calculations when the modulus is prime.

# Example: Calculate modular inverse of 3 mod 13
a = 3
p = 13

# Fermat's theorem tells us that 3^(13-2) ≡ 3^11 (mod 13) is the inverse of 3 mod 13.
# This is because 3^(13-1) ≡ 1 (mod 13), and thus 3^11 is the modular inverse.
print(f"Modular inverse of 3 mod 13 = {pow(a, p-2, p)}")

# Runtime Analysis:
# - Time Complexity: O(log(p-2)) due to exponentiation by squaring.
# - Space Complexity: O(1), as we aren't using any extra space.
# Best Case: Small modulus, making computations faster.
# Worst Case: Large primes, though still efficient due to logarithmic time.

# Use case:
# Modular inverses are crucial in cryptographic protocols, error detection, and coding theory where division under a modulus is needed.

# Considerations:
# - Ensure the modulus is prime for this method to be valid.
# - This method is computationally efficient but doesn't work for non-prime moduli, where other algorithms like the Extended Euclidean Algorithm are needed.

# Subtopic: Large Prime Moduli
#-----------------------------------------------------------
# When working with large prime numbers in cryptography (e.g., RSA encryption), 
# Fermat's Little Theorem provides a means of fast computation for modular inverses, powers, and reductions.
# This is especially useful in systems requiring real-time security computations.

# Example: Large prime exponentiation
# Computing (7^12345) % 1000000007, a common task in competitive programming or cryptography.
# We will not compute 7^12345 directly as it would lead to extremely large numbers.
a = 7
b = 12345
p = 1000000007

# Modular exponentiation using pow() ensures that intermediate results are kept manageable via modulus application.
print(f"(7^12345) % 1000000007 = {pow(a, b, p)}")

# Runtime Analysis:
# - Time Complexity: O(log(b)) using exponentiation by squaring, suitable for very large exponents.
# - Space Complexity: O(1).
# Best Case: Small exponent, even faster.
# Worst Case: Very large exponents, but still logarithmic time complexity.

# Use case:
# Algorithms involving large primes, such as RSA encryption and decryption, require handling of large powers and moduli. 
# Fermat's Little Theorem ensures these computations are feasible in reasonable time, even for cryptographic-sized inputs.

# Considerations:
# - The pow() function in Python is highly optimized for modular arithmetic, but be cautious of implementation differences in other programming languages.
# - For non-prime moduli, consider alternatives such as Euler's theorem or direct methods.

#=================================================================================
# Algorithms: Mathematical Algorithms - Fast Exponentiation (Exponentiation by Squaring)
#=================================================================================

# Topic: Fast Exponentiation (also known as Exponentiation by Squaring)
#-----------------------------------------------------------
# This algorithm efficiently calculates the power of a number (base^exponent) in O(log n) time,
# significantly improving over the naive approach of multiplying the base 'exponent' times, 
# which has a time complexity of O(n).
# The idea is to reduce the exponent by half at each step, squaring the base, thus minimizing the number of multiplications.

# Subtopic: Example of calculating base^exponent
# Use Case: When large exponents need to be computed, especially in cryptographic algorithms (e.g., RSA),
# where performance is crucial for operations involving big integers.

# Example 1: Simple exponentiation of 2^10
base = 2
exponent = 10
result = 1
exp = exponent  # Preserve original exponent for clarity in the example

# Loop through while the exponent is greater than 0
while exp > 0:
    # If the exponent is odd, multiply the result by the base
    if exp % 2 == 1:
        result *= base
    # Square the base and halve the exponent (integer division)
    base *= base
    exp //= 2

# Output the result for base^10
print(f"2^10 = {result}")

# Explanation:
# - The exponent is halved in each step, and the base is squared. 
# - When the exponent is odd, the current base value is multiplied into the result.
# - By the time the loop ends, we have calculated the result efficiently.

# Runtime Analysis:
# - Time Complexity: O(log n), since we halve the exponent at each step.
# - Space Complexity: O(1), as we use only a few additional variables.
# Best Case: In every case, the runtime is O(log n), regardless of the input values.
# Worst Case: Same as the best case, as the exponent is consistently halved.

# Subtopic: Mathematical insight behind fast exponentiation
# Fast exponentiation leverages properties of powers:
#  - If the exponent is even: base^exponent = (base^2)^(exponent/2)
#  - If the exponent is odd: base^exponent = base * (base^2)^(exponent//2)
# These two rules allow us to break down the problem into smaller, easier-to-manage computations.

# Sub-subtopic: Practical considerations
# In languages with fixed-width integer types, beware of overflow when working with very large exponents and bases.
# Python’s native int type automatically handles large numbers using arbitrary-precision arithmetic,
# but this is not the case in many other programming languages.

# Example 2: Exponentiation with a large base and exponent
base = 10
exponent = 50
result = 1
exp = exponent  # Preserve original exponent

while exp > 0:
    if exp % 2 == 1:
        result *= base
    base *= base
    exp //= 2

# Output the result for 10^50
print(f"10^50 = {result}")

# Use case:
# Calculating powers with large exponents is crucial in computational fields such as cryptography,
# scientific simulations, and algorithms dealing with big numbers (e.g., number theory applications).

# Subtopic: Pitfalls and Best Practices
# - Edge Case 1: Exponent = 0
# The result of any base raised to the power of 0 is always 1 (base^0 = 1).
base = 5
exponent = 0
print(f"5^0 = {1 if exponent == 0 else base}")

# - Edge Case 2: Base = 0 and Exponent > 0
# 0 raised to any positive exponent is always 0 (0^n = 0 for n > 0).
base = 0
exponent = 3
print(f"0^3 = {0 if base == 0 and exponent > 0 else base}")

# - Edge Case 3: Negative Exponent
# If the exponent is negative, the result is the reciprocal of the base raised to the positive exponent (base^-n = 1/(base^n)).
# Python handles this by converting the exponent to positive and then inverting the result.
base = 2
exponent = -3
result = 1 / (base ** abs(exponent))
print(f"2^-3 = {result}")

# Sub-subtopic: Advanced Considerations
# - Modulo exponentiation (a variation of fast exponentiation): Often used in cryptography for computations such as modular inverses.
# Instead of calculating base^exponent directly, you calculate (base^exponent) % mod. This ensures results remain manageable for very large numbers.

# Example 3: Fast Exponentiation with Modulo (e.g., RSA algorithm use case)
base = 7
exponent = 13
mod = 23
result = 1
exp = exponent

while exp > 0:
    if exp % 2 == 1:
        result = (result * base) % mod
    base = (base * base) % mod
    exp //= 2

# Output result for 7^13 % 23
print(f"7^13 % 23 = {result}")

# Runtime Analysis:
# - Time Complexity: O(log n), similar to standard fast exponentiation.
# - Space Complexity: O(1), as only a few extra variables are used.
# Best Case: O(log n) consistently, regardless of mod size.
# Worst Case: O(log n) since each operation involves the same logarithmic reduction of the exponent.

# Use case:
# Modulo exponentiation is crucial in public-key cryptography algorithms (RSA, Diffie-Hellman key exchange), 
# where computations with extremely large numbers must stay within a reasonable range by taking modulo a large prime.

# Consideration:
# Ensure the modulus is greater than 1 to avoid unnecessary divisions by 0. Additionally, working with negative exponents 
# in modular arithmetic requires modular inverses, which is a more advanced topic not covered in basic fast exponentiation.


#=================================================================================
# Algorithms, Mathematical Algorithms, Matrix Exponentiation
#=================================================================================
# Matrix exponentiation is a powerful technique for solving problems involving 
# linear recurrences in logarithmic time. It's especially useful in algorithms 
# related to Fibonacci numbers, dynamic programming, and other mathematical modeling.

# Subtopic: Matrix Representation of Fibonacci Sequence
#-----------------------------------------------------------
# The nth Fibonacci number can be calculated in O(log n) time using matrix exponentiation.
# The recurrence relation for Fibonacci numbers is:
# F(n) = F(n-1) + F(n-2)
# This relation can be represented in matrix form as:
# | F(n)   | = | 1 1 | * | F(n-1) |
# | F(n-1) |   | 1 0 |   | F(n-2) |
# By exponentiating the matrix, we can compute the nth Fibonacci number efficiently.

# Example matrix representing the Fibonacci relation.
# The base matrix for Fibonacci sequence
fib_matrix = [[1, 1], [1, 0]]
print(f"Base Fibonacci matrix: {fib_matrix}")

# Runtime Analysis:
# - Time Complexity of matrix exponentiation: O(log n), since we reduce the exponent by half each time.
# - Space Complexity: O(1), since only a constant amount of space is needed for the matrix.
# Best Case: O(log n) - logarithmic time due to binary exponentiation.
# Worst Case: O(log n) - logarithmic time still holds as we reduce the matrix exponentiation progressively.

# Subtopic: Use of Binary Exponentiation in Matrix Exponentiation
#-----------------------------------------------------------
# To exponentiate the matrix, binary exponentiation is used, where the power is reduced by half at each step.
# This approach is far more efficient than performing matrix multiplication n times.
# Binary exponentiation is key here, as it ensures logarithmic time complexity.

# Example of a matrix raised to the power of n
n = 5  # We want to raise the Fibonacci matrix to the 5th power
print(f"Raising Fibonacci matrix to power {n} (using binary exponentiation)")

# Consideration:
# When dealing with very large numbers (e.g., finding the Fibonacci number for a large 'n'), 
# integer overflow can be an issue in some languages. However, Python handles arbitrarily large integers natively.

# Subtopic: Matrix Multiplication
#-----------------------------------------------------------
# Matrix multiplication is a key operation in matrix exponentiation. The product of two 2x2 matrices A and B is:
# C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
# C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
# C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
# C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
# Performing this multiplication takes constant time O(1) for 2x2 matrices, 
# and matrix exponentiation can be optimized by repeated squaring (binary exponentiation).
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
print(f"Matrix A: {matrix_a}, Matrix B: {matrix_b}")

# The product of two matrices:
product_matrix = [
    [matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0],
     matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]],
    [matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0],
     matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]]
]
print(f"Product of Matrix A and Matrix B: {product_matrix}")

# Runtime Analysis for Matrix Multiplication:
# - Time Complexity: O(1) for 2x2 matrices, but for larger n x n matrices, it becomes O(n^3) 
#   using the standard matrix multiplication algorithm.
# - Space Complexity: O(1) for 2x2 matrices, but O(n^2) for storing larger product matrices.

# Subtopic: Special Use Cases
#-----------------------------------------------------------
# Matrix exponentiation is not only useful for the Fibonacci sequence but also for other linear recurrence relations.
# Example: The same method can be applied to solve the recurrence relation in dynamic programming problems like:
# - Tribonacci sequence
# - Population growth models with recursive relations
# - Discrete dynamical systems, etc.

# Edge case consideration:
# Matrix exponentiation is highly efficient, but it's essential to check edge cases such as when n = 0, 
# in which case the result should often be the identity matrix for consistent results.

# Subtopic: Practical Implementation Considerations
#-----------------------------------------------------------
# When implementing matrix exponentiation, it's important to ensure that matrix operations are optimized.
# This can include reducing redundant computations by memoization or using libraries like NumPy for large matrices.
# For larger matrices (e.g., 100x100 or more), utilizing GPU acceleration can greatly improve performance.
# While Python's built-in data structures handle small matrices well, performance will degrade for larger, more complex datasets.

# Example of potential improvement:
# Libraries like NumPy can handle large matrix operations much more efficiently.
# Instead of manually implementing matrix multiplication, NumPy's built-in matrix functions
# can leverage hardware optimizations, leading to faster and more reliable results.
import numpy as np
matrix_a_np = np.array([[1, 2], [3, 4]])
matrix_b_np = np.array([[5, 6], [7, 8]])
product_matrix_np = np.dot(matrix_a_np, matrix_b_np)
print(f"Product using NumPy: {product_matrix_np}")

# Final Thoughts:
# Matrix exponentiation is a crucial tool in algorithm design for problems involving recurrence relations.
# The combination of binary exponentiation and matrix multiplication allows for efficient solutions to 
# what would otherwise be computationally expensive operations.
# Understanding the interplay between time complexity and matrix operations is essential for writing 
# high-performance code in fields ranging from computer graphics to financial modeling.


#=================================================================================
# Algorithms, String Algorithms
#=================================================================================

# Topic: Reversing a String
#-----------------------------------------------------------
# Reversing a string is a common operation in many applications, such as when dealing with 
# palindromes or processing text in reverse order (e.g., undo operations). 
# Python makes it easy with slicing.
# Slicing is a Python feature that allows extracting portions of sequences (strings, lists, etc.).

# Example 1: Basic string reversal using slicing
# In this case, we use slicing with a step of -1 to reverse the entire string.
# The slice notation [::-1] means: start at the end of the string, go to the beginning, 
# and step backwards by 1.
s = "hello"
print(f"The reversed string of '{s}' is: '{s[::-1]}'")

# Runtime Analysis:
# - Time Complexity: O(n), where 'n' is the length of the string. We must process each character once.
# - Space Complexity: O(n), as a new reversed string of the same length is created.
# Best Case: O(n), as we still need to visit every character even in trivial cases like a 1-character string.
# Worst Case: O(n), same reasoning as the best case, since string reversal requires touching each character.

# Use case:
# String reversal is useful in tasks like detecting palindromes, performing undo operations, 
# or reversing a sequence for processing (such as reversing lines in a text editor).

# Consideration:
# Although Python strings are immutable (cannot be changed in place), slicing creates a new string,
# which may introduce performance bottlenecks in memory-sensitive applications if strings are large.

# Example 2: Reverse string manually using a loop
# This demonstrates reversing the string character by character. It’s less Pythonic, but helps to understand
# what happens under the hood.

s = "world"
reversed_s = ""  # Initialize an empty string
for char in s:   # Loop through each character in the original string
    reversed_s = char + reversed_s  # Prepend the current character to the reversed string
print(f"Reversed string of '{s}' manually is: '{reversed_s}'")

# Runtime Analysis:
# - Time Complexity: O(n), as we iterate over each character and concatenate it.
# - Space Complexity: O(n), since a new string is constructed.
# Best Case: O(n) for a string with 1 or more characters, no shortcuts.
# Worst Case: O(n) as string reversal requires touching each character.

# Pitfalls:
# - Prepending in a loop creates new strings each time due to immutability in Python. 
# This approach is less efficient than slicing because of the repeated memory allocations.
# Therefore, slicing is preferred for performance reasons when reversing strings in Python.

# Topic: Counting Characters in a String
#-----------------------------------------------------------
# Another common task in string algorithms is counting how many times a specific character appears.

# Example 3: Count occurrences of a specific character in a string using the built-in count() method
# Python provides a built-in method count() to count occurrences of substrings or characters.

s = "hello world"
char_to_count = 'o'
print(f"The character '{char_to_count}' appears {s.count(char_to_count)} time(s) in '{s}'.")

# Runtime Analysis:
# - Time Complexity: O(n), as the method scans through the string once to count the occurrences.
# - Space Complexity: O(1), no extra space is used apart from the counter.
# Best Case: O(n), even for cases where the character doesn't exist, the entire string is scanned.
# Worst Case: O(n), in cases where the character appears frequently or rarely.

# Use case:
# Useful for counting specific patterns or characters in strings, such as counting how often 
# vowels appear in a text, detecting frequency distributions of characters, or parsing log files.

# Example 4: Counting multiple characters using a dictionary
# This method is more general, allowing us to count occurrences of all characters in a string. 
# A dictionary stores each character as a key and its count as the value.

s = "abracadabra"
char_counts = {}
for char in s:
    if char in char_counts:
        char_counts[char] += 1  # Increment count if the character already exists in the dictionary
    else:
        char_counts[char] = 1   # Initialize count for the new character
print(f"Character counts in '{s}' are: {char_counts}")

# Runtime Analysis:
# - Time Complexity: O(n), where 'n' is the length of the string, as we need to visit each character once.
# - Space Complexity: O(k), where 'k' is the number of unique characters in the string.
# Best Case: O(n), where 'n' is the length of the string. The dictionary access is O(1) on average.
# Worst Case: O(n), with very frequent or very rare characters, but still linear.

# Consideration:
# Using a dictionary efficiently handles counting because dictionary lookups (hashmap) are O(1) on average.
# For extremely large strings, consider memory overhead if there are many unique characters. 

# Pitfalls:
# - Watch out for memory usage when strings contain a high number of unique characters, as the dictionary will grow.

# Topic: Checking if a String is a Palindrome
#-----------------------------------------------------------
# A palindrome is a string that reads the same forward and backward. This problem is commonly used
# in algorithmic challenges to test understanding of string manipulation and efficiency.

# Example 5: Checking for palindrome by comparing the original string with its reversed version
s = "racecar"
print(f"Is '{s}' a palindrome? {'Yes' if s == s[::-1] else 'No'}")

# Runtime Analysis:
# - Time Complexity: O(n), where 'n' is the length of the string, because we need to reverse the string and then compare.
# - Space Complexity: O(n), due to creating the reversed string.
# Best Case: O(n), we must always reverse the string, regardless of whether it's a palindrome or not.
# Worst Case: O(n), even for strings that are clearly not palindromes (such as strings with differing start and end characters).

# Consideration:
# Palindrome checks can be optimized by only comparing characters up to the middle of the string.
# This avoids unnecessary comparisons after reaching the halfway point.

# Example 6: Optimized palindrome check without reversing the string
# Instead of reversing the string, compare characters from the beginning and end moving towards the center.

s = "madam"
is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:  # Compare characters from the start and end
        is_palindrome = False
        break  # Exit the loop early if a mismatch is found
print(f"Is '{s}' a palindrome? {'Yes' if is_palindrome else 'No'}")

# Runtime Analysis:
# - Time Complexity: O(n/2) = O(n), where 'n' is the length of the string. We only compare up to half the string.
# - Space Complexity: O(1), since no additional space is used besides a few variables.
# Best Case: O(1) if the first comparison already shows that the string is not a palindrome.
# Worst Case: O(n) when the string is a palindrome, requiring comparisons for all characters.

# Pitfalls:
# Ensure the string is pre-processed (e.g., case-insensitive, trimmed of spaces) if you need to ignore 
# casing or spaces when checking for palindromes (e.g., "A man a plan a canal Panama").

#=================================================================================
# End of String Algorithms
#=================================================================================


#=================================================================================
#  Algorithms, String Algorithms, String Matching Algorithms
#=================================================================================

# Topic: Naive String Matching Algorithm
#-----------------------------------------------------------
# The naive string matching algorithm looks for a pattern 'P' in a text 'T' by checking 
# every possible starting position in 'T' where 'P' could appear.
# This algorithm compares each character in 'P' with the substring of 'T' of the same length.

text = "AABAACAADAABAABA"
pattern = "AABA"

# The outer loop considers each possible starting point in 'text' for matching
# The inner loop checks if the substring matches the pattern exactly
for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        print(f"Pattern found at index {i}")

# Runtime Analysis:
# - Time Complexity: O((n - m + 1) * m), where 'n' is the length of the text, 
#   and 'm' is the length of the pattern.
#   The outer loop runs 'n - m + 1' times, and each comparison takes O(m) time.
# - Space Complexity: O(1), since the algorithm uses constant space for comparisons.
# Best Case: O(n) occurs when the first few matches are found early, minimizing comparisons.
# Worst Case: O(n * m) happens when the algorithm checks almost all positions in the text,
#   especially when 'P' and 'T' share many common characters, but there is no match.

# Use case:
# The naive approach is ideal for small texts and patterns where readability is 
# prioritized over efficiency. However, for larger strings, more optimized algorithms 
# like KMP or Boyer-Moore are preferred.

# Consideration:
# This approach is inefficient for long texts and patterns with repetitive characters.
# Algorithms like Knuth-Morris-Pratt (KMP) or Boyer-Moore can significantly reduce the number of comparisons.


# Topic: Knuth-Morris-Pratt (KMP) Algorithm - Partial Matching (LPS Array)
#-----------------------------------------------------------
# The KMP algorithm improves the naive string matching by avoiding redundant comparisons.
# It does this by preprocessing the pattern into an LPS (longest proper prefix which is 
# also a suffix) array. This allows the algorithm to skip unnecessary checks, leading to 
# a more efficient search.

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

# LPS array for the pattern "ABABCABAB"
lps = [0, 0, 1, 2, 0, 1, 2, 3, 4]  # This array must be computed beforehand in the KMP algorithm
print(f"The LPS array for the pattern is: {lps}")

# Runtime Analysis:
# - Time Complexity: O(n + m), where 'n' is the length of the text and 'm' is the length of the pattern.
#   Preprocessing the LPS array takes O(m) time, and the string matching takes O(n) time.
# - Space Complexity: O(m) due to the storage of the LPS array.
# Best Case: O(n) occurs when there are very few mismatches, leading to minimal backtracking.
# Worst Case: O(n + m), where the algorithm has to process both the text and pattern fully.

# Use case:
# The KMP algorithm is useful when dealing with large texts and patterns, 
# especially when patterns contain repetitive sequences. It is ideal for applications 
# such as text searching in editors, pattern matching in DNA sequences, or network packet filtering.

# Consideration:
# Although KMP has better runtime efficiency than the naive approach, its LPS preprocessing 
# may add overhead in simpler cases or with small input sizes. 


# Topic: Boyer-Moore Algorithm - Bad Character and Good Suffix Heuristics
#-----------------------------------------------------------
# The Boyer-Moore algorithm uses two heuristics to optimize the search:
# 1. Bad Character Heuristic: When a mismatch occurs, it shifts the pattern based on 
#    the last occurrence of the mismatched character in the pattern.
# 2. Good Suffix Heuristic: When a mismatch occurs, it shifts the pattern to align 
#    the suffix of the pattern with the next possible match.

text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"

# Boyer-Moore shift for the bad character heuristic
bad_char_shift = {'A': 1, 'E': 4, 'H': 7, 'I': 3, 'L': 1, 'M': 1, 'P': 1, 'R': 5, 'S': 2, 'X': 6}
print(f"Bad character shift table: {bad_char_shift}")

# In an actual Boyer-Moore implementation, these tables would be dynamically generated
# for any pattern and text combination. They allow the algorithm to skip over large sections
# of the text, leading to a potential best-case performance of O(n/m), where 'm' is the length
# of the pattern and 'n' is the length of the text.

# Runtime Analysis:
# - Time Complexity: Best case O(n/m), but on average it is O(n) where 'n' is the length of the text.
#   Worst case is still O(n * m), but this is rare due to the two heuristics working together.
# - Space Complexity: O(m), for storing the shift tables based on the pattern.
# Best Case: O(n/m), where large sections of the text can be skipped based on mismatches.
# Worst Case: O(n * m), but this happens rarely, usually when many characters match but a late mismatch occurs.

# Use case:
# Boyer-Moore is one of the fastest string search algorithms in practice for typical text 
# searches, especially when searching long patterns in long texts. It is ideal for use 
# in applications like text processing software, web search engines, and even DNA sequence analysis.

# Consideration:
# The Boyer-Moore algorithm may not be as efficient with very small patterns or with patterns 
# containing many repeated characters (e.g., 'AAAAA') where the heuristics do not provide 
# much advantage. In such cases, KMP or other algorithms might be preferred.

#=================================================================================


#=================================================================================
# String Matching Algorithms: Knuth-Morris-Pratt (KMP) Algorithm
#=================================================================================

# Topic: Knuth-Morris-Pratt (KMP) Algorithm for String Matching
#-------------------------------------------------------------
# The KMP algorithm is a powerful technique for string matching. It preprocesses the pattern to create a 
# partial match table (also called the "longest prefix which is also suffix" array), which allows the algorithm 
# to skip unnecessary comparisons while searching for the pattern in the text. 
# This approach significantly reduces the worst-case time complexity compared to brute force methods.

# Subtopic: Example 1 - Simple string matching
#--------------------------------------------------------------
# Let's demonstrate how KMP would be used in a simple string matching scenario. 
# Assume we have the following text and pattern.
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

print(f"Text: {text}")
print(f"Pattern: {pattern}")

# Sub-subtopic: Preprocessing phase - Building the LPS (Longest Prefix Suffix) array
#--------------------------------------------------------------
# The LPS array stores the lengths of the proper prefix of the pattern that are also suffixes. 
# This array helps in determining the next positions to compare in the pattern when a mismatch occurs.
# Let's show the LPS array for the given pattern:
# Pattern: ABABCABAB
# LPS:     0 1 2 0 1 2 3 4 5
# Explanation:
# - The first two characters 'A' and 'B' have no proper prefix that matches a suffix, so the LPS values are 0.
# - The first three characters "ABA" have the prefix "A" matching the suffix "A", so the LPS value is 1 for the third position.
# - This continues, giving us the LPS array, which is used during the matching phase.

# Subtopic: Example 2 - Visualizing pattern matching progress
#--------------------------------------------------------------
# The KMP algorithm compares the pattern with the text, but when a mismatch happens, it uses the LPS array to avoid unnecessary comparisons.
# Let's visualize how the algorithm works. Assume the following scenario:
# Text:      ABABDABACDABABCABAB
# Pattern:   ABABCABAB
# The algorithm starts comparing the first character of the pattern with the first character of the text. 
# If a mismatch occurs after a few matches, instead of restarting the comparison from the next character of the text, 
# the LPS array is consulted to decide how far the pattern can shift while keeping the partial match intact.

# Runtime Analysis:
#--------------------------------------------------------------
# - Time Complexity: O(n + m), where 'n' is the length of the text and 'm' is the length of the pattern.
#   This is due to the preprocessing step (O(m)) and the actual matching step (O(n)).
#   The matching process ensures that each character is compared at most once, making it efficient.
# - Space Complexity: O(m) because the algorithm needs additional space to store the LPS array.
# Best Case: O(n + m) when there are very few or no mismatches, and the pattern is quickly found.
# Worst Case: O(n + m) even when there are frequent mismatches because the LPS array ensures that redundant comparisons are skipped.

# Use case:
# The KMP algorithm is ideal for large-scale text matching problems where brute force methods would be inefficient.
# It is commonly used in text editors, plagiarism detection tools, and search engines.

# Subtopic: Example 3 - Handling edge cases
#--------------------------------------------------------------
# Edge Case 1: Pattern is longer than the text
# When the pattern length exceeds the text length, the algorithm doesn't perform any comparison, 
# as it is impossible for the pattern to be found in the text.
text = "A"
pattern = "ABABCABAB"
print(f"Text: {text}")
print(f"Pattern: {pattern}")
# No comparison is done in this case since the pattern cannot possibly fit within the text.

# Edge Case 2: Pattern is an empty string
# If the pattern is empty, it's trivially found at every position of the text.
text = "A"
pattern = ""
print(f"Text: {text}")
print(f"Pattern (empty): {pattern}")
# In this case, we could return an array of positions where the empty pattern "matches," but typically,
# this case is handled by returning 0 (or every position, depending on the application).

# Edge Case 3: Text is an empty string
# If the text is empty but the pattern is not, no match is possible.
text = ""
pattern = "ABABCABAB"
print(f"Text (empty): {text}")
print(f"Pattern: {pattern}")
# Here, no matches are found since there's no text to search in.

# Considerations:
#--------------------------------------------------------------
# 1. Ensure proper handling of LPS array calculation, as an incorrectly built LPS array will lead to faulty pattern matching.
# 2. The KMP algorithm assumes the pattern and text consist of uniform character types (like ASCII or Unicode). 
#    Handling mixed encodings might lead to issues or require extra preprocessing.
# 3. Integer overflow is not an issue in Python, but in languages like C/C++, we need to be cautious about 
#    array indexing, especially when dealing with large datasets.

# Uncommon Insight:
#--------------------------------------------------------------
# Although KMP is one of the most efficient string matching algorithms, for some specific cases like searching in DNA sequences 
# where the alphabet size is very small (only A, T, G, C), other algorithms like Boyer-Moore or suffix array techniques 
# may outperform KMP because of their ability to skip larger sections of the text on each mismatch.


#=================================================================================
# Algorithms, String Algorithms, String Matching Algorithms: Rabin-Karp Algorithm
#=================================================================================

# Topic: Rabin-Karp Algorithm for String Matching
#-----------------------------------------------------------
# The Rabin-Karp algorithm is used to search for a pattern string within a larger text string.
# It uses hashing to speed up the comparison of substrings, providing an average-case time complexity of O(n + m),
# where 'n' is the length of the text and 'm' is the length of the pattern.

# Subtopic: Understanding the concept of rolling hash
#-----------------------------------------------------------
# Instead of recalculating the hash of every substring from scratch, the rolling hash technique
# allows you to compute the hash of the next substring using the previous substring’s hash, which saves time.
# The formula for the rolling hash is:
# new_hash = (old_hash - hash_value_of_leftmost_char) * d + hash_value_of_new_rightmost_char
# where 'd' is the base (number of characters in the alphabet) and 'q' is a large prime number used to reduce hash collisions.

# Example scenario: Searching for the pattern 'abc' in the text 'abcababc'.
# First, calculate the hash of the pattern and the initial substring of the text with the same length as the pattern.

# Assume we're working with ASCII, so 'd' (number of characters in the alphabet) is 256.
# 'q' is a large prime number to avoid hash collisions.
d = 256
q = 101  # Prime number used for mod operation to reduce collisions.

# Initialize the text and pattern
text = "abcababc"
pattern = "abc"
n = len(text)
m = len(pattern)

# Initializing hash values for the pattern and the first window of text
pattern_hash = 0  # Hash value for the pattern
text_hash = 0     # Hash value for the text window
h = 1             # The value of d^(m-1), used in the rolling hash

# Subtopic: Preprocessing step - Calculating initial hash values
#-----------------------------------------------------------
# We calculate the hash value for the pattern and the initial window of the text.
# Also, we compute the value of h = d^(m-1) to remove the leftmost character during rolling hash.
for i in range(m-1):
    h = (h * d) % q

# Best Case Runtime Analysis:
# - Best case occurs when the pattern matches in the first comparison (O(n + m)).
# Worst Case Runtime Analysis:
# - Worst case occurs when hash collisions happen frequently, requiring full character comparisons (O(n*m)).

# Calculate the hash value of the pattern and the first window of text
for i in range(m):
    pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
    text_hash = (d * text_hash + ord(text[i])) % q

# Subtopic: Rolling hash - Sliding the window over the text
#-----------------------------------------------------------
# Now, we slide the window over the text, one character at a time.
# If the hash values match, we then check the actual substring (since hash collisions can occur).
for i in range(n - m + 1):
    
    # If the hash values match, check the actual characters
    if pattern_hash == text_hash:
        # Check if the substrings are actually equal
        if text[i:i+m] == pattern:
            print(f"Pattern found at index {i}")

    # Calculate hash value for the next window of text:
    # Remove leading character and add the next character to the window.
    if i < n - m:
        text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
        
        # We might get a negative value for text_hash, convert it to positive
        if text_hash < 0:
            text_hash += q

# Runtime Analysis:
# - Time Complexity: Average case O(n + m) due to efficient hashing and sliding window mechanism.
# - Space Complexity: O(1) extra space used for hash calculations and variables.
# - Best Case: O(n + m), when no hash collisions occur, and matches are quickly identified.
# - Worst Case: O(n*m), when hash collisions frequently occur, forcing character-by-character comparisons.

# Subtopic: Edge cases and potential pitfalls
#-----------------------------------------------------------
# Edge case 1: Empty pattern or text
# If either the pattern or the text is empty, string matching cannot be performed.
text_empty = ""
pattern_empty = "abc"
if not text_empty or not pattern_empty:
    print("One of the strings is empty; string matching cannot be performed.")

# Edge case 2: Pattern longer than text
# If the pattern is longer than the text, it's impossible to find the pattern.
text = "abc"
pattern = "abcd"
if len(pattern) > len(text):
    print("Pattern is longer than the text; string matching cannot be performed.")

# Subtopic: Use cases for Rabin-Karp
#-----------------------------------------------------------
# 1. Detecting plagiarism in large bodies of text, where string matching is necessary across many documents.
# 2. Searching for a substring in DNA sequences or other large datasets where frequent substring matches are required.
# 3. Simple word search in documents, where false positives can be tolerated but efficient matching is desired.

# Consideration:
# While Rabin-Karp is efficient in practice for average cases, frequent hash collisions in worst-case scenarios can degrade 
# performance to O(n*m). Using a large prime number 'q' reduces the likelihood of such collisions, improving overall efficiency.



#=================================================================================
# Algorithms, String Algorithms: Boyer-Moore String Matching Algorithm
#=================================================================================

# Topic: Boyer-Moore Algorithm Overview
#-----------------------------------------------------------
# The Boyer-Moore algorithm is an efficient string-matching algorithm.
# It compares the pattern to the text from right to left, using heuristics to skip sections of the text, reducing the number of comparisons.
# Boyer-Moore uses two heuristics:
# 1. Bad Character Heuristic: Moves the pattern based on the rightmost occurrence of a mismatched character.
# 2. Good Suffix Heuristic: Moves the pattern based on suffix matches.
# It's particularly effective when the pattern is long and the alphabet is large.

# Example:
# We will print comparisons between a text and a pattern using a simplified logic.
# Note: The complete Boyer-Moore algorithm involves additional preprocessing, but this illustrates the matching concept.

text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"

# Let's assume the pattern is being compared from the last character to the first
# To illustrate the comparison process:
print(f"Text: {text}")
print(f"Pattern: {pattern}")

# Initial comparison starts from the end of the pattern.
# In practice, the last character of the pattern is aligned with the corresponding character in the text.
# If a mismatch occurs, the pattern is shifted according to the bad character or good suffix rules.
print(f"Comparing '{text[17]}' from text with '{pattern[6]}' from pattern")

# This comparison is a match, so we continue comparing the preceding characters.
print(f"Comparing '{text[16]}' from text with '{pattern[5]}' from pattern")

# If a mismatch occurs, let's say between 'P' in text and 'M' in pattern, the pattern will shift.
print(f"Mismatch: '{text[15]}' from text and '{pattern[4]}' from pattern")

# In a real Boyer-Moore implementation, the shift would depend on the heuristics.
# However, here we illustrate the concept by printing that a shift would occur.
print("Pattern shift occurs based on mismatch")

# Runtime Analysis:
# - Best Case: O(n/m), where 'n' is the length of the text and 'm' is the length of the pattern.
#   The algorithm performs very well when there are frequent mismatches, as large portions of the text are skipped.
# - Worst Case: O(n*m), occurring in pathological cases like when both the text and pattern consist of the same repeating character.
#   For example, text = "AAAAAAAAA" and pattern = "AAA", since the pattern keeps partially matching.
# - Average Case: Typically much faster than O(n*m), making it preferred in practice for large texts with long patterns.

# Use case:
# Boyer-Moore is highly efficient for searching in large bodies of text, such as scanning documents or DNA sequences, especially when the alphabet is large.
# It outperforms simpler algorithms like brute force when dealing with large datasets where the pattern is long.

# Considerations:
# Preprocessing the pattern takes O(m + |Σ|), where |Σ| is the size of the alphabet.
# While preprocessing adds overhead, it pays off for long texts. However, for very short patterns, algorithms like Knuth-Morris-Pratt (KMP) may be faster due to less setup.
# The Boyer-Moore algorithm is case-sensitive by default, so for case-insensitive matching, convert both the text and pattern to lowercase or uppercase.

# Pitfalls:
# Care must be taken with the bad character heuristic if the alphabet is small (e.g., binary data), as it may not yield large shifts.
# For highly repetitive patterns and text, Boyer-Moore's performance can degrade to O(n*m), meaning other algorithms might be more efficient in these specific cases.


#=================================================================================
# String Algorithms: Longest Palindromic Substring
#=================================================================================
# Problem Statement:
# Given a string, we need to find the longest palindromic substring within the given string.
# A palindrome is a sequence of characters that reads the same forward and backward.

# Example String:
string = "babad"

# Subtopic: Understanding Palindromes
#-----------------------------------------------------------
# A palindrome can be of odd or even length:
# - Odd-length palindrome: "aba", where 'b' is the center.
# - Even-length palindrome: "abba", where the center is between 'b' and 'b'.
# This understanding is crucial for deciding the approach to solving the problem.

# Subtopic: Expanding around center approach
#-----------------------------------------------------------
# A common technique to find the longest palindrome in O(n^2) time complexity involves expanding
# around each character (or between two consecutive characters) as potential centers.
# This approach is simple and intuitive, allowing us to check all potential centers without needing extra memory.
# We start by treating each index of the string as a center and expand outward while the substring remains a palindrome.

# Subtopic: Iterating through each center and expanding
#-----------------------------------------------------------
# Let's consider each index of the string as a potential center for a palindrome.
# We expand outward while the substring remains a palindrome, checking both odd-length and even-length cases.

# We begin with index 2 ('b') of "babad", treating it as a center for both odd and even cases:
center_index = 2
left, right = center_index, center_index

# Odd-length palindrome:
#-----------------------------------------------------------
# Here, we expand around a single center. Starting at index 2, we check left and right.
# Example: Starting from 'b' at index 2, expanding left (index 1, 'a') and right (index 3, 'a'),
# the substring becomes "aba" which is a palindrome.
while left >= 0 and right < len(string) and string[left] == string[right]:
    print(f"Odd-length palindrome found: {string[left:right+1]}")
    left -= 1
    right += 1

# Even-length palindrome:
#-----------------------------------------------------------
# For even-length palindromes, the center is between two consecutive characters.
# Example: Considering 'bb' between index 1 and 2 in "abba", we expand outward and check the characters.
# In this case, we start with two consecutive indices (center_index and center_index + 1).
left, right = center_index, center_index + 1
while left >= 0 and right < len(string) and string[left] == string[right]:
    print(f"Even-length palindrome found: {string[left:right+1]}")
    left -= 1
    right += 1

# Runtime Analysis:
#-----------------------------------------------------------
# - Time Complexity: O(n^2), where 'n' is the length of the string.
#   For each center, we expand outward in both directions (left and right), leading to an O(n) check for each of the n centers.
# - Space Complexity: O(1), since we are using only constant space to track indices and the palindrome.
# Best Case: O(n), where the string consists of all identical characters (e.g., "aaaa"). The longest palindrome would be the entire string.
# Worst Case: O(n^2), when the string has no palindromes longer than a single character, forcing us to check all potential centers.

# Use case:
#-----------------------------------------------------------
# This algorithm is useful in string manipulation problems where the longest palindromic substring must be identified quickly without needing extra memory.
# It is applicable in tasks like DNA sequence analysis, pattern recognition, or text processing where palindromic structures carry significance.

# Considerations:
#-----------------------------------------------------------
# - In cases where performance is critical and the input string is very large, a more advanced approach like Manacher's Algorithm can be used to reduce time complexity to O(n).
# - Be mindful of edge cases, such as strings of length 1 (trivially a palindrome) or strings with no palindromes longer than one character.


#=================================================================================
# Topic: String Algorithms - Checking if Two Strings are Anagrams
#=================================================================================

# An anagram is a rearrangement of the characters of one string to form another string.
# To check if two strings are anagrams, we can use different methods.
# Below we explore multiple approaches, their runtimes, and their potential pitfalls.

#-----------------------------------------------------------
# Method 1: Sorting Approach
#-----------------------------------------------------------
# Concept:
# - Two strings are anagrams if their sorted character arrays are identical.
# - Sorting both strings and comparing them achieves the goal.
# - Time Complexity: O(n log n), where 'n' is the length of the string, due to sorting.
# - Space Complexity: O(n), due to the storage needed for the sorted strings.
string1 = "listen"
string2 = "silent"
print(f"Are '{string1}' and '{string2}' anagrams (using sorting)? {sorted(string1) == sorted(string2)}")

# Runtime Analysis:
# - Time Complexity: O(n log n) because sorting is typically the most expensive operation here.
# - Space Complexity: O(n) since sorting creates new arrays.
# Best Case: O(n log n) — Sorting is necessary in all cases.
# Worst Case: Also O(n log n), as sorting has to be done fully.

# Use case:
# Suitable for moderate-length strings where sorting is acceptable, and memory usage isn't critical.

# Consideration:
# This approach creates additional space for sorted arrays. For very large strings, 
# consider alternate methods to save space or reduce time complexity.

#-----------------------------------------------------------
# Method 2: Frequency Count Approach
#-----------------------------------------------------------
# Concept:
# - Another efficient way to check for anagrams is by counting character frequencies.
# - If both strings have identical character frequency distributions, they are anagrams.
# - Time Complexity: O(n), where 'n' is the length of the string.
# - Space Complexity: O(1) if we assume only lowercase English letters (fixed alphabet size).
from collections import Counter

string1 = "triangle"
string2 = "integral"
print(f"Are '{string1}' and '{string2}' anagrams (using frequency count)? {Counter(string1) == Counter(string2)}")

# Runtime Analysis:
# - Time Complexity: O(n), as we are just counting characters, which takes linear time.
# - Space Complexity: O(1) if we assume a fixed alphabet size (e.g., lowercase English letters).
# - If the alphabet size isn't fixed, the space complexity becomes O(n) because we may need
#   to store up to 'n' unique characters.
# Best Case: O(n) — All character counts match early on.
# Worst Case: O(n) — We must compare the entire frequency distribution.

# Use case:
# This is a preferred method for large strings, especially if the alphabet size is fixed and small.

# Consideration:
# Counters offer a more memory-efficient solution, especially when the input size is large.
# Be cautious when using this method for strings with different alphabets or non-standard characters,
# as this could increase memory usage.

#-----------------------------------------------------------
# Method 3: XOR Character Approach (Advanced/Uncommon)
#-----------------------------------------------------------
# Concept:
# - A lesser-known method involves XORing the ASCII values of characters from both strings.
# - If the two strings are anagrams, the XOR of all characters will be zero.
# - This method is limited to strings that have the same length and character set.
# - Time Complexity: O(n), where 'n' is the length of the strings.
# - Space Complexity: O(1), since no extra space is needed for counting or sorting.
string1 = "abc"
string2 = "bca"
xor_result = 0

# XOR all characters of both strings
for char in string1 + string2:
    xor_result ^= ord(char)

print(f"Are '{string1}' and '{string2}' anagrams (using XOR)? {xor_result == 0}")

# Runtime Analysis:
# - Time Complexity: O(n), as we are only traversing the strings once.
# - Space Complexity: O(1), no extra storage is used.
# Best Case: O(n), as XOR operates in linear time.
# Worst Case: O(n), linear in all cases.

# Use case:
# Useful when memory is highly constrained or when the character set is simple (e.g., ASCII).
# This method avoids the overhead of sorting or storing frequency counts.

# Consideration:
# This method does not work for strings of different lengths or character sets.
# It's a bit tricky to implement and understand, so use it cautiously in production environments.
# Additionally, this approach is sensitive to encoding issues, as it relies on the ASCII values of characters.

#-----------------------------------------------------------
# Method 4: Hash Map/Dictionary Approach
#-----------------------------------------------------------
# Concept:
# - Using a hash map or dictionary, we can count the occurrences of each character.
# - For two strings to be anagrams, their frequency distributions must match.
# - Time Complexity: O(n), where 'n' is the length of the string.
# - Space Complexity: O(1), if we assume a fixed character set size.

string1 = "night"
string2 = "thing"
char_count = {}

# Count characters in the first string
for char in string1:
    char_count[char] = char_count.get(char, 0) + 1

# Subtract the count based on the second string
for char in string2:
    if char not in char_count:
        char_count[char] = -1
    else:
        char_count[char] -= 1

# Check if all counts are zero
anagram = all(value == 0 for value in char_count.values())
print(f"Are '{string1}' and '{string2}' anagrams (using hash map)? {anagram}")

# Runtime Analysis:
# - Time Complexity: O(n), since we traverse each string only once.
# - Space Complexity: O(1), assuming the alphabet size is fixed.
# Best Case: O(n), all characters match quickly.
# Worst Case: O(n), we need to process every character.

# Use case:
# This method is especially useful when working with larger strings and the frequency of character 
# comparisons needs to be minimized. It scales well with both time and space for larger strings.

# Consideration:
# Be careful when using this method with large character sets, as it can increase the memory footprint.
# Handling edge cases (like strings of different lengths) can require additional logic.

#-----------------------------------------------------------
# Additional Insights:
# - While the sorting approach is simple and intuitive, the counting approach (using frequency counters) 
#   is more efficient for larger strings or applications where memory usage is critical.
# - The XOR method is rarely used due to its limitation with character sets and encoding issues.
# - Choosing the right algorithm depends on the trade-off between space and time complexity.
# - Real-world applications like spell checkers, text comparison tools, and security algorithms can benefit 
#   from efficient anagram detection.

#=================================================================================
# String Algorithms: Substring Search Algorithms
#=================================================================================

# Topic: Naive Approach for Substring Search
#-----------------------------------------------------------
# The naive approach compares the target substring (pattern) with every possible
# substring of the main string (text) of the same length. This involves iterating
# through each character in the main string, then checking if the next characters match
# the pattern.

# Example: Searching for a pattern "ABC" in a text "AABABC"
text = "AABABC"
pattern = "ABC"

# Outer loop: Iterate through the main string where pattern can fit
# (len(text) - len(pattern) + 1 ensures that the loop stops before the pattern exceeds the text length)
for i in range(len(text) - len(pattern) + 1):
    # Inner condition: Check if the substring of 'text' starting at index 'i' matches 'pattern'
    if text[i:i+len(pattern)] == pattern:
        print(f"Pattern found at index {i}")

# Runtime Analysis:
# - Time Complexity: O((n - m + 1) * m) where n is the length of 'text' and m is the length of 'pattern'.
#   In the worst case, every substring of length 'm' is compared to the 'pattern', leading to O(n * m).
# - Space Complexity: O(1) since no additional memory is required beyond the input strings.
# Best Case: The first characters of the text match the pattern, so the complexity reduces to O(m).
# Worst Case: The pattern is not found, or is located at the end of the string, so we check all substrings (O(n * m)).

# Use case:
# The naive approach is simple and works well for small strings or situations where performance is not critical.
# However, for large inputs or when patterns need to be matched frequently, more efficient algorithms are preferred.

# Consideration:
# The naive approach can be inefficient for long strings or patterns, especially if the pattern appears near the end
# of the text. In such cases, the entire string is scanned unnecessarily even after mismatches are found early on.

# -----------------------------------------------------------

# Topic: Knuth-Morris-Pratt (KMP) Algorithm for Substring Search
#-----------------------------------------------------------
# The KMP algorithm improves the naive approach by eliminating unnecessary comparisons. 
# It achieves this by preprocessing the pattern to create a 'lps' (longest prefix that is also a suffix) array,
# which allows the algorithm to skip comparisons when mismatches are found.
# This results in O(n + m) time complexity, a significant improvement over the O(n * m) of the naive method.

# For simplicity, the following example focuses on the substring search process after preprocessing has occurred.

# Example: Searching for a pattern "ABC" in a text "AABABC" using the KMP algorithm
text = "AABABC"
pattern = "ABC"
lps = [0, 0, 0]  # Precomputed LPS array for the pattern "ABC"

# 'i' is the index for text, 'j' is the index for pattern
i = 0  # Initial index of text
j = 0  # Initial index of pattern

while i < len(text):
    # Check if characters match
    if text[i] == pattern[j]:
        i += 1
        j += 1
        # If we have matched the entire pattern
        if j == len(pattern):
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]  # Use LPS to avoid unnecessary comparisons
    else:
        # Mismatch: Use the LPS array to determine the next index in the pattern
        if j != 0:
            j = lps[j - 1]
        else:
            i += 1

# Runtime Analysis:
# - Time Complexity: O(n + m), where 'n' is the length of the text and 'm' is the length of the pattern.
#   This is because each character in the text is processed at most once.
# - Space Complexity: O(m) for storing the 'lps' array.
# Best Case: The pattern is found early in the text, leading to fewer comparisons, still O(n + m).
# Worst Case: The pattern is not found or involves repetitive partial matches, but the LPS array prevents full rechecks.

# Use case:
# The KMP algorithm is ideal for large-scale pattern matching problems, such as DNA sequence analysis or real-time
# text search in large datasets. It ensures that patterns can be searched in linear time.

# Consideration:
# Preprocessing the pattern (building the LPS array) is crucial to achieving the linear time complexity.
# While the time complexity is linear, the setup and understanding of the LPS array can be challenging for beginners.

# -----------------------------------------------------------

# Topic: Boyer-Moore Algorithm for Substring Search
#-----------------------------------------------------------
# The Boyer-Moore algorithm searches for patterns by scanning the text from right to left
# and skipping sections of the text based on the pattern's mismatches. 
# It uses two heuristics: the bad character rule and the good suffix rule to maximize the number of shifts.
# This approach can achieve O(n / m) in the best case.

# Example: Searching for a pattern "ABC" in a text "AABABC" using Boyer-Moore algorithm
# Note: Full implementation would require additional preprocessing for both heuristics, but we are focusing on the core idea.
text = "AABABC"
pattern = "ABC"

# Outer loop: Start from the rightmost character of the current window in the text
i = len(pattern) - 1  # Set 'i' to the last character of the first window in the text

while i < len(text):
    # Inner loop: Compare the pattern with the current window in the text
    j = len(pattern) - 1  # Start comparing from the last character of the pattern
    while j >= 0 and text[i] == pattern[j]:
        i -= 1
        j -= 1
    # If j < 0, it means the pattern has been matched
    if j < 0:
        print(f"Pattern found at index {i + 1}")
        i += len(pattern)  # Shift to the next potential match location
    else:
        # Shift the window based on the bad character rule or good suffix rule (preprocessing omitted here)
        i += max(1, j)  # Simplified: shift by at least 1, but heuristics can make larger shifts

# Runtime Analysis:
# - Time Complexity: In the best case, O(n / m) due to the large skips enabled by the heuristics.
#   In the worst case, O(n * m), but this is rare when using both bad character and good suffix rules.
# - Space Complexity: O(m) for the preprocessed data structures (bad character table, good suffix table).
# Best Case: When the pattern is highly unique, large skips can reduce the time complexity to O(n / m).
# Worst Case: If the text and pattern share many repeated characters, the time complexity can degrade to O(n * m).

# Use case:
# Boyer-Moore is highly efficient for searching long patterns in large texts. It is commonly used in search engines
# and text editors where performance is critical.

# Consideration:
# The Boyer-Moore algorithm's performance depends heavily on preprocessing. It is most beneficial when dealing with long
# patterns and large texts. For shorter patterns, simpler algorithms like KMP may perform better due to lower setup costs.


#=================================================================================
# Algorithms, Miscellaneous Algorithms
#=================================================================================

# Topic: Factorial Calculation
#-----------------------------------------------------------
# The factorial of a non-negative integer 'n' is the product of all positive integers <= n.
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Factorial is represented as n! and is used in combinatorics, probability, and analysis of algorithms.
n = 5
factorial = 1
# We initialize 'factorial' to 1 because the factorial of 0 is defined as 1 (base case).
for i in range(1, n + 1):
    factorial *= i  # Iteratively multiply the current value by 'i' to compute n!
print(f"The factorial of {n} is: {factorial}")

# Runtime Analysis:
# - Time Complexity: O(n), as we need to iterate from 1 to n.
# - Space Complexity: O(1), since we are using a constant amount of additional space (only 'factorial' and 'i' variables).
# Best Case: O(n), even if n is 1, the loop runs once.
# Worst Case: O(n), where n is large, and we must iterate n times.

# Use cases:
# Factorials are commonly used in:
# 1. Combinatorics (e.g., calculating permutations and combinations).
# 2. Probability (e.g., binomial coefficients).
# 3. Algorithm complexity analysis.
# 4. Solving recurrence relations in dynamic programming.
# 
# Considerations:
# Factorial grows very quickly, leading to overflow in most programming languages when n becomes large.
# In Python, the built-in 'int' can handle arbitrarily large integers, but in other languages, such as C/C++, 
# you might encounter integer overflow with larger values (e.g., n > 20 for 32-bit integers).
# Python's arbitrary-precision integers make it suitable for handling large factorial calculations.

#-----------------------------------------------------------

# Topic: Fibonacci Sequence (Iterative Approach)
#-----------------------------------------------------------
# The Fibonacci sequence is a series where each number is the sum of the two preceding ones.
# The sequence starts with 0 and 1, i.e., F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2.
# This algorithm uses iteration to calculate Fibonacci numbers, avoiding recursion's potential pitfalls like stack overflow.
n = 10
a, b = 0, 1  # Initialize the first two Fibonacci numbers.
print(a, end=" ")  # Print the first number.
# Use a loop to generate Fibonacci numbers up to 'n'.
for _ in range(n - 1):  # We already printed the first number, so we loop n-1 times.
    print(b, end=" ")  # Print the next Fibonacci number.
    a, b = b, a + b  # Update 'a' and 'b' to the next Fibonacci pair.
print()

# Runtime Analysis:
# - Time Complexity: O(n), as we compute each Fibonacci number once.
# - Space Complexity: O(1), since only a few variables (a, b, and the loop counter) are used.
# Best Case: O(n), the complexity remains linear for any value of n.
# Worst Case: O(n), as the loop always iterates exactly n-1 times.

# Use cases:
# The Fibonacci sequence appears in various mathematical and scientific applications, such as:
# 1. Dynamic programming problems, where the recursive structure naturally arises.
# 2. Algorithms like Fibonacci search (an improvement over binary search in some cases).
# 3. Number theory and combinatorial problems.
# 
# Considerations:
# Unlike the recursive version, this iterative approach is space-efficient and avoids the risk of stack overflow.
# Fibonacci numbers grow exponentially, so large values of 'n' will result in very large numbers, 
# though Python's integers can handle this (arbitrary precision).
# An optimization, such as using matrix exponentiation, can reduce time complexity to O(log n) for large 'n'.

#-----------------------------------------------------------

# Topic: Greatest Common Divisor (GCD) using Euclidean Algorithm
#-----------------------------------------------------------
# The Euclidean algorithm is an efficient method to compute the greatest common divisor (GCD) of two numbers.
# GCD is the largest positive integer that divides both numbers without a remainder.
# The algorithm is based on the property: gcd(a, b) = gcd(b, a % b).
# This property allows us to reduce the problem size significantly with each iteration.
a, b = 48, 18
while b != 0:  # Continue until the remainder is zero.
    a, b = b, a % b  # Replace 'a' with 'b' and 'b' with 'a % b'.
print(f"The GCD of 48 and 18 is: {a}")

# Runtime Analysis:
# - Time Complexity: O(log(min(a, b))), since each iteration reduces the problem size by a factor of about 2.
# - Space Complexity: O(1), because only a fixed number of variables are used.
# Best Case: O(1), when one number is a divisor of the other from the start.
# Worst Case: O(log(min(a, b))), such as for consecutive Fibonacci numbers where the number of iterations is maximized.

# Use cases:
# GCD has numerous applications in areas like:
# 1. Simplifying fractions.
# 2. Cryptography (e.g., RSA algorithm).
# 3. Modular arithmetic.
# 4. Solving Diophantine equations in number theory.
# 
# Considerations:
# The Euclidean algorithm is highly efficient, even for large numbers. In practice, it is faster than simple division-based methods.
# Be cautious of integer overflow when working with very large numbers in lower-level languages.

#-----------------------------------------------------------

# Topic: Prime Number Check (Trial Division)
#-----------------------------------------------------------
# A prime number is only divisible by 1 and itself.
# To check if a number 'n' is prime, we only need to test for divisibility up to the square root of 'n'.
# This reduces the number of checks significantly compared to testing all numbers up to 'n'.
n = 29
is_prime = True  # Assume n is prime unless proven otherwise.
if n <= 1:
    is_prime = False  # Numbers <= 1 are not prime.
else:
    for i in range(2, int(n**0.5) + 1):  # Test divisibility up to sqrt(n).
        if n % i == 0:  # If divisible, n is not prime.
            is_prime = False
            break  # No need to continue testing after finding a divisor.
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

# Runtime Analysis:
# - Time Complexity: O(√n), as we only check divisibility up to the square root of 'n'.
# - Space Complexity: O(1), since we only use a fixed amount of space.
# Best Case: O(1), when n is small (e.g., 2 or 3) or when a small divisor is found early.
# Worst Case: O(√n), when n is prime, requiring us to check all potential divisors up to √n.

# Use cases:
# Prime number checks are used in:
# 1. Cryptography (e.g., key generation in RSA).
# 2. Number theory.
# 3. Finding prime factors of large numbers.
# 
# Considerations:
# This method is efficient for small to moderately large numbers. For very large numbers (e.g., in cryptographic applications),
# more advanced algorithms like the Miller-Rabin primality test are used, which provide probabilistic guarantees of primality.


#=================================================================================
# Algorithms, Miscellaneous Algorithms, Randomized Algorithms
#=================================================================================

# Topic: Randomized Algorithms
#-----------------------------------------------------------
# Randomized algorithms use random numbers at one or more points during their logic to influence 
# decision-making. These algorithms are useful when a deterministic solution is either too slow 
# or complex, and randomness offers a simpler, faster solution on average.

# Subtopic: Randomized Number Generator
#-----------------------------------------------------------
# Importing the `random` module to generate random numbers.
# This is a foundational operation in randomized algorithms.
import random

# Generating a random integer between 1 and 100 (inclusive).
# Random integers are useful for scenarios like shuffling data, simulations, or random sampling.
random_number = random.randint(1, 100)
print(f"A random number between 1 and 100: {random_number}")

# Runtime Analysis:
# - Time Complexity: O(1), generating a random number in a bounded range is constant time.
# - Space Complexity: O(1), only one variable is allocated to store the random number.
# Best Case: O(1), regardless of the range, the random number generation is constant time.
# Worst Case: O(1), the operation is independent of the input size.

# Use Case:
# This is often used in simulations, games, or any scenario where unpredictability is needed.
# For instance, randomized algorithms in sorting or selection processes benefit from this mechanism.

# Consideration:
# Randomness is pseudorandom; this means numbers are determined algorithmically and 
# hence, not truly random. For cryptographic purposes, specialized random generators 
# like `secrets` (Python's `secrets` module) should be used for security purposes.


# Subtopic: Randomized Shuffling
#-----------------------------------------------------------
# Shuffling the elements of a list randomly using the Fisher-Yates (Knuth) shuffle algorithm.
# This is an O(n) algorithm where each element is swapped with a randomly chosen element.
# Random shuffling is useful in algorithms such as Quicksort (randomized pivot) and in Monte Carlo simulations.
data_list = [1, 2, 3, 4, 5]
random.shuffle(data_list)
print(f"Shuffled list: {data_list}")

# Runtime Analysis:
# - Time Complexity: O(n), where n is the length of the list.
# - Space Complexity: O(1), shuffling is done in-place, meaning no extra space is used beyond the input list.
# Best Case: O(n), always linear as we must shuffle all elements regardless of their initial order.
# Worst Case: O(n), same as best case since all elements must be processed.

# Use Case:
# Shuffling can be used in card games, sampling from datasets, or when randomized input is needed 
# to ensure that no specific order is assumed. For example, ensuring fair random ordering in lottery systems.

# Consideration:
# If the data set is extremely large and memory becomes a constraint, 
# shuffling large data may incur performance issues, and memory-efficient techniques should be used.


# Subtopic: Randomized Selection (Reservoir Sampling)
#-----------------------------------------------------------
# Reservoir sampling is used to randomly select 'k' elements from a large dataset/stream
# of unknown or large size, where storing all the elements is infeasible.
# Example: selecting 3 random elements from a list of 100 elements
# This algorithm ensures that every element in the dataset has an equal probability of being chosen.
k = 3
dataset = list(range(1, 101))  # A dataset of 100 elements
reservoir = []

# Select the first 'k' elements directly to initialize the reservoir
for i in range(k):
    reservoir.append(dataset[i])

# Now replace elements in the reservoir with probability based on their position
for i in range(k, len(dataset)):
    j = random.randint(0, i)
    if j < k:
        reservoir[j] = dataset[i]

print(f"Randomly selected elements (Reservoir Sampling): {reservoir}")

# Runtime Analysis:
# - Time Complexity: O(n), where n is the size of the dataset, as we must process each element once.
# - Space Complexity: O(k), since we only store the reservoir of size 'k' irrespective of the size of the dataset.
# Best Case: O(n), always linear since each element must be seen and considered.
# Worst Case: O(n), the entire dataset is processed once, but only 'k' elements are stored.

# Use Case:
# Reservoir sampling is widely used in scenarios where streaming data needs to be sampled,
# such as monitoring logs in real-time, large dataset sampling for surveys, or maintaining a randomized 
# subset of data for machine learning when the dataset cannot fit in memory.

# Consideration:
# The probability of selecting elements is crucial and must be uniform.
# Failing to update the reservoir correctly will result in skewed selections, which can negatively affect results.


# Subtopic: Randomized Pivot Selection in QuickSort
#-----------------------------------------------------------
# Randomized QuickSort is an optimized version of the classical QuickSort algorithm.
# In standard QuickSort, the pivot selection (if consistently poor) can lead to O(n^2) time complexity.
# By selecting a random pivot, the likelihood of encountering worst-case performance is significantly reduced,
# bringing the expected time complexity closer to O(n log n).

data_list = [10, 7, 8, 9, 1, 5]
pivot = random.choice(data_list)  # Randomly choosing a pivot for partitioning
print(f"Randomly chosen pivot for QuickSort: {pivot}")

# Runtime Analysis for QuickSort with random pivot:
# - Best Case: O(n log n), occurs when the pivot consistently divides the array into two equal halves.
# - Worst Case: O(n^2), although the randomized pivot reduces the probability of this happening.
# - Expected Case: O(n log n), due to random pivot selection, the expected case is typically close to the best case.
# Space Complexity: O(log n) due to recursion stack.

# Use Case:
# Randomized QuickSort is often preferred over the standard deterministic version, particularly 
# in scenarios where performance consistency is crucial. Examples include sorting in competitive programming, 
# large-scale sorting in distributed systems, or backend services where the dataset's characteristics 
# are unknown or vary widely.

# Consideration:
# Randomized algorithms, while efficient on average, may still encounter worst-case scenarios.
# To mitigate this in QuickSort, techniques like tail recursion optimization or switching to 
# a non-recursive sorting algorithm like insertion sort for small datasets can be used.

#=================================================================================
# Algorithms, Miscellaneous Algorithms, Randomized Algorithms, Randomized Quick Sort
#=================================================================================

# Randomized Quick Sort Explanation:
# Quick Sort is a divide-and-conquer sorting algorithm that partitions an array around a pivot element, 
# sorting smaller sub-arrays recursively. Randomized Quick Sort adds randomness to the pivot selection 
# to minimize the chances of encountering the worst-case scenario, improving performance on average.
# The key idea is to randomly select a pivot, reducing the probability of consistently picking a bad pivot.

# Example Scenario:
# Given an unsorted array, the algorithm will sort it by choosing a random pivot in each recursive step.

# Subtopic: Initial unsorted array
array = [3, 6, 8, 10, 1, 2, 1]

# The print statement shows the unsorted array before applying randomized quick sort.
# This allows us to visually verify the effect of the algorithm after sorting.
print(f"Unsorted array: {array}")

# Subtopic: Random pivot selection insight
# Instead of choosing the first or last element as a pivot, we randomly select a pivot.
# This reduces the likelihood of consistently encountering the worst-case time complexity, O(n^2),
# which occurs when the pivot consistently partitions poorly (e.g., selecting min or max).
import random

# Randomly selecting a pivot index
pivot_index = random.randint(0, len(array) - 1)

# This pivot is used to partition the array into two parts.
pivot = array[pivot_index]

# Sub-subtopic: Partitioning insight
# Partitioning divides the array into two sub-arrays:
# - Elements less than the pivot on one side
# - Elements greater than the pivot on the other side
# After partitioning, the pivot is placed in its final sorted position.
left_partition = [x for x in array if x < pivot]
right_partition = [x for x in array if x > pivot]

# The elements equal to the pivot are included in the middle, and the array is printed to show partitioning results.
print(f"Pivot selected: {pivot}")
print(f"Left partition: {left_partition}")
print(f"Right partition: {right_partition}")

# Sub-subtopic: Recursive quick sort insight
# Randomized Quick Sort recursively sorts the left and right partitions.
# The base case for recursion occurs when the array contains 1 or 0 elements, in which case it is already sorted.

# Final sorted array after combining sorted partitions with the pivot
sorted_array = left_partition + [pivot] + right_partition
print(f"Partially sorted array after 1st partition: {sorted_array}")

# Use Case 1: Sorting large, unsorted arrays efficiently
# Randomized quick sort is useful for large datasets where deterministic quick sort might be prone to worst-case behavior.

# Use Case 2: Sorting nearly sorted arrays
# Randomized quick sort still performs well even if the input is partially sorted, unlike some algorithms (e.g., bubble sort).

# Pitfalls and Considerations:
# - Randomized quick sort is in-place but not stable, meaning that the relative order of equal elements is not preserved.
# - Although randomized quick sort typically runs in O(n log n) time, the worst case is O(n^2), 
#   which happens if the random pivot selection consistently divides the array unevenly.

# Runtime Analysis:
# - Time Complexity: 
#   - Best Case: O(n log n), when the pivot divides the array into two roughly equal halves at each step.
#   - Average Case: O(n log n), since the randomized pivot reduces the chance of consistently poor partitions.
#   - Worst Case: O(n^2), if the pivot consistently results in highly unbalanced partitions (e.g., always choosing min or max).
# - Space Complexity: O(log n) for the recursion stack in the best/average case, and O(n) in the worst case due to recursion depth.

# Consideration: In practice, randomized quick sort is one of the fastest sorting algorithms for large datasets, 
# outperforming algorithms like merge sort due to smaller constant factors and in-place partitioning.

#=================================================================================
# Algorithms, Miscellaneous Algorithms, Randomized Algorithms, Monte Carlo Methods
#=================================================================================

# Topic: Estimating the value of Pi using a Monte Carlo Method
#-----------------------------------------------------------
# Monte Carlo methods rely on randomness to obtain numerical results. Here, we will estimate the value of Pi.
# The concept is based on randomly generating points inside a square and counting how many fall inside the inscribed circle.
# The ratio of the points inside the circle to the total points can be used to estimate Pi.

# Subtopic: High-level explanation of the approach
#-----------------------------------------------------------
# 1. We generate random points (x, y) inside a unit square where both x and y range from 0 to 1.
# 2. If the distance of the point from the origin (0, 0) is less than or equal to 1, it lies inside the quarter circle.
# 3. The ratio of points inside the quarter circle to total points is approximately π/4.
# 4. Multiplying this ratio by 4 gives an estimate of Pi.

# Importing required libraries for random number generation
import random

# Total number of points to generate. The larger the number of points, the more accurate the estimate.
total_points = 10000
inside_circle = 0  # Counter for points that fall inside the quarter circle

# Subtopic: Iterating through points and calculating their distance from the origin
#-----------------------------------------------------------
# For each point, we generate random x, y coordinates between 0 and 1.
# If the point lies within the circle (i.e., x^2 + y^2 <= 1), we increment the 'inside_circle' counter.

for _ in range(total_points):
    x = random.random()  # Generate random x-coordinate
    y = random.random()  # Generate random y-coordinate
    
    # Check if the point lies inside the quarter circle by calculating its Euclidean distance from the origin
    if x**2 + y**2 <= 1:
        inside_circle += 1  # Increment if inside the circle

# Subtopic: Calculating Pi using the ratio of points
#-----------------------------------------------------------
# The ratio of points inside the circle to the total points is approximately equal to π/4.
# To get the estimate of Pi, multiply the ratio by 4.
pi_estimate = 4 * inside_circle / total_points

print(f"Estimated value of Pi after {total_points} iterations is: {pi_estimate}")

# Runtime Analysis:
# - Time Complexity: O(n), where 'n' is the number of points generated (total_points).
#   Each iteration takes constant time to generate a point and check if it lies inside the circle.
# - Space Complexity: O(1), since we are using only a few variables (total_points, inside_circle, etc.).
# Best Case: O(n), the method always requires iterating through all points.
# Worst Case: O(n), similar to the best case, we have a fixed number of iterations and no early exit points.

# Use case:
# Monte Carlo methods, like this one, are highly useful when an analytical solution is complex or unknown.
# They can be applied to problems in computational physics, finance (for option pricing), and integration where deterministic methods are infeasible.

# Considerations:
# 1. Accuracy: The accuracy of the Pi estimation increases as the number of points increases. 
#    However, increasing the points significantly may lead to diminishing returns due to the probabilistic nature of the algorithm.
# 2. Random Number Generation: The quality of the random number generator affects the result. 
#    In some applications, using pseudo-random generators may introduce bias.
# 3. Parallelization: Monte Carlo simulations can be parallelized easily since each point calculation is independent.
#    This allows for better performance in distributed systems or using multi-threading.

# Pitfalls:
# - Precision limitations: For very large numbers of points, floating-point precision can affect the outcome, especially in languages with fixed-precision arithmetic.
# - Randomness source: The randomness source should be carefully chosen, as poor random number generation could skew results, especially for smaller iterations.

# Uncommon insight:
# - This Monte Carlo simulation can be extended to higher dimensions. In such cases, the value of Pi can be generalized to estimate the volume of a hypersphere,
#   with the dimensionality affecting the number of points required for accurate estimations.

# Subtopic: Edge cases
#-----------------------------------------------------------
# - If 'total_points' is 0, the algorithm would result in a division by zero. 
#   Ensure 'total_points' is a positive integer before executing the simulation.
# - Very low values for 'total_points' (e.g., 1 or 2) result in a poor estimate due to inadequate sampling.
#   A practical lower bound should be used based on the desired precision of Pi.



#=================================================================================
# Algorithms, Miscellaneous Algorithms, Network Flow Algorithms
#=================================================================================

# Topic: Basic Breadth-First Search (BFS) Algorithm in a Graph
#-----------------------------------------------------------
# BFS is a fundamental graph traversal algorithm used to explore all nodes level by level.
# It's widely used in network flow problems like finding the shortest path in unweighted graphs, 
# or for finding augmenting paths in flow networks (e.g., Ford-Fulkerson algorithm).

# Consider an example graph represented as an adjacency list.
# Adjacency list stores each node's neighbors.
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Start node for BFS traversal
start_node = 0

# Initialize the queue with the start node, typically for BFS
# The queue data structure is optimal for BFS since it ensures that nodes are processed in the order they are discovered.
queue = [start_node]

# Visited set keeps track of nodes that have been explored to avoid processing the same node multiple times.
visited = set([start_node])

print("BFS Traversal Order:")

# BFS algorithm, processes nodes level by level.
# While there are nodes in the queue to process:
while queue:
    # Pop the first node in the queue (FIFO order)
    node = queue.pop(0)  # O(1) for popping from the front
    print(node)  # Print the node as it is visited
    
    # Process all unvisited neighbors of the current node
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)  # Mark the neighbor as visited to avoid reprocessing
            queue.append(neighbor)  # Add the neighbor to the queue to explore it next

# Runtime Analysis:
# - Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges.
#   This is because every node and every edge is processed once.
# - Space Complexity: O(V), because we use additional space to store the visited set and the queue.
# Best Case: O(V + E), happens when every node and edge is connected and traversed.
# Worst Case: O(V + E), same as the best case since all nodes and edges must be traversed.
# Special Case: In sparse graphs (few edges), E is close to V, so complexity is closer to O(V).

# Use case:
# BFS is optimal when you need to find the shortest path in an unweighted graph or when all edge weights are uniform.
# This method is often used in network flow problems like Edmonds-Karp (an implementation of Ford-Fulkerson) for finding augmenting paths.

# Consideration:
# In real-world scenarios like network flow algorithms, BFS is used to find augmenting paths in residual graphs.
# This algorithm guarantees the shortest path in terms of number of edges in unweighted graphs, which is crucial in scenarios like data packet routing.

# Pitfall:
# One possible pitfall is not properly managing visited nodes, which can lead to infinite loops in cyclic graphs. 
# Always ensure you check if a node is visited before enqueuing it.
# Also, using a list for the queue (as in this case) may lead to performance issues if the graph is very large due to the O(n) time complexity of popping from the front. 
# In those cases, using a deque (double-ended queue) is a better choice, as it supports O(1) popleft operations.

# Improvement:
# For larger graphs, we could use collections.deque() instead of a list to reduce the time complexity of popping from the front, as list pop(0) is O(n) in Python.
# An optimization like this can be especially important in large-scale applications such as social network analysis or large-scale recommendation systems where performance is critical.


#=================================================================================
# Algorithms, Miscellaneous Algorithms, Network Flow Algorithms
#=================================================================================
# Subtopic: Ford-Fulkerson Method for Maximum Flow
#-----------------------------------------------------------
# The Ford-Fulkerson method is a greedy algorithm used to compute the maximum flow in a flow network.
# The idea is to find augmenting paths from the source to the sink and increase the flow along these paths.
# It uses the concept of residual capacity, which is the remaining capacity of the edge after accounting for flow.
# The algorithm iterates until no more augmenting paths can be found.

# Example: Simulating a flow network with a small, simple graph.
# Assume we have a graph represented as an adjacency matrix (2D array), where each value represents
# the capacity of an edge between two nodes.

# Graph structure:
# Node 0: Source
# Node 1, 2: Intermediate nodes
# Node 3: Sink
# Capacity matrix where graph[i][j] represents the capacity from node i to node j.

graph = [
    [0, 16, 13, 0],  # Source (0) to others
    [0, 0, 10, 12],  # Intermediate node 1
    [0, 4, 0, 14],   # Intermediate node 2
    [0, 0, 0, 0]     # Sink (3)
]

# To keep things simple, let's print the graph structure to understand the capacities:
print("Capacity Matrix:")
for row in graph:
    print(row)

# Runtime Analysis (High Level):
#-----------------------------------------------------------
# - Time Complexity: O(max_flow * E), where E is the number of edges in the graph.
#   Each time an augmenting path is found, the flow is increased, and the process continues.
#   Finding paths takes O(E) using DFS or BFS, but the number of iterations depends on the total maximum flow.
#   In practice, this can lead to long runtimes if the flow values are large.
# - Space Complexity: O(V^2), where V is the number of vertices.
#   The adjacency matrix representation requires V^2 space to store capacities between each pair of nodes.

# Subtopic: Path Augmentation Concept
#-----------------------------------------------------------
# The Ford-Fulkerson method repeatedly searches for an augmenting path in the residual graph.
# If such a path is found, flow is added along this path.
# The residual graph is updated by reducing the capacity of forward edges and increasing the capacity of reverse edges.

# Example: Printing an augmenting path (This is purely illustrative)
# Augmenting path found: 0 -> 1 -> 3 with capacity 12
print("Augmenting path: 0 -> 1 -> 3, Flow: 12")

# In a real implementation, we'd now update the residual graph to reflect the new flow.
# This would involve reducing the capacities along the forward edges and increasing capacities along the reverse edges.

# Potential Pitfalls and Considerations:
#-----------------------------------------------------------
# 1. Floating-Point Precision: In some implementations where capacities are non-integer values,
#    floating-point precision issues could arise, especially when computing the residual graph.
#    To avoid such pitfalls, it's better to work with integers or handle precision issues carefully.
# 2. Infinite Loops: The algorithm assumes augmenting paths will eventually be blocked.
#    If care is not taken in choosing augmenting paths (e.g., if paths with very small capacities are selected repeatedly),
#    the algorithm may not converge efficiently.
# 3. Scalability: For very large graphs or networks, Ford-Fulkerson may not scale efficiently. More advanced algorithms
#    like the Edmonds-Karp algorithm (which is an implementation of Ford-Fulkerson using BFS) can guarantee better performance.

# Subtopic: Use Cases for Ford-Fulkerson
#-----------------------------------------------------------
# The Ford-Fulkerson method is used in various practical scenarios:
# 1. **Network Design**: Determining the maximum capacity of a network for data flow or transportation.
# 2. **Bipartite Matching**: Finding maximum matching in bipartite graphs, where nodes can be divided into two distinct sets.
# 3. **Project Management**: Analyzing workflow bottlenecks in process management by calculating the maximum capacity of tasks between stages.
# 4. **Sports Scheduling**: Used in algorithms that determine feasible match schedules based on the number of resources (teams, fields, etc.).

# Best Case: O(E) where the graph has a single augmenting path with the maximum capacity. The algorithm terminates early as no more paths can be found.
# Worst Case: O(max_flow * E) where each iteration increases the flow minimally, causing many iterations.


#=================================================================================
# Algorithms, Miscellaneous Algorithms, Network Flow Algorithms, Edmonds-Karp Algorithm
#=================================================================================

# The Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network.
# It uses a breadth-first search (BFS) to find augmenting paths and runs in O(V * E^2) time, where V is the number of vertices and E is the number of edges.
# The algorithm repeatedly finds the shortest augmenting path in terms of the number of edges, ensuring that each iteration is efficient.

#-----------------------------------------------------------
# Topic: Breadth-First Search (BFS) for finding augmenting paths
#-----------------------------------------------------------

# The BFS is used to find the shortest augmenting path (in terms of the number of edges) from the source to the sink in the flow network.
# An augmenting path is a path from the source to the sink where every edge has available capacity > 0.

# Example: Representing a flow network as a capacity matrix.
# In the matrix, rows represent source nodes, and columns represent target nodes. The value at matrix[i][j] represents the capacity of the edge from node i to node j.
capacity = [
    [0, 16, 13, 0, 0, 0],  # Node 0: edges to other nodes with their capacities.
    [0, 0, 10, 12, 0, 0],  # Node 1: edges to other nodes with their capacities.
    [0, 4, 0, 0, 14, 0],   # Node 2: edges to other nodes with their capacities.
    [0, 0, 9, 0, 0, 20],   # Node 3: edges to other nodes with their capacities.
    [0, 0, 0, 7, 0, 4],    # Node 4: edges to other nodes with their capacities.
    [0, 0, 0, 0, 0, 0]     # Node 5: Sink node, no outgoing edges.
]

# We start by printing the capacity matrix, which is crucial for understanding the initial state of the flow network.
print("Initial capacity matrix:")
for row in capacity:
    print(row)

# Key Insight: 
# Each row represents a node, and each value in the row represents the capacity of an edge from the node (row) to another node (column).
# The matrix is an adjacency matrix of a directed graph, where non-zero values indicate directed edges and their capacities.

#-----------------------------------------------------------
# Topic: Pathfinding with BFS in the network
#-----------------------------------------------------------
# We use BFS to explore the network and find an augmenting path from the source (node 0) to the sink (node 5).
# An augmenting path is found if we can traverse from the source to the sink while respecting capacity constraints (i.e., non-zero capacity).
# BFS ensures we explore the shortest path in terms of edge count, which minimizes the number of edges involved in each augmenting path.
# The goal is to maximize flow by pushing flow through these paths iteratively.

from collections import deque  # We use a deque to efficiently implement the BFS queue.

# BFS to find if there's an augmenting path and to store the parent of each node.
def bfs(source, sink, parent):
    visited = [False] * len(capacity)  # Track which nodes have been visited.
    queue = deque([source])  # Initialize the BFS queue with the source node.
    visited[source] = True  # Mark the source node as visited.

    while queue:
        u = queue.popleft()  # Get the next node to explore.

        # Explore all nodes adjacent to 'u' (i.e., all edges from 'u' with non-zero capacity).
        for v, cap in enumerate(capacity[u]):
            # If the node 'v' is unvisited and the capacity from 'u' to 'v' is greater than 0
            if not visited[v] and cap > 0:
                queue.append(v)  # Add 'v' to the queue for further exploration.
                visited[v] = True  # Mark 'v' as visited.
                parent[v] = u  # Store the path (the parent of 'v' is 'u').

                # If we reach the sink node, we've found an augmenting path.
                if v == sink:
                    return True  # An augmenting path exists.

    return False  # No augmenting path exists, which means we cannot push more flow.

#-----------------------------------------------------------
# Topic: Augmenting flow in the network
#-----------------------------------------------------------
# Once an augmenting path is found, we calculate the maximum flow that can be pushed along this path.
# The flow pushed is the minimum capacity of any edge in the path (i.e., the bottleneck capacity).

source = 0  # Source node
sink = 5    # Sink node
parent = [-1] * len(capacity)  # Array to store the parent of each node during BFS, initialized with -1.

max_flow = 0  # Initialize the maximum flow in the network to 0.

# We repeatedly search for augmenting paths using BFS and push flow through them.
while bfs(source, sink, parent):
    path_flow = float('Inf')  # Start with an infinite flow.

    # Find the minimum capacity in the augmenting path.
    s = sink
    while s != source:
        path_flow = min(path_flow, capacity[parent[s]][s])
        s = parent[s]  # Move to the previous node in the path.

    # Update the capacities of the edges in the augmenting path.
    v = sink
    while v != source:
        u = parent[v]
        capacity[u][v] -= path_flow  # Decrease the capacity of the forward edge.
        capacity[v][u] += path_flow  # Increase the capacity of the reverse edge (for residual graph).
        v = parent[v]  # Move to the previous node in the path.

    max_flow += path_flow  # Add the path flow to the total flow.
    print(f"Augmenting path found with flow: {path_flow}")
    print("Updated capacity matrix:")
    for row in capacity:
        print(row)

print(f"The maximum possible flow is: {max_flow}")

# Runtime Analysis of Edmonds-Karp Algorithm:
# - Time Complexity: O(V * E^2), where V is the number of vertices and E is the number of edges.
#   This complexity arises from the O(E) BFS search and the fact that each edge can be part of at most O(V) augmenting paths.
# - Space Complexity: O(V^2), due to the capacity matrix that stores edge capacities between all pairs of nodes.

# Best Case:
# The best case occurs when the network is structured such that few augmenting paths are required (e.g., very high initial capacities). This minimizes the number of iterations.

# Worst Case:
# The worst case happens in dense networks with many nodes and low capacities, where BFS must traverse many paths and adjust the capacity matrix often.

# Key Considerations:
# 1. Capacity constraints: Real-world networks may involve dynamic or changing capacities, requiring careful tracking.
# 2. Integer overflow: Large flows can cause overflow in languages without arbitrary precision integers.
# 3. Flow reversal: After augmenting, reverse edges may take on flow, effectively undoing part of the original path if needed in future iterations.
# 4. Edge cases: Networks with disconnected components, zero-capacity edges, or circular dependencies should be handled gracefully.
