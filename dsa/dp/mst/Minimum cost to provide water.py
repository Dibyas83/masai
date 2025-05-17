
"""

Given an integer N, where N denotes the number of villages numbered 1 to N, an array wells[] where wells[i] denotes the cost to build a water well in the i'th city, a 2D array pipes in form of [X Y C] which denotes that the cost to connect village X and Y with water pipes is C. Your task is to provide water to each and every village either by building a well in the village or connecting it to some other village having water. Find the minimum cost to do so.

Examples:

Input: N=3, wells=[1, 2, 2], pipes=[[1 2 1], [2 3 1]]
Output: 3
Explanation: Build well in village1 to provide water with cost=1
connect village2 and village1 with cost =1 , now village1 and village2 have water.
Finally connect village3 with village2  with cost=1 , now all the villages have water with total cost=3.



Input: N=4, wells[1, 1, 1, 1], pipes=[[1 2 100], [2 3 100], [2 4 50]]
Output: 4
Explanation: Clearly its better to construct well at each village rather than building costly roads. Hence total cost=1+1+1+1=4.



Minimum Cost to provide water using Kruskal’s Minimum Spanning Tree (MST) Algorithm & Disjoint Set Union:
We can create a graph with villages as vertices and use pipes array to form edges between these villages, also we need to construct a pseudo vertex that is connected to each and every village 'i' with an edges weight of wells[i] , in this way we can take care of cost of building the pipes and wells simultaneously. The MST cost of this graph will give us our answer i.e. the minimum cost to provide water to each village.



Illustration:

Suppose, N=4, wells[1, 2, 1, 2], pipes=[[1 2 1], [1 3 3],[2 3 3], [3 4 1]]
Step 1: We construct the graph with villages as the vertex and use pipes array to form edges as shown in fig-1



Initial-graph-to-find-minimum-water-supply-cost
fig-1
Step 2: Create a pseudo node (0) and add edges from 0 to all other vertices from 1 to N , assign edge weight as wells[i] , for each 'i' 1 to N.



file
fig-2
Step 3: Find the MST of the above graph and return the MST cost= 1+1+1+1= 4 as the answer.



Finding-The-MST-For-Minimum-Water-Supply-Cost
fig-3
Step-by-step algorithm:

Firstly initialize the DSU data structure i.e. make(), find(), Union(), and parent array.
Create a set 'st' to store the edges sorted in ascending order on the basis of edge weight.
Insert the edges in 'st' using the pipes array.
Edges between villages(1 to N) and pseudo vertex(0) have to be inserted with edge weight=wells[i] for each village 'i'.
Apply Kruskal's MST algorithm on the set 'st'.
return the MST cost as the answer.
Below is the implementation of the above algorithm:




1
import heapq
2
​
3
# This function is used to initialize the DSU.
4
def make(i, parent, sizez):
5
    parent[i] = i
6
    sizez[i] = 1
7
​
8
# This function is used to find the parent of each component of DSU
9
def find(v, parent):
10
    if v == parent[v]:
11
        return v
12
    parent[v] = find(parent[v], parent)
13
    return parent[v]
14
​
15
# This function is used to merge two components of DSU
16
def union(a, b, parent, sizez):
17
    a = find(a, parent)
18
    b = find(b, parent)
19
    if a != b:
20
        if sizez[a] < sizez[b]:
21
            a, b = b, a
22
        parent[b] = a
23
        sizez[a] += sizez[b]
24
​
25
# Function to solve the problem
26
def min_cost_to_provide_water(n, wells, pipes):
27
    edges = []
28
​
29
    # Inserting the edges into the heap sorted by weights
30
    for pipe in pipes:
31
        u, v, wt = pipe
32
        edges.append((wt, u, v))
33
​
34
    # Inserting the edges created by the pseudo-vertex i.e., 0
35
    for i in range(n):
36
        edges.append((wells[i], 0, i + 1))
37
​
38
    # Initializing DSU
39
    parent = [0] * (n + 1)
40
    sizez = [0] * (n + 1)
41
    for i in range(n + 1):
42
        make(i, parent, sizez)
43
​
44
    answer = 0
45
​
46
    # Applying Kruskal's MST algorithm
47
    edges.sort()
48
    for edge in edges:
49
        wt, u, v = edge
50
        if find(u, parent) != find(v, parent):
51
            answer += wt
52
            union(u, v, parent, sizez)
53
​
54
    return answer
55
​
56
# Driver Function
57
if __name__ == "__main__":
58
    N = 3
59
    wells = [1, 2, 2]
60
    pipes = [
61
        (1, 2, 1),
62
        (2, 3, 1)
63
    ]
64
​
65
    # Function call
66
    print(min_cost_to_provide_water(N, wells, pipes))

Output
3
Time Complexity: O(E*log(N)), where E is the number of edges and N is the number of vertices in the formed graph.
Auxiliary Space: O(N)
"""
"""


"""








