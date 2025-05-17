

"""

Given an array, the task is to find the largest divisible subset in the given array.
Note: A subset is called divisible if for every pair (x, y) in the subset, either x divides y or y divides x.

Examples:

Input: arr[]  = [1, 16, 7, 8, 4]
Output: 16 8 4 1
Explanation: In the output subset, for every pair either the first element divides second or second divides first.


Input : arr[] = [2, 4, 3, 8]
Output : 8 4 2
Explanation: In the output subset, for every pair either the first element divides second or second divides first.


Try it on GfG Practice
redirect icon
A simple solution is to generate all subsets of a given set. For every generated subset, check if it is divisible or not. Finally print the largest divisible subset.

Table of Content

Using Recursion – O(2^n) Time and O(n) Space
Using Top-Down DP(Memoization) – O(n^2) Time and O(n) Space
Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n) Space
Using Recursion – O(2^n) Time and O(n) Space
For the recursive approach to find the largest divisible subset, first sort all array elements in increasing order. The purpose of sorting is to make sure that all divisors of an element appear before it. We can break down the solution into two main cases.
In both cases, the number of available elements decreases by one.

If the current element can be included in the subset (i.e., it is divisible by the last included element), we add it to the current subset and recursively check the next elements.
If the current element cannot be included, we skip it and recursively check the next element.
Mathematically, the recurrence relation will look like:


largestDivisibleSubset(arr, i, prev) = largestDivisibleSubset(arr, i + 1, arr[i]) OR largestDivisibleSubset(arr, i + 1, prev)


Below is the implementation of the above approach:




1
# Python Implementation for Largest Divisible Subset
2
# using Recursion
3
​
4
def lds(res, curr, i, prev, arr):
5
​
6
    # Base case: check if we've reached the
7
    # end of the array
8
    if i >= len(arr):
9
​
10
        # Update ans if the current
11
        # subset is larger
12
        if len(curr) > len(res):
13
            res[:] = curr[:]
14
        return
15
​
16
    # Include current element if divisible by
17
    # previous element
18
    if not curr or arr[i] % prev == 0:
19
        curr.append(arr[i])
20
​
21
        # Recur with the current number included
22
        lds(res, curr, i + 1, arr[i], arr)
23
​
24
        # Backtrack to explore other possibilities
25
        curr.pop()
26
​
27
    # Exclude current element and move to the next
28
    # Recur without including the current number
29
    lds(res, curr, i + 1, prev, arr)
30
​
31
# Main function to find the largest divisible subset
32
def LargestSubset(arr):
33
​
34
    arr.sort()
35
    res = []
36
    curr = []
37
​
38
    # Start the recursive search
39
    lds(res, curr, 0, 1, arr)
40
    return res
41
​
42
​
43
if __name__ == "__main__":
44
​
45
    arr = [1, 16, 7, 8, 4]
46
​
47
    res = LargestSubset(arr)
48
​
49
    for num in res:
50
        print(num, end=" ")

Output
1 4 8 16
Using Top-Down DP(Memoization) – O(n^2) Time and O(n) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming.

1. Optimal Substructure:


For an array of integers, the largest divisible subset including the current element can be determined by considering all preceding elements.
If arr[i] is divisible by arr[j] (for j < i), then the size of the largest divisible subset that includes arr[i] is:
lds(i) = max(1, lds(j) + 1) for all j such that arr[i] % arr[j] = 0
2. Overlapping Subproblems:
The recursive approach leads to overlapping subproblems, where many subproblems are computed multiple times. For example, while evaluating the largest subset for arr[i], results for previously computed arr[j] may be recalculated.


First, sort the array in ascending order to simplify divisibility checks.
Use a memo[] array to keep track of the largest subset size at each index and a parent array for backtracking.
Set all entries in the memo array to -1, indicating uncomputed values.
Loop through the sorted array, calculating the largest divisible subset size by checking previous elements and updating the memo and parent arrays.
After determining the largest size, use the parent array to reconstruct the actual subset.
Below is the implementation of the above approach:




1
# Python Implementation for Largest Divisible Subset
2
# using Memoization
3
​
4
def lds(arr, memo, parent, i):
5
​
6
    # If this subproblem has already been solved,
7
    # return the result
8
    if memo[i] != -1:
9
        return memo[i]
10
​
11
    maxLength = 1
12
    bestParent = -1
13
​
14
    # Try to include arr[i] in the subset
15
    for j in range(i):
16
        if arr[i] % arr[j] == 0:
17
            length = lds(arr, memo, parent, j) + 1
18
            if length > maxLength:
19
                maxLength = length
20
                bestParent = j
21
​
22
    # Store the result in memo and parent
23
    # for backtracking
24
    memo[i] = maxLength
25
    parent[i] = bestParent
26
    return maxLength
27
​
28
# Main function to find the largest
29
# divisible subset
30
def LargestSubset(arr):
31

32
    n = len(arr)
33
    arr.sort()
34
    memo = [-1] * n
35
    parent = [-1] * n
36
​
37
    # Find the largest subset size
38
    maxSize = 0
39
    lastIndex = 0
40
​
41
    for i in range(n):
42
        size = lds(arr, memo, parent, i)
43
        if size > maxSize:
44
            maxSize = size
45
            lastIndex = i
46
​
47
    # Backtrack to construct the subset
48
    res = []
49
    while lastIndex != -1:
50
        res.append(arr[lastIndex])
51
        lastIndex = parent[lastIndex]
52
​
53
    # Result needs to be in ascending
54
    # order
55
    res.reverse()
56
    return res
57
​
58
​
59
if __name__ == "__main__":
60
​
61
    arr = [1, 16, 7, 8, 4]
62
    res = LargestSubset(arr)
63
    print(" ".join(map(str, res)))

Output
1 4 8 16
Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n) Space
The approach utilizes dynamic programming to iteratively build the solution by calculating it in a bottom-up manner. Instead of using recursion, we fill in a table that captures the size of the largest divisible subset for each element in the sorted array.

A one-dimensional array dp of size n is created to store the size of the largest divisible subset ending at each index, initialized to 1 (each element is a subset of itself).
A parent array of size n is also created to keep track of the indices of the preceding elements in the subset, initialized to -1.
For each element arr[i], we look at all previous elements arr[j] (for j < i).

The dynamic programming relation is as follows:

if (arr[i] % arr[j] == 0) and (dp[i] < dp[j]+1)
THEN
dp[i] = dp[j] + 1
parent[i] = j


This means if arr[i] is divisible by arr[j], we update dp[i] to include arr[i] in the subset, incrementing the count from dp[j], and set parent[i] to j to keep track of this relationship. During the filling of the dp array, we also maintain maxSize to keep track of the maximum subset size found so far, along with lastIndex to record the index of the last element in that subset.

Once the dp array is fully populated, we backtrack using the parent array starting from lastIndex to construct the actual largest divisible subset.

Below is the implementation of the above approach:




1
# Python Implementation for Largest Divisible Subset
2
# using Tabulation
3
def LargestSubset(arr):
4
​
5
    arr.sort()
6
    n = len(arr)
7
​
8
    # Table to store the size of
9
    # largest subset
10
    dp = [1] * n
11
​
12
    # To keep track of previous elements
13
    parent = [-1] * n
14
​
15
    # Fill dp table
16
    max_size = 1
17
    last_index = 0
18
​
19
    for i in range(1, n):
20
        for j in range(i):
21
            if arr[i] % arr[j] == 0 and dp[i] < dp[j] + 1:
22
                dp[i] = dp[j] + 1
23
                parent[i] = j
24
​
25
        # Update max_size and last_index
26
        if dp[i] > max_size:
27
            max_size = dp[i]
28
            last_index = i
29
​
30
    # Backtrack to construct the subset
31
    res = []
32
    while last_index >= 0:
33
        res.append(arr[last_index])
34
        last_index = parent[last_index]
35
​
36
    # Reverse the result to get it
37
    # in correct order
38
    res.reverse()
39
    return res
40
​
41
​
42
if __name__ == "__main__":
43
​
44
    arr = [1, 16, 7, 8, 4]
45
​
46
    res = LargestSubset(arr)
47
    for num in res:
48
        print(num, end=" ")

Output
1 4 8 16 
"""







