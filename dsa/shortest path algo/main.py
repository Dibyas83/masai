
"""
DSA Shortest Path
The Shortest Path Problem
The shortest path problem is famous in the field of computer science.

To solve the shortest path problem means to find the shortest possible route or path between two
vertices (or nodes) in a Graph.

In the shortest path problem, a Graph can represent anything from a road network to a communication
 network, where the vertices can be intersections, cities, or routers, and the edges can be roads,
  flight paths, or data links.

F
2
4
3
4
5
2
B
C
5
5
3
A
4
4
E
D
G
The shortest path from vertex D to vertex F in the Graph above is D->E->C->F, with a total path
weight of 2+4+4=10. Other paths from D to F are also possible, but they have a higher total weight
, so they can not be considered to be the shortest path.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Where to

Unmute
Duration
2:00
/
Current Time
0:00

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Brand logo

Solutions to The Shortest Path Problem
Dijkstra's algorithm and the Bellman-Ford algorithm find the shortest path from one start vertex,
to all other vertices.

To solve the shortest path problem means to check the edges inside the Graph until we find a path
where we can move from one vertex to another using the lowest possible combined weight along the
edges.

This sum of weights along the edges that make up a path is called a path cost or a path weight.

Algorithms that find the shortest paths, like Dijkstra's algorithm or the Bellman-Ford algorithm
, find the shortest paths from one start vertex to all other vertices.

To begin with, the algorithms set the distance from the start vertex to all vertices to be
infinitely long. And as the algorithms run, edges between the vertices are checked over and over,
 and shorter paths might be found many times until the shortest paths are found at the end.

Every time an edge is checked and it leads to a shorter distance to a vertex being found and
 updated, it is called a relaxation, or relaxing an edge.

Positive and Negative Edge Weights
Some algorithms that find the shortest paths, like Dijkstra's algorithm, can only find the
shortest paths in graphs where all the edges are positive. Such graphs with positive distances
 are also the easiest to understand because we can think of the edges between vertices as
 distances between locations.

4
3
3
3
B
C
2
3
4
7
5
A
E
D
If we interpret the edge weights as money lost by going from one vertex to another, a positive
edge weight of 4 from vertex A to C in the graph above means that we must spend $4 to go from A
to C.

But graphs can also have negative edges, and for such graphs the Bellman-Ford algorithm can be
used to find the shortest paths.

4
-3
3
3
B
C
-4
2
4
7
5
A
E
D
And similarly, if the edge weights represent money lost, the negative edge weight -3 from vertex
 C to A in the graph above can be understood as an edge where there is more money to be made than
  money lost by going from C to A. So if for example the cost of fuel is $5 going from C to A,
  and we get paid $8 for picking up packages in C and delivering them in A, money lost is -3,
  meaning we are actually earning $3 in total.

ADVERTISEMENT

Negative Cycles in Shortest Path Problems
Finding the shortest paths becomes impossible if a graph has negative cycles.

Having a negative cycle means that there is a path where you can go in circles, and the edges
that make up this circle have a total path weight that is negative.

In the graph below, the path A->E->B->C->A is a negative cycle because the total path weight is
5+2-4-4=-1.

5
-4
3
3
B
5
C
1
-4
2
4
7
5
A
-2
E
3
D
0
The reason why it is impossible to find the shortest paths in a graph with negative cycles is
 that it will always be possible to continue running an algorithm to find even shorter paths.

Let's say for example that we are looking for the shortest distance from vertex D in graph above,
 to all other vertices. At first we find the distance from D to E to be 3, by just walking the
 edge D->E. But after this, if we walk one round in the negative cycle E->B->C->A->E, then the
 distance to E becomes 2. After walking one more round the distance becomes 1, which is even s
 horter, and so on. We can always walk one more round in the negative cycle to find a shorter
 distance to E, which means the shortest distance can never be found.

Luckily, the the Bellman-Ford algorithm, that runs on graphs with negative edges, can be implemented
 with detection for negative cycles.

"""


