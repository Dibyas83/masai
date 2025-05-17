

"""
Given a matrix dist[][] of size n x n, where dist[i][j] represents the weight of the edge from node i to node j. If there is no direct edge, dist[i][j] is set to a large value (e.g., 10⁸) to represent infinity. The diagonal entries dist[i][i] are 0, since the distance from a node to itself is zero. The graph may contain negative edge weights, but it does not contain any negative weight cycles.

Your task is to determine the shortest path distance between all pair of nodes i and j in the graph.

Example:

Input: dist[][] = [[0, 4, 10⁸, 5, 10⁸],
                           [10⁸, 0, 1,  10⁸, 6],
                           [2, 10⁸, 0, 3, 10⁸],
                           [10⁸, 10⁸, 1, 0, 2],
                          [1, 10⁸, 10⁸, 4, 0]]


5
Output:[[0, 4, 5, 5, 7],
              [3, 0, 1, 4, 6],
              [2, 6, 0, 3, 5],
             [3, 7, 1, 0, 2],
             [1, 5, 5, 4, 0]]
Explanation:


1
Each cell dist[i][j] in the output shows the shortest distance from node i to node j, computed by considering all possible intermediate nodes using the Floyd-Warshall algorithm.


Try it on GfG Practice
redirect icon
Floyd Warshall Algorithm:
The Floyd–Warshall algorithm works by maintaining a two-dimensional array that represents the distances between nodes. Initially, this array is filled using only the direct edges between nodes. Then, the algorithm gradually updates these distances by checking if shorter paths exist through intermediate nodes.

This algorithm works for both the directed and undirected weighted graphs and can handle graphs with both positive and negative weight edges.

Note: It does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative).

Idea Behind Floyd Warshall Algorithm:
Suppose we have a graph dist[][] with V vertices from 0 to V-1. Now we have to evaluate a dist[][] where dist[i][j] represents the shortest path between vertex i to j.


Let us assume that vertices i to j have intermediate nodes. The idea behind Floyd Warshall algorithm is to treat each and every vertex k from 0 to V-1 as an intermediate node one by one. When we consider the vertex k, we must have considered vertices from 0 to k-1 already. So we use the shortest paths built by previous vertices to build shorter paths with vertex k included.


The following figure shows the above optimal substructure property in Floyd Warshall algorithm:



Why Floyd Warshall Works (Correctness Proof)?
The algorithm relies on the principle of optimal substructure, meaning:

If the shortest path from i to j passes through some vertex k, then the path from i to k and the path from k to j must also be shortest paths.
The iterative approach ensures that by the time vertex k is considered, all shortest paths using only vertices 0 to k-1 have already been computed.
By the end of the algorithm, all shortest paths are computed optimally because each possible intermediate vertex has been considered.

Why Floyd-Warshall Algorithm better for Dense Graphs and not for Sparse Graphs?
Dense Graph: A graph in which the number of edges are significantly much higher than the number of vertices.
Sparse Graph: A graph in which the number of edges are very much low.


No matter how many edges are there in the graph the Floyd Warshall Algorithm runs for O(V3) times therefore it is best suited for Dense graphs. In the case of sparse graphs, Johnson’s Algorithm is more suitable.


Step-by-step implementation

Start by updating the distance matrix by treating each vertex as a possible intermediate node between all pairs of vertices.
Iterate through each vertex, one at a time. For each selected vertex k, attempt to improve the shortest paths that pass through it.
When we pick vertex number k as an intermediate vertex, we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices.
For every pair (i, j) of the source and destination vertices respectively, there are two possible cases.
k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is.
k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k] + dist[k][j], if dist[i][j] > dist[i][k] + dist[k][j]
Repeat this process for each vertex k until all intermediate possibilities have been considered.
Illustration:

Floyd-Warshall-Algorithm-01.webpFloyd-Warshall-Algorithm-01.webp





1
# Solves the all-pairs shortest path
2
# problem using Floyd Warshall algorithm
3
def floydWarshall(dist):
4
    V = len(dist)
5
​
6
    # Add all vertices one by one to
7
    # the set of intermediate vertices.
8
    for k in range(V):
9
​
10
        # Pick all vertices as source one by one
11
        for i in range(V):
12
​
13
            # Pick all vertices as destination
14
            # for the above picked source
15
            for j in range(V):
16
                #shortest path from
17
                #i to j
18
                if(dist[i][k] != 100000000 and dist[k][j]!= 100000000):
19
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j]);
20
​
21
if __name__ == "__main__":
22

23
    INF = 100000000;
24
    dist = [
25
        [0, 4, INF, 5, INF],
26
        [INF, 0, 1, INF, 6],
27
        [2, INF, 0, 3, INF],
28
        [INF, INF, 1, 0, 2],
29
        [1, INF, INF, 4, 0]
30
    ]
31

32
    floydWarshall(dist)
33
    for i in range(len(dist)):
34
        for j in range(len(dist)):
35
            print(dist[i][j], end=" ")
36
        print()

Output
0 4 5 5 7
3 0 1 4 6
2 6 0 3 5
3 7 1 0 2
1 5 5 4 0
Time Complexity: O(V3), where V is the number of vertices in the graph and we run three nested loops each of size V.
Auxiliary Space: O(1).

Read here for detailed analysis: complexity analysis of the Floyd Warshall algorithm


Note: The above program only prints the shortest distances. We can modify the solution to print the shortest paths also by storing the predecessor information in a separate 2D matrix.

Real World Applications of Floyd-Warshall Algorithm
In computer networking, the algorithm can be used to find the shortest path between all pairs of nodes in a network. This is termed as network routing.
Flight Connectivity In the aviation industry to find the shortest path between the airports.
GIS(Geographic Information Systems) applications often involve analyzing spatial data, such as road networks, to find the shortest paths between locations.
Kleene’s algorithm which is a generalization of floyd warshall, can be used to find regular expression for a regular language.
Important Interview questions related to Floyd-Warshall
How to Detect Negative Cycle in a graph using Floyd Warshall Algorithm?
How is Floyd-warshall algorithm different from Dijkstra’s algorithm?
How is Floyd-warshall algorithm different from Bellman-Ford algorithm?


"""

