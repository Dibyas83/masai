
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

best running time we can hope to achieve for any algorithm that processes each of n objects that are
not already in the computer’s memory, because reading in the n objects already requires n operations

4 - The next function we discuss in this section is the n-log-n function,
f(n) = nlogn
. This function grows a little more rapidly than the linear function and a lot less rapidly than the
 quadratic function; therefore, we would greatly prefer an algorithm with a running time that is 
 proportional to nlogn, than one with quadratic running time
- the fastest possible algorithms for sorting n arbitrary values require time proportional to nlog n

5 -  quadratic function,
f(n) = n2
That is, given an input value n, the function f assigns the product of n with itself.Many algorithms 
that have nested loops, where the inner loop performs a linear number of operations and  the outer loop
is performed a linear number of times. Thus, in such cases, the algorithm performs n · n = n2 operations

1+2+3 ...n-2 + n-1 + n = n/2 * n  + n = n(n-1)/2

 - A polynomial function has the form,
f(n) = a0 +a1n+a2n^2 +a3n^3 +···+adn^d,
where a0,a1,...,ad are constants, called the coefficients of the polynomial, and
ad = 0. Integer d, which indicates the highest power in the polynomial, is called
the degree of the polynomial
For example, the following functions are all polynomials:
• f(n) = 2+5n+n^2
• f(n) = 1+n^3
• f(n) = 1
• f(n) = n
• f(n) = n^2

- e exponential function,
f(n) = bn,
where b is a positive constant, called the base, and the argument n is the exponent. That is, function 
f(n) assigns to the input argument n the value obtained by mul￾tiplying the base b by itself n times.

256 = 16^2 = (2^4)^2 = 2^4·2 = 28 = 256 (Exponent Rule 1)
• 243 = 3^5 = 3^2+3 = 3^2*3^3 = 9 · 27 = 243 (Exponent Rule 2)
• 16 = 1024/64 = 2^10/2^6 = 2^(10−6) = 24 = 16 (Exponent Rule 3)

Geometric Sums
Suppose we have a loop for which each iteration takes a multiplicative factor longer
than the previous one
For any integer n ≥ 0 and any real number a such that a > 0 and
a!= 1, consider the summation

  (a^(n+1) −1)/a−1 = 1+a+a^2 +···+a^n

(a + a2 + a3 + a4 + a5)*a3/a3
(a-2 + a-1 + 1 + a1 + a2)*a3/a3
1+4+16+64+256+1024 = (4^5)/(4-1)  -1   + 4^5
1+3+9+27+81+243
1+2+4+8+16+32

The Ceiling and Floor Functions
One additional comment concerning the functions above is in order. When dis￾cussing logarithms, we noted 
that the value is generally not an integer,yet therunning time of an algorithm is usually expressed by means
of an integer quantity,such as the number of operations performed. Thus, the analysis of an algorithm
may sometimes involve the use of the floor function and ceiling function, which
are defined respectively as follows:
• [x] = the largest integer less than or equal to x.
• [x] = the smallest integer greater than or equal to x.

-------------------------------------------
f(n) ≤ c · g(n) when n ≥ n0

By the big-Oh definition, we need to find a real constant c > 0 and
an integer constant n0 ≥ 1 such that 8n+5 ≤ cn for every integer n ≥ n0. It is easy
to see that a possible choice is c = 9 and n0 = 5. Indeed, this is one of infinitely
many choices available because there is a trade-off between c and n0. For example,
we could rely on constants c = 13 and n0 = 1.

The big-Oh notation allows us to say that a function f(n) is “less than or equal
to” another function g(n) up to a constant factor and in the asymptotic sense as n
grows toward infinity

: 5n2 +3nlogn+2n+5 is O(n2).
Justification: 5n^2 +3nlogn+2n+5 ≤ (5+3+2+5)n^2 = cn2, for c = 15, when
n ≥ n0 = 1.
Example 3.11: 20n3 +10nlog n+5 is O(n3).
Justification: 20n3 +10nlogn+5 ≤ 35n3, for n ≥ 1.
Example 3.12: 3log n+2 is O(logn).
Justification: 3logn+ 2 ≤ 5logn, for n ≥ 2. Note that logn is zero for n = 1.
That is why we use n ≥ n0 = 2 in this case.
Example 3.13: 2n+2 is O(2n).
Justification: 2n+2 = 2n ·22 = 4·2n; hence, we can take c = 4 and n0 = 1 in this
case.
Example 3.14: 2n+100log n is O(n).
Justification: 2n+100log n ≤ 102n, for n ≥ n0 = 1; hence, we can take c = 102 in this case


 Big-Omega “greater than or equal to”

: 3nlog n−2n is Ω(nlog n).
Justification: 3nlog n− 2n = nlog n+ 2n(logn− 1) ≥ nlogn for n ≥ 2; hence,
we can take c = 1 and n0 = 2 in this case.

Big-Theta
In addition, there is a notation that allows us to say that two functions grow at the
same rate, up to constant factors. We say that f(n) is Θ(g(n)), pronounced “ f(n)
is big-Theta of g(n),

