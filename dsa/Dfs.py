"""

Depth First Search or DFS for a Graph
Last Updated : 29 Mar, 2025
In Depth First Search (or DFS) for a graph, we traverse all adjacent vertices one by one. When we traverse an adjacent vertex, we completely finish the traversal of all vertices reachable through that adjacent vertex. This is similar to a tree, where we first completely traverse the left subtree and then move to the right subtree. The key difference is that, unlike trees, graphs may contain cycles (a node may be visited more than once). To avoid processing a node multiple times, we use a boolean visited array.

Example:

Note : There can be multiple DFS traversals of a graph according to the order in which we pick adjacent vertices. Here we pick vertices as per the insertion order.


Input: adj =  [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]


Input_undirected_Graph
Output: [0 1 2 3 4]
Explanation:  The source vertex s is 0. We visit it first, then we visit an adjacent.
Start at 0: Mark as visited. Output: 0
Move to 1: Mark as visited. Output: 1
Move to 2: Mark as visited. Output: 2
Move to 3: Mark as visited. Output: 3 (backtrack to 2)
Move to 4: Mark as visited. Output: 4 (backtrack to 2, then backtrack to 1, then to 0)


Not that there can be more than one DFS Traversals of a Graph. For example, after 1, we may pick adjacent 2 instead of 0 and get a different DFS. Here we pick in the insertion order.


Input: [[2,3,1], [0], [0,4], [0], [2]]


Input_undirected_Graph2
Output: [0 2 4 3 1]
Explanation: DFS Steps:


Start at 0: Mark as visited. Output: 0
Move to 2: Mark as visited. Output: 2
Move to 4: Mark as visited. Output: 4 (backtrack to 2, then backtrack to 0)
Move to 3: Mark as visited. Output: 3 (backtrack to 0)
Move to 1: Mark as visited. Output: 1 (backtrack to 0)


Try it on GfG Practice
redirect icon
Table of Content

DFS from a Given Source of Undirected Graph:
DFS for Complete Traversal of Disconnected Undirected Graph
DFS from a Given Source of Undirected Graph:
The algorithm starts from a given source and explores all reachable vertices from the given source. It is similar to Preorder Tree Traversal where we visit the root, then recur for its children. In a graph, there might be loops. So we use an extra visited array to make sure that we do not process a vertex again.


Let us understand the working of Depth First Search with the help of the following Illustration: for the source as 0.

DFS-for-a-Graph-2.webpDFS-for-a-Graph-2.webp





def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    # Recursively visit all adjacent vertices that are not visited yet
    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfsRec(adj, visited, i, res)


def DFS(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)  # Start DFS from vertex 0
    return res


def add_edge(adj, s, t):
    adj[s][t] = 1
    adj[t][s] = 1  # Since it's an undirected graph


# Driver code
V = 5
adj = [[0] * V for _ in range(V)]  # Adjacency matrix

# Define the edges of the graph
edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

# Populate the adjacency matrix with edges
for s, t in edges:
    add_edge(adj, s, t)

res = DFS(adj)  # Perform DFS
print(" ".join(map(str, res)))

Output
0 1 2 3 4
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to dfsRec function.

Please refer Complexity Analysis of Depth First Search for details.

DFS for Complete Traversal of Disconnected Undirected Graph
The above implementation takes a source as an input and prints only those vertices that are reachable from the source and would not print all vertices in case of disconnected graph. Let us now talk about the algorithm that prints all vertices without any source and the graph maybe disconnected.


The idea is simple, instead of calling DFS for a single vertex, we call the above implemented DFS for all all non-visited vertices one by one.




# Create an adjacency list for the graph
from collections import defaultdict


def add_edge(adj, s, t):
    adj[s].append(t)
    adj[t].append(s)

# Recursive function for DFS traversal


def dfs_rec(adj, visited, s, res):
    # Mark the current vertex as visited
    visited[s] = True
    res.append(s)

    # Recursively visit all adjacent vertices that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i, res)

# Main DFS function to perform DFS for the entire graph


def dfs(adj):
    visited = [False] * len(adj)
    res = []
    # Loop through all vertices to handle disconnected graph
    for i in range(len(adj)):
        if not visited[i]:
            # If vertex i has not been visited,
            # perform DFS from it
            dfs_rec(adj, visited, i, res)
    return res


V = 6
# Create an adjacency list for the graph
adj = defaultdict(list)

# Define the edges of the graph
edges = [[1, 2], [2, 0], [0, 3], [4, 5]]

# Populate the adjacency list with edges
for e in edges:
    add_edge(adj, e[0], e[1])
res = dfs(adj)

print(' '.join(map(str, res)))

Output
0 2 1 3 4 5
Time complexity: O(V + E). Note that the time complexity is same here because we visit every vertex at most once and every edge is traversed at most once (in directed) and twice in undirected.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to dfsRec function.

Related Articles:

Depth First Search or DFS on Directed Graph
Breadth First Search or BFS for a Graph

"""
"""
Depth First Search or DFS on Directed Graph
Last Updated : 09 Aug, 2024
Depth-First Search (DFS) is a basic algorithm used to explore graph structures. In directed graphs, DFS can start from a specific point and explore all the connected nodes. It can also be used to make sure every part of the graph is visited, even if the graph has disconnected sections. This article explains how DFS works when starting from a single point and how it can be used to explore an entire graph, including disconnected parts.

Example:

Input: V = 5, E = 5, edges = {{1, 2}, {1, 0}, {2, 0}, {2, 3}, {4, 2}}, source = 1

3
 
Output: 1 2 0 3
Explanation: DFS Steps:

Start at 1: Mark as visited. Output: 1
Move to 2: Mark as visited. Output: 2
Move to 0: Mark as visited. Output: 0 (backtrack to 2)
Move to 3: Mark as visited. Output: 3 (backtrack to 2)
All neighbors of 2 explored (backtrack to 1)
All neighbors of 1 explored (end of traversal)
Input: V = 5, E = 4, edges = {{0, 2}, {0, 3}, {2, 4}, {1, 0}}, source = 2

4
 
Output: 2 4
Explanation: DFS Steps:

Start at 2: Mark as visited. Output: 2
Move to 4: Mark as visited. Output: 4 (backtrack to 2)
All neighbors of 2 explored (backtrack to start)
DFS from a Given Source in Directed Graph
Depth-First Search (DFS) from a given source is a method of exploring a directed graph by starting at a specific vertex and traversing each node as far as we can go down in the path. If we reach a vertex that has no unvisited neighbors, we backtrack to the previous vertex to explore any other paths that haven't been visited yet. This approach is particularly useful for tasks such as finding paths, checking connectivity, and exploring all reachable nodes from a starting point.

How It Works:

Keep a boolean visited array to keep track of which vertices have already been visited. This will help in not entering in infinite loops when there are cycles in the graph.
Use Recursion to visited all unvisited neighbours of source node:
First marks the current vertex as visited and processes the current vertex (for example, by printing its value).
Then, recursively visits each unvisited neighbor of the current vertex.
If a vertex has no unvisited neighbors, backtracks to the previous vertex to explore other unvisited paths.
Below is the implementation of the above approach:




def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)

def dfs_rec(adj, visited, s):
    # Mark the current vertex as visited
    visited[s] = True

    # Print the current vertex
    print(s, end=" ")

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, s):
    visited = [False] * len(adj)
    # Call the recursive DFS function
    dfs_rec(adj, visited, s)


if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)

Output
DFS from source: 1
1 2 0 3 4 
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to DFSRec function.

Please refer Complexity Analysis of Depth First Search: for details.

DFS for Complete Traversal of Disconnected Directed Graphs
In a directed graph, edges have a specific direction means we can travel from one vertex to another only in the direction the edge points. A disconnected graph is one in which not all vertices are reachable from a single vertex.

The above implementation takes a source as an input and prints only those vertices that are reachable from the source and would not print all vertices in case of disconnected graph. Let us now talk about the algorithm that prints all vertices without any source and the graph maybe disconnected.

To handle such a graph in DFS, we must ensure that the DFS algorithm starts from every unvisited vertex and this results in covering all components of the graph




class Graph:
    def __init__(self, vertices):
        # Adjacency list
        self.adj = [[] for _ in range(vertices)]  

    def add_edge(self, s, t):
        self.adj[s].append(t)  

    def dfs_rec(self, visited, s):
        visited[s] = True 
        print(s, end=" ") 

        # Recursively visit all adjacent vertices
        # that are not visited yet
        for i in self.adj[s]:
            if not visited[i]:
                self.dfs_rec(visited, i)

    def dfs(self):
        visited = [False] * len(self.adj) 

        # Loop through all vertices to handle disconnected
        # graph
        for i in range(len(self.adj)):
            if not visited[i]:
                  # Perform DFS from unvisited vertex
                self.dfs_rec(visited, i)


if __name__ == "__main__":
    V = 6  # Number of vertices
    graph = Graph(V)

    # Define the edges of the graph
    edges = [(1, 2), (2, 0), (0, 3), (4, 5)]

    # Populate the adjacency list with edges
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    print("Complete DFS of the graph:")
    graph.dfs()  # Perform DFS

Output
Complete DFS of the graph:
0 2 1 3 4 5 
Time Complexity: O(V + E). Note that the time complexity is same here because we visit every vertex at most once and every edge is traversed at most once (in directed) and twice in undirected.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to DFSRec function.
"""