"""

DSA Dijkstra's Algorithm
Dijkstra's shortest path algorithm was invented in 1956 by the Dutch computer scientist Edsger W. Dijkstra during a twenty minutes coffee break, while out shopping with his fiancée in Amsterdam.

The reason for inventing the algorithm was to test a new computer called ARMAC.

Dijkstra's Algorithm
Dijkstra's algorithm finds the shortest path from one vertex to all other vertices.

It does so by repeatedly selecting the nearest unvisited vertex and calculating the distance to all the unvisited neighboring vertices.


Run Dijkstra's
Dijkstra's algorithm is often considered to be the most straightforward algorithm for solving the shortest path problem.

Dijkstra's algorithm is used for solving single-source shortest path problems for directed or undirected paths. Single-source means that one vertex is chosen to be the start, and the algorithm will find the shortest path from that vertex to all other vertices.

Dijkstra's algorithm does not work for graphs with negative edges. For graphs with negative edges, the Bellman-Ford algorithm that is described on the next page, can be used instead.

To find the shortest path, Dijkstra's algorithm needs to know which vertex is the source, it needs a way to mark vertices as visited, and it needs an overview of the current shortest distance to each vertex as it works its way through the graph, updating these distances when a shorter distance is found.

How it works:

Set initial distances for all vertices: 0 for the source vertex, and infinity for all the other.
Choose the unvisited vertex with the shortest distance from the start to be the current vertex. So the algorithm will always start with the source as the current vertex.
For each of the current vertex's unvisited neighbor vertices, calculate the distance from the source and update the distance if the new, calculated, distance is lower.
We are now done with the current vertex, so we mark it as visited. A visited vertex is not checked again.
Go back to step 2 to choose a new current vertex, and keep repeating these steps until all vertices are visited.
In the end we are left with the shortest path from the source vertex to every other vertex in the graph.
In the animation above, when a vertex is marked as visited, the vertex and its edges become faded to indicate that Dijkstra's algorithm is now done with that vertex, and will not visit it again.

Note: This basic version of Dijkstra's algorithm gives us the value of the shortest path cost to every vertex, but not what the actual path is. So for example, in the animation above, we get the shortest path cost value 10 to vertex F, but the algorithm does not give us which vertices (D->E->C->D->F) that make up this shortest path. We will add this functionality further down here on this page.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Comments

Unmute
Duration 
2:14
/
Current Time 
0:00

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Brand logo

A Detailed Dijkstra Simulation
Run the simulation below to get a more detailed understanding of how Dijkstra's algorithm runs on a specific graph, finding the shortest distances from vertex D.

inf
F
2
5
5
3
inf
B
inf
C
5
5
2
2
inf
A
4
4
4
inf
E
0
D
inf
G
2
2
5
5
4
4
2
2
6
6
8
2
Play
Reset
This simulation shows how distances are calculated from vertex D to all other vertices, by always choosing the next vertex to be the closest unvisited vertex from the starting point.

Follow the step-by-step description below to get all the details of how Dijkstra's algorithm calculates the shortest distances.

ADVERTISEMENT

Manual Run Through
Consider the Graph below.

F
2
5
3
4
5
2
B
C
5
5
2
A
4
4
E
D
G
We want to find the shortest path from the source vertex D to all other vertices, so that for example the shortest path to C is D->E->C, with path weight 2+4=6.

To find the shortest path, Dijkstra's algorithm uses an array with the distances to all other vertices, and initially sets these distances to infinite, or a very big number. And the distance to the vertex we start from (the source) is set to 0.

distances = [inf, inf, inf, 0, inf, inf, inf]
#vertices   [ A ,  B ,  C , D,  E ,  F ,  G ]
The image below shows the initial infinite distances to other vertices from the starting vertex D. The distance value for vertex D is 0 because that is the starting point.

inf
F
2
5
3
4
5
2
inf
B
inf
C
5
5
2
inf
A
4
4
inf
E
0
D
inf
G
Dijkstra's algorithm then sets vertex D as the current vertex, and looks at the distance to the adjacent vertices. Since the initial distance to vertices A and E is infinite, the new distance to these are updated with the edge weights. So vertex A gets the distance changed from inf to 4, and vertex E gets the distance changed to 2. As mentioned on the previous page, updating the distance values in this way is called 'relaxing'.

inf
F
2
5
3
4
5
2
inf
B
inf
C
5
5
2
4
A
4
4
2
E
0
D
inf
G
After relaxing vertices A and E, vertex D is considered visited, and will not be visited again.

The next vertex to be chosen as the current vertex must the vertex with the shortest distance to the source vertex (vertex D), among the previously unvisited vertices. Vertex E is therefore chosen as the current vertex after vertex D.

inf
F
2
5
3
4
5
2
inf
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
The distance to all adjacent and not previously visited vertices from vertex E must now be calculated, and updated if needed.

The calculated distance from D to vertex A, via E, is 2+4=6. But the current distance to vertex A is already 4, which is lower, so the distance to vertex A is not updated.

The distance to vertex C is calculated to be 2+4=6, which is less than infinity, so the distance to vertex C is updated.

Similarly, the distance to node G is calculated and updated to be 2+5=7.

The next vertex to be visited is vertex A because it has the shortest distance from D of all the unvisited vertices.

inf
F
2
5
3
4
5
2
inf
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
The calculated distance to vertex C, via A, is 4+3=7, which is higher than the already set distance to vertex C, so the distance to vertex C is not updated.

Vertex A is now marked as visited, and the next current vertex is vertex C because that has the lowest distance from vertex D between the remaining unvisited vertices.

11
F
2
5
3
4
5
2
8
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
Vertex F gets updated distance 6+5=11, and vertex B gets updated distance 6+2=8.

Calculated distance to vertex G via vertex C is 6+5=11 which is higher than the already set distance of 7, so distance to vertex G is not updated.

Vertex C is marked as visited, and the next vertex to be visited is G because is has the lowest distance between the remaining unvisited vertices.

11
F
2
5
3
4
5
2
8
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
Vertex F already has a distance of 11. This is lower than the calculated distance from G, which is 7+5=12, so the distance to vertex F is not updated.

Vertex G is marked as visited, and B becomes the current vertex because it has the lowest distance of the remaining unvisited vertices.

10
F
2
5
3
4
5
2
8
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
The new distance to F via B is 8+2=10, because it is lower than F's existing distance of 11.

Vertex B is marked as visited, and there is nothing to check for the last unvisited vertex F, so Dijkstra's algorithm is finished.

Every vertex has been visited only once, and the result is the lowest distance from the source vertex D to every other vertex in the graph.

Implementation of Dijkstra's Algorithm
To implement Dijkstra's algorithm, we create a Graph class. The Graph represents the graph with its vertices and edges:

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
Line 3: We create the adj_matrix to hold all the edges and edge weights. Initial values are set to 0.

Line 4: size is the number of vertices in the graph.

Line 5: The vertex_data holds the names of all the vertices.

Line 7-10: The add_edge method is used to add an edge from vertex u to vertex v, with edge weight weight.

Line 12-14: The add_vertex_data method is used to add a vertex to the graph. The index where the vertex should belong is given with the vertex argument, and data is the name of the vertex.

The Graph class also contains the method that runs Dijkstra's algorithm:

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances
Line 18-19: The initial distance is set to infinity for all vertices in the distances array, except for the start vertex, where the distance is 0.

Line 20: All vertices are initially set to False to mark them as not visited in the visited array.

Line 23-28: The next current vertex is found. Outgoing edges from this vertex will be checked to see if shorter distances can be found. It is the unvisited vertex with the lowest distance from the start.

Line 30-31: If the next current vertex has not been found, the algorithm is finished. This means that all vertices that are reachable from the source have been visited.

Line 33: The current vertex is set as visited before relaxing adjacent vertices. This is more effective because we avoid checking the distance to the current vertex itself.

Line 35-39: Distances are calculated for not visited adjacent vertices, and updated if the new calculated distance is lower.

After defining the Graph class, the vertices and edges must be defined to initialize the specific graph, and the complete code for this Dijkstra's algorithm example looks like this:

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

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

# Dijkstra's algorithm from D to all vertices
print("\nDijkstra's Algorithm starting from vertex D:")
distances = g.dijkstra('D')
for i, d in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[i]}: {d}")
ADVERTISEMENT

Dijkstra's Algorithm on Directed Graphs
To run Dijkstra's algorithm on directed graphs, very few changes are needed.

Similarly to the change we needed for cycle detection for directed graphs, we just need to remove one line of code so that the adjacency matrix is not symmetric anymore.

Let's implement this directed graph and run Dijkstra's algorithm from vertex D.

inf
F
2
5
3
4
5
2
inf
B
inf
C
5
5
2
inf
A
4
4
inf
E
0
D
inf
G
Here is the implementation of Dijkstra's algorithm on the directed graph, with D as the source vertex:

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
            #self.adj_matrix[v][u] = weight   For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D -> A, weight 5
g.add_edge(3, 4, 2)  # D -> E, weight 2
g.add_edge(0, 2, 3)  # A -> C, weight 3
g.add_edge(0, 4, 4)  # A -> E, weight 4
g.add_edge(4, 2, 4)  # E -> C, weight 4
g.add_edge(4, 6, 5)  # E -> G, weight 5
g.add_edge(2, 5, 5)  # C -> F, weight 5
g.add_edge(1, 2, 2)  # B -> C, weight 2
g.add_edge(1, 5, 2)  # B -> F, weight 2
g.add_edge(6, 5, 5)  # G -> F, weight 5

# Dijkstra's algorithm from D to all vertices
print("Dijkstra's Algorithm starting from vertex D:\n")
distances = g.dijkstra('D')
for i, d in enumerate(distances):
    print(f"Shortest distance from D to {g.vertex_data[i]}: {d}")
The image below shows us the shortest distances from vertex D as calculated by Dijkstra's algorithm.

11
F
2
5
3
4
5
2
inf
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
This result is similar to the previous example using Dijkstra's algorithm on the undirected graph. However, there's a key difference: in this case, vertex B cannot be visited from D, and this means that the shortest distance from D to F is now 11, not 10, because the path can no longer go through vertex B.

ADVERTISEMENT

Returning The Paths from Dijkstra's Algorithm
With a few adjustments, the actual shortest paths can also be returned by Dijkstra's algorithm, in addition to the shortest path values. So for example, instead of just returning that the shortest path value is 10 from vertex D to F, the algorithm can also return that the shortest path is "D->E->C->B->F".

10
F
2
5
3
4
5
2
8
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
To return the path, we create a predecessors array to keep the previous vertex in the shortest path for each vertex. The predecessors array can be used to backtrack to find the shortest path for every vertex.

Example
Python:

class Graph:
    # ... (rest of the Graph class)

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return distances, predecessors

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)  # Join the vertices with '->'

g = Graph(7)

# ... (rest of the graph setup)

# Dijkstra's algorithm from D to all vertices
print("Dijkstra's Algorithm starting from vertex D:\n")
distances, predecessors = g.dijkstra('D')
for i, d in enumerate(distances):
    path = g.get_path(predecessors, 'D', g.vertex_data[i])
    print(f"{path}, Distance: {d}")
Line 7 and 29: The predecessors array is first initialized with None values, then it is updated with the correct predecessor for each vertex as the shortest path values are updated.

Line 33-42: The get_path method uses the predecessors array and returns a string with the shortest path from start to end vertex.

ADVERTISEMENT

Dijkstra's Algorithm with a Single Destination Vertex
Let's say we are only interested in finding the shortest path between two vertices, like finding the shortest distance between vertex D and vertex F in the graph below.

inf
F
2
5
3
4
5
2
inf
B
inf
C
5
5
2
inf
A
4
4
inf
E
0
D
inf
G
5
inf
H
4
inf
I
2
inf
J
Dijkstra's algorithm is normally used for finding the shortest path from one source vertex to all other vertices in the graph, but it can also be modified to only find the shortest path from the source to a single destination vertex, by just stopping the algorithm when the destination is reached (visited).

This means that for the specific graph in the image above, Dijkstra's algorithm will stop after visiting F (the destination vertex), before visiting vertices H, I and J because they are farther away from D than F is.

Below we can see the status of the calculated distances when Dijkstra's algorithm has found the shortest distance from D to F, and stops running.

10
F
2
5
3
4
5
2
8
B
6
C
5
5
2
4
A
4
4
2
E
0
D
7
G
5
12
H
4
11
I
2
inf
J
In the image above, vertex F has just got updated with distance 10 from vertex B. Since F is the unvisited vertex with the lowest distance from D, it would normally be the next current vertex, but since it is the destination, the algorithm stops. If the algorithm did not stop, J would be the next vertex to get an updated distance 11+2=13, from vertex I.

The code below is Dijkstra's algorithm implemented to find the shortest path to a single destination vertex:

Example
Python:

class Graph:
    # ... (existing methods)

    def dijkstra(self, start_vertex_data, end_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        end_vertex = self.vertex_data.index(end_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None or u == end_vertex:
                print(f"Breaking out of loop. Current vertex: {self.vertex_data[u]}")
                print(f"Distances: {distances}")
                break

            visited[u] = True
            print(f"Visited vertex: {self.vertex_data[u]}")

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return distances[end_vertex], self.get_path(predecessors, start_vertex_data, end_vertex_data)

# Example usage
g = Graph(7)
# ... (rest of the graph setup)
distance, path = g.dijkstra('D', 'F')
print(f"Path: {path}, Distance: {distance}")
Line 20-23: If we are about to choose the destination vertex as the current vertex and mark it as visited, it means we have already calculated the shortest distance to the destination vertex, and Dijkstra's algorithm can be stopped in this single destination case.

Time Complexity for Dijkstra's Algorithm
With 
V
 as the number of vertices in our graph, the time complexity for Dijkstra's algorithm is

O
(
V
2
)

The reason why we get this time complexity is that the vertex with the lowest distance must to be search for to choose the next current vertex, and that takes 
O
(
V
)
 time. And since this must to be done for every vertex connected to the source, we need to factor that in, and so we get time complexity 
O
(
V
2
)
 for Dijkstra's algorithm.

By using a Min-heap or Fibonacci-heap data structure for the distances instead (not yet explained in this tutorial), the time needed to search for the minimum distance vertex is reduced from 
O
(
V
)
 to 
O
(
log
V
)
, which results in an improved time complexity for Dijkstra's algorithm

O
(
V
⋅
log
V
+
E
)

Where 
V
 is the number of vertices in the graph, and 
E
 is the number of edges.

The improvement we get from using a Min-heap data structure for Dijkstra's algorithm is especially good if we have a large and sparse graph, which means a graph with a large number of vertices, but not as many edges.

The implementation of Dijkstra's algorithm with the Fibonacci-heap data structure is better for dense graphs, where each vertex has an edge to almost every other vertex.

DSA Exercises
Test Yourself With Exercises
Exercise:
Using Dijkstra's algorithm to find the shortest paths from vertex C in this graph:


What is the next vertex to be visited after C is visited?

Using Dijkstra's algorithm,
the next vertex to be visited 
after vertex C is vertex 
.

"""















