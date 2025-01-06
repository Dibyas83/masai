from functools import reduce

x = [1, 2, 3]
y = x[:]
y.append(4)
print(x, y)


x = 10
y = 20
x, y = y, x + y
print(x, y)

def func(nums=[]):
    nums.append(len(nums))
    return nums

print(func())
print(func())


x = 5
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()

print(outer())


s = "Python"
print(s[::-2])

x = [1, 2, 3]
y = (x, )
x.append(4)
print(y)

from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d)

x = {1, 2, 3}
y = {3, 4, 5}
print(x & y, x | y, x - y)

class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.x += 1

obj = B()
print(obj.x)


def sor_ted(arr):
    n = len(arr)
    flag = False
    for i in range(1,n):
        if arr[i-1] <= arr[i]:
            flag = True
        else:
            flag = False
            break

    if flag == True:
        print("Yes")
    else:
        print("No")


t = [5,4,3,2,1]
sor_ted(t)




print("-------------------------15")
t= 2
N = 5

arr= list(map(int,input().strip().split(" ")))
new_arr = []
min1 = 0
for i in range(N):
    if arr[i] < min1:
        min1 = arr[i]
for st in arr:
    if st != min1:
        new_arr.append(st)
    else:
        new_arr.append("-1")
print(new_arr)






