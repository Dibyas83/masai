
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2) # until n-9 = 1 and n-n = 0  becomes

"""
factorial(4) calls 4 * factorial(3)
factorial(3) calls 3 * factorial(2)
factorial(2) calls 2 * factorial(1)
factorial(1) calls 1 * factorial(0)
factorial(0) returns 1 (base case)
factorial(1) returns 1 * 1 = 1
factorial(2) returns 2 * 1 = 2
factorial(3) returns 3 * 2 = 6
factorial(4) returns 4 * 6 = 24

Recursive algorithms can be elegant and concise for solvingcertain types of problems,
but they can also be less efficient than iterative solutions due to the overhead of function calls.
It's important to consider the trade-offs between recursion and iteration when choosing an algorithm
"""

n = int(input())
for i in range(1,n+1):
    print(fib(i),end=" ")

#---------------
"""
We have also implemented the algorithm to demonstrate that it works, and in doing so we have unintentionally 
used a well established technique within Dynamic Programming called tabulation, where the solution is found 
by solving subproblems bottom-up, using some kind of table
Since the most basic subproblem solutions are stored in the table first, when solving a subproblem later that 
relies on previous subproblems, the algorithm can just pick these solutions right from the table, no need to 
compute them again.
"""
# dynamic prog
def nth_fibo(n):
    if n==0: return 0
    if n==1: return 1

    F = [None] * (n + 1)

    F[0] = 0
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
        print(F[i])

    return F[n]

n = 6
result = nth_fibo(n)
print(f"The {n}th Fibonacci number is {result}")

"""
Another technique used in Dynamic Programming is called memoization. In this case, using memoization 
essentially solves the problem recursively with brute force where the solution is found recursively,
but stores the subproblem solutions for later as the algorithm runs to avoid doing the same calculations
 more than once.it checks first to see if that solution has already been computed
 The memoization technique is called "top-down" because the initial function call is for the main problem, 
 and it results in new function calls for solving smaller and smaller subproblems.
"""
#using memorizin top down
def Fmemo(n):
    if memo[n] != None: # Already computed
        return memo[n]
    else: # Computation needed
        print('Computing Fmemo('+str(n)+')')
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = Fmemo(n - 1) + Fmemo(n - 2) # feb3 = feb2 + feb1=1+1=2,feb6 = feb5 + feb4
        return memo[n]  # goes to top no need to recompute memo[6] = fmemo5 + fmemo4 is store.fmemo5 becomes f34 + f3
#    and f4 becomes f3 + f2

n = int(input())
memo = [None] * (n + 1)
print('F(6) = ',Fmemo(n))
print('memo = ',memo)


