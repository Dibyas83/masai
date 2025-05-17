
"""

Given an undirected connected graph of n vertices and a list of m edges in a graph and for each pair of vertices that are connected by an edge. There are two edges between them, one curved edge and one straight edge i.e. the tuple (x, y, w1, w2) means that between vertices x and y, there is a straight edge with weight w1 and a curved edge with weight w2. You are given two vertices a and b and you have to go from a to b through a series of edges such that in the entire path you can use at most 1 curved edge. Your task is to find the shortest path from a to b satisfying the above condition. If there is no path from a to b, return -1.

Examples:

Input: n = 4, m = 4, a = 2, b = 4, edges = {{1, 2, 1, 4}, {1, 3, 2, 4}, {1, 4, 3, 1}, {2, 4, 6, 5}}
Output: 2
Explanation: We can follow the path 2->1->4. This gives a distance of 1+3 = 4 if we follow all straight paths. But we can take the curved path  from 1 -> 4, which costs 1. This will result in a cost of 1+1 = 2



Input: n = 2, m = 1, a = 1, b = 2, edges = {{1, 2, 4, 1}}
Output : 1
Explanation: Take the curved path from 1 to 2 which costs 1.



Try it on GfG Practice
redirect icon
Approach: To solve the problem follow the below idea:

The idea is to use Dijkstra's algorithm to find the shortest path from source vertex a to all other vertices in the graph using the straight edges and store the result in array da[], and then from the destination vertex b to all other vertices and store the result in db[].
Now, iterate through all the curved edges in the graph and find the minimum distance between node a and node b that we can get by taking at most one curved edge.
We can find this by calculating the distance from a to u and from v to b, where (u, v, cw) is the curved edge plus the weights of the curved edge.
Now take the minimum of this value and the existing minimum distance from a to b that is stored in da[b]. Hence we are checking all the possibilities of taking exactly one curved edge, so we can guarantee that we are getting the shortest distance.
For each node, we have to find minimum of da[u] + cw + db[v] and da[v] + cw + db[u], cw is the weight of curved edge u - v, da[u] = minimum distance of node a to u without curved edge. db[u] = minimum distance of node b to u without curved edge.
Now, check if the resulting minimum distance is greater than or equal to 1000000001, that indicates that there is no path from a to b, and return -1.
Below are the steps for the above approach:

Make an adjacency list from the given edges.
Run Dijkstra considering node a, as the source node to find the shortest distance from node a to all other nodes in the graph and store the result in a vector say da where each element represents the shortest distance from node a to that node.
Run Dijkstra considering node b, as the source node to find the shortest distance from node b, to all other nodes in the graph and store the result in a vector say db where each element represents the shortest distance from node b to that node.
Initialize a variable say ans = da[b], means without using any curved edges.
Run a loop over the edges, and find minimum of da[u] + cw + db[v] and da[v] + cw + db[u].
If ans is greater than or equal to 1000000001, return -1. Else, return ans.
Below are the steps for the above approach:




1
import heapq
2
​
3
​
4
def dijkstra(u, b, n, adj):
5
    dis = [1000000001] * (n+1)
6
    pq = [(0, u)]
7
    dis[u] = 0
8
​
9
    while pq:
10
        d, u = heapq.heappop(pq)
11
​
12
        if d > dis[u]:
13
            continue
14
​
15
        for v, w in adj[u]:
16
            if dis[v] > dis[u] + w:
17
                dis[v] = dis[u] + w
18
                heapq.heappush(pq, (dis[v], v))
19
​
20
    return dis
21
​
22
​
23
def shortest_path(n, m, a, b, edges):
24
    adj = [[] for _ in range(n+1)]
25
    curved = []
26
​
27
    for u, v, w, cw in edges:
28
        adj[u].append((v, w))
29
        adj[v].append((u, w))
30
        curved.append((u, v, cw))
31
​
32
    da = dijkstra(a, b, n, adj)
33
    db = dijkstra(b, a, n, adj)
34
    ans = da[b]
35
​
36
    for u, v, cw in curved:
37
        ans = min(ans, da[u] + cw + db[v])
38
        ans = min(ans, da[v] + cw + db[u])
39
​
40
    if ans >= 1000000001:
41
        return -1
42
    return ans
43
​
44
​
45
# Driver code
46
if __name__ == '__main__':
47
    n, m = 4, 4
48
    a, b = 2, 4
49
    edges = [
50
        [1, 2, 1, 4],
51
        [1, 3, 2, 4],
52
        [1, 4, 3, 1],
53
        [2, 4, 6, 5]
54
    ]
55
    ans = shortest_path(n, m, a, b, edges)
56
    print(ans)

Output
2
Time Complexity: O((m+n)log(n)), As we the has n nodes and m edges
Auxiliary Space: O(n+m), For storing the adjacency list and distance vector

Related Articles:

Introduction to Graphs – Data Structure and Algorithm Tutorials

"""










