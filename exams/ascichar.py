a=""
b=""
N = 26
ty = [i for i in range(30,30+N)]
st = list("".join(map(str,ty)))
# t = str(st)
t = str(ty)
print(t)
# print(st[1])
print(type(t[1]))
# print(type(st[1]))

yu = [chr(j) for j in range(97,97+N)]
y = list("".join(map(str,yu)))
print(y)
print(type(yu[1]))
for i in range(len(ty)):
    a += st[i]
    b += y[i]

print(a)
print(b)
for i in range(len(ty)):
    m = "=".join(a[i],b[i])