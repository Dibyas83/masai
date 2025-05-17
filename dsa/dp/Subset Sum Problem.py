
"""
Given an array arr[] of non-negative integers and a value sum, the task is to check if there is a subset of the given array whose sum is equal to the given sum.

Examples:

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.


Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output: False
Explanation: There is no subset that add up to 30.


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Using Recursion – O(2^n) Time and O(n) Space
[Better Approach 1] Using Top-Down DP (Memoization) – O(sum*n) Time and O(sum*n) Space
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(sum*n) Time and O(sum*n) Space
[Expected Approach] Using Space Optimized DP – O(sum*n) Time and O(sum) Space
[Naive Approach] Using Recursion – O(2^n) Time and O(n) Space
For the recursive approach, there will be two cases (In both cases, the number of available elements decreases by 1)


Consider the ‘last’ element to be a part of the subset. Now the new required sum = required sum – value of ‘last’ element.
Don’t include the ‘last’ element in the subset. Then the new required sum = old required sum.
Mathematically the recurrence relation will look like the following:

isSubsetSum(arr, n, sum) = isSubsetSum(arr, n-1, sum) OR isSubsetSum(arr, n-1, sum – arr[n-1])


Base Cases:


isSubsetSum(arr, n, sum) = false, if sum > 0 and n = 0
isSubsetSum(arr, n, sum) = true, if sum = 0
Follow the below steps to implement the recursion:

Build a recursive function and pass the index to be considered (here gradually moving from the last end) and the remaining sum amount.
For each index check the base cases.
If the answer is true for any recursion call, then there exists such a subset. Otherwise, no such subset exists.



1
# Python implementation for subset sum
2
# problem using recursion
3
def isSubsetSumRec(arr, n, sum):
4

5
    # Base Cases
6
    if sum == 0:
7
        return True
8
    if n == 0:
9
        return False
10
​
11
    # If the last element is greater
12
    # than the sum, ignore it
13
    if arr[n - 1] > sum:
14
        return isSubsetSumRec(arr, n - 1, sum)
15
​
16
    # Check if sum can be obtained by including
17
    # or excluding the last element
18
    return (isSubsetSumRec(arr, n - 1, sum) or
19
            isSubsetSumRec(arr, n - 1, sum - arr[n - 1]))
20
​
21
def isSubsetSum(arr, sum):
22
    return isSubsetSumRec(arr, len(arr), sum)
23
​
24
if __name__ == "__main__":
25

26
    arr = [3, 34, 4, 12, 5, 2]
27
    sum = 9
28
​
29
    if isSubsetSum(arr, sum):
30
        print("True")
31
    else:
32
        print("False")

Output
True
[Better Approach 1] Using Top-Down DP (Memoization) – O(sum*n) Time and O(sum*n) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming.

1. Optimal Substructure:


The solution to the subset sum problem can be derived from the optimal solutions of smaller subproblems. Specifically, for any given n (the number of elements considered) and a target sum, we can express the recursive relation as follows:


If the last element (arr[n-1]) is greater than sum, we cannot include it in our subset isSubsetSum(arr,n,sum) = isSubsetSum(arr,n-1,sum)
If the last element is less than or equal to sum, we have two choices:


Include the last element in the subset, isSubsetSum(arr,n,sum) = isSubsetSum(arr,n-1,sum-arr[n−1])
Exclude the last element, isSubsetSum(arr,n,sum) = isSubsetSum(arr,n-1,sum)
2. Overlapping Subproblems:


When implementing a recursive approach to solve the subset sum problem, we observe that many subproblems are computed multiple times. For instance, when computing isSubsetSum(arr, sum), where arr[] = {2,3,1,1} and sum = 4 we might need to compute isSubsetSum(1,3) multiple times.


subset-sum-problem
Overlapping subproblems

The recursive solution involves changing two parameters: the current index in the array (n) and the current target sum (sum). We need to track both parameters, so we create a 2D array of size (n+1) x (sum+1) because the value of n will be in the range [0, n] and sum will be in the range [0, sum].
We initialize the 2D array with -1 to indicate that no subproblems have been computed yet.
We check if the value at memo[n][sum] is -1. If it is, we proceed to compute the result. otherwise, we return the stored result.



1
# Python implementation for subset sum
2
# problem using memoization
3
def isSubsetSumRec(arr, n, sum, memo):
4
​
5
    # If the sum is zero, we found
6
    # a subset
7
    if sum == 0:
8
        return True
9
​
10
    # If no elements are left
11
    if n <= 0:
12
        return False
13
​
14
    # If the value is already
15
    # computed, return it
16
    if memo[n][sum] != -1:
17
        return memo[n][sum]
18
​
19
    # If the last element is greater
20
    # than the sum, ignore it
21
    if arr[n - 1] > sum:
22
        memo[n][sum] = isSubsetSumRec(arr, n - 1, sum, memo)
23
    else:
24

25
        # Include or exclude the last element
26
        # directly
27
        memo[n][sum] = (isSubsetSumRec(arr, n - 1, sum, memo)
28
                        or isSubsetSumRec(arr, n - 1, sum - arr[n - 1], memo))
29
​
30
    return memo[n][sum]
31
​
32
​
33
def isSubsetSum(arr, sum):
34
    n = len(arr)
35
    memo = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
36
    return isSubsetSumRec(arr, n, sum, memo)
37
​
38
​
39
if __name__ == "__main__":
40
    arr = [1, 5, 3, 7, 4]
41
    sum = 12
42
​
43
    if isSubsetSum(arr, sum):
44
        print("True")
45
    else:
46
        print("False")

Output
True
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(sum*n) Time and O(sum*n) Space
The approach is similar to the previous one. just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner.

So we will create a 2D array of size (n + 1) * (sum + 1) of type boolean. The state dp[i][j] will be true if there exists a subset of elements from arr[0 . . . i] with sum = ‘j’.


The dynamic programming relation is as follows:


if (arr[i-1] > j)
    dp[i][j] = dp[i-1][j]
else
    dp[i][j] = dp[i-1][j] OR dp[i-1][j-arr[i-1]]


This means that if the current element has a value greater than the ‘current sum value’ we will copy the answer for previous cases and if the current sum value is greater than the ‘ith’ element we will see if any of the previous states have already computed the sum= j OR any previous states computed a value ‘j – arr[i]’ which will solve our purpose.




1
# Python implementation for subset sum
2
# problem using tabulation
3
def isSubsetSum(arr, sum):
4
    n = len(arr)
5
​
6
    # Create a 2D list for storing
7
    # results of subproblems
8
    dp = [[False] * (sum + 1) for _ in range(n + 1)]
9
​
10
    # If sum is 0, then answer is
11
    # true (empty subset)
12
    for i in range(n + 1):
13
        dp[i][0] = True
14
​
15
    # Fill the dp table in bottom-up manner
16
    for i in range(1, n + 1):
17
        for j in range(1, sum + 1):
18
            if j < arr[i - 1]:
19

20
                # Exclude the current element
21
                dp[i][j] = dp[i - 1][j]
22
            else:
23

24
                # Include or exclude
25
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
26
​
27
    return dp[n][sum]
28
​
29
​
30
if __name__ == "__main__":
31
    arr = [3, 34, 4, 12, 5, 2]
32
    sum_value = 9
33
​
34
    if isSubsetSum(arr, sum_value):
35
        print("True")
36
    else:
37
        print("False")

Output
True
[Expected Approach] Using Space Optimized DP – O(sum*n) Time and O(sum) Space
In previous approach of dynamic programming we have derive the relation between states as given below:


if (arr[i-1] > j)
    dp[i][j] = dp[i-1][j]
else
    dp[i][j] = dp[i-1][j] OR dp[i-1][j-arr[i-1]]


If we observe that for calculating current dp[i][j] state we only need previous row dp[i-1][j] or dp[i-1][j-arr[i-1]]. There is no need to store all the previous states just one previous state is used to compute result.


Approach:

Define two arrays prev and curr of size sum+1 to store the just previous row result and current row result respectively.
Once curr array is calculated then curr becomes our prev for the next row.
When all rows are processed the answer is stored in prev array.



1
# Python Program for Space Optimized Dynamic Programming
2
# Solution to Subset Sum Problem
3
def isSubsetSum(arr, sum):
4
    n = len(arr)
5
    prev = [False] * (sum + 1)
6
    curr = [False] * (sum + 1)
7
​
8
    # Base case: sum 0 can always
9
    # be achieved
10
    prev[0] = True
11
​
12
    # Fill the dp table in a
13
    # bottom-up manner
14
    for i in range(1, n + 1):
15
        for j in range(sum + 1):
16
            if j < arr[i - 1]:
17
                curr[j] = prev[j]
18
            else:
19
                curr[j] = prev[j] or prev[j - arr[i - 1]]
20
        prev = curr.copy()
21
​
22
    return prev[sum]
23
​
24
if __name__ == "__main__":
25
    arr = [3, 34, 4, 12, 5, 2]
26
    sum_value = 9
27
    if isSubsetSum(arr, sum_value):
28
        print("True")
29
    else:
30
        print("False")

Output
True
Related articles:

Subset Sum Problem in O(sum) space
Perfect Sum Problem (Print all subsets with given sum)

"""

