y = "afdfsdsfg"
print(y[-3:])
numss = [1,2,3,5,6,11]
from functools import reduce
product = reduce(lambda n,m: n*m , numss) # rolling computatio x*y over all elements by selecting pairs
product1 = reduce(lambda n,m: n**m , numss)
print(product)
print(product1)
squares = list(map(lambda w:w**2,numss)) # maping xsq to numss
print(squares)
even_no = list(filter(lambda e : e % 3 == 0,numss))
even3 = list(filter(lambda e : e < 4 ,numss))
print(even_no)
print(even3)
print("--------------------1")

num = [5,6,7,8,9,3,3]
square = list(map(lambda x: x**2,num))
print(square)
filt = list(filter(lambda y:y%2==0,num))
filt1 = list(map(lambda y:y%2==0,num))
filt2 = list(filter(lambda y:y<7,num))
print(filt)
print(filt1)
print(filt2)

from functools import reduce
product = reduce(lambda x,y:x*y,num) # (5*6)*7)*8....
product2 = reduce(lambda x,y:x+y,num) # (5+6)+7)+8....
product3 = reduce(lambda x,y:x**y,[2,3,4]) # (5+6)+7)+8....
print(product)
print(product2)
print(product3)
# op = list(map(lambda o: o%2 == 0,[1,2,3,4],[6,7,8,9]))
# op = list(map(lambda o: o%2 == 0,[[1,2,3,4],[6,7,8,9]]))
# op2 = list(map(lamda o:o + 4,list(map(lambda o: o%2 == 0,[1,2,3,4])),[6,7,8,9])))
op = list(map(lambda o: o*2,list(map(lambda o: o*2,[1,2,3,4]))))
print(op)
print("----------------------------=====================")

#O(1) - constant time
#O(n) - linear time
#O(n**2) = quadratic time
# O(log n ) loarithmic time
# O(n^2) quadratic space memory grows faster as data increases
# const time


def first_item(item):  # O(1) time always picks first even if 1000
    return item[0]


# linear ex
def find_item(items,target):  # O(n)searches all
    for item in items:
        if item == target:
            return True
    return False

# quadratic ex O(n^2) compare one item in list1 with all in list2
def check_all_pairs(items):  # 3 colors of 20 things mixed in list
    for i in range(len(items)): # for every pair of color of
        for j in range(len(items)):
            if items[i] == items[j] and i != j: # i& j are colors
                print("matching pair found!")

# log ex-O(log n)

# nuss1 = [1, 2, 3, 5, 6, 11,15,22,26,34,46,54, 55,58,77,80,90, 100]
nuss1 = [1, 2, 3, 5, 55, 58, 77, 80, 90, 100]
target = 2
low, high = nuss1[0], nuss1[-1]
mid = len(nuss1) // 2
ind = mid
while True:
    print(mid)
    if nuss1[0] == target:
        print(0)
    if nuss1[-1] == target:
        print(-1)

    if nuss1[mid] == target:
        print(ind)
        break
    if nuss1[mid] < target:
        nuss1 = nuss1[(mid+1)::1]
        mid = len(nuss1) // 2
        print(mid)
        ind += mid
    elif nuss1[mid] > target:
        nuss1 = nuss1[0:(mid):1]  # 0,1,2,3,4    0,1
        mid = len(nuss1) // 2
        print(mid)
        ind -= mid  # 5-2 = 3  3-1=2

    else:
        print(-1)
        break

print("-----------------------guess")

def tricky_sum(n):
    co = 0
    for i in range(n):
        for j in range(i):
            co += 1
    return co

print(tricky_sum(5))
def f(c):
    return c**2


t = f(5)
print(t)


g = lambda v: v**2
print(g(4))

# O(n^2) size of the element inc


def create_table(n):
    table = [[0]*i for i in range(n)]
    return table


def create_table2(n):
    table = [list(range(i)) for i in range(n)]
    return table

print(create_table2(5))
print("---------------56")








from functools import reduce

nums = [1,2,3,5]

square = list(map(lambda x:x**2,[1,2,3,5]))
even = list(filter(lambda x:x%2 == 0,nums))
ev3 = list(filter(lambda x:x < 3,nums))
print("=============================================1")
ev5 = reduce(lambda x, y : x * y ,nums)
print(ev5)
print(square)
print(even)
print(nums[-3:])
def cac(item, target):
    for item in item:
        if item == target:
            return True
        return False

#def check(items):
    #for i in range(len(items)):
       # for j in range(len(items)):

            #if items[i] == items[j] and i != j:
        #print("found")


def store(n):
    num = []
    for i in range(n):
        num.append(i)
    return num


def f(x):
    return x**2




