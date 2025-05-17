
"""
Maximize the number of segments of length x, y and z
Last Updated : 05 Dec, 2024
Given a rod of length n, the task is to cut the rod in such a way that the total number of segments of length x, y, and z is maximized. The segments can only be of length x, y, and z.
Note: If no segment can be cut then return 0.

Examples:

Input: n = 4, x = 2, y = 1, z = 1
Output: 4
Explanation: Total length is 4, and the cut lengths are 2, 1 and 1.  We can make maximum 4 segments each of length 1.


Input: n = 5, x = 5, y = 3, z = 2
Output: 2
Explanation: Here total length is 5, and the cut lengths are 5, 3 and 2. We can make two segments of lengths 3 and 2.


Input: n = 7, x = 8, y = 9, z = 10
Output: 0
Explanation: Here the total length is 7, and the cut lengths are 8, 9, and 10. We cannot cut the segment into lengths that fully utilize the segment, so the output is 0.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(3^n) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
Using Recursion – O(3^n) Time and O(n) Space
For the recursive approach, the function explores all possible ways to cut the rod into segments of given lengths. At each step, it considers three options:

Reduce the length by the first segment length (x).
Reduce the length by the second segment length (y).
Reduce the length by the third segment length (z).
The recurrence relation for the problem is as follows:


if n < 0
maxCutHelper(n, x, y, z) = -1,


else
maxCutHelper(n, x, y, z) =  1 + max(maxCutHelper(n – x, x, y, z), maxCutHelper(n – y, x, y, z), maxCutHelper(n – z, x, y, z))


Base Cases:


If the rod length is zero (n = 0), return 0 (no more cuts can be made).
If the rod length becomes negative (n < 0), return -1 (invalid result).



1
# Python implementation to find max cut segments
2
# using Recursion
3
​
4
# Helper function to maximize the number
5
# of cuts using recursion
6
def maxCutHelper(n, x, y, z):
7
​
8
    # Base case: If the length is zero,
9
    # return zero cuts
10
    if n == 0:
11
        return 0
12
​
13
    # Base case: If the length becomes negative,
14
    # return an invalid result
15
    if n < 0:
16
        return -1
17
​
18
    # Recursive step: Try all three segment
19
    # lengths and choose the maximum result
20
    cut1 = maxCutHelper(n - x, x, y, z)
21
    cut2 = maxCutHelper(n - y, x, y, z)
22
    cut3 = maxCutHelper(n - z, x, y, z)
23
​
24
    # Get the maximum number of cuts among
25
    # the 3 options
26
    maxCut = max(cut1, cut2, cut3)
27
​
28
    # If no valid cut found, return negative
29
    # value indicating no valid cuts
30
    if maxCut == -1:
31
        return -1
32
​
33
    return maxCut + 1
34
​
35
# Main function to start the cutting process
36
def maximizeTheCuts(n, x, y, z):
37

38
    res = maxCutHelper(n, x, y, z)
39
​
40
    # No valid cuts found
41
    if res == -1:
42
        return 0
43
​
44
    return res
45
​
46
if __name__ == "__main__":
47
​
48
    n = 11
49
    x = 2
50
    y = 3
51
    z = 5
52
​
53
    print(maximizeTheCuts(n, x, y, z))

Output
5
Using Top-Down DP (Memoization) – O(n) Time and O(n) Space
The recursive approach is optimized using memoization, storing previously computed results in a memo array to avoid redundant computations. The two key properties of dynamic programming are utilized:

1. Optimal Substructure: The solution for maximizing cuts can be derived from smaller subproblems:


If the rod length n is zero, the number of cuts is zero.
If the rod length becomes negative, the result is invalid (-1).
Otherwise, for each segment length (x, y, z), the solution is the maximum result of reducing the rod by that segment length and recursively solving the subproblem.
2. Overlapping Subproblems: The function repeatedly computes results for the same rod length (n) with the same segment lengths. Using a memoization array memo, where memo[n] stores the result for rod length n, avoids redundant calculations.


Initialize a memoization array memo of size n + 1 with -1.
In the recursive function, check if the result for the current rod length (n) is already computed (memo[n] != -1). If so, return the stored result.
Otherwise, compute the result using the recurrence relation, and store it in memo[n].



1
# Python implementation to find max cut segments
2
# using Recursion and Memoization
3
​
4
# Helper function to maximize the number
5
# of cuts using recursion and memoization
6
def maxCutHelper(n, x, y, z, memo):
7
​
8
    # Base case: If the length is zero,
9
    # return zero cuts
10
    if n == 0:
11
        return 0
12
​
13
    # Base case: If the length becomes negative,
14
    # return an invalid result
15
    if n < 0:
16
        return -1
17
​
18
    # If the result is already computed,
19
    # return it from the memo dictionary
20
    if n in memo:
21
        return memo[n]
22
​
23
    # Recursive step: Try all three segment
24
    # lengths and choose the maximum result
25
    cut1 = maxCutHelper(n - x, x, y, z, memo)
26
    cut2 = maxCutHelper(n - y, x, y, z, memo)
27
    cut3 = maxCutHelper(n - z, x, y, z, memo)
28
​
29
    # Get the maximum number of cuts among
30
    # the 3 options
31
    maxCut = max(cut1, cut2, cut3)
32
​
33
    # If no valid cut found, return negative
34
    # value indicating no valid cuts
35
    if maxCut == -1:
36
        memo[n] = -1
37
        return -1
38
​
39
    memo[n] = maxCut + 1
40
    return memo[n]
41
​
42
# Main function to start the cutting process
43
def maximizeTheCuts(n, x, y, z):
44

45
    # Create a memoization dictionary
46
    memo = {}
47
​
48
    res = maxCutHelper(n, x, y, z, memo)
49
​
50
    # No valid cuts found
51
    if res == -1:
52
        return 0
53
​
54
    return res
55
​
56
if __name__ == "__main__":
57
​
58
    n = 11
59
    x = 2
60
    y = 3
61
    z = 5
62
​
63
    print(maximizeTheCuts(n, x, y, z))

Output
5
Using Bottom-Up DP (Tabulation) – O(n) Time and O(n) Space
The approach is similar to the previous one, but instead of breaking down the problem recursively, we iteratively build up the solution by calculating in a bottom-up manner. So, we will create a 1D array dp of size (n + 1) of type integer. The state dp[i] will store the maximum number of cuts possible for a rod of length i.

The dynamic programming relation is as follows:


If the current rod length i is less than the segment length x: dp[i] = dp[i]
Otherwise, we update dp[i] as: dp[i] = max(dp[i], dp[i – k] + 1), where k can be x, y, or z.
This means that if the current rod length is smaller than the segment length, no cut is possible for this length, and we keep the previous value. Otherwise, we check if adding a segment of length k results in a greater number of cuts and update the value of dp[i] accordingly. Finally, if no valid cuts are possible for the rod of length n, we return 0. Otherwise, the value at dp[n] will give the maximum number of cuts.




1
# Python implementation to find max cut segments
2
# using Tabulation
3
​
4
# Main function to start the cutting process
5
def maximizeTheCuts(n, x, y, z):
6
​
7
    # Create a table to store results of subproblems
8
    dp = [0] * (n + 1)
9
​
10
    for i in range(1, n + 1):
11
​
12
        # Check if the current length is at least x
13
        # If so, check if the previous result
14
        # (dp[i - x]) is valid (not -1)
15
        # Update dp[i] by considering this cut
16
        if i >= x and dp[i - x] != -1:
17
            dp[i] = max(dp[i], dp[i - x] + 1)
18
​
19
        # Similarly, check for the other two possible
20
        # cuts (y and z)
21
        if i >= y and dp[i - y] != -1:
22
            dp[i] = max(dp[i], dp[i - y] + 1)
23
​
24
        if i >= z and dp[i - z] != -1:
25
            dp[i] = max(dp[i], dp[i - z] + 1)
26
​
27
        # If no valid cut was found for length i,
28
        if dp[i] == 0:
29
            dp[i] = -1
30
​
31
    # If no valid cuts are found for the full
32
    # length n, return 0
33
    if dp[n] == -1:
34
        return 0
35
​
36
    # Return the maximum number of cuts for
37
    # the rod of length n
38
    return dp[n]
39
​
40
if __name__ == "__main__":
41
​
42
    n = 11
43
    x = 2
44
    y = 3
45
    z = 5
46
​
47
    print(maximizeTheCuts(n, x, y, z))

Output
5

"""






