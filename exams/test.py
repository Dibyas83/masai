
a = [1,2,3,4,5,6,7,8]
t = int(input())
n = int(input())
arr = [int(input()) for j in range(n)]
l = len(arr)
for te in range(t):
    max1 = 0
    for i in range(n):
        if arr[i] > max1:
            max1 = arr[i]
    max2 = 0
    for j in range(n):
        if arr[j] > max2 and arr[j] != max1:
            max2 = arr[j]
    print(max2)



def nd_best(t,n):
    t = int(input())
    n = int(input())
    arr = [j for j in range(n)]
    l = len(arr)
    for te in range(t):
        max1 = 0
        for i in range(n):
            if arr[i] > max1:
                max1 = arr[i]
        max2 = 0
        for j in range(n):
            if arr[j] > max2 and arr[j] != max1:
                max2 = arr[j]
        print(max2)






