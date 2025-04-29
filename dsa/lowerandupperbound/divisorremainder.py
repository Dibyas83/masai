"""

Find minimum x such that (x % k) * (x / k) == n
Last Updated : 07 Mar, 2023
Given two positive integers n and k. Find minimum positive integer x such that the (x % k) * (x / k) == n, where % is the modulus operator and / is the integer division operator.
Examples:

Input : n = 4, k = 6
Output :10
Explanation : (10 % 6) * (10 / 6) = (4) * (1) = 4 which is equal to n

Input : n = 5, k = 5
Output : 26
Naive Solution: A simple approach is to run a while loop until we find a solution that satisfies the given equation, but this would be very slow.
Efficient Solution: The key idea here is to notice that the value of (x % k) lies in the range [1, k – 1]. (0 is not included, since we can’t divide n by (x % k) when it is zero). Now, we need to find the largest possible number in the range that divides n and hence the given equation becomes x = (n * k) / (x % k) + (x % k).
Note : (x % k) is added to the answer since for the current value of modulus (x % k), it must not be contradicting that on one hand x is such that the remainder upon dividing by k is (x % k) and on the other x is (n * k) / (x % k) whose remainder is simply zero when we divide this value by k.

Steps to solve the problem:

 Initialize a variable ans to the maximum integer value.
Iterate over all possible remainders from k-1 to 1 using a for loop with a decrementing step size.
 If the remainder divides n, calculate the cost of cutting the ribbon into pieces of length k or shorter as rem + (n / rem) * k and 4.    store it in the ans variable.
 return the minimum value of ans.
Below is the implementation of the above approach.




# Python 3 program to find the minimum positive
# x such that the given equation holds true

# This function gives the required answer
def minimumX(n, k):


    ans = 10 ** 18

    # Iterate over all possible remainders
    for i in range(k - 1, 0, -1):
        if n % i == 0:
            ans = min(ans, i + (n / i) * k)
    return ans

# Driver Code
n, k = 4, 6

print(minimumX(n, k))

n, k = 5, 5

print(minimumX(n, k))

# This code is contributed
# by Mohit Kumar
Output:
10
26
"""