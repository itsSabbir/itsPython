#===============================================================================
# Algorithms, Sorting Algorithms, Bubble Sort
#===============================================================================

"""
In this section, we explore sorting algorithms, specifically the Bubble Sort algorithm.
Sorting algorithms are foundational for efficient data organization, enhancing performance
in both searching and other data manipulation tasks.
Bubble Sort, while simple and easy to implement, has significant limitations in terms of performance
when dealing with larger datasets, making it an educational example or suitable only for small datasets.

### Bubble Sort Algorithm Overview:
- Bubble Sort works by repeatedly traversing the list, comparing adjacent elements, 
  and swapping them if they are out of order. This process continues until no swaps are necessary,
  meaning the list is sorted.
- The name "Bubble Sort" comes from the smaller elements "bubbling" to the top of the list as the process repeats.

### Time Complexity:
- **Best Case**: O(n) - When the list is already sorted, the algorithm only needs to traverse the list once.
  This is an uncommon case and can only be achieved with the optimized version of Bubble Sort that includes
  the 'swapped' flag to detect an early exit.
- **Average Case**: O(n^2) - In a typical random list, each element needs to be compared with others,
  leading to a quadratic number of comparisons and swaps.
- **Worst Case**: O(n^2) - The worst case occurs when the list is sorted in reverse order, 
  requiring the maximum number of swaps and passes through the list.

### Space Complexity:
- **O(1)** - Bubble Sort is an in-place sorting algorithm, meaning it does not require extra space 
  proportional to the input size. Only a few auxiliary variables (like 'swapped') are needed.

### Stability:
- Bubble Sort is stable, meaning that if two elements have the same value, they will remain 
  in the same relative positions after sorting. This is an important feature in cases where 
  the relative order of equal elements is significant (e.g., sorting by secondary criteria).

### Example of Bubble Sort Implementation
"""

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

"""
### Detailed Insights:

1. **The outer loop**: It iterates n times, where n is the number of elements in the list.
   In each pass, the largest unsorted element is placed in its correct position, so 
   after i passes, the last i elements are already sorted.

2. **The inner loop**: This compares adjacent elements and swaps them if the previous element is greater
   than the next. After each complete pass of the inner loop, the largest element moves to the end.

3. **Early termination**: The 'swapped' flag ensures that if a pass doesn't swap any elements,
   the algorithm terminates early, reducing the number of unnecessary comparisons.
   This makes the best-case time complexity O(n), when the array is already sorted.

### Advanced Tips:
- Bubble Sort is inefficient for large datasets due to its O(n^2) time complexity in the average and worst cases.
  For performance-critical applications, use more advanced algorithms like Quick Sort (O(n log n) on average) 
  or Merge Sort (O(n log n) guaranteed).
- Bubble Sort is, however, easy to implement and can be useful for small or nearly sorted datasets 
  where simplicity is a priority.
- It is also useful in scenarios where stability is a requirement and the dataset is small enough 
  to make performance less of an issue.

### Use Cases:
- **Educational Tool**: Bubble Sort is often used to introduce the concept of sorting algorithms because
  it is easy to understand and visualize.
- **Small Datasets**: It can be used in cases where the dataset is small (e.g., less than 100 elements) 
  and performance isn't critical.
- **Stable Sorting**: In cases where maintaining the relative order of equal elements is important (like 
  sorting by multiple criteria), Bubble Sort can be used since it is a stable sorting algorithm.

### Runtime Analysis:
- **Best Case (O(n))**: The algorithm stops early when the list is already sorted (thanks to the swapped flag).
- **Average and Worst Case (O(n^2))**: In these cases, each element must be compared with nearly all other elements, 
  leading to quadratic time complexity.

### Pitfalls:
- **Performance**: Bubble Sort performs poorly with large datasets. Its quadratic time complexity means
  that for larger arrays, sorting time increases dramatically. 
  For example, sorting an array of 1,000 elements would require up to 1,000,000 comparisons.
- Always use more efficient algorithms like Quick Sort or Python’s built-in Timsort (which is O(n log n))
  for handling larger arrays or more complex real-world data sets.
"""
