


"""
We are given two numbers n and k, the task is to find how many permutations of the first n number have exactly k inversion. Two elements in a sequence form an inversion if the smaller element appears before the larger element.

Examples:

Input: n = 3, k = 1
Output: 2
Explanation: Total Permutation of first 3 numbers are 123, 132, 213, 231, 312, 321
Permutation with 1 inversion: 132 and 213


Input: n = 3, k = 3
Output: 1
Explanation: Permutation with 3 inversions: 321


Try it on GfG Practice
redirect icon
Table of Content

Using Recursion – O(n! * k) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n*k*k) Time and O(n*k) Space
Using Bottom-Up DP (Tabulation) – O(n*k*k) Time and O(n*k) Space
Using Recursion – O(n! * k) Time and O(n) Space
Base Cases:


If n == 0, no permutations are possible, so return 0.
If k == 0, there is exactly one permutation (the sorted order), so return 1.
Recursive Relation:


For each possible position i where the nth element can be placed (where i ranges from 0 to min(k, n-1)), we recursively call the function to calculate the number of permutations of n-1 elements with k-i inversions. This represents placing the nth element in a way that creates i inversions.
countPermWithkInversions(n, k) = Σ(countPermWithkInversions(n-1, k-i)) for i = 0 to min(k, n-1)





1
# Python code to count permutations with exactly
2
# k inversions using Recursion
3
def countPermWithkInversions(n, k):
4
​
5
    # Base cases
6
    # no permutations possible with 0 elements
7
    if n == 0:
8
        return 0
9
​
10
    # Only one way to have 0 inversions: sorted order
11
    if k == 0:
12
        return 1
13
​
14
    # Initialize result for this recursive step
15
    result = 0
16
​
17
    # Recursively sum up all valid counts
18
    # by placing the nth largest element
19
    # in positions that create the
20
    # required inversion counts
21
    for i in range(min(k, n - 1) + 1):
22
        result += countPermWithkInversions(n - 1, k - i)
23
​
24
    return result
25

26
if __name__ == "__main__":
27

28
    n = 4
29
    k = 2
30
​
31
    print(countPermWithkInversions(n, k))

Output
5
Using Top-Down DP (Memoization) – O(n*k*k) Time and O(n*k) Space
The above recursive solution satisfies two key properties of Dynamic Programming, enabling us to use memoization for an optimized approach.

1. Optimal Substructure


We solve the problem of counting permutations with exactly k inversions by breaking it into subproblems involving fewer elements and inversions. Specifically, if we have n elements and k required inversions, we can compute it by trying positions for the largest element in a way that contributes to the inversion count.


The recursive relation is:


countPermWithkInversions(n, k) = Σ countPermWithkInversions(n-1, k-i)
Here, we consider placing the largest element in positions that create i inversions, where i ranges from 0 to min(k, n-1).


2. Overlapping Subproblems:


Many subproblems are computed multiple times when finding permutations for smaller subsets and inversion counts. For example, while calculating the result for (n, k), subproblems for (n-1, k-i) are encountered repeatedly.


We use a 2D array memo of size (n+1) x (k+1), initialized to -1, to store results of subproblems. If a result is already stored in memo[n][k], we return it directly, avoiding redundant calculations.




1
# Python code to find number of permutation
2
# with k inversions using Memoization
3
​
4
def kInversionsHelper(n, k, memo):
5

6
    # Base case: If there are no elements,
7
    # no permutations are possible
8
    if n == 0:
9
        return 0
10
​
11
    # Base case: If k is 0, only one way to
12
    # have 0 inversions: sorted order
13
    if k == 0:
14
        return 1
15
​
16
    # Check if the result is already
17
    # computed (memoization)
18
    if memo[n][k] != -1:
19
        return memo[n][k]
20
​
21
    result = 0
22
​
23
    # Loop through possible inversion counts
24
    # for the nth largest element
25
    for i in range(min(k, n - 1) + 1):
26

27
        # Recursively count permutations for the
28
        # remaining elements and inversions
29
        result = (result + kInversionsHelper(n - 1, k - i, memo))
30
​
31
    memo[n][k] = result
32
    return result
33
​
34
def countPermWithkInversions(n, k):
35

36
    # Initialize memoization table with -1
37
    # to indicate uncomputed values
38
    memo = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]
39
    return kInversionsHelper(n, k, memo)
40
​
41
if __name__ == "__main__":
42

43
    n = 4
44
    k = 2
45
​
46
    print(countPermWithkInversions(n, k))

Output
5
Using Bottom-Up DP (Tabulation) – O(n*k*k) Time and O(n*k) Space
We create a 2D array dp of size (n + 1)*(k + 1), where the state dp[l][r] represents the number of permutations of l elements with exactly r inversions.

Base Case: dp[l][0] = 1 for all l, since there’s only one way to have zero inversions-by arranging elements in sorted order.


For each element count l from 1 to n:


For each inversion count r from 1 to k, calculate the number of valid permutations.
To compute dp[l][r], we iterate over all possible positions of the largest element, which can create up to min(r, l-1) inversions, summing up the results from previous states
This relation fills the DP table by counting valid permutations based on subproblems:


dp[l][r] = sum of dp[l-1][r-i] for all valid i.
The final result is stored in dp[n][k], representing the total permutations of n elements with exactly k inversions.




1
# Python code to find number of permutation
2
# with k inversions using Tabulation
3
​
4
def countPermWithkInversions(n, k):
5

6
    # Initialize a 2D table for dynamic programming
7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
8
​
9
    # Base case: If k is 0, only one way to
10
    # have 0 inversions: sorted order
11
    for l in range(n + 1):
12
        dp[l][0] = 1
13
​
14
    # Fill the table using the tabulation method
15
    for l in range(1, n + 1):
16
        for r in range(1, k + 1):
17
            for i in range(min(r, l - 1) + 1):
18

19
                # Count permutations for the remaining
20
                # elements and inversions
21
                dp[l][r] = (dp[l][r] + dp[l - 1][r - i])
22
​
23
    return dp[n][k]
24

25
if __name__ == "__main__":
26
​
27
    n = 4
28
    k = 2
29
​
30
    print(countPermWithkInversions(n, k))

Output
5
Time Complexity: O(n*k*k), where n is the number of elements and k is the number of inversions, due to the nested loops iterating through n, k, and possible inversions.
Auxiliary Space: O(n*k), because we maintain a 2D table of size (n+1)×(k+1) to store the computed values for dynamic programming.

"""







