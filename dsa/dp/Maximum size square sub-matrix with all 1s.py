
"""
Given a binary matrix mat of size n * m, the task is to find out the maximum length of a side of a square sub-matrix with all 1s.

Example:

Input:
mat = [
   [0, 1, 1, 0, 1],
   [1, 1, 0, 1, 0],
   [0, 1, 1, 1, 0],
   [1, 1, 1, 1, 0],
   [1, 1, 1, 1, 1],
   [0, 0, 0, 0, 0] ]


Output: 3
Explanation: The maximum length of a side of the square sub-matrix is 3 where every element is 1.


maximum-size-square-sub-matrix-with-all-1s



Input:
mat = [[1, 1],
            [1, 1]]

Output: 2
Explanation: The maximum length of a side of the square sub-matrix is 2. The matrix itself is the maximum sized sub-matrix in this case.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(3^(n+m)) Time and O(n+m) Space
Using Top-Down DP (Memoization) – O(n*m) Time and O(n*m) Space
Using Bottom-Up DP (Tabulation) – O(n*m) Time and O(n*m) Space
Using Space Optimized DP – O(n*m) Time and O(n) Space
Using Recursion – O(3^(n+m)) Time and O(n+m) Space
The idea is to recursively determine the side length of the largest square sub-matrix with all 1s at each cell. For each cell, if its value is 0, we return 0 since it cannot contribute to a square. Otherwise, we calculate the possible side length of a square ending at this cell by finding the minimum square side lengths from the right, bottom, and bottom-right diagonal cells and adding 1 to this minimum. This value gives the largest possible square side length for that cell, and we update the maximum side length by comparing it with the result at each cell.


The recurrence equation will be as follows:

Side(i, j) = 1 + minimum(Side(i, j+1), Side(i+1, j), Side(i+1, j+1)) for cells i, j where mat[i][j] = 1.
Otherwise Side(i,j) = 0.



1
# Python program to find out the maximum length
2
# of a side of a square sub-matrix with all 1s.
3
​
4
def maxSquareRecur(i, j, mat, ans):
5
​
6
    # Return 0 for invalid cells
7
    if i < 0 or i == len(mat) or j < 0 or j == len(mat[0]):
8
        return 0
9
​
10
    # Find the side of square for right, bottom,
11
    # and diagonal cells.
12
    right = maxSquareRecur(i, j + 1, mat, ans)
13
    down = maxSquareRecur(i + 1, j, mat, ans)
14
    diagonal = maxSquareRecur(i + 1, j + 1, mat, ans)
15
​
16
    # If mat[i][j]==0, then square cannot
17
    # be formed.
18
    if mat[i][j] == 0:
19
        return 0
20
​
21
    # Side of square will be
22
    val = 1 + min(right, down, diagonal)
23
    ans[0] = max(ans[0], val)
24
​
25
    return val
26
​
27
def maxSquare(mat):
28
    ans = [0]
29
    maxSquareRecur(0, 0, mat, ans)
30
    return ans[0]
31
​
32
if __name__ == "__main__":
33
    mat = [
34
        [0, 1, 1, 0, 1],
35
        [1, 1, 0, 1, 0],
36
        [0, 1, 1, 1, 0],
37
        [1, 1, 1, 1, 0],
38
        [1, 1, 1, 1, 1],
39
        [0, 0, 0, 0, 0]
40
    ]
41
    print(maxSquare(mat))

Output
3
Using Top-Down DP (Memoization) – O(n*m) Time and O(n*m) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:


1. Optimal Substructure:


The side of square originating from i, j, i.e., maxSquare(i, j), depends on the optimal solutions of the subproblems maxSquare(i, j+1) , maxSquare(i+1, j) and maxSquare(i+1, j+1). By finding the minimum value in these optimal substructures, we can efficiently calculate the side of square at (i,j).


2. Overlapping Subproblems:


While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times.


There are two parameters, i and j that changes in the recursive solution. So we create a 2D array of size n*m for memoization.
We initialize this array as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program to find out the maximum length
2
# of a side of a square sub-matrix with all 1s.
3
​
4
def maxSquareRecur(i, j, mat, ans, memo):
5
​
6
    # Return 0 for invalid cells
7
    if i < 0 or i == len(mat) or j < 0 or j == len(mat[0]):
8
        return 0
9
​
10
    # If value is memoized, return value.
11
    if memo[i][j] != -1:
12
        return memo[i][j]
13
​
14
    # Find the side of square for right, bottom,
15
    # and diagonal cells.
16
    right = maxSquareRecur(i, j + 1, mat, ans, memo)
17
    down = maxSquareRecur(i + 1, j, mat, ans, memo)
18
    diagonal = maxSquareRecur(i + 1, j + 1, mat, ans, memo)
19
​
20
    # If mat[i][j]==0, then square cannot
21
    # be formed.
22
    if mat[i][j] == 0:
23
        memo[i][j] = 0
24
        return 0
25
​
26
    # Side of square will be
27
    val = 1 + min(right, down, diagonal)
28
    ans[0] = max(ans[0], val)
29
​
30
    # Memoize the value and return it.
31
    memo[i][j] = val
32
    return val
33
​
34
​
35
def maxSquare(mat):
36
    n, m = len(mat), len(mat[0])
37
    ans = [0]
38
​
39
    # Create 2d array for memoization
40
    memo = [[-1 for _ in range(m)] for _ in range(n)]
41
    maxSquareRecur(0, 0, mat, ans, memo)
42
    return ans[0]
43
​
44
​
45
if __name__ == "__main__":
46
    mat = [
47
        [0, 1, 1, 0, 1],
48
        [1, 1, 0, 1, 0],
49
        [0, 1, 1, 1, 0],
50
        [1, 1, 1, 1, 0],
51
        [1, 1, 1, 1, 1],
52
        [0, 0, 0, 0, 0]
53
    ]
54
    print(maxSquare(mat))

Output
3
Using Bottom-Up DP (Tabulation) – O(n*m) Time and O(n*m) Space
The approach is similar to the previous one. just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner. The idea is to create a 2-D array. Then fill the values using dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) for cells having value equal to 1. Otherwise, set dp[i][j] = 0.





1
# Python program to find out the maximum length
2
# of a side of a square sub-matrix with all 1s.
3
​
4
def maxSquare(mat):
5
    n, m = len(mat), len(mat[0])
6
    ans = 0
7
​
8
    # Create 2d array for tabulation
9
    dp = [[0] * (m + 1) for _ in range(n + 1)]
10
​
11
    # Fill the dp
12
    for i in range(n - 1, -1, -1):
13
        for j in range(m - 1, -1, -1):
14
​
15
            # If square cannot be formed
16
            if mat[i][j] == 0:
17
                dp[i][j] = 0
18
                continue
19
​
20
            dp[i][j] = 1 + min(dp[i][j + 1], \
21
                               dp[i + 1][j], dp[i + 1][j + 1])
22
​
23
            ans = max(ans, dp[i][j])
24
​
25
    return ans
26
​
27
if __name__ == "__main__":
28
    mat = [
29
        [0, 1, 1, 0, 1],
30
        [1, 1, 0, 1, 0],
31
        [0, 1, 1, 1, 0],
32
        [1, 1, 1, 1, 0],
33
        [1, 1, 1, 1, 1],
34
        [0, 0, 0, 0, 0]
35
    ]
36
    print(maxSquare(mat))

Output
3
Using Space Optimized DP – O(n*m) Time and O(n) Space
The idea is store the values for the next column only. We can observe that for a given cell (i,j), its value is only dependent on the two cells of the next column and the bottom cell of current column.





1
# Python program to find out the maximum length
2
# of a side of a square sub-matrix with all 1s.
3
​
4
def maxSquare(mat):
5
    n, m = len(mat), len(mat[0])
6
    ans = 0
7
​
8
    # Create 1d array
9
    dp = [0] * (n + 1)
10
​
11
    # variable to store the value of
12
    # {i, j+1} as its value will be
13
    # lost while setting dp[i][j+1].
14
    diagonal = 0
15
​
16
    # Traverse column by column
17
    for j in range(m - 1, -1, -1):
18
        for i in range(n - 1, -1, -1):
19
            tmp = dp[i]
20
​
21
            # If square cannot be formed
22
            if mat[i][j] == 0:
23
                dp[i] = 0
24
            else:
25
                dp[i] = 1 + min(dp[i], \
26
                                diagonal, dp[i + 1])
27
​
28
            diagonal = tmp
29
            ans = max(ans, dp[i])
30
​
31
    return ans
32
​
33
if __name__ == "__main__":
34
    mat = [
35
        [0, 1, 1, 0, 1],
36
        [1, 1, 0, 1, 0],
37
        [0, 1, 1, 1, 0],
38
        [1, 1, 1, 1, 0],
39
        [1, 1, 1, 1, 1],
40
        [0, 0, 0, 0, 0]
41
    ]
42
    print(maxSquare(mat))

Output
3


"""








