
"""
undirected - edge(u,v)=edge(v,u)  bidirectional roads
directed - edge(u,v)!=edge(v,u)  u to v

weighted graph with cost,distance,quantity as edge triplet(u,v,w) and specify directed or undirected
special graphs

trees - undirected graph with no cycles,it is a connected graph with n nodes and n-1 edges

rooted trees - is a tree with designated root.edges pointing away(arborescence,out-tree) or to root node(anti-arborescence,in-tree)

directed acyclic graphs(dag)- directed,no cycle,  represents structure with dependencies(scheduler,build system,compiler) complete prerequisites or dependency before going to next level or nodes.all out-trees are DAGs

Bipartite graph - verices can be split into 2 independent groups u,v such that every edge connects between u and v.matching peoples to jobs with constraints

Complete graph - their is a unique edge between between every pair of nodes (n) denoted as Kn - K1 , K2, K3,K4,worst case

Representation

Adjacency matrx m is asimple way to represent graph.cell m[i][j] represents the edge weight of going from node i to node j

  A    ->  <-     B                 A   B   C   D
  |               |              A  0   4   1   9
->  <-        ->  <-             B  3   0   6   11
  |               |              C  4   1   0   2
  C    ->  <-     D              D  6   5  -4   0

ITS space efficient for representing dense graphs,edge weight lookup is 0(1) constant time
its  space comp is n**2 and iteration requires n**2 time

adj list - is a way to represent a graph as a map from nodes to lists of edges
A-> [(B,4)(C,1)]  B->[(C,6)]  C->[(A,4),(B,1),(D,2)] ,D->[]

A     --4>    --B
4>           >1//   >up.right  <down,left
||
<1    //<6
C --   2>     --D

it is space efficient for sparse graph,iteration is efficient but not for denser graphs,edge weight lookup is o(e)

edge list represent a graph as an unordered list of edges
[(C,A,4),(A,C,1),
(B,C,6),(A,B,4),
(C,B,1),(C,D,2)]

William fiset - reduction of graphs problems to less
see if its directed or undirected, weighted,sparse or dense
should i use an adjacency matrix,adjacency list,an edge list or other structure to represent the graph efficiently

1 SPF Problem-weighted ,finding shortest path of edges from node a to b.
ans - bfs(unweighted),dijsktra,bellman ford,a*

2 connectivity problem -if there exists a path between a and b
ans- use union find data structure,or search algo like dfs,bfs

3 detecting negetive(weights) cycles problem - affected(getting smaller and smaller costs) and unaffected(in currency exchange going through lower price crrency then higher price exchange)
ans - bellman-ford  floyd marshall

4 .strongly connected components(sccs) are self contained cycles within a directed graph where every other vertex in a given cycle can reach every other vertex in the same cycle.equivalent to finding strongly connected components in a undirected graphs in a directed grsph
ans tarjam and kosarajus algo

5 - travelling salesman - given a list of citis ,distance find shortest possible route that visits each city exactly once and return to the origin.
ans - Held-karp with dp,branch and bound ,and approximation algo as ant colony optimization

6 - finding bridges in graph- a bridge/ cut edge  is any edge in a graph whose removal increases the no of connected components.they represent weak points,bottlenecks or vulnerabilities in a graph

7- articulation point/ cut vertex - is any node in agraph whose removal increases the no connected components,they represent weak points,bottlenecks or vulnerabilities in a graph

8 find MSP tree - it is a subsetof the edges of a connected,edge weighted graph that connects all the vertices together,without any cycle and min edge sum.there may be many mst in graph.used in approx,transport,circuit
ans kruskals,prims and boruvka

9 network flow |max flow - with an infinite input source how much flow can w push through the network.ex - if edges are roads with car,pipes with water the volume of water allowed to flow through the pipes ,the no of cars road can sustain,people roaming in hallways  SRC --------------------- SINK
--------------------------

    DFS - IS A SEARCH ALGO used to explore nodes and edges of a graph .tc is O(V+E) VERtice EDGE which is directly proportional to size of graph and is often used as a building block in other algorithms
its augmented to perform tasks such as count connected components,determine conectivity ,or find bridges/articulation points then dfs really shines

- it takes paths upto point where it cant go any further , then it backtracks and continues

labeling is done for backtracking

global or class scope variables
n = no of nodes
g = adjacency list
visited = [f,f,f,f,f,....nf]

funs dfs(at):
    if visited[at]: return
      visited[at] = true

    neighbors = graph[at]
    for next in neighbors:
      dfs(next)

    # stsrt dfs at node 0
    start node = 0
    dfs(start_node)

------------------
connected components - sometimes a graph is split into multiple components, each nodes in compenent marked differently
start dfs and mark all reachable nodes as being part of the same component

n = no of nodes
g = adjacency list
count =0  (no of connected component)
components = empty integer array  - max size n - which component the node  belongs to
visited = [f,f,f,f,f,....nf]

func findcomponents():
    for (i=0; i<n; i++):
     if !visited[i]:
      count++
      dfs[i]
    return(count,components)

func dfs(at):
  visited[at] = true
  components[at] = count
  for (next : g[at]):
    if !visited[next]:
      dfs(next)

bfs tc O(V+E) = bfs algo is particularly useful for one thing finding shortest path on unweighted graphs
itexplores all the neighbor nodes first ,before moving to the next level neighbors.
for this it maintains a que starting from 0 9 7 11 10 8  6 3     until we run out of nodes,we dont add a node as neighbor if it is already somebodys neighbor
                            neighbor of 0  |-----|-of 9|of 7|


global or class scope variables
n = no of nodes
g = adjacency list representing un weighted graph
s= start node e = end node , 0 <= e , s < n
function bfs(s,e):
    # do a bfs starting at node s
    prev = solve(s)

    # return reconstructed path from s -> e
    return recunstuctpath(s, e, prev)

func solve(s):
  q = due data structure with enque and deque
  q.enque(s)

  visited = [,f,f,f,f..nf]
  visited[s] = true
  prev = [null,.....,null]  array of shortest path from start to end node, it tracks who the parent of node i was so that we can reconstruct the path later
  while !q.isempty():
    node = q.deque()  pull out the top node
    neighbors = g.get(node)  then get the neighbors of this node from adjacency list

    for(next:neighbors):
      if !visited[next]:  loop over unvisited node and enque it and label
        q.enque(next)
        visited[next] = true
        prev[next] = node  keep track of the parent node of the next node
  return prev

func reconstructpath(s,e prev):

    reconst path going backward from end node to start node asumming we can reach it
     path = []
     for (at = e; at != null; at = prev[at]);
       path.add(at)

    path.reverse()
    if s and e are connected return the path
    if path[0] == s:
      return path
    return[]
------------------------------
Grids are a form of implicit graph, we can determine neighbors based on our location within the grid.

convert the grid to a familiar format such as an adjacency list/matrix

empty grid   adj list:              adj matrix
            it is a mapping       0  1  2  3  4  5      0,0 is the starting point
 0  1       0 -> [1,2]          0 0  1  1  0  0  0
 2  3       1 -> [0,3]          1 1  0  0  1  0  0      using [-1,-1],[-1,1],[1,1],[1,-1]
 4  5       2 -> [0,3,4]        2 1  0  0  1  1  0
            3 -> [1,2,5]        3 0  1  1  0  0  1
            4 -> [2,5]          4 0  0  1  0  0  1
            5 -. [3,4]          5 0  0  0  1  1  0

DIRECTION VECTOR

define the direction vector for n,s e,w
dr = [-1, +1, 0,0]
dc = [0 , 0,+1,-1]

for(i=0;i<4;i++);
rr = r + dr[i]
cc = c + dc[i]

if rr < 0 or cc < 0: continue   within grid checks
if rr >= r or cc >= c: continue
rr,cc is a neighboring cell of r,c

DUNGEON PROBLEM
Size r*c  start at s exit at e.cell full of rock is indicated by a # and empty cell by '.' .

s . . # . . .
. # . . . # .
. # . . . . .
. . # # . . .
# . # e . # .

from each node it travels to all its neighbor untill it cant.we store in que as x,y pair
which will require a lot of packing and unpacking of values to and from the que

Alternative approach is using one que for each dimension so in a 3d grid one que each for x,y,z
r,c = row,col
m =   input
sr,sc =r,c values at start
rq,cq =  empty row que,col que to  enq and deq elements

move count = 0 no of steps taken
nodes left in layer = 1
nodes in next layer = 0

reached_end = false
visited =     r*c value represents it

dr = [-1, +1, 0,0]
dc = [0 , 0,+1,-1]

ans

func solve():
  rq.enque(sr)
  cq.enque(sc)
  visited[sr][sc] = true
  while rq,size() > 0: # cq.size() > 0
    r = rq.deque()
    c = cq.deque()
    if m[r][c] =='e':
      reached_end = true
      break
    explore_neihbors(r,c)
    if nodes_left_inlayer == 0:
      nodes_left_inlayer = nodes_in_nextlayer
      nodes_in_nextlayer = 0
      move_count ++       no of steps taken
  if reached_end:
    return move_count   steps in the path to end
  return -1

func explore_neihbors(r,c):
  for(i=0;i<4;i++);
   rr = r + dr[i]
   cc = c + dc[i]

   if rr < 0 or cc < 0: continue  skip out of bound locations
   if rr >= 0 or cc > C: continue

   if visited[rr][cc]: continue
   if m[rr][cc] == #: continue

   rq.enque(rr) if above conditions not true
   cq.enque(cc)
   visited[rr][cc] = true
   nodes_in_nextlayer++

"""
"""
topological sort

class A        class C         class J
               class D

               class E         class H
class B        class F         class I
to take class H ist class A,B,D and E is prerequisites.there is an ordwring on the nodes of the graph
or if its dependencies are met
topological order need not be unique
agraph which contains a cycle cannot have a valid ordering
Directed Acyclic Graphs -  these are graphs with directed edges and no cycles ,has a valid topological ordering

to cheeck graph does not contain a directed cycle is to use Tarjans strongly connected component algo used to find cycles

Trees have topo ordering as they have no cycle.ordering i done from leaf nodes to root
1- begining with the selected node,do DFS EXPLORING ONLY UNVSITED NODES.
2- on recursive callback of the dfs add the current node to the topological ordering in reverse order.

dfs reursion call stack: (start)node h>,node j> ,node m(end)   backtrack to j 
dfs reursion call stack: (start)node h>,node j> ,node l(end)   backtrack to j 
dfs reursion call stack: (start)node h>,node j(end)   backtrack to h
dfs reursion call stack: (start)node h>,node i(end)   backtrack to h
then pick another random node
dfs reursion call stack: (start)node e > node a > node d > node g(end)   backtrack to d 
dfs reursion call stack: (start)node e > node a > node d(end)   backtrack to a 
dfs reursion call stack: (start)node e > node a(end)   backtrack to e 
dfs reursion call stack: (start)node e >  node f> node k(end)   backtrack to f
dfs reursion call stack: (start)node e >  node f(end)   backtrack to e
dfs reursion call stack: (start)node c > node b(end)   backtrack to c

add m then l,j,i,h,g,d,a,k,f,e,b,c to the topological ordering in reverse

func topsort(graph):
  n = graph.nooofnodes()
  v = [f,f,f....]

------------
single source shortest path(sssp) problem can be solved efficiently with dag in o(v+e) time
because nodes can be ordered in atopological ordering via topsort and processed sequentially
 from root we mark all nodes distance as  infinity in topological order and place the shortest dist as we travers
      b             e
a           d       f       h
      c             g


distance 0  3  6  i  i  i  i  i  from a
nodes    a  b  c  d  e  f  g  h   

distance 0  3  6  7  14  i  i  i  from a > b > we place the shortest dist available through b
nodes    a  b  c  d  e   f  g  h

distance 0  3  6  7  14  i  i  i  from a > c > we place the shortest dist available through c
nodes    a  b  c  d  e   f  g  h

distance 0  3  6  7  3  12  9  11  from a > rest> we place the shortest dist available through all
nodes    a  b  c  d  e   f  g  h

11 is the shortest path
similarly longest path(np-hard) can be found in linear time on dag in o(v+e)
 the trick is to multiply all edge values by -1 then find the shortest path and then multiply the  edge values bt -1 again
 as -4 sp > -11 so if path is (-3 + -11 + -9 ) * -1 = 23

"""
"""
/**
 * This topological sort implementation takes an adjacency list of an acyclic graph and returns an
 * array with the indexes of the nodes in a (non unique) topological order which tells you how to
 * process the nodes in the graph. More precisely from wiki: A topological ordering is a linear
 * ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes
 * before v in the ordering.
 *
 * <p>Time Complexity: O(V + E)
 *
 * @author William Fiset, william.alexandre.fiset@gmail.com
 */
"""

