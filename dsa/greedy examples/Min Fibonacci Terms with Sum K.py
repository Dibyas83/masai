

"""

Minimum Fibonacci terms with sum equal to K
Last Updated : 11 Feb, 2025
Given a number k, the task is to find the minimum number of Fibonacci terms (including repetitions) whose sum equals k.
Note: You may use any Fibonacci number multiple times.

Examples:

Input: k = 7
Output: 2
Explanation: Possible ways to sum up to 7 using Fibonacci numbers:
5 + 2 = 7 (2 terms)
3 + 3 + 1 = 7 (3 terms)
2 + 2 + 2 + 1 = 7 (4 terms)
The minimum number of terms is 2, using 5 + 2.

Input: k = 13
Output: 1
Explanation: Possible ways to sum up to 13 using Fibonacci numbers:
13 = 13 (1 term)
8 + 5 = 13 (2 terms)
Using 13 directly gives the minimum number of terms, which is 1.


Like Binary Representation where we represent every number as sum of powers of 2, we can represent every every number as sum of Fibonacci Numbers. For example: 19 = 13+5+1. This is known as a Zeckendorf Representation. For example, to get n, we can n times add 1. Here we need to minimize the count of Fibonacci numbers that contribute to sum. So this problem is basically coin change problem with coins having Fibonacci values. By taking some examples, we can notice that With Fibonacci coin values Greedy approach works.

Firstly we calculate Fibonacci terms till less than or equal to k. then start from the last term and keep subtracting that term from k until k >(nth term). Also along with this keep increasing the count of the number of terms.


Below is the implementation of the above approach:




1
# Python implementation to find the minimum number
2
# of Fibonacci terms required to sum up to k
3
​
4
def minimumFibonacciTerms(k):
5
    fib = [1, 1]
6
​
7
    # Generate Fibonacci numbers up to k
8
    while fib[-1] < k:
9
        fib.append(fib[-1] + fib[-2])
10
​
11
    count = 0
12
​
13
    # Start from the largest Fibonacci number
14
    for i in range(len(fib) - 1, -1, -1):
15

16
        # Use the largest possible Fibonacci number
17
        while k >= fib[i]:
18
            k -= fib[i]
19
            count += 1
20
​
21
    return count
22
​
23
if __name__ == "__main__":
24

25
    k = 7
26

27
    print(minimumFibonacciTerms(k))

Output
2
"""













