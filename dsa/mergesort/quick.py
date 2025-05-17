
n= int(input().strip())
arr1 = list(map(int,input().split(" ")))
def inc_merge(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j],arr[i] # if less arr will remain same i=0,j=0, if high i=-1,j=0 change to next jth places
            print(arr)
    arr[i+1],arr[high] = arr[high],arr[i+1] #  if higher interchange
    return i + 1 # places the pivot in correct position

def quicksrt(arr,low,high): # creating two arrays

    if low < high:

        partion = inc_merge(arr,low,high)
        quicksrt(arr,low,partion-1)
        quicksrt(arr,partion+1,high)


quicksrt(arr1,0,n-1)
for i in range(n):
    print(arr1[i],end=" ")








