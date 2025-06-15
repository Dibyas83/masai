
"""
A vertex, also called a node, is a point or an object in the Graph, and an edge is used to connect two vertices with
each other.

Graphs are non-linear because the data structure allows us to have different paths to get from one vertex to another
, unlike with linear data structures like Arrays or Linked Lists.

Graphs are used to represent and solve problems where the data consists of objects and relationships between them,
such as:

Social Networks: Each person is a vertex, and relationships (like friendships) are the edges. Algorithms can suggest
 potential friends.
Maps and Navigation: Locations, like a town or bus stops, are stored as vertices, and roads are stored as edges.
Algorithms can find the shortest route between two locations when stored as a Graph.
Internet: Can be represented as a Graph, with web pages as vertices and hyperlinks as edges.
Biology: Graphs can model systems like neural networks or the spread of diseases.

A weighted Graph is a Graph where the edges have values. The weight value of an edge can represent things like
distance, capacity, time, or probability.

A connected Graph is when all the vertices are connected through edges somehow. A Graph that is not connected, is
 a Graph with isolated (disjoint) subgraphs, or single isolated vertices.

A directed Graph, also known as a digraph, is when the edges between the vertex pairs have a direction. The
direction of an edge can represent things like hierarchy or flow.

A cyclic Graph is defined differently depending on whether it is directed or not:

A directed cyclic Graph is when you can follow a path along the directed edges that goes in circles. Removing the
 directed edge from F to G in the animation above makes the directed Graph not cyclic anymore.
An undirected cyclic Graph is when you can come back to the same vertex you started at without using the same edge
more than once. The undirected Graph above is cyclic because we can start and end up in vertes C without using the
same edge twice.
A loop, also called a self-loop, is an edge that begins and ends on the same vertex. A loop is a cycle that only
consists of one edge. By adding the loop on vertex A in the animation above, the Graph becomes cyclic.

Below are short introductions of the different Graph representations, but Adjacency Matrix is the representation
we will use for Graphs moving forward in this tutorial, as it is easy to understand and implement, and works in
all cases relevant for this tutorial.

Graph representations store information about which vertices are adjacent, and how the edges between the vertices
 are. Graph representations are slightly different if the edges are directed or weighted.

Two vertices are adjacent, or neighbors, if there is an edge between them.

Adjacency Matrix Graph Representation
Adjacency Matrix is the Graph representation (structure) we will use for this tutorial.

How to implement an Adjacency Matrix is shown on the next page.

The Adjacency Matrix is a 2D array (matrix) where each cell on index (i,j) stores information about the edge
from vertex i to vertex j.

Below is a Graph with the Adjacency Matrix representation next to it.

- A B C D
A   1 1 1
B 1   1
C 1 1
D 1
An undirected Graph
and the adjacency matrix
The adjacency matrix above represents an undirected Graph, so the values '1' only tells us where the edges are.
Also, the values in the adjacency matrix is symmetrical because the edges go both ways (undirected Graph).

To create a directed Graph with an adjacency matrix, we must decide which vertices the edges go from and to, by
 inserting the value at the correct indexes (i,j). To represent a weighted Graph we can put other values than '1'
 inside the adjacency matrix.

Below is a directed and weighted Graph with the Adjacency Matrix representation next to it.

- A B C D
A   3 2
B
C   1
D 4

A directed and weighted Graph,
and its adjacency matrix.
In the adjacency matrix above, the value 3 on index (0,1) tells us there is an edge from vertex A to vertex B, and
 the weight for that edge is 3.

As you can see, the weights are placed directly into the adjacency matrix for the correct edge, and for a directed
 Graph, the adjacency matrix does not have to be symmetric.
------------------------
Adjacency List Graph Representation
In case we have a 'sparse' Graph with many vertices, we can save space by using an Adjacency List compared to using
 an Adjacency Matrix, because an Adjacency Matrix would reserve a lot of memory on empty Array elements for edges
 that don't exist.

A 'sparse' Graph is a Graph where each vertex only has edges to a small portion of the other vertices in the Graph.

An Adjacency List has an array that contains all the vertices in the Graph, and each vertex has a Linked List
(or Array) with the vertex's edges.

0 A - 3-1-2-null
1 B - 0-2-null
2 C - 1-0-null
3 D - 0-null

An undirected Graph
and its adjacency list.
In the adjacency list above, the vertices A to D are placed in an Array, and each vertex in the array has its
index written right next to it.

Each vertex in the Array has a pointer to a Linked List that represents that vertex's edges. More specifically,
the Linked List contains the indexes to the adjacent (neighbor) vertices.

So for example, vertex A has a link to a Linked List with values 3, 1, and 2. These values are the indexes to
A's adjacent vertices D, B, and C.

An Adjacency List can also represent a directed and weighted Graph, like this:

0 A -1,3 - 2,2 - null    (1 and 2 are node serials or index and 2and 3 are their weights of edges
1 B - null
2 C - 1,1 - null
3 D -0,4 - null
A directed and weighted Graph
and its adjacency list.

In the Adjacency List above, vertices are stored in an Array. Each vertex has a pointer to a Linked List with
edges stored as i,w, where i is the index of the vertex the edge goes to, and w is the weight of that edge.

Node D for example, has a pointer to a Linked List with an edge to vertex A. The values 0,4 means that vertex
D has an edge to vertex on index 0 (vertex A), and the weight of that edge is 4.




"""
"""
DSA Graphs Implementation
A Basic Graph Implementation
Before we can run algorithms on a Graph, we must first implement it somehow.

To implement a Graph we will use an Adjacency Matrix, like the one below.

- A B C D
A   1 1 1
B 1   1
C 1 1
D 1

An undirected Graph
and its adjacency matrix
To store data for each vertex, in this case the letters A, B, C, and D, the data is put in a separate array that 
matches the indexes in the adjacency matrix, like this:

vertexData = [ 'A', 'B', 'C', 'D']
For an undirected and not weighted Graph, like in the image above, an edge between vertices i and j is stored 
with value 1. It is stored as 1 on both places (j,i) and (i,j) because the edge goes in both directions. As you 
can see, the matrix becomes diagonally symmetric for such undirected Graphs.

Let's look at something more specific. In the adjacency matrix above, vertex A is on index 0, and vertex D is on
 index 3, so we get the edge between A and D stored as value 1 in position (0,3) and (3,0), because the edge goes 
 in both directions.

Below is a basic implementation of the undirected Graph from the image above.

Example
Python:
"""
vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

