
"""
Find the Nth row in Pascal’s Triangle
Last Updated : 26 Apr, 2025
Given a non-negative integer n, the task is to find the nth row of Pascal’s Triangle.

Note: The row index starts from 1.

Examples:

Input: n = 4
Output: 1 3 3 1
Explanation: The elements in the 4th row are 1 3 3 1 as shown in Pascal Triangle.


Nth-row-in-Pascals-Triangle
Input: n = 1
Output: 1
Explanation: The elements in the 1th row is 1 as shown in Pascal Triangle.


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Using Recursion – O(2^n) Time and O(n) Space
[Better Approach] Using Recursion Level by Level – O(n^2) Time and O(n) Space
[Expected Approach] Using Combinatorics – O(n) Time and O(n) Space
[Naive Approach] Using Recursion – O(2^n) Time and O(n) Space
The idea is to use the property that each element i in the Pascal triangle is equal to the sum of two elements directly above it (i-1 and i), with the base condition that the first and last element of any row will be equal to 1.





1
# Python program to Find the nth row in
2
# Pascal’s Triangle using Recursion
3
​
4
# Function which recursively finds the
5
# ith value of nth row.
6
def findVal(i, n):
7

8
    # First and last value of each
9
    # row will always be 1.
10
    if i == 1 or i == n:
11
        return 1
12

13
    # Find the (i-1)th and ith
14
    # value of previous row
15
    return findVal(i - 1, n - 1) + findVal(i, n - 1)
16
​
17
# Function to find the elements
18
# of n'th row in Pascal's Triangle
19
def nthRowOfPascalTriangle(n):
20
    res = []
21

22
    for i in range(1, n + 1):
23
        val = findVal(i, n)
24
        res.append(val)
25

26
    return res
27
​
28
if __name__ == "__main__":
29
    n = 4
30
    ans = nthRowOfPascalTriangle(n)
31
​
32
    for i in range(len(ans)):
33
        print(ans[i], end=" ")
34
    print()

Output
1 3 3 1
[Better Approach] Using Recursion Level by Level – O(n^2) Time and O(n) Space
The idea is to recursively find the n’th row by recursively finding the previous row. Then use the previous row to calculate the values of current row.





1
# Python program to Find the nth row in
2
# Pascal’s Triangle using Recursion
3
​
4
# Function to find the elements
5
# of n'th row in Pascal's Triangle
6
def nthRowOfPascalTriangle(n):
7
    curr = []
8
​
9
    # 1st element of every row is 1
10
    curr.append(1)
11
​
12
    # Check if the row that has to
13
    # be returned is the first row
14
    if n == 1:
15
        return curr
16
​
17
    # Generate the previous row
18
    prev = nthRowOfPascalTriangle(n - 1)
19
​
20
    for i in range(1, len(prev)):
21
​
22
        # Generate the elements of the current
23
        # row with the help of the previous row
24
        val = prev[i - 1] + prev[i]
25
        curr.append(val)
26
​
27
    curr.append(1)
28
​
29
    # Return the row
30
    return curr
31
​
32
if __name__ == "__main__":
33
    n = 4
34
    ans = nthRowOfPascalTriangle(n)
35
​
36
    for val in ans:
37
        print(val, end=" ")
38
    print()

Output
1 3 3 1
[Expected Approach] Using Combinatorics – O(n) Time and O(n) Space
The idea is to use the mathematical relationship between consecutive elements in a Pascal’s Triangle row, rather than computing the entire triangle. Since the nth row consists of binomial coefficients nC0, nC1, …, nCn, we can calculate each element directly from the previous one using the formula: nCr = (nCr-1 * (n-r+1))/r. This approach starts with nC0 = 1 and efficiently computes each subsequent value


Note: This approach uses 0-based indexing because the mathematical formula used for calculating binomial coefficients aligns with 0-based indexing.

pascal-s-triangle
Step by step approach:

Start with first element of the row as 1 (nC0 = 1).
For each subsequent element, use the formula nCr = (nCr-1 * (n-r+1))/r.
Build the row progressively by calculating one element at a time.
Adjust for 1-based indexing by decrementing n before calculations.
How is the formula calculated?

nCi = n! / (i! * (n-i)!) : ith element of nth row
nCi+1 = n! / ((i+1)! * (n-(i+1))!) : (i+1)th element of nth row
Dividing (i+1)th element by ith element: nCi+1 / nCi = [n! / ((i+1)! * (n-i-1)!)] / [n! / (i! * (n-i)!)]
Simplifying: nCi+1 = nCi * (n-i) / (i+1) – This lets us compute each element from the previous one



1
# Python program to Find the nth row in Pascal’s
2
# Triangle using efficient approach
3
​
4
# Function to find the elements
5
# of n'th row in Pascal's Triangle
6
def nthRowOfPascalTriangle(n):
7
​
8
    # To follow 0 based indexing, decrement n
9
    n -= 1
10
​
11
    res = []
12
​
13
    # nC0 = 1
14
    prev = 1
15
    res.append(prev)
16
​
17
    for i in range(1, n + 1):
18
​
19
        # nCr = (nCr-1 * (n - r + 1))/r
20
        curr = (prev * (n - i + 1)) // i
21
        res.append(curr)
22
        prev = curr
23
​
24
    return res
25
​
26
if __name__ == "__main__":
27
    n = 4
28
    ans = nthRowOfPascalTriangle(n)
29
​
30
    for val in ans:
31
        print(val, end=" ")
32
    print()

Output
1 3 3 1 

"""






