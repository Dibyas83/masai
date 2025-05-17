
"""


def permutation(n,k):
    k =[3,2,1]
    l =len(k)
    ct = 0

    for i in range(l):
        times = n // k[i]
        if (n % k[i]) in k:
            ct += 1
    return k[i]*(times-1) + k

n = 48
k = [6,7,8]
print(permutation(n,k))
"""
def cut(p,n):  # price, n length
    if n == 0:
        return 0
    q = -1
    for i in range(1,n):
        q = max(q,p[i] + cut(p,n-i))
    return q

p = [1,2,3,4,5,6,7,8]
n=6
print(cut(p, n))

