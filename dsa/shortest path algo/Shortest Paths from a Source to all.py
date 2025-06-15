
"""

Dijkstra's Algorithm to find Shortest Paths from a Source to all
Last Updated : 21 May, 2025
Given a weighted undirected graph represented as an edge list and a source vertex src, find the shortest path
distances from the source vertex to all other vertices in the graph. The graph contains V vertices, numbered
from 0 to V - 1.

Note: The given graph does not contain any negative edge.

Examples:

Input: src = 0, V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]

1
Graph with 5 node
Output:  0 4 8 10 10
Explanation:  Shortest Paths:
0 to 1 = 4. 0 → 1
0 to 2 = 8. 0 → 2
0 to 3 = 10. 0 → 2 → 3
0 to 4 = 10. 0 → 1 → 4

Try it on GfG Practice
redirect icon
Dijkstra’s Algorithm using Min Heap - O(E*logV) Time and O(V) Space

In Dijkstra's Algorithm, the goal is to find the shortest distance from a given source node to all other nodes
in the graph. As the source node is the starting point, its distance is initialized to zero. From there, we
teratively pick the unprocessed node with the minimum distance from the source, this is where a min-heap (priority
queue) or a set is typically used for efficiency. For each picked node u, we update the distance to its neighbors
v using the formula: dist[v] = dist[u] + weight[u][v], but only if this new path offers a shorter distance than
the current known one. This process continues until all nodes have been processed.

Step-by-Step Implementation

Set dist[source]=0 and all other distances as infinity.
Push the source node into the min heap as a pair <distance, node> → i.e., <0, source>.
Pop the top element (node with the smallest distance) from the min heap.
For each adjacent neighbor of the current node:
Calculate the distance using the formula:
dist[v] = dist[u] + weight[u][v]
    If this new distance is shorter than the current dist[v], update it.
    Push the updated pair <dist[v], v> into the min heap
Repeat step 3 until the min heap is empty.
Return the distance array, which holds the shortest distance from the source to all nodes.
"""

import heapq
import sys


# Function to construct adjacency
def constructAdj(edges, V):
    # adj[u] = list of [v, wt]
    adj = [[] for _ in range(V)]

    for edge in edges:
        u, v, wt = edge
        adj[u].append([v, wt])
        adj[v].append([u, wt])

    return adj


# Returns shortest distances from src to all other vertices
def dijkstra(V, edges, src):
    # Create adjacency list
    adj = constructAdj(edges, V)

    # Create a priority queue to store vertices that
    # are being preprocessed.
    pq = []

    # Create a list for distances and initialize all
    # distances as infinite
    dist = [sys.maxsize] * V

    # Insert source itself in priority queue and initialize
    # its distance as 0.
    heapq.heappush(pq, [0, src])
    dist[src] = 0

    # Looping till priority queue becomes empty (or all
    # distances are not finalized)
    while pq:
        # The first vertex in pair is the minimum distance
        # vertex, extract it from priority queue.
        u = heapq.heappop(pq)[1]

        # Get all adjacent of u.
        for x in adj[u]:
            # Get vertex label and weight of current
            # adjacent of u.
            v, weight = x[0], x[1]

            # If there is shorter path to v through u.
            if dist[v] > dist[u] + weight:
                # Updating distance of v
                dist[v] = dist[u] + weight
                heapq.heappush(pq, [dist[v], v])

    # Return the shortest distance array
    return dist


# Driver program to test methods of graph class
if __name__ == "__main__":
    V = 5
    src = 0

    # edge list format: {u, v, weight}
    edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]];

    result = dijkstra(V, edges, src)

    # Print shortest distances in one line
    print(' '.join(map(str, result)))







