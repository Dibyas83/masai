# sum 1 + 1/r + 1/r^2   .. n

def solve(n,r):
    if n < 1:
        return 1
    return  1/r**n + solve(n-1,r)

n,r = map(int,input().split(" "))
num = solve(n,r)
print("{0:.4f}".format(num))






