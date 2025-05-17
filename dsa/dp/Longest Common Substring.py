
"""

Given two strings ‘s1‘ and ‘s2‘, find the length of the longest common substring.

Example:

Input: s1 = “GeeksforGeeks”, s2 = “GeeksQuiz”
Output : 5
Explanation:
The longest common substring is “Geeks” and is of length 5.


Input: s1 = “abcdxyz”, s2 = “xyzabcd”
Output : 4
Explanation:
The longest common substring is “abcd” and is of length 4.


Input: s1 = “abc”, s2 = “”
Output : 0.


Try it on GfG Practice
redirect icon
Approach:

We have discussed a Dynamic programming based solution for the Longest common substring. The auxiliary space used by the solution is O(m*n), where m and n are lengths of strings s1 and s2. The space used by the solution can be reduced to O(2*n).

Suppose we are at position dp[i][j]. Now if s1[i-1] == s2[j-1], then we add the value of dp[i-1][j-1] to our result. That is we add value from previous row and value for all other rows below the previous row are never used. So, at a time we are using only two consecutive rows. This observation can be used to reduce the space required to find length of longest common substring.
Instead of creating a matrix of size m*n, we create a matrix of size 2*n. A variable currRow is used to represent that either row 0 or row 1 of this matrix is currently used to find length. Initially row 0 is used as current row for the case when length of string s1 is zero. At the end of each iteration, current row is made previous row and previous row is made new current row.





1
# Python program to find
2
# Longest Common Substring
3
​
4
# Function to find longest common substring.
5
def longestCommonSubstr(s1, s2):
6

7
    # Find length of both strings.
8
    m = len(s1)
9
    n = len(s2)
10
​
11
    # Variable to store length of longest
12
    # common substring.
13
    result = 0
14
​
15
    # Matrix to store result of two
16
    # consecutive rows at a time.
17
    dp = [[0] * (n + 1) for _ in range(2)]
18
​
19
    # Variable to represent which row of
20
    # matrix is current row.
21
    currRow = 0
22
​
23
    # For a particular value of i and j,
24
    # dp[currRow][j] stores length of longest
25
    # common substring in string X[0..i] and Y[0..j].
26
    for i in range(m + 1):
27
        for j in range(n + 1):
28
            if i == 0 or j == 0:
29
                dp[currRow][j] = 0
30
            elif s1[i - 1] == s2[j - 1]:
31
                dp[currRow][j] = dp[1 - currRow][j - 1] + 1
32
                result = max(result, dp[currRow][j])
33
            else:
34
                dp[currRow][j] = 0
35
​
36
        # Make current row as previous row and previous
37
        # row as new current row.
38
        currRow = 1 - currRow
39
​
40
    return result
41
​
42
if __name__ == "__main__":
43
    s1 = "GeeksforGeeks"
44
    s2 = "GeeksQuiz"
45
​
46
    print(longestCommonSubstr(s1, s2))

Output
5
Time Complexity: O(m*n), where m is the length of string s1 and n is the length of string s2
Auxiliary Space: O(2*n), since we only need to keep track of two rows at any given time
"""







