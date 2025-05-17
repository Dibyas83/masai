

def sumof(noof,n):
    if n == noof: # matched
        return True
    if n < noof:
        return False # overshot
    return sumof(noof * 10, n) or sumof(noof * 20, n)

t = int(input())
for _ in range(t):
    n = int(input())
    res = sumof(1,n)   # then noof becomes 10 then 100
    if res:
        print("Yes")
    else:
        print("No")






