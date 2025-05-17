
"""

A greedy algorithm is a problem-solving approach that makes the best immediate choice at each step to
find a solution, without considering future consequences. It aims to find a locally optimal solution at
each step, hoping that these local optima will lead to a globally optimal solution.
Here's a more detailed explanation:
Key Characteristics:
Top-down approach:
Greedy algorithms work by starting with the initial state and making the best choice at each step,
moving towards a solution.
Local optimality:
They focus on making the best choice at each stage, without backtracking or considering the potential impact
 of a choice on the overall solution.
No backtracking:
Once a choice is made, it is not reversed, even if it leads to a suboptimal overall solution.
Simplicity:
Greedy algorithms are generally easy to understand and implement.
When Greedy Algorithms Work:
Greedy choice property:
Choosing the best option at each stage can lead to the global optimal solution.
Optimal substructure:
An optimal solution to the complete problem contains optimal solutions to its subproblems.
Examples of Greedy Algorithms:
Huffman coding:
Used for data compression, assigning variable-length codes to characters based on their frequency.
Minimum spanning tree algorithms (Kruskal's and Prim's):
Find the most cost-effective way to connect all nodes in a graph.
Coin change problem:
Finding the minimum number of coins needed to make a certain amount of change.
Fractional knapsack problem:
Deciding which items to include in a knapsack to maximize profit, given weight constraints.
Limitations:
Not always optimal:
While greedy algorithms can be efficient, they may not always find the globally optimal solution.
May get stuck in local optima:
If a local optimal choice is made, it may lead to a suboptimal solution overall.
In essence, a greedy algorithm is a straightforward approach to optimization problems, where the best
immediate choice is made at each step, hoping to find the overall best solution.
"""
"""
geeeks

At every step of the algorithm, we make a choice that looks the best at the moment. To make the choice
, we sometimes sort the array so that we can always get the next optimal choice quickly. We sometimes 
also use a priority queue to get the next optimal item.
After making a choice, we check for constraints (if there are any) and keep picking until we find the solution.
Greedy algorithms do not always give the best solution. For example, in coin change and 0/1 knapsack problems, 
we get the best solution using Dynamic Programming.
Examples of popular algorithms where Greedy gives the best solution are Fractional Knapsack, Dijkstra's 
algorithm, Kruskal's algorithm, Huffman coding and Prim's Algorithm


Greedy Choice Property: The optimal solution can be constructed by making the best local choice at each step.
Optimal Substructure: The optimal solution to the problem contains the optimal solutions to its subproblems.





"""





















