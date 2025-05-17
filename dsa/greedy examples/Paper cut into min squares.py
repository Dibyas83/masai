
"""

Paper Cut into Minimum Number of Squares
Last Updated : 19 Apr, 2025
Given a rectangular paper of dimensions a x b. The task is to cut the entire paper into the minimum number of square pieces. We can choose square pieces of any size, but they must be cut without overlapping or leaving any extra space.

Examples:

Input: a = 5, b = 8


Paper-cut-into-minimum-number-of-squares-1
5 squares cut from Paper of size 5 X 8

Output: 5
Explanation: We can cut the paper into 5 squares: 1 square of size 5×5, 1 square of size 3×3, 1 square of size 2×2 and 2 squares of size 1×1.


Input: a = 13, b = 11


Paper-cut-into-minimum-number-of-squares-2
6 squares cut from Paper of size 13 X 11

Output: 6
Explanation: We can cut the paper into 6 squares: 1 square of size 7×7, 1 square of size 6×6, 1 square of size 5×5, 2 squares of size 4×4 and 1 square of size 1×1.


Input: a = 6, b = 7


Paper-cut-into-minimum-number-of-squares-3
5 squares cut from Paper of size 6 X 7

Output: 5
Explanation: We can cut the paper into 5 squares: 1 square of size 4×4, 2 squares of size 3×3 and 2 squares of size 3×3.


Table of Content

[Incorrect Approach 1] Using Greedy Technique
[Incorrect Approach 2] Using Dynamic Programming
[Correct Approach] Using DFS and Dynamic Programming
[Incorrect Approach 1] Using Greedy Technique
At the first sight, it might seem that the problem can be easily solved by cutting the largest square possible from the paper first, followed by cutting the largest square from the remaining paper and so on till we have cut the entire paper. But, this solution is incorrect.


Why Greedy Approach won’t work?


Consider a paper of size 6×7, then if we try to cut the paper greedily we will get 7 squares: 1 square of size 6×6 and 6 squares of size 1×1, whereas the correct solution is: 5. Hence, greedy approach won’t work.


[Incorrect Approach 2] Using Dynamic Programming
Dynamic Programming with vertical or horizonal cuts: Another solution which might seem correct is using Dynamic Programming. We can maintain a dp[][] table such that dp[i][j] = minimum number of squares that can be cut from paper of size i x j. Then for paper of size axb,


We can try to cut it along each row: dp[i][j] = min(dp[i][j], 1 + dp[i – k][j] + dp[k][j]), where k can be in the range [1, i – 1].
We can try to cut it along each column: dp[i][j] = min(dp[i][j], 1 + dp[i][j – k] + dp[i][k]), where k can be in the range [1, j – 1].
Finally, minimum of all cuts will be the answer. But, this solution is also incorrect.


 Why cutting vertically or horizontally with Dynamic Programming Approach won’t work?


This won’t work because we are assuming that a vertical or horizontal cut will always divide the rectangle into two parts. Consider a paper of size 13×11, then if we try to cut the paper using DP approach, we will get 8 squares but the correct answer (as shown in Examples) is 6. Hence, Dynamic Programming won’t work.


[Correct Approach] Using DFS and Dynamic Programming
The idea is to cut the entire paper using DFS in bottom-up manner. In every step, find the lowest-left corner of the paper and try to cut squares of all possible size from that corner. After cutting a square, again find the lowest-left corner of the remaining paper to cut squares of all possible sizes and so on. But if we try all possible cuts from the lowest-left corner of every possible paper size, then it would be quite inefficient. We can optimize it by using Dynamic Programming to store minimum cuts for each possible paper size.


To uniquely identify any paper size, we can maintain a remSq[] array, such that remSq[i] stores the number of remaining squares of size 1×1 in the ith column of the paper. So, for a paper of size 6×7, remSq[] = {6, 6, 6, 6, 6, 6, 6}. Also to find the lowest-left corner, we will find the first index having the maximum remaining squares. So, we can hash the value of remSq[] array to find a unique key for all the possible values of remSq[] array.





1
# Python Program to find minimum number of squares to cut
2
# from a paper of size axb
3
​
4
# function to get the hash key for remSq array
5
def getKey(remSq, b):
6
    base = 1
7
    key = 0
8
    for i in range(b):
9
        key += remSq[i] * base
10
        base = base * (b + 1)
11
    return key
12
​
13
# Recursive function to find the minimum number of square cuts
14
# for a given remSq array
15
def minCutUtil(remSq, a, b, memo):
16
​
17
    # pointers to mark the start and end of range
18
    # with maximum remaining squares
19
    start = 0
20
​
21
    # Check if we have previously calculated the answer
22
    # for the same state
23
    key = getKey(remSq, b)
24
    if key in memo:
25
        return memo[key]
26
​
27
    maxRemSq = 0
28
​
29
    # Find the starting point of min height
30
    for i in range(b):
31
        if remSq[i] > maxRemSq:
32
            maxRemSq = remSq[i]
33
            start = i
34
​
35
    # If max remaining squares = 0, then we have already
36
    # cut the entire paper
37
    if maxRemSq == 0:
38
        return 0
39
​
40
    end = start
41
    newRemSq = remSq[:]
42
​
43
    ans = float('inf')
44
​
45
    # Find the ending point of min height
46
    while end < b:
47
​
48
        # length of edge of square from start till current end
49
        squareEdge = end - start + 1
50
​
51
        # If the current column does not have maximum remaining
52
        # squares or if it's impossible to cut a square of
53
        # size squareEdge, then break out of the loop
54
        if newRemSq[end] != maxRemSq or \
55
           newRemSq[end] - squareEdge < 0:
56
            break
57
​
58
        # If we can cut a square of size squareEdge,
59
        # update the remainingSquares
60
        for i in range(start, end + 1):
61
            newRemSq[i] = maxRemSq - squareEdge
62
​
63
        # Find the solution for new remainingSquares
64
        ans = min(ans, 1 + minCutUtil(newRemSq, a, b, memo))
65
        end += 1
66
​
67
    memo[key] = ans
68
    return ans
69
​
70
# Function to find the minimum number of squares we can cut
71
# using paper of size a X b
72
def minCut(a, b):
73
​
74
    # if the given rectangle is a square
75
    if a == b:
76
        return 1
77
​
78
    # Initialize remaining squares = a for all the b columns
79
    remSq = [a] * b
80
​
81
    memo = {}
82
    return minCutUtil(remSq, a, b, memo)
83
​
84
if __name__ == "__main__":
85
​
86
    # Sample Input
87
    a = 13
88
    b = 11
89
​
90
    # Function call to get minimum number
91
    # of squares for axb
92
    print(minCut(a, b))

Output
6
Time Complexity: O(a^b), for each of b columns, we can have a squares.
Auxiliary Space: O(a^b), due to memoization storing each unique state.
"""








