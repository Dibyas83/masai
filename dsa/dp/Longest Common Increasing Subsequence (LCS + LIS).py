
"""
Given two arrays, a[] and b[], find the length of the longest common increasing subsequence(LCIS). LCIS refers to a subsequence that is present in both arrays and strictly increases.
Prerequisites: LCS, LIS.

Examples:

Input: a[] = [3, 4, 9, 1], b[] = [5, 3, 8, 9, 10, 2, 1]
Output: 2
Explanation: The longest increasing subsequence that is common is {3, 9} and its length is 2.


Input: a[] = [1, 1, 4, 3], b[] = [1, 1, 3, 4]
Output: 2
Explanation: There are two common subsequences {1, 4} and {1, 3} both of length 2.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(2^(m+n)) Time and O(m+n) Space
Using Top-Down DP (Memoization) – O(m*n*m) Time and O(m*n*m) Space
Using Bottom-Up DP (Tabulation) – O(m*n) Time and O(n) Space
Using Recursion – O(2^(m+n)) Time and O(m+n) Space
We can identify a recursive pattern in this problem. There are three state variables: i index for array a[], j index for array b[] and prevIndex index of the previous element that we included from array a[].

We consider two cases for recursion:

If the element satisfies the following conditions, we include it in the subsequence and move on to the next element in both a[] and b[]
prevIndex is equal to -1 or a[prevIndex] is greater than a[i].
a[i] is equal to b[j].
We iterate to next element in either a or b.
Recurrence relation:

if (a[i] == b[j] and (prevIndex == -1 or a[i] < a[prevIndex]))


LCIS(i, j, prevIndex) = 1 + LCIS(i-1, j-1, i)
otherwise


LCIS(i, j, prevIndex) = max(LCIS(i-1, j, prevIndex), LCIS(i, j-1, prevIndex))​
Base Case: If either array is completely traversed i.e. if (i < 0 || j < 0) return 0





1
# Python Program to find length of the
2
# Longest Common Increasing Subsequence (LCIS)
3
​
4
def findLCIS(i, j, prevIndex, a, b):
5

6
        # Base case: If either array is fully traversed
7
        if i < 0 or j < 0:
8
            return 0
9

10
        include = 0
11
        exclude = 0
12

13
        # If current elements are equal and
14
        # satisfy the increasing condition
15
        if a[i] == b[j] and (prevIndex == -1 or a[i] < a[prevIndex]):
16

17
            # Include the current element
18
            include = 1 + findLCIS(i - 1, j - 1, i, a, b)
19

20
        # Explore skipping an element from either array
21
        exclude = max(findLCIS(i - 1, j, prevIndex, a, b),
22
                      findLCIS(i, j - 1, prevIndex, a, b))
23

24
        # Return the maximum of including or
25
        #excluding the current element
26
        return max(include, exclude)
27
​
28
def LCIS(a, b):
29

30
        # Start recursion from the last indices with no previous element
31
        return findLCIS(len(a) - 1, len(b) - 1, -1, a, b)
32
​
33
if __name__ == "__main__":
34

35
    a = [3, 4, 9, 1]
36
    b = [5, 3, 8, 9, 10, 2, 1]
37
​
38
    print(LCIS(a, b))

Output
2
Using Top-Down DP (Memoization) – O(m*n*m) Time and O(m*n*m) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:

1. Optimal Substructure: Maximum subsequence length for a given i, j and prevIndex , i.e., LCIS(i, j, prevIndex), depends on the optimal solutions of the subproblems LCIS(i-1, j, prevIndex), LCIS(i, j-1, prevIndex)  and LCIS(i-1, j-1, i). By choosing the maximum of these optimal substructures, we can efficiently calculate the maximum subsequence length.


2. Overlapping Subproblems: While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times.


There are three parameter that change in the recursive solution: i going from 0 to m-1, j going from 0 to n-1 and prevIndex going from 0 to m-1. So we create a 3D array of size m*n*m for memoization.
We initialize this array as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# A Python program to find length of the Longest Common
2
# Increasing Subsequence (LCIS) using memoization
3
def findLCIS(i, j, prev_index, a, b, memo):
4

5
    # Base case: If either array is fully traversed
6
    if i < 0 or j < 0:
7
        return 0
8
​
9
    # If the result has already been computed, return it
10
    if memo[i][j][prev_index + 1] != -1:
11
        return memo[i][j][prev_index + 1]
12
​
13
    include = 0
14
    exclude = 0
15
​
16
    # If the current elements match and satisfy the increasing condition
17
    if a[i] == b[j] and (prev_index == -1 or a[i] < a[prev_index]):
18

19
         # Include the current element
20
        include = 1 + findLCIS(i - 1, j - 1, i, a, b, memo)
21
​
22
    # Explore excluding the current element from either array
23
    exclude = max(findLCIS(i - 1, j, prev_index, a, b, memo),
24
                  findLCIS(i, j - 1, prev_index, a, b, memo))
25
​
26
    # Store the result in the memo table and return it
27
    memo[i][j][prev_index + 1] = max(include, exclude)
28
    return memo[i][j][prev_index + 1]
29
​
30
def LCIS(a, b):
31
    m = len(a)
32
    n = len(b)
33

34
    # Initialize the memoization table with -1
35
    # (indicating uncomputed states)
36
    memo = [[[ -1 for _ in range(m + 1)] for _ in range(n)] for _ in range(m)]
37
​
38
    # Start recursion from the last indices with
39
    # no previous element
40
    return findLCIS(m - 1, n - 1, -1, a, b, memo)
41
​
42
a = [3, 4, 9, 1 ]
43
b = [5, 3, 8, 9, 10, 2, 1]
44
print(LCIS(a, b))

Output
2
Using Bottom-Up DP (Tabulation) – O(m*n) Time and O(n) Space
The idea is to iterate of every index j of b[] for every index i in a[]. We use a linear array dp of length n intialized with zero to keep track of the LCIS ending on jth index of b[].  We also use a variable currentLength to store the length of the LCIS for the current element of a[]. This variable helps to keep track of the LCIS ending at the previous index of a[] but not including the current element in a[].


If a[i] is equal to b[j], then found a potential element of the LCIS that ends at b[j]. At this point, we can update dp[j] to be the maximum of its current value and currentLength + 1. This is because currentLength keeps track of the longest LCIS that ends at a previous index in a[].
If a[i] > b[j], it means that b[j] can be part of an increasing subsequence that ends with a[i]. Hence, we need to update the currentLength to be the maximum value between currentLength and dp[j]. This ensures that currentLength holds the length of the longest subsequence ending at any previous element b[k] (where k < j).
After iterating through all elements of a[] and b[], the value of dp[] will hold the lengths of LCIS ending at each index of b[]. The maximum value in the dp[] array will be the length of the Longest Common Increasing Subsequence.




1
# Java Program to find length of the Longest Common
2
# Increasing Subsequence (LCIS) using tabulation
3
def LCIS(a, b):
4
    m = len(a)
5
    n = len(b)
6
​
7
    # Initialize a DP array to store lengths
8
    # of LCIS ending at each index of b
9
    dp = [0] * n
10
​
11
    # Iterate through each element in a
12
    for i in range(m):
13
        currentLength = 0
14
​
15
        # Iterate through each element in b
16
        for j in range(n):
17

18
            # If a[i] == b[j], we may have found a
19
            # new LCIS ending at j in b
20
            if a[i] == b[j]:
21
                dp[j] = max(dp[j], currentLength + 1)
22

23
            # If a[i] > b[j], it means b[j] could be
24
            # part of an increasing subsequence
25
            elif a[i] > b[j]:
26
                currentLength = max(currentLength, dp[j])
27
​
28
    # The maximum value in dp[] is the length of the
29
    # longest common increasing subsequence
30
    return max(dp)
31
​
32
​
33
a = [3, 4, 9, 1 ]
34
b = [5, 3, 8, 9, 10, 2, 1]
35
print(LCIS(a, b))

Output
2


"""











