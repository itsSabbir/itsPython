# Algorithms in Python - Graph Algorithms - in the Python Programming Language
# ============================================================================

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
from typing import Dict, List, Tuple, Set, Optional
from collections import deque, defaultdict
import time
import random

# 1. Overview and Historical Context
# ----------------------------------
# Graph algorithms are a fundamental part of computer science, dealing with the 
# analysis and manipulation of graph structures. These algorithms have roots 
# dating back to the 18th century with Euler's solution to the Seven Bridges of 
# Königsberg problem, widely considered the first theorem in graph theory.

# Key milestones in the development of graph algorithms:
# - 1736: Euler's Seven Bridges of Königsberg solution
# - 1856: Kirchhoff's theorem for counting spanning trees
# - 1930s: Depth-First Search (DFS) formalized by Tarjan
# - 1956: Dijkstra's algorithm for shortest paths
# - 1961: Prim's algorithm for minimum spanning trees
# - 1962: Kruskal's algorithm for minimum spanning trees
# - 1965: Floyd-Warshall algorithm for all-pairs shortest paths

# In Python, graph algorithms have been implemented since the language's early 
# days. The NetworkX library, introduced in 2002, became a cornerstone for 
# graph algorithm implementation and analysis in Python.

# Significance in modern software development:
# - Social network analysis
# - Route planning and navigation systems
# - Optimization problems in logistics and supply chain management
# - Network flow problems in telecommunications and transportation
# - Machine learning applications, especially in graph neural networks

# 2. Syntax, Key Concepts, and Code Examples
# ------------------------------------------

class Graph:
    def __init__(self, directed: bool = False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u: int, v: int, weight: int = 1):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_vertices(self) -> List[int]:
        return list(self.graph.keys())
    
    def get_edges(self) -> List[Tuple[int, int, int]]:
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                if self.directed or u <= v:
                    edges.append((u, v, weight))
        return edges

def dfs_recursive(graph: Graph, start: int, visited: Set[int] = None) -> List[int]:
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor, _ in graph.graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    return result

def bfs(graph: Graph, start: int) -> List[int]:
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(neighbor for neighbor, _ in graph.graph[vertex] if neighbor not in visited)
    return result

def dijkstra(graph: Graph, start: int) -> Dict[int, int]:
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def prim_mst(graph: Graph) -> List[Tuple[int, int, int]]:
    start_vertex = next(iter(graph.graph))
    mst = []
    visited = set([start_vertex])
    edges = [(weight, start_vertex, to) for to, weight in graph.graph[start_vertex]]
    heapq.heapify(edges)
    
    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for next_to, next_weight in graph.graph[to]:
                if next_to not in visited:
                    heapq.heappush(edges, (next_weight, to, next_to))
    
    return mst

def kruskal_mst(graph: Graph) -> List[Tuple[int, int, int]]:
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
    
    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    result = []
    edges = sorted(graph.get_edges(), key=lambda x: x[2])
    parent = {}
    rank = {}
    for vertex in graph.get_vertices():
        parent[vertex] = vertex
        rank[vertex] = 0
    
    for u, v, weight in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append((u, v, weight))
            union(parent, rank, x, y)
    
    return result

def floyd_warshall(graph: Graph) -> Dict[Tuple[int, int], int]:
    vertices = graph.get_vertices()
    dist = {(u, v): float('infinity') for u in vertices for v in vertices}
    
    for u in vertices:
        dist[(u, u)] = 0
        for v, weight in graph.graph[u]:
            dist[(u, v)] = weight
    
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])
    
    return dist

def topological_sort(graph: Graph) -> List[int]:
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor, _ in graph.graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)
    
    visited = {v: False for v in graph.get_vertices()}
    stack = []
    for v in graph.get_vertices():
        if not visited[v]:
            dfs(v, visited, stack)
    return stack[::-1]