3nlog n+4n+5logn is Θ(nlog n).
Justification: 3nlogn ≤ 3nlog n+4n+5logn ≤ (3+4+5)nlogn for n ≥ 2
----------------------------------------

Constant-Time Operations
Given an instance, named data, of the Python list class, a call to the function,len(data), is evaluated in 
constant time. This is a very simple algorithm becausethe list class maintains, for each list, an instance 
variable that records the current length of the list. This allows it to immediately report that length,
rather than take time to iteratively count each of the elements in the list. Using asymptotic notation,
we say that this function runs in O(1) time

Python’s lists are implemented as array-based sequences, references to a list’s elements are stored in a
consecutive block of memory. The jth element of the list can be found,not by iterating through the list 
one element at a time, but by validating the index,and using it as an offset into the underlying array

If the sequence is given to us in random order, the probability that the jth element is the largest of the
first j elements is 1/ j (assuming uniqueness). Hence, the expected number of times we update the biggest 
(including initialization) is Hn = ∑n j=1  1/ j, which is known as the nth Harmonic number. It turns out 
(see Proposition B.16) that Hn is O(logn).Therefore, the expected number of times the biggest value is
updated by find max on a randomly ordered sequence is O(logn).

-------
Prefix Averages
The next problem we consider is computing what are known as prefix averages
of a sequence of numbers  A[ j] = ∑j i=0 S[i]/(j +1) .
Computing prefix averages has many applications in economics and statistics. For
example, given the year-by-year returns of a mutual fund, ordered from recent to
past, an investor will typically want to see the fund’s average annual returns

1 - It computes every element of A separately, using an inner
loop to compute the partial sum.

2-Even though the ex￾pression, sum(S[0:j+1]), seems like a single command, it is a function call and
an evaluation of that function takes O(j + 1) time in this context. Technically, the
computation of the slice, S[0:j+1], also uses O(j + 1) time, as it constructs a new
list instance for storage. So the running time of prefix average2 is still dominated
by a series of steps that take time proportional to 1+2+3+···+n, and thus O(n2)

3- In our first two algorithms, the prefix sum is computed anew for each value of j.That 
contributed O(j) time for each j,leading to the quadratic behavior.the running time of prefix average3 is O(n


"""
#1
def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0]*n # create new list of n zeros
    for j in range(n):
        total = 0 # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1) # record the average
    return A
#running time of prefix average1 is O(n^2)

#2
def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]"""
    n = len(S)
    A = [0]*n # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1) # record the average
    return A
#3
def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]"""
    n = len(S)
    A = [0]*n # create new list of n zeros
    total = 0 # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j] # update prefix sum to include S[j]
        A[j] = total / (j+1) # compute average based on current sum
    return A

#-----------------The three-way set disjointness
# problem is to determine if the intersection of the three sequences is empty, namely,
# that there is no element x such that x ∈ A, x ∈ B, and x ∈ C
def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False # we found a common value
    return True # if we reach this, sets are disjoint
#If each of the original sets has size n, then the worst-case running time of this function is O(n3).

"""
The test a == b is evaluated O(n2) times.
The rest of the time spent depends upon how many matching (a,b) pairs exist. As
we have noted, there are at most n such pairs, and so the management of the loop
over C, and the commands within the body of that loop, use at most O(n2) time.
By our standard application of Proposition 3.9, the total time spent is O(n2).
"""
def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False # we found a common value
    return True
#----------------
"""
Element Uniqueness
A problem that is closely related to the three-way set disjointness problem is the
element uniqueness problem. In the former, we are given three collections and we presumed that there were no
duplicates within a single collection. In the element uniqueness problem, we are given a single sequence S with
n elements and asked whether all elements of that collection are distinct from each other.Code Fragment 3.7, 
solves the element uniqueness problem by looping through all distinct pairs of indices j < k,checking if any of
those pairs refer to elements that are equivalent to each other. It does this using two
nested for loops, such that the first iteration of the outer loop causes n−1 iterations
of the inner loop, the second iteration of the outer loop causes n − 2 iterations of
the inner loop, and so on. Thus, the worst-case running time of this function is
proportional to
(n−1)+(n−2) +···+2+1,
which we recognize as the familiar O(n2) summation from Proposition 3.3

"""
def unique1(S):
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False # found duplicate pair
    return True

"""
An even better algorithm for the element uniqueness problem is based on using sorting as a problem-solving
tool. In this case, by sorting the sequence of elements,we are guaranteed that any duplicate elements will be 
placed next to each other.Thus,to determine if there are any duplicates,all we need to do is perform a single
pass over the sorted sequence, looking for consecutive duplicate.Once the data is sorted, the subsequent loop 
runs in O(n) time, and so the entire unique2 algorithm runs in O(nlogn) time
"""
def unique2(S):
    """Return True if there are no duplicate elements in sequence S."""
    temp = sorted(S) # create a sorted copy of S
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False # found duplicate pair
    return True

























