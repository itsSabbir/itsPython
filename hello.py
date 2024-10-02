# print("Hello, World!")

from itertools import permutations

def generate_combinations(array, n):
    # Ensure array has enough elements for n-digit combinations
    if len(array) < n:
        print("The array doesn't have enough elements to form n-digit numbers.")
        return
    
    # Generate all unique permutations of length n
    unique_combinations = list(permutations(array, n))
    
    # Print each combination as a single number
    for combination in unique_combinations:
        print("".join(map(str, combination)))
'[]'
# Example usage
array = [1, 8, 3, 4]  # Your array of numbers
n = 4  # Length of combinations you want

generate_combinations(array, n)

