"""
Approximate solution for Travelling Salesman Problem using MST
Last Updated : 08 Apr, 2025
Given a 2d matrix cost[][] of size n where cost[i][j] denotes the cost of moving from city i to city j. The task is to complete a tour from city 0 (0-based index) to all other towns such that we visit each city exactly once and then return to city 0 at minimum cost.

Note: There is a difference between the Hamiltonian Cycle and TSP. The Hamiltonian cycle problem is to find if there exists a tour that visits every city exactly once. Here we know that the Hamiltonian Tour exists (because the graph is complete) and, many such tours exist, the problem is to find a minimum weight Hamiltonian Cycle.

Examples:

Input: cost[][] = [[0, 111], [112, 0]]
Output: 223
Explanation: We can visit 0->1->0 and cost = 111 + 112 = 223.


Input: cost[][] = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]]
Output: 3000
Explanation: We can visit 0->1->2->0 and cost = 1000 + 1000 + 1000 = 3000.


We introduced Travelling Salesman Problem and discussed Naive and Dynamic Programming Solutions for the problem. Both of the solutions are infeasible. In fact, there is no polynomial time solution available for this problem as the problem is a known NP-Hard problem. There are approximate algorithms to solve the problem though. The approximate algorithms work only if the problem instance satisfies Triangle-Inequality.

What is Triangle Inequality?

The least distant path to reach a vertex j from i is always to reach j directly from i, rather than through some other vertex k (or vertices), i.e., dis(i, j) is always less than or equal to dis(i, k) + dist(k, j). The Triangle-Inequality holds in many practical situations.


Using Minimum Spanning Tree – 2 Approximate Algorithm
When the cost function satisfies the triangle inequality, we can design an approximate algorithm for TSP that returns a tour whose cost is never more than twice the cost of an optimal tour. The idea is to use Minimum Spanning Tree (MST). Following is the MST based algorithm.


Algorithm:

Let 1 be the starting and ending point for salesman.
Construct MST from with 1 as root using Prim’s Algorithm.
List vertices visited in preorder walk of the constructed MST and add 1 at the end.
Let us consider the following example. The first diagram is the given graph. The second diagram shows MST constructed with 1 as root. The preorder traversal of MST is 1-2-4-3. Adding 1 at the end gives 1-2-4-3-1 which is the output of this algorithm.


Euler1

 MST_TSP

In this case, the approximate algorithm produces the optimal tour, but it may not produce optimal tour in all cases.


How is algorithm 2-approximate?

The cost of the output produced by the above algorithm is never more than twice the cost of best possible output. Let us see how is this guaranteed by the above algorithm.


Let us define a term full walk to understand this. A full walk is lists all vertices when they are first visited in preorder, it also list vertices when they are returned after a subtree is visited in preorder. The full walk of above tree would be 1-2-1-4-1-3-1.


Following are some important facts that prove the 2-approximateness.

The cost of best possible Travelling Salesman tour is never less than the cost of MST. (The definition of MST says, it is a minimum cost tree that connects all vertices).
The total cost of full walk is at most twice the cost of MST (Every edge of MST is visited at-most twice)
The output of the above algorithm is less than the cost of full walk. In above algorithm, we print preorder walk as output. In preorder walk, two or more edges of full walk are replaced with a single edge. For example, 2-1 and 1-4 are replaced by 1 edge 2-4. So if the graph follows triangle inequality, then this is always true.
From the above three statements, we can conclude that the cost of output produced by the approximate algorithm is never more than twice the cost of best possible solution.
"""


# function to calculate the cost of the tour
def tourCost(tour):
    cost = 0
    for edge in tour:
        cost += edge[2]
    return cost


# function to find the eulerian circuit
def eulerianCircuit(adj, u, tour, visited, parent):
    visited[u] = True
    tour.append(u)

    for neighbor in adj[u]:
        v = neighbor[0]
        if v == parent:
            continue

        if visited[v] == False:
            eulerianCircuit(adj, v, tour, visited, u)


# function to find the minimum spanning tree
import heapq


def findMST(adj, mstCost):
    n = len(adj)

    # to marks the visited nodes
    visited = [False] * n

    # stores edges of minimum spanning tree
    mstEdges = []

    pq = []
    heapq.heappush(pq, [0, 0, -1])

    while pq:
        current = heapq.heappop(pq)

        u = current[1]
        weight = current[0]
        parent = current[2]

        if visited[u]:
            continue

        mstCost[0] += weight
        visited[u] = True

        if parent != -1:
            mstEdges.append([u, parent, weight])

        for neighbor in adj[u]:
            v = neighbor[0]
            if v == parent:
                continue
            w = neighbor[1]

            if not visited[v]:
                heapq.heappush(pq, [w, v, u])
    return mstEdges


