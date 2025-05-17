


"""

Prim’s algorithm is a Greedy algorithm like Kruskal’s algorithm. This algorithm always starts with a single node and moves through several adjacent nodes, in order to explore all of the connected edges along the way.

The algorithm starts with an empty spanning tree.
The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST, and the other set contains the vertices not yet included.
At every step, it considers all the edges that connect the two sets and picks the minimum weight edge from these edges. After picking the edge, it moves the other endpoint of the edge to the set containing MST.
A group of edges that connects two sets of vertices in a graph is called Articulation Points (or Cut Vertices) in graph theory. So, at every step of Prim’s algorithm, find a cut, pick the minimum weight edge from the cut, and include this vertex in MST Set (the set that contains already included vertices).

Working of the Prim’s Algorithm
Step 1: Determine an arbitrary vertex as the starting vertex of the MST. We pick 0 in the below diagram.
Step 2: Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
Step 3: Find edges connecting any tree vertex with the fringe vertices.
Step 4: Find the minimum among these edges.
Step 5: Add the chosen edge to the MST. Since we consider only the edges that connect fringe vertices with the rest, we never get a cycle.
Step 6: Return the MST and exit

Prims-Algorithm-1.webpPrims-Algorithm-1.webp


How to implement Prim’s Algorithm?
Follow the given steps to utilize the Prim’s Algorithm mentioned above for finding MST of a graph:

Create a set mstSet that keeps track of vertices already included in MST.
Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign the key value as 0 for the first vertex so that it is picked first.
While mstSet doesn’t include all vertices
Pick a vertex u that is not there in mstSet and has a minimum key value.
Include u in the mstSet.
Update the key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices. For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value as the weight of u-v.
The idea of using key values is to pick the minimum weight edge from the cut. The key values are used only for vertices that are not yet included in MST, the key value for these vertices indicates the minimum weight edges connecting them to the set of vertices included in MST.

Below is the implementation of the approach:

Try it on GfG Practice
redirect icon



1
# A Python3 program for
2
# Prim's Minimum Spanning Tree (MST) algorithm.
3
# The program is for adjacency matrix
4
# representation of the graph
5
​
6
# Library for INT_MAX
7
import sys
8
​
9
​
10
class Graph():
11
    def __init__(self, vertices):
12
        self.V = vertices
13
        self.graph = [[0 for column in range(vertices)]
14
                      for row in range(vertices)]
15
​
16
    # A utility function to print
17
    # the constructed MST stored in parent[]
18
    def printMST(self, parent):
19
        print("Edge \tWeight")
20
        for i in range(1, self.V):
21
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])
22
​
23
    # A utility function to find the vertex with
24
    # minimum distance value, from the set of vertices
25
    # not yet included in shortest path tree
26
    def minKey(self, key, mstSet):
27
​
28
        # Initialize min value
29
        min = sys.maxsize
30
​
31
        for v in range(self.V):
32
            if key[v] < min and mstSet[v] == False:
33
                min = key[v]
34
                min_index = v
35
​
36
        return min_index
37
​
38
    # Function to construct and print MST for a graph
39
    # represented using adjacency matrix representation
40
    def primMST(self):
41
​
42
        # Key values used to pick minimum weight edge in cut
43
        key = [sys.maxsize] * self.V
44
        parent = [None] * self.V  # Array to store constructed MST
45
        # Make key 0 so that this vertex is picked as first vertex
46
        key[0] = 0
47
        mstSet = [False] * self.V
48
​
49
        parent[0] = -1  # First node is always the root of
50
​
51
        for cout in range(self.V):
52
​
53
            # Pick the minimum distance vertex from
54
            # the set of vertices not yet processed.
55
            # u is always equal to src in first iteration
56
            u = self.minKey(key, mstSet)
57
​
58
            # Put the minimum distance vertex in
59
            # the shortest path tree
60
            mstSet[u] = True
61
​
62
            # Update dist value of the adjacent vertices
63
            # of the picked vertex only if the current
64
            # distance is greater than new distance and
65
            # the vertex in not in the shortest path tree
66
            for v in range(self.V):
67
​
68
                # graph[u][v] is non zero only for adjacent vertices of m
69
                # mstSet[v] is false for vertices not yet included in MST
70
                # Update the key only if graph[u][v] is smaller than key[v]
71
                if self.graph[u][v] > 0 and mstSet[v] == False \
72
                and key[v] > self.graph[u][v]:
73
                    key[v] = self.graph[u][v]
74
                    parent[v] = u
75
​
76
        self.printMST(parent)
77
​
78
​
79
# Driver's code
80
if __name__ == '__main__':
81
    g = Graph(5)
82
    g.graph = [[0, 2, 0, 6, 0],
83
               [2, 0, 3, 8, 5],
84
               [0, 3, 0, 0, 7],
85
               [6, 8, 0, 0, 9],
86
               [0, 5, 7, 9, 0]]
87
​
88
    g.primMST()

Output
Edge 	Weight
0 - 1 	2
1 - 2 	3
0 - 3 	6
1 - 4 	5
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



1
import heapq
2
​
3
def tree(V, E, edges):
4
    # Create an adjacency list representation of the graph
5
    adj = [[] for _ in range(V)]
6
    # Fill the adjacency list with edges and their weights
7
    for i in range(E):
8
        u, v, wt = edges[i]
9
        adj[u].append((v, wt))
10
        adj[v].append((u, wt))
11
    # Create a priority queue to store edges with their weights
12
    pq = []
13
    # Create a visited array to keep track of visited vertices
14
    visited = [False] * V
15
    # Variable to store the result (sum of edge weights)
16
    res = 0
17
    # Start with vertex 0
18
    heapq.heappush(pq, (0, 0))
19
    # Perform Prim's algorithm to find the Minimum Spanning Tree
20
    while pq:
21
        wt, u = heapq.heappop(pq)
22
        if visited[u]:
23
            continue
24
            # Skip if the vertex is already visited
25
        res += wt
26
        # Add the edge weight to the result
27
        visited[u] = True
28
        # Mark the vertex as visited
29
        # Explore the adjacent vertices
30
        for v, weight in adj[u]:
31
            if not visited[v]:
32
                heapq.heappush(pq, (weight, v))
33
                # Add the adjacent edge to the priority queue
34
    return res
35
  # Return the sum of edge weights of the Minimum Spanning Tree
36
if __name__ == "__main__":
37
    graph = [[0, 1, 5],
38
             [1, 2, 3],
39
             [0, 2, 1]]
40
    # Function call
41
    print(tree(3, 3, graph))

Output
4
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

"""