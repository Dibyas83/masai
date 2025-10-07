
"""
s, Archimedes could dip the crown and an equal-weight amount of gold into a bowl of water to see if they both
displaced the same amount. This discovery was unfortunate for the goldsmith, however, for when Archimedes did
his analysis, the crown displaced more water than an equal-weight lump of pure gold, indicating that the crown
was not, in fact, pure gold

a data structure is a systematic way of organizing and access￾ing data, and an algorithm is a step-by-step procedure
for performing some task in a finite amount of time focus on the relationship between the running time of an
algorithm and the size of its input. We are interestedin characterizing an algorithm’s running time as a function
of the input size

The time function measures relative to what is known as the “wall clock.” Because many processes share use of a
computer’s central processing unit (or CPU), the elapsed time will depend on what other processes are running on
the computer when the test is performed. A fairer metric is the number of CPU cycles that are used by the algorithm.
This can be determined using the clock function of the time module, but even this measure might not be consistent if
repeating the identical algorithm on the identical input, and its granularity will depend upon the computer
system. Python includes a more advanced module, named  ** timeit ** ,to help automate such evaluations with repetition to
account for such variance among trials.


"""

from time import time
start_time = time( ) # record the starting time
#run algorithm
end_time = time( ) # record the ending time
elapsed = end_time - start_time # compute the elapsed time

