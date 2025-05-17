
"""
Given 3 strings say s1, s2 and s3. The task is to find the longest common sub-sequence in all three given sequences.

Examples:

Input:  s1 = “geeks” , s2 = “geeksfor”, s3 = “geeksforgeeks”
Output : 5
Explanation: Longest common subsequence is “geeks” i.e., length = 5

Input: s1= “abcd1e2” , s2= “bc12ea” , s3= “bd1ea”
Output: 3
Explanation: Longest common subsequence is “b1e” i.e. length = 3.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(3^(n1+n2+n3)) Time and O(min(n1, n2, n3)) Space
Using Top-Down DP (Memoization) – O(n1*n2*n3) Time and O(n1*n2*n3) Space
Using Bottom-Up DP (Tabulation)– O(n1*n2*n3) Time and O(n1*n2*n3) Space
Using Recursion – O(3^(n1+n2+n3)) Time and O(min(n1, n2, n3)) Space
This problem is simply an extension of LCS.
Let the input sequences be s1[0..n1-1], s2[0..n2-1], and s3[0..n3-1], with lengths n1, n2, and n3, respectively. Let lis(s1[0..n1-1], s2[0..n2-1], s3[0..n3-1]) represent the length of the longest common subsequence (LCS) among these three sequences, s1, s2, and s3.

The idea is to break the problem into smaller subproblems and then combine the solutions to solve the original problem using recursion. We compare the last characters of the three strings, and there are two cases to consider:

When the last characters match: In this case, we reduce the problem by recursively calling the function for smaller substrings, removing the last character from each string.
When the last characters do not match: Here, we need to consider the maximum result from three different cases, each time excluding one character from one of the strings.
Base Cases: If any of the strings s1, s2, or s3 has a length of 0, the Longest Common Subsequence (LCS) is 0.
Recurrence Relation:


If the last characters of s1, s2, and s3 are the same: These characters contribute to the LCS. Therefore, we add 1 to the LCS and call the recursive function with the previous characters of all three strings:


LCSof3(n1, n2, n3) = 1 + LCSof3(n1-1, n2-1, n3-1)
If the last characters do not match, we consider three possibilities:


Exclude the last character of s1 and compute the LCS for s1[0..n1-2], s2, and s3
LCSof3(n1, n2, n3) = LCSof3(n1-1, n2, n3)
Exclude the last character of s2 and compute the LCS for s1, s2[0..n2-2], and s3
LCSof3(n1, n2, n3) = LCSof3(n1, n2-1, n3)
Exclude the last character of s3 and compute the LCS for s1, s2, and s3[0..n3-2]
LCSof3(n1, n2, n3) = LCSof3(n1, n2, n3-1)
Thus, the final LCS is the maximum result obtained from these three cases:


LCSof3(n1, n2, n3) = max(LCSof3(n1-1, n2 , n3), LCSof3(n1, n2-1, n3), LCSof3(n1, n2, n3-1))



1
# Python program to find the Longest Common Subsequence of
2
# three string using recursion
3
​
4
​
5
def findLCSOf3(s1, s2, s3, n1, n2, n3):
6
​
7
    # Base case: If any of the strings is empty
8
    if n1 == 0 or n2 == 0 or n3 == 0:
9
        return 0
10
​
11
    # If last characters of s1, s2, and s3 are the same
12
    if s1[n1 - 1] == s2[n2 - 1] == s3[n3 - 1]:
13
        return 1 + findLCSOf3(s1, s2, s3, n1 - 1, n2 - 1, n3 - 1)
14
​
15
    # If last characters are not the same, calculate
16
    # LCS by excluding one string at a time
17
    return max(
18
        findLCSOf3(s1, s2, s3, n1 - 1, n2, n3),
19
        findLCSOf3(s1, s2, s3, n1, n2 - 1, n3),
20
        findLCSOf3(s1, s2, s3, n1, n2, n3 - 1)
21
    )
22
​
23
​
24
def lcsOf3(s1, s2, s3):
25
    n1 = len(s1)
26
    n2 = len(s2)
27
    n3 = len(s3)
28
    return findLCSOf3(s1, s2, s3, n1, n2, n3)
29
​
30
​
31
if __name__ == "__main__":
32
    s1 = "AGGT12"
33
    s2 = "12TXAYB"
34
    s3 = "12XBA"
35
    res = lcsOf3(s1, s2, s3)
36
    print(res)

Output
2
Using Top-Down DP (Memoization) – O(n1*n2*n3) Time and O(n1*n2*n3) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming.

1. Optimal Substructure:


The solution to the Longest Common Subsequence (LCS) of three strings can be derived from the optimal solutions of smaller subproblems. Specifically, for given strings s1, s2, and s3 with lengths n1, n2, and n3, we can express the recursive relation as follows:


 If the last characters of s1, s2, and s3 are the same:
 LCSof3(n1, n2, n3) = 1+LCSof3(n1-1, n2-1, n3-1)
 If the last characters do not match, we consider three possibilities. the final LCS is the maximum result obtained from these three cases:
 LCSof3(n1, n2, n3)=max(LCSof3(n1-1, n2, n3),LCSof3(n1, n2-1, n3), LCSof3(n1, n2, n3-1))
2. Overlapping Subproblems:


When using a recursive approach to solve the Longest Common Subsequence (LCS) problem for three strings, we observe that many subproblems are computed multiple times. For example, when calculating LCSof3(s1, s2, s3) for strings s1, s2, and s3 with lengths n1, n2, and n3, we may end up recomputing the LCS for the same combinations of string prefixes multiple times.
The recursive solution involves changing three parameters: the current indices of the three strings (n1, n2, n3). We need to track these parameters, so we create a 3D array of size (n1+1) x (n2+1) x (n3+1), where n1, n2, and n3 represent the lengths of strings s1, s2, and s3. This array is used to store the results of subproblems for each combination of indices in the three strings.
We initialize the 3D array with -1 to indicate that no subproblems have been computed yet.
We check if the value at memo[n1][n2][n3] is -1. If it is, we proceed to compute the result. otherwise, we return the stored result.



1
# Python program to find the Longest Common Subsequence of
2
# three string using memoization
3
​
4
def findLCSOf3(s1, s2, s3, n1, n2, n3, memo):
5

6
    # Base case: If any of the strings is empty
7
    if n1 == 0 or n2 == 0 or n3 == 0:
8
        return 0
9
​
10
    # If the result is already computed,
11
    # return it from the memo table
12
    if memo[n1][n2][n3] != -1:
13
        return memo[n1][n2][n3]
14
​
15
    # If the last characters of s1, s2, and s3 are the same
16
    if s1[n1 - 1] == s2[n2 - 1] and s2[n2 - 1] == s3[n3 - 1]:
17
        memo[n1][n2][n3] = 1 + \
18
            findLCSOf3(s1, s2, s3, n1 - 1, n2 - 1, n3 - 1, memo)
19
        return memo[n1][n2][n3]
20
​
21
    # If last characters do not match,
22
    # calculate LCS by excluding one string at a time
23
    memo[n1][n2][n3] = max(
24
        findLCSOf3(s1, s2, s3, n1 - 1, n2, n3, memo),
25
        findLCSOf3(s1, s2, s3, n1, n2 - 1, n3, memo),
26
        findLCSOf3(s1, s2, s3, n1, n2, n3 - 1, memo)
27
    )
28
    return memo[n1][n2][n3]
29
​
30
​
31
def lcsOf3(s1, s2, s3):
32
    n1, n2, n3 = len(s1), len(s2), len(s3)
33
​
34
    # Initialize the memoization table with -1
35
    memo = [[[-1 for _ in range(n3 + 1)]
36
             for _ in range(n2 + 1)] for _ in range(n1 + 1)]
37
​
38
    # Call the recursive function
39
    return findLCSOf3(s1, s2, s3, n1, n2, n3, memo)
40
​
41
​
42

43
s1 = "AGGT12"
44
s2 = "12TXAYB"
45
s3 = "12XBA"
46
res = lcsOf3(s1, s2, s3);
47
print(res)

Output
2
Using Bottom-Up DP (Tabulation)– O(n1*n2*n3) Time and O(n1*n2*n3) Space
The approach is similar to the previous one. just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner.

We create a 3D DP array of size (n1 + 1) * (n2 + 1) * (n3 + 1) where each state dp[i][j][k] represents the length of the Longest Common Subsequence (LCS) of the first i characters of string s1, the first j characters of string s2, and the first k characters of string s3.


The dynamic programming relation for LCS of three strings is as follows:


Base case: If any of the strings is empty (i == 0, j == 0, or k == 0), the LCS is 0:
if i == 0 or j == 0 or k == 0 dp[i][j][k] = 0


Recursive relation:
If the last characters of s1, s2, and s3 are the same, they contribute to the LCS. We add 1 to the result of the subproblem that excludes the last character from each string:
if s1[i-1] == s2[j-1] && s2[j-1] == s3[k-1]  dp[i][j][k] = dp[i-1][j-1][k-1] + 1


If the last characters do not match, we need to check three cases:


Exclude the last character of s1: In this case, we compute the LCS by considering the first i-1 characters of s1, the first j characters of s2, and the first k characters of s3:
dp[i][j][k] = dp[i-1][j][k]
Exclude the last character of s2: In this case, we compute the LCS by considering the first i characters of s1, the first j-1 characters of s2, and the first k characters of s3:
dp[i][j][k] = dp[i][j-1][k]
Exclude the last character of s3: In this case, we compute the LCS by considering the first i characters of s1, the first j characters of s2, and the first k-1 characters of s3:
dp[i][j][k] = dp[i][j][k-1]
The final result, dp[n1][n2][n3], gives the length of the LCS of the three strings.





1
# Python program to find the Longest Common Subsequence of
2
# three string using tabulation
3
​
4
def lcsOf3(s1, s2, s3):
5
    n1 = len(s1)
6
    n2 = len(s2)
7
    n3 = len(s3)
8
​
9
    # Create a 3D array (dp) to store
10
    # the LCS lengths for each combination of substrings
11
    dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)]
12
          for _ in range(n1 + 1)]
13
​
14
    # Build dp[n1+1][n2+1][n3+1] in bottom-up fashion
15
    # dp[i][j][k] contains length of LCS of s1[0..i-1],
16
    # s2[0..j-1], and s3[0..k-1]
17
    for i in range(n1 + 1):
18
        for j in range(n2 + 1):
19
            for k in range(n3 + 1):
20
                if i == 0 or j == 0 or k == 0:
21
                    dp[i][j][k] = 0
22
                elif s1[i - 1] == s2[j - 1] and s1[i - 1] == s3[k - 1]:
23
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + \
24
                        1
25
                else:
26

27
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i]
28
                                      [j - 1][k], dp[i][j][k - 1])
29
​
30
    # dp[n1][n2][n3] contains length of LCS for
31
    # s1[0..n1-1], s2[0..n2-1], and s3[0..n3-1]
32
    return dp[n1][n2][n3]
33
​
34
​
35
if __name__ == "__main__":
36
    s1 = "AGGT12"
37
    s2 = "12TXAYB"
38
    s3 = "12XBA"
39
    res = lcsOf3(s1, s2, s3)
40
    print(res)

Output
2

"""