from collections import defaultdict
from typing import List, Dict, Optional

class Edge:
    def __init__(self, f: int, t: int, w: int):
        self.from_node = f
        self.to = t
        self.weight = w
"""
 // Helper method that performs a depth first search on the graph to give
  // us the topological ordering we want. Instead of maintaining a stack
  // of the nodes we see we simply place them inside the ordering array
  // in reverse order for simplicity.
"""
def dfs(i: int, at: int, visited: List[bool], ordering: List[int], graph: Dict[int, List[Edge]]) -> int:
    visited[at] = True
    edges = graph.get(at)

    if edges is not None:
        for edge in edges:
            if not visited[edge.to]:
                i = dfs(i, edge.to, visited, ordering, graph)

    ordering[i] = at
    return i - 1
"""
 // Finds a topological ordering of the nodes in a Directed Acyclic Graph (DAG)
  // The input to this function is an adjacency list for a graph and the number
  // of nodes in the graph.
  //
  // NOTE: 'numNodes' is not necessarily the number of nodes currently present
  // in the adjacency list since you can have singleton nodes with no edges which
  // wouldn't be present in the adjacency list but are still part of the graph!
  //
"""
def topological_sort(graph: Dict[int, List[Edge]], num_nodes: int) -> List[int]:
    ordering = [0] * num_nodes
    visited = [False] * num_nodes
    i = num_nodes - 1

    for at in range(num_nodes):
        if not visited[at]:
            i = dfs(i, at, visited, ordering, graph)

    return ordering
