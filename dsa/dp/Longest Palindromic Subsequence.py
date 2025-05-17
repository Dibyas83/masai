

"""
Given a string s, find the length of the Longest Palindromic Subsequence in it.

Note: The Longest Palindromic Subsequence (LPS) is the maximum-length subsequence of a given string that is also a Palindrome.

LPS
Longest Palindromic Subsequence

Examples:

Input: s = “bbabcbcab”
Output: 7
Explanation: Subsequence “babcbab” is the longest subsequence which is also a palindrome.


Input: s = “abcd”
Output: 1
Explanation: “a”, “b”, “c” and “d” are palindromic and all have a length 1.


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] – Using Recursion – O(2^n) Time and O(1) Space
[Better Approach 1] Using Memoization – O(n^2) Time and O(n^2) Space
[Better Approach 2] Using Tabulation – O(n^2) Time and O(n^2) Space
[Expected Approach] Using Tabulation – O(n^2) Time and O(n) Space
[Alternate Approach] Using Longest Common Subsequence – O(n^2) Time and O(n) Space
[Naive Approach] – Using Recursion – O(2^n) Time and O(1) Space
The idea is to recursively generate all possible subsequences of the given string s and find the longest palindromic subsequence. To do so, create two counters low and high and set them to point to first and last character of string s. Start matching the characters from both the ends of the string. For each case, there are two possibilities:


If characters are matching, increment the value low and decrement the value high by 1 and recur to find the LPS of new substring. And return the value result + 2.
Else make two recursive calls for (low + 1, hi) and (lo, hi-1).  And return the max of 2 calls.



1
# Python program to find the lps
2
​
3
# Returns the length of the longest
4
# palindromic subsequence in seq
5
def lps(s, low, high):
6
​
7
    # Base case
8
    if low > high:
9
        return 0
10
​
11
    # If there is only 1 character
12
    if low == high:
13
        return 1
14
​
15
    # If the first and last characters match
16
    if s[low] == s[high]:
17
        return lps(s, low + 1, high - 1) + 2
18
​
19
    # If the first and last characters do not match
20
    return max(lps(s, low, high - 1), lps(s, low + 1, high))
21
​
22
​
23
def longestPalinSubseq(s):
24
    return lps(s, 0, len(s) - 1)
25
​
26
​
27
if __name__ == "__main__":
28
    s = "bbabcbcab"
29
    print(longestPalinSubseq(s))

Output
7
[Better Approach 1] Using Memoization – O(n^2) Time and O(n^2) Space
In the above approach, lps() function is calculating the same substring multiple times. The idea is to use memoization to store the result of subproblems thus avoiding repetition. To do so, create a 2d array memo[][] of order n*n, where memo[i][j] stores the length of LPS of substring s[i] to s[j]. At each step, check if the substring is already calculated, if so return the stored value else operate as in above approach.





1
# Python program to find the lps
2
​
3
# Returns the length of the longest
4
# palindromic subsequence in seq
5
def lps(s, low, high, memo):
6
​
7
    # Base case
8
    if low > high:
9
        return 0
10
​
11
    # If there is only 1 character
12
    if low == high:
13
        return 1
14
​
15
    # If the value is already calculated
16
    if memo[low][high] != -1:
17
        return memo[low][high]
18
​
19
    # If the first and last characters match
20
    if s[low] == s[high]:
21
        memo[low][high] = lps(s, low + 1, high - 1, memo) + 2
22

23
    else:
24
        # If the first and last characters do not match
25
        memo[low][high] = max(lps(s, low, high - 1, memo),
26
                              lps(s, low + 1, high, memo))
27
    return memo[low][high]
28
​
29
def longestPalinSubseq(s):
30
    n = len(s)
31
    memo = [[-1 for _ in range(n)] for _ in range(n)]
32
    return lps(s, 0, n - 1, memo)
33
​
34
if __name__ == "__main__":
35
    s = "bbabcbcab"
36
    print(longestPalinSubseq(s))

Output
7
[Better Approach 2] Using Tabulation – O(n^2) Time and O(n^2) Space
The above approach can be implemented using tabulation to minimize the auxiliary space required for recursive stack. The idea is create a 2d array dp[][] of order n*n, where element dp[i][j] stores the length of LPS of substring s[i] to s[j]. Start from the smaller substring and try to build answers for longer ones. At each step there are two possibilities:


if s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2
else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
dp[0][n-1] stores the length of the longest palindromic subsequence of string s.





1
# Python program to find the lps
2
​
3
# Function to find the LPS
4
def longestPalinSubseq(s):
5
    n = len(s)
6
​
7
    # Create a DP table
8
    dp = [[0] * n for _ in range(n)]
9
​
10
    # Build the DP table for all the substrings
11
    for i in range(n - 1, -1, -1):
12
        for j in range(i, n):
13
​
14
            # If there is only one character
15
            if i == j:
16
                dp[i][j] = 1
17
                continue
18
​
19
            # If characters at position i and j are the same
20
            if s[i] == s[j]:
21
                if i + 1 == j:
22
                    dp[i][j] = 2
23
                else:
24
                    dp[i][j] = dp[i + 1][j - 1] + 2
25
            else:
26
​
27
                # Otherwise, take the maximum length
28
                # from either excluding i or j
29
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
30
​
31
    # The final answer is stored in dp[0][n-1]
32
    return dp[0][n - 1]
33
​
34
if __name__ == "__main__":
35
    s = "bbabcbcab"
36
    print(longestPalinSubseq(s))

Output
7
[Expected Approach] Using Tabulation – O(n^2) Time and O(n) Space
In the above approach, for calculating the LPS of substrings starting from index i, only the LPS of substrings starting from index i+1 are required. Thus instead of creating 2d array, idea is to create two arrays of size, curr[] and prev[], where curr[j] stores the lps of substring from s[i] to s[j], while prev[j] stores the lps of substring from s[i+1] to s[j]. Else everything will be similar to above approach.





1
# Python program to find the length of the lps
2
​
3
# Function to find the length of the lps
4
def longestPalinSubseq(s):
5
    n = len(s)
6
​
7
    # Create two arrays: one for the current state (dp)
8
    # and one for the previous state (dpPrev)
9
    curr = [0] * n
10
    prev = [0] * n
11
​
12
    # Loop through the string in reverse (starting from the end)
13
    for i in range(n - 1, -1, -1):
14
​
15
        # Initialize the current state of dp
16
        curr[i] = 1
17
​
18
        # Loop through the characters ahead of i
19
        for j in range(i + 1, n):
20
​
21
            # If the characters at i and j are the same
22
            if s[i] == s[j]:
23
​
24
                # Add 2 to the length of the palindrome between them
25
                curr[j] = prev[j - 1] + 2
26
            else:
27
​
28
                # Take the maximum between excluding either i or j
29
                curr[j] = max(prev[j], curr[j - 1])
30
​
31
        # Update previous to the current state of dp
32
        prev = curr[:]
33
​
34
    return curr[n - 1]
35
​
36
if __name__ == "__main__":
37
    s = "bbabcbcab"
38
    print(longestPalinSubseq(s))

Output
7
[Alternate Approach] Using Longest Common Subsequence – O(n^2) Time and O(n) Space
The idea is to reverse the given string s and find the length of the longest common subsequence of original and reversed string.



"""






