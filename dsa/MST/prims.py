"""
The generic minimum spanning tree (MST) algorithm is a greedy approach to finding the MST of a connected,
undirected graph. It works by iteratively adding "safe" edges to a set until the set forms a spanning tree.
 A safe edge is one that can be added without creating a cycle and is part of some minimum spanning tree.
Here's a more detailed breakdown:
Initialization: Start with an empty set of edges, A.
Iteration: While A is not a spanning tree (i.e., doesn't connect all vertices):
Find a safe edge: Identify an edge (u, v) that can be added to A without creating a cycle and is part of some
 minimum spanning tree.
Add the safe edge: Add (u, v) to the set A.
Termination: The algorithm terminates when A becomes a spanning tree (i.e., it connects all vertices with |V|-1
edges, where |V| is the number of vertices).
Return: Return the set A, which now contains the edges of a minimum spanning tree.
Key Concepts:
Loop Invariant: At each step, A is a subset of some minimum spanning tree.
Safe Edge: An edge that can be added to A without violating the loop invariant.
Greedy Approach: The algorithm always tries to add the "best" possible edge at each step (in terms of minimizing
the total weight of the MST).
Specific Implementations (e.g., Kruskal's and Prim's algorithms) build upon this generic framework by providing
specific strategies for finding "safe" edges:
Kruskal's Algorithm:
Iterates through the sorted edges in non-decreasing order and adds an edge if it connects different connected
components (trees).
-------------------------------------------
Prim's Algorithm:
Starts with a single vertex and iteratively grows the MST by adding the lightest edge that connects a vertex in
the tree to a vertex outside the tree.

Prim’s Algorithm for Minimum Spanning Tree (MST)

Prim’s algorithm is a Greedy algorithm like Kruskal's algorithm. This algorithm always starts with a single node and moves through several adjacent nodes, in order to explore all of the connected edges along the way.

The algorithm starts with an empty spanning tree.
The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST, and the other set contains the vertices not yet included.
At every step, it considers all the edges that connect the two sets and picks the minimum weight edge from these edges. After picking the edge, it moves the other endpoint of the edge to the set containing MST.
A group of edges that connects two sets of vertices in a graph is called Articulation Points (or Cut Vertices) in graph theory. So, at every step of Prim’s algorithm, find a cut, pick the minimum weight edge from the cut, and include this vertex in MST Set (the set that contains already included vertices).

Working of the Prim's Algorithm
Step 1: Determine an arbitrary vertex as the starting vertex of the MST. We pick 0 in the below diagram.
Step 2: Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
Step 3: Find edges connecting any tree vertex with the fringe vertices.
Step 4: Find the minimum among these edges.
Step 5: Add the chosen edge to the MST. Since we consider only the edges that connect fringe vertices with the rest, we never get a cycle.
Step 6: Return the MST and exit

Prims-Algorithm-1.webpPrims-Algorithm-1.webp


How to implement Prim's Algorithm?
Follow the given steps to utilize the Prim's Algorithm mentioned above for finding MST of a graph:

Create a set mstSet that keeps track of vertices already included in MST.
Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign the key value as 0 for the first vertex so that it is picked first.
While mstSet doesn't include all vertices
Pick a vertex u that is not there in mstSet and has a minimum key value.
Include u in the mstSet.
Update the key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices. For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value as the weight of u-v.
The idea of using key values is to pick the minimum weight edge from the cut. The key values are used only for vertices that are not yet included in MST, the key value for these vertices indicates the minimum weight edges connecting them to the set of vertices included in MST.

Below is the implementation of the approach:

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
Time Complexity: O(V2), As, we are using adjacency matrix, if the input graph is represented using an adjacency 
list, then the time complexity of Prim’s algorithm can be reduced to O((E+V) * logV) with the help of 
a binary heap.
Auxiliary Space: O(V)

Optimized Implementation using Adjacency List Representation (of Graph) and Priority Queue
We transform the adjacency matrix into adjacency list using ArrayList<ArrayList<Integer>>. in Java, list of list 
in Python  
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
It has a time complexity of O((E+V)*log(V)) using a binary heap or Fibonacci heap, where E is the number of edges
 and V is the number of vertices.
It is a relatively simple algorithm to understand and implement compared to some other MST algorithms.
Disadvantages:

Like Kruskal’s algorithm, Prim’s algorithm can be slow on dense graphs with many edges, as it requires iterating 
over all edges at least once.
Prim’s algorithm relies on a priority queue, which can take up extra memory and slow down the algorithm on very 
large graphs.
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

#---------------------

"""
w3c school
DSA Prim's Algorithm
Prim's algorithm was invented in 1930 by the Czech mathematician Vojtěch Jarník.

The algorithm was then rediscovered by Robert C. Prim in 1957, and also rediscovered by Edsger W. Dijkstra in 1959. Therefore, the algorithm is also sometimes called "Jarník's algorithm", or the "Prim-Jarník algorithm".

Prim's Algorithm
Prim's algorithm finds the Minimum Spanning Tree (MST) in a connected and undirected graph.


