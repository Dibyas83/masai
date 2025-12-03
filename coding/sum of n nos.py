def sum(n):
    if n==1:
        return 1

    return n + sum(n-1)

n=6
print(sum(n))


