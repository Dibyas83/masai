
"""
There are n cities and there are roads in between some of the cities. Somehow all the roads are damaged simultaneously. We have to repair the roads to connect the cities again. There is a fixed cost to repair a particular road.

Input is in the form of edges {u, v, w} where, u and v are city indices. w is the cost to rebuild the road between u and v. Print out the minimum cost to connect all the cities by repairing roads.

Examples:

Input: {{1, 2, 1}, {1, 3, 2}, {1, 4, 3}, {1, 5, 4},
            {2, 3, 5}, {2, 5, 7}, {3, 4, 6}}
Output: 10
Explanation: Refer the fig…


citymap-2
Citymap with 5 cities and 7 damaged road

Input : {{1, 2, 1}, {1, 3, 1}, {1, 4, 100},
            {2, 3, 1}, {4, 5, 2}, {4, 6, 2}, {5, 6, 2}}
Output : 106
Explanation: Minimum cost to connect all the cities is 106

Input: {{1,2,5},{2,4,2},{4,3,1},{1,3,7},{1,4,7},{3,,5,3}}
Output: 11
Explanation: Minimum cost to connect all the cities is 11


[Approach] Using Prim’s Algorithm – O(ElogV) Time and O(n) Space
We can solve this problem using Prim’s Algorithm, which finds the Minimum Spanning Tree (MST) to connect all cities with the minimum repair cost.


Steps-by-step approach:
Start from any random city (usually city 1).
Use a Min-Heap (Priority Queue) to always pick the cheapest edge.
Maintain a visited array to keep track of cities included in the MST.
Add edges to the MST until all cities are connected and return answer at last.



1
import heapq
2
# Function to find the minimum cost to connect all the cities
3
def findMST(n, edges):
4
    adj = [[] for _ in range(n + 1)]  # 1-based indexing
5
​
6
    # Convert edge list to adjacency list
7
    for u, v, w in edges:
8
        adj[u].append((w, v))
9
        adj[v].append((w, u))
10
​
11
    pq = [(0, 1)]  # (weight, node), start from node 1
12
    inMST = [False] * (n + 1)  # 1-based indexing
13
    mstCost = 0
14
​
15
    while pq:
16
        w, u = heapq.heappop(pq)
17
        if inMST[u]:
18
            continue
19
        inMST[u] = True
20
        mstCost += w
21
​
22
        for weight, v in adj[u]:
23
            if not inMST[v]:
24
                heapq.heappush(pq, (weight, v))
25
​
26
    return mstCost
27
​
28
# Example usage with 1-based indexing
29
city1 = [
30
    (1, 2, 1), (1, 3, 2), (1, 4, 3), (1, 5, 4),
31
    (2, 3, 5), (2, 5, 7), (3, 4, 6)
32
]
33
print(findMST(5, city1))
34
​
35
city2 = [
36
    (1, 2, 1), (1, 3, 1), (1, 4, 100),
37
    (2, 3, 1), (4, 5, 2), (4, 6, 2), (5, 6, 2)
38
]
39
print(findMST(6, city2))

Output
10
106


"""




