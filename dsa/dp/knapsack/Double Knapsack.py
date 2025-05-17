
"""
Double Knapsack | Dynamic Programming
Last Updated : 16 Nov, 2024
Given an array arr[] containing the weight of ‘n‘ distinct items, and two knapsacks that can withstand capactiy1 and capacity2 weights, the task is to find the sum of the largest subset of the array ‘arr’, that can be fit in the two knapsacks. It’s not allowed to break any items in two, i.e. an item should be put in one of the bags as a whole.

Examples:

Input: arr[] = [8, 3, 2], capacity1 = 10, capacity2 = 3
Output: 13
Explanation: The first and third items are placed in the first knapsack, while the second item is placed in the second knapsack. This results in a total weight of 13.


Input: arr[] = [8, 5, 3] capacity1 = 10, capacity2 = 3
Output: 11
Explanation: The first item is placed in the first knapsack, and the third item is placed in the second knapsack. This results in a total weight of 11.


Table of Content

Using Recursion– O(2^n) Time and O(n) Space
Using Memoization – O(n*capacity1*capacity2) Time and O(n*capacity1*capacity2) Space
Using Tabulation – O(n*capacity1*capacity2) Time and O(n*capacity1*capacity2) Space
Using Recursion– O(2^n) Time and O(n) Space
A recursive solutions is to try out all the possible ways of filling the two knapsacks and choose the one giving the maximum weight.

Every item has 3 choices:


Don’t include the current item: If we don’t include the current item (i.e., arr[curr]), the maximum weight is simply the same as if we move on to the next item, keeping both knapsack capacities unchanged:


findMaxWeight(curr, n, arr, capacity1, capacity2) = findMaxWeight(curr+1, n, arr, capacity1, capacity2)
Include the current item in the first knapsack: If the current item can fit into the first knapsack (i.e., arr[curr] ≤ capacity1), then we include it in the first knapsack, reduce the capacity of the first knapsack by arr[curr], and proceed to the next item with updated capacities. The recurrence relation for this choice is:


findMaxWeight(curr, n, arr, capacity1, capacity2) = max(findMaxWeight(curr+1, n, arr, capacity1-arr[cur], capacity2)+arr[curr], findMaxWeight(curr+1, n, arr, capacity1, capacity2))
Include the current item in the second knapsack: If the current item can fit into the second knapsack (i.e., arr[curr] ≤ capacity2), then we include it in the second knapsack, reduce the capacity of the second knapsack by arr[curr], and proceed to the next item with updated capacities. The recurrence relation for this choice is:


findMaxWeight(curr, n, arr, capacity1, capacity2) = max(findMaxWeight(curr+1, n, arr, capacity1, capacity2-arr[curr])+arr[curr], findMaxWeight(curr+1, n, arr, capacity1, capacity2))



1
# Python program to find the largest subset of
2
# the array that can fit into two knapsacks
3
#  using recursion
4
​
5
def findMaxWeight(curr, n, arr, capacity1, capacity2):
6

7
    # Base case: if all items have been considered
8
    if curr >= n:
9
        return 0
10
​
11
    # Option 1: Don't take the current item
12
    res = findMaxWeight(curr + 1, n, arr, capacity1, capacity2)
13
​
14
    # Option 2: If the current item can be
15
    # added to the first knapsack, do it
16
    if capacity1 >= arr[curr]:
17
        takeInFirst = arr[curr] + \
18
            findMaxWeight(curr + 1, n, arr, capacity1 - arr[curr], capacity2)
19
        res = max(res, takeInFirst)
20
​
21
    # Option 3: If the current item can be
22
    # added to the second knapsack, do it
23
    if capacity2 >= arr[curr]:
24
        takeInSecond = arr[curr] + \
25
            findMaxWeight(curr + 1, n, arr, capacity1, capacity2 - arr[curr])
26
        res = max(res, takeInSecond)
27
    return res
28
​
29
​
30
def maxWeight(arr, capacity1, capacity2):
31
    n = len(arr)
32
    res = findMaxWeight(0, n, arr, capacity1, capacity2)
33
    return res
34
​
35
if __name__ == "__main__":
36
    arr = [8, 2, 3]
37
    capacity1 = 10
38
    capacity2 = 3
39
    res = maxWeight(arr, capacity1, capacity2)
40
    print(res)

Output
13
Using Memoization – O(n*capacity1*capacity2) Time and O(n*capacity1*capacity2) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming.

1. Optimal Substructure: The solution to the two-knapsack problem can be derived from the optimal solutions of smaller subproblems. Specifically, for any given n (the number of items considered) and the remaining capacities of the two knapsacks (capacity1 and capacity2), we can express the recursive relation as follows.


2. Overlapping Subproblems: In the recursive solution to the problem of maximizing the weight in two knapsacks, we observe that many subproblems are computed multiple times, which leads to overlapping subproblems.


We need to track all three parameters, so we create a 3D memoization table of size (n+1) x (capacity1+1) x (capacity2+1).
This table is initialized with -1 to indicate that no subproblems have been computed yet.
If the value at memo[curr][capacity1][capacity2] is not -1, return the already computed result to avoid recomputing the same subproblem.



1
# Python program to find the largest subset of
2
# the array that can fit into two knapsack
3
# using memoization
4
​
5
​
6
def findMaxWeight(curr, n, arr, capacity1, capacity2, memo):
7
​
8
    # Base case: if all items have been considered
9
    if curr >= n:
10
        return 0
11
​
12
    # If the result is already computed for
13
    # this subproblem, return it
14
    if memo[curr][capacity1][capacity2] != -1:
15
        return memo[curr][capacity1][capacity2]
16
​
17
    # Option 1: Don't take the current item
18
    res = findMaxWeight(curr + 1, n, arr, capacity1, capacity2, memo)
19
​
20
    # Option 2: If the current item can be added
21
    # to the first knapsack, do it
22
    if capacity1 >= arr[curr]:
23
        takeInFirst = arr[curr] + \
24
            findMaxWeight(curr + 1, n, arr, capacity1 - arr[curr], capacity2, memo)
25
        res = max(res, takeInFirst)
26
​
27
    # Option 3: If the current item can be added
28
    # to the second knapsack, do it
29
    if capacity2 >= arr[curr]:
30
        takeInSecond = arr[curr] + \
31
            findMaxWeight(curr + 1, n, arr, capacity1, capacity2 - arr[curr], memo)
32
        res = max(res, takeInSecond)
33
​
34
    # Store the result in the memoization table and
35
    # return it
36
    memo[curr][capacity1][capacity2] = res
37
    return res
38
​
39
​
40
def maxWeight(arr, capacity1, capacity2):
41
    n = len(arr)
42
​
43
    # Create a memoization table with all values
44
    # initialized to -1
45
    memo = [[[-1 for _ in range(capacity2 + 1)]
46
             for _ in range(capacity1 + 1)] for _ in range(n)]
47
​
48
    return findMaxWeight(0, n, arr, capacity1, capacity2, memo)
49
​
50
​
51
if __name__ == "__main__":
52
    arr = [8, 2, 3]
53
    capacity1 = 10
54
    capacity2 = 3
55
    res = maxWeight(arr, capacity1, capacity2)
56
    print(res)

Output
13
Using Tabulation – O(n*capacity1*capacity2) Time and O(n*capacity1*capacity2) Space
The approach is similar to the previous one. just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner.

So we will create 3D array dp of size (n + 1) x (capacity1 + 1) x (capacity2 + 1). Here, dp[i][j][k] represents the maximum weight that can be achieved by considering items from arr[0] to arr[i-1] with two knapsacks of remaining capacities j and k.


Base Case:
If no items are considered (i = 0), then no weight can be placed in either knapsack, so:
dp[0][j][k]=0 for all j, k


Recurrence Relation:
For each item i (1<=i<=n), we have three choices:


Do not include item arr[i-1] in either knapsack
dp[i][j][k] = dp[i-1][j][k]
Include item arr[i-1] in the first knapsack if its weight arr[i-1] is less than or equal to j:
dp[i][j][k] = max(dp[i][j][k], arr[i-1] + dp[i-1][j – arr[i-1]][k])
Include item arr[i-1] in the second knapsack if its weight arr[i-1] is less than or equal to k:
dp[i][j][k] = max(dp[i][j][k], arr[i-1] + dp[i-1][j][k – arr[i-1]])



1
# Python program to find the largest subset of
2
# the array that can fit into two knapsack
3
# using tabulation
4
​
5
def maxWeight(arr, capacity1, capacity2):
6
    n = len(arr)
7
​
8
    # Initialize a 3D DP array with dimensions
9
    # (n+1) x (w1+1) x (w2+1)
10
    dp = [[[0 for _ in range(capacity2 + 1)] for _ in range(capacity1 + 1)]
11
          for _ in range(n + 1)]
12
​
13
    # Fill the DP array iteratively
14
    for i in range(1, n + 1):
15
        weight = arr[i - 1]
16
        for j in range(capacity1 + 1):
17
            for k in range(capacity2 + 1):
18
​
19
                # Option 1: Don't take the current item
20
                dp[i][j][k] = dp[i - 1][j][k]
21
​
22
                # Option 2: Take the current item in the
23
                # first knapsack, if possible
24
                if j >= weight:
25
                    dp[i][j][k] = max(dp[i][j][k], weight +
26
                                      dp[i - 1][j - weight][k])
27
​
28
                # Option 3: Take the current item in the
29
                # second knapsack, if possible
30
                if k >= weight:
31
                    dp[i][j][k] = max(dp[i][j][k], weight +
32
                                      dp[i - 1][j][k - weight])
33
​
34
    return dp[n][capacity1][capacity2]
35
​
36
​
37

38
arr = [8, 2, 3]
39
capacity1 = 10
40
capacity2 = 3
41
res = maxWeight(arr, capacity1, capacity2)
42
print(res)

Output
13

"""







