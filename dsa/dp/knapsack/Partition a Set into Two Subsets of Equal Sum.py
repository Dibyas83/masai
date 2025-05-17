
"""
Given an array arr[], the task is to check if it can be partitioned into two parts such that the sum of elements in both parts is the same.
Note: Each element is present in either the first subset or the second subset, but not in both.

Examples:

Input: arr[] = [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11]


Input: arr[] = [1, 5, 3]
Output: false
Explanation: The array cannot be partitioned into equal sum sets.


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Using Recursion – O(2^n) Time and O(n) Space
[Better Approach 1] Using Top-Down DP (Memoization) – O(sum*n) Time and O(sum*n) Space
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(sum*n) Time and O(sum*n) Space
[Expected Approach] Using Space Optimized DP – O(sum*n) Time and O(sum) Space
The following are the two main steps to solve this problem:

Calculate the sum of the array. If the sum is odd, this cannot be two subsets with an equal sum, so return false.
If the sum of the array elements is even, calculate sum/2 and find a subset of the array with a sum equal to sum/2.
The first step is simple. The second step is crucial, it can be solved either using recursion or Dynamic Programming.
[Naive Approach] Using Recursion – O(2^n) Time and O(n) Space
Let isSubsetSum(arr, n, sum/2) be the function that returns true if there is a subset of arr[0..n-1] with sum equal to sum/2
The isSubsetSum problem can be divided into two subproblems


 isSubsetSum() without considering last element (reducing n to n-1)
 isSubsetSum() considering the last element (reducing sum/2 by arr[n-1] and n to n-1)
If any of the above subproblems return true, then return true.
isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) OR isSubsetSum (arr, n-1, sum/2 – arr[n-1])


Step by Step implementation:

First, check if the sum of the elements is even or not.
After checking, call the recursive function isSubsetSum with parameters as input array, array size, and sum/2
If the sum is equal to zero then return true (Base case)
If n is equal to 0 and sum is not equal to zero then return false (Base case)
Check if the value of the last element is greater than the remaining sum then call this function again by removing the last element
Else call this function again for both the cases stated above and return true, if anyone of them returns true
Print the answer



1
# Python program to partition a Set
2
# into Two Subsets of Equal Sum
3
# using recursion
4
def isSubsetSum(n, arr, sum):
5

6
    # base cases
7
    if sum == 0:
8
        return True
9
    if n == 0:
10
        return False
11
​
12
    # If element is greater than sum, then ignore it
13
    if arr[n-1] > sum:
14
        return isSubsetSum(n-1, arr, sum)
15
​
16
    # Check if sum can be obtained by any of the following
17
    # (a) including the current element
18
    # (b) excluding the current element
19
    return isSubsetSum(n-1, arr, sum) or \
20
           isSubsetSum(n-1, arr, sum - arr[n-1])
21
​
22
def equalPartition(arr):
23

24
    # Calculate sum of the elements in array
25
    arrSum = sum(arr)
26
​
27
    # If sum is odd, there cannot be two
28
    # subsets with equal sum
29
    if arrSum % 2 != 0:
30
        return False
31
​
32
    # Find if there is subset with sum equal
33
    # to half of total sum
34
    return isSubsetSum(len(arr), arr, arrSum // 2)
35
​
36
if __name__ == "__main__":
37
    arr = [1, 5, 11, 5]
38
    if equalPartition(arr):
39
        print("True")
40
    else:
41
        print("False")

Output
True
[Better Approach 1] Using Top-Down DP (Memoization) – O(sum*n) Time and O(sum*n) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming.

1. Optimal Substructure:


The solution to the subset sum problem can be derived from the optimal solutions of smaller subproblems. Specifically, for any given n (the number of elements considered) and a target sum, we can express the recursive relation as follows:


If the last element (arr[n-1]) is greater than sum, we cannot include it in our subset isSubsetSum(arr,n,sum) = isSubsetSum(arr,n-1,sum)
If the last element is less than or equal to sum, we have two choices:


Include the last element in the subset, isSubsetSum(arr, n, sum) = isSubsetSum(arr, n-1, sum-arr[n-1])
Exclude the last element, isSubsetSum(arr, n, sum) = isSubsetSum(arr, n-1, sum)
2. Overlapping Subproblems:


When implementing a recursive approach to solve the subset sum problem, we observe that many subproblems are computed multiple times.


The recursive solution involves changing two parameters: the current index in the array (n) and the current target sum (sum). We need to track both parameters, so we create a 2D array of size (n+1) x (sum + 1) because the value of n will be in the range [0, n] and sum will be in the range [0, sum].
We initialize the 2D array with -1 to indicate that no subproblems have been computed yet.
We check if the value at memo[n][sum] is -1. If it is, we proceed to compute the result. otherwise, we return the stored result.



1
# Python program to partition a Set
2
# into Two Subsets of Equal Sum
3
# using top down approach
4
def isSubsetSum(n, arr, sum, memo):
5

6
    # base cases
7
    if sum == 0:
8
        return True
9
    if n == 0:
10
        return False
11
​
12
    if memo[n-1][sum] != -1:
13
        return memo[n-1][sum]
14
​
15
    # If element is greater than sum, then ignore it
16
    if arr[n-1] > sum:
17
        return isSubsetSum(n-1, arr, sum, memo)
18
​
19
    # Check if sum can be obtained by any of the following
20
    # (a) including the current element
21
    # (b) excluding the current element
22
    memo[n-1][sum] = isSubsetSum(n-1, arr, sum, memo) or\
23
                     isSubsetSum(n-1, arr, sum - arr[n-1], memo)
24
    return memo[n-1][sum]
25
​
26
def equalPartition(arr):
27

28
    # Calculate sum of the elements in array
29
    arrSum = sum(arr)
30
​
31
    # If sum is odd, there cannot be two
32
    # subsets with equal sum
33
    if arrSum % 2 != 0:
34
        return False
35
​
36
    memo = [[-1 for _ in range(arrSum+1)] for _ in range(len(arr))]
37

38
    # Find if there is subset with sum equal
39
    # to half of total sum
40
    return isSubsetSum(len(arr), arr, arrSum // 2, memo)
41
​
42
if __name__ == "__main__":
43
    arr = [1, 5, 11, 5]
44
    if equalPartition(arr):
45
        print("True")
46
    else:
47
        print("False")

Output
True
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(sum*n) Time and O(sum*n) Space
The approach is similar to the previous one. just instead of breaking down the problem recursively, we iteratively build up the solution by calculating in bottom-up manner.

So we will create a 2D array of size (n + 1) * (sum + 1) of type boolean. The state dp[i][j] will be true if there exists a subset of elements from arr[0 . . . i] with sum = ‘j’.


The dynamic programming relation is as follows:


if (arr[i-1]>j)
    dp[i][j]=dp[i-1][j]
else
  dp[i][j]=dp[i-1][j] OR dp[i-1][j-arr[i-1]]


This means that if the current element has a value greater than the ‘current sum value’ we will copy the answer for previous cases and if the current sum value is greater than the ‘ith’ element we will see if any of the previous states have already computed the sum = j OR any previous states computed a value ‘j – arr[i]’ which will solve our purpose.




1
# Python program to partition a Set
2
# into Two Subsets of Equal Sum
3
# using top up approach
4
def equalPartition(arr):
5

6
    # Calculate sum of the elements in array
7
    arrSum = sum(arr)
8
    n = len(arr)
9
​
10
    # If sum is odd, there cannot be two
11
    # subsets with equal sum
12
    if arrSum % 2 != 0:
13
        return False
14
​
15
    arrSum = arrSum // 2
16
​
17
    # Create a 2D array for storing results
18
    # of subproblems
19
    dp = [[False] * (arrSum + 1) for _ in range(n + 1)]
20
​
21
    # If sum is 0, then answer is true (empty subset)
22
    for i in range(n + 1):
23
        dp[i][0] = True
24
​
25
    # Fill the dp table in bottom-up manner
26
    for i in range(1, n + 1):
27
        for j in range(1, arrSum + 1):
28
            if j < arr[i - 1]:
29

30
                # Exclude the current element
31
                dp[i][j] = dp[i - 1][j]
32
            else:
33

34
                # Include or exclude
35
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
36
​
37
    return dp[n][arrSum]
38
​
39
if __name__ == "__main__":
40
    arr = [1, 5, 11, 5]
41
    if equalPartition(arr):
42
        print("True")
43
    else:
44
        print("False")

Output
True
[Expected Approach] Using Space Optimized DP – O(sum*n) Time and O(sum) Space
In previous approach of dynamic programming we have derive the relation between states as given below:


if (arr[i-1]>j)
    dp[i][j] = dp[i-1][j]
else
    dp[i][j] = dp[i-1][j] OR dp[i-1][j-arr[i-1]]


If we observe that for calculating current dp[i][j] state we only need previous row dp[i-1][j] or dp[i-1][j-arr[i-1]]. There is no need to store all the previous states just one previous state is used to compute result.


Approach:

Define two arrays prev and curr of size sum+1 to store the just previous row result and current row result respectively.
Once curr array is calculated then curr becomes our prev for the next row.
When all rows are processed the answer is stored in prev array.



1
# Python program to partition a Set
2
# into Two Subsets of Equal Sum
3
# using space optimised
4
def equalPartition(arr):
5

6
    # Calculate sum of the elements in array
7
    arrSum = sum(arr)
8
​
9
    # If sum is odd, there cannot be two
10
    # subsets with equal sum
11
    if arrSum % 2 != 0:
12
        return False
13
​
14
    arrSum = arrSum // 2
15
​
16
    n = len(arr)
17
    prev = [False] * (arrSum + 1)
18
    curr = [False] * (arrSum + 1)
19
​
20
    # Mark prev[0] = true as it is true
21
    # to make sum = 0 using 0 elements
22
    prev[0] = True
23
​
24
    # Fill the subset table in
25
    # bottom-up manner
26
    for i in range(1, n + 1):
27
        for j in range(arrSum + 1):
28
            if j < arr[i - 1]:
29
                curr[j] = prev[j]
30
            else:
31
                curr[j] = (prev[j] or prev[j - arr[i - 1]])
32
​
33
        prev = curr.copy()
34
​
35
    return prev[arrSum]
36
​
37
if __name__ == "__main__":
38
    arr = [1, 5, 11, 5]
39
    if equalPartition(arr):
40
        print("True")
41
    else:
42
        print("False")

Output
True
Related Articles:

Subset Sum Problem
Perfect Sum Problem (Print all subsets with given sum)


"""









