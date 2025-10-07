

def ispossible(n,m,arr,mid):
    sm = 0
    for i in range(n):
        if arr[i] > mid:
            sm +=  arr[i] - mid  # how many items machine i  can produce in mid time  5//1= 5, 5//2= 2.5
    return sm >= m

def totalwood(arr,m,n):
    low = min(arr)
    high = max(arr)
    while low <= high:
        mid = low + ((high-low)) // 2 # for opposite calculations
        if ispossible(n,m,arr,mid): # sm >= m, more is produced
            low = mid + 1  # to dec wood inc mid height req.gradually low reaches high
        else:
            high = mid - 1  # to inc wood down height of mid
    return low - 1

def inp():
    n,m = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    print(totalwood(arr, m, n))


inp()
"""
7 12
1 3 5 8 11 14 16
"""







