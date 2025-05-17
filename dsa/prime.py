"""
Prime and Composite Numbers
Last Updated : 14 Oct, 2024
Prime and Composite Numbers are commonly used classifications of Natural Numbers based on divisibility. A prime number is divisible by only 1 and itself and a composite number is divisible by one or two more other Every natural number, except 0 or 1, is either prime or composite.

Table of Content

Prime Numbers vs Composite Numbers
Prime and Composite Numbers Chart
Tests for Prime and Composite numbers
Important Facts about Prime and Compsite Numbers
Practice Questions on Prime and Composite Numbers
Prime Numbers vs Composite Numbers
The following table lists five differences between a prime and composite number:

Prime Numbers	Composite Numbers
All the natural numbers greater than 1 that have only two factors - one and the number itself are called prime numbers.	All natural numbers that can be expressed as a product of at least two smaller natural numbers are known as composite numbers.
Prime numbers have exactly two factors - 1 and the number itself.	Composite numbers have at least 3 or more factors.
All the prime numbers except 2 are odd numbers.	There is no such pattern for composite numbers. They can be odd or even both.
Their prime factorization has only one prime factor i.e., the number itself.	Their prime factorization has one or more other prime factors. For example, 49 has a prime factor of 7 and
The product of two prime numbers is a composite number

The product of two composite numbers is also a composite number

Examples: 2, 3, 5, 7, ...	Examples: 4, 6, 8, 9, 10, ...
Prime and Composite Numbers Chart
A prime and composite numbers chart is a table that lists all the numbers from 1 to 100 and identifies them as either prime or composite. Here is the prime and composite numbers chart

Prime-and-Composite-Numbers
Tests for Prime and Composite numbers
We can use below quick steps.

If the given number is 0 or 1, then it is neither prime not composite.
If a number is even and not 2, then it is composite
For other cases, a simple way is to find all divisors of a given number and check if the divisors are other than 1 and the number itself. If there are other, then the number is composite, else prime.
Also Check:

Prime and Composite Numbers Calculator
Different methods to check if a number is prime
Important Facts about Prime and Compsite Numbers
The number 2 is the only even prime number. All other even numbers can be divided by 2, making them composite. This uniqueness makes 2 particularly interesting in number theory​.
Twin primes are pairs of prime numbers that differ by 2, such as (3, 5) and (11, 13). It is conjectured that there are infinitely many twin primes, although this has yet to be proven​
The product of two prime numbers is always a composite number.
All other prime numbers, with the exception of two and three, are either 6n+1 or 6n-1
The smallest composite number is 4, as it can be divided by 1, 2, and 4. Every composite number can be factored into prime numbers
All even numbers greater than 2 are composite, as they can be divided by 2. This property highlights a simple way to identify composite numbers within a specific range.
Every composite number can be expressed as a product of prime numbers in a unique way (up to the order of factors), which is known as its prime factorization.
Read More:

Interesting Facts about Prime Numbers
Real Life Applications of Composite Numbers
Real Life Applications of Prime Numbers
Practice Questions on Prime and Composite Numbers
Here are some practice questions/problems based on prime and composite numbers:

1. Is 1 a composite number?

2. Check whether 23 is a prime number.

3. Check whether 56 is a prime number.

4. Check whether 2779 is a prime number. (Hint: Use Efficient Primarility Test)

5. Use Eratosthenes sieve to find all the prime numbers from 1 to 100.

6. Find the prime factors of 69.

AI
Here's how to find the prime factors of a composite number using Python:
Python

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

number = 123456
result = prime_factors(number)
print(f"The prime factors of {number} are: {result}")
This code works by:
Initializing an empty list factors to store the prime factors.
Starting with the smallest prime number, 2, and checking if it divides the input number n.
If it does, the code appends d to the factors list and divides n by d.
If d no longer divides n the code increments d and repeats steps 2 and 3.
The process continues until d * d is greater than n.
If n is still greater than 1, it means that n itself is a prime number, so it's appended to the factors list.
Finally, the function returns the factors list

"""

"""
geeks

Python Program for Efficient program to print all prime factors of a given number
Last Updated : 16 May, 2023
Given a number n, write an efficient function to print all prime factors of n. 

For example, if the input number is 12, then output should be "2 2 3". And if the input number is 315, then output should be "3 3 5 7". Following are the steps to find all prime factors. 

1) While n is divisible by 2, print 2 and divide n by 2. 

2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i, increment i by 2 and continue. 

3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2. 
"""
# Python program to print prime factors

