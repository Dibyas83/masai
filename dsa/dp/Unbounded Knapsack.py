

"""

Unbounded Knapsack (Repetition of items allowed)
Last Updated : 15 Nov, 2024
Given a knapsack weight, say capacity and a set of n items with certain value vali and weight wti, The task is to fill the knapsack in such a way that we can get the maximum profit. This is different from the classical Knapsack problem, here we are allowed to use an unlimited number of instances of an item.

Examples:

Input: capacity = 100, val[]  = [1, 30], wt[] = [1, 50]
Output: 100
Explanation: There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50 instances of 1 unit weight items.
We get maximum value with option 2.

Input: capacity = 8, val[] = [10, 40, 50, 70], wt[]  = [1, 3, 4, 5]
Output : 110
Explanation: We get maximum value with one unit of weight 5 and one unit of weight 3.


Try it on GfG Practice
redirect icon
Table of Content

Using Recursive Method – O(2^n) time and O(capacity) space
Using Top-Down DP (Memoization) – O(n*capacity) Time and O(n*capacity) Space
Using Bottom-Up DP (Tabulation) – O(n*capacity) Time and O(n*capacity) Space
Using Space Optimized DP – O(n*capacity) Time and O(capacity) Space
Using Recursive Method – O(2^n) time and O(capacity) space
The idea is to explore the two possibilities for each item in the list. We start by considering the first item and check if it can be included in the knapsack, meaning its weight is less than or equal to the current remaining weight capacity.


If we include the item, we add its value to the total profit and recursively solve the problem with the same item but with reduced weight.
If we exclude the item, we move to the next item in the list without changing the weight. The recursion continues until we have considered all items, and the maximum profit is obtained by either including or excluding each item in every step.
The solution is found by returning the maximum of the two choices-whether to include or exclude the item at each stage.The recurrence relation can be expressed as:


knapSackRecur(i, capacity) = max(knapSackRecur(i, capacity – wt[i]) + val[i], knapSackRecur(i + 1, capacity))



1
# Python program to implement
2
# unbounded knapsack problem using recursion.
3
​
4
def knapSackRecur(i, capacity, val, wt):
5
    if i == len(val):
6
        return 0
7
​
8
    # Consider current item only if
9
    # its weight is less than equal
10
    # to maximum weight.
11
    take = 0
12
    if wt[i] <= capacity:
13
        take = val[i] + knapSackRecur(i, capacity - wt[i], val, wt)
14
​
15
    # Skip the current item
16
    noTake = knapSackRecur(i + 1, capacity, val, wt)
17
​
18
    # Return maximum of the two.
19
    return max(take, noTake)
20
​
21
def knapSack(capacity, val, wt):
22
    return knapSackRecur(0, capacity, val, wt)
23
​
24
if __name__ == "__main__":
25
    val = [1, 1]
26
    wt = [2, 1]
27
    capacity = 3
28
    print(knapSack(capacity, val, wt))

Output
3
Using Top-Down DP (Memoization) – O(n*capacity) Time and O(n*capacity) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming.

1. Optimal Substructure: The Unbounded Knapsack Problem has an optimal substructure property, meaning the solution to the problem can be derived from the solutions to smaller subproblems. Specifically, for any given item i and remaining capacity w, we can express the recursive relation as follows:


Include the current item: If the weight of the current item wt[i] is less than or equal to the current capacity w, we can include it multiple times. The new problem becomes knapSack(i, capacity – wt[i], val, wt), where i does not increment because repetition of items is allowed.
Exclude the current item: If we do not include the current item, the problem becomes knapSack(i + 1, capacity, val, wt).
2. Overlapping Subproblems: When implementing the recursive solution, we notice that many subproblems are computed multiple times. For example, in the recursive call knapSack(i, capacity), we might need to compute knapSack(i, capacity – wt[i]) and knapSack(i + 1, capacity) multiple times, especially when the weight w is large.


There are two parameters i and capacity that changes in the recursive solution. So we create a 2D matrix of size n*(capacity+1) for memoization.
We initialize this matrix as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program to implement
2
# unbounded knapsack problem using memoization.
3
​
4
def knapSackRecur(i, capacity, val, wt, memo):
5
    if i == len(val):
6
        return 0
7
​
8
    # If value is memoized.
9
    if memo[i][capacity] != -1:
10
        return memo[i][capacity]
11
​
12
    # Consider current item only if
13
    # its weight is less than equal
14
    # to maximum weight.
15
    take = 0
16
    if wt[i] <= capacity:
17
        take = val[i] + knapSackRecur(i, capacity - wt[i], val, wt, memo)
18
​
19
    # Skip the current item
20
    noTake = knapSackRecur(i + 1, capacity, val, wt, memo)
21
​
22
    # store maximum of the two and return it.
23
    memo[i][capacity] = max(take, noTake)
24
    return memo[i][capacity]
25
​
26
def knapSack(capacity, val, wt):
27

28
    # 2D matrix for memoization.
29
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(val))]
30
    return knapSackRecur(0, capacity, val, wt, memo)
31
​
32
if __name__ == "__main__":
33
    val = [1, 1]
34
    wt = [2, 1]
35
    capacity = 3
36
    print(knapSack(capacity, val, wt))

Output
3
Using Bottom-Up DP (Tabulation) – O(n*capacity) Time and O(n*capacity) Space
 The idea is to fill the dp table based on previous values. For each item, we either include it or exclude it to compute the maximum value for each given knapsack weight. The table is filled in an iterative manner from i = n-1 to i = 0 and for each weight from 1 to capacity.





1
# Python program to implement
2
# unbounded knapsack problem using tabulation
3
​
4
def knapSack(capacity, val, wt):
5

6
    # 2D matrix for tabulation.
7
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(val) + 1)]
8
​
9
    # Calculate maximum profit for each
10
    # item index and knapsack weight.
11
    for i in range(len(val) - 1, -1, -1):
12
        for j in range(1, capacity + 1):
13
​
14
            take = 0
15
            if j - wt[i] >= 0:
16
                take = val[i] + dp[i][j - wt[i]]
17
            noTake = dp[i + 1][j]
18
​
19
            dp[i][j] = max(take, noTake)
20
​
21
    return dp[0][capacity]
22
​
23
if __name__ == "__main__":
24
    val = [1, 1]
25
    wt = [2, 1]
26
    capacity = 3
27
    print(knapSack(capacity, val, wt))

Output
3
Using Space Optimized DP – O(n*capacity) Time and O(capacity) Space
The idea is store only the next row values. We can observe that for a given index i, its value depends only on current (i) and next (i+1) row. So only store these values and update them after each step.





1
# Python program to implement
2
# unbounded knapsack problem using space optimised
3
​
4
def knapSack(capacity, val, wt):
5
​
6
    # 1D matrix for tabulation.
7
    dp = [0] * (capacity + 1)
8
​
9
    # Calculate maximum profit for each
10
    # item index and knapsack weight.
11
    for i in range(len(val) - 1, -1, -1):
12
        for j in range(1, capacity + 1):
13
​
14
            take = 0
15
            if j - wt[i] >= 0:
16
                take = val[i] + dp[j - wt[i]]
17
            noTake = dp[j]
18
​
19
            dp[j] = max(take, noTake)
20
​
21
    return dp[capacity]
22
​
23
​
24
if __name__ == "__main__":
25
    val = [1, 1]
26
    wt = [2, 1]
27
    capacity = 3
28
    print(knapSack(capacity, val, wt))

Output
3
"""







