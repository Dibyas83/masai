


"""
Given an matrix of size m x n, the task is to find the count of all unique possible paths from top left to the bottom right with the constraints that from each cell we can either move only to the right or down.

Examples:

Input: m = 2, n = 2
Output: 2
Explanation: There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)


Input: m = 2, n = 3
Output: 3
Explanation: There are three paths
(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)
(0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
(0, 0) -> (1, 0) -> (1, 1) -> (1, 2)


Try it on GfG Practice
redirect icon
Using Recursion – O(2^(n+m)) Time and O(n+m) Space
We can recursively move either to the right or down from the start until we reach the destination and then adding up all valid paths to get the answer. A person can reach  from cell (i, j) to (i+1, j)  or (i, j+1). Thus for each cell (i, j) we can calculate the number of ways to reach destination by  adding up both value. This gives us the following recurrence relation:


numberOfPaths(i, j)  =  numberOfPaths(i+1, j)  +  numberOfPaths(i, j+1)



1
# Python program to count all possible paths
2
# from top left to bottom right
3
# using recursion
4
​
5
​
6
def numberOfPaths(m, n):
7
​
8
    # If either given row number is first
9
    # or given column number is first
10
    if(m == 1 or n == 1):
11
        return 1
12
​
13
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)
14
​
15
​
16
if __name__ == '__main__':
17
    m = 3
18
    n = 3
19
    res = numberOfPaths(m, n)
20
    print(res)

Output
6
Using Top-Down DP (Memoization) – O(m*n) Time and O(m*n) Space
 If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:


1. Optimal Substructure:


 Number of unique possibe path to reach cell (n,m)  depends on the optimal solutions of the subproblems numberOfPaths(n, m-1) and numberOfPaths(n-1, m). By combining these optimal substrutures, we can efficiently calculate the total number of ways to reach the (n, m)th cell.


2. Overlapping Subproblems:


While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times. For example, when calculating numberOfPaths(3, 3), we recursively calculate  numberOfPaths(3, 2) and numberOfPaths(2, 3), which in turn will recursively compute  numberOfPaths(2, 2) again from numberOfPaths(3, 2) and numberOfPaths(2, 3). This redundancy leads to overlapping subproblems.


The recursive solution involves changing two parameters:  m which is representing the current row and n which is representing the current column. We need to track both parameter, so we need to create 2D array of size (m+1) x (n+1). because the m will be in range of [0,m] and n will be in range of [0,n].




1
# Python implementation to count of possible paths to reach
2
# using Using Top-Down DP (Memoization)
3
​
4
def countPaths(m, n, memo):
5
    if n == 1 or m == 1:
6
        memo[m][n] = 1
7
        return 1
8
​
9
    # Add the element in the memo table
10
    # If it was not computed before
11
    if  memo[m][n] == 0:
12
         memo[m][n] = countPaths(m-1,n, memo) + \
13
            countPaths(m,n-1, memo)
14
​
15
    return  memo[m][n]
16
​
17
​
18
def number_of_paths(m, n):
19

20
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
21
    ans = countPaths(m, n, memo)
22
    return ans
23
​
24
if __name__ == "__main__":
25
    n, m = 3, 3
26
​
27
    res = number_of_paths(m, n)
28
    print(res)

Output
6
Using Bottom-Up DP (Tabulation) – O(m * n) Time and O(m * n) Space
The approach is similar to the previous one. just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner. Maintain a dp[][] table such that dp[i][j] stores the count all unique possible paths to reach the cell (i, j).

Base Case:


For i =0 and  0 <= j < m , dp[i][j] = 1
for j=0  and  0 <=i< n , dp[i][j] = 1
Recursive Case:


For i > 1 and j>1 ,  dp[i][j] = dp[i-1][j] + dp[i][j-1]



1
# Python3 program to count all possible paths
2
# from top left to bottom right
3
#  using tabulation
4
​
5
​
6
def numberOfPaths(m, n):
7
​
8
    dp = [[0 for x in range(n)] for y in range(m)]
9
​
10
    # Count of paths to reach any
11
    # cell in first column is 1
12
    for i in range(m):
13
        dp[i][0] = 1
14
​
15
    # Count of paths to reach any
16
    # cell in first row is 1
17
    for j in range(n):
18
        dp[0][j] = 1
19
​
20
    # Calculate count of paths for other
21
    # cells in bottom-up
22
    # manner using the recursive solution
23
    for i in range(1, m):
24
        for j in range(1, n):
25
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
26
    return dp[m - 1][n - 1]
27
​
28
​
29
if __name__ == '__main__':
30
    m = 3
31
    n = 3
32
    res = numberOfPaths(m, n)
33
    print(res)

Output
6
Using Space Optimized DP – O(n*m) Time and O(n) Space
  In the previous approach using dynamic programming, we derived a relation between states as follows:


dp[i][j] = dp[i-1][j]+dp[i][j-1]
If we observe carefully, we see that to calculate the current state dp[i][j] , we need the previous row dp[i-1][j]  value and the current row dp[i][j-1] value. There is no need to store all  previous states  Instead, we can maintain a single prev array to store values from the previous row, and  update its values to represent the current row as we iterate.


dp[j] = dp[j] + dp[j-1]
Here, dp[j-1] represents the value of the current row’s previous cell (i.e., the left cell in the current row, dp[i][j-1]), while dp[j] holds the value from the previous row in the same column (i.e., dp[i-1][j] ).





1
# A Python program to count all possible paths
2
# from top left to bottom right
3
# using space optimised
4
​
5
​
6
def numberOfPaths(p, q):
7
​
8
    # Create a 1D array to store
9
    # results of subproblems
10
    dp = [1 for i in range(q)]
11
    for i in range(p - 1):
12
        for j in range(1, q):
13
            dp[j] += dp[j - 1]
14
    return dp[q - 1]
15
​
16
​
17
if __name__ == '__main__':
18
    print(numberOfPaths(3, 3))

Output
6
Time Complexity: O(m x n), The program uses nested loops to fill the 1D array “dp”. The outer loop runs “m” times, and the inner loop runs “n” times. Therefore, the time complexity of the program is O(m*n).
Auxiliary Space: O(n), The program uses a 1D array “dp” of size “n” to store the results of subproblems. Hence, the space complexity of the program is O(n).

Note: the count can also be calculated using the formula (m-1 + n-1)!/(m-1)! * (n-1)!

Using combinatorics – O(1) Time and O(1) Space
To solve the problem follow the below idea:

In this combinatorics approach, We have to calculate m+n-2Cn-1 here which will be (m+n-2)! / (n-1)! (m-1)!
m = number of rows, n = number of columns.


Total number of moves in which we have to move down to reach the last row = m – 1 (m rows, since we are starting from (1, 1) that is not included)
Total number of moves in which we have to move right to reach the last column = n – 1 (n column, since we are starting from (1, 1) that is not included)


Down moves = (m – 1)
Right moves = (n – 1)
Total moves = Down moves + Right moves = (m – 1) + (n – 1)


Now think of moves as a string of ‘R’ and ‘D’ characters where ‘R’ at any ith index will tell us to move ‘Right’ and ‘D’ will tell us to move ‘Down’. Now think of how many unique strings (moves) we can make where in total there should be (n – 1 + m – 1) characters and there should be (m – 1) ‘D’ character and (n – 1) ‘R’ character?


Choosing positions of (n – 1) ‘R’ characters results in the automatic choosing of (m – 1) ‘D’ character positions


The number of ways to choose positions for (n – 1) ‘R’ character = Total positions C n – 1 = Total positions C m – 1 = (n – 1 + m – 1) !=
(
n
–
1
+
m
–
1
)
!
(
n
–
1
)
!
(
m
–
1
)
!

(n–1)!(m–1)!
(n–1+m–1)!
​



Another way to think about this problem:


Count the Number of ways to make an N digit Binary String (String with 0s and 1s only) with ‘X’ zeros and ‘Y’ ones (here we have replaced ‘R’ with ‘0’ or ‘1’ and ‘D’ with ‘1’ or ‘0’ respectively whichever suits you better)





1
# Python3 program to count all possible
2
# paths from top left to top bottom
3
# using combinatorics
4
​
5
​
6
def numberOfPaths(m, n):
7
    path = 1
8
    # We have to calculate m + n-2 C n-1 here
9
    # which will be (m + n-2)! / (n-1)! (m-1)! path = 1;
10
    for i in range(n, (m + n - 1)):
11
        path *= i
12
        path //= (i - n + 1)
13
​
14
    return path
15
​
16
​
17

18
res = numberOfPaths(3, 3)
19
print(res)

Output
6
Time Complexity: O(m), The time complexity is O(m), where m is the maximum of m and n. This is because the for loop iterates m times, and each iteration involves a constant number of arithmetic operations.
Auxiliary Space: O(1),

"""







