
t = int(input())
for _ in range(t):
    n = int(input())
    inc = int(input())
    dec = int(input())
    a,b = [], []
    for i in range(n):
        p, q = map(int,input().split(" "))
        a.append(p)
        b.append(q)
    a.sort()
    b.sort()
    cost = 0
    for i in range(n):
        if a[i] < b[i]:
            cost += (b[i] - a[i]) * inc
        else:
            cost += (a[i] - b[i]) * dec
    print(cost)


"""
1
3
6
4
3 1
1 2
1 2
"""