Run Prim's
The MST found by Prim's algorithm is the collection of edges in a graph, that connects all vertices, with a minimum sum of edge weights.

Prim's algorithm finds the MST by first including a random vertex to the MST. The algorithm then finds the vertex with the lowest edge weight from the current MST, and includes that to the MST. Prim's algorithm keeps doing this until all nodes are included in the MST.

Prim's algorithm is greedy, and has a straightforward way to create a minimum spanning tree.

For Prim's algorithm to work, all the nodes must be connected. To find the MST's in an unconnected graph, Kruskal's algorithm can be used instead. You can read about Kruskal's algorithm on the next page.

How it works:

Choose a random vertex as the starting point, and include it as the first vertex in the MST.
Compare the edges going out from the MST. Choose the edge with the lowest weight that connects a vertex among the MST vertices to a vertex outside the MST.
Add that edge and vertex to the MST.
Keep doing step 2 and 3 until all vertices belong to the MST.
NOTE: Since the starting vertex is chosen at random, it is possible to have different edges included in the MST for the same graph, but the total edge weight of the MST will still have the same minimum value.

Manual Run Through
Let's run through Prim's algorithm manually on the graph below, so that we understand the detailed step-by-step operations before we try to program it.

Prim's algorithm starts growing the Minimum Spanning Tree (MST) from a random vertex, but for this demonstration vertex A is chosen as the starting vertex.

4
3
3
5
6
4
2
7
4
5
3
7
5
A
B
C
D
E
F
G
H
From vertex A, the MST grows along the edge with the lowest weight. So vertices A and D now belong to the group of vertices that belong to the Minimum Spanning Tree.

4
3
3
5
6
4
2
7
4
5
3
7
5
A
B
C
D
E
F
G
H
A parents array is central to how Prim's algorithm grows the edges in the MST.

At this point, the parents array looks like this:

parents = [-1,  0, -1,  0,  3,  3, -1, -1]
#vertices [ A,  B,  C,  D,  E,  F,  G,  H]
Vertex A, the starting vertex, has no parent, and has therefore value -1. Vertex D's parent is A, that is why D's parent value is 0 (vertex A is located at index 0). B's parent is also A, and D is the parent of E and F.

The parents array helps us to keep the MST tree structure (a vertex can only have one parent).

Also, to avoid cycles and to keep track of which vertices are currently in the MST, the in_mst array is used.

The in_mst array currently looks like this:

 in_mst = [ true, false, false,  true, false, false, false, false]
#vertices [    A,     B,     C,     D,     E,     F,     G,     H]
The next step in Prim's algorithm is to include one more vertex as part of the MST, and the vertex closest to the current MST nodes A and D is chosen.

Since both A-B and D-F have the same lowest edge weight 4, either B or F can be chosen as the next MST vertex. We choose B as the next MST vertex for this demonstration.

4
3
3
5
6
4
2
7
4
5
3
7
5
A
B
C
D
E
F
G
H
As you can see, the MST edge to E came from vertex D before, now it comes from vertex B, because B-E with weight 6 is lower than D-E with weight 7. Vertex E can only have one parent in the MST tree structure (and in the parents array), so B-E and D-E cannot both be MST edges to E.

The next vertex in the MST is vertex C, because edge B-C with weight 3 is the shortest edge weight from the current MST vertices.

4
3
3
5
6
4
2
7
4
5
3
7
5
A
B
C
D
E
F
G
H
As vertex C is included in the MST, edges out from C are checked to see if there are edges with a lower weight from this MST vertex to vertices outside the MST. Edge C-E has a lower weight (3) than the previous B-E MST edge (6), and the C-H edge gets included in the MST with edge weight 2.

Vertex H is the next to be included in the MST, as it has the lowest edge weight 6, and vertex H becomes the parent of vertex G in the parents array.

4
3
3
5
6
4
2
7
4
5
3
7
5
A
B
C
D
E
F
G
H
The next vertex to be included in the MST is either E or F because they have both the lowest edge weight to them: 4.

We choose vertex E as the next vertex to be included in the MST for this demonstration.

4
3
3
5
6
4
2
7
4
5
3
7
5
A
B
C
D
E
F
G
H
The next and last two vertices to be added to the MST are vertices F and G. D-F is the MST edge to F, and E-G is the MST edge to G because these edges are the edges with the lowest weight from the current MST.

Run the simulation below to see Prim's algorithm doing the manual steps that we have just done.

4
3
3
5
6
4
2
7
4
5
3
7
5
A
B
C
D
E
F
G
H

Run Prim's
Implementation of Prim's Algorithm
For Prim's algorithm to find a Minimum Spanning Tree (MST), we create a Graph class. We will use the methods inside this Graph class later to create the graph from the example above, and to run Prim's algorithm on it.

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
Line 3-5: At first, the adjacency matrix is empty, meaning there are no edges in the graph. Also, the vertices have no names to start with.

Line 7-10: The add_edge method is for adding an edge, with an edge weight value, to the undirected graph.

