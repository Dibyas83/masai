# combination of steps(1,2 or 3) taken to reach end(4 steps)
n= int(input()) #steps
def ways(n):
    if n<0:
        return 0
    if n == 0:
        return  1
    return  ways(n-1) + ways(n-2) + ways(n-3) # forms stack
ans = ways(n)
print(ans)

