"""
visualize the results by plotting
the performance of each run of the algorithm as a point with x-coordinate equal to
the input size, n, and y-coordinate equal to the running time, t. Figure 3.1 displays
such hypothetical data. This visualization may provide some intuition regarding
the relationship between problem size and execution time for the algorithm. This
may lead to a statistical analysis that seeks to fit the best function of the input size
to the experimental data. To be meaningful, this analysis requires that we choose
good sample inputs and test enough of them to be able to make sound statistical
claims about the algorithm’s running time.

perform an analysis directly on a high-level description of the algorithm (either in
the form of an actual code fragment, or language-independent pseudo-code). We
define a set of primitive operations such as the following:
• Assigning an identifier to an object
• Determining the object associated with an identifier
• Performing an arithmetic operation (for example, adding two numbers)
• Comparing two numbers
• Accessing a single element of a Python list by index
• Calling a function (excluding operations executed within the function)
• Returning from a function.
Formally, a primitive operation corresponds to a low-level instruction with an exe￾cution time that is constant

for the remainder of this book, unless we specifyotherwise, we will characterize running times in terms of the 
worst case, as a func￾tion of the input size, n, of the algorithm

we briefly discuss the seven most important functions used in the
analysis of algorithms.

1 -The simplest function we can think of is the constant function   f(n) = c
In other words, it does not matter what the value of n is; f(n) will always be equal to the constant value c

, the most fundamental con￾stant function is g(n) = 1, and this is the typical constant function we use in this
book. Note that any other constant function, f(n) = c, can be written as a constant
c times g(n). That is, f(n) = cg(n) in this case.

2-logarithm function f(n) = logb n, for some constant b > 1. This function is defined as follows:
        x = logb n if and only if b^x = n.
By definition, logb 1 = 0. The value b is known as the base of the logarithm.

We note that most handheld calculators have a button marked LOG, but this is
typically for calculating the logarithm base-10, not base-two

e most common base for the logarithm function in computer science is 2,
as computers store integers in binary, and because a common operation in many
algorithms is to repeatedly divide an input in half. In fact, this base is so common
that we will typically omit it from the notation when it is 2. That is, for us,
        logn = log2 n

Computing the logarithm function exactly for any integer n involves the use
of calculus, but we can use an approximation that is good enough for our pur￾poses without calculus.
ceiling -logb n For positive integer,n, this value is equal to the number of times we can divide n by b before we get
a number less than or equal to 1.
For example, the evaluation of 
log3 27 =  3,
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
4. logb a = logd a/logd b           =log4 64 =3           log2 64 / log2 4   =6/2=3
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
is performed a linear number of times. Thus, in such cases, the algorithm performs n · n = n^2 operations
also arise in the context of nested loops where the first iteration of a loop uses one operation, the second 
uses two operations, the third uses three operations, and so on
1+2+3 ...n-2 + n-1 + n = n/2 * n  + n =(n+1 ,(n-1)+2,(n-2) + 3, .....)= n(n+1)/2

6 - cubic function f(n) = n3

7- Most of the functions we have listed so far can each be viewed as being part of a
larger class of functions, the polynomials. A polynomial function has the form,

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

8 - e exponential function,
f(n) = bn,
where b is a positive constant, called the base, and the argument n is the exponent. That is, function 
f(n) assigns to the input argument n the value obtained by mul￾tiplying the base b by itself n times.
If we have a loop that starts by performing one operation and then doubles the number of operations performed with 
each iteration, then the number of operations performed in the nth iteration is 2n.

256 = 16^2 = (2^4)^2 = 2^4·2 = 28 = 256 (Exponent Rule 1)
• 243 = 3^5 = 3^2+3 = 3^2*3^3 = 9 · 27 = 243 (Exponent Rule 2)
• 16 = 1024/64 = 2^10/2^6 = 2^(10−6) = 2^4 = 16 (Exponent Rule 3)

Geometric Sums
Suppose we have a loop for which each iteration takes a multiplicative factor longer
than the previous one
For any integer n ≥ 0 and any real number a such that a > 0 and
a!= 1, consider the summation

  (a^(n+1) −1)/a−1 = 1+a+a^2 +···+a^n
1+2+4+8+···+2^(n−1) = 2^(n −1)

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

 Thus,
we can perform an analysis of an algorithm by estimating the number of primitive
operations executed up to a constant factor, rather than getting bogged down in
language-specific or hardware-specific analysis of the exact number of operations
that execute on the computer
The big-Oh notation allows us to say that a function f(n) is “less than or equal
to” another function g(n) up to a constant factor and in the asymptotic sense as n
grows toward infinity


def find max(data):
”””Return the maximum element from a nonempty Python list.”””
 biggest = data[0] # The initial value to beat
 for val in data: # For each value:
 if val > biggest # if it is greater than the best so far,
 biggest = val # we have found a new best (so far)
 return biggest # When loop ends, biggest is the max

This is a classic example of an algorithm with a running time that grows pro￾portional to n, as the loop executes once for each data element, with some fixed
number of primitive operations executing for each pass


: 5n2 +3nlogn+2n+5 is O(n2).
Justification: 5n^2 +3nlogn+2n+5 ≤ (5+3+2+5)n^2 = cn^2, for c = 15, when
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


 Big-Omega
Just as the big-Oh notation provides an asymptotic way of saying that a function is
“less than or equal to” another function, the following notations provide an asymp￾totic way of saying that a function grows at a rate that is “greater than or equal to”
that of another.

: 3nlog n−2n is Ω(nlog n).
Justification: 3nlog n− 2n = nlog n+ 2n(logn− 1) ≥ nlogn for n ≥ 2; hence,
we can take c = 1 and n0 = 2 in this case.

Big-Theta
In addition, there is a notation that allows us to say that two functions grow at the
same rate, up to constant factors. We say that f(n) is Θ(g(n)), pronounced “ f(n)
is big-Theta of g(n),

3nlog n+4n+5logn is Θ(nlog n).
Justification: 3nlogn ≤ 3nlog n+4n+5logn ≤ (3+4+5)nlogn for n ≥ 2


Exponential Running Times
There is a famous story about the inventor of the game of chess. He asked only that
his king pay him 1 grain of rice for the first square on the board, 2 grains for the
second, 4 grains for the third, 8 for the fourth, and so on. It is an interesting test of
programming skills to write a program to compute exactly the number of grains of
rice the king would have to  pay.
using patterns only in expon not the infinite value
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

t we update the current biggest in an iteration of the loop only if the current
element is bigger than all the elements that precede it. If the sequence is given to
us in random order, the probability that the j
th element is the largest of the first j
elements is 1/ j (assuming uniqueness). Hence, the expected number of times we
update the biggest (including initialization) is Hn = ∑n
j=1 1/ j, which is known as
the nth Harmonic number. It turns out (see Proposition B.16) that Hn is O(logn).
Therefore, the expected number of times the biggest value is updated by find max
on a randomly ordered sequence is O(logn)

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
        A[j] = total / (j+1) #  j is 0 initially record the average after each year
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
"""
Even though the ex￾pression, sum(S[0:j+1]), seems like a single command, it is a function call and
an evaluation of that function takes O(j + 1) time in this context. Technically, the
computation of the slice, S[0:j+1], also uses O(j + 1) time, as it constructs a new
list instance for storage. So the running time of prefix average2 is still dominated
by a series of steps that take time proportional to 1+2+3+···+n, and thus O(n2).
"""
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

"""
In our first two algorithms, the prefix sum is computed anew for each value of j.
That contributed O(j) time for each j, leading to the quadratic behavior. In algo￾rithm prefix average3, we
maintain the current prefix sum dynamically, effectively computing S[0] +S[1] +··· +S[ j] as total + S[j], 
where value total is equal to the sum S[0] + S[1] + ··· + S[ j − 1] computed by the previous pass of the loop over j
"""

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
The test a == b is evaluated O(n2) times.the rest of the time spent depends upon how many matching (a,b) pairs
exist. As we have noted, there are at most n such pairs, and so the management of the loop over C, and the commands
within the body of that loop, use at most O(n2) time.By our standard application of Proposition 3.9, the total 
time spent is O(n2).innermost loop, over C, executes at most n times.
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
those pairs refer to elements that are equivalent to each other. It does this using two nested for loops, such that
the first iteration of the outer loop causes n−1 iterations of the inner loop, the second iteration of the outer 
loop causes n − 2 iterations of the inner loop, and so on. Thus, the worst-case running time of this function is
proportional to  (n−1)+(n−2) +···+2+1,
which we recognize as the familiar O(n^2) summation from Proposition 3.3

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
tool(The built-in function, sorted). In this case, by sorting the sequence of elements,we are guaranteed that any duplicate elements will be 
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

"""
d. Logically, these two statements are the same, but the latter, which is called the contrapositive of the first,
may be easier to think about.
Example 3.18: Let a and b be integers. If ab is even, then a is even or b is even.
Justification: To justify this claim, consider the contrapositive, “If a is odd and
b is odd, then ab is odd.” So, suppose a = 2 j+1 and b = 2k+1, for some integers
j and k. Then ab = 4 jk+2 j +2k+1 = 2(2 jk+ j +k) +1; hence, ab is odd.

