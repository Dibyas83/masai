
def sum(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + sum(n-1) # recursive call ,when it becomes n + n-1 +n-2 ....n-n it calculates

n= 5
print(sum(n))









