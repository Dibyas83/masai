"""
Printing Paths in Dijkstra's Shortest Path Algorithm
Last Updated : 18 Jan, 2024
Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in
the given graph.
We have discussed Dijkstra's Shortest Path algorithm in the below posts.

Dijkstra’s shortest path for adjacency matrix representation
Dijkstra’s shortest path for adjacency list representation
The implementations discussed above only find shortest distances, but do not print paths. In this post-printing
of paths is discussed.

Example:

Input: Consider below graph and source as 0,


Graph Used in the problem

Output
Vertex     Distance    Path
0 -> 1          4        0 1
0 -> 2          12        0 1 2
0 -> 3          19        0 1 2 3
0 -> 4          21        0 7 6 5 4
0 -> 5          11        0 7 6 5
0 -> 6          9        0 7 6
0 -> 7          8        0 7
0 -> 8          14        0 1 2 8
The idea is to create a separate array parent[]. Value of parent[v] for a vertex v stores parent vertex of v
in shortest path tree. The parent of the root (or source vertex) is -1. Whenever we find a shorter path
through a vertex u, we make u as a parent of the current vertex.

Once we have the parent array constructed, we can print the path using the below recursive function.

void printPath(int parent[], int j)
{
    // Base Case : If j is source
    if (parent[j]==-1)
        return;

    printPath(parent, parent[j]);

    printf("%d ", j);
}

"""
import sys

NO_PARENT = -1


def dijkstra(adjacency_matrix, start_vertex):
    n_vertices = len(adjacency_matrix[0])

    # shortest_distances[i] will hold the
    # shortest distance from start_vertex to i
    shortest_distances = [sys.maxsize] * n_vertices

    # added[i] will true if vertex i is
    # included in shortest path tree
    # or shortest distance from start_vertex to
    # i is finalized
    added = [False] * n_vertices

    # Initialize all distances as
    # INFINITE and added[] as false
    for vertex_index in range(n_vertices):
        shortest_distances[vertex_index] = sys.maxsize
        added[vertex_index] = False

    # Distance of source vertex from
    # itself is always 0
    shortest_distances[start_vertex] = 0

    # Parent array to store shortest
    # path tree
    parents = [-1] * n_vertices

    # The starting vertex does not
    # have a parent
    parents[start_vertex] = NO_PARENT

    # Find shortest path for all
    # vertices
    for i in range(1, n_vertices):
        # Pick the minimum distance vertex
        # from the set of vertices not yet
        # processed. nearest_vertex is
        # always equal to start_vertex in
        # first iteration.
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        # Mark the picked vertex as
        # processed
        added[nearest_vertex] = True

        # Update dist value of the
        # adjacent vertices of the
        # picked vertex.
        for vertex_index in range(n_vertices):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]

            if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance

    print_solution(start_vertex, shortest_distances, parents)


# A utility function to print
# the constructed distances
# array and shortest paths
def print_solution(start_vertex, distances, parents):
    n_vertices = len(distances)
    print("Vertex\t Distance\tPath")

    for vertex_index in range(n_vertices):
        if vertex_index != start_vertex:
            print("\n", start_vertex, "->", vertex_index, "\t\t", distances[vertex_index], "\t\t", end="")
            print_path(vertex_index, parents)


# Function to print shortest path
# from source to current_vertex
# using parents array
def print_path(current_vertex, parents):
    # Base case : Source node has
    # been processed
    if current_vertex == NO_PARENT:
        return
    print_path(parents[current_vertex], parents)
    print(current_vertex, end=" ")


# Driver code
if __name__ == '__main__':
    adjacency_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                        [4, 0, 8, 0, 0, 0, 0, 11, 0],
                        [0, 8, 0, 7, 0, 4, 0, 0, 2],
                        [0, 0, 7, 0, 9, 14, 0, 0, 0],
                        [0, 0, 0, 9, 0, 10, 0, 0, 0],
                        [0, 0, 4, 14, 10, 0, 2, 0, 0],
                        [0, 0, 0, 0, 0, 2, 0, 1, 6],
                        [8, 11, 0, 0, 0, 0, 1, 0, 7],
                        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    dijkstra(adjacency_matrix, 0)

















