
def solvesum(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    return n + solvesum(n-1)


print(solvesum(5))



