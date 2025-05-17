
"""
Climbing stairs to reach the top
Last Updated : 11 Jan, 2025
There are n stairs, and a person standing at the bottom wants to climb stairs to reach the top. The person can climb either 1 stair or 2 stairs at a time, the task is to count the number of ways that a person can reach at the top.

Note: This problem is similar to Count ways to reach Nth stair (Order does not matter) with the only difference that in this problem, we count all distinct ways where different orderings of the steps are considered unique.

Examples:

Input: n = 1
Output: 1
Explanation: There is only one way to climb 1 stair.


Input: n = 2
Output: 2
Explanation: There are two ways to reach 2th stair: {1, 1} and {2}.


Input: n = 4
Output: 5
Explanation: There are five ways to reach 4th stair: {1, 1, 1, 1}, {1, 1, 2}, {2, 1, 1}, {1, 2, 1} and {2, 2}.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(2^n) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
Using Space Optimized DP – O(n) Time and O(1) Space
Using Matrix Exponentiation – O(logn) Time and O(1) Space
Using Recursion – O(2^n) Time and O(n) Space
We can easily identify the recursive nature of this problem. A person can reach nth stair either from (n-1)th stair or (n-2)th stair. Thus, for each stair n, we calculate the number of ways to reach the (n-1)th and (n-2)th stairs, and add them to get the total number of ways to reach the nth stair. This gives us the following recurrence relation:

countWays(n) = countWays(n-1) + countWays(n-2)


Note: The above recurrence relation is same as Fibonacci numbers.




1
# Python program to count number of ways to reach
2
# nth stair using recursion
3
​
4
def countWays(n):
5
​
6
    # Base cases: If there are 0 or 1 stairs,
7
    # there is only one way to reach the top.
8
    if n == 0 or n == 1:
9
        return 1
10
​
11
    return countWays(n - 1) + countWays(n - 2)
12
​
13
n = 4
14
print(countWays(n))

Output
5
Time Complexity: O(2n), as we are making two recursive calls for each stair.
Auxiliary Space: O(n), as we are using recursive stack space.

Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:


1. Optimal Substructure:


Number of ways to reach the nth stair, i.e., countWays(n), depends on the optimal solutions of the subproblems countWays(n-1) and countWays(n-2). By combining these optimal substructures, we can efficiently calculate the total number of ways to reach the nth stair.


2. Overlapping Subproblems:


While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times. For example, when calculating countWays(4), we recursively calculate countWays(3) and countWays(2), which in turn will recursively compute countWays(2) again. This redundancy leads to overlapping subproblems.


Recursion-tree-for-Climbing-Stairs
Overlapping Subproblems in Climbing Stairs

There is only one parameter that changes in the recursive solution and it can go from 0 to n. So we create a 1D array of size n+1 for memoization.
We initialize this array as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program to count number of ways to reach nth stair
2
# using memoization
3
​
4
def countWaysRec(n, memo):
5

6
    # Base cases
7
    if n == 0 or n == 1:
8
        return 1
9
​
10
    # if the result for this subproblem is
11
    # already computed then return it
12
    if memo[n] != -1:
13
        return memo[n]
14
​
15
    memo[n] = countWaysRec(n - 1, memo) + countWaysRec(n - 2, memo)
16
    return memo[n]
17
​
18
def countWays(n):
19

20
    # Memoization array to store the results
21
    memo = [-1] * (n + 1)
22
    return countWaysRec(n, memo)
23
​
24
if __name__ == "__main__":
25
    n = 4
26
    print(countWays(n))

Output
5
Time Complexity: O(n), as we compute each subproblem only once using memoization.
Auxiliary Space: O(n), due to the memoization array and the recursive stack space(both take linear space only).

Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
The approach is similar to the previous one; just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner. Maintain a dp[] table such that dp[i] stores the number of ways to reach ith stair.


Base Case: For i = 0 and i = 1, dp[i] = 1
Recursive Case: For i > 1, dp[i] = dp[i – 1] + dp[i – 2]
illustration:

Climbing-stairs-to-reach-the-top-1.webpClimbing-stairs-to-reach-the-top-1.webp



1
# Python program to count number of ways
2
# to reach nth stair using Tabulation
3
​
4
def countWays(n):
5
    dp = [0] * (n + 1)
6

7
    # Base cases
8
    dp[0] = 1
9
    dp[1] = 1
10
​
11
    for i in range(2, n + 1):
12
        dp[i] = dp[i - 1] + dp[i - 2];
13

14
    return dp[n]
15
​
16
n = 4
17
print(countWays(n))

Output
5
Using Space Optimized DP – O(n) Time and O(1) Space
In the above approach, we observe that each subproblem only depends on the results of previous two subproblems, that is dp[i] depends on dp[i – 1] and dp[i – 2] only. So, we can optimize the space complexity by using just two variables to store these last two values.





1
# Python program to count number of ways to
2
# reach nth stair using Space Optimized DP
3
​
4
def countWays(n):
5

6
    # variable prev1, prev2 - to store the
7
    # values of last and second last states
8
    prev1 = 1
9
    prev2 = 1
10

11
    for i in range(2, n + 1):
12
        curr = prev1 + prev2
13
        prev2 = prev1
14
        prev1 = curr
15

16
    # In last iteration final value
17
    # of curr is stored in prev.
18
    return prev1
19
​
20
n = 4
21
print(countWays(n))

Output
5
Using Matrix Exponentiation – O(logn) Time and O(1) Space
This problem is quite similar to the Fibonacci approach, with only one difference in the base case (the Fibonacci sequence value for 0 is 0, whereas in this problem it is 1). To know more about how to calculate fibonacci number using Matrix Exponentiation, please refer to this post.




1
# Python Program to count no. of ways to reach
2
# nth stairs using matrix Exponentiation
3
​
4
def multiply(a, b):
5

6
    # Matrix to store the result
7
    res = [[0, 0], [0, 0]]
8
​
9
    # Matrix Multiplication
10
    res[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
11
    res[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
12
    res[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
13
    res[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
14
​
15
    # Copy the result back to the first matrix
16
    a[0][0] = res[0][0]
17
    a[0][1] = res[0][1]
18
    a[1][0] = res[1][0]
19
    a[1][1] = res[1][1]
20
​
21
def power(m, expo):
22

23
    # Initialize result with identity matrix
24
    res = [[1, 0], [0, 1]]
25
​
26
    while expo > 0:
27
        if expo & 1:
28
            multiply(res, m)
29
        multiply(m, m)
30
        expo >>= 1
31
​
32
    return res
33
​
34
def countWays(n):
35

36
    # base case
37
    if n == 0 or n == 1:
38
        return 1
39
​
40
    m = [[1, 1], [1, 0]]
41

42
    # Matrix initialMatrix = {{f(1), 0}, {f(0), 0}}, where f(0)
43
    # and f(1) are first two terms of sequence
44
    initialMatrix = [[1, 0], [1, 0]]
45
​
46
    # Multiply matrix m (n - 1) times
47
    res = power(m, n - 1)
48
​
49
    multiply(res, initialMatrix)
50
​
51
    # Return the final result as an integer
52
    return res[0][0]
53
​
54
n = 4
55
print(countWays(n))

Output
5

"""





