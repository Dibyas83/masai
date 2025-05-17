
"""

Minimum Sum Path in a Triangle
Last Updated : 06 Nov, 2024
Given a triangular array, find the minimum path sum from top to bottom. For each step, we can move to the adjacent numbers of the row below. i.e., if we are on an index i of the current row, we can move to either index i or index i + 1 on the next row.

Examples :

Input: triangle[][] =  [[2],
                                   [3, 7],
                                  [8, 5, 6],
                                 [6, 1, 9, 3]]
Output: 11
Explanation : The path is 2 → 3 → 5 → 1, which results in a minimum sum of 2 + 3 + 5 + 1 = 11.


Input: triangle[][] =  [[3],
                                   [6, 9],
                                  [8, 7, 1],
                                  [9, 6, 8, 2]]
Output: 15
Explanation: The path is 3 → 9 → 1 → 2, which results in a minimum sum of 3 + 9 + 1 + 2 = 15.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(2 ^ (n*n)) Time and O(n) Space
Using Memoization – O(n*n) Time and O(n*n) Space
Using Tabulation – O(n*n) Time and O(n*n) Space
Using Space Optimized DP – O(n*n) Time and O(n) Space
Using Recursion – O(2 ^ (n*n)) Time and O(n) Space
This problem follows the recursive property. At each position in the triangle, the minimum path sum will depend on the minimum path sums of adjacent positions in the row below. Thus, for any position (i, j) in the triangle, we can find the minimum path sum using the minimum path sums of (i+1, j) and (i+1, j+1) positions. This gives us the following recurrence relation:

minPathSum(i, j) = triangle[i][j] + min(minPathSum(i+1, j), minPathSum(i+1 ,j+1))





1
# Python program to find Minimum Sum Path in
2
# a Triangle using Recursion
3
​
4
​
5
def minSumPathRec(triangle, i, j):
6
​
7
    # Base Case: If we go below the last row return zero.
8
    if i == len(triangle):
9
        return 0
10
​
11
    # Find the current min path sum by recursively calculating
12
    # the minimum path sum of the next row's adjacent elements
13
    return triangle[i][j] + min(minSumPathRec(triangle, i + 1, j),
14
                                minSumPathRec(triangle, i + 1, j + 1))
15
​
16
​
17
def minSumPath(triangle):
18
    return minSumPathRec(triangle, 0, 0)
19
​
20
​
21
triangle = [
22
    [2],
23
    [3, 9],
24
    [1, 6, 7]
25
]
26
​
27
print(minSumPath(triangle))

Output
6
Using Memoization – O(n*n) Time and O(n*n) Space
If we notice carefully, we can observe that this recursive solution holds the following two properties of Dynamic Programming:


1. Optimal Substructure: The minPathSum(i, j), depends on the optimal solution of subproblem minPathSum(i + 1, j) and minPathSum(i + 1, j + 1). By combining these optimal substructures, we can efficiently calculate the minimum path sum of the position (i, j).


2. Overlapping Subproblems: We can see that we are computing the same subproblems multiple times, minPathSum(i + 1, j + 1) will be computed in minPathSum(i, j) as well as minPathSum(i, j + 1). This redundancy leads to overlapping subproblems.


There are two parameters(i and j) that change in the recursive solution and then can go from 0 to n. So we create a 2D array of size n x n for memoization.
We initialize this array as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program to Find Minimum Sum Path in
2
# a Triangle using Memoization
3
​
4
def minSumPathRec(triangle, i, j, memo):
5
​
6
    # Base Case
7
    if i == len(triangle):
8
        return 0
9
​
10
    # if the result for this subproblem is
11
    # already computed then return it
12
    if memo[i][j] != -1:
13
        return memo[i][j]
14
​
15
    # Recursive Case
16
    memo[i][j] = triangle[i][j] + min(minSumPathRec(triangle, i + 1, j, memo),
17
                                      minSumPathRec(triangle, i + 1, j + 1, memo))
18
    return memo[i][j]
19
​
20
​
21
def minSumPath(triangle):
22
    n = len(triangle)
23
​
24
    # Memo array to store the result
25
    memo = [[-1] * n for i in range(n)]
26
    return minSumPathRec(triangle, 0, 0, memo)
27
​
28
​
29
triangle = [
30
    [2],
31
    [3, 9],
32
    [1, 6, 7]
33
]
34
​
35
print(minSumPath(triangle))

Output
6
Using Tabulation – O(n*n) Time and O(n*n) Space
The approach is similar to the previous one; just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner. Maintain a dp[][] table such that dp[i][j] stores the minimum path sum to reach position (i, j).


Base Case: For the last row i.e., i = n – 1, dp[i][j] = triangle[i][j]
Recursive Case: For i < n-1, dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i+1][j+1)



1
# Python program to Find Minimum Sum Path
2
# in a Triangle using Tabulation
3
​
4
def min_sum_path(triangle):
5
    n = len(triangle)
6
​
7
    # DP array to store the result
8
    dp = [[0] * n for _ in range(n)]
9
​
10
    # Base Case: The last row will be the
11
    # same as triangle
12
    for i in range(n):
13
        dp[n - 1][i] = triangle[n - 1][i]
14
​
15
    # Calculation of the remaining rows,
16
    # in bottom up manner
17
    for i in range(n - 2, -1, -1):
18
        for j in range(len(triangle[i])):
19
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j],
20
                                            dp[i + 1][j + 1])
21
​
22
    return dp[0][0]
23
​
24
​
25
triangle = [[2],
26
            [3, 9],
27
            [1, 6, 7]]
28
​
29
print(min_sum_path(triangle))

Output
6
Using Space Optimized DP – O(n*n) Time and O(n) Space
In the above approach, we observe that each subproblem only depends on the results of the next row in the triangle, specifically the two adjacent values directly below. Thus, we can optimize the space complexity by using just a 1D array to store these values.





1
# Python program to Find Minimum Sum Path in a Triangle
2
# using Space Optimized DP
3
​
4
​
5
def minSumPath(triangle):
6
    n = len(triangle)
7

8
    # 1-D dp to store the result
9
    dp = triangle[-1][:]
10
​
11
    # Calculation of the remaining rows,
12
    # in bottom up manner
13
    for i in range(n - 2, -1, -1):
14
        for j in range(len(triangle[i])):
15
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
16
​
17
    return dp[0]
18
​
19
​
20
if __name__ == "__main__":
21
    triangle = [
22
        [2],
23
        [3, 9],
24
        [1, 6, 7]
25
    ]
26
​
27
    print(minSumPath(triangle))

Output
6

"""






