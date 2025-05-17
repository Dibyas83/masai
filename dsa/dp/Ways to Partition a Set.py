

"""

Bell Numbers (Number of ways to Partition a Set)
Last Updated : 09 Nov, 2024
Given a set of n elements, find the number of ways of partitioning it.

Examples:

Input:  n = 2
Output: 2
Explanation: Let the set be {1, 2}. The partitions are {{1},{2}} and {{1, 2}}.


Input:  n = 3
Output: 5
Explanation: Let the set be {1, 2, 3}. The partitions are {{1},{2},{3}}, {{1},{2, 3}}, {{2},{1, 3}}, {{3},{1, 2}}, {{1, 2, 3}}.


Try it on GfG Practice
redirect icon
What is a Bell Number?
Let S(n, k) be total number of partitions of n elements into k sets. The value of the n’th Bell Number is the sum of S(n, k) for k = 1 to n.
Bell(n)=∑​S (n,k) for k ranges from [1,n]
Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)

How does above recursive formula work?
When we add a (n+1)’th element to k partitions, there are two possibilities.
1) It is added as a single element set to existing partitions, i.e, S(n, k-1)
2) It is added to all sets of every partition, i.e., k*S(n, k).
First few Bell numbers are 1, 1, 2, 5, 15, 52, 203, ….

Table of Content

Using recursion – O(2 ^ n)  Time and O(n) Space
Using Top-Down DP (Memoization) – O(n^2) Time and O(n^2) Space
Using Bottom-Up DP (Tabulation – 1) – O(n^2) Time and O(n^2) Space
Using Bottom-Up DP (Tabulation – 2) – O(n^2) Time and O(n^2) Space
Using Space Optimized DP – O(n^2) Time and O(n) Space
Using recursion – O(2 ^ n)  Time and O(n) Space
We can recursively calculate the number of ways to partition a set of n elements by considering each element and either placing it in an existing subset or creating a new subset. For each element, we calculate the number of ways to partition the remaining n-1 elements into k subsets and then sum these values for all possible k. This gives us the following recurrence relation for Stirling numbers of the second kind:


S(n,k) = k * S( n – 1, k) + S(n – 1, k – 1)
Finally, to find the Bell number, we sum S(n, k) for all values of k from 1 to n. This gives us the total number of ways to partition the set.





1
# Python program to find the Bell Number using recursion
2
​
3
# Function to compute Stirling numbers of
4
# the second kind S(n, k) with memoization
5
def stirling(n, k):
6

7
    # Base cases
8
    if n == 0 and k == 0: return 1
9
    if k == 0 or n == 0: return 0
10
    if n == k: return 1
11
    if k == 1: return 1
12
​
13
    # Recursive formula
14
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)
15
​
16
# Function to calculate the total number of
17
# ways to partition a set of `n` elements
18
def bellNumber(n):
19
​
20
    result = 0
21
​
22
    # Sum up Stirling numbers S(n, k) for
23
    # all k from 1 to n
24
    for k in range(1, n + 1):
25
        result += stirling(n, k)
26
    return result
27
​
28
n = 5
29
result = bellNumber(n)
30
print(result)

Output
52
Using Top-Down DP (Memoization) – O(n^2) Time and O(n^2) Space
 If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:


1. Optimal Substructure:  The number of ways to partition a set of n elements into k subsets depends on two smaller subproblems:


The number of ways to partition the first n-1 elements into k subsets, and
The number of ways to partition the first n-1 elements into k-1 subsets and then add the new element as its own subset. By combining these optimal solutions, we can efficiently calculate the total number of ways to partition the set.
2. Overlapping Subproblems: In the recursive approach, certain subproblems are recalculated multiple times. For example, when computing S(n, k), the subproblems S(n-1, k) and S(n-1, k-1) are recomputed multiple times. This redundancy leads to overlapping subproblems, which can be avoided using memoization or tabulation.


Follow the steps below to solve the problem:

Use recursion with memoization to calculate Stirling numbers of the second kind, S(n,k), which represent the number of ways to partition n items into k non-empty subsets.
Define base cases for S(0, 0), S(n, 0), S(n, n), and S(n, 1) to handle specific situations in the recursive formula.
Use the formula S(n, k) = k × S(n-1, k) + S(n-1, k-1) to compute the Stirling numbers with previously stored results.
For a given n, sum S(n, k) for all from 1 to n to calculate the Bell number, which represents the total ways to partition n elements.
Output the computed Bell number for the given n.



1
# Python code of finding the bellNumber
2
# Using Memoization
3
​
4
# Function to compute Stirling numbers of
5
# the second kind S(n, k) with memoization
6
​
7
def stirling(n, k, memo):
8
​
9
    # Base cases
10
    if n == 0 and k == 0:
11
        return 1
12
    if k == 0 or n == 0:
13
        return 0
14
    if n == k:
15
        return 1
16
    if k == 1:
17
        return 1
18
​
19
    # Check if result is already
20
    # computed
21
    if memo[n][k] != -1:
22
        return memo[n][k]
23
​
24
    # Recursive formula
25
    memo[n][k] = k * stirling(n - 1, k, memo) + stirling(n - 1, k - 1, memo)
26
    return memo[n][k]
27
​
28
# Function to calculate the total number of
29
# ways to partition a set of n elements
30
​
31
def bellNumber(n):
32

33
    # Initialize memoization table with -1
34
    memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
35
    result = 0
36
​
37
    # Sum up Stirling numbers S(n, k) for all k from 1 to n
38
    for k in range(1, n + 1):
39
        result += stirling(n, k, memo)
40
    return result
41
​
42
if __name__ == "__main__":
43

44
    n = 5
45
    result = bellNumber(n)
46
    print(result)

Output
52
Using Bottom-Up DP (Tabulation – 1) – O(n^2) Time and O(n^2) Space
A Simple Method to compute n’th Bell Number is to one by one compute S(n, k) for k = 1 to n and return sum of all computed values. Refer Count number of ways to partition a set into k subsets for computation of S(n, k).





1
# Python code to calculate the Bell number for a given integer `n`
2
​
3
# Function to calculate the Bell number for a
4
# given integer `n`
5
def bellNumber(n):
6
​
7
    # Create a 2D list for Stirling numbers of
8
    # the second kind
9
    dp = [[0] * (n + 1) for _ in range(n + 1)]
10
​
11
    # Fill the table using dynamic programming
12
    for i in range(n + 1):
13
        for j in range(n + 1):
14
​
15
            # These are some base cases
16
            if j > i:
17
                dp[i][j] = 0
18
            elif i == j:
19
                dp[i][j] = 1
20
            elif i == 0 or j == 0:
21
                dp[i][j] = 0
22
            else:
23
​
24
                # Recurrence relation: Stirling number calculation
25
                dp[i][j] = j * dp[i - 1][j] + dp[i - 1][j - 1]
26
​
27
    # Sum up Stirling numbers for all j
28
    # from 0 to n to get the Bell number
29
    ans = 0
30
    for i in range(n + 1):
31
        ans += dp[n][i]
32
​
33
    # Return the Bell number
34
    return ans
35
​
36
​
37
if __name__ == "__main__":
38
​
39
    n = 5
40
    result = bellNumber(n)
41
    print(result)

Output
52
Using Bottom-Up DP (Tabulation – 2) – O(n^2) Time and O(n^2) Space
A Better Method is to use Bell Triangle. Below is a sample Bell Triangle for first few Bell Numbers.



1
1 2
2 3 5
5 7 10 15
15 20 27 37 52


Follow the steps below to solve the problem:

Create a 2D array to store Bell numbers, starting with bell[0][0] = 1 as the base case.
Use dynamic programming to fill the table based on the recurrence relation. For each i, set bell[i][0] = bell[i-1][i-1] and compute bell[i][j] using the formula bell[i][j] = bell[i-1][j-1] + bell[i][j-1] for all valid j.
The formula computes the Bell numbers by using the Stirling numbers of the second kind, which count ways to partition a set of i elements into j non-empty subsets.
The Bell number for n is stored in bell[n][0].



1
# Python program to find n'th Bell number
2
​
3
# Function to calculate the Bell number for a given integer `n`
4
def bellNumber(n):
5
    dp = [[0] * (n + 1) for _ in range(n + 1)]
6
    dp[0][0] = 1
7
​
8
    for i in range(1, n + 1):
9

10
        # Explicitly fill for j = 0
11
        dp[i][0] = dp[i - 1][i - 1]
12
​
13
        # Fill for remaining values of j
14
        for j in range(1, i + 1):
15
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
16
​
17
    return dp[n][0]
18
​
19
​
20
if __name__ == "__main__":
21

22
    n = 5
23
    result = bellNumber(n)
24
    print(result)

Output
52
Using Space Optimized DP – O(n^2) Time and O(n) Space
We can use a 1-D array to represent the previous row of the Bell triangle. We initialize dp[0] to 1, since there is only one way to partition an empty set.


To compute the Bell numbers for n > 0, we first set dp[0] = dp[i-1], since the first element in each row is the same as the last element in the previous row. Then, we use the recurrence relation dp[j] = prev + dp[j-1] to compute the Bell number for each partition, where prev is the value of dp[j] in the previous iteration of the inner loop. We update prev to the temporary variable temp before updating dp[j]. Finally, we return dp[0], which is the Bell number for the partition of a set with n elements into non-empty subsets.





1
# Python program to find n'th Bell number using
2
# tabulation
3
​
4
def bell_numbers(n):
5

6
    # Initialize the previous row of the
7
    # Bell triangle with dp[0] = 1
8
    dp = [1] + [0] * n
9
​
10
    for i in range(1, n + 1):
11

12
        # The first element in each row is the same
13
        # as the last element in the previous row
14
        prev = dp[0]
15
        dp[0] = dp[i - 1]
16
        for j in range(1, i + 1):
17

18
            # The Bell number for n is the sum of the
19
            # Bell numbers for all previous partitions
20
            temp = dp[j]
21
            dp[j] = prev + dp[j - 1]
22
            prev = temp
23
​
24
    return dp[0]
25
​
26
n = 5
27
print(bell_numbers(n))

Output
52
"""






