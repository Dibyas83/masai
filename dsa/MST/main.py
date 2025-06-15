

"""
DSA Minimum Spanning Tree
The Minimum Spanning Tree Problem
The Minimum Spanning Tree (MST) is the collection of edges required to connect all vertices in an undirected graph, with the minimum total edge weight.


Find MST
The animation above runs Prim's algorithm to find the MST. Another way to find the MST, which also works for unconnected graphs, is to run Kruskal's algorithm.

It is called a Minimum Spanning Tree, because it is a connected, acyclic, undirected graph, which is the definition of a tree data structure.

In the real world, finding the Minimum Spanning Tree can help us find the most effective way to connect houses to the internet or to the electrical grid, or it can help us finding the fastest route to deliver packages.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Where to
Video Player is loading.Play VideoBrand logo


An MST Thought Experiment
Let's imagine that the circles in the animation above are villages that are without electrical power, and you want to connect them to the electrical grid. After one village is given electrical power, the electrical cables must be spread out from that village to the others. The villages can be connected in a lot of different ways, each route having a different cost.

The electrical cables are expensive, and digging ditches for the cables, or stretching the cables in the air is expensive as well. The terrain can certainly be a challenge, and then there is perhaps a future cost for maintenance that is different depending on where the cables end up.

All these route costs can be factored in as edge weights in a graph. Every vertex represents a village, and every edge represents a possible route for the electrical cable between two villages.

After such a graph is created, the Minimum Spanning Tree (MST) can be found, and that will be the most effective way to connect these villages to the electrical grid.

And this is actually what the first MST algorithm (Borůvka's algorithm) was made for in 1926: To find the best way to connect the historical region of Moravia, in the Check Republic, to the electrical grid.

MST Algorithms
The next two pages in this tutorial explains two algorithms that finds the Minimum Spanning Tree in a graph: Prim's algorithm, and Kruskal's algorithm.

Prim's algorithm	Kruskal's algorithm
Can it find MSTs (a Minimum Spanning Forest) in an unconnected graph?	No	Yes
How does it start?	The MST grows from a randomly chosen vertex.	The first edge in the MST is the edge with lowest edge weight.
What time complexity does it have?
O
(
V
2
)
, or
O
(
E
⋅
log
V
)
 (Optimized)
O
(
E
⋅
log
E
)

"""