Line 12-14: The add_vertex_data method is used for giving names to the vertices, like for example 'A' or 'B'.

Now that the structure for creating a graph is in place, we can implement Prim's algorithm as a method inside the Graph class:

    def prims_algorithm(self):
        in_mst = [False] * self.size
        key_values = [float('inf')] * self.size
        parents = [-1] * self.size

        key_values[0] = 0  # Starting vertex

        print("Edge \tWeight")
        for _ in range(self.size):
            u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])

            in_mst[u] = True

            if parents[u] != -1:  # Skip printing for the first vertex since it has no parent
                print(f"{self.vertex_data[parents[u]]}-{self.vertex_data[u]} \t{self.adj_matrix[u][parents[u]]}")

            for v in range(self.size):
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u
Line 17: The in_mst array holds the status of which vertices are currently in the MST. Initially, none of the vertices are part of the MST.

Line 18: The key_values array holds the current shortest distance from the MST vertices to each vertex outside the MST.

Line 19: The MST edges are stored in the parents array. Each MST edge is stored by storing the parent index for each vertex.

Line 21: To keep it simple, and to make this code run like in the "Manual Run Through" animation/example above, the first vertex (vertex A at index 0) is set as the staring vertex. Changing the index to 4 will run Prim's algorithm from vertex E, and that works just as well.

Line 25: The index is found for the vertex with the lowest key value that is not yet part of the MST. Check out these explanations for min and lambda to better understand this Python code line.

Line 32-35: After a new vertex is added to the MST (line 27), this part of the code checks to see if there are now edges from this newly added MST vertex that can lower the key values to other vertices outside the MST. If that is the case, the key_values and parents arrays are updated accordingly. This can be seen clearly in the animation when a new vertex is added to the MST and becomes the active (current) vertex.

Now let's create the graph from the "Manual Run Through" above and run Prim's algorithm on it:

Example
Python:

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def prims_algorithm(self):
        in_mst = [False] * self.size
        key_values = [float('inf')] * self.size
        parents = [-1] * self.size

        key_values[0] = 0  # Starting vertex

        print("Edge \tWeight")
        for _ in range(self.size):
            u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])

            in_mst[u] = True

            if parents[u] != -1:  # Skip printing for the first vertex since it has no parent
                print(f"{self.vertex_data[parents[u]]}-{self.vertex_data[u]} \t{self.adj_matrix[u][parents[u]]}")

            for v in range(self.size):
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u

g = Graph(8)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')

g.add_edge(0, 1, 4)  # A - B
g.add_edge(0, 3, 3)  # A - D
g.add_edge(1, 2, 3)  # B - C
g.add_edge(1, 3, 5)  # B - D
g.add_edge(1, 4, 6)  # B - E
g.add_edge(2, 4, 4)  # C - E
g.add_edge(2, 7, 2)  # C - H
g.add_edge(3, 4, 7)  # D - E
g.add_edge(3, 5, 4)  # D - F
g.add_edge(4, 5, 5)  # E - F
g.add_edge(4, 6, 3)  # E - G
g.add_edge(5, 6, 7)  # F - G
g.add_edge(6, 7, 5)  # G - H

print("Prim's Algorithm MST:")
g.prims_algorithm()
Line 32: We can actually avoid the last loop in Prim's algorithm by changing this line to for _ in range(self.size - 1):. This is because when there is just one vertex not yet in the MST, the parent vertex for that vertex is already set correctly in the parents array, so the MST is actually already found at this point.

Time Complexity for Prim's Algorithm
For a general explanation of what time complexity is, visit this page.

With 
V
 as the number of vertices in our graph, the time complexity for Prim's algorithm is

O
(
V
2
)

The reason why we get this time complexity is because of the nested loops inside the Prim's algorithm (one for-loop with two other for-loops inside it).

The first for-loop (line 24) goes through all the vertices in the graph. This has time complexity 
O
(
V
)
.

The second for-loop (line 25) goes through all the adjacent vertices in the graph to find the vertex with the lowest key value that is outside the MST, so that it can be the next vertex included in the MST. This has time complexity 
O
(
V
)
.

After a new vertex is included in the MST, a third for-loop (line 32) checks all other vertices to see if there are outgoing edges from the newly added MST vertex to vertices outside the MST that can lead to lower key values and updated parent relations. This also has time complexity 
O
(
V
)
.

Putting the time complexities together we get:

O
(
V
)
⋅
(
O
(
V
)
+
O
(
V
)
)
=
O
(
V
)
⋅
(
2
⋅
O
(
V
)
)
=
O
(
V
⋅
2
⋅
V
)
=
O
(
2
⋅
V
2
)
=
O
(
V
2
)

By using a priority queue data structure to manage key values, instead of using an array like we do here, the time complexity for Prim's algorithm can be reduced to:

O
(
E
⋅
log
V
)

Where 
E
 is the number of edges in the graph, and 
V
 is the number of vertices.

Such an implementation of Prim's algorithm using a priority queue is best for sparse graphs. A graph is sparse when the each vertex is just connected to a few of the other vertices.


"""










