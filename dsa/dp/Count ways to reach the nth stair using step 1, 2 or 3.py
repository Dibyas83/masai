
"""
Count ways to reach the nth stair using step 1, 2 or 3
Last Updated : 12 Dec, 2024
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. The task is to implement a method to count how many possible ways the child can run up the stairs.

Examples:

Input: 4
Output: 7
Explanation: There are seven ways: {1, 1, 1, 1}, {1, 2, 1}, {2, 1, 1}, {1, 1, 2}, {2, 2}, {3, 1}, {1, 3}.


Input: 3
Output: 4
Explanation: There are four ways: {1, 1, 1}, {1, 2}, {2, 1}, {3}.


Table of Content

Using Recursion – O(3^n) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
Using Space Optimized DP – O(n) Time and O(1) Space
Using Matrix Exponentiation – O(log n) Time and O(1) Space
Using Recursion – O(3^n) Time and O(n) Space
There are n stairs, and a person is allowed to jump next stair, skip one stair or skip two stairs. So there are n stairs. So if a person is standing at i-th stair, the person can move to i+1, i+2, i+3-th stair. A recursive function can be formed where at current index i the function is recursively called for i+1, i+2 and i+3 th stair.
There is another way of forming the recursive function. To reach a stair i, a person has to jump either from i-1, i-2 or i-3 th stair.

countWays(n) = countWays(n-1) + countWays(n-2) + countWays(n-3)


Below is the implementation of the above approach:




1
# Python program to count number of
2
# ways to reach nth stair.
3
​
4
def countWays(n):
5

6
    # Base case for 0th stair
7
    if n == 0:
8
        return 1
9

10
    # For invalid stair, return 0.
11
    if n < 0:
12
        return 0
13
​
14
    # Count number of ways to reach (n-1), (n-2),
15
    # (n-3) stair
16
    return countWays(n - 1) + countWays(n - 2) + countWays(n - 3)
17
​
18
if __name__ == "__main__":
19
    n = 4
20
    print(countWays(n))

Output
7
Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:


1. Optimal Substructure:


Number of ways to reach the nth stair, i.e., countWays(n), depends on the optimal solutions of the subproblems countWays(n-1) , countWays(n-2) and countWays(n-3). By combining these optimal substructures, we can efficiently calculate the total number of ways to reach the nth stair.


2. Overlapping Subproblems:


While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times. For example, when calculating countWays(4), we recursively calculate countWays(3) and countWays(2) and  countWays(1) which in turn will recursively compute countWays(2) again. This redundancy leads to overlapping subproblems.


There is only one parameter that changes in the recursive solution and it can go from 0 to n. So we create a 1D array of size n+1 for memoization.
We initialize this array as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program to count number of
2
# ways to reach nth stair.
3
​
4
# Recursive function to count number
5
# of ways to reach nth stair
6
def countWaysRecur(n, memo):
7

8
    # Base case for 0th stair
9
    if n == 0:
10
        return 1
11

12
    # For invalid stair, return 0.
13
    if n < 0:
14
        return 0
15

16
    # If n'th stair is memoized,
17
    # return its value
18
    if memo[n] != -1:
19
        return memo[n]
20
​
21
    # Count number of ways to reach (n-1), (n-2),
22
    # (n-3)th stair and memoize it.
23
    memo[n] = countWaysRecur(n - 1, memo) + \
24
    countWaysRecur(n - 2, memo) + countWaysRecur(n - 3, memo)
25
    return memo[n]
26
​
27
def countWays(n):
28
    memo = [-1] * (n + 1)
29
    return countWaysRecur(n, memo)
30
​
31
if __name__ == "__main__":
32
    n = 4
33
    print(countWays(n))

Output
7
Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
The idea is to create a 1-D array, fill values for first three stairs and compute the values from 3 to n using the previous three results. For i=3 to n, do dp[i] = dp[i-1] + dp[i-2] + dp[i-3].


Below is the implementation of the above approach:




1
# Python program to count number of
2
# ways to reach nth stair.
3
​
4
def countWays(n):
5

6
    # Base case for 0th and 1st stair
7
    if n == 0 or n == 1:
8
        return 1
9

10
    # base case for 2nd stair
11
    if n == 2:
12
        return 2
13

14
    # Initializing a matrix of size n+1
15
    dp = [0] * (n + 1)
16

17
    # insert ans values for 0,1,2 stair
18
    dp[0] = 1
19
    dp[1] = 1
20
    dp[2] = 2
21

22
    # building dp in bottom up manner
23
    for i in range(3, n + 1):
24
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
25

26
    return dp[n]
27
​
28
if __name__ == "__main__":
29
    n = 4
30
    print(countWays(n))

Output
7
Using Space Optimized DP – O(n) Time and O(1) Space
The idea is to store only the previous three computed values. We can observe that for a given stair, only the result of last three stairs are needed. So only store these three values and update them after each step.


Below is the implementation of the above approach:




1
# Python program to count number of
2
# ways to reach nth stair.
3
​
4
def countWays(n):
5
​
6
    # Base case for 0th and 1st stair
7
    if n == 0 or n == 1:
8
        return 1
9
​
10
    # base case for 2nd stair
11
    if n == 2:
12
        return 2
13
​
14
    # Variables to store values
15
    # of previous 3 stairs.
16
    prev3 = 1
17
    prev2 = 1
18
    prev1 = 2
19
​
20
    # building dp in bottom up manner
21
    for i in range(3, n + 1):
22
        val = prev1 + prev2 + prev3
23
​
24
        # Replace previous stair values
25
        # with next stairs.
26
        prev3 = prev2
27
        prev2 = prev1
28
        prev1 = val
29
​
30
    return prev1
31
​
32
if __name__ == "__main__":
33
    n = 4
34
    print(countWays(n))

Output
7
Using Matrix Exponentiation – O(log n) Time and O(1) Space
The recurrence relation for a given step is given as countWays(n) = countWays(n-1) + countWays(n-2) + countWays(n-3) starting with countWays(0)=1, countWays(1)=1, countWays(2)=2.


Refer to Matrix Exponentiation to understand how matrix exponentiation works.

Below is the implementation of the above approach:




1
# Python program to count number of
2
# ways to reach nth stair.
3
​
4
# Function to multiply two 3x3 matrices
5
def multiply(a, b):
6

7
    # Matrix to store the result
8
    c = [[0] * 3 for _ in range(3)]
9
​
10
    for i in range(3):
11
        for j in range(3):
12
            for k in range(3):
13
                c[i][j] += a[i][k] * b[k][j]
14
​
15
    # Copy the result back to the first matrix
16
    for i in range(3):
17
        for j in range(3):
18
            a[i][j] = c[i][j]
19
​
20
# Function to calculate (Matrix M) ^ expo
21
def power(m, expo):
22

23
    # Initialize result with identity matrix
24
    ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
25
​
26
    # Fast Exponentiation
27
    while expo:
28
        if expo & 1:
29
            multiply(ans, m)
30
        multiply(m, m)
31
        expo >>= 1
32
​
33
    return ans
34
​
35
# function to count number of
36
# ways to reach nth stair.
37
def countWays(n):
38

39
    # base condition
40
    if n == 0 or n == 1:
41
        return 1
42
​
43
    # Matrix M to generate the next step value.
44
    m = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
45
​
46
    # first 3 values of steps are:
47
    # findWays(0) = 1
48
    # findWays(1) = 1
49
    # findWays(2) = 2
50
    # f = {{findWays(2), 0, 0}, {findWays(1), 0, 0},
51
    #  {findWays(0), 0,0}}
52
    f = [[2, 0, 0], [1, 0, 0], [1, 0, 0]]
53
​
54
    res = power(m, n - 2)
55
    multiply(res, f)
56
​
57
    return res[0][0]
58
​
59
if __name__ == "__main__":
60
    n = 4
61
    print(countWays(n))

Output
7


"""