"""
Detecting negative cycle using Floyd Warshall
Last Updated : 13 Oct, 2023
We are given a directed graph. We need compute whether the graph has negative cycle or not. A negative cycle is one in which the overall sum of the cycle comes negative.

negative_cycle

Negative weights are found in various applications of graphs. For example, instead of paying cost for a path, we may get some advantage if we follow the path.

Examples: 

Input : 4 4
        0 1 1
        1 2 -1
        2 3 -1
        3 0 -1

Output : Yes
The graph contains a negative cycle.
Detecting negative cycle using Floyd Warshall

We have discussed Bellman Ford Algorithm based solution for this problem.
In this post, Floyd Warshall Algorithm based solution is discussed that works for both connected and disconnected graphs.
Distance of any node from itself is always zero. But in some cases, as in this example, when we traverse further from 4 to 1, the distance comes out to be -2, i.e. distance of 1 from 1 will become -2. This is our catch, we just have to check the nodes distance from itself and if it comes out to be negative, we will detect the required negative cycle.

Implementation:




# Python Program to check
# if there is a
# negative weight
# cycle using Floyd
# Warshall Algorithm
 
  
# Number of vertices
# in the graph
V = 4
      
# Define Infinite as a
# large enough value. This 
# value will be used 
#for vertices not connected 
# to each other 
INF = 99999
      
# Returns true if graph has
# negative weight cycle
# else false.
def negCyclefloydWarshall(graph):
          
    # dist[][] will be the
    # output matrix that will 
    # finally have the shortest 
    # distances between every
    # pair of vertices 
    dist=[[0 for i in range(V+1)]for j in range(V+1)]
      
    # Initialize the solution
    # matrix same as input
    # graph matrix. Or we can
    # say the initial values 
    # of shortest distances
    # are based on shortest 
    # paths considering no
    # intermediate vertex. 
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
      
    ''' Add all vertices one
        by one to the set of 
        intermediate vertices.
    ---> Before start of a iteration,
         we have shortest
        distances between all pairs
        of vertices such 
        that the shortest distances
        consider only the
        vertices in set {0, 1, 2, .. k-1}
        as intermediate vertices.
    ----> After the end of a iteration,
          vertex no. k is 
        added to the set of
        intermediate vertices and 
        the set becomes {0, 1, 2, .. k} '''
    for k in range(V):
     
        # Pick all vertices 
        # as source one by one
        for i in range(V):
                  
            # Pick all vertices as
            # destination for the
            # above picked source
            for j in range(V):
         
                # If vertex k is on
                # the shortest path from
                # i to j, then update
                # the value of dist[i][j]
                if (dist[i][k] + dist[k][j] < dist[i][j]):
                        dist[i][j] = dist[i][k] + dist[k][j]
  
    # If distance of any
    # vertex from itself
    # becomes negative, then
    # there is a negative
    # weight cycle.
    for i in range(V):
        if (dist[i][i] < 0):
            return True
  
    return False
 
          
# Driver code
 
      
''' Let us create the
    following weighted graph
            1
    (0)----------->(1)
    /|\               |
     |               |
  -1 |               | -1
     |                \|/
    (3)<-----------(2)
        -1     '''
          
graph = [ [0, 1, INF, INF],
          [INF, 0, -1, INF],
          [INF, INF, 0, -1],
          [-1, INF, INF, 0]]
          
if (negCyclefloydWarshall(graph)):
    print("Yes")
else:
    print("No") 
 
# This code is contributed
# by Anant Agarwal.
Output
Yes
The time complexity of the Floyd Warshall algorithm is O(V^3) where V is the number of vertices in the graph. This is because the algorithm uses a nested loop structure, where the outermost loop runs V times, the middle loop runs V times and the innermost loop also runs V times. Therefore, the total number of iterations is V * V * V which results in O(V^3) time complexity.

The space complexity of the Floyd Warshall algorithm is O(V^2) where V is the number of vertices in the graph. This is because the algorithm uses a 2D array of size V x V to store the shortest distances between every pair of vertices. Therefore, the total space required is V * V which results in O(V^2) space complexity.


"""

