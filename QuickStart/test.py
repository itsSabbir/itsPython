# Modifying the structure to avoid slashes in folder/file names
# Replacing slashes with dashes to avoid FileNotFoundError
import os

structure = {
    "Data Structures": {
        "1. Basic Data Structures": [
            "Arrays", "Linked Lists",
            "Singly Linked List", "Doubly Linked List", "Circular Linked List",
            "Stacks", "Queues", "Simple Queue", "Circular Queue", "Priority Queue", "Deque (Double-ended Queue)"
        ],
        "2. Hash-based Structures": [
            "Hash Table", "Hash Set", "Hash Map (Dictionary)"
        ],
        "3. Tree Structures": [
            "Binary Tree", "Binary Search Tree (BST)", "AVL Tree", "Red-Black Tree",
            "Segment Tree", "Fenwick Tree (Binary Indexed Tree)", "B-Trees", "N-ary Tree", "Trie (Prefix Tree)"
        ],
        "4. Graph Structures": [
            "Adjacency Matrix", "Adjacency List", "Incidence Matrix"
        ],
        "5. Specialized Data Structures": [
            "Heap", "Min-Heap", "Max-Heap", "Disjoint Set (Union-Find)", "Bloom Filter", "Skip List",
            "Suffix Tree", "Suffix Array", "K-D Tree", "Quad Tree", "Octree"
        ],
        "6. Dynamic Programming Structures": [
            "Memoization Table", "Dynamic Array"
        ],
        "7. String Structures": [
            "Rope", "Suffix Tree", "Suffix Array"
        ]
    },
    "Algorithms": {
        "1. Sorting Algorithms": [
            "Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort",
            "Counting Sort", "Radix Sort", "Bucket Sort", "Shell Sort", "Tim Sort"
        ],
        "2. Searching Algorithms": [
            "Linear Search", "Binary Search", "Ternary Search", "Jump Search", "Interpolation Search", "Exponential Search"
        ],
        "3. Graph Algorithms": [
            "Traversal Algorithms", "Depth-First Search (DFS)", "Breadth-First Search (BFS)",
            "Shortest Path Algorithms", "Dijkstra’s Algorithm", "Bellman-Ford Algorithm", "Floyd-Warshall Algorithm",
            "Minimum Spanning Tree Algorithms", "Prim’s Algorithm", "Kruskal’s Algorithm",
            "Topological Sorting", "Graph Cycle Detection", "Strongly Connected Components (Kosaraju’s Algorithm, Tarjan’s Algorithm)",
            "Eulerian Path-Circuit", "Hamiltonian Path-Circuit"
        ],
        "4. Dynamic Programming Algorithms": [
            "Fibonacci Sequence", "Knapsack Problem", "0-1 Knapsack", "Fractional Knapsack",
            "Longest Common Subsequence", "Longest Increasing Subsequence", "Edit Distance", "Coin Change Problem",
            "Matrix Chain Multiplication", "Subset Sum Problem"
        ],
        "5. Backtracking Algorithms": [
            "N-Queens Problem", "Sudoku Solver", "Subset Generation", "Permutations and Combinations", "Rat in a Maze Problem"
        ],
        "6. Greedy Algorithms": [
            "Activity Selection Problem", "Huffman Coding", "Kruskal’s Algorithm", "Prim’s Algorithm", "Fractional Knapsack Problem"
        ],
        "7. Mathematical Algorithms": [
            "Greatest Common Divisor (GCD)", "Prime Number Algorithms (Sieve of Eratosthenes)",
            "Fermat’s Little Theorem", "Fast Exponentiation", "Matrix Exponentiation"
        ],
        "8. String Algorithms": [
            "String Matching Algorithms", "Knuth-Morris-Pratt (KMP) Algorithm", "Rabin-Karp Algorithm", "Boyer-Moore Algorithm",
            "Longest Palindromic Substring", "Anagram Checking", "Substring Search Algorithms"
        ],
        "9. Miscellaneous Algorithms": [
            "Randomized Algorithms", "Randomized Quick Sort", "Monte Carlo Methods",
            "Network Flow Algorithms", "Ford-Fulkerson Method", "Edmonds-Karp Algorithm"
        ]
    }
}

# Function to create folders and files based on the structure
def create_folders_and_files(base_dir, structure):
    for main_topic, subtopics in structure.items():
        # Create main topic folder
        main_topic_path = os.path.join(base_dir, main_topic)
        os.makedirs(main_topic_path, exist_ok=True)
        
        # Loop through subtopics
        for subtopic, items in subtopics.items():
            # Create subtopic folder
            subtopic_path = os.path.join(main_topic_path, subtopic)
            os.makedirs(subtopic_path, exist_ok=True)
            
            # Create individual files for each item
            for item in items:
                file_path = os.path.join(subtopic_path, f"{item}.py")
                with open(file_path, 'w') as file:
                    file.write(f"# {item}\n\n")
                    file.write(f"This file contains information about {item}.\n")

# Create folders and files in the current directory
create_folders_and_files(".", structure)
