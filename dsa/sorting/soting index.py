

def sortedindex(arr):
    n = len(arr)
    arr1 = list(range(n))
    print(arr1)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1] = arr[j+1] , arr[j]
                arr1[j] , arr1[j + 1] = arr1[j+1] , arr1[j]
    print(" ".join(map(str,arr1)))
    #return arr1

n= int(input())
arr = list(map(int,input().split(" ")))
t=int(input())
while t > 0:
    print(sortedindex(arr))
    t-= 1















