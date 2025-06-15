
"""
Dijkstra’s Algorithm for Adjacency List Representation | Greedy Algo-8
Last Updated : 29 Mar, 2025
The Dijkstra's Algorithm, we can either use the matrix representation or the adjacency list representation to
represent the graph, while the time complexity of Dijkstra's Algorithm using matrix representation is O(V^2).
The time complexity of Dijkstra's Algorithm using adjacency list representation is O(ELogV). The adjacency list
representation not only reduces the space used by this algorithm but also optimizes its time complexity.

Examples:

Input:  src = 0, the graph is shown below.

1-(2)
Output:  0 4 12 19 21 11 9 8 14
Explanation:  Shortest Paths:
0 to 1 = 4.
0 to 2 = 12. 0->1->2
0 to 3 = 19. 0->1->2->3
0 to 4 = 21. 0->7->6->5->4
0 to 5 = 11. 0->7->6->5
0 to 6 = 9. 0->7->6
0 to 7 = 8. 0->7
0 to 8 = 14. 0->1->2->8

In Dijkstra's algorithm, two sets are maintained where one set contains a list of vertices already included
in SPT (Shortest Path Tree), and another set contains vertices not yet included. With adjacency list
representation, all vertices of a graph can be traversed in O(V+E) time using BFS.
The idea is to traverse all vertices of the graph using BFS and use a Min Heap to store the vertices not
yet included in SPT (or the vertices for which the shortest distance is not finalized yet).  Min Heap is
used as a priority queue to get the minimum distance vertex from a set of not-yet-included vertices.

Dijkstra’s Algorithm for Adjacency List Representation using Min heap
Create a Min Heap of size V where V is the number of vertices in the graph. Every node of the min-heap contains
 the vertex number and distance value of the vertex.
Initialize Min Heap with source vertex as root (the distance value assigned to source vertex is 0). The distance
value assigned to all other vertices is INF (infinite).

While Min Heap is not empty, do the following :
Extract the vertex with minimum distance value node from Min Heap. Let the extracted vertex be u.

For every adjacent vertex v of u, check if v is in the Min Heap. If v is in the Min Heap and the distance value
is more than the weight of u-v plus the distance value of u, then update the distance value of v.

Dijkastra-Algorithm--8.webpDijkastra-Algorithm--8.webp

Let us understand with the following example. Let the given source vertex be 0

Initially, the distance value of the source vertex is 0, and INF (infinite) for all other vertices. So source
vertex is extracted from Min Heap and distance values of vertices adjacent to 0 (1 and 7) are updated.
The vertices in the sptset are the vertices for which minimum distances are finalized and are not in Min Heap.
Since the distance value of vertex 1 is minimum among all nodes in Min Heap, it is extracted from Min Heap, and
distance values of vertices adjacent to 1 are updated (distance is updated if the vertex is in Min Heap and
distance through 1 is shorter than the previous distance).

Pick the vertex with a minimum distance value from the min-heap. Vertex 7 is picked. So min-heap now contains
all vertices except 0, 1, and 7. Update the distance values of adjacent vertices of 7. The distance value of
vertex 6 and 8 becomes finite (15 and 9 respectively).

Pick the vertex with a minimum distance from the min-heap. Vertex 6 is picked, and the distance values of
adjacent vertices of 6 are updated. The distance values of vertex 5 and 8 are updated.

The above steps are repeated till the min-heap doesn't become empty. Finally, we get the following shortest
 path tree.

"""

# A Python program for Dijkstra's shortest
# path algorithm for adjacency
# list representation of graph

from collections import defaultdict
import sys


class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2

        if (left < self.size and
           self.array[left][1]
            < self.array[smallest][1]):
            smallest = left

        if (right < self.size and
           self.array[right][1]
            < self.array[smallest][1]):
            smallest = right

        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:

            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    # Standard function to extract minimum
    # node from heap
    def extractMin(self):

        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in  heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is
        # not heapified. This is a O(Logn) loop
        while (i > 0 and self.array[i][1] <
                  self.array[(i - 1) // 2][1]):

            # Swap this node with its parent
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swapMinHeapNode(i, (i - 1)//2 )

            # move to parent index
            i = (i - 1) // 2;

    # A utility function to check if a given
    # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


def printArr(dist, n):
    print ("Vertex\tDistance from source")
    for i in range(n):
        print ("%d\t\t%d" % (i,dist[i]))


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):

        # Add an edge from src to dest.  A new node
        # is added to the adjacency list of src. The
        # node is added at the beginning. The first
        # element of the node has the destination
        # and the second elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # Since graph is undirected, add an edge
        # from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    # The main function that calculates distances
    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src):

        V = self.V  # Get the number of vertices in graph
        dist = []   # dist values used to pick minimum
                    # weight edge in cut

        # minHeap represents set E
        minHeap = Heap()

        #  Initialize min heap with all vertices.
        # dist value of all vertices
        for v in range(V):
            dist.append(1e7)
            minHeap.array.append( minHeap.
                                newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])

        # Initially size of min heap is equal to V
        minHeap.size = V;

        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:

            # Extract the vertex
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if (minHeap.isInMinHeap(v) and
                     dist[u] != 1e7 and \
                   pCrawl[1] + dist[u] < dist[v]):
                        dist[v] = pCrawl[1] + dist[u]

                        # update distance value
                        # in min heap also
                        minHeap.decreaseKey(v, dist[v])

        printArr(dist,V)


