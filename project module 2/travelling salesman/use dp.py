"""

Travelling Salesman Problem using Dynamic Programming
Last Updated : 26 Nov, 2024
Given a 2d matrix cost[][] of size n where cost[i][j] denotes the cost of moving from city i to city j. The task is to complete a tour from city 0 (0-based index) to all other cities such that we visit each city exactly once and then at the end come back to city 0 at minimum cost.

Note the difference between Hamiltonian Cycle and TSP. The Hamiltonian cycle problem is to find if there exists a tour that visits every city exactly once. Here we know that Hamiltonian Tour exists (because the graph is complete) and in fact, many such tours exist, the problem is to find a minimum weight Hamiltonian Cycle.

Examples:

Input: cost[][] = [[0, 111], [112, 0]]
Output: 223
Explanation: We can visit 0->1->0 and cost = 111 + 112 = 223.


Input: cost[][] = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]]
Output: 3000
Explanation: We can visit 0->1->2->0 and cost = 1000 + 1000 + 1000 = 3000.


Try it on GfG Practice
redirect icon
Table of Content

Exploring All Permutations – O(n!) Time and O(n) Space
Using Recursion – O(n!) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n*n*2^n) Time and O(n*2^n) Space
Exploring All Permutations – O(n!) Time and O(n) Space
The given graph is a complete graph, meaning there is an edge between every pair of nodes. A naive approach to solve this problem is to generate all permutations of the nodes, and calculate the cost for each permutation, and select the minimum cost among them. Please refer to Traveling Salesman Problem (TSP) Implementation.


Using Recursion – O(n!) Time and O(n) Space
The idea behind this approach is to use two parameters: curr, which denotes the currently visited node, and mask, which represents the set of all visited nodes using bitmasking. These two parameters are sufficient to define the state at any given point in the problem.
Let tsp(curr, mask) be the function that calculates the minimum cost to visit all cities, where mask represents the set of cities that have been visited, and curr denotes the current city being visited.


The recurrence relation for the TSP problem is defined as:


 tsp(curr, mask) = min(cost[curr][i] + tsp(i, mask ∣ (1<<i))), for all cities i that have not been visited yet.
where:


curr is the current city in the tour.
mask represents the cities that have already been visited.
cost[curr][i] is the cost to travel from city curr to city i.
tsp(i, mask | (1 << i)) represents the cost of visiting the remaining cities in the new mask (after visiting city i), and continuing the tour from city i.
Base Case: The base case occurs when all cities have been visited, which can be identified when:
mask == ((1 << n) – 1)
In this case, the function simply returns the cost of traveling back to the starting city (city 0):
tsp(curr, mask) = cost[curr][0]





1
# Python program to find the shortest possible route
2
# that visits every city exactly once and returns to
3
# the starting point using memoization and bitmasking
"""
# Python program to find the shortest possible route
# that visits every city exactly once and returns to
# the starting point using memoization and bitmasking

import sys


def totalCost(mask, pos, n, cost):
    # Base case: if all cities are visited, return the
    # cost to return to the starting city (0)
    if mask == (1 << n) - 1: # 1111 = 4*4 - 1
        return cost[pos][0]

    ans = sys.maxsize

    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0:
            # If city i is not visited, visit it and
            #  update the mask
            ans = min(ans, cost[pos][i] +
                      totalCost(mask | (1 << i), i, n, cost))

    return ans


def tsp(cost):
    n = len(cost)

    # Start from city 0, and only city 0 is visited
    # initially (mask = 1)
    return totalCost(1, 0, n, cost)


if __name__ == "__main__":
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    result = tsp(cost)
    print(result)
"""
Output
80
Using Top-Down DP (Memoization) – O(n*n*2^n) Time and O(n*2^n) Space
If we observe closely, we can see that the recursive relation tsp() in the Traveling Salesman Problem (TSP) exhibits the overlapping subproblems, where the same subproblems are recalculated multiple times in different recursion paths. To optimize this, we can use memoization to store the results of previously computed subproblems, thus avoiding redundant calculations.


In this case, there are two parameters that change: mask, which represents the cities visited so far, and curr, which represents the current city. Since both parameters have a finite range (i.e., mask can have up to 2^n distinct values and curr can take n possible values), we can use a 2D array of size n x (1<<n) to store the results for each combination of mask and curr and initialize it as -1 to indicate that the values are not computed.





1
# Python program to find the shortest possible route
2
# that visits every city exactly once and returns to
3
# the starting point using memoization and bitmasking
"""


# Python program to find the shortest possible route
# that visits every city exactly once and returns to
# the starting point using memoization and bitmasking

def totalCost(mask, curr, n, cost, memo):
    # Base case: if all cities are visited, return the
    # cost to return to the starting city (0)
    if mask == (1 << n) - 1:
        return cost[curr][0]

    # If the value has already been computed, return it
    # from the memo table
    if memo[curr][mask] != -1:
        return memo[curr][mask]

    ans = float('inf')

    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0:
            # If city i is not visited
            # Visit city i and update the mask
            ans = min(ans, cost[curr][i] +
                      totalCost(mask | (1 << i), i, n, cost, memo))

    # Memoize the result
    memo[curr][mask] = ans
    return ans


def tsp(cost):
    n = len(cost)

    # Initialize memoization table with -1
    # (indicating uncomputed states)
    memo = [[-1] * (1 << n) for _ in range(n)]

    # Start from city 0, with only city 0 visited initially (mask = 1)
    return totalCost(1, 0, n, cost, memo)


cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
res = tsp(cost)
print(res)