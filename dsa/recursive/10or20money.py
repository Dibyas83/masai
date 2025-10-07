

def sumof(amt,n):
    if n == amt: # matched
        return True
    if n < amt:
        return False # overshot
    return sumof(amt * 10, n) or sumof(amt * 20, n)

t = int(input())
for _ in range(t):
    n = int(input())
    res = sumof(1,n)   # then noof becomes 10 then 100
    if res:
        print("Yes")
    else:
        print("No")



x = [1, 2, 3]
y = [4, 5, 6]

for i, j in zip(x, y):
    if i + j > 6:
        break
    print(i * j)



