

def solve(n):
    if (n==0):
        return
    if n==1 or n==2:
        return 1
    return solve(n-1) + solve(n-2)

n = int(input())
print(solve(n))