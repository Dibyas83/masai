
"""

Given a directed and weighted graph of N nodes and M edges, the task is to find the 1st to Kth shortest path lengths from node 1 to N.

Examples:


Input: N = 4, M = 6, K = 3, edges = {{1, 2, 1}, {1, 3, 3}, {2, 3, 2}, {2, 4, 6}, {3, 2, 8}, {3, 4, 1}}
Output: 4 4 7
Explanation: The shortest path length from 1 to N is 4, 2nd shortest length is also 4 and 3rd shortest length is 7.


Input: N = 3, M = 3, K = 2, edges = {{1, 2, 2}, {2, 3, 2}, {1, 3, 1}}
Output: 1 4


Approach: The idea is to traverse all vertices of the graph using BFS and use priority queue to store the vertices for which the shortest distance is not finalized yet, and also to get the minimum distance vertex. Follow the steps below for the approach.

Initialize a priority queue, say, pq of size N to store the vertex number and distance value.
Initialize a 2-d vector, say, dis of size N*K and initialize all values with a very large number, say, 1e9.
Set dis[1][0] to zero, the distance value of the source vertex.
Iterate while pq is not empty.
Pop the value from pq, and store the vertex value in variable u and vertex distance in variable d.
If d is greater than the distance u, then continue.
For every adjacent vertex v of u check if the Kth distance value is more than the weight of u-v plus the distance value of u, then update the Kth distance value of v and sort the k distances of vertex v.
Below is the implementation of the above approach:




import heapq


def findKShortest(edges, n, m, k):
    # Initialize graph
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        # Storing edges
        g[edges[i][0]].append((edges[i][1], edges[i][2]))

    # Vector to store distances
    dis = [[1e9 for _ in range(k)] for __ in range(n + 1)]

    # Initialization of priority queue
    pq = []
    heapq.heappush(pq, (0, 1))
    dis[1][0] = 0

    # while pq has elements
    while pq:
        # Storing the node value
        d, u = heapq.heappop(pq)

        if dis[u][k - 1] < d:
            continue

        # Traversing the adjacency list
        for dest, cost in g[u]:
            # Checking for the cost
            if d + cost < dis[dest][k - 1]:
                dis[dest][k - 1] = d + cost

                # Sorting the distances
                dis[dest].sort()

                # Pushing elements to priority queue
                heapq.heappush(pq, (d + cost, dest))

    # Printing K shortest paths
    print(*dis[n][:k])


# Given Input
N, M, K = 4, 6, 3
edges = [(1, 2, 1), (1, 3, 3), (2, 3, 2), (2, 4, 6), (3, 2, 8), (3, 4, 1)]

# Function Call
findKShortest(edges, N, M, K)
Output
4 4 7
Time Complexity: O((N+M)*KlogK)
Auxiliary Space: O(NK)
"""









