
#  using memoization and bitmasking

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

