

list1 = [1,2,3,4,2,5,6]
set1 = set(list1)
list2 = [1,5,2,9,7,5,6]
set2 = set(list2)
print(set1 ^ set2)
print(set1 - set2)
print(set2 - set1)
print(set1.intersection(set2))
print(len(set1.intersection(set2)))
"""
T = int(input())
N = int(input())
arrA = list(input().split(" "))
arrB = list(input().split(" "))
arrB.reverse()
print(arrA)
print(arrB)

set1 = set(arrA)
set2 = set(arrB)
print(len(set1.intersection(set2)))
"""
def intersec():
    T = int(input())
    for _ in range(T):
        N = int(input())
        ct = 0
        arrA = list(input().split(" "))
        arrB = list(input().split(" "))
        arrB.reverse()
        for i in arrA:
            if i in arrB:
                ct += 1
                arrB.remove(i)
        print(ct)

intersec()


def intersec():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arrA = list(input().split(" "))
        arrB = list(input().split(" "))
        arrB.reverse()
        set1 = set(arrA)
        set2 = set(arrB)
        print(len(set1.intersection(set2)))


intersec()



































