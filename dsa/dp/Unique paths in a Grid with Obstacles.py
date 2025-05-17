

"""
Given a grid[][] of size m * n, let us assume we are starting at (1, 1) and our goal is to reach (m, n). At any instance, if we are on (x, y), we can either go to (x, y + 1) or (x + 1, y). The task is to find the number of unique paths if some obstacles are added to the grid.
Note: An obstacle and space are marked as 1 and 0 respectively in the grid.

Examples:

Input:
grid[][] = [[0, 0, 0],
                  [0, 1, 0],
                 [0, 0, 0]]


Output: 2
Explanation: There are two ways to reach the bottom-right corner:


Right -> Right -> Down -> Down
Down -> Down -> Right -> Right
Input:
grid[][] = [[0, 1],
                 [0, 0]]


Output: 1
Explanation: There is only one way to reach the bottom-right corner:


Down -> Right
Table of Content

Using Recursion – O(2^(m*n)) Time and O(m+n) Space
Using Top-Down DP(Memoization) – O(m*n) Time and O(m*n) Space
Using Bottom-Up DP (Tabulation) – O(m*n) Time and O(m*n) Space
Using Space Optimised DP – O(m*n) Time and O(n) Space
Using Recursion – O(2^(m*n)) Time and O(m+n) Space
We have discussed the problem of counting the number of unique paths in a Grid when no obstacle was present in the grid. But here the situation is quite different. While moving through the grid, we can get some obstacles that we can not jump and the way to reach the bottom right corner is blocked.

For this approach, the recursive solution will explore two main cases from each cell:

Move to the cell below the current position.
Move to the cell to the right of the current position.
Base Cases:


If i == r or j == c: The current position is out of bounds, so there are no paths available. Return 0.
If grid[i][j] == 1: The current cell is an obstacle, so it cannot be used. Return 0.
If i == r-1 and j == c-1: The function has reached the destination, so there is exactly one path. Return 1.
The recurrence relation will be:


UniquePathHelper(i, j, r, c, grid) = UniquePathHelper(i+1, j, r, c, grid) + UniquePathHelper(i, j+1, r, c, grid)



1
# Python code to find number of unique paths
2
# using Recursion
3
​
4
# Helper function to find unique paths recursively
5
def UniquePathHelper(i, j, r, c, grid):
6

7
    # If out of bounds, return 0
8
    if i == r or j == c:
9
        return 0
10
​
11
    # If cell is an obstacle, return 0
12
    if grid[i][j] == 1:
13
        return 0
14

15
    # If reached the bottom-right cell, return 1
16
    if i == r-1 and j == c-1:
17
        return 1
18
​
19
    # Recur for the cell below and the cell to the right
20
    return UniquePathHelper(i+1, j, r, c, grid) + \
21
           UniquePathHelper(i, j+1, r, c, grid)
22
​
23
# Function to find unique paths with obstacles
24
def uniquePathsWithObstacles(grid):
25
    r, c = len(grid), len(grid[0])
26
    return UniquePathHelper(0, 0, r, c, grid)
27
​
28
if __name__ == "__main__":
29

30
  grid = [[0, 0, 0],
31
          [0, 1, 0],
32
          [0, 0, 0]]
33
​
34
  print(uniquePathsWithObstacles(grid))

Output
2
Using Top-Down DP(Memoization) – O(m*n) Time and O(m*n) Space
1. Optimal Substructure
The solution for finding unique paths from (0, 0) to (r-1, c-1) can be broken down into smaller subproblems. Specifically, to find the number of unique paths to any cell (i, j), we need the results of two smaller subproblems:


The number of paths to the cell below, (i+1, j).
The number of paths to the cell to the right, (i, j+1).
2. Overlapping Subproblems
When implementing a recursive solution to find the number of unique paths in a grid with obstacles, we observe that many subproblems are computed multiple times. For instance, when computing UniquePathHelper(i, j), where i and j represent the current cell in the grid, we might need to compute the same value for the same cell multiple times during recursion.


The recursive solution involves changing two parameters: the current row index i and the current column index j representing the current position in the grid. To track the results for each cell, we create a 2D array of size r x c where r is the number of rows and c is the number of columns in the grid. The value of i will range from 0 to r-1 and j will range from 0 to c-1.
We initialize the 2D array with -1 to indicate that no subproblems have been computed yet.
We check if the value at memo[i][j] is -1. If it is, we proceed to compute the result. otherwise, we return the stored result.



1
# Python code to find number of unique paths
2
# using Memoization
3
​
4
# Helper function to find unique paths recursively
5
# with memoization
6
def UniquePathHelper(i, j, r, c, grid, memo):
7

8
    # If out of bounds, return 0
9
    if i == r or j == c:
10
        return 0
11
​
12
    # If cell is an obstacle, return 0
13
    if grid[i][j] == 1:
14
        return 0
15

16
    # If reached the bottom-right cell, return 1
17
    if i == r-1 and j == c-1:
18
        return 1
19
​
20
    # If value is already computed, return it
21
    if (i, j) in memo:
22
        return memo[(i, j)]
23
​
24
    # Memoize the result of recursive calls
25
    memo[(i, j)] = UniquePathHelper(i+1, j, r, c, grid, memo) + \
26
                   UniquePathHelper(i, j+1, r, c, grid, memo)
27

28
    return memo[(i, j)]
29
​
30
# Function to find unique paths with obstacles
31
def uniquePathsWithObstacles(grid):
32
    r, c = len(grid), len(grid[0])
33
    memo = {}
34
    return UniquePathHelper(0, 0, r, c, grid, memo)
35
​
36
if __name__ == "__main__":
37

38
  grid = [[0, 0, 0],
39
          [0, 1, 0],
40
          [0, 0, 0]]
41
​
42
  print(uniquePathsWithObstacles(grid))

Output
2
Using Bottom-Up DP (Tabulation) – O(m*n) Time and O(m*n) Space
In this case, the problem is to find the number of unique paths in a grid with obstacles. The state dp[i][j] will represent the number of unique paths to reach the cell (i, j).

Dynamic Programming Relation:


Base Case: The starting point (0, 0) is initialized to 1 if it is not an obstacle (grid[0][0] == 0).
For each cell (i, j): If the cell contains an obstacle (grid[i][j] == 1), then there are no paths to this cell, so dp[i][j] = 0.
Otherwise, if there is no obstacle, we calculate the number of paths by accumulating paths from the cell above (dp[i-1, j]) and from the left (dp[i, j-1]), i.e dp[i][j] = dp[i-1][j] + dp[i][j-1]
This means that for each cell, we check the cells directly above and to the left. If either of those cells has a valid path, we add it to the current cell.




1
# Python code to find unique paths with obstacles
2
# using tabulation
3
def uniquePathsWithObstacles(grid):
4
    r, c = len(grid), len(grid[0])
5

6
    # Initialize DP table with zeros
7
    dp = [[0] * c for _ in range(r)]
8
​
9
    # Initialize starting cell if there's
10
    # no obstacle
11
    if grid[0][0] == 0:
12
        dp[0][0] = 1
13
​
14
    # Fill the DP table
15
    for i in range(r):
16
        for j in range(c):
17

18
            # If cell has an obstacle, set
19
            # paths to 0
20
            if grid[i][j] == 1:
21
                dp[i][j] = 0
22
            else:
23

24
                # Accumulate paths from top cell
25
                if i > 0:
26
                    dp[i][j] += dp[i-1][j]
27

28
                # Accumulate paths from left cell
29
                if j > 0:
30
                    dp[i][j] += dp[i][j-1]
31
​
32
    # Return paths count for the
33
    # bottom-right cell
34
    return dp[r-1][c-1]
35
​
36
if __name__ == "__main__":
37

38
  grid = [[0, 0, 0],
39
          [0, 1, 0],
40
          [0, 0, 0]]
41
​
42
  print(uniquePathsWithObstacles(grid))

Output
2
Using Space Optimised DP – O(m*n) Time and O(n) Space
Since each dp[i][j] only depends on the previous row and the current row’s left cell, we can optimize space by using a single 1D array dp of size c (number of columns).

dp[j] holds the cumulative paths up to the current cell in the previous row,
dp[j – 1] adds paths from the left cell of the current row.
After all rows are processed, dp[c-1] will contain the total unique paths to reach the bottom-right corner of the grid.



1
# Python code to find unique paths with
2
# obstacles using space optimization
3
​
4
def uniquePathsWithObstacles(grid):
5
    r, c = len(grid), len(grid[0])
6
​
7
    # Initialize DP array with zeros
8
    dp = [0] * c
9
​
10
    # Set the starting cell if there's
11
    # no obstacle
12
    dp[0] = 1 if grid[0][0] == 0 else 0
13
​
14
    # Fill the DP array for each row
15
    for i in range(r):
16
        for j in range(c):
17

18
            # If there's an obstacle,
19
            # set dp[j] to 0
20
            if grid[i][j] == 1:
21
                dp[j] = 0
22
            elif j > 0:
23

24
                # Add the value from the
25
                # left cell
26
                dp[j] += dp[j - 1]
27
​
28
    # Return paths count for the
29
    # bottom-right cell
30
    return dp[c - 1]
31
​
32
if __name__ == "__main__":
33

34
    grid = [[0, 0, 0],
35
            [0, 1, 0],
36
            [0, 0, 0]]
37
​
38
    print(uniquePathsWithObstacles(grid))

Output
2

"""








