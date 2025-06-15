
"""



"""

import  sys  # to assign infinite cost to vertices not visited
from heapq import heappush, heappop, heapify  # for priority queue
def dijsktra(graph,src,dest):
    inf = sys.maxsize  # not acessed or visited
    node_data = {'a':{'cost':inf,'pred':[]},
                 'b':{'cost':inf,'pred':[]},
                 'c':{'cost':inf,'pred':[]},
                 'd':{'cost':inf,'pred':[]},
                 'e':{'cost':inf,'pred':[]},
                 'f':{'cost':inf,'pred':[]}

                 }
    node_data[src]['cost'] = 0
    visited = []
    n = len(node_data)
    temp = src  # temp the src wii be assigned to min node , as the src changes in anather heap
    for i in range(n-1):  # n is no of vertixes
        if temp not in visited:
            visited.append(temp)
            min_heap = [] # empty set
            for  j in graph[temp]: # now temp is src a so j will be b and c,when temp is b j will be a,c,d
                if j not in visited: # if in visited cost will not be considered
                    cost = node_data[temp]['cost'] + graph[temp][j] # graph[a][b] is cost of a to b = 2
                    if cost < node_data[j]['cost']: # cost to be less than cost of neighbors b,c in node_data.j becomes b and c in loop
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp) # path initially no predecessor
                    heappush(min_heap,(node_data[j]['cost'],j))  # this will add or push cost to neighbors and neighbors
        heapify(min_heap)
        temp = min_heap[0][1] # 0 will give cost and will give neighbor b
    print("shortest distance:" + str(node_data[dest]['cost']))
    print("shortest path:" + str(node_data[dest]['pred'] + list(dest))) # list(dest) is for last element


if __name__== "__main__":
    graph = {
        'a':{'b':2,'c':4},  # nodes as key and values(anather dict) as connected neighbors
        'b':{'a':2,'c':3,'d':2},
        'c':{'a':4,'b':3,'e':5,'d':2},
        'd':{'b':8,'c':2,'e':11,'f':22},
        'e':{'c':5,'d':11,'f':1},
        'f':{'d':22,'e':1}
    }
    source = 'a'
    destination = 'f'
    dijsktra(graph,'a','f')
    #print(dijsktra(graph,'a','f'))


"""

Dijkstra's shortest path algorithm in Python
Last Updated : 08 Mar, 2025
Given a graph and a source vertex in the graph, find the shortest paths from source to all vertices in the given graph. Dijkstra’s algorithm is a popular algorithm for solving many single-source shortest path problems having non-negative edge weight in the graphs i.e., it is to find the shortest distance between two vertices on a graph. It was conceived by Dutch computer scientist Edsger W. Dijkstra in 1956.

Algorithm
Dijkstra's algorithm is very similar to Prim's algorithm for minimum spanning tree. Like Prim's MST, we generate an SPT (shortest path tree) with a given source as root. We maintain two sets, one set contains vertices included in the shortest-path tree, another set includes vertices not yet included in the shortest-path tree. At every step of the algorithm, we find a vertex that is in the other set (set of not yet included) and has a minimum distance from the source. Below are the detailed steps used in Dijkstra's algorithm to find the shortest path from a single source vertex to all other vertices in the given graph. 

1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty. 
2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first. 
3) While sptSet doesn't include all vertices: 

Pick a vertex u which is not there in sptSet and has minimum distance value.
Include u to sptSet.
Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if the sum of a distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.

"""

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = 1e7

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)

# w3school------------------------
"""
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

"""

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