print('vertexData:',vertexData)
print_adjacency_matrix(adjacency_matrix)

"""
This implementation is basically just a two dimensional array, but to get a better sense of how the vertices are
 connected by edges in the Graph we have just implemented, we can run this function:

Example
Python:
"""
def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ")
        print()  # new line

print(print_connections(adjacency_matrix, vertexData))

"""
Graph Implementation Using Classes
A more proper way to store a Graph is to add an abstraction layer using classes so that a Graph's vertices, edges,
 and relevant methods, like algorithms that we will implement later, are contained in one place.

Programming languages with built-in object-oriented functionality like Python and Java, make implementation of 
Graphs using classes much easier than languages like C, without this built-in functionality.
- A B C D
A 0 1 1 1
B 1 0 1 0
C 1 1 0 0
D 1 0 0 0

An undirected Graph
and its adjacency matrix
Here is how the undirected Graph above can be implemented using classes.

Example
Python:
"""
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C

g.print_graph()

#in the code above, the matrix symmetry we get for undirected Graphs is provided for on line 9 and 10, and this
# saves us some code when initializing the edges in the Graph on lines 29-32.

"""
Implementation of Directed and Weighted Graphs
To implement a Graph that is directed and weighted, we just need to do a few changes to previous implementation of 
the undirected Graph.

To create directed Graphs, we just need to remove line 10 in the previous example code, so that the matrix is not 
automatically symmetric anymore.

The second change we need to do is to add a weight argument to the add_edge() method, so that instead of just having
 value 1 to indicate that there is an edge between two vertices, we use the actual weight value to define the edge.

- A B C D
A   3 2
B
C   1
D 4


A directed and weighted Graph,
and its adjacency matrix.
Below is the implementation of the directed and weighted Graph above.

Example
Python:
"""
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            #self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        print(self.adj_matrix)
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        print(self.vertex_data)
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3)  # A -> B with weight 3
g.add_edge(0, 2, 2)  # A -> C with weight 2
g.add_edge(3, 0, 4)  # D -> A with weight 4
g.add_edge(2, 1, 1)  # C -> B with weight 1

g.print_graph()
"""
Line 3: All edges are set to None initially.

Line 7: The weight can now be added to an edge with the additional weight argument.

Line 10: By removing line 10, the Graph can now be set up as being directed.

On the next page we will see how Graphs can be traversed, and on the next pages after that we will look at different 
algorithms that can run on the Graph data structure.

"""

