
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)  + fib(n-3) # until n-9 = 1 and n-n = 0  becomes

n = int(input())
for i in range(1,n+1):
    print(fib(i),end=" ")









