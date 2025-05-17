
"""
Given a fence with n posts and k colors, the task is to find out the number of ways of painting the fence so that not more than two consecutive posts have the same color.

Examples:

Input: n = 2, k = 4
Output: 16
Explanation: We have 4 colors and 2 posts.
Ways when both posts have same color: 4
Ways when both posts have diff color: 4(choices for 1st post) * 3(choices for 2nd post) = 12


Input: n = 3, k = 2
Output: 6
Explanation: The following image depicts the 6 possible ways of painting 3 posts with 2 colors:


painting-fence-algorithm-2
Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(2^n) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
Using Space Optimized DP – O(n) Time and O(1) Space
Using Recursion – O(2^n) Time and O(n) Space
The idea is to define our solution in terms of two choices: painting the last post a different color from the previous one or painting the last two posts the same color. This gives us the recurrence relation:


countWays(n) = countWays(n-1)*(k-1) + countWays(n-2)*(k-1)


Case 1: Different Color for the Last Post
If we paint the last post a different color from the one before it, we have k-1 choices (all colors except the previous post’s color). This means the number of ways to paint the first n-1 posts is multiplied by k-1.


Case 2: Same Color for the Last Two Posts
If the last two posts are the same color, they must differ from the post before them (the third-last post). Thus, we have k-1 choices for the last two posts, and the number of ways to paint the first n-2 posts is given by countWays(n-2).


Consider the following image, in which c, c’ and c” are the respective colors of posts i, i-1, and i-2.

painting-fence-algorithm





1
# Python program for Painting Fence Algorithm
2
# using recursion
3
​
4
# Returns count of ways to color k posts
5
def countWays(n, k):
6

7
    # base cases
8
    if n == 1:
9
        return k
10
    if n == 2:
11
        return k * k
12

13
    # Ways in which last fence
14
    # is of different color.
15
    cnt1 = countWays(n - 1, k) * (k - 1)
16

17
    # Ways in which last 2 fences
18
    # are of same color.
19
    cnt2 = countWays(n - 2, k) * (k - 1)
20

21
    return cnt1 + cnt2
22
​
23
if __name__ == "__main__":
24
    n = 3
25
    k = 2
26
    print(countWays(n, k))

Output
6
Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:


1. Optimal Substructure:


Number of ways to paint the nth fence, i.e., countWays(n), depends on the solutions of the subproblems countWays(n-1) , and countWays(n-2). By adding these optimal substructures, we can efficiently calculate the total number of ways to reach the nth fence.


2. Overlapping Subproblems:


While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times. For example, when calculating countWays(4), we recursively calculate countWays(3) and countWays(2) which in turn will recursively compute countWays(2) again. This redundancy leads to overlapping subproblems.


There is only one parameter that changes in the recursive solution and it can go from 1 to n. So we create a 1D array of size n+1 for memoization.
We initialize this array as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program for Painting Fence Algorithm
2
# using memoization
3
​
4
def countWaysRecur(n, k, memo):
5

6
    # base cases
7
    if n == 1:
8
        return k
9
    if n == 2:
10
        return k * k
11

12
    if memo[n] != -1:
13
        return memo[n]
14

15
    # Ways in which last fence
16
    # is of different color.
17
    cnt1 = countWaysRecur(n - 1, k, memo) * (k - 1)
18

19
    # Ways in which last 2 fences
20
    # are of same color.
21
    cnt2 = countWaysRecur(n - 2, k, memo) * (k - 1)
22

23
    memo[n] = cnt1 + cnt2
24
    return memo[n]
25
​
26
# Returns count of ways to color k posts
27
def countWays(n, k):
28

29
    memo = [-1] * (n + 1)
30
    return countWaysRecur(n, k, memo)
31
​
32
if __name__ == "__main__":
33
    n = 3
34
    k = 2
35
    print(countWays(n, k))

Output
6
Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
The idea is to create a 1-D array, fill values for first two fences and compute the values from 3 to n using the previous two results. For i = 3 to n, do dp[i] = dp[i-1]*(k-1) + dp[i-2]*(k-1).





1
# Python program for Painting Fence Algorithm
2
# using tabulation
3
​
4
def countWays(n, k):
5

6
    # base cases
7
    if n == 1:
8
        return k
9
    if n == 2:
10
        return k * k
11

12
    dp = [0] * (n + 1)
13

14
    # Fill value for 1 and 2 fences
15
    dp[1] = k
16
    dp[2] = k * k
17

18
    for i in range(3, n + 1):
19
        dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
20

21
    return dp[n]
22
​
23
if __name__ == "__main__":
24
    n = 3
25
    k = 2
26
    print(countWays(n, k))

Output
6
Using Space Optimized DP – O(n) Time and O(1) Space
The idea is to store only the previous two computed values. We can observe that for a given fence, only the result of last three fences are needed. So only store these three values and update them after each step.





1
# Python program for Painting Fence Algorithm
2
# using space optimised
3
​
4
def countWays(n, k):
5

6
    # base cases
7
    if n == 1:
8
        return k
9
    if n == 2:
10
        return k * k
11

12
    # Fill value for 1 and 2 fences
13
    prev2 = k
14
    prev1 = k * k
15

16
    for i in range(3, n + 1):
17
        curr = prev1 * (k - 1) + prev2 * (k - 1)
18

19
        # update the values
20
        prev2 = prev1
21
        prev1 = curr
22

23
    return prev1
24
​
25
if __name__ == "__main__":
26
    n = 3
27
    k = 2
28
    print(countWays(n, k))

Output
6

"""





