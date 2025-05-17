

"""
A minimum spanning tree (MST) and a shortest path tree differ in their goals. An MST aims to find a subset of
edges from a graph that connects all vertices with the minimum total edge weight, forming a tree. A shortest
path tree, on the other hand, finds a tree rooted at a specific vertex where the path from the root to any other
 vertex is the shortest path in the graph.
Key Differences:
Objective:
MST minimizes the total weight of all edges in the tree, while a shortest path tree focuses on minimizing distances
 from a specific root vertex.
Output:
MST is a tree that connects all vertices with minimal total cost, and a shortest path tree is a rooted tree where
the path from the root to each vertex is the shortest path.
Uniqueness:
A MST is unique (except for ties in edge weights), while a shortest path tree is not necessarily unique.
Paths between vertices:
In an MST, the path between two vertices might not be the shortest path between those vertices in the graph. In a
shortest path tree, all paths from the root to any other vertex are the shortest paths.
In simpler terms:
Imagine you're building a network between several cities. A MST would be the cheapest way to connect all cities,
even if some routes might be longer than others. A shortest path tree would focus on finding the quickest way to
get from one specific city to all others, regardless of overall network cost.



        ------geek---------

Difference between Minimum Spanning Tree and Shortest Path
Last Updated : 01 Jul, 2021
Spanning tree: A spanning tree (T) of an undirected graph(G) is a subgraph which is a tree that includes all the
 vertices of a graph (G) and the minimum number of edges required to connect the graph (G). And it is a known
 maximal set of edges with no cycles.

Properties:

If a graph(G) is not connected then it does not contain a spanning tree (i.e. it has many spanning-tree forests).
If a graph(G) has V vertices then the spanning tree of that graph G has V-1 edges.
In the case of a complete (Kn) undirected, labeled, and unweighted graph, the number of possible spanning trees
can be found out By using Cayley’s formula: Kn = nn-2.
For the K3 graph (i.e. complete graph of 3 vertices) the number of possible spanning trees is 33-2 = 31= 3.

Possible spanning trees in K3 graph

The number of minimum spanning trees of a graph other than a complete graph can find out by using the Kirchhoff theorem.
The Shortest path:


Shortest path(A, B, D, E) between vertices A and E in the weighted directed graph

The shortest path between any two vertices (say between A and E) in a graph such that the sum of weights of edges
that are present in the path (i.e. ABDE) is minimum among all possible paths between A and E.
The shortest path can find out for graphs which are directed, undirected or mixed.
The problem for finding the shortest path can be categorized as
Single-source the shortest path: In this, the shortest path is calculated from a source vertex to all other vertices
 present inside the graph.
Single-destination the shortest path: In this, the shortest path is calculated from all vertices in the directed
graph to a single destination vertex. This can be converted into a single pair with the shortest path problem by
reversing the edges of the directed graph.
All pairs the shortest path: In this, the shortest path is calculated between every pair of vertices.
The followings are the difference between the Minimum spanning tree(MST) and the Shortest path:



Minimum spanning tree(MST)	The Shortest path
In MST there is no source and no destination, but it is the subset (tree) of the graph(G) which connects all the
vertices of the graph G without any cycles and the minimum possible total edge weight.	There is a source and
destination, and one need to find out the shortest path between them
Graph (G) should be connected, undirected, edge-weighted, labeled.	It is not necessary for the Graph (G) to be
connected, undirected, edge-weighted, labeled.
Here relaxation of edges is not performed but here the minimum edge weight is chosen one by one from the set of
all edge weights (sorted according to min weight) and the tree is formed by them (i.e. there should not be any cycle).

Here the relaxation of edges is performed.



Here d(U) means the distance of source vertex S to vertex where C(U, V) is the distance between U and V.
If d(U) > d(V) + C(U, V) then d(U) = d(V) + C(U, V).
For example, 20>10+5, d(U) = 15, is the minimum distance from source vertex S to vertex U.
Therefore, relaxation is performed.
In this case, a minimum spanning tree can be formed but negative weights edge cycles are not generally used. Using
the cycle property of MST, the minimum edge weight among all the edge weights in the negative edge cycle can be
selected.	If the graph is connected, and if a negative weight edge cycle present in the graph. Then the shortest
 path can not be computed, but the negative edge cycle can be detected using the Bellman-Ford algorithm.
In the case of a disconnected graph, the minimum spanning tree can not be formed but many spanning-tree forests can
 be formed.	In the case of a disconnected graph, the distance between two vertices present in two different components
  is infinity.
Here the Greedy approach is used for finding MST for a graph, For example, Prim’s algorithm and Kruskal’s algorithm.

The Dijkstra algorithm based on the Greedy approach and Bellman ford based on Dynamic programming are generally
used for finding the single-source shortest paths.
Floyd-War shall algorithm based on the Dynamic programming is used for finding all pairs the shortest path.
If there are N vertices are present inside graph G then the minimum spanning tree of the graph will contain N-1
edges and N vertices.	If there are N vertices present inside graph G, then in the shortest path between two
vertices there can be at most N-1 edges, and at most N vertices can be present in the shortest path.
It is used in network design (computer networks, telecommunication networks, water supply networks) and in circuit
design applications, and many more.	It is used to find out direction between physical locations like in Google Maps.












"""
"""
safe edge
In the context of Minimum Spanning Trees (MSTs), a safe edge is an edge that can be added to a current subset of 
an MST without violating the MST's properties. Essentially, it's an edge that, if added, will still result in a valid MST. 
More formally:
Safe edge for a subgraph A:
An edge e is safe for a subgraph A (a subset of the edges of a connected graph) if A ∪ {e} is also a subset of 
some MST. In simpler terms, adding e to A doesn't make A stop being a subset of a potential MST. 
Safe edge theorem:
This theorem states that a light edge (an edge with the minimum weight crossing a cut that respects a set of edges)
 is always a safe edge. 
Key points about safe edges:
Prims Algorithm: In Prim's algorithm, a safe edge is always the least-weighted edge connecting the growing tree to
 a vertex not yet in the tree. 
Kruskal's Algorithm: Kruskal's algorithm relies on the fact that safe edges can be added greedily to a growing MST. 
Relationship to Minimum Spanning Trees: Every safe edge must be part of some minimum spanning tree. 
Example:
Imagine a graph with two distinct components, represented by sets of vertices S and V-S. If an edge (u,v) connects
 a vertex u in S to a vertex v in V-S and (u,v) is the minimum-weight edge crossing the cut (S, V-S), then (u,v)
  is a safe edge. Adding this edge will connect the two components without increasing the total weight of the edges
   in the subgraph, and the resulting subgraph remains a potential subset of an MST. 


Generic-MST(G, w)
  1   A = φ
  2   while A does not form a spanning tree
  3       find an edge (u,v) that is safe for A
  4       A = A ∪ {(u,v)}
  5   return A
  
Invariant: Prior to each iteration, A is a subset of some minimum spanning tree.

Safe edge: An edge that may be added to A without violating the invariant that A is a subset of some 
minimum spanning tree.

Cut: is a partition of V into S and V−S.

Crossing: An edge (u,v) ∈ E crosses the cut (S, V−S) if one of its endpoints is in S and the other is in (V−S).

Respecting: A cut respects a set A of edges if no edge in A crosses the cut.

Light edge: An edge is a light edge crossing a cut if its weight is the minimum of any edge crossing the 
cut. Note that there may be more than one light edge.

"""
"""
The generic minimum spanning tree (MST) algorithm is a greedy approach to finding the MST of a connected,
undirected graph. It works by iteratively adding "safe" edges to a set until the set forms a spanning tree.
A safe edge is one that can be added without creating a cycle and is part of some minimum spanning tree. 
Here's a more detailed breakdown:
Initialization: Start with an empty set of edges, A. 
Iteration: While A is not a spanning tree (i.e., doesn't connect all vertices):
Find a safe edge: Identify an edge (u, v) that can be added to A without creating a cycle and is part of some
minimum spanning tree. 
Add the safe edge: Add (u, v) to the set A. 
Termination: The algorithm terminates when A becomes a spanning tree (i.e., it connects all vertices with |V|-1
edges, where |V| is the number of vertices). 
Return: Return the set A, which now contains the edges of a minimum spanning tree. 
Key Concepts:
Loop Invariant: At each step, A is a subset of some minimum spanning tree. 
Safe Edge: An edge that can be added to A without violating the loop invariant. 
Greedy Approach: The algorithm always tries to add the "best" possible edge at each step (in terms of minimizing 
the total weight of the MST). 
Specific Implementations (e.g., Kruskal's and Prim's algorithms) build upon this generic framework by providing 
specific strategies for finding "safe" edges:
Kruskal's Algorithm:
Iterates through the sorted edges in non-decreasing order and adds an edge if it connects different connected 
components (trees). 
Prim's Algorithm:
Starts with a single vertex and iteratively grows the MST by adding the lightest edge that connects a vertex in
the tree to a vertex outside the tree. 


"""









