"""
Logarithmic time complexity, denoted as O(log n), means the runtime of an algorithm increases very slowly as the input size grows. It's characterized by a runtime that's proportional to the logarithm of the input size. This makes algorithms with O(log n) time complexity highly efficient, especially for large datasets.
Key characteristics of logarithmic time complexity:
Slow Growth:
The runtime increases much slower than linear or quadratic time complexities as the input size increases.
Halving Input:
Algorithms with O(log n) often involve halving the input size in each step, such as in binary search.
Divide and Conquer:
These algorithms often employ divide-and-conquer strategies, breaking down problems into smaller subproblems.
Examples:
Binary search, searching for a term in a binary search tree, and operations on heaps often exhibit O(log n) time complexity.
Why is it efficient?
Large Datasets:
O(log n) algorithms are highly efficient for large datasets because the increase in runtime is minimal as the input size grows.
Binary Search:
The classic example of O(log n) is binary search, which repeatedly halves the search space until the target element is found.
"""

"""
Note: An exponential function is the exact opposite of a logarithmic function. When a value is being multiplied repeatedly it is said to grow exponentially whereas when the value is being divided repeatedly it is said to grow logarithmically.

Different Types of Logarithmic Complexities
Now that we know what is a logarithm, let’s deep dive into different types of logarithmic complexities that exists, such as:

Simple Log Complexity (Loga b)
Simple logarithmic complexity refers to log of b to the base a. As mentioned, it refers to the time complexity in terms of base a. In design and analysis of algorithms, we generally use 2 as the base for log time complexities. The below graph shows how the simple log complexity behaves.

Simple Log Complexity (Log(a) b)
Simple Log Complexity (Log(a) b)

 There are several standard algorithms that have logarithmic time complexity:

Merge sort
Binary search
Heap sort
Double Logarithm (log log N)
Double logarithm is the power to which a base must be raised to reach a value ‘x’ such that when the base is raised to a power ‘x’ it reaches a value equal to given number.

Double Logarithm (log log N)
Double Logarithm (log log N)

Example:

logarithm (logarithm (256)) for base 2 = log2(log2(256)) = log2(8) = 3. 


Explanation: 28 = 256, Since 2 needs to be raised to a power of 8 to give 256, Thus logarithm of 256 base 2 is 8. Now 2 needs to be raised to a power of 3 to give 8 so log2(8) = 3.


N logarithm N (N * log N)
N*logN complexity refers to product of N and log of N to the base 2. N * log N time complexity is generally seen in sorting algorithms like Quick sort, Merge Sort, Heap sort. Here N is the size of data structure (array) to be sorted and log N is the average number of comparisons needed to place a value at its right place in the sorted array. 

N * log N
N * log N

logarithm2 N (log2 N)
log2 N complexity refers to square of log of N to the base 2. 

log2 N
log2 N

N2 logarithm N (N2 * log N)
N2*log N complexity refers to product of square of N and log of N to the base 2. This Order of time complexity can be seen in case where an N * N * N 3D matrix needs to be sorted along the rows. The complexity of sorting each row would be N log N and for N rows it will be N * (N * log N). Thus the complexity will be N2 log N,

N2 * log N
N2 * log N

N3 logarithm N (N3 log N)
N3*log N complexity refers to product of cube of N and log of N to the base 2. This Order of time complexity can be seen in cases where an N * N matrix needs to be sorted along the rows. The complexity of sorting each row would be N log N and for N rows it will be N * (N * log N) and for N width it will be N * N * (N log N). Thus the complexity will be N3 log N,

N3 log N
N3 log N

logarithm √N (log √N)
log √N complexity refers to log of square root of N to the base 2.

log √N
log √N

Examples To Demonstrate Logarithmic Time Complexity
Example 1: loga b
Task: We have a number N which has an initial value of 16 and the task is to reduce the given number 
to 1 by repeated division of 2. 
Approach:

Initialize a variable number_of_operation with a value 0 .
Run a for loop from N till 1.
In each iteration reduce the value of N to half.
Increment the number_of_operation variable by one.
Return the number_of_operation variable.

"""

if __name__ == "__main__":

    N = 16
    number_of_operations = 0
    print("Logarithmic reduction of N: ", end="")
    i = N
    while (i > 1):
        print(i, end=" ")
        number_of_operations += 1
        i = i // 2

    print()
    print("Algorithm Runtime for reducing N to 1:", number_of_operations)

"""
Example 2: Binary search algorithm (log N)
Linearly Searching a value in an array of size N can be very hectic, even when the array is sorted but
using binary search this can be done in a lot easier way and in lesser time as the algorithm reduces the 
search space by half in each operation thus gives a complexity of log2(N), Here base is 2 because process 
repeatedly reduces to half. 

Consider an array Arr[] = {2, 4, 6, 8, 10, 12, 14, 16, 18}, If it is required to find the index of 8 then 
the algorithm will work as following:
"""
print("---------------------index")

# Python program for finding the index of 8

def find_position(val, Arr, n):
    global steps
    l = 0
    r = n - 1

    while (l <= r):
        steps += 1
        m = l + (r - l) // 2
        if (Arr[m] == val):
            return m
        elif (Arr[m] < val):
            l = m + 1
        else:
            r = m - 1

    return -1


# Driver code
Arr = [2, 4, 6, 8, 10, 12, 14, 16,20,22,33,37,51]
steps = 0

#  Function Call
idx = find_position(14, Arr, 13)

print("8 was present on index: {0}".format(idx))

#  Since the worst case runtime of Binary search is
# log(N) so the count of steps must be less than log(N)
print("Algorithm Runtime: {0}".format(steps))

# This code is contributed by Pushpesh Raj.

"""
Example 3: Binary search algorithm (log log N)
An example where the time complexity of algorithm is Double logarithmic along with a length factor N is
when prime numbers from 1 to N need to be found.
"""
import math

MAX_SIZE = 1000001

# isprime[]: isprime[i] is True if number is prime
# prime[]: stores all prime numbers less than N
# SPF[] that store smallest prime factor of number
# [for Exp: smallest prime factor of '8' and '16'
# is '2' so we put SPF[8] = 2, SPF[16] = 2]
isprime = [True] * MAX_SIZE
prime = []
SPF = [0] * MAX_SIZE

# Function generate all prime numbers less than N in O(n)
def manipulated_seive(N):
    global isprime, prime, SPF

    # 0 and 1 are not prime
    isprime[0] = isprime[1] = False

    # Fill rest of the entries
    for i in range(2, N):
        # If isprime[i] is True then i is prime number
        if isprime[i]:
            # put i into prime[] list
            prime.append(i)

            # A prime number is its own smallest prime factor
            SPF[i] = i

        # Remove all multiples of i*prime[j] which are
        # not prime by making isprime[i*prime[j]] = False
        # and put the smallest prime factor of i*Prime[j] as
        # prime[j] [for example: let i = 5, j = 0, prime[j]
        # = 2 [i*prime[j] = 10] so the smallest prime factor
        # of '10' is '2' that is prime[j]] this loop runs
        # only one time for numbers which are not prime
        j = 0
        while j < len(prime) and i * prime[j] < N and prime[j] <= SPF[i]:
            isprime[i * prime[j]] = False

            # put the smallest prime factor of i*prime[j]
            SPF[i * prime[j]] = prime[j]

            j += 1

# Driver program to test above function
if __name__ == "__main__":
    N = 13 # Must be less than MAX_SIZE

    manipulated_seive(N)

    # Print all prime numbers less than N
    for i in range(len(prime)):
        if prime[i] <= N:
            print(prime[i], end=" ")
        else:
            break