"""
 // A useful application of the topological sort is to find the shortest path
  // between two nodes in a Directed Acyclic Graph (DAG). Given an adjacency list
  // this method finds the shortest path to all nodes starting at 'start'
  //
  // NOTE: 'numNodes' is not necessarily the number of nodes currently present
  // in the adjacency list since you can have singleton nodes with no edges which
  // wouldn't be present in the adjacency list but are still part of the graph!
  //
"""
def dag_shortest_path(graph: Dict[int, List[Edge]], start: int, num_nodes: int) -> List[Optional[int]]:
    topsort = topological_sort(graph, num_nodes)
    dist = [None] * num_nodes
    dist[start] = 0

    for i in range(num_nodes):
        node_index = topsort[i]
        if dist[node_index] is not None:
            adjacent_edges = graph.get(node_index)
            if adjacent_edges is not None:
                for edge in adjacent_edges:
                    new_dist = dist[node_index] + edge.weight
                    if dist[edge.to] is None:
                        dist[edge.to] = new_dist
                    else:
                        dist[edge.to] = min(dist[edge.to], new_dist)

    return dist

# Example usage of topological sort
if __name__ == "__main__":
    # Graph setup
    N = 7
    graph = defaultdict(list)
    graph[0].append(Edge(0, 1, 3))
    graph[0].append(Edge(0, 2, 2))
    graph[0].append(Edge(0, 5, 3))
    graph[1].append(Edge(1, 3, 1))
    graph[1].append(Edge(1, 2, 6))
    graph[2].append(Edge(2, 3, 1))
    graph[2].append(Edge(2, 4, 10))
    graph[3].append(Edge(3, 4, 5))
    graph[5].append(Edge(5, 4, 7))

    ordering = topological_sort(graph, N)

    # Prints: [6, 0, 5, 1, 2, 3, 4]
    print(ordering)

    # Finds all the shortest paths starting at node 0
    dists = dag_shortest_path(graph, 0, N)

    # Find the shortest path from 0 to 4 which is 8.0
    print(dists[4])

    # Find the shortest path from 0 to 6 which
    # is None since 6 is not reachable!
    print(dists[6])

