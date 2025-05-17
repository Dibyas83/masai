from new.ex4 import name1

n= int(input().strip())
arr1 = list(map(int,input().split(" ")))
def dec_merge(arr,left,mid,right):
    n1 = mid -left + 1
    n2 =right-mid
    l= [0]* n1
    r = [0] * n2

    for i in range(n1):
        l[i] = arr[left + i]
    for j in range(n2):
        r[j] = arr[mid + j + 1]
    print(l,"l")
    print(r,"r")

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2: # merge in descending order
        if l[i] >= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
        print(arr,"progress")

    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1
    print(arr,"remaining")

def mergesrt(arr,left,right):

    if left < right:

        mid = (left + right) // 2
        mergesrt(arr,left,mid)

        mergesrt(arr,mid+1,right)

        dec_merge(arr,left,mid,right)

mergesrt(arr1,0,n-1)
for i in range(n):
    print(arr1[i],end=" ")