#--------------------------------

"""
DSA Graphs Traversal
Graphs Traversal
To traverse a Graph means to start in one vertex, and go along the edges to visit other vertices until all vertices, 
or as many as possible, have been visited.

F
B
C
A
E
D
G
Result:

DFS Traverse from D
Understanding how a Graph can be traversed is important for understanding how algorithms that run on Graphs work.

The two most common ways a Graph can be traversed are:

Depth First Search (DFS)
Breadth First Search (BFS)
DFS is usually implemented using a Stack or by the use of recursion (which utilizes the call stack), while BFS is 
usually implemented using a Queue.

The Call Stack keeps functions running in the correct order.

If for example FunctionA calls FunctionB, FunctionB is placed on top of the call stack and starts running. Once 
FunctionB is finished, it is removed from the stack, and then FunctionA resumes its work.

Depth First Search Traversal
Depth First Search is said to go "deep" because it visits a vertex, then an adjacent vertex, and then that vertex' 
adjacent vertex, and so on, and in this way the distance from the starting vertex increases for each recursive 
iteration.

How it works:

Start DFS traversal on a vertex.
Do a recursive DFS traversal on each of the adjacent vertices as long as they are not already visited.
Run the animation below to see how Depth First Search (DFS) traversal runs on a specific Graph, starting in vertex 
D (it is the same as the previous animation).

F
B
C
A
E
D
G
Result:

DFS Traverse from D
The DFS traversal starts in vertex D, marks vertex D as visited. Then, for every new vertex visited, the traversal 
method is called recursively on all adjacent vertices that have not been visited yet. So when vertex A is visited 
in the animation above, vertex C or vertex E (depending on the implementation) is the next vertex where the traversal 
continues.

"""


class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)


g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

print("\nDepth First Search starting from vertex D:")
g.dfs('D')

"""
Line 60: The DFS traversal starts when the dfs() method is called.

Line 33: The visited array is first set to false for all vertices, because no vertices are visited yet at this point.

Line 35: The visited array is sent as an argument to the dfs_util() method. When the visited array is sent as an
 argument like this, it is actually just a reference to the visited array that is sent to the dfs_util() method, 
 and not the actual array with the values inside. So there is always just one visited array in our program, and 
 the dfs_util() method can make changes to it as nodes are visited (line 25).

Line 28-30: For the current vertex v, all adjacent nodes are called recursively if they are not already visited.

Breadth First Search Traversal
Breadth First Search visits all adjacent vertices of a vertex before visiting neighboring vertices to the adjacent
 vertices. This means that vertices with the same distance from the starting vertex are visited before vertices 
 further away from the starting vertex are visited.

How it works:

Put the starting vertex into the queue.
For each vertex taken from the queue, visit the vertex, then put all unvisited adjacent vertices into the queue.
Continue as long as there are vertices in the queue.
Run the animation below to see how Breadth First Search (BFS) traversal runs on a specific Graph, starting in vertex D.

F
B
C
A
E
D
G
Result:

BFS Traverse from D
As you can see in the animation above, BFS traversal visits vertices the same distance from the starting vertex, 
before visiting vertices further away. So for example, after visiting vertex A, vertex E and C are visited before
 visiting B, F and G because those vertices are further away.

Breadth First Search traversal works this way by putting all adjacent vertices in a queue (if they are not already
 visited), and then using the queue to visit the next vertex.

This code example for Breadth First Search traversal is the same as for the Depth First Search code example above,
 except for the bfs() method:


"""


def bfs(self, start_vertex_data):
    queue = [self.vertex_data.index(start_vertex_data)]
    visited = [False] * self.size
    visited[queue[0]] = True

    while queue:
        current_vertex = queue.pop(0)
        print(self.vertex_data[current_vertex], end=' ')

        for i in range(self.size):
            if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True



"""
Line 2-4: The bfs() method starts by creating a queue with the start vertex inside, creating a visited array, and setting the start vertex as visited.

Line 6-13: The BFS traversal works by taking a vertex from the queue, printing it, and adding adjacent vertices to the queue if they are not visited yet, and then continue to take vertices from the queue in this way. The traversal finishes when the last element in the queue has no unvisited adjacent vertices.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Introduction

Unmute
Duration 
2:49
/
Current Time 
0:03

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Next
Stay
Brand logo

DFS and BFS Traversal of a Directed Graph
Depth first and breadth first traversals can actually be implemented to work on directed Graphs (instead of undirected) with just very few changes.

Run the animation below to see how a directed Graph can be traversed using DFS or BFS.

F
B
C
A
E
D
G
Result:

 BFS
 DFS

Traverse from D
To go from traversing a directed Graph instead of an undirected Graph, we just need to remove the last line in the add_edge() method:
"""
def add_edge(self, u, v):
    if 0 <= u < self.size and 0 <= v < self.size:
        self.adj_matrix[u][v] = 1
        #self.adj_matrix[v][u] = 1

