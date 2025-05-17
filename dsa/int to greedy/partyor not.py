
def party(n,c,r,a):
    a.sort()
    sum1 = 0
    for i in range(c):
        sum1 += a[i]
    if sum1 <= r:
        return "party"
    else:
        return "Sad"

n,c,r = map(int,input().split(" "))
a = list(map(int,input().split(" ")))
res = party(n, c, r, a)
print(res)