def strongly_connected_components(graph: Graph) -> List[List[int]]:
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor, _ in graph.graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)
    
    def transpose():
        g = Graph(directed=True)
        for u in graph.graph:
            for v, weight in graph.graph[u]:
                g.add_edge(v, u, weight)
        return g
    
    def dfs_scc(v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor, _ in g_transposed.graph[v]:
            if not visited[neighbor]:
                dfs_scc(neighbor, visited, component)
    
    stack = []
    visited = {v: False for v in graph.get_vertices()}
    for v in graph.get_vertices():
        if not visited[v]:
            dfs(v, visited, stack)
    
    g_transposed = transpose()
    visited = {v: False for v in graph.get_vertices()}
    scc = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_scc(v, visited, component)
            scc.append(component)
    
    return scc

# 3. Best Practices, Common Pitfalls, and Advanced Tips
# -----------------------------------------------------
# Best Practices:
# 1. Choose the appropriate graph representation (adjacency list vs. matrix) based on the problem and graph density.
# 2. Use efficient data structures like heapq for priority queues in algorithms like Dijkstra's.
# 3. Implement graph algorithms iteratively when possible to avoid stack overflow in large graphs.
# 4. Use type hints to improve code readability and catch potential errors early.
# 5. Properly handle disconnected graphs in your implementations.

# Common Pitfalls:
# 1. Forgetting to handle cycles in directed graphs, leading to infinite loops.
# 2. Not considering negative edge weights in shortest path algorithms.
# 3. Implementing inefficient graph traversals, leading to poor performance on large graphs.
# 4. Neglecting to handle self-loops and multi-edges in graph representations.
# 5. Incorrectly implementing priority queues, affecting the correctness of algorithms like Dijkstra's.

# Advanced Tips:
# 1. Use bit manipulation techniques for faster set operations in graph algorithms.
# 2. Implement iterative deepening for memory-efficient depth-limited search.
# 3. Use dynamic programming techniques to optimize certain graph algorithms.
# 4. Implement parallel processing for graph algorithms on large-scale graphs.
# 5. Utilize graph compression techniques for memory-efficient storage of large graphs.

def iterative_deepening_dfs(graph: Graph, start: int, goal: int) -> Optional[List[int]]:
    def dls(node, depth):
        if depth == 0 and node == goal:
            return [node]
        if depth > 0:
            for neighbor, _ in graph.graph[node]:
                path = dls(neighbor, depth - 1)
                if path:
                    return [node] + path
        return None

    max_depth = len(graph.get_vertices())
    for depth in range(max_depth):
        path = dls(start, depth)
        if path:
            return path
    return None

# 4. Integration and Real-World Applications
# ------------------------------------------
# Graph algorithms are widely used in various domains and applications:

# 1. Social Network Analysis:
#    - Friend recommendation systems
#    - Influencer identification
#    - Community detection

# 2. Transportation and Logistics:
#    - Shortest path algorithms for navigation systems
#    - Network flow algorithms for traffic optimization
#    - Traveling Salesman Problem for route planning

# 3. Bioinformatics:
#    - Protein-protein interaction networks
#    - Gene regulatory networks
#    - Phylogenetic tree construction

# 4. Computer Networks:
#    - Routing protocols (e.g., OSPF using Dijkstra's algorithm)
#    - Network topology analysis
#    - Detecting network vulnerabilities

# 5. Recommendation Systems:
#    - Collaborative filtering using bipartite graphs
#    - Content-based recommendation using similarity graphs

# Real-world example: Social Network Friend Recommendation

class SocialNetwork:
    def __init__(self):
        self.graph = Graph(directed=False)
    
    def add_friendship(self, user1: int, user2: int):
        self.graph.add_edge(user1, user2)
    
    def recommend_friends(self, user: int, max_recommendations: int = 5) -> List[Tuple[int, int]]:
        visited = set([user])
        queue = deque([(user, 0)])
        recommendations = []
        
        while queue and len(recommendations) < max_recommendations:
            current_user, distance = queue.popleft()
            
            if distance > 0:
                recommendations.append((current_user, distance))
            
            for friend, _ in self.graph.graph[current_user]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, distance + 1))
        
        return sorted(recommendations, key=lambda x: (x[1], x[0]))[:max_recommendations]

def demonstrate_social_network():
    social_network = SocialNetwork()
    
    # Add some friendships
    friendships = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6)]
    for u, v in friendships:
        social_network.add_friendship(u, v)
    
    # Get friend recommendations for user 1
    recommendations = social_network.recommend_friends(1)
    print("Friend recommendations for user 1:")
    for user, distance in recommendations:
        print(f"User {user} (distance: {distance})")

# 5. Advanced Concepts and Emerging Trends
# ----------------------------------------
# 1. Graph Neural Networks (GNNs):
#    - Combining graph theory with deep learning for tasks like node classification and link prediction
#    - Applications in recommender systems, drug discovery, and social network analysis

# 2. Streaming Graph Algorithms:
#    - Processing graph data in a streaming fashion for large-scale, dynamic graphs
#    - Applications in real-time social network analysis and fraud detection

# 3. Quantum Graph Algorithms:
#    - Leveraging quantum computing to solve graph problems more efficiently
#    - Potential for exponential speedup in certain graph problems

