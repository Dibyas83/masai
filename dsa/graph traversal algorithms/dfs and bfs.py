
"""
Graphs Traversal
To traverse a Graph means to start in one vertex, and go along the edges to visit other vertices until all vertices, or as many as possible, have been visited.

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
DFS is usually implemented using a Stack or by the use of recursion (which utilizes the call stack), while BFS is usually implemented using a Queue.

The Call Stack keeps functions running in the correct order.

If for example FunctionA calls FunctionB, FunctionB is placed on top of the call stack and starts running. Once FunctionB is finished, it is removed from the stack, and then FunctionA resumes its work.

Depth First Search Traversal
Depth First Search is said to go "deep" because it visits a vertex, then an adjacent vertex, and then that vertex' adjacent vertex, and so on, and in this way the distance from the starting vertex increases for each recursive iteration.

How it works:

Start DFS traversal on a vertex.
Do a recursive DFS traversal on each of the adjacent vertices as long as they are not already visited.
Run the animation below to see how Depth First Search (DFS) traversal runs on a specific Graph, starting in vertex D (it is the same as the previous animation).

F
B
C
A
E
D
G
Result:

DFS Traverse from D
The DFS traversal starts in vertex D, marks vertex D as visited. Then, for every new vertex visited, the traversal method is called recursively on all adjacent vertices that have not been visited yet. So when vertex A is visited in the animation above, vertex C or vertex E (depending on the implementation) is the next vertex where the traversal continues.

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

Line 35: The visited array is sent as an argument to the dfs_util() method. When the visited array is sent as an argument like this, it is actually just a reference to the visited array that is sent to the dfs_util() method, and not the actual array with the values inside. So there is always just one visited array in our program, and the dfs_util() method can make changes to it as nodes are visited (line 25).

Line 28-30: For the current vertex v, all adjacent nodes are called recursively if they are not already visited.

Breadth First Search Traversal
Breadth First Search visits all adjacent vertices of a vertex before visiting neighboring vertices to the adjacent vertices. This means that vertices with the same distance from the starting vertex are visited before vertices further away from the starting vertex are visited.

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
As you can see in the animation above, BFS traversal visits vertices the same distance from the starting vertex, before visiting vertices further away. So for example, after visiting vertex A, vertex E and C are visited before visiting B, F and G because those vertices are further away.

Breadth First Search traversal works this way by putting all adjacent vertices in a queue (if they are not already visited), and then using the queue to visit the next vertex.

This code example for Breadth First Search traversal is the same as for the Depth First Search code example above, except for the bfs() method:


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
Java - Type Casting
Video Player is loading.Play VideoBrand logo

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

def add_edge(self, u, v):
    if 0 <= u < self.size and 0 <= v < self.size:
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
We must also take care when we build our Graph because the edges are now directed.

The code example below contains both BFS and DFS traversal of the directed Graph from the animation above:

Example
"""


class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            # self.adj_matrix[v][u] = 1

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







