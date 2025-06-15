
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n=8 # 8 will ask 7 & 6,7will ask 6 & 5,6 will ask 5 & 4,3 will ask 2&1 once these are found 3 will be found and stored in mem, 2 will ask 1 & 0 which will give 1(0+1) as answer
print(fib(n))

# now dynamic

def fib(n,dp):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1: # if already calculated ,get from here
        print("------------------------------------------------[")
        print(f"memo of fib{n} is acessed from dp as {dp[n]}")
        return dp[n]
    else: # n not calculated so calculate
        dp[n] = fib(n-1,dp) + fib(n-2,dp) # save in dp
        print(dp)
        print(dp[n])
        print(f"for fib{n}")
        print("-------------------------------------------------]")
        return dp[n]
"""
dp =[-1,-1,-1,-1,-1,-1,-1,-1]
n = 7
[-1, -1, 1, -1, -1, -1, -1, -1]
1
for fib2
-------------------------------------------------]
[-1, -1, 1, 2, -1, -1, -1, -1]
2
for fib3
-------------------------------------------------]
------------------------------------------------[
memo of fib2 is acessed from dp as 1
[-1, -1, 1, 2, 3, -1, -1, -1]
3
for fib4
-------------------------------------------------]
------------------------------------------------[
memo of fib3 is acessed from dp as 2
[-1, -1, 1, 2, 3, 5, -1, -1]
5
for fib5
-------------------------------------------------]
------------------------------------------------[
memo of fib4 is acessed from dp as 3
[-1, -1, 1, 2, 3, 5, 8, -1]
8
for fib6
-------------------------------------------------]
------------------------------------------------[
memo of fib5 is acessed from dp as 5
[-1, -1, 1, 2, 3, 5, 8, 13]
13
for fib7
-------------------------------------------------]
13
[-1, -1, 1, -1, -1, -1, -1, -1]
[-1, -1, 1, 2, -1, -1, -1, -1]
memo
[-1, -1, 1, 2, 3, -1, -1, -1]
memo
[-1, -1, 1, 2, 3, 5, -1, -1]
memo
[-1, -1, 1, 2, 3, 5, 8, -1]
memo
[-1, -1, 1, 2, 3, 5, 8, 13]
13
only fib 2  and 3 calculated rest all came from memory from recursive setting done it auto sends to mem

from dp2 it is stored,dp1 and dp0 remain -1
"""
n=7
dp =[-1]*(n+1)  # top-down memoization(rec),botup-tabulation(iterative)
print(fib(n,dp))

#tabulation method



def fib(n,dp):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1: # if already calculated ,get from here
        print("memo")
        return dp[n]
    else: # n not calculated so calculate
        dp[n] = fib(n-1,dp) + fib(n-2,dp) # save in dp
        print(dp)
        return dp[n]
n=7
dp =[9]*(n+1)  # top-down memoization(rec),botup-tabulation(iterative)
dp[0] = 0
dp[1] = 1
for i in range(2,10):
    dp[1] = dp[i-1] + dp[i-2] # calculating from prev values
print(dp[n])