an application of DeMorgan’s Law. This law helps us deal with negations, for it states that the negation of
a statement of the form “p or q” is“ not p and not q.” Likewise, it states that the negation of a statement 
of the form “p and q” is “not p or not q.”

Contradiction
Another negative justification technique is justification by contradiction, which also often involves 
using DeMorgan’s Law. In applying the justification by con￾tradiction technique, we establish that a 
statement q is true by first supposing that q is false and then showing that this assumption leads to a
contradiction (such as 2 != 2 or 1 > 3)
By reaching such a contradiction, we show that no consistent sit￾uation exists with q being false, so q must be true

Let ab be odd. We wish to show that a is odd and b is odd. So,with the hope of leading to a contradiction, let us
assume the opposite, namely,suppose a is even or b is even. In fact, without loss of generality, we can assume
that a is even (since the case for b is symmetric). Then a = 2 j for some integerj. Hence, ab = (2 j)b = 2(jb),
that is, ab is even. But this is a contradiction: ab cannot simultaneously be odd and even. 
Therefore, a is odd and b is odd
"""
"""
t F(1) = 1, F(2) = 2, and F(n) = F(n − 2) + F(n − 1) for n > 2. (See Sec￾tion 1.8.) We claim that F(n) < 2**n.
We will show our claim is correct by induction.
Base cases: (n ≤ 2). F(1) = 1 < 2 = 21 and F(2) = 2 < 4 = 22.
Induction step: (n > 2). Suppose our claim is true for all n < n. Consider F(n).
Since n > 2, F(n) = F(n−2)+F(n−1). Moreover, since both n−2 and n−1 are
less than n, we can apply the inductive assumption (sometimes called the “inductive
hypothesis”) to imply that F(n) < 2n−2 +2n−1, since
2n−2 +2n−1 < 2**n−1 +2**n−1 = 2 · 2**(n−1) = 2n.

n+ (n−1)n/2 = (2n+n**2 −n)/2 = (n**2 +n)/2 = n(n+1)/2 .
"""
def find(S, val):#"""Return index j such that S[j] == val, or -1 if no such element"""
    n = len(S)
    j=0
    while j < n:
        if S[j] == val:
            return j # a match was found at index j
        j += 1
    return -1

def evensum(S):#Return the sum of the elements with even index in sequence S
    n = len(S)
    tot=0
    for j in range(0,n,2):
        tot += S[j]

    return tot

"""
A prefix sum of a sequence (array) is a new sequence where each element is the sum of all preceding elements in the original sequence, including the element at the current index. Essentially, it's a cumulative sum.
How it works:
1. Initialization:
The first element of the prefix sum array is the same as the first element of the original array.
2. Iteration:
For each subsequent element in the original array, the prefix sum is calculated by adding the current element to the previous prefix sum. 
"""


# Function to find the prefix sum array
def findPrefixSum(arr):
    n = len(arr)

    # to store the prefix sum
    prefixSum = [0] * n

    # initialize the first element
    prefixSum[0] = arr[0]

    # Adding present element with previous element
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    return prefixSum


if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    prefixSum = findPrefixSum(arr)
    for i in prefixSum:
        print(i, end=" ")

def prifixsum(S1):#Return the sum of the prifix sums of sequence S
    n = len(S1)
    tot=0
    for j in range(n):
        for k in range(1+j):
            tot += S1[k]

    return tot
s1 = [10, 20, 10, 5, 15]
print(prifixsum(s1))


def prifixsum2(S2):#Return the sum of the prifix sums of sequence S
    n = len(S2)
    tot = 0
    pref = 0
    for j in range(n):
        pref += S2[j]
        tot += pref

    return tot
s1 = [10, 20, 10, 5, 15]
print(prifixsum2(s1))

def check(A,B):#Return the number of elements in B equal to the sum of prefix sums in A.a and b same length
    n = len(A)

    ct = 0
    for i in range(n):
        tot = 0
        for j in range(n):
            for k in range(1 + j):
                tot += A[k]
            print(B[i], tot)
            if B[i] == tot:
                ct += 1
    return ct
s1 = [10, 20, 10, 5, 15]
s2 = [10, 30, 10, 45, 15]
print(check(s1,s2))

def check2(A1,B1):#Return the number of elements in B equal to the sum of prefix sums in A.a and b same length
    n = len(A1)
    ct = 0
    for i in range(n):
        tot = 0
        for k in range(1 + i):
            tot += A1[k]
        print(B1[i], tot)
        if B1[i] == tot:
            ct += 1
    return ct
s1 = [10, 20, 10, 5, 15]
s2 = [10, 30, 10, 45, 15]
print(check2(s1,s2))





