
#bubble short
def sortedindex(arr):
    n = len(arr)
    arr1 = list(range(n)) # indexes of arr

    print(arr1)
    print(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1] = arr[j+1] , arr[j]
                arr1[j] , arr1[j + 1] = arr1[j+1] , arr1[j]
    u= " ".join(map(str,arr1))
    u2= " ".join(map(str,arr))
    print(u2)
    return u

n= int(input())
arr = list(map(int,input().split(" ")))
t=int(input())
while t > 0:
    print(sortedindex(arr))
    t-= 1


"""

7 
4 2 5 6 1 8 4
"""












