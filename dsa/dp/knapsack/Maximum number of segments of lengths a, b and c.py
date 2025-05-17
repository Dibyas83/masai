
"""
Given a positive integer N, find the maximum number of segments of lengths a, b and c that can be formed from N .
Examples :


Input : N = 7, a = 5, b, = 2, c = 5
Output : 2
N can be divided into 2 segments of lengths
2 and 5. For the second example,

Input : N = 17, a = 2, b = 1, c = 3
Output : 17
N can be divided into 17 segments of 1 or 8
segments of 2 and 1 segment of 1. But 17 segments
of 1 is greater than 9 segments of 2 and 1.


To understand any DP problem clearly, we need to write first of all its recursive code and then go for optimization.

Recursion-Based Solution:

Here for any value of n, we have 3 possibilities, for making the maximum segment count
if (n >= a) we can make 1 segment of length a + another possible segment from the length of n - a
if (n >= b) we can make 1 segment of length b + another possible segment from the length of n - b
if (n >= c) we can make 1 segment of length c + another possible segment from the length of n - c
so now we have to take the maximum possible segment above in 3 condition
Below is an implementation for the same.




# Python implementation to divide N into maximum
# number of segments of length a, b and c

# Function to find the maximum number
# of segments
def maximumSegments(n, a, b, c):
    # Base case
    if n == 0:
        return 0

    maxa = float('-inf')
    # Conditions

    # Making one segment of length a
    if n >= a:
        maxa = max(maxa,
                   1 + maximumSegments(n - a, a, b, c))
    # Making one segment of length b
    if n >= b:
        maxa = max(maxa,
                   1 + maximumSegments(n - b, a, b, c))
    # Making one segment of length c
    if n >= c:
        maxa = max(maxa,
                   1 + maximumSegments(n - c, a, b, c))

    # Return maximum out of all possible segment
    return maxa

# Driver code
if __name__ == '__main__':
    n = 7
    a = 5
    b = 2
    c = 5

    # Function call
    print(maximumSegments(n, a, b, c))

 # This code is contributed by divyansh2212
Output
2
Time Complexity: O(3n)
Auxiliary Space : O(n)

Optimized Approach : The approach used is Dynamic Programming. The base dp0 will be 0 as initially it has no segments. After that, iterate from 1 to n, and for each of the 3 states i.e, dpi+a, dpi+b and dpi+c, store the maximum value obtained by either using or not using the a, b or c segment.
The 3 states to deal with are :



dpi+a=max(dpi+1, dpi+a);
dpi+b=max(dpi+1, dpi+b);
dpi+c=max(dpi+1, dpi+c);


Below is the implementation of above idea :





# Python implementation
# to divide N into maximum
# number of segments of
# length a, b and c

# function to find
# the maximum number
# of segments
def maximumSegments(n, a, b, c) :

    # stores the maximum
    # number of segments
    # each index can have
    dp = [-1] * (n + 10)

    # 0th index will have
    # 0 segments base case
    dp[0] = 0

    # traverse for all possible
    # segments till n
    for i in range(0, n) :

        if (dp[i] != -1) :

            # conditions
            if(i + a <= n ): # avoid buffer overflow
                dp[i + a] = max(dp[i] + 1,
                            dp[i + a])

            if(i + b <= n ): # avoid buffer overflow
                dp[i + b] = max(dp[i] + 1,
                            dp[i + b])

            if(i + c <= n ): # avoid buffer overflow
                dp[i + c] = max(dp[i] + 1,
                            dp[i + c])

    return dp[n]

# Driver code
n = 7
a = 5
b = 2
c = 5
print (maximumSegments(n, a,
                    b, c))

# This code is contributed by
# Manish Shaw(manishshaw1)
Output
2
Time Complexity: O(N), as we are using a loop to traverse N times.
Auxiliary Space: O(N), as we are using extra space for dp array

"""