"""
Depth First Search or DFS for a Graph
Last Updated : 29 Mar, 2025
In Depth First Search (or DFS) for a graph, we traverse all adjacent vertices one by one. When we traverse an adjacent vertex, we completely finish the traversal of all vertices reachable through that adjacent vertex. This is similar to a tree, where we first completely traverse the left subtree and then move to the right subtree. The key difference is that, unlike trees, graphs may contain cycles (a node may be visited more than once). To avoid processing a node multiple times, we use a boolean visited array.

Example:

Note : There can be multiple DFS traversals of a graph according to the order in which we pick adjacent vertices. Here we pick vertices as per the insertion order.


Input: adj =  [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]


Input_undirected_Graph
Output: [0 1 2 3 4]
Explanation:  The source vertex s is 0. We visit it first, then we visit an adjacent. 
Start at 0: Mark as visited. Output: 0
Move to 1: Mark as visited. Output: 1 
Move to 2: Mark as visited. Output: 2 
Move to 3: Mark as visited. Output: 3 (backtrack to 2)
Move to 4: Mark as visited. Output: 4 (backtrack to 2, then backtrack to 1, then to 0)


Not that there can be more than one DFS Traversals of a Graph. For example, after 1, we may pick adjacent 2 instead of 0 and get a different DFS. Here we pick in the insertion order.


Input: [[2,3,1], [0], [0,4], [0], [2]]


Input_undirected_Graph2
Output: [0 2 4 3 1]
Explanation: DFS Steps:


Start at 0: Mark as visited. Output: 0
Move to 2: Mark as visited. Output: 2
Move to 4: Mark as visited. Output: 4 (backtrack to 2, then backtrack to 0)
Move to 3: Mark as visited. Output: 3 (backtrack to 0)
Move to 1: Mark as visited. Output: 1 (backtrack to 0)


Try it on GfG Practice
redirect icon
Table of Content

DFS from a Given Source of Undirected Graph:
DFS for Complete Traversal of Disconnected Undirected Graph
DFS from a Given Source of Undirected Graph:
The algorithm starts from a given source and explores all reachable vertices from the given source. It is similar to Preorder Tree Traversal where we visit the root, then recur for its children. In a graph, there might be loops. So we use an extra visited array to make sure that we do not process a vertex again.


Let us understand the working of Depth First Search with the help of the following Illustration: for the source as 0.

DFS-for-a-Graph-1.webpDFS-for-a-Graph-1.webp





def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    # Recursively visit all adjacent vertices that are not visited yet
    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfsRec(adj, visited, i, res)


def DFS(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)  # Start DFS from vertex 0
    return res


def add_edge(adj, s, t):
    adj[s][t] = 1
    adj[t][s] = 1  # Since it's an undirected graph


# Driver code
V = 5
adj = [[0] * V for _ in range(V)]  # Adjacency matrix

# Define the edges of the graph
edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

# Populate the adjacency matrix with edges
for s, t in edges:
    add_edge(adj, s, t)

res = DFS(adj)  # Perform DFS
print(" ".join(map(str, res)))

Output
0 1 2 3 4 
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to dfsRec function.

Please refer Complexity Analysis of Depth First Search for details.

DFS for Complete Traversal of Disconnected Undirected Graph
The above implementation takes a source as an input and prints only those vertices that are reachable from the source and would not print all vertices in case of disconnected graph. Let us now talk about the algorithm that prints all vertices without any source and the graph maybe disconnected. 


The idea is simple, instead of calling DFS for a single vertex, we call the above implemented DFS for all all non-visited vertices one by one.




# Create an adjacency list for the graph
from collections import defaultdict


def add_edge(adj, s, t):
    adj[s].append(t)
    adj[t].append(s)

# Recursive function for DFS traversal


def dfs_rec(adj, visited, s, res):
    # Mark the current vertex as visited
    visited[s] = True
    res.append(s)

    # Recursively visit all adjacent vertices that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i, res)

# Main DFS function to perform DFS for the entire graph


def dfs(adj):
    visited = [False] * len(adj)
    res = []
    # Loop through all vertices to handle disconnected graph
    for i in range(len(adj)):
        if not visited[i]:
            # If vertex i has not been visited,
            # perform DFS from it
            dfs_rec(adj, visited, i, res)
    return res


V = 6
# Create an adjacency list for the graph
adj = defaultdict(list)

# Define the edges of the graph
edges = [[1, 2], [2, 0], [0, 3], [4, 5]]

# Populate the adjacency list with edges
for e in edges:
    add_edge(adj, e[0], e[1])
res = dfs(adj)

print(' '.join(map(str, res)))

Output
0 2 1 3 4 5 
Time complexity: O(V + E). Note that the time complexity is same here because we visit every vertex at most once and every edge is traversed at most once (in directed) and twice in undirected.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to dfsRec function.

"""

