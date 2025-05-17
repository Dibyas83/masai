
"""

Given a 2D grid of size n*n, where each cell represents the cost to traverse through that cell, the task is to find the minimum cost to move from the top left cell to the bottom right cell. From a given cell, we can move in 4 directions: left, right, up, down.

Note: It is assumed that negative cost cycles do not exist in input matrix.

Example:

Input: grid = {{9, 4, 9, 9},
                        {6, 7, 6, 4},
                       {8, 3, 3, 7},
                      {7, 4, 9, 10}}
Output: 43
Explanation: The minimum cost path is 9 + 4 + 7 + 3 + 3 + 7 + 10.


Try it on GfG Practice
redirect icon
Approach:

The idea is to use Dijkstra’s algorithm to find the minimum cost path through the grid. This approach treats the grid as a graph where each cell is a node, and the algorithm dynamically explores the most cost-effective path to the bottom-right cell by always expanding the lowest-cost paths first.


Step by step approach:

Use a min-heap to always process the lowest-cost path first and push the top left cell into it.
Initialize a cost matrix with maximum values, setting the start cell’s cost to its grid value.
For each cell, check all 4 neighboring cells
If a lower cost path is found, then update the cost of cell and push it into heap.
Return the minimum cost to reach the bottom-right cell.
Below is the implementation of the above approach:




1
# Python program to find minimum Cost Path with
2
# Left, Right, Bottom and Up moves allowed
3
import heapq
4
​
5
# Function to check if cell is valid.
6
def isValidCell(i, j, n):
7
    return i >= 0 and i < n and j >= 0 and j < n
8
​
9
def minimumCostPath(grid):
10
    n = len(grid)
11

12
    # Min heap to implement Dijkstra
13
    pq = []
14

15
    # 2D grid to store minimum cost
16
    # to reach every cell.
17
    cost = [[float('inf')] * n for _ in range(n)]
18
    cost[0][0] = grid[0][0]
19

20
    # Direction vector to move in 4 directions
21
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
22

23
    heapq.heappush(pq, [grid[0][0], 0, 0])
24

25
    while pq:
26
        c, i, j = heapq.heappop(pq)
27

28
        # Check for all 4 neighbouring cells.
29
        for d in dir:
30
            x, y = i + d[0], j + d[1]
31

32
            # If cell is valid and cost to reach this cell
33
            # from current cell is less
34
            if isValidCell(x, y, n) and cost[i][j] + grid[x][y] < cost[x][y]:
35

36
                # Update cost to reach this cell.
37
                cost[x][y] = cost[i][j] + grid[x][y]
38

39
                # Push the cell into heap.
40
                heapq.heappush(pq, [cost[x][y], x, y])
41

42
    # Return minimum cost to
43
    # reach bottom right cell.
44
    return cost[n - 1][n - 1]
45
​
46
if __name__ == "__main__":
47
    grid = [
48
        [9, 4, 9, 9],
49
        [6, 7, 6, 4],
50
        [8, 3, 3, 7],
51
        [7, 4, 9, 10]
52
    ]
53

54
    print(minimumCostPath(grid))

Output
43
Time Complexity: O(n^2 log(n^2))
Auxiliary Space: O(n^2 log(n^2))

Why dynamic programming cannot be used?

Dynamic programming fails here because allowing movement in all four directions creates cycles where cells can be revisited, breaking the optimal substructure assumption. This means the cost to reach a cell from a given cell isn’t fixed but depends on the entire path.

Related Articles:

Min Cost Path

"""







