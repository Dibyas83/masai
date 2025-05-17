
"""

Traveling Salesman Problem (TSP) in Python
Last Updated : 31 May, 2024
The Traveling Salesman Problem (TSP) is a classic algorithmic problem in the fields of computer science and operations research. It involves finding the shortest possible route that visits a set of cities and returns to the origin city. The challenge of TSP lies in its NP-hard nature, meaning that as the number of cities increases, the problem becomes exponentially more complex to solve optimally.

What is Traveling Salesman Problem (TSP)?
In TSP, a "salesman" starts at a home city, visits a list of given cities exactly once, and returns to the home city, minimizing the total travel distance or cost. This problem can be applied to various practical scenarios, including logistics, planning, and manufacturing.

Approaches to Solve Traveling Salesman Problem (TSP):
There are several approaches to solving TSP, ranging from exact algorithms that guarantee an optimal solution to heuristic and metaheuristic methods that provide approximate solutions. Some common methods include:

Brute Force: Checking all possible permutations of cities to find the shortest route. This method guarantees an optimal solution but is computationally infeasible for large datasets due to its factorial time complexity.
Dynamic Programming: The Held-Karp algorithm uses dynamic programming to reduce the time complexity to ?(?2⋅2?)O(n2⋅2n), which is still exponential but more efficient than brute force for moderately sized problems.
Greedy Algorithms: These provide quick but often suboptimal solutions by making locally optimal choices at each step.
Genetic Algorithms: These use principles of natural selection and genetics to find approximate solutions.
Simulated Annealing: This probabilistic technique approximates the global optimum of a given function by iterative improvement.
Implementing of Traveling Salesman Problem (TSP) in Python
Let's implement a simple solution using dynamic programming (Held-Karp algorithm) in Python. This method involves breaking the problem into smaller subproblems and solving each subproblem only once, storing the results to avoid redundant calculations.

Step-by-Step Implementation:
Define the Problem: Represent the cities and the distances between them using a distance matrix.
Initialize the Dynamic Programming Table: Create a table to store the minimum costs of visiting subsets of cities.
Iterate Through Subsets: Compute the minimum costs for visiting subsets of cities and update the table.
Compute the Optimal Path: Reconstruct the optimal path from the dynamic programming table.
Below is the implementation of the above approach:

"""


n = 4  # there are four nodes in example graph (graph is 1-based)

# dist[i][j] represents shortest distance to go from i to j
# this matrix can be calculated for any given graph using
# all-pair shortest path algorithms
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
        0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

# memoization for top down recursion
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
    # base case
    # if only ith bit and 1st bit is set in our mask,
    # it implies we have visited all other nodes already
    if mask == ((1 << i) | 3):
        return dist[1][i]

    # memoization
    if memo[i][mask] != -1:
        return memo[i][mask]

    res = 10**9  # result of this sub-problem

    # we have to travel all nodes j in mask and end the path at ith node
    # so for every node j in mask, recursively calculate cost of
    # travelling all nodes in mask
    # except i and then travel back from node j to node i taking
    # the shortest path take the minimum of all possible j nodes
    for j in range(1, n+1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
    memo[i][mask] = res  # storing the minimum value
    return res


# Driver program to test above logic
ans = 10**9
for i in range(1, n+1):
    # try to go from node 1 visiting all nodes in between to i
    # then return from i taking the shortest route to 1
    ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])

print("The cost of most efficient tour = " + str(ans))
"""

Output
The cost of most efficient tour = 80
Time Complexity : O(n2*2n) where O(n* 2n) are maximum number of unique subproblems/states and O(n) for transition (through for loop as in code) in every states.
Auxiliary Space: O(n*2n), where n is number of Nodes/Cities here.
"""