"""
Depth First Search or DFS on Directed Graph
Last Updated : 09 Aug, 2024
Depth-First Search (DFS) is a basic algorithm used to explore graph structures. In directed graphs, DFS can start from a specific point and explore all the connected nodes. It can also be used to make sure every part of the graph is visited, even if the graph has disconnected sections. This article explains how DFS works when starting from a single point and how it can be used to explore an entire graph, including disconnected parts.

Example:

Input: V = 5, E = 5, edges = {{1, 2}, {1, 0}, {2, 0}, {2, 3}, {4, 2}}, source = 1

3
 
Output: 1 2 0 3
Explanation: DFS Steps:

Start at 1: Mark as visited. Output: 1
Move to 2: Mark as visited. Output: 2
Move to 0: Mark as visited. Output: 0 (backtrack to 2)
Move to 3: Mark as visited. Output: 3 (backtrack to 2)
All neighbors of 2 explored (backtrack to 1)
All neighbors of 1 explored (end of traversal)
Input: V = 5, E = 4, edges = {{0, 2}, {0, 3}, {2, 4}, {1, 0}}, source = 2

4
 
Output: 2 4
Explanation: DFS Steps:

Start at 2: Mark as visited. Output: 2
Move to 4: Mark as visited. Output: 4 (backtrack to 2)
All neighbors of 2 explored (backtrack to start)
DFS from a Given Source in Directed Graph
Depth-First Search (DFS) from a given source is a method of exploring a directed graph by starting at a specific vertex and traversing each node as far as we can go down in the path. If we reach a vertex that has no unvisited neighbors, we backtrack to the previous vertex to explore any other paths that haven't been visited yet. This approach is particularly useful for tasks such as finding paths, checking connectivity, and exploring all reachable nodes from a starting point.

How It Works:

Keep a boolean visited array to keep track of which vertices have already been visited. This will help in not entering in infinite loops when there are cycles in the graph.
Use Recursion to visited all unvisited neighbours of source node:
First marks the current vertex as visited and processes the current vertex (for example, by printing its value).
Then, recursively visits each unvisited neighbor of the current vertex.
If a vertex has no unvisited neighbors, backtracks to the previous vertex to explore other unvisited paths.
Below is the implementation of the above approach:




def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)

def dfs_rec(adj, visited, s):
    # Mark the current vertex as visited
    visited[s] = True

    # Print the current vertex
    print(s, end=" ")

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, s):
    visited = [False] * len(adj)
    # Call the recursive DFS function
    dfs_rec(adj, visited, s)


if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)

Output
DFS from source: 1
1 2 0 3 4 
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to DFSRec function.

Please refer Complexity Analysis of Depth First Search: for details.

DFS for Complete Traversal of Disconnected Directed Graphs
In a directed graph, edges have a specific direction means we can travel from one vertex to another only in the direction the edge points. A disconnected graph is one in which not all vertices are reachable from a single vertex.

The above implementation takes a source as an input and prints only those vertices that are reachable from the source and would not print all vertices in case of disconnected graph. Let us now talk about the algorithm that prints all vertices without any source and the graph maybe disconnected.

To handle such a graph in DFS, we must ensure that the DFS algorithm starts from every unvisited vertex and this results in covering all components of the graph




class Graph:
    def __init__(self, vertices):
        # Adjacency list
        self.adj = [[] for _ in range(vertices)]  

    def add_edge(self, s, t):
        self.adj[s].append(t)  

    def dfs_rec(self, visited, s):
        visited[s] = True 
        print(s, end=" ") 

        # Recursively visit all adjacent vertices
        # that are not visited yet
        for i in self.adj[s]:
            if not visited[i]:
                self.dfs_rec(visited, i)

    def dfs(self):
        visited = [False] * len(self.adj) 

        # Loop through all vertices to handle disconnected
        # graph
        for i in range(len(self.adj)):
            if not visited[i]:
                  # Perform DFS from unvisited vertex
                self.dfs_rec(visited, i)


if __name__ == "__main__":
    V = 6  # Number of vertices
    graph = Graph(V)

    # Define the edges of the graph
    edges = [(1, 2), (2, 0), (0, 3), (4, 5)]

    # Populate the adjacency list with edges
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    print("Complete DFS of the graph:")
    graph.dfs()  # Perform DFS

Output
Complete DFS of the graph:
0 2 1 3 4 5 
Time Complexity: O(V + E). Note that the time complexity is same here because we visit every vertex at most once and every edge is traversed at most once (in directed) and twice in undirected.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to DFSRec function.
"""

"""
Depth First Search or DFS for disconnected Graph
Last Updated : 13 Jun, 2023
Given a Disconnected Graph, the task is to implement DFS or Depth First Search Algorithm for this Disconnected Graph.

Example:


Input: 



Disconnected Graph
Disconnected Graph



Output: 0 1 2 3


Algorithm for DFS on Disconnected Graph:
In the post for Depth First Search for Graph, only the vertices reachable from a given source vertex can be visited. All the vertices may not be reachable from a given vertex, as in a Disconnected graph. This issue can be resolved by following the below idea:


Iterate over all the vertices of the graph and for any unvisited vertex, run a DFS from that vertex. The recursive function in this case remains the same as in the previous post.


Code Implementation of DFS for Disconnected Graph:
# Python3 program to print DFS traversal
# for complete graph
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal.
    # It uses recursive DFSUtil
    def DFS(self):

        # Create a set to store all visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal starting from all
        # vertices one by one
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)


# Driver's code
if __name__ == "__main__":
    print("Following is Depth First Traversal")
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    # Function call
    g.DFS()
Output
Following is Depth First Traversal 
0 1 2 3 
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V), since an extra visited array of size V is required.
"""





















