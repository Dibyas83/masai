
"""
Yes, a graph can be represented using both an adjacency matrix and an adjacency list. An adjacency matrix is a 2D array where each element represents the presence or absence of an edge between two vertices. An adjacency list is a collection of lists, where each list corresponds to a vertex and contains its adjacent vertices.
Adjacency Matrix:
Representation:
A square matrix where rows and columns represent vertices. An entry (i, j) is 1 if there's an edge from vertex i to j, and 0 otherwise.
Suitable for:
Dense graphs (many edges) where checking for the existence of an edge is a common operation.
Pros:
Efficient for checking if an edge exists (constant time), easy to implement.
Cons:
Can be space-inefficient for sparse graphs (few edges), since it stores all possible edges even if they don't exist.
Adjacency List:
Representation:
An array (or vector) of linked lists. Each element of the array corresponds to a vertex, and its linked list contains the vertices that are adjacent to it.
Suitable for:
Sparse graphs where there are relatively few edges.
Pros:
Space-efficient for sparse graphs, as it only stores existing edges. Efficient for finding neighbors of a vertex.
Cons:
Checking if an edge exists between two vertices can be slower (linear time in the number of neighbors of the vertex) compared to an adjacency matrix.

Edge Lists
Now that we're all caught up on the fundamentals of graphs, let's talk implementation!

The first implementation strategy is called an edge list. An edge list is a list or array of all the edges in a graph. Edge lists are one of the easier representations of a graph.

In this implementation, the underlying data structure for keeping track of all the nodes and edges is a single list of pairs. Each pair represents a single edge and is comprised of the two unique IDs of the nodes involved. Each line/edge in the graph gets an entry in the edge list, and that single data structure then encodes all nodes and relationships.

Edge Lists
In the graph above, we have three nodes: 1, 2, and 3. Each edge is given an index and represents a reference from one node to another. There isn't any particular order to the edges as they appear in the edge list, but every edge must be represented. For this example, the edge list would look like the attached snippet:

cpp
go
java
javascript
python
edge_list = [
	[1,2],
	[2,3],
	[3,1]
]
Due to the fact that an edge list is really just an array, the only way to find something in this array is by iterating through it.

For example, if we wanted to see if vertex 1 was connected to vertex 2, we'd need to iterate through the previous array and look for the existence of a pair [1,2] or [2,1].

This is fine for this specific graph since it only has three vertices and three edges. But as you can imagine, having to iterate through a much larger array would increase complexity.

Checking to see if a particular edge existed in a large array isn't guaranteed to have a sense of order, and the edge could be at the very end of the list. Additionally, there may not be any edge at all, and we'd still have to iterate through the whole thing to check for it. This would take linear time, O(E) (E being the number of edges) to get it done.

Please find the implementation of an edge list attached.

class Node:
    def __init__(self, name):
        self.name = name
        self.edge_list = []

    def get_name(self):
        return self.name

    def get_edges(self):
        return self.edge_list

class Edge:
    def __init__(self, dest, weight=1):
        self.dest_vertex = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_dest_vertex(self):
        return self.dest_vertex

class Graph:
    def __init__(self):
        self.nodes = set()

    def add_edge(self, v1, v2, weight):
        return v1.get_edges().append(Edge(v2, weight)) and v2.get_edges().append(Edge(v1, weight))

    def add_vertex(self, v):
        return self.nodes.add(v)

    def print_graph(self):
        for v in self.nodes:
            print("vertex name:", v.get_name())
            for e in v.get_edges():
                print("destVertex:", e.get_dest_vertex().get_name(), ", weight:", e.get_weight())
            print()

our_graph = Graph()

# nodes
v0 = Node("0")
v1 = Node("1")
v2 = Node("2")
v3 = Node("3")

our_graph.add_vertex(v0)
our_graph.add_vertex(v1)
our_graph.add_vertex(v2)
our_graph.add_vertex(v3)

# edges
our_graph.add_edge(v0, v1, 2)
our_graph.add_edge(v1, v2, 3)
our_graph.add_edge(v2, v0, 1)
our_graph.add_edge(v2, v3, 1)
our_graph.add_edge(v3, v2, 4)

our_graph.print_graph()

Edge List:
A list of tuples, where each tuple represents an edge and contains the two vertices it connects.
Space complexity is O(E).
Choice of Representation:
Adjacency Matrix:
Suitable for dense graphs (many edges) and when checking for the existence of an edge between two vertices is frequently needed, as this can be done in constant time.
Adjacency List:
Suitable for sparse graphs (few edges) and when finding the neighbors of a vertex is a common operation, as this can be done by iterating through the list.
Edge List:
Suitable for graphs with a small number of edges and when the main operations involve iterating through all edges, as it can be done efficiently.


Adjacency Matrix
While an edge list won't end up being the most efficient choice, we can move beyond a list and implement a matrix. For many, a matrix is a significantly better kinesthetic representation for a graph.

An adjacency matrix is a matrix that represents exactly which vertices/nodes in a graph have edges between them. It serves as a lookup table, where a value of 1 represents an edge that exists and a 0 represents an edge that does not exist. The indices of the matrix model the nodes.

Once we've determined the two nodes that we want to find an edge between, we look at the value at the intersection of those two nodes to determine whether there's a link.

Adjacency Matrix
In this illustration, we can see that the adjacency matrix has a chain of cells with value 0 diagonally. In fact, this is true of most graphs that we'll deal with, as most won't be self-referential. In other words, since node 2 does not (or can not) have a link to itself, if we were to draw a line from column 2 to row 2, the value will be 0.

However, if we wanted to see if node 3 was connected to node 1, we'd find there to be a relationship. We could find column 3, row 1, and see that the value is 1, which means that there is an edge between these two nodes.

Adjacency matrices are easy to follow and represent. Looking up, inserting and removing an edge can all be done in O(1) or constant time. However, they do have a downfall, which is that they can take up more space than is necessary. An adjacency matrix always consumes O(V^2) (V being vertices) amount of space.

Nevertheless, adjacency matrices are definitely a step up from an edge list. Their representation would look like this:

 RUN CODE
RESET
PYTHON
1
matrix = [
2
  [0, 1, 1],
3
  [1, 0, 1],
4
  [1, 1, 0]
5
]
Build your intuition. Fill in the missing part by typing it in.
The function below returns an object for the specified vertex. Fill in the missing snippet for the method.

# Original code in Java
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[False] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, i, j):
        self.adj_matrix[i][j] = True
        self.adj_matrix[j][i] = True

    def remove_edge(self, i, j):
        self.adj_matrix[i][j] = False
        self.adj_matrix[j][i] = False

    def __str__(self):
        s = ""
        for i in range(self.num_vertices):
            s += str(i) + ": "
            s += " ".join(["1" if j else "0" for j in self.adj_matrix[i]]) + "\n"
        return s


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

print(g)

Adjacency Lists
Let's say both edge lists and adjacency matrices seem to fail our requirements, what do we do? Well, we combine them together and create a hybrid implementation!

This is what an adjacency list is-- a hybrid between an adjacency matrix and an edge list. An adjacency list is an array of linked lists that serves the purpose of representing a graph. What makes it unique is that its shape also makes it easy to see which vertices are adjacent to any other vertices. Each vertex in a graph can easily reference its neighbors through a linked list.

Due to this, an adjacency list is the most common representation of a graph. Another reason is that graph traversal problems often require us to be able to easily figure out which nodes are the neighbors of another node. In most graph traversal interview problems, we don't really need to build the entire graph. Rather, it's important to know where we can travel (or in other words, who the neighbors of a node are).

Implementation of an Adjacency List
In this illustration, each vertex is given an index in its list. The list has all of its neighboring vertices stored as a linked list (can also be an array) adjacent to it.

For example, the last element in the list is the vertex 3, which has a pointer to a linked list of its neighbors. The list that is adjacent to vertex 3 contains references to two other vertices (1 and 2), which are the two nodes that are connected to the node 3.

Thus, just by looking up the node 3, we can quickly determine who its neighbors are and, by proxy, realize that it has two edges connected to it.

This all results from the structure of an adjacency list making it easy to determine all the neighbors of one particular vertex. In fact, retrieving one node's neighbors takes constant or O(1) time, since all we need to do is find the index of the node we're looking for and pull out its list of adjacent vertices.

Please see the implementation of adjacency list attached.

# Class representing a simple graph using an edge list converted to adjacency list
class Graph:
    # Basic constructor method
    def __init__(self, edge_list, num_of_nodes):
        # Convert edge list to adjacency list,
        # represented with a multi-dimensional array
        self.adjacency_list = [[] for _ in range(num_of_nodes)]

        # Add edges to corresponding nodes of the graph
        for (origin, dest) in edge_list:
            self.adjacency_list[origin].append(dest)


# Helper method to print adjacency list representation
def print_graph(graph):
    for origin in range(len(graph.adjacency_list)):
        # print current vertex and all its neighboring vertices
        for dest in graph.adjacency_list[origin]:
            print(f'{origin} —> {dest} ', end='')
        print()


if __name__ == '__main__':
    # Set up an edge list and number of nodes
    edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4)]
    num_of_nodes = 6

    graph = Graph(edge_list, num_of_nodes)
    print_graph(graph)

One Pager Cheat Sheet

The graph data structure, though often intimidating to students, is a crucial tool for modeling information, allowing for complex abilities like social networking, and is used by companies like LinkedIn and Google to understand networks and relationships through various graph algorithms.
A graph is a programmatic representation of connected things or entities, which uses nodes (dots) to represent items and connections (lines) between them known as edges, allowing us to model and document structures or relationships, such as those in social networks or internet web pages.
In graph terminology, dots are referred to as nodes or vertices, lines are called edges, and the graph itself is a data structure representing relationships; edges can be ordered or unordered depending on if the graph is directed or undirected, and may have weights signifying the link strength between vertices.
A graph in computer science and mathematics consists of two essential components, nodes/vertices representing distinct entities, and edges depicting the relationships or interactions between these entities, with attributes like direction and weight indicating specific aspects of these relationships.
The concept of a social network can be modeled as a graph, where users are represented as vertices and friendship relations are represented as edges, as demonstrated with a graph containing Peter, Kevin, Jake, and Daniel.
Undirected graphs represent two-way relationships with edges that can be traversed in both directions, while directed graphs represent one-way relations with edges that can be traversed in a single direction.
In graph theory, there are two types of graphs: undirected graphs, which represent two-way relationships and can be traversed in both directions, and directed graphs, which represent one-way relationships and can only be traversed in one direction.
The applications of graphs include finding the shortest path, finding the best starting point, breadth-first and depth-first traversal, searching, inserting, deleting from a tree or linked list, graph classification, finding missing relationships through link prediction, and node classification.
The statement affirms that breadth-first and depth-first traversals are search algorithms used for navigating 'tree' and 'graph' data structures in a horizontal and vertical manner respectively.
An edge list is an implementation strategy for graphs where all the edges are stored in a single list of pairs, each pair representing an edge through the two unique IDs of the nodes involved.
To find something in an edge list, an array-like data structure, one needs to iterate through it which is a linear time operation (O(E)), leading to increased complexity in the case of larger arrays.
An adjacency matrix is a type of matrix used to represent the vertices/nodes and connection/links in a graph, where 1 indicates an existing edge and 0 indicates a non-existing one, enabling lookup, insertion, and removal of an edge in O(1) or constant time, but consumes O(V^2) space, where V is the number of vertices.
The get() method, used in the context of the adjacency matrix graph representation, takes an index as a parameter to return the vertex at that particular index in the vertices list, representing each vertex or node in the graph as a list.
This provides a complete implementation of an adjacency matrix.
The toString() method in Java, overridden in the Matrix class definition, creates a readable string representation of an object by returning a String that contains all attributes of the object, such as the size and values of a matrix, thereby providing an efficient way to view all data related to the object.
An adjacency list is a hybrid of an edge list and an adjacency matrix, serving as the most common representation of a graph due to its linked list structure that makes it easy to identify neighboring vertices, which is crucial for graph traversal problems.
The illustration depicts an adjacency list where each vertex has an index in its list with neighboring vertices stored as a linked list or array, enabling quick determination of a node's neighbors and their connections, taking a constant or O(1) time to retrieve.
Understanding the basics of implementing graphs is fundamental to solving complex computer science problems, since graphs are likely utilized in any complex computation.

"""
"""
geeeks

Graph and its representations
Last Updated : 05 Oct, 2024
A Graph is a non-linear data structure consisting of vertices and edges. The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(V, E).

Representations of Graph
Here are the two most common ways to represent a graph : For simplicity, we are going to consider only unweighted graphs in this post.

Adjacency Matrix
Adjacency List
Adjacency Matrix Representation
An adjacency matrix is a way of representing a graph as a matrix of boolean (0's and 1's)

Let's assume there are n vertices in the graph So, create a 2D matrix adjMat[n][n] having dimension n x n.

If there is an edge from vertex i to j, mark adjMat[i][j] as 1. 
If there is no edge from vertex i to j, mark adjMat[i][j] as 0.
Representation of Undirected Graph as Adjacency Matrix:
The below figure shows an undirected graph. Initially, the entire Matrix is ​​initialized to 0. If there is an edge from source to destination, we insert 1 to both cases (adjMat[source][destination] and adjMat[destination][source]) because we can go either way.

Undirected_to_Adjacency_matrix
Undirected Graph to Adjacency Matrix



1
def add_edge(mat, i, j):
2
  
3
    # Add an edge between two vertices
4
    mat[i][j] = 1  # Graph is 
5
    mat[j][i] = 1  # Undirected
6
​
7
def display_matrix(mat):
8
  
9
    # Display the adjacency matrix
10
    for row in mat:
11
        print(" ".join(map(str, row)))  
12
​
13
# Main function to run the program
14
if __name__ == "__main__":
15
    V = 4  # Number of vertices
16
    mat = [[0] * V for _ in range(V)]  
17
​
18
    # Add edges to the graph
19
    add_edge(mat, 0, 1)
20
    add_edge(mat, 0, 2)
21
    add_edge(mat, 1, 2)
22
    add_edge(mat, 2, 3)
23
​
24
    # Optionally, initialize matrix directly
25
    """
