
"""
Longest Common Subsequence (LCS)
Last Updated : 04 Mar, 2025
Given two strings, s1 and s2, the task is to find the length of the Longest Common Subsequence. If there is no common subsequence, return 0. A subsequence is a string generated from the original string by deleting 0 or more characters, without changing the relative order of the remaining characters.

For example, subsequences of “ABC” are “”, “A”, “B”, “C”, “AB”, “AC”, “BC” and “ABC”. In general, a string of length n has 2n subsequences.

Examples:

Input: s1 = “ABC”, s2 = “ACD”
Output: 2
Explanation: The longest subsequence which is present in both strings is “AC”.


Input: s1 = “AGGTAB”, s2 = “GXTXAYB”
Output: 4
Explanation: The longest common subsequence is “GTAB”.


Input: s1 = “ABC”, s2 = “CBA”
Output: 1
Explanation: There are three longest common subsequences of length 1, “A”, “B” and “C”.


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Using Recursion – O(2 ^ min(m, n)) Time and O(min(m, n)) Space
[Better Approach] Using Memoization – O(m * n) Time and O(m * n) Space
[Expected Approach 1] Using Bottom-Up DP (Tabulation) – O(m * n) Time and O(m * n) Space
[Expected Approach 2] Using Bottom-Up DP (Space-Optimization):
Applications of LCS
Problems based on LCS
[Naive Approach] Using Recursion – O(2 ^ min(m, n)) Time and O(min(m, n)) Space
The idea is to compare the last characters of s1 and s2. While comparing the strings s1 and s2 two cases arise:


Match : Make the recursion call for the remaining strings (strings of lengths m-1 and n-1) and add 1 to result.
Do not Match : Make two recursive calls. First for lengths m-1 and n, and second for m and n-1. Take the maximum of two results.
Base case : If any of the strings become empty, we return 0.


For example, consider the input strings s1 = “ABX” and s2 = “ACX”.

LCS(“ABX”, “ACX”) = 1 + LCS(“AB”, “AC”) [Last Characters Match]


 LCS(“AB”, “AC”) = max( LCS(“A”, “AC”) , LCS(“AB”, “A”) ) [Last Characters Do Not Match]


LCS(“A”, “AC”) = max( LCS(“”, “AC”) , LCS(“A”, “A”) ) = max(0, 1 + LCS(“”, “”)) = 1


LCS(“AB”, “A”) = max( LCS(“A”, “A”) , LCS(“AB”, “”) ) = max( 1 + LCS(“”, “”, 0)) = 1


So overall result is 1 + 1 = 2





1
# A Naive recursive implementation of LCS problem
2
​
3
# Returns length of LCS for s1[0..m-1], s2[0..n-1]
4
def lcsRec(s1, s2, m, n):
5

6
    # Base case: If either string is empty, the length of LCS is 0
7
    if m == 0 or n == 0:
8
        return 0
9
​
10
    # If the last characters of both substrings match
11
    if s1[m - 1] == s2[n - 1]:
12
​
13
        # Include this character in LCS and recur for remaining substrings
14
        return 1 + lcsRec(s1, s2, m - 1, n - 1)
15
​
16
    else:
17
        # If the last characters do not match
18
        # Recur for two cases:
19
        # 1. Exclude the last character of S1
20
        # 2. Exclude the last character of S2
21
        # Take the maximum of these two recursive calls
22
        return max(lcsRec(s1, s2, m, n - 1), lcsRec(s1, s2, m - 1, n))
23
​
24
def lcs(s1,s2):
25
    m = len(s1)
26
    n = len(s2)
27
    return lcsRec(s1,s2,m,n)
28
​
29
if __name__ == "__main__":
30
    s1 = "AGGTAB"
31
    s2 = "GXTXAYB"
32
    print(lcs(s1, s2))

Output
4
[Better Approach] Using Memoization (Top Down DP) – O(m * n) Time and O(m * n) Space
To optimize the recursive solution, we use a 2D memoization table of size (m+1)×(n+1)(m+1) \times (n+1)(m+1)×(n+1), initialized to −1-1−1 to track computed values. Before making recursive calls, we check this table to avoid redundant computations of overlapping subproblems. This prevents repeated calculations, improving efficiency through memoization or tabulation.


Longest-Common-Subsequence
Overlapping Subproblems in Longest Common Subsequence




1
def lcsRec(s1, s2, m, n, memo):
2
    # Base Case
3
    if m == 0 or n == 0:
4
        return 0
5
​
6
    # Already exists in the memo table
7
    if memo[m][n] != -1:
8
        return memo[m][n]
9
​
10
    # Match
11
    if s1[m - 1] == s2[n - 1]:
12
        memo[m][n] = 1 + lcsRec(s1, s2, m - 1, n - 1, memo)
13
        return memo[m][n]
14
​
15
    # Do not match
16
    memo[m][n] = max(lcsRec(s1, s2, m, n - 1, memo),
17
                     lcsRec(s1, s2, m - 1, n, memo))
18
    return memo[m][n]
19
​
20
​
21
def lcs(s1, s2):
22
    m = len(s1)
23
    n = len(s2)
24
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
25
    return lcsRec(s1,s2,m,n,memo)
26

27
if __name__ == "__main__":
28
    s1 = "AGGTAB"
29
    s2 = "GXTXAYB"
30
    print(lcs(s1, s2))

Output
4
[Expected Approach 1] Using Bottom-Up DP (Tabulation) – O(m * n) Time and O(m * n) Space
There are two parameters that change in the recursive solution and these parameters go from 0 to m and 0 to n. So we create a 2D dp array of size (m+1) x (n+1).


We first fill the known entries when m is 0 or n is 0.
Then we fill the remaining entries using the recursive formula.
Say the strings are S1 = “AXTY” and S2 = “AYZX”, Follow below :

Longest-Common-Subsequence.webpLongest-Common-Subsequence.webp



1
def lcs(S1, S2):
2
    m = len(S1)
3
    n = len(S2)
4
​
5
    # Initializing a matrix of size (m+1)*(n+1)
6
    dp = [[0] * (n + 1) for x in range(m + 1)]
7
​
8
    # Building dp[m+1][n+1] in bottom-up fashion
9
    for i in range(1, m + 1):
10
        for j in range(1, n + 1):
11
            if S1[i - 1] == S2[j - 1]:
12
                dp[i][j] = dp[i - 1][j - 1] + 1
13
            else:
14
                dp[i][j] = max(dp[i - 1][j],
15
                               dp[i][j - 1])
16
​
17
    # dp[m][n] contains length of LCS for S1[0..m-1]
18
    # and S2[0..n-1]
19
    return dp[m][n]
20
​
21
​
22
if __name__ == "__main__":
23
    S1 = "AGGTAB"
24
    S2 = "GXTXAYB"
25
    print(lcs(S1, S2))

Output
4
[Expected Approach 2] Using Bottom-Up DP (Space-Optimization):
One important observation in the above simple implementation is, in each iteration of the outer loop we only need values from all columns of the previous row. So there is no need to store all rows in our DP matrix, we can just store two rows at a time and use them. We can further optimize to use only one array.

Please refer this post: A Space Optimized Solution of LCS


Applications of LCS
LCS is used to implement diff utility (find the difference between two data sources). It is also widely used by revision control systems such as Git for multiple changes made to a revision-controlled collection of files.

Problems based on LCS
LCS of 3 Strings
Printing LCS
Longest Palindromic Subsequence
Shortest Common Supersequence
Minimum Insertions and Deletions
Edit Distance
Minimum Insertions for Palindrome
Longest Common Substring
Longest Palindromic Substring
Longest Repeated Subsequence
Count Distinct Subsequences
Regular Expression Matching
Related Links:
Print LCS of two Strings
Dynamic Programming
LCS and Edit Distance Dynamic
Programming Practice Problems

"""




