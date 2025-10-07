
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

print(fact(4))

def fa(n):
    if n==1:
        return 1
    else:
        return n *fa(n-1)

print(fa(4))