"""
We must also take care when we build our Graph because the edges are now directed.

The code example below contains both BFS and DFS traversal of the directed Graph from the animation above:

Example
Python:
"""
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            #self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
            
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size

        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)
        
    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
        
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=' ')
            
            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D -> A
g.add_edge(3, 4)  # D -> E
g.add_edge(4, 0)  # E -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 5)  # C -> F
g.add_edge(2, 6)  # C -> G
g.add_edge(5, 1)  # F -> B
g.add_edge(1, 2)  # B -> C

g.print_graph()

print("\nDepth First Search starting from vertex D:")
g.dfs('D')

print("\n\nBreadth First Search starting from vertex D:")
g.bfs('D')

"""
Now that we have looked at two basic algorithms for how to traverse Graphs, we will use the next pages to see 
how other algorithms can run on the Graph data structure.

"""
"""
DSA Graphs Cycle Detection
Cycles in Graphs
A cycle in a Graph is a path that starts and ends at the same vertex, where no edges are repeated. It is similar to walking through a maze and ending up exactly where you started.

F
B
C
A
E
D
G
Is cyclic:

DFS Cycle Detection
A cycle can be defined slightly different depending on the situation. A self-loop for example, where an edge goes from and to the same vertex, might or might not be considered a cycle, depending on the problem you are trying to solve.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Introduction

Unmute
Duration 
2:49
/
Current Time 
0:00

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Brand logo

Cycle Detection
It is important to be able to detect cycles in Graphs because cycles can indicate problems or special conditions in many applications like networking, scheduling, and circuit design.

The two most common ways to detect cycles are:

Depth First Search (DFS): DFS traversal explores the Graph and marks vertices as visited. A cycle is detected when the current vertex has an adjacent vertex that has already been visited.
Union-Find: This works by initially defining each vertex as a group, or a subset. Then these groups are joined for every edge. Whenever a new edge is explored, a cycle is detected if two vertices already belong to the same group.
How cycle detection with DFS and Union-Find work, and how they are implemented, are explained in more detail below.

DFS Cycle Detection for Undirected Graphs
To detect cycles in an undirected Graph using Depth First Search (DFS), we use a code very similar to the DFS traversal code on the previous page, with just a few changes.

How it works:

Start DFS traversal on each unvisited vertex (in case the Graph is not connected).
During DFS, mark vertices as visited, and run DFS on the adjacent vertices (recursively).
If an adjacent vertex is already visited and is not the parent of the current vertex, a cycle is detected, and True is returned.
If DFS traversal is done on all vertices and no cycles are detected, False is returned.
Run the animation below to see how DFS cycle detection runs on a specific Graph, starting in vertex A (this is the same as the previous animation).

F
B
C
A
E
D
G
Is cyclic:

DFS Cycle Detection
The DFS traversal starts in vertex A because that is the first vertex in the adjacency matrix. Then, for every new vertex visited, the traversal method is called recursively on all adjacent vertices that have not been visited yet. The cycle is detected when vertex F is visited, and it is discovered that the adjacent vertex C has already been visited.

Example
Python:
"""
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def dfs_util(self, v, visited, parent):
        visited[v] = True

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, v):
                        return True
                elif parent != i:
                    return True
        return False

    def is_cyclic(self):
        visited = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                if self.dfs_util(i, visited, -1):
                    return True
        return False

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

print("\nGraph has cycle:", g.is_cyclic())

