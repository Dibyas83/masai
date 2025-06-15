
"""
a= 10
for i in range(10):
    if a%5 == 0:
        a = a+5
    else:
        a+=1
    print(a)

a= 10
for i in range(10):
    if i%2 == 0:
        i+=2
    else:
        i+=1
    print(i)


withdraw = int(input())
bal = int(input())
while bal > 10000:
    bal = bal - withdraw
    if bal < 10000:
        withdraw = 0
    print(bal)

st1 = input()
rotstr = input()
for i in range(len(st1)):
    st1 = st1[-1] + st1[0:-1]
    if st1 == rotstr:
        print("palindrome")


def fib(n):
    if n == 0:
        return
    if n == 1 or  n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


k=4
for i in range(k):
    n = int(input())
    print(fib(n))

#def sort(a,st,end,pivot):

n = int(input())
str12 = input()
v = "aeiou"
ct = 0
for i in range(0,n-1):
    if i == n-2:
        if str12[i] and str12[i+1] in v:
            ct = ct
    if i != n-2 and str12[i] in v:
        if str12[i+1] in v and str12[i+2] not in v:
            ct+=1
print(ct)

#--------------
arr = [1,-2,4,5,-3,2,-4]
n = int(input())
max= 0
curr = n
for i in range(len(arr)):
    #curr = n
    curr += arr[i]
    print(curr)
    print(max,i-1,"i")
    if curr >= max: max = curr
    print(max,"f")
"""























