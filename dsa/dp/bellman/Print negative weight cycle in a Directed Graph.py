
"""

Given a weighted directed graph consisting of V vertices and E edges. The task is to print the cyclic path whose sum of weight is negative. If there is no such path present then print “-1”.


Input: V = 5, E = 5, Below is the graph:



Here, for the given negative cycle o/p (1->2->3->4->1) ; In fig there has to be Edge from 4–>1  not from 4–>0





Output: 1 2 3 4 1
Explanation:
Given graph contains a negative cycle, (1->2->3->4->1)


Input: V = 5, E = 5, Below is the graph:






Output: 0 1 2 3 4 0
Explanation:
Given graph contains a negative cycle, (0->1->2->3->4->0)



Approach: The idea is to use Bellman-Ford Algorithm which is used to detect a negative cycle or not. To print the negative cycles, perform the Nth iteration of Bellman-Ford and pick a vertex from any edge which is relaxed in this iteration. Using this vertex and its ancestors, the negative cycle can be printed. Below are the steps:

Perform N-1 iterations of Bellman-Ford algorithm and relax each edge (u, v). Keep track of parent of each vertex and store in an array parent[].
Now, do one more iteration and if no edge relaxation take place in this Nth iteration, then there is no cycle of negative weight exists in the graph.
Otherwise take a variable C and store the vertex v from any edge (u, v), which is relaxed in the Nth iteration.
Now, starting from the C vertex go towards its ancestors until a cycle is found and finally print it.
This cycle will be the desired cycle of negative weight.
Below is the implementation of the above approach:




# Python3 program for the above approach

# Structure to represent a weighted
# edge in graph
class Edge:
    def __init__(self):
        self.src = 0
        self.dest = 0
        self.weight = 0

# Structure to represent a directed
# and weighted graph
class Graph:

    def __init__(self):

        # V. Number of vertices, E.
        # Number of edges
        self.V = 0
        self.E = 0

        # Graph is represented as
        # an array of edges.
        self.edge = []

# Creates a new graph with V vertices
# and E edges
def createGraph(V, E):
    graph = Graph();
    graph.V = V;
    graph.E = E;
    graph.edge = [Edge() for i in range(graph.E)]
    return graph;

# Function runs Bellman-Ford algorithm
# and prints negative cycle(if present)
def NegCycleBellmanFord(graph, src):
    V = graph.V;
    E = graph.E;
    dist =[1000000 for i in range(V)]
    parent =[-1 for i in range(V)]
    dist[src] = 0;

    # Relax all edges |V| - 1 times.
    for i in range(1, V):
        for j in range(E):

            u = graph.edge[j].src;
            v = graph.edge[j].dest;
            weight = graph.edge[j].weight;

            if (dist[u] != 1000000 and
                dist[u] + weight < dist[v]):

                dist[v] = dist[u] + weight;
                parent[v] = u;

    # Check for negative-weight cycles
    C = -1;
    for i in range(E):
        u = graph.edge[i].src;
        v = graph.edge[i].dest;
        weight = graph.edge[i].weight;

        if (dist[u] != 1000000 and
            dist[u] + weight < dist[v]):

            # Store one of the vertex of
            # the negative weight cycle
            C = v;
            break;

    if (C != -1):
        for i in range(V):
            C = parent[C];

        # To store the cycle vertex
        cycle = []
        v = C

        while (True):
            cycle.append(v)
            if (v == C and len(cycle) > 1):
                break;
            v = parent[v]

        # Reverse cycle[]
        cycle.reverse()

        # Printing the negative cycle
        for v in cycle:
            print(v, end = " ");
        print()
    else:
        print(-1);

# Driver Code
if __name__=='__main__':

    # Number of vertices in graph
    V = 5;

    # Number of edges in graph
    E = 5;
    graph = createGraph(V, E);

    # Given Graph
    graph.edge[0].src = 0;
    graph.edge[0].dest = 1;
    graph.edge[0].weight = 1;

    graph.edge[1].src = 1;
    graph.edge[1].dest = 2;
    graph.edge[1].weight = 2;

    graph.edge[2].src = 2;
    graph.edge[2].dest = 3;
    graph.edge[2].weight = 3;

    graph.edge[3].src = 3;
    graph.edge[3].dest = 4;
    graph.edge[3].weight = -3;

    graph.edge[4].src = 4;
    graph.edge[4].dest = 1;
    graph.edge[4].weight = -3;

    # Function Call
    NegCycleBellmanFord(graph, 0);

# This code is contributed by Pratham76
Output:
1 2 3 4 1


Time Complexity: O(V*E)
Auxiliary Space: O(V)
"""