# function to implement approximate TSP
def approximateTSP(adj):
    n = len(adj)

    # to store the cost of minimum spanning tree
    mstCost = [0]

    # stores edges of minimum spanning tree
    mstEdges = findMST(adj, mstCost)

    # to mark the visited nodes
    visited = [False] * n

    # create adjacency list for mst
    mstAdj = [[] for _ in range(n)]
    for e in mstEdges:
        mstAdj[e[0]].append([e[1], e[2]])
        mstAdj[e[1]].append([e[0], e[2]])

    # to store the eulerian tour
    tour = []
    eulerianCircuit(mstAdj, 0, tour, visited, -1)

    # add the starting node to the tour
    tour.append(0)

    # to store the final tour path
    tourPath = []

    for i in range(len(tour) - 1):
        u = tour[i]
        v = tour[i + 1]
        weight = 0

        # find the weight of the edge u -> v
        for neighbor in adj[u]:
            if neighbor[0] == v:
                weight = neighbor[1]
                break

        # add the edge to the tour path
        tourPath.append([u, v, weight])

    return tourPath


# function to calculate if the
# triangle inequality is violated
def triangleInequality(adj):
    n = len(adj)

    # Sort each adjacency list based
    # on the weight of the edges
    for i in range(n):
        adj[i].sort(key=lambda a: a[1])

    # check triangle inequality for each
    # triplet of nodes (u, v, w)
    for u in range(n):
        for x in adj[u]:
            v = x[0]
            costUV = x[1]
            for y in adj[v]:
                w = y[0]
                costVW = y[1]
                for z in adj[u]:
                    if z[0] == w:
                        costUW = z[1]
                        if (costUV + costVW < costUW) and (u < w):
                            return True
    # no violations found
    return False


# function to create the adjacency list
def createList(cost):
    n = len(cost)

    # to store the adjacency list
    adj = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            # if there is no edge between u and v
            if cost[u][v] == 0:
                continue
            # add the edge to the adjacency list
            adj[u].append([v, cost[u][v]])

    return adj


# function to solve the travelling salesman problem
def tsp(cost):
    # create the adjacency list
    adj = createList(cost)

    """ check for triangle inequality violations
    if triangleInequality(adj):
        print("Triangle Inequality Violation")
        return -1
    """

    # construct the travelling salesman tour
    tspTour = approximateTSP(adj)

    # calculate the cost of the tour
    tspCost = tourCost(tspTour)

    return tspCost


if __name__ == "__main__":
    cost = [
        [0, 1000, 5000],
        [5000, 0, 1000],
        [1000, 5000, 0]
    ]

    print(tsp(cost))

"""
Time Complexity: O(n ^ 3), the time complexity of triangleInequality() function is O(n ^ 3) as we are using 3 nested loops, and all other functions are working in O(n ^ 2), and O(n ^ 2 * log n) time complexity, thus the overall time complexity will be O(n ^ 3).
Space Complexity: O(n ^ 2), to store the adjacency list, and creating MST.

Using Christofides Algorithm – 1.5 Approximate Algorithm
The Christofides algorithm or Christofides–Serdyukov algorithm is an algorithm for finding approximate solutions to the travelling salesman problem, on instances where the distances form a metric space (they are symmetric and obey the triangle inequality).It is an approximation algorithm that guarantees that its solutions will be within a factor of 3/2 of the optimal solution length


Algorithm:

Create a minimum spanning tree T of G.
Let O be the set of vertices with odd degree in T. By the handshaking lemma, O has an even number of vertices.
Find a minimum-weight perfect matching M in the subgraph induced in G by O.
Combine the edges of M and T to form a connected multigraph H in which each vertex has even degree.
Form an Eulerian circuit in H.
Make the circuit found in previous step into a Hamiltonian circuit by skipping repeated vertices (shortcutting).

"""


# function to calculate the cost of the tour
def tourCost(tour):
    cost = 0
    for edge in tour:
        cost += edge[2]
    return cost


# function to find the minimum matching edges
def findMinimumMatching(adj, oddNodes):
    # to store the matching edges
    matchingEdges = []

    # if there are no odd nodes
    if not oddNodes:
        return matchingEdges

    # to store the candidate edges
    candidateEdges = []

    for i in range(len(oddNodes)):
        u = oddNodes[i]
        for j in range(i + 1, len(oddNodes)):
            v = oddNodes[j]
            for neighbor in adj[u]:
                if neighbor[0] == v:
                    candidateEdges.append([u, v, neighbor[1]])
                    break

    # sort the candidate edges based on the weight
    candidateEdges.sort(key=lambda a: a[2])

    # to store the matched nodes
    matched = set()

    # find the minimum matching edges
    for e in candidateEdges:
        if e[0] not in matched and e[1] not in matched:
            matchingEdges.append(e)
            matched.add(e[0])
            matched.add(e[1])
        if len(matched) == len(oddNodes):
            break

    return matchingEdges


