

"""
A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected, and undirected graph is a spanning tree (no cycles and connects all vertices) that has minimum weight. The weight of a spanning tree is the sum of all edges in the tree.

In Kruskal’s algorithm, we sort all edges of the given graph in increasing order. Then it keeps on adding new edges and nodes in the MST if the newly added edge does not form a cycle. It picks the minimum weighted edge at first and the maximum weighted edge at last. Thus we can say that it makes a locally optimal choice in each step in order to find the optimal solution. Hence this is a Greedy Algorithm.

How to find MST using Kruskal’s algorithm?
Below are the steps for finding MST using Kruskal’s algorithm:

Sort all the edges in a non-decreasing order of their weight.
Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If the cycle is not formed, include this edge. Else, discard it.
Repeat step 2 until there are (V-1) edges in the spanning tree.
Kruskal’s Algorithm uses the Disjoint Set Data Structure to detect cycles.

Illustration:
The graph contains 9 vertices and 14 edges. So, the minimum spanning tree formed will be having (9 – 1) = 8 edges.


Kruskals-Minimum-Spanning-Tree-MST-Algorithm-1.webpKruskals-Minimum-Spanning-Tree-MST-Algorithm-1.webp




Try it on GfG Practice
redirect icon



1
from functools import cmp_to_key
2
​
3
def comparator(a,b):
4
    return a[2] - b[2];
5
​
6
def kruskals_mst(V, edges):
7
​
8
    # Sort all edges
9
    edges = sorted(edges,key=cmp_to_key(comparator))
10

11
    # Traverse edges in sorted order
12
    dsu = DSU(V)
13
    cost = 0
14
    count = 0
15
    for x, y, w in edges:
16

17
        # Make sure that there is no cycle
18
        if dsu.find(x) != dsu.find(y):
19
            dsu.union(x, y)
20
            cost += w
21
            count += 1
22
            if count == V - 1:
23
                break
24
    return cost
25

26
# Disjoint set data structure
27
class DSU:
28
    def __init__(self, n):
29
        self.parent = list(range(n))
30
        self.rank = [1] * n
31
​
32
    def find(self, i):
33
        if self.parent[i] != i:
34
            self.parent[i] = self.find(self.parent[i])
35
        return self.parent[i]
36
​
37
    def union(self, x, y):
38
        s1 = self.find(x)
39
        s2 = self.find(y)
40
        if s1 != s2:
41
            if self.rank[s1] < self.rank[s2]:
42
                self.parent[s1] = s2
43
            elif self.rank[s1] > self.rank[s2]:
44
                self.parent[s2] = s1
45
            else:
46
                self.parent[s2] = s1
47
                self.rank[s1] += 1
48
​
49
​
50
if __name__ == '__main__':
51

52
    # An edge contains, weight, source and destination
53
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
54
    print(kruskals_mst(4, edges))

Output
Following are the edges in the constructed MST
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Minimum Cost Spanning Tree: 19
Time Complexity: O(E * log E) or O(E * log V)

Sorting of edges takes O(E*logE) time.
After sorting, we iterate through all edges and apply the find-union algorithm. The find and union operations can take at most O(logV) time.
So overall complexity is O(E*logE + E*logV) time.
The value of E can be at most O(V2), so O(logV) and O(logE) are the same. Therefore, the overall time complexity is O(E * logE) or O(E*logV)
Auxiliary Space: O(E+V), where V is the number of vertices and E is the number of edges in the graph.

Problems based on Minimum Spanning Tree
Prim’s Algorithm for MST
Minimum cost to connect all cities
Minimum cost to provide water
Second Best Minimum Spanning Tree
Check if an edge is a part of any MST
Minimize count of connections

"""




