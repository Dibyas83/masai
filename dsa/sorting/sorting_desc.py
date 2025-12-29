# using shrinking window and rec

def qsort(arr,low,high):
    if high <= low:
        return

    start = low # original is not changed
    end = high
    mid = (start + (end -start)) // 2
    pivot = arr[mid]

    while start <= end:
        while arr[start] >= pivot:
            start += 1 # go to next
        while arr[end] < pivot:
            end -= 1
        if start <= end: # window completely not shrinken
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
    print(low, end)


    qsort(arr,low, end)
    qsort(arr,start,high)
    #print(start, high)


n= int(input())
arr = list(map(int,input().split(" ")))
qsort(arr,0,high=len(arr)-1)
print(" ".join(map(str, arr)))


"""

7 
4 2 5 6 1 8 4
"""









