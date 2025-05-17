
"""

Given a string s, the task is to find the minimum number of characters to be inserted to convert it to a palindrome.

Examples:

Input: s = “geeks”
Output: 3
Explanation: “skgeegks” is a palindromic string, which requires 3 insertions.


Input: s= “abcd”
Output: 3
Explanation: “abcdcba” is a palindromic string.


Input: s= “aba”
Output: 0
Explanation: Given string is already a palindrome hence no insertions are required.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(2^n) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n^2) Time and O(n^2) Space
Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n^2) Space
Using Space Optimized DP – O(n ^ 2) Time and O(n) Space
Using Recursion – O(2^n) Time and O(n) Space
The minimum number of insertions in the string str[l…..h] can be given as:


if str[l] is equal to str[h] findMinInsertions(str[l+1…..h-1])
otherwise, min(findMinInsertions(str[l…..h-1]), findMinInsertions(str[l+1…..h])) + 1



1
# Python approach to find Minimum
2
# insertions to form a palindrome
3
​
4
# Recursive function to find
5
# minimum number of insertions
6
def minRecur(s, l, h):
7

8
    # Base case
9
    if l >= h:
10
        return 0
11

12
    # if first and last char are same
13
    # then no need to insert element
14
    if s[l] == s[h]:
15
        return minRecur(s, l + 1, h - 1)
16

17
    # Insert at begining or insert at end
18
    return min(minRecur(s, l + 1, h),
19
               minRecur(s, l, h - 1)) + 1
20
​
21
def findMinInsertions(s):
22
    return minRecur(s, 0, len(s) - 1)
23
​
24
if __name__ == "__main__":
25
    s = "geeks"
26
    print(findMinInsertions(s))

Output
3
Using Top-Down DP (Memoization) – O(n^2) Time and O(n^2) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:

1. Optimal Substructure: The minimum number of insertions required to make the substring str[l…h] a palindrome depends on the optimal solutions of its subproblems. If str[l] is equal to str[h] then we call recursive call on l + 1 and h – 1 other we make two recursive call to get optimal answer.


2. Overlapping Subproblems: When using a recursive approach, we notice that certain subproblems are computed multiple times. To avoid this redundancy, we can use memoization by storing the results of already computed subproblems in a 2D array.


The problem involves changing two parameters: l (starting index) and h (ending index). Hence, we need to create a 2D array of size (n x n) to store the results, where n is the length of the string. By using this 2D array, we can efficiently reuse previously computed results and optimize the solution.




1
# Python approach to find Minimum
2
# insertions to form a palindrome
3
​
4
# Recursive function to find
5
# minimum number of insertions
6
def minRecur(s, l, h, memo):
7

8
    # Base case
9
    if l >= h:
10
        return 0
11
​
12
    # If value is memoized
13
    if memo[l][h] != -1:
14
        return memo[l][h]
15

16
    # if first and last char are same
17
    # then no need to insert element
18
    if s[l] == s[h]:
19
        memo[l][h] = minRecur(s, l + 1, h - 1, memo)
20
        return memo[l][h]
21

22
    # Insert at begining or insert at end
23
    memo[l][h] = min(minRecur(s, l + 1, h, memo),
24
                     minRecur(s, l, h - 1, memo)) + 1
25
    return memo[l][h]
26
​
27
def findMinInsertions(s):
28
    n = len(s)
29
    memo = [[-1] * n for _ in range(n)]
30
    return minRecur(s, 0, n - 1, memo)
31
​
32
if __name__ == "__main__":
33
    s = "geeks"
34
    print(findMinInsertions(s))

Output
3
Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n^2) Space
The iterative approach for finding the minimum number of insertions needed to make a string palindrome follows a similar concept to the recursive solution but builds the solution in a bottom-up manner using a 2D dynamic programming table.


Base Case:


if l == h than dp[l][h] = 0. Where 0 <= l <= n – 1
If the substring has two characters (h == l + 1), we check if they are the same. If they are, dp[l][h] = 0, otherwise, dp[l][h] = 1.
Recursive Case:


If str[l] == str[h], then dp[l][h] = dp[l+1][h-1].
Otherwise, dp[l][h] = min(dp[l+1][h], dp[l][h-1]) + 1.



1
# Python approach to find Minimum
2
# insertions to form a palindrome
3
​
4
# Function to find minimum insertions
5
# to make string palindrome
6
def findMinInsertions(s):
7
    n = len(s)
8

9
    # dp[i][j] will store the minimum number of insertions needed
10
    # to convert str[i..j] into a palindrome
11
    dp = [[0] * n for _ in range(n)]
12
​
13
    # len is the length of the substring
14
    for length in range(2, n + 1):
15
        for l in range(n - length + 1):
16

17
            # ending index of the current substring
18
            h = l + length - 1
19
​
20
            # If the characters at both ends are
21
            # equal, no new insertions needed
22
            if s[l] == s[h]:
23
                dp[l][h] = dp[l + 1][h - 1]
24
            else:
25

26
                # Insert at the beginning or at the end
27
                dp[l][h] = min(dp[l + 1][h], dp[l][h - 1]) + 1
28
​
29
    # The result is in dp[0][n-1] which
30
    # represents the entire string
31
    return dp[0][n - 1]
32
​
33
if __name__ == "__main__":
34
    s = "geeks"
35
    print(findMinInsertions(s))

Output
3
Using Space Optimized DP – O(n ^ 2) Time and O(n) Space
The idea is to reuse the array in such a way that we store the results for the previous row in the same array while iterating through the columns.





1
# Python approach to find Minimum
2
# insertions to form a palindrome
3
​
4
# Function to find minimum insertions
5
# to make string palindrome
6
def findMinInsertions(s):
7
    n = len(s)
8
    dp = [0] * n
9
​
10
    # Iterate over each character from right to left
11
    for l in range(n - 2, -1, -1):
12

13
        # This represents dp[l+1][h-1] from the previous row
14
        prev = 0
15
        for h in range(l + 1, n):
16

17
            # Save current dp[h] before overwriting
18
            temp = dp[h]
19

20
            if s[l] == s[h]:
21

22
                # No new insertion needed if characters match
23
                dp[h] = prev
24
            else:
25

26
                # Take min of two cases + 1
27
                dp[h] = min(dp[h], dp[h - 1]) + 1
28

29
            # Update prev for the next column
30
            prev = temp
31
​
32
    return dp[n - 1]
33
​
34
if __name__ == "__main__":
35
    s = "geeks"
36
    print(findMinInsertions(s))

Output
3
"""