import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i)
            n = n // i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


# Driver Program to test above function

n = 315
primeFactors(n)

# This code is contributed by Harshit Agrawal
# Code Improved by Sarthak Shrivastava

"""
Output:

3 3 5 7
Time complexity: O(sqrt(n))
Auxiliary space: O(1)

How does this work? 

The steps 1 and 2 take care of composite numbers and step 3 takes care of prime numbers. To prove that the complete algorithm works, we need to prove that steps 1 and 2 actually take care of composite numbers. This is clear that step 1 takes care of even numbers. And after step 1, all remaining prime factor must be odd (difference of two prime factors must be at least 2), this explains why i is incremented by 2. 

Now the main part is, the loop runs till square root of n not till n. 

To prove that this optimization works, let us consider the following property of composite numbers. 

Every composite number has at least one prime factor less than or equal to square root of itself. 

This property can be proved using counter statement. Let a and b be two factors of n such that a*b = n. If both are greater than √n, then a.b > √n, * √n, which contradicts the expression "a * b = n".

 In step 2 of the above algorithm, we run a loop and do following in loop 

a) Find the least prime factor i (must be less than √n,) 

b) Remove all occurrences i from n by repeatedly dividing n by i. 

c) Repeat steps a and b for divided n and i = i + 2. The steps a and b are repeated till n becomes either 1 or a prime number. Please refer complete article on Efficient program to print all prime factors of a given number for more details!

Approach#2: Using Sieve of Eratosthenes
This approach prints all the prime factors of a given number 'n'. It first initializes an array 'spf' with indices from 0 to n+1 with values set to 0. It then assigns the value of 'i' to the corresponding index in the array for all 'i' from 2 to n. For even numbers, the value of 2 is assigned to the corresponding index in the array. Then, for all odd numbers 'i' from 3 to the square root of 'n', the array index 'spf[i]' is checked, and if it equals to 'i', then all multiples of 'i' in the range from 'i*i' to 'n' are checked and their corresponding array values are set to 'i'. Finally, the prime factors of the given number are printed using the array 'spf'.

Algorithm
1. Create a boolean array "prime[0..n]" and initialize all entries it as true.
2. Mark all the multiples of 2, 3, 5, ..., sqrt(n) as not prime. Here, instead of marking, we store the smallest prime factor for every composite number.
3. Traverse the array from smallest prime factor of i to sqrt(n) while i divides n. The smallest prime factor of n will be a prime factor.
4. If n is a prime number and greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2.

"""


def primeFactors(n):
    spf = [0 for i in range(n + 1)]
    spf[1] = 1
    for i in range(2, n + 1):
        spf[i] = i
    for i in range(4, n + 1, 2):
        spf[i] = 2

    for i in range(3, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i

    while n != 1:
        print(spf[n], end=" ")
        n = n // spf[n]


# example usage
n = 315
primeFactors(n)


"""
Output
3 3 5 7 
Time Complexity: O(n*log(log(n)))
Space Complexity: O(n)

Approach#3: Using anonymous function

The approach uses anonymous function to generate all prime factors of a given number. It then uses a while loop and for loop to repeatedly call the function and append the factors to a list until the given number n is reduced to 1. Finally, it prints the prime factors of n separated by a space.

Algorithm
1. Define an anonymous function prime_factors that takes a positive integer n as input and generates all prime factors of n.
2. Initialize an empty list factors.
3. Use a while loop to repeatedly call the prime_factors function and append the factors to factors until n is reduced to 1.
4. Inside the while loop, use a for loop to iterate over the prime factors of n generated by the prime_factors function.
5. Append each factor to factors and update n by dividing it by the factor.
6. Print the prime factors of n separated by a space using the print function with the * operator to unpack the list of factors as arguments.
"""
# Using anonymous function
prime_factors = lambda n: [i for i in range(2, n+1) if n%i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))]
n = 315
factors = []
while n > 1:
    for factor in prime_factors(n):
        factors.append(factor)
        n //= factor
print(*factors)



"""
Output
3 5 7 3
Time complexity: O(n^1.5)
Auxiliary Space: O(n) or O(log n)


"""