"""
Comparison of Dijkstra’s and Floyd–Warshall algorithms
Last Updated : 16 Oct, 2023
Dijkstra Algorithm

Dijkstra’s Algorithm is a Single-Source Shortest Path SSSP algorithm, i.e., given a source vertex it finds the shortest path from the source to all other vertices. The idea is to generate a SPT (shortest path tree) with a given source as a root and with two sets, 


one set contains vertices included in the shortest-path tree, 
other set includes vertices not yet included in the shortest-path tree. 

At every step of the algorithm, find a vertex that is in the other set (set not yet included) and has a minimum distance from the source.


Floyd Warshall Algorithm

Floyd Warshall Algorithm is All-Pair Shortest Path algorithm, which is to find shortest distance between all pair of vertices. The idea is to use a 2-D Distance Array and initialize it with direct edge weights and then iteratively considers all possible intermediate vertices to update the array. The algorithm checks if a path through an intermediate vertex offers a shorter distance between two nodes.


Comparison of Dijkstra’s and Floyd–Warshall algorithms on the basis of algorithm:
Dijkstra Algorithm:

Dijkstra’s Algorithm uses a Greedy approach to find the shortest path from the source to all other vertices. It starts from the source vertex and maintains a set of vertices with known minimum distances from the source. The key idea of the Greedy strategy is selecting the vertex with the currently shortest known distance from the Source and exploring it next. 


Floyd Warshall Algorithm:

Floyd Warshall Algorithm uses Dynamic Programming approach to compute shortest distance between all pair of vertices. The idea of dp approach is to maintain a 2-D Distance Array and initialize it with direct edge weights effectively solving the subproblems for vertex pairs that have direct connections. It then considers additional intermediate vertices to optimize the paths between all pairs.


Comparison of Dijkstra’s and Floyd–Warshall algorithms on the basis of Complexity Analysis:
Dijkstra Algorithm:

The time complexity of Dijkstra Algorithm depends on the specific implementation and data structures used. In a straightforward implementation for dense graphs where E (no. of edges) is approximately equal to V2  (no. of Vertices)  time complexity is of O(V2) . However, for Sparse graphs using Priority queue or Min-heap is more optimal which gives time complexity of  O(E + V*log(V)).


Floyd Warshall Algorithm:

For the Floyd Warshall Algorithm, the time complexity is O(V^3), where V represents the number of vertices in the graph. It involves three nested loops that iterate through all possible pairs of nodes and consider all possible intermediaries, leading to a cubic time complexity.


Complete Comparison of Dijkstra’s and Floyd–Warshall algorithms
Comparison Basis

Dijkstra Algorithm

Floyd Warshall Algorithm

Introduction

Dijkstra’s algorithm is a single-source shortest path algorithm used to find the shortest paths from a single source vertex to all other vertices in a weighted graph.

The Floyd-Warshall algorithm is an all-pairs shortest path algorithm used to find the shortest paths between all pairs of vertices in a weighted graph.

Algorithm

Greedy approach,as it selects the vertex with the shortest distance

It uses Dynamic programming, to compute all pair shortest paths.

Data Structure

It Typically uses a priority queue or min-heap.

It uses a two-dimensional array.

Negative Edges

Dijkstra’s algorithm does not work correctly with graphs that have negative edge weights.

The Floyd-Warshall algorithm can handle graphs with both positive and negative edge weights.

Time Complexity

With a priority queue or min-heap, time complexity is O(E + V*log(V)).

The time complexity of the Floyd-Warshall algorithm is O(V^3).

Auxilary Space

O(V) with priority queue or min-heap.

The auxiliary space complexity is O(V^2) because of 2D array used.

Use Case

It is efficient for finding shortest paths from a single source.

It is suitable for finding shortest paths between all pairs of vertices


"""