26
    mat = [
27
        [0, 1, 0, 0],
28
        [1, 0, 1, 0],
29
        [0, 1, 0, 1],
30
        [0, 0, 1, 0]
31
    ]
32
    """
33
​
34
    # Display adjacency matrix
35
    print("Adjacency Matrix:")
36
    display_matrix(mat)

Output
Adjacency Matrix Representation
0 1 1 0 
1 0 1 0 
1 1 0 1 
0 0 1 0 
Representation of Directed Graph as Adjacency Matrix:
The below figure shows a directed graph. Initially, the entire Matrix is ​​initialized to 0. If there is an edge from source to destination, we insert 1 for that particular adjMat[source][destination].

Directed_to_Adjacency_matrix
Directed Graph to Adjacency Matrix
Adjacency List Representation
An array of Lists is used to store edges between two vertices. The size of array is equal to the number of vertices (i.e, n). Each index in this array represents a specific vertex in the graph. The entry at the index i of the array contains a linked list containing the vertices that are adjacent to vertex i.

Let's assume there are n vertices in the graph So, create an array of list of size n as adjList[n].

adjList[0] will have all the nodes which are connected (neighbour) to vertex 0.
adjList[1] will have all the nodes which are connected (neighbour) to vertex 1 and so on.
Representation of Undirected Graph as Adjacency list:
The below undirected graph has 3 vertices. So, an array of list will be created of size 3, where each indices represent the vertices. Now, vertex 0 has two neighbours (i.e, 1 and 2). So, insert vertex 1 and 2 at indices 0 of array. Similarly, For vertex 1, it has two neighbour (i.e, 2 and 0) So, insert vertices 2 and 0 at indices 1 of array. Similarly, for vertex 2, insert its neighbours in array of list.

Graph-Representation-of-Undirected-graph-to-Adjacency-List
Undirected Graph to Adjacency list



1
def add_edge(adj, i, j):
2
    adj[i].append(j)
3
    adj[j].append(i)  # Undirected
4
​
5
def display_adj_list(adj):
6
    for i in range(len(adj)):
7
        print(f"{i}: ", end="")
8
        for j in adj[i]:
9
            print(j, end=" ")
10
        print()
11
​
12
# Create a graph with 4 vertices and no edges
13
V = 4
14
adj = [[] for _ in range(V)]
15
​
16
# Now add edges one by one
17
add_edge(adj, 0, 1)
18
add_edge(adj, 0, 2)
19
add_edge(adj, 1, 2)
20
add_edge(adj, 2, 3)
21
​
22
print("Adjacency List Representation:")
23
display_adj_list(adj)

Output
Adjacency List Representation:
0: 1 2 
1: 0 2 
2: 0 1 3 
3: 2 
Representation of Directed Graph as Adjacency list:
The below directed graph has 3 vertices. So, an array of list will be created of size 3, where each 
indices represent the vertices. Now, vertex 0 has no neighbours. For vertex 1, it has two neighbour 
(i.e, 0 and 2) So, insert vertices 0 and 2 at indices 1 of array. Similarly, for vertex 2, insert its 
neighbours in array of list.

Graph-Representation-of-Directed-graph-to-Adjacency-List

"""











