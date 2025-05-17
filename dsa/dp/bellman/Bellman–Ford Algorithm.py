
"""
Given a weighted graph with V vertices and E edges, along with a source vertex src, the task is to compute the shortest distances from the source to all other vertices. If a vertex is unreachable from the source, its distance should be marked as 108. In the presence of a negative weight cycle, return -1 to signify that shortest path calculations are not feasible.

Examples:

Input: V = 5, edges = [[0, 1, 5], [1, 2, 1], [1, 3, 2], [2, 4, 1], [4, 3, -1]], src = 0


bellman_ford_input_images
Output: [0, 5, 6, 6, 7]
Explanation:  Shortest Paths:
For 0 to 1 minimum distance will be 5. By following path 0 → 1
For 0 to 2 minimum distance will be 6. By following path 0 → 1  → 2
For 0 to 3 minimum distance will be 6. By following path 0 → 1  → 2 → 4 → 3
For 0 to 4 minimum distance will be 7. By following path 0 → 1  → 2 → 4


Input: V = 4, edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]], src = 0


input-2
Output: [-1]
Explanation: The graph contains a negative weight cycle formed by the path 1 → 2 → 3 → 1, where the total weight of the cycle is negative.


Try it on GfG Practice
redirect icon
Table of Content

Bellman-Ford Algorithm – O(V*E) Time and O(V) Space
Negative weight cycle:
Limitation of Dijkstra’s Algorithm:
Principle of Relaxation of Edges
Why Relaxing Edges (V – 1) times gives us Single Source Shortest Path?
Detection of a Negative Weight Cycle
Problems based on Shortest Path
Approach: Bellman-Ford Algorithm – O(V*E) Time and O(V) Space
Negative weight cycle:
A negative weight cycle is a cycle in a graph, whose sum of edge weights is negative. If you traverse the cycle, the total weight accumulated would be less than zero.

BellmanFord-Algorithm-eXAMPLE
In the presence of negative weight cycle in the graph, the shortest path doesn’t exist because with each traversal of the cycle shortest path keeps decreasing.

Limitation of Dijkstra’s Algorithm:
Since, we need to find the single source shortest path, we might initially think of using Dijkstra’s algorithm. However, Dijkstra is not suitable when the graph consists of negative edges. The reason is, it doesn’t revisit those nodes which have already been marked as visited. If a shorter path exists through a longer route with negative edges, Dijkstra’s algorithm will fail to handle it.

Principle of Relaxation of Edges
Relaxation means updating the shortest distance to a node if a shorter path is found through another node. For an edge (u, v) with weight w:
If going through u gives a shorter path to v from the source node (i.e., distance[v] > distance[u] + w), we update the distance[v] as distance[u] + w.
In the bellman-ford algorithm, this process is repeated (V – 1) times for all the edges.
Why Relaxing Edges (V – 1) times gives us Single Source Shortest Path?
A shortest path between two vertices can have at most (V – 1) edges. It is not possible to have a simple path with more than (V – 1) edges (otherwise it would form a cycle). Therefore, repeating the relaxation process (V – 1) times ensures that all possible paths between source and any other node have been covered.

Assuming node 0 as the source vertex, let’s see how we can relax the edges to find the shortest paths:

baleman-fort
In the first relaxation, since the shortest paths for vertices 1 and 2 are unknown (infinite, i.e., 108), the shortest paths for vertices 2 and 3 will also remain infinite (108) . And, for vertex 1, the distance will be updated to 4, as dist[0] + 4 < dist[1] (i.e., 0 + 4 < 108).
In the second relaxation, the shortest path for vertex 2 is still infinite (e.g. 108), which means the shortest path for vertex 3 will also remain infinite. For vertex 2, the distance can be updated to 3, as dist[1] + (-1) = 3.
In the third relaxation, the shortest path for vertex 3 will be updated to 5, as dist[2] + 2 = 5.
So, in above example, dist[1] is updated in 1st relaxation, dist[2] is updated in second relaxation, so the dist for the last node (V – 1), will be updated in (V – 1) th relaxation.

Detection of a Negative Weight Cycle
As we have discussed earlier that, we need (V – 1) relaxations of all the edges to achieve single source shortest path. If one additional relaxation (Vth) for any edge is possible, it indicates that some edges with overall negative weight has been traversed once more. This indicates the presence of a negative weight cycle in the graph.
Bellman-Ford is a single source shortest path algorithm. It effectively works in the cases of negative edges and is able to detect negative cycles as well. It works on the principle of relaxation of the edges.


Illustration:

BellmanFord-Algorithm-1.webpBellmanFord-Algorithm-1.webp





1
def bellmanFord(V, edges, src):
2

3
    # Initially distance from source to all other vertices
4
    # is not known(Infinite) e.g. 1e8.
5
    dist = [100000000] * V
6
    dist[src] = 0
7
​
8
    # Relaxation of all the edges V times, not (V - 1) as we
9
    # need one additional relaxation to detect negative cycle
10
    for i in range(V):
11
        for edge in edges:
12
            u, v, wt = edge
13
            if dist[u] != 100000000 and dist[u] + wt < dist[v]:
14

15
                # If this is the Vth relaxation, then there
16
                # is a negative cycle
17
                if i == V - 1:
18
                    return [-1]
19

20
                # Update shortest distance to node v
21
                dist[v] = dist[u] + wt
22
    return dist
23
​
24
if __name__ == '__main__':
25
    V = 5
26
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
27
​
28
    src = 0
29
    ans = bellmanFord(V, edges, src)
30
    print(' '.join(map(str, ans)))

Output
0 5 6 6 7
Problems based on Shortest Path
Shortest Path in Directed Acyclic Graph
Shortest path with one curved edge in an undirected Graph
Minimum Cost Path
Path with smallest difference between consecutive cells
Print negative weight cycle in a Directed Graph
1st to Kth shortest path lengths in given Graph
Shortest path in a Binary Maze
Minimum steps to reach target by a Knight
Number of ways to reach at destination in shortest time
Snake and Ladder Problem
Word Ladder


"""