"""
Bellman-Ford vs Floyd-Warshall's algorithm: A Comparative Analysis
Last Updated : 05 Jan, 2024
Bellman-Ford Algorithm:
The Bellman-Ford algorithm is a single-source shortest-path algorithm that works by iteratively relaxing edges in the graph until the shortest path to all vertices is found. It is especially useful for graphs with negative edge weights, as it can detect negative cycles and return a suitable error message.



Floyd-Warshall Algorithm:
The Floyd-Warshall algorithm is a multi-source shortest path algorithm that works by computing the shortest path between all pairs of vertices in the graph using dynamic programming. It is known for its simplicity and ease of implementation, making it a popular choice in many applications.



In this article, we will compare and contrast the Bellman-Ford algorithm and the Floyd-Warshall algorithm, examining their respective strengths and weaknesses, time and space complexity, and implementation details.

As we know that both of these algorithms work on Directed Graphs, Let us take a common example to understand the approaches of these algorithms.


Given a directed, weighted Graph
Bellman-ford's Algorithm
The Bellman-Ford algorithm can be implemented as follows:

Initialize the distance from the source vertex (i.e. 0) to all other vertices in the graph to infinity, except for the distance from the source vertex to itself, which is 0.
For each vertex in the graph, repeat the following process |V|-1 times (where |V| is the number of vertices in the graph):
For each edge (u, v) in the graph, where u is the source vertex and v is the destination vertex, relax the edge by updating the distance to v if the distance to u plus the weight of (u, v) is less than the current distance to v.
After the (|V|-1)th iteration, check for the presence of negative cycles by iterating over all the edges in the graph and checking if any of them can still be relaxed. If so, then a negative cycle is present, and the algorithm returns a suitable error message.
Here's how the algorithm would work:

Initialize the distance from A to all other vertices to infinity, except for the distance from A to itself, which is 0: dist[0] = 0.
Repeat the process of relaxing edges 5 times (|V|-1 = 6-1 = 5) to relax all edges in the graph.
Check for negative cycles by iterating over all edges in the graph. In this case, there are no negative cycles, as all edges have been relaxed in the previous step.
Hence our distance from source 0 to each node will look like this,


Distance Array
Implementation of Bellman-Ford's Algorithm:



1
# python code for the above approach:
2
class Solution:
3
    def shortest_paths(self, grid, V):
4
        dist = [float('inf')] * V
5
​
6
        # Taking 0 as our source
7
        dist[0] = 0
8
​
9
        # Relaxing V-1 times
10
        for i in range(V):
11
            # For each value in the given
12
            # list of [u, v, wt]
13
            for u, v, wt in grid:
14
                # If there exists a better
15
                # distance and previous dist
16
                # of u should not be infinite
17
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
18
                    dist[v] = dist[u] + wt
19
​
20
        # If negative cycle exists then
21
        # it will still reduce for
22
        # Vth traversal
23
        for u, v, wt in grid:
24
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
25
                print("ERROR ALERT, Negative Cycle exists")
26
​
27
        print("The shortest distances from ")
28
        for i in range(V):
29
            print(" 0 to", i, "--->", dist[i])
30
​
31
​
32
# Driver code
33
if __name__ == "__main__":
34
    V = 6
35
    grid = [[0, 1, 2], [0, 3, 5], [0, 4, 3], [1, 0, 3], [1, 5, 6], [
36
        1, 2, 2], [1, 3, 2], [2, 5, 1], [2, 3, 1], [3, 4, 1], [4, 3, 2]]
37
    s1 = Solution()
38
​
39
    # Function call
40
    s1.shortest_paths(grid, V)

Output
The shortest distances from 
 0 to 0 ---> 0
 0 to 1 ---> 2
 0 to 2 ---> 4
 0 to 3 ---> 4
 0 to 4 ---> 3
 0 to 5 ---> 5
Time complexity: O(|V||E|)
Auxiliary space: O(|V|)

Floyd-Warshall's Algorithm
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of nodes in a weighted graph. It works by maintaining a distance matrix where each entry (i, j) represents the shortest distance from node i to node j. The algorithm starts by initializing the distance matrix with the weights of the edges in the graph. Then, it iteratively updates the distance matrix by considering all possible intermediate nodes and choosing the path with the minimum total weight.



Implementation of Floyd-Warshall's Algorithm:



1
# Python code for the above approach:
2
​
3
class Solution:
4
    def shortest_dist(self, matrix):
5
        N = len(matrix)
6
​
7
        # changing value of -1 
8
        # to infinite
9
        for i in range(N):
10
            for j in range(N):
11
                if matrix[i][j] == -1:
12
                    matrix[i][j] = float('inf')
13
​
14
                # The distance of node to 
15
                # itself will be 0.
16
                if i == j:
17
                    matrix[i][j] = 0
18
​
19
        # Assign the better distance 
20
        # (if exist) in the matrix
21
        # one by one making each node 
22
        # as our intermediate node
23
        for via in range(N):
24
            for i in range(N):
25
                for j in range(N):
26
                    matrix[i][j] = min(matrix[i][j], matrix[i][via] + matrix[via][j])
27
​
28
        # Replacing infinity to -1, 
29
        # after the work is done
30
        for i in range(N):
31
            for j in range(N):
32
                if matrix[i][j] == float('inf'):
33
                    matrix[i][j] = -1
34
​
35
# Driver code
36
if __name__ == "__main__":
37
    grid = [[0, 1, 2], [0, 3, 5], [0, 4, 3], [1, 0, 3], [1, 5, 6], [1, 2, 2], [1, 3, 2], [2, 5, 1], [2, 3, 1], [3, 4, 1], [4, 3, 2]]
38
    V = 6
39
    matrix = [[-1 for _ in range(V)] for _ in range(V)]
40
​
41
    # Creating matrix representation
42
    for it in grid:
43
        u, v, wt = it[0], it[1], it[2]
44
        matrix[u][v] = wt
45
​
46
    obj = Solution()
47
​
48
    # Function call
49
    obj.shortest_dist(matrix)
50
​
51
    for row in matrix:
52
        for it in row:
53
            if it == -1:
54
                it = -1
55
            print(it, end="\t")
56
        print()
57
​
58
​
59
# This code is contributed by Pushpesh raj

Output
0    2    4    4    3    5    
3    0    2    2    3    3    
-1    -1    0    1    2    1    
-1    -1    -1    0    1    -1    
-1    -1    -1    2    0    -1    
-1    -1    -1    -1    -1    0    
Time complexity: O(N^3)
Auxiliary Space: O(N^2)

"""