# 4. Hypergraph Algorithms:
#    - Extending traditional graph algorithms to hypergraphs, where edges can connect multiple vertices
#    - Applications in collaborative filtering and computer vision

# 5. Graph Embedding Techniques:
#    - Representing graph structures in continuous vector spaces
#    - Applications in link prediction, node classification, and graph visualization

# Example: Simple Graph Embedding using Node2Vec-inspired approach

import numpy as np

def simple_node2vec(graph: Graph, dimensions: int = 64, walk_length: int = 10, num_walks: int = 10) -> Dict[int, np.ndarray]:
    def random_walk(start_node):
        walk = [start_node]
        for _ in range(walk_length - 1):
            current = walk[-1]
            neighbors = [v for v, _ in graph.graph[current]]
            if not neighbors:
                break
            walk.append(random.choice(neighbors))
        return walk
    
    walks = []
    for _ in range(num_walks):
        for node in graph.get_vertices():
            walks.append(random_walk(node))
    
    # Simplified word2vec-style training (this is a placeholder and not a real implementation)
    node_embeddings = {node: np.random.rand(dimensions) for node in graph.get_vertices()}
    
    # In a real implementation, you would train the embeddings using the random walks
    # and techniques similar to word2vec (e.g., skip-gram model)
    
    return node_embeddings

# 6. FAQs and Troubleshooting
# ---------------------------

# Q: How do I choose between DFS and BFS for graph traversal?
# A: The choice depends on your specific problem:
#    - Use DFS when you need to explore as far as possible along each branch before backtracking.
#    - Use BFS when you need to find the shortest path in an unweighted graph or explore nodes level by level.

# Q: How can I detect cycles in a graph?
# A: You can use DFS with a recursion stack or color-coding approach:

