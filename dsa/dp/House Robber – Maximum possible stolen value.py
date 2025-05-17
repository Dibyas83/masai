
"""
House Robber – Maximum possible stolen value
Last Updated : 01 Oct, 2024
There are n houses built in a line, each of which contains some money in it. A robber wants to steal money from these houses, but he can’t steal from two adjacent houses. The task is to find the maximum amount of money which can be stolen.

Examples:

Input: hval[] = {6, 7, 1, 3, 8, 2, 4}
Output: 19
Explanation: The thief will steal from house 1, 3, 5 and 7, total money = 6 + 1 + 8 + 4 = 19.

Input: hval[] = {5, 3, 4, 11, 2}
Output: 16
Explanation: Thief will steal from house 1 and 4, total money = 5 + 11 = 16.


Try it on GfG Practice
redirect icon
Given an array, the solution is to find the maximum sum subsequence where no two selected elements are adjacent.

Table of Content

[Naive Approach] Using Recursion- O(2 ^ n) Time and O(n) Space
[Better Approach] Using Memoization – O(n) Time and O(n) Space
[Expected Approach 1] Using Tabulation – O(n) Time and O(n) Space
[Expected Approach 2] Using Tabulation (Space-Optimized) – O(n) Time and O(1) Space
[Naive Approach] Using Recursion- O(2n) Time and O(n) Space
The idea is to explore all the possibilities for each house using Recursion. We can start from the last house and for each house, we have two choices:


Rob the current house and skip the house just before it.
Skip the current house and move to the next house.
So, the recurrence relation will be:


maxLootRec(n) = max(hval[n – 1] + maxLootRec(n – 2), maxLootRec(n – 1)),
where maxLootRec(n) returns the maximum amount of money which can be stolen if n houses are left.





1
# Python Program to solve House Robber Problem using Recursion
2
​
3
# Calculate the maximum stolen value recursively
4
def maxLootRec(hval, n):
5

6
    # If no houses are left, return 0.
7
    if n <= 0:
8
        return 0
9

10
    # If only 1 house is left, rob it.
11
    if n == 1:
12
        return hval[0]
13
​
14
    # Two Choices: Rob the nth house and do not rob the nth house
15
    pick = hval[n - 1] + maxLootRec(hval, n - 2)
16
    notPick = maxLootRec(hval, n - 1)
17
​
18
    # Return the max of two choices
19
    return max(pick, notPick)
20
​
21
# Function to calculate the maximum stolen value
22
def maxLoot(hval):
23
    n = len(hval)
24

25
    # Call the recursive function for n houses
26
    return maxLootRec(hval, n)
27
​
28
if __name__ == "__main__":
29
    hval = [6, 7, 1, 3, 8, 2, 4]
30
    print(maxLoot(hval))

Output
19
Time Complexity: O(2n). Every house has 2 choices to pick and not pick.
Auxiliary Space: O(n). For recursion stack space

[Better Approach] Using Memoization – O(n) Time and O(n) Space
The above solution has optimal substructure and overlapping subproblems. See the below recursion tree, maxLootRec(2) is being evaluated twice.


Recursion-Tree-for-House-Robber
Recursion Tree for House Robber

We can optimize this solution using a memo array of size (n + 1), such that memo[i] represents the maximum value that can be collected from first i houses. Please note that there is only one parameter that changes in recursion and the range of this parameter is from 0 to n.





1
# Python Program to solve House Robber Problem using Memoization
2
​
3
def maxLootRec(hval, n, memo):
4
    if n <= 0:
5
        return 0
6
    if n == 1:
7
        return hval[0]
8
​
9
    # Check if the result is already computed
10
    if memo[n] != -1:
11
        return memo[n]
12
​
13
    pick = hval[n - 1] + maxLootRec(hval, n - 2, memo)
14
    notPick = maxLootRec(hval, n - 1, memo)
15
​
16
    # Store the max of two choices in the memo array and return it
17
    memo[n] = max(pick, notPick)
18
    return memo[n]
19
​
20
def maxLoot(hval):
21
    n = len(hval)
22

23
    # Initialize memo array with -1
24
    memo = [-1] * (n + 1)
25
    return maxLootRec(hval, n, memo)
26
​
27
if __name__ == "__main__":
28
    hval = [6, 7, 1, 3, 8, 2, 4]
29
    print(maxLoot(hval))

Output
19
Time Complexity: O(n). Every house is computed only once.
Auxiliary Space: O(n). For recursion stack space and memo array.

[Expected Approach 1] Using Tabulation – O(n) Time and O(n) Space
The idea is to build the solution in bottom-up manner. We create a dp[] array of size n+1 where dp[i] represents the maximum value that can be collected with first i houses. We first fill the known values, dp[0] and dp[1] and then fill the remaining values using the formula: dp[i] = max(hval[i] + dp[i – 2], dp[i – 1]). The final result will be stored at dp[n].





1
# Python Program to solve House Robber Problem using Tabulation
2
​
3
def maxLoot(hval):
4
    n = len(hval)
5

6
    # Create a dp array to store the maximum loot at each house
7
    dp = [0] * (n + 1)
8
​
9
    # Base cases
10
    dp[0] = 0
11
    dp[1] = hval[0]
12
​
13
    # Fill the dp array using the bottom-up approach
14
    for i in range(2, n + 1):
15
        dp[i] = max(hval[i - 1] + dp[i - 2], dp[i - 1])
16
​
17
    return dp[n]
18
​
19
hval = [6, 7, 1, 3, 8, 2, 4]
20
print(maxLoot(hval))

Output
19
Time Complexity: O(n), Every house is computed only once.
Auxiliary Space O(n), We are using a dp array of size n.

[Expected Approach 2] Space-Optimized DP – O(n) Time and O(1) Space
On observing the dp[] array in the previous approach, it can be seen that the answer at the current index depends only on the last two values. In other words, dp[i] depends only on dp[i – 1] and dp[i – 2]. So, instead of storing the result in an array, we can simply use two variables to store the last and second last result.





1
# Python Program to solve House Robber Problem using
2
# Space Optimized Tabulation
3
​
4
# Function to calculate the maximum stolen value
5
def maxLoot(hval):
6
    n = len(hval)
7
​
8
    if n == 0:
9
        return 0
10
    if n == 1:
11
        return hval[0]
12
​
13
    # Set previous 2 values
14
    secondLast = 0
15
    last = hval[0]
16
​
17
    # Compute current value using previous two values
18
    # The final current value would be our result
19
    res = 0
20
    for i in range(1, n):
21
        res = max(hval[i] + secondLast, last)
22
        secondLast = last
23
        last = res
24
​
25
    return res
26
​
27
hval = [6, 7, 1, 3, 8, 2, 4]
28
print(maxLoot(hval))

Output
19
Time Complexity: O(n), Every value is computed only once.
Auxiliary Space: O(1), as we are using only two variables.

"""