# Driver program to test the above functions
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)

# This code is contributed by Divyanshu Mehta

"""
Time Complexity: The time complexity of the above code/algorithm looks O(V^2) as there are two nested while 
loops. If we take a closer look, we can observe that the statements in the inner loop are executed O(V+E) 
times (similar to BFS). The inner loop has a decreaseKey() operation which takes O(log V) time. So overall 
time complexity is O(E+V)*O(log V) which is O((E+V)*logV) = O(E log V) 

Note that the above code uses Binary Heap for Priority Queue implementation. Time complexity can be reduced 
to O(E + V logV) using the Fibonacci Heap. The reason is, that Fibonacci Heap takes O(1) time for decrease-key 
operation while Binary Heap takes O(logn) time.

Space Complexity: O(V)
The space complexity of Dijkstra’s algorithm is O(V) as we maintain two priority queues or heaps (in the case
 of binary heap). The heap stores the nodes that are not yet included in SPT (shortest path tree). We also 
 maintain an array to store the distance values of each node.

Dijkstra’s Algorithm for Adjacency List Representation using Built-in Priority Queue (or Heap)
This approach shows the implementation of Dijkstra's Algorithm with a priority queue to extract minimum and
decrease key. However, the problem is, that priority_queue doesn’t support the decrease key. To resolve this
problem, do not update a key, but insert one more copy of it. So we allow multiple instances of the same
vertex in the priority queue. This approach doesn’t require decreasing key operations and has below important
properties. 

Whenever the distance of a vertex is reduced, we add one more instance of a vertex in priority_queue. Even if
 there are multiple instances, we only consider the instance with minimum distance and ignore other instances. 
 
The time complexity remains  O(E * LogV)  as there will be at most O(E) vertices in the priority queue and
 O(logE) is the same as O(logV) 

"""
import heapq


# Function to add an edge to the adjacency list
def addEdge(adj, u, v, wt):
    adj[u].append((v, wt))
    adj[v].append((u, wt))


# Function to find the shortest paths from source to all other vertices
def shortestPath(adj, V, src):
    # Create a priority queue to store vertices that are being preprocessed
    pq = []

    # Create an array for distances and initialize all distances as infinite (INF)
    dist = [float('inf')] * V

    # Insert source itself in the priority queue and initialize its distance as 0
    heapq.heappush(pq, (0, src))
    dist[src] = 0

    # Loop until the priority queue becomes empty
    while pq:

        # Extract the vertex with minimum
        # distance from the priority queue
        distance, u = heapq.heappop(pq)

        # Get all adjacent vertices of u
        for v, weight in adj[u]:
            # If there is a shorter path to v through u
            if dist[v] > dist[u] + weight:
                # Update distance of v
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    # Print shortest distances stored in dist[]
    print("Vertex Distance from Source")
    for i in range(V):
        print(i, "    ", dist[i])


# Main function
if __name__ == "__main__":
    V = 9
    adj = [[] for _ in range(V)]

    # Making the graph
    addEdge(adj, 0, 1, 4)
    addEdge(adj, 0, 7, 8)
    addEdge(adj, 1, 2, 8)
    addEdge(adj, 1, 7, 11)
    addEdge(adj, 2, 3, 7)
    addEdge(adj, 2, 8, 2)
    addEdge(adj, 2, 5, 4)
    addEdge(adj, 3, 4, 9)
    addEdge(adj, 3, 5, 14)
    addEdge(adj, 4, 5, 10)
    addEdge(adj, 5, 6, 2)
    addEdge(adj, 6, 7, 1)
    addEdge(adj, 6, 8, 6)
    addEdge(adj, 7, 8, 7)

    # Finding shortest paths from source vertex 0
    shortestPath(adj, V, 0)

"""
Time Complexity: O(E*logV), Where E is the number of edges and V is the number of vertices.
Auxiliary Space: O(V), Where V is the number of vertices.

Notes: 

The code calculates the shortest distance but doesn’t calculate the path information. We can create a parent 
array, update the parent array when distance is updated (like prim’s implementation), and use it to show 
the shortest path from the source to different vertices.
The code is for undirected graphs, same Dijkstra function can be used for directed graphs also.
The code finds the shortest distances from the source to all vertices. If we are interested only in the 
shortest distance from the source to a single target, we can break the for loop when the picked minimum 
distance vertex is equal to the target (Step 3 of the algorithm).
Dijkstra’s algorithm doesn't work for graphs with negative weight edges. For graphs with negative weight 
edges, the Bellman-Ford algorithm can be used.

"""