# function to find the eulerian circuit
def eulerianCircuit(adj, u, tour, visited, parent):
    visited[u] = True
    tour.append(u)

    for neighbor in adj[u]:
        v = neighbor[0]
        if v == parent:
            continue
        if not visited[v]:
            eulerianCircuit(adj, v, tour, visited, u)


# function to find the minimum spanning tree
import heapq


def findMST(adj, mstCost):
    n = len(adj)

    # to marks the visited nodes
    visited = [False] * n

    # stores edges of minimum spanning tree
    mstEdges = []

    pq = []
    heapq.heappush(pq, [0, 0, -1])

    while pq:
        current = heapq.heappop(pq)

        u = current[1]
        weight = current[0]
        parent = current[2]

        if visited[u]:
            continue

        mstCost[0] += weight
        visited[u] = True

        if parent != -1:
            mstEdges.append([u, parent, weight])

        for neighbor in adj[u]:
            v = neighbor[0]
            if v == parent:
                continue
            w = neighbor[1]
            if not visited[v]:
                heapq.heappush(pq, [w, v, u])
    return mstEdges


# function to implement approximate TSP
def approximateTSP(adj):
    n = len(adj)

    # to store the cost of minimum spanning tree
    mstCost = [0]

    # stores edges of minimum spanning tree
    mstEdges = findMST(adj, mstCost)

    # to store the degree of each node
    degrees = [0] * n

    # create adjacency list for mst
    mstAdj = [[] for _ in range(n)]
    for e in mstEdges:
        mstAdj[e[0]].append([e[1], e[2]])
        mstAdj[e[1]].append([e[0], e[2]])
        degrees[e[0]] += 1
        degrees[e[1]] += 1

    # to store nodes with odd degrees
    oddNodes = []

    # nodes with odd degrees
    for i in range(n):
        if degrees[i] % 2 != 0:
            oddNodes.append(i)

    # find the minimum matching edges
    matchingEdges = findMinimumMatching(adj, oddNodes)

    # create a multigraph
    multigraphAdj = [list(lst) for lst in mstAdj]
    for e in matchingEdges:
        multigraphAdj[e[0]].append([e[1], e[2]])
        multigraphAdj[e[1]].append([e[0], e[2]])

    # to store the eulerian tour
    tour = []

    # to mark the visited nodes
    visited = [False] * n

    eulerianCircuit(multigraphAdj, 0, tour, visited, -1)

    # add the starting node to the tour
    tour.append(0)
    # to store the final tour path
    tourPath = []

    for i in range(len(tour) - 1):
        u = tour[i]
        v = tour[i + 1]
        weight = 0

        # find the weight of the edge u -> v
        for neighbor in adj[u]:
            if neighbor[0] == v:
                weight = neighbor[1]
                break

        # add the edge to the tour path
        tourPath.append([u, v, weight])

    return tourPath


# function to calculate if the
# triangle inequality is violated
def triangleInequality(adj):
    n = len(adj)

    # Sort each adjacency list based
    # on the weight of the edges
    for i in range(n):
        adj[i].sort(key=lambda a: a[1])

    # check triangle inequality for each
    # triplet of nodes (u, v, w)
    for u in range(n):
        for x in adj[u]:
            v = x[0]
            costUV = x[1]
            for y in adj[v]:
                w = y[0]
                costVW = y[1]
                for z in adj[u]:
                    if z[0] == w:
                        costUW = z[1]
                        # if the triangle inequality is violated
                        if (costUV + costVW < costUW) and (u < w):
                            return True
    # no violations found
    return False


# function to create the adjacency list
def createList(cost):
    n = len(cost)

    # to store the adjacency list
    adj = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            # if there is no edge between u and v
            if cost[u][v] == 0:
                continue
            # add the edge to the adjacency list
            adj[u].append([v, cost[u][v]])

    return adj


# function to solve the travelling salesman problem
def tsp(cost):
    # create the adjacency list
    adj = createList(cost)

    """ check for triangle inequality violations
    if triangleInequality(adj):
        print("Triangle Inequality Violation")
        return -1
    """

    # construct the travelling salesman tour
    tspTour = approximateTSP(adj)

    # calculate the cost of the tour
    tspCost = tourCost(tspTour)

    return tspCost


if __name__ == "__main__":
    cost = [
        [0, 1000, 5000],
        [5000, 0, 1000],
        [1000, 5000, 0]
    ]

    print(tsp(cost))

"""
Time Complexity: O(n ^ 3), the time complexity of triangleInequality() function is O(n ^ 3) as we are using 3 nested loops, and all other functions are working in O(n ^ 2), and O(n ^ 2 * log n) time complexity, thus the overall time complexity will be O(n ^ 3).
Space Complexity: O(n ^ 2), to store the adjacency list, and creating MST.

"""




