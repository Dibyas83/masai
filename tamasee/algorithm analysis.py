
"""
a data structure is a systematic way of organizing and access￾ing data, and an algorithm is a step-by-step procedure
for performing some task in a finite amount of time focus on the relationship between the running time of an
algorithm and the size of its input. We are interestedin characterizing an algorithm’s running time as a function
of the input size

The time function measures relative to what is known as the “wall clock.” Because many processes share use of a
computer’s central processing unit (or CPU), the elapsed time will depend on what other processes are running on
the computer when the test is performed. A fairer metric is the number of CPU cycles that are used by the algorithm.
This can be determined using the clock function of the time module, but even this measure might not be consistent if
repeating the identical algorithm on the identical input, and its granularity will depend upon the computer
system. Python includes a more advanced module, named timeit, to help automate such evaluations with repetition to
account for such variance among trials.


"""

from time import time
start_time = time( ) # record the starting time
#run algorithm
end_time = time( ) # record the ending time
elapsed = end_time - start_time # compute the elapsed time

"""
for the remainder of this book, unless we specifyotherwise, we will characterize running times in terms of the 
worst case, as a func￾tion of the input size, n, of the algorithm

we briefly discuss the seven most important functions used in the
analysis of algorithms.

1 -The simplest function we can think of is the constant function
In other words, it does not matter what the value of n is; f(n) will always be equal to the constant value c

, the most fundamental con￾stant function is g(n) = 1, and this is the typical constant function we use in this
book. Note that any other constant function, f(n) = c, can be written as a constant
c times g(n). That is, f(n) = cg(n) in this case.

2-logarithm function f(n) = logb n, for some constant b > 1. This function is defined as follows:
        x = logb n if and only if bx = n.
By definition, logb 1 = 0. The value b is known as the base of the logarithm.
e most common base for the logarithm function in computer science is 2,
as computers store integers in binary, and because a common operation in many
algorithms is to repeatedly divide an input in half. In fact, this base is so common
that we will typically omit it from the notation when it is 2. That is, for us,
        logn = log2 n

Computing the logarithm function exactly for any integer n involves the use
of calculus, but we can use an approximation that is good enough for our pur￾poses without calculus.
For example, the evaluation of 
log3 27 is 3,
because ((27/3)/3)/3 = 1. Likewise, 
log4 64 is 3, because ((64/4)/4)/4 = 1,
and 
log2 12 is 4, because (((12/2)/2)/2)/2 = 0.75 ≤ 1

following proposition describes several important identities that involve
logarithms for any base greater than 1.
Proposition 3.1 (Logarithm Rules): Given real numbers a > 0, b > 1, c > 0
and d > 1, we have:
1. logb(ac) = logb a+logb c         =log2 4*16=6         log2 4=2    log2 16=4
2. logb(a/c) = logb a−logb c
3. logb(a^c) = clogb a
4. logb a = logd a/logd b           =log4 64            log2 64 / log2 4   
5. b^logd a = a^logd b   -8^log2 16=8^4=2^12    16^log2 8=16^3=2^12
applications-
• log(2n) = log2+logn = 1+logn, by rule 1
• log(n/2) = logn−log2 = logn−1, by rule 2
• log n3 = 3log n, by rule 3
• log 2n = nlog 2 = n · 1 = n, by rule 3
• log4 n = (logn)/log 4 = (logn)/2, by rule 4
• 2log n = nlog 2 = n1 = n, by rule 5.

3-  linear function,
f(n) = n.
That is, given an input value n, the linear function f assigns the value n itself.
This function arises in algorithm analysis any time we have to do a single basic
operation for each of n elements. For example, comparing a number x to each
element of a sequence of size n will require n comparisons

e best running time we can hope to achieve for any algorithm that
processes each of n objects that are not already in the computer’s memory, because
reading in the n objects already requires n operations





"""