#----------------------
"""
/**
 * This Topological sort takes an adjacency matrix of an acyclic graph and returns an array with the
 * indexes of the nodes in a (non unique) topological order which tells you how to process the nodes
 * in the graph. More precisely from wiki: A topological ordering is a linear ordering of its
 * vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the
 * ordering.
 *
 * <p>Time Complexity: O(V^2)
 *
 * @author Micah Stairs
 */
"""
import numpy as np

class TopologicalSortAdjacencyMatrix:

    @staticmethod
    def topological_sort(adj):
        n = len(adj)
        visited = [False] * n
        order = [0] * n
        index = n - 1

        for u in range(n):
            if not visited[u]:
                index = TopologicalSortAdjacencyMatrix.visit(adj, visited, order, index, u)

        return order

    @staticmethod
    def visit(adj, visited, order, index, u):
        if visited[u]:
            return index
        visited[u] = True

        for v in range(len(adj)):
            if adj[u][v] is not None and not visited[v]:
                index = TopologicalSortAdjacencyMatrix.visit(adj, visited, order, index, v)

        order[index] = u
        return index - 1

    @staticmethod
    def dag_shortest_path(adj, start):
        n = len(adj)
        dist = [float('inf')] * n
        dist[start] = 0.0

        for u in TopologicalSortAdjacencyMatrix.topological_sort(adj):
            for v in range(n):
                if adj[u][v] is not None:
                    new_dist = dist[u] + adj[u][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist

        return dist

if __name__ == "__main__":
    N = 7
    adj_matrix = np.full((N, N), None)

    adj_matrix[0][1] = 3.0
    adj_matrix[0][2] = 2.0
    adj_matrix[0][5] = 3.0

    adj_matrix[1][3] = 1.0
    adj_matrix[1][2] = 6.0

    adj_matrix[2][3] = 1.0
    adj_matrix[2][4] = 10.0

    adj_matrix[3][4] = 5.0

    adj_matrix[5][4] = 7.0

    ordering = TopologicalSortAdjacencyMatrix.topological_sort(adj_matrix)

    print(ordering)

    dists = TopologicalSortAdjacencyMatrix.dag_shortest_path(adj_matrix, 0)

    print(dists[4])

    print(dists[6])

"""
Dijkstras algorithm - it is asingle source shortest path algo(a starting node is given) for graphs with non negetive edges
tc = is o(e+log(v))

a priority que of key-value pairs of(node index,dist) pairs which tell you which node to visit next based on sorted min value.
then loop through pq .pq are implimented as heap
        b
    4/       \1
  a     |2    d --3 e    a  b  c  d  e
    1\       /5          0  4  1
        c
key,value(index,dist)
    0, 0
    1, 4
    2, 1     node 2 is selected

key,value(index,dist) 0>2>   through 2    
    1, 4     every duplicates key are removed(lazy implimentation) and best added by selecting min
    1, 3     
    3, 6
    3, 4
    4, 7
eager version of dijk algo avoids duplicate entry using indexed priority que  ,where only values are changed key remains intact

------------------------
D-ARY HEAP OPTIMIZATION
In dense graphs updating key,value pairs is more than dequeing which took time
dary heap is a heap variant in which each node has d children so less key ,val  updates

d = 4                      5,2
       2,6          3,3             8,5       9,4

    - - - -     1,9 0,7 6,5 1,7    - - - -    - - - 4,8

if we want to update 6,5 to 6,1 it will take 2 operation

d = 4                      6,1
       2,6          5,2             8,5       9,4

    - - - -     1,9 0,7 3,3 1,7    - - - -    - - - 4,8
to remove root change with right most it will take 8 steps
d = 4                      5,2 (4,8)
       2,6          3,3(4,8)          8,5       9,4

    - - - -     1,9 0,7 4,8 1,7     - - - -    - - - -
------------------------------
dijsk   SPA ALGO

-----------------------
Bellman-ford algo it is also SSSP algo- it can find the shortest path from one node to any other node.

it  can handle negetive edge by detecting  and determine where they accur.
it is used in finance when performing an arbitrage between two or more markets.
                                   ^3
                     -1         3>   >-2
start node)  0   4>   1   3>  ^2        ^5   
                2>              1>    2>       
                      6    2>       ^4
* - unaffected nodes
- - in negetive cycle
^ - reachable by negetive cycle- they will go to negetive infininity

e edge
v vertex
s id of the starting node
d be an array of size v that tracks the best distance from s to each node. set to infinity
starting is 0
relax each edge v-1 times(updating with shorter path from start yo end) untill we detect cycles to - infinity
loop and  update d
v no of iteration
when we will relax the edgws then distance decreases ,then loops to infinite the edges linked to it



"""
import numpy as np

class Edge:
    def __init__(self, from_node, to_node, cost):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost
"""
/**
   * An implementation of the Bellman-Ford algorithm. The algorithm finds the shortest path between
   * a starting node and all other nodes in the graph. The algorithm also detects negative cycles.
   * If a node is part of a negative cycle then the minimum cost for that node is set to
   * Double.NEGATIVE_INFINITY.
   *
   * @param edges - An edge list containing directed edges forming the graph
   * @param V - The number of vertices in the graph.
   * @param start - The id of the starting node
   */
"""
def bellman_ford(edges, V, start):
    dist = [float('inf')] * V
    dist[start] = 0
    """

        // Only in the worst case does it take V-1 iterations for the Bellman-Ford
        // algorithm to complete. Another stopping condition is when we're unable to
        // relax an edge, this means we have reached the optimal solution early.
        boolean relaxedAnEdge = true;

        // For each vertex, apply relaxation for all the edges
    """

    relaxed_an_edge = True
    for v in range(V - 1):
        if not relaxed_an_edge:
            break
        relaxed_an_edge = False
        for edge in edges:
            if dist[edge.from_node] + edge.cost < dist[edge.to_node]:
                dist[edge.to_node] = dist[edge.from_node] + edge.cost
                relaxed_an_edge = True
                """
                  // Run algorithm a second time to detect which nodes are part
                    // of a negative cycle. A negative cycle has occurred if we
                    // can find a better path beyond the optimal solution.
                """

    relaxed_an_edge = True
    for v in range(V - 1):
        if not relaxed_an_edge:
            break
        relaxed_an_edge = False
        for edge in edges:
            if dist[edge.from_node] + edge.cost < dist[edge.to_node]:
                dist[edge.to_node] = float('-inf')
                relaxed_an_edge = True

    return dist # shortest distance to every node

if __name__ == "__main__":
    E = 10
    V = 9
    start = 0
    edges = [
        Edge(0, 1, 1),
        Edge(1, 2, 1),
        Edge(2, 4, 1),
        Edge(4, 3, -3),
        Edge(3, 2, 1),
        Edge(1, 5, 4),
        Edge(1, 6, 4),
        Edge(5, 6, 5),
        Edge(6, 7, 4),
        Edge(5, 7, 3)
    ]

    d = bellman_ford(edges, V, start)

    for i in range(V):
        print(f"The cost to get from node {start} to {i} is {d[i]:.2f}")

    # Output:
    # The cost to get from node 0 to 0 is 0.00
    # The cost to get from node 0 to 1 is 1.00
    # The cost to get from node 0 to 2 is -Infinity
    # The cost to get from node 0 to 3 is -Infinity
    # The cost to get from node 0 to 4 is -Infinity
    # The cost to get from node 0 to 5 is 5.00
    # The cost to get from node 0 to 6 is 5.00
    # The cost to get from node 0 to 7 is 8.00
    # The cost to get from node 0 to 8 is Infinity


"""
FLOYD-WARSHALL algo is all -pairs shortest path(APSP) algo,it can find the shortest path between all pairs of nodes.
tc = O(v***3)
it is used when less graph size,can detect neg cycles
it is not used on graph with weighted edges

it is represented with a 2d matrix ,if no edge then infinity

        C  ----------->2 D
        |5               |2         ACDB IS SHORTER           
        A  ---------->11 B

we use dynamic with a 3d matrix of size n*n*n dp[k][i][j] prog to find alt path and shortest path
dp[k][i][j] = m[i][j]  when k=0  dist between i and j           k
                                                           i  ------- j           
otherwise  recursive func dp[k][i][j] = min(dp[k-1][i][j],dp[k-1][i][k],dp[k-1][k][j]) is used

if the path goes through negative edge node the path is compromised 
so the algo is run second time   and mark also while looping
if i >j = neg   return null inf solution
if i >j = pos   return path
------------------------------------------------
BRIDGES AND  ARTICULATION POINT

bridge or cut edges which if removed, increases the connected components

articulation point or cut vertex is any node whose removal inc connected components
they hint at weak points,bottlenecks in graph ,so quickly find them using dfs traversal labeling
nodes with an increasing id value and keep track of nodes id and its low link value(lowest id reachable from that node wen doing a dfs(including itself)
During dfs bridges will be found where the id of the node your edge is coming from is less than the low link value of the node your edge is going to.

tc = O(v(v+e))

articulation points - on a connected component with 3 or more vertices if an edge(u,v) is a bridge then either u or v is an articulation point.
         c                              m \   / p
       / |                              |   b   |
a --- b  |    b is articulation point   n /   \ o
       \ |    even if no bridges if articulation point is removed two components would be  formed
         d


-------------
TARJANS ALGO FORor to find STRoNGLY CONNECTED COMPONENTS  SSC
SSC can be thought of as self-contained cycles within a directed graph where every vertex in a given cycle reach every other vertex in the same cycle.
lowlink values - is the smallest node id reachable from that node when doing a dfs(including itself)
    0       0       3       low link value also depends on starting point
    0  ---->1------>3       0 is the starting point
    <     / |       |       to update node u's low link value to node v's low-link value there has to be a path of edges from u to v and node v must be on the stack.
    |  </   <       >
    2  ---->4<----->5
    0       4       4

traversal- start dfs upon visiting a node assign it an id and a low-link value.also mark current nodes as visited and add them to  asee stack
on dfs callback make prev node lowlink value with current node low link value

a node starts a ssc when its id is equal to its low link value
then we remove all the nodes associated to ssc

"""

"""
TSP  = given a list of cities and the dist between each pair of cities,fnd the sh path that visits each city once and returns to the origin city
hamiltonian cycle (visits every node once ) of min cost.
it is np-hard to np-complete means no optimal sol
so there are many approx sol

1- brute force by trying all possible permutations of node orderings which takes O(n!) time
2 dp tc O(n**2  * 2**n)  to compute the optimal sol for all the subpaths of length n ,while using inforation from the already known optimal partial tours of length n-1

next choose a starting point and compute and store the optimal value from s to each node x this will solve tsp probem for all paths of len n = 2
        two nodes           3 nodes 1001 leads to 1011(0-3-1) and 1101(0-3-2)
0 ---->1  0-1       0011    then reconnect back to start then all would be 1111
| \    |  0-2       0101
|  \   |  0-3       1001  ,for 3 nodes or path of length 3  we need to
>    > |    remember or store two things from each of of the n =2 cases 
2 ---->3    1- set of visited nodes in the subpath- by using 32 bit int ,if ith node is visited ith bit is flipped to 1 
            2 -the index of the last visited node in the path
            these two form our dp state



-----------------------------------
eulerian path - is apath of edges that visits all the edges in a graph once.
eulerian circuit is apath of edges that start and ends on the same vertex.
                node degrees                 /
                    /                       <
    undirected graph --       directed graph<---
                    \                       \
    node degree = 3           in degree = 2  >                   
                               out degree = 1       

conditions reqquired for a valid eulerian path/circuit

                eulerian circuit        eulerian path
undirected   every vertex has an        vertex has even degree or exactly 
graph         even degree               two vertices have odd degree

directed     every vertex has equal     atleast one vertex has in-out=1 
graph       indegree and outdegree      or out-in = 1 ,rest out=in

start node has one extra outgoing edge
end node has one extra incoming node

------------------------
PRIMS MIN SPAN TREE-it is greedy mst algo that works well on dense graphs
it has better tc lazy version O(E*LOG(E)) EAGER VERSION O(E*LOG(V)).
it cannot work on a disconnected graph

Given an undirected with weighted edges a MST is a subset of the edges in the graph which connects all
vertices together (without creating any cycles) while minimizing the total edge cost.
 
a graph could have multiple valid MSTs of equal costs

1 - maintain a min priority que that sorts edges based on min edge cost .this will be used to determine the
next node to visit and the edge used to get there.iterate over all edges of s ,adding them to the que.do 
not add edges to pq which point to nodes already visited.
2- undirected graph is like two directed graph in opposite direction

3-we will keep track of the pq containing edge object as triplets:(start node,end node,edge cost)

4- if leeser cost to a node is found the old higher path cost is removed from pq

5-graph representing an adjacency list of weighted edges(two directed edges.for dense graph use adjacency matrix)
visited = [f,f,f......]
-mstedges[edgecount++] = edge
-mstcost += cost

if edge count != m: (multicomponent)
  return null
return mstcost,mstedges
 
-----------eagers prim

instead of blindly inserting edges into a pq which could later become stale the eager version tracks (node,edge) key-value pairs
that can easily be updated and polled to determine the next best edge to add to mst
 
 1-any MST with directed edges, each node is paired with exactly one incoming edge except starting node,bbut can have multiple edge leaving 
 
 
 
 
 
 
 
"""



