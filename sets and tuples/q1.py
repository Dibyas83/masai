"""


arr = list(map(int,input().strip().split(" ")))
def unique(arr):
    arr2 = set(arr)
    arr3 = list(arr2)
    print(arr3)


arr1 = list(map(int,input().strip().split()))
unique(arr1)
"""

def unique_ele(lis):

    uniq = []
    for num in lis:

        if lis.count(num) == 1:

            uniq.append(num)


    print(uniq)


y = [3,4,5,6,2,7,3]
unique_ele(y)