def has_cycle(graph: Graph) -> bool:
    def dfs_cycle(v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor, _ in graph.graph[v]:
            if not visited[neighbor]:
                if dfs_cycle(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[v] = False
        return False
    
    visited = {v: False for v in graph.get_vertices()}
    rec_stack = {v: False for v in graph.get_vertices()}
    
    for v in graph.get_vertices():
        if not visited[v]:
            if dfs_cycle(v, visited, rec_stack):
                return True
    return False

# Q: How do I handle disconnected components in a graph?
# A: Iterate through all vertices and perform your algorithm on unvisited vertices:

def handle_disconnected_components(graph: Graph, algorithm):
    visited = set()
    results = []
    for v in graph.get_vertices():
        if v not in visited:
            result = algorithm(graph, v)
            results.append(result)
            visited.update(result)
    return results

# Q: How can I improve the performance of Dijkstra's algorithm for sparse graphs?
# A: Use a Fibonacci heap instead of a binary heap for the priority queue:

import fibheap

def dijkstra_fibonacci(graph: Graph, start: int) -> Dict[int, int]:
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    heap = fibheap.makefheap()
    nodes = {}
    for v in graph.get_vertices():
        nodes[v] = fibheap.Node(distances[v], v)
        fibheap.fheappush(heap, nodes[v])
    
    while heap.num_nodes:
        current_distance, current_vertex = fibheap.fheappop(heap)
        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                fibheap.fheapdecrease(heap, nodes[neighbor], distance)
    
    return distances

# Q: How do I handle negative edge weights in shortest path algorithms?
# A: Use the Bellman-Ford algorithm instead of Dijkstra's:

def bellman_ford(graph: Graph, start: int) -> Dict[int, int]:
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    
    for _ in range(len(graph.get_vertices()) - 1):
        for u in graph.get_vertices():
            for v, weight in graph.graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Check for negative-weight cycles
    for u in graph.get_vertices():
        for v, weight in graph.graph[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative-weight cycle")
    
    return distances

# 7. Recommended Tools, Libraries, and Resources
# ----------------------------------------------

# Tools and Libraries:
# 1. NetworkX: Comprehensive library for graph algorithms and analysis
#    pip install networkx

# 2. igraph: High-performance graph library with Python bindings
#    pip install python-igraph

# 3. graph-tool: Efficient graph analysis library (requires compilation)
#    https://graph-tool.skewed.de/

# 4. SNAP (Stanford Network Analysis Platform): Large-scale network analysis
#    https://snap.stanford.edu/snappy/

# 5. PyViz: Visualization tools for graphs and networks
#    pip install pyviz

# Resources:
# 1. "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
# 2. "Algorithm Design" by Kleinberg and Tardos
# 3. "Graph Algorithms in the Language of Linear Algebra" by Kepner and Gilbert
# 4. Stanford's CS161 course on Algorithms: https://stanford-cs161.github.io/winter2021/
# 5. MIT's 6.006 Introduction to Algorithms: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

# Online Resources:
# 1. Graph Algorithms Visualizations: https://visualgo.net/en/graphds
# 2. Codeforces Graph Algorithms Tutorial: https://codeforces.com/blog/entry/16221
# 3. Awesome Graph Classification (GitHub): https://github.com/benedekrozemberczki/awesome-graph-classification

# 8. Performance Analysis and Optimization
# ----------------------------------------

import timeit

def benchmark_algorithm(algorithm, graph: Graph, *args, **kwargs):
    start_time = timeit.default_timer()
    result = algorithm(graph, *args, **kwargs)
    end_time = timeit.default_timer()
    return result, end_time - start_time

def generate_random_graph(num_vertices: int, num_edges: int, directed: bool = False) -> Graph:
    graph = Graph(directed)
    vertices = list(range(num_vertices))
    for _ in range(num_edges):
        u, v = random.sample(vertices, 2)
        weight = random.randint(1, 100)
        graph.add_edge(u, v, weight)
    return graph

def compare_algorithms(algorithms, graph: Graph, *args, **kwargs):
    results = {}
    for name, algorithm in algorithms.items():
        result, time_taken = benchmark_algorithm(algorithm, graph, *args, **kwargs)
        results[name] = (result, time_taken)
    return results

# Example usage:
def demonstrate_performance_analysis():
    graph = generate_random_graph(1000, 5000)
    start_vertex = random.choice(graph.get_vertices())
    
    algorithms = {
        "DFS": dfs_recursive,
        "BFS": bfs,
        "Dijkstra": dijkstra
    }
    
    results = compare_algorithms(algorithms, graph, start_vertex)
    
    print("Performance Analysis:")
    for name, (result, time) in results.items():
        print(f"{name}: {time:.6f} seconds")

# Optimization Strategies:
# 1. Use appropriate data structures (e.g., heapq for priority queues)
# 2. Implement iterative versions of recursive algorithms for large graphs
# 3. Use bit manipulation techniques for set operations
# 4. Employ graph compression techniques for memory efficiency
# 5. Implement parallel processing for large-scale graphs

# Example of optimizing Prim's algorithm using a Fibonacci heap:
def prim_mst_optimized(graph: Graph) -> List[Tuple[int, int, int]]:
    start_vertex = next(iter(graph.graph))
    mst = []
    visited = set()
    heap = fibheap.makefheap()
    nodes = {}
    
    for v in graph.get_vertices():
        if v == start_vertex:
            nodes[v] = fibheap.Node(0, (None, v))
        else:
            nodes[v] = fibheap.Node(float('infinity'), (None, v))
        fibheap.fheappush(heap, nodes[v])
    
    while heap.num_nodes:
        weight, (frm, to) = fibheap.fheappop(heap)
        if to not in visited:
            visited.add(to)
            if frm is not None:
                mst.append((frm, to, weight))
            for neighbor, edge_weight in graph.graph[to]:
                if neighbor not in visited and edge_weight < nodes[neighbor].key:
                    fibheap.fheapdecrease(heap, nodes[neighbor], edge_weight)
                    nodes[neighbor].value = (to, neighbor)
    
    return mst

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

# When adding new sections or expanding existing ones, consider the following:
# - Relevance to the main topic of graph algorithms in Python.
# - Clarity and depth of explanations.
# - Practical applicability of examples and tips.
# - Up-to-date information on Python language features and best practices.

# Your contributions help keep this resource valuable for Python developers at all levels. Thank you for your interest in improving this note sheet!

def main():
    # Demonstrate basic graph operations
    graph = Graph()
    edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 5), (3, 4, 2)]
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    
    print("DFS:", dfs_recursive(graph, 0))
    print("BFS:", bfs(graph, 0))
    print("Dijkstra's shortest paths:", dijkstra(graph, 0))
    print("Prim's MST:", prim_mst(graph))
    print("Kruskal's MST:", kruskal_mst(graph))
    
    # Demonstrate advanced concepts
    print("\nStrongly Connected Components:", strongly_connected_components(graph))
    print("Topological Sort:", topological_sort(graph))
    
    # Demonstrate real-world application
    print("\nSocial Network Friend Recommendation:")
    demonstrate_social_network()
    
    # Demonstrate performance analysis
    print("\nPerformance Analysis:")
    demonstrate_performance_analysis()

if __name__ == "__main__":
    main()