"""
Line 66: The DFS cycle detection starts when the is_cyclic() method is called.

Line 37: The visited array is first set to false for all vertices, because no vertices are visited yet at this point.

Line 38-42: DFS cycle detection is run on all vertices in the Graph. This is to make sure all vertices are visited in case the Graph is not connected. If a node is already visited, there must be a cycle, and True is returned. If all nodes are visited just ones, which means no cycles are detected, False is returned.

Line 24-34: This is the part of the DFS cycle detection that visits a vertex, and then visits adjacent vertices recursively. A cycle is detected and True is returned if an adjacent vertex has already been visited, and it is not the parent node.

DFS Cycle Detection for Directed Graphs
To detect cycles in Graphs that are directed, the algorithm is still very similar as for undirected Graphs, but the code must be modified a little bit because for a directed Graph, if we come to an adjacent node that has already been visited, it does not necessarily mean that there is a cycle.

Just consider the following Graph where two paths are explored, trying to detect a cycle:

1
2
C
B
D
A
In path 1, the first path to be explored, vertices A->B->C are visited, no cycles detected.

In the second path to be explored (path 2), vertices D->B->C are visited, and the path has no cycles, right? But without changes in our program, a false cycle would actually be detected when going from D to the adjacent vertex B, because B has already been visited in path 1. To avoid such false detections, the code is modified to detect cycles only in case a node has been visited before in the same path.

F
B
C
A
E
D
G
Is cyclic:

DFS Cycle Detection
To implement DFS cycle detection on a directed Graph, like in the animation above, we need to remove the symmetry we have in the adjacency matrix for undirected Graphs. We also need to use a recStack array to keep track of visited vertices in the current recursive path.

Example
Python:
"""
class Graph:
    # ......
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    # ......
    def dfs_util(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        print("Current vertex:",self.vertex_data[v])

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, recStack):
                        return True
                elif recStack[i]:
                    return True

        recStack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.size
        recStack = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                print() #new line
                if self.dfs_util(i, visited, recStack):
                    return True
        return False

g = Graph(7)

# ......

g.add_edge(3, 0)  # D -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 1)  # C -> B
g.add_edge(2, 4)  # C -> E
g.add_edge(1, 5)  # B -> F
g.add_edge(4, 0)  # E -> A
g.add_edge(2, 6)  # C -> G

g.print_graph()

print("Graph has cycle:", g.is_cyclic())

"""
Line 6: This line is removed because it is only applicable for undirected Graphs.

Line 26: The recStack array keeps an overview over which vertices have been visited during a recursive exploration of a path.

Line 14-19: For every adjacent vertex not visited before, do a recursive DFS cycle detection. If an adjacent vertex has been visited before, also in the same recursive path (line 13), a cycle has been found, and True is returned.

Union-Find Cycle Detection
Detecting cycles using Union-Find is very different from using Depth First Search.

Union-Find cycle detection works by first putting each node in its own subset (like a bag or container). Then, for every edge, the subsets belonging to each vertex are merged. For an edge, if the vertices already belong to the same subset, it means that we have found a cycle.

F
E
D
A
C
B
G
Is cyclic:

Union-Find Cycle Detection
In the animation above, Union-Find cycle detection explores the edges in the Graph. As edges are explored, the subset of vertex A grows to also include vertices B, C, and D. The cycle is detected when the edge between A and D is explored, and it is discovered that both A and D already belong to the same subset.

The edges between D, E, and F also construct a circle, but this circle is not detected because the algorithm stops (returns True) when the first circle is detected.

Union-Find cycle detection is only applicable for Graphs that are undirected.

Union-Find cycle detection is implemented using the adjacency matrix representation, so setting up the Graph structure with vertices and edges is basically the same as in previous examples.

Example
Python:
"""
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.parent = [i for i in range(size)]  # Union-Find array

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        print('Union:',self.vertex_data[x],'+',self.vertex_data[y])
        self.parent[x_root] = y_root
        print(self.parent,'\n')

    def is_cyclic(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.adj_matrix[i][j]:
                    x = self.find(i)
                    y = self.find(j)
                    if x == y:
                        return True
                    self.union(x, y)
        return False

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(1, 0)  # B - A
g.add_edge(0, 3)  # A - D
g.add_edge(0, 2)  # A - C
g.add_edge(2, 3)  # C - D
g.add_edge(3, 4)  # D - E
g.add_edge(3, 5)  # D - F
g.add_edge(3, 6)  # D - G
g.add_edge(4, 5)  # E - F

print("Graph has cycle:", g.is_cyclic())
"""
Line 6: The parent array contains the root vertex for every subset. This is used to detect a cycle by checking if two vertices on either side of an edge already belong to the same subset.

Line 17: The find method finds the root of the set that the given vertex belongs to.

Line 22: The union method combines two subsets.

Line 29: The is_cyclic method uses the find method to detect a cycle if two vertices x and y are already in the same subset. If a cycle is not detected, the union method is used to combine the subsets.




"""







