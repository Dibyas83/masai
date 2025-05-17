"""
The generic minimum spanning tree (MST) algorithm is a greedy approach to finding the MST of a connected, undirected graph. It works by iteratively adding "safe" edges to a set until the set forms a spanning tree. A safe edge is one that can be added without creating a cycle and is part of some minimum spanning tree.
Here's a more detailed breakdown:
Initialization: Start with an empty set of edges, A.
Iteration: While A is not a spanning tree (i.e., doesn't connect all vertices):
Find a safe edge: Identify an edge (u, v) that can be added to A without creating a cycle and is part of some minimum spanning tree.
Add the safe edge: Add (u, v) to the set A.
Termination: The algorithm terminates when A becomes a spanning tree (i.e., it connects all vertices with |V|-1 edges, where |V| is the number of vertices).
Return: Return the set A, which now contains the edges of a minimum spanning tree.
Key Concepts:
Loop Invariant: At each step, A is a subset of some minimum spanning tree.
Safe Edge: An edge that can be added to A without violating the loop invariant.
Greedy Approach: The algorithm always tries to add the "best" possible edge at each step (in terms of minimizing the total weight of the MST).
Specific Implementations (e.g., Kruskal's and Prim's algorithms) build upon this generic framework by providing specific strategies for finding "safe" edges:
Kruskal's Algorithm:
Iterates through the sorted edges in non-decreasing order and adds an edge if it connects different connected components (trees).
Prim's Algorithm:
Starts with a single vertex and iteratively grows the MST by adding the lightest edge that connects a vertex in the tree to a vertex outside the tree.

"""
# A Python3 program for
# Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix
# representation of the graph

# Library for INT_MAX
import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print
    # the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.primMST()

"""
Time Complexity: O(V2), As, we are using adjacency matrix, if the input graph is represented using an adjacency list, then the time complexity of Prim’s algorithm can be reduced to O((E+V) * logV) with the help of a binary heap.
Auxiliary Space: O(V)

Optimized Implementation using Adjacency List Representation (of Graph) and Priority Queue
We transform the adjacency matrix into adjacency list using ArrayList<ArrayList<Integer>>. in Java, list of list in Python  
and array of  vectors in C++.
Then we create a Pair class to store the vertex and its weight .
We sort the list on the basis of lowest weight.
We create priority queue and push the first vertex and its weight in the queue
Then we just traverse through its edges and store the least weight in a variable called ans.
At last after all the vertex we return the ans.

"""
import heapq

def tree(V, E, edges):
    # Create an adjacency list representation of the graph
    adj = [[] for _ in range(V)]
    # Fill the adjacency list with edges and their weights
    for i in range(E):
        u, v, wt = edges[i]
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    # Create a priority queue to store edges with their weights
    pq = []
    # Create a visited array to keep track of visited vertices
    visited = [False] * V
    # Variable to store the result (sum of edge weights)
    res = 0
    # Start with vertex 0
    heapq.heappush(pq, (0, 0))
    # Perform Prim's algorithm to find the Minimum Spanning Tree
    while pq:
        wt, u = heapq.heappop(pq)
        if visited[u]:
            continue
            # Skip if the vertex is already visited
        res += wt
        # Add the edge weight to the result
        visited[u] = True
        # Mark the vertex as visited
        # Explore the adjacent vertices
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
                # Add the adjacent edge to the priority queue
    return res
  # Return the sum of edge weights of the Minimum Spanning Tree
if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    # Function call
    print(tree(3, 3, graph))

"""
Time Complexity: O((E+V)*log(V)) where V is the number of vertex and E is the number of edges
Auxiliary Space: O(E+V) where V is the number of vertex and E is the number of edges

Advantages and Disadvantages of Prim’s algorithm
Advantages:

Prim’s algorithm is guaranteed to find the MST in a connected, weighted graph.
It has a time complexity of O((E+V)*log(V)) using a binary heap or Fibonacci heap, where E is the number of edges and V is the number of vertices.
It is a relatively simple algorithm to understand and implement compared to some other MST algorithms.
Disadvantages:

Like Kruskal’s algorithm, Prim’s algorithm can be slow on dense graphs with many edges, as it requires iterating over all edges at least once.
Prim’s algorithm relies on a priority queue, which can take up extra memory and slow down the algorithm on very large graphs.
The choice of starting node can affect the MST output, which may not be desirable in some applications.
Problems based on Minimum Spanning Tree
Kruskal’s Algorithm for MST
Minimum cost to connect all cities
Minimum cost to provide water
Second Best Minimum Spanning Tree
Check if an edge is a part of any MST
Minimize count of connections


"""
import heapq

def prim_mst(graph, start_node):
    mst = []
    visited = set()
    edges = [(0, start_node, start_node)]  # (weight, to, from)
    heapq.heapify(edges)

    while edges:
        weight, to_node, from_node = heapq.heappop(edges)
        if to_node not in visited:
            visited.add(to_node)
            if from_node != to_node: # Avoid adding the initial node's self-loop
                mst.append((from_node, to_node, weight))

            for neighbor, neighbor_weight in graph[to_node].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (neighbor_weight, neighbor, to_node))

    return mst

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 2, 'D': 5},
    'B': {'A': 2, 'C': 6, 'D': 8},
    'C': {'B': 6, 'E': 9},
    'D': {'A': 5, 'B': 8, 'E': 7},
    'E': {'C': 9, 'D': 7}
}

start_node = 'A'
mst = prim_mst(graph, start_node)

print("Minimum Spanning Tree:")
for edge in mst:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")